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
from typing import Any, Annotated, Union

import json

import pandas as pd
import pandas_diff as pd_diff
import tqdm

import typer

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

        if esgf_dataset_info["latest"]:
            res.loc[idx, "publication_status"] = "published"

        else:
            # Not sure if this logic is correct, but we can start like this
            # and then interate.
            res.loc[idx, "publication_status"] = "retracted"

    return res


def hack_in_prototype_amip_info(db_df: pd.DataFrame) -> pd.DataFrame:
    """
    Hack in the prototype AMIP info

    This can be removed once this information is actually published
    """
    common = {
        "contact": "zelinka1@llnl.gov; durack1@llnl.gov",
        "further_info_url": "https://pcmdi.llnl.gov/mips/amip",
        "institution_id": "PCMDI",
        "license_id": "CC BY 4.0",
        "mip_era": "CMIP6Plus",
        "source_version": "1.0",
        "target_mip": "Prototype",
        "comment": (
            "Prototype dataset for the evaluation of SST forcing uncertainty "
            "over the satellite era - not for production use in any simulations, "
            "including CMIP7"
        ),
    }

    to_add = {
        "PCMDI-AMIP-ERSST5-1-0": {
            "source": "PCMDI-AMIP ERSST5 1.0: SST based on NOAA ERSST 5.0",
            **common,
        },
        "PCMDI-AMIP-Had1p1-1-0": {
            "source": "PCMDI-AMIP Had-1.1 1.0: SST based on UK MetOffice HadISST 1.1",
            **common,
        },
        "PCMDI-AMIP-OI2p1-1-0": {
            "source": "PCMDI-AMIP OI-2.1 1.0: SST based on NOAA NCEP OI2.1",
            **common,
        },
        # "PCMDI-AMIP-Had2p4-1-0" appears to be missing from
        # https://github.com/PCMDI/input4MIPs_CVs/pull/26
        # hence not included yet
    }
    for source_id, values in to_add.items():
        if source_id in db_df["source_id"]:
            continue

        flat = {k: None for k in db_df.columns}
        flat["source_id"] = source_id
        flat["publication_status"] = "registered"
        flat = flat | values
        row = pd.Series(flat)

        db_df = pd.concat([db_df, row.to_frame().T]).reset_index(drop=True)

    return db_df


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


def other_manual_fixes(db_df: pd.DataFrame) -> pd.DataFrame:
    """
    Other manual fixes to the database
    """
    out = db_df.copy()

    # Abandoned source IDs
    out.loc[out["source_id"] == "CR-CMIP-0-2-0", "publication_status"] = "abandoned"
    out.loc[out["source_id"] == "SOLARIS-HEPPA-CMIP-4-1", "publication_status"] = (
        "never_published"
    )
    out.loc[out["source_id"] == "UOEXETER-CMIP-0-1-0", "never_published"] = (
        "in_publishing_queue"
    )
    out.loc[out["source_id"] == "UOEXETER-CMIP-1-1-2", "publication_status"] = (
        "in_publishing_queue"
    )

    # missing license ID for early CMIP6Plus data
    for srcId in [
        "MRI-JRA55-do-1-6-0",
        "PCMDI-AMIP-1-1-9",
        "SOLARIS-HEPPA-CMIP-4-2",
        "SOLARIS-HEPPA-CMIP-4-3",
    ]:
        out.loc[out["source_id"] == srcId, "license_id"] = "CC BY 4.0"

    # Post-publication comments
    out.loc[
        out["source_id"] == "SOLARIS-HEPPA-CMIP-4-2", "comment_post_publication"
    ] = (
        "An issue was encountered with the proton ionization data in v4.2. "
        "It was hence retracted. "
        "The original comment from the data provider is "
        '<a href="https://github.com/PCMDI/input4MIPs_CVs/issues/17#issuecomment-2255378927">here</a>.'
    )

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

    with open(DB_DIR / "input-data" / "esgf.json") as fh:
        esgf_raw = json.load(fh)

    with open(repo_root_dir / "CVs" / "input4MIPs_source_id.json") as fh:
        source_ids_raw = json.load(fh)

    pmount_df = pd.DataFrame(pmount_raw)

    db_df = merge_pmount_and_esgf_data(pmount_df=pmount_df, esgf_raw=esgf_raw)

    db_df = hack_in_prototype_amip_info(db_df)

    db_df = add_missing_source_ids(db_df=db_df, cvs_source_ids_raw=source_ids_raw)

    db_df = other_manual_fixes(db_df=db_df)

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
