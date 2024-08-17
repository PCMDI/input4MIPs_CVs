"""
Tooling for analysing changes in the database
"""

from __future__ import annotations

import json
import urllib.request
from itertools import chain
from pathlib import Path
from typing import Union

import pandas as pd
import pandas_diff as pd_diff

URL_DB_JSON_MAIN = "https://raw.githubusercontent.com/PCMDI/input4MIPs_CVs/main/Database/input4MIPs_db_file_entries.json"
"""URL which points to the database's state in main"""


def format_db_entry_for_comment(entry: dict[str, str]) -> str:
    """
    Format a database entry for a comment on GitHub

    Parameters
    ----------
    entry
        Entry to format

    Returns
    -------
    :
        Formatted entry, ready to be used in a GitHub comment
    """
    components = [
        "Entry: ",
        "",
        "```json",
        json.dumps(entry, indent=4, sort_keys=True),
        "```",
        "",
    ]
    return "\n".join(components)


def diff_db_to_changes_comment(
    db_main: pd.DataFrame,
    db_source: pd.DataFrame,
    commit_id: Union[str, None] = None,
    max_characters: int = 65536,
) -> str:
    """
    Get the difference between the database states, returning a GitHub compatible comment

    Parameters
    ----------
    db_main
        State of the database in main

    db_source
        State of the database in the repository as it is currently checked out

    commit_id
        The commit ID from which `db_source` was generated.

        If supplied, we use this to create a more informative message.
        Otherwise, we just use a generic message.

    max_characters
        The maximum of characters that can be included in a comment.

        If our first iteration is too big,
        we then go to various summaries.

    Returns
    -------
    :
        Comment which can be posted to GitHub (by hand or as part of an action)
    """
    # Should probably decouple the diff keys from the comment generation.
    # I can't think through that right now, so here we are.
    diff_keys = ["source_id", "tracking_id"]
    diffs_raw = pd_diff.get_diffs(before=db_main, after=db_source, keys=diff_keys)

    if diffs_raw.empty:
        if commit_id:
            return f"No changes to the database between 'main' branch and {commit_id}"

        return "No changes to the database"

    keys_col = ",".join(diff_keys)
    diffs = diffs_raw.drop("object_keys", axis="columns").rename(
        {"object_values": keys_col}, axis="columns"
    )

    diffs_incl_source_id = diffs.copy()
    diffs_incl_source_id["source_id"] = diffs_incl_source_id[keys_col].apply(
        lambda x: x.split(",")[0]
    )

    summary_table = (
        diffs_incl_source_id[
            [
                "source_id",
                "operation",
                "attribute_changed",
                "old_value",
                "new_value",
            ]
        ]
        .fillna("None")
        .value_counts(dropna=False)
        .sort_values(ascending=False)
        .to_frame()
    )
    # Summary table
    comment_summary_table_l = []
    if commit_id:
        comment_summary_table_l.append(
            f"Changes to the database between commit {commit_id} and the 'main' branch"
        )

    else:
        comment_summary_table_l.append("Changes to the database")

    comment_summary_table_l.append("")
    comment_summary_table_l.append("<details>")
    comment_summary_table_l.append("<summary>Summary table</summary>")
    comment_summary_table_l.append(summary_table.to_html())
    comment_summary_table_l.append("</details>")
    comment_summary_table_l.append("")

    # Overview table
    overview_cols = ["operation", keys_col]
    overview_view = diffs[overview_cols].drop_duplicates()

    comment_overview_l = []

    comment_overview_l.append("")
    comment_overview_l.append("<details>")
    comment_overview_l.append("<summary>Overview</summary>")
    comment_overview_l.append(overview_view.to_html())
    comment_overview_l.append("</details>")
    comment_overview_l.append("")

    # Overview by source ID
    comment_by_source_id_l = []

    overview_view_incl_source_id = overview_view.copy()
    overview_view_incl_source_id["source_id"] = overview_view_incl_source_id[
        keys_col
    ].apply(lambda x: x.split(",")[0])

    comment_by_source_id_l.append("<details>")
    comment_by_source_id_l.append("<summary>Overview, split by source ID</summary>")
    for source_id, sidf in overview_view_incl_source_id.groupby("source_id"):
        source_id, _ = sidf[keys_col].iloc[0].split(",")
        comment_by_source_id_l.append("<details>")
        comment_by_source_id_l.append(f"<summary>Source ID: {source_id}</summary>")
        comment_by_source_id_l.append(sidf.to_html())
        comment_by_source_id_l.append("</details>")

    comment_by_source_id_l.append("</details>")

    # Details of individual operations by source ID
    comment_by_source_id_individual_operations_l = []

    comment_by_source_id_individual_operations_l.append("<details>")
    comment_by_source_id_individual_operations_l.append(
        "<summary>Detailed changes, split by source ID</summary>"
    )
    for source_id, sidf in diffs_incl_source_id.groupby("source_id"):
        comment_by_source_id_individual_operations_l.append("<details>")
        comment_by_source_id_individual_operations_l.append(
            f"<summary>Source ID: {source_id}</summary>"
        )

        ovdf = sidf.drop("source_id", axis="columns")
        for (diff_keys_str, operation), operation_df in ovdf.groupby(
            [keys_col, "operation"]
        ):
            _, tracking_id = diff_keys_str.split(",")

            comment_by_source_id_individual_operations_l.append("<details>")
            if operation == "create":
                if operation_df.shape[0] != 1:
                    # Given grouping, creation should only affect one row
                    raise AssertionError(operation_df)

                comment_by_source_id_individual_operations_l.append(
                    f"<summary>Created entry for tracking ID: {tracking_id}</summary>"
                )
                entry = operation_df["object_json"].iloc[0]
                comment_by_source_id_individual_operations_l.append(
                    format_db_entry_for_comment(entry)
                )

            elif operation == "delete":
                if operation_df.shape[0] != 1:
                    # Given grouping, delete should only affect one row
                    raise AssertionError(operation_df)

                comment_by_source_id_individual_operations_l.append(
                    f"<summary>Deleted entry for tracking ID: {tracking_id}</summary>"
                )
                entry = operation_df["object_json"].iloc[0]
                comment_by_source_id_individual_operations_l.append(
                    format_db_entry_for_comment(entry)
                )

            elif operation == "modify":
                comment_by_source_id_individual_operations_l.append(
                    f"<summary>Modified entry for tracking ID: {tracking_id}</summary>"
                )
                comment_by_source_id_individual_operations_l.append("")
                for operation_id, mod_row in operation_df.iterrows():
                    comment_by_source_id_individual_operations_l.append(
                        f"- Altered {mod_row.attribute_changed!r}"
                    )
                    comment_by_source_id_individual_operations_l.append(
                        f"    - Old value: {mod_row.old_value!r}"
                    )
                    comment_by_source_id_individual_operations_l.append(
                        f"    - New value: {mod_row.new_value!r}"
                    )

                comment_by_source_id_individual_operations_l.append("")

            else:
                raise NotImplementedError(operation)

            comment_by_source_id_individual_operations_l.append("</details>")

        comment_by_source_id_individual_operations_l.append("</details>")

    comment_by_source_id_individual_operations_l.append("</details>")

    all_components = [
        comment_summary_table_l,
        comment_overview_l,
        comment_by_source_id_l,
        comment_by_source_id_individual_operations_l,
    ]
    for i in range(len(all_components)):
        if i < 1:
            components_to_use = all_components

        else:
            components_to_use = all_components[:-i]

        comment = "\n".join(chain.from_iterable(components_to_use))
        if len(comment) <= max_characters:
            break

    else:
        msg = "Comment still too long"
        raise NotImplementedError(msg)

    return comment


def get_pr_db_changes_comment(
    current_db_path: Path, commit_id: Union[str, None]
) -> str:
    """
    Get the changes comment to post to a pull request
    """
    with urllib.request.urlopen(URL_DB_JSON_MAIN) as url:
        db_main = pd.DataFrame(json.load(url))

    with open(current_db_path) as fh:
        db_source = pd.DataFrame(json.load(fh))

    return diff_db_to_changes_comment(
        db_main=db_main, db_source=db_source, commit_id=commit_id
    )
