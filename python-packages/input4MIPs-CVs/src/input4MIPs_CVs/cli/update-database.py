"""
Update our database

This script merges information from:

- a scrape of the ESGF
- parsing the files using input4MIPs validation
- the registered source IDs
- a few other custom overrides contained within the script

TODO: move scripts for all automatable processes into here,
or automate the processes and document where that automation happens.
"""

from __future__ import annotations

import copy
import json
from typing import Annotated, Any, Union

import pandas as pd
import pandas_diff as pd_diff
import tqdm
import typer
import yaml

from input4MIPs_CVs.cli.options import REPO_ROOT_DIR_OPTION


def merge_pmount_and_esgf_data(
    pmount_df: pd.DataFrame, esgf_raw: dict[str, Any]
) -> pd.DataFrame:
    res = pmount_df.copy()

    for idx, row in tqdm.tqdm(
        res.iterrows(), desc="Adding ESGF data to pmount records"
    ):
        if row.esgf_dataset_master_id not in esgf_raw:
            # Data not in ESGF yet
            # Print info and move in
            print(f"{row.esgf_dataset_master_id} is not in our ESGF records yet")

            continue

        esgf_dataset_info = esgf_raw[row.esgf_dataset_master_id]

        # Grab info of interest from the ESGF records
        esgf_field_db_field_map = {
            "_timestamp": "timestamp",
            "data_node": "data_node",
            "latest": "latest",
            "replica": "replica",
            # Have to work out what this field should be before handling
            # "xlink": "xlink",
        }
        for esgf_field, db_field in esgf_field_db_field_map.items():
            res.loc[idx, db_field] = esgf_dataset_info[esgf_field]

        if esgf_dataset_info["retracted"]:
            res.loc[idx, "publication_status"] = "retracted"

        else:
            res.loc[idx, "publication_status"] = "published"

    return res


def add_missing_source_ids(
    db_df: pd.DataFrame,
    cvs_source_ids_raw: dict[str, dict[str, str]],
    missing_ids_publication_status: str = "registered",
) -> pd.DataFrame:
    """
    Add any missing source IDs to the database

    Parameters
    ----------
    db_df
        Database `pd.DataFrame`

    cvs_source_ids_raw
        Source IDs captured in the CVs

    missing_ids_publication_status
        Publication status to assign to any source IDs
        which are not in `db_df`.

    Returns
    -------
    :
        Database with missing source IDs from `cvs_source_ids` added
    """
    db_source_ids = set(db_df["source_id"].unique())
    cvs_source_ids = set(cvs_source_ids_raw.keys())

    missing_from_db_source_ids = cvs_source_ids.difference(db_source_ids)
    missing_from_cvs_source_ids = db_source_ids.difference(cvs_source_ids)

    template = {k: None for k in db_df.columns}
    db_entries_from_missing_source_ids_l = []
    for source_id in missing_from_db_source_ids:
        placeholder_entry = copy.deepcopy(template)

        for k, v in cvs_source_ids_raw[source_id].items():
            if k == "authors":
                # Skip this, shouldn't be in the database.
                # The CVs need to be rethought to handle this better.
                # We're starting to see the limits of not using an actual database.
                continue

            if k == "dataset_category":
                # Skip this, it is managed elsewhere in the database
                # and is only in source ID to help downstream users
                # (although even that is an ongoing discussion,
                # see https://github.com/PCMDI/input4MIPs_CVs/issues/201)
                continue

            placeholder_entry[k] = v

        placeholder_entry["source_id"] = source_id
        placeholder_entry["publication_status"] = missing_ids_publication_status
        placeholder_entry["activity_id"] = "input4MIPs"
        db_entries_from_missing_source_ids_l.append(placeholder_entry)

    db_df = pd.concat(
        [db_df, pd.DataFrame(db_entries_from_missing_source_ids_l)]
    ).reset_index(drop=True)

    missing_json_entries = {}
    for source_id in missing_from_cvs_source_ids:
        source_id_keys = [
            "contact",
            "further_info_url",
            "institution_id",
            "license_id",
            "mip_era",
            "source_version",
        ]
        source_id_row = db_df[db_df["source_id"] == source_id][
            source_id_keys
        ].drop_duplicates()
        if source_id_row.shape[0] != 1:
            msg = "Should only have one row now"
            raise AssertionError(msg)

        source_id_row = source_id_row.iloc[0]

        entry = {k: source_id_row.loc[k] for k in source_id_keys}
        missing_json_entries[source_id] = entry

    if missing_json_entries:
        entry_json = json.dumps(
            missing_json_entries, sort_keys=True, indent=4, separators=(",", ":")
        )
        print(
            f"Source ID {'entry' if len(missing_json_entries.keys()) == 1 else 'entries'} "
            f"missing from CVs:\n{entry_json}"
        )

    return db_df


def add_supplementary_source_id_info(
    db_df: pd.DataFrame, supplementary_source_id_info: dict[str, dict[str, str]]
) -> pd.DataFrame:
    """
    Add supplementary source ID info to the database

    Parameters
    ----------
    db_df
        Input database

    supplementary_source_id_info
        Supplementary info to appy at the source ID level.

    Returns
    -------
    :
        Updated database
    """
    out = db_df.copy()
    for source_id, updates in supplementary_source_id_info.items():
        source_id_loc = out["source_id"] == source_id
        for key, value in updates.items():
            out.loc[source_id_loc, key] = value

    return out


def print_diffs(start: pd.DataFrame, end: pd.DataFrame) -> None:
    """
    Print the difference in our database start before and after the merge
    """
    print("Creating diffs")
    diff_keys = ["source_id", "tracking_id"]
    diffs = pd_diff.get_diffs(start, end, diff_keys)

    for _, row in diffs.iterrows():
        if row["operation"] == "create":
            print(f"Added entry for {diff_keys}: {row['object_values']}")

        elif row["operation"] == "modify":
            print(
                f"For entry {diff_keys}: {row['object_values']}, "
                f"modified {row['attribute_changed']} "
                f"from {row['old_value']} to {row['new_value']}"
            )

        elif row["operation"] == "delete":
            if row.object_json["tracking_id"] is not None:
                raise NotImplementedError(row["operation"])

            print(
                f"Removed entry {diff_keys}: {row['object_values']}, "
                "This had no files associated with it, "
                f"it was just a placeholder for a dataset that had "
                f"publication status: {row.object_json['publication_status']}"
            )

        else:
            raise NotImplementedError(row["operation"])


def main(
    repo_root_dir: REPO_ROOT_DIR_OPTION,
    create_diffs: Annotated[
        bool, typer.Option(help="Show the changes made to the database")
    ] = True,
    check_unchanged: Annotated[
        bool,
        typer.Option(
            help="Should an error be raised if the database will change as a result of running this command?"
        ),
    ] = False,
) -> None:
    """
    Merge the information scraped from ESGF and the files

    Exits with zero if there are no changes to the database.
    Exits with one if there would be changes to the database.
    """
    DB_DIR = repo_root_dir / "Database"

    DB_FILE = DB_DIR / "input4MIPs_db_file_entries.json"
    """Output database file"""

    with open(DB_FILE, "r") as fh:
        db_start_raw = json.load(fh)

    db_start_df = pd.DataFrame(db_start_raw)

    pmount_raw = []
    db_files = list((DB_DIR / "input-data" / "pmount").glob("*.json"))
    for file in tqdm.tqdm(db_files, desc="Loading pmount entries"):
        with open(file) as fh:
            pmount_raw.append(json.load(fh))

    with open(DB_DIR / "input-data" / "esgf-input4MIPs.json") as fh:
        esgf_raw = json.load(fh)

    with open(DB_DIR / "input-data" / "supplementary-source-id-info.yaml") as fh:
        supplementary_source_id_info = yaml.safe_load(fh)

    with open(repo_root_dir / "CVs" / "input4MIPs_source_id.json") as fh:
        source_ids_raw = json.load(fh)

    pmount_df = pd.DataFrame(pmount_raw)

    db_df = merge_pmount_and_esgf_data(pmount_df=pmount_df, esgf_raw=esgf_raw)

    db_df = add_missing_source_ids(db_df=db_df, cvs_source_ids_raw=source_ids_raw)

    db_df = add_supplementary_source_id_info(
        db_df=db_df, supplementary_source_id_info=supplementary_source_id_info
    )

    idx_compare_cols = ["sha256", "source_id"]
    db_unchanged = (
        db_df.set_index(idx_compare_cols)
        .sort_index()
        .equals(db_start_df.set_index(idx_compare_cols).sort_index())
    )

    if db_unchanged:
        print(f"No changes to {DB_FILE}")
        raise typer.Exit(0)

    if check_unchanged:
        print(
            "`--check-unchanged` flag used and database would be changed if we continued"
        )
        raise typer.Exit(1)

    # Otherwise, carry on and update the database

    if create_diffs:
        print_diffs(start=db_start_df, end=db_df)

    def get_sort_key(record: dict[str, Union[str, None]]) -> str:
        """
        Get the key for sorting our entries
        """
        if record["sha256"] is not None:
            return record["sha256"]

        # Not a file, just a registered dataset
        return record["source_id"]

    to_dump = sorted(
        db_df.sort_values("sha256").to_dict(orient="records"), key=get_sort_key
    )
    with open(DB_FILE, "w") as fh:
        json.dump(
            to_dump,
            fh,
            ensure_ascii=True,
            sort_keys=True,
            indent=4,
            separators=(",", ":"),
        )

    print(f"Updated {DB_FILE}")


if __name__ == "__main__":
    typer.run(main)
