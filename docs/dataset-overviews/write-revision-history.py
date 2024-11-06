"""
Write the revision history sections in our overview files
"""

from __future__ import annotations

import json
import textwrap
from pathlib import Path
# from typing import Callable

import pandas as pd

HERE = Path(__file__).parent

# Could open this up in future to avoid hard-coded name.
# Fine for now.
REPO_ROOT = HERE.parents[1]
CURRENT_DB_PATH = REPO_ROOT / "Database" / "input4MIPs_db_file_entries.json"
CMIP7_PHASES_SOURCE_IDS_CSV = HERE / "cmip7_phases_source_ids.csv"

with open(CURRENT_DB_PATH) as fh:
    db_source = pd.DataFrame(json.load(fh))

cmip7_phases_source_ids = pd.read_csv(CMIP7_PHASES_SOURCE_IDS_CSV)


def get_cmip7_phase_source_id_summary(cmip7_phase: str) -> tuple[str, ...]:
    """
    Get the summary of source IDs to use for a given phase of CMIP7

    Parameters
    ----------
    cmip7_phase
        CMIP7 phase for which to create the source ID summary

    Returns
    -------
    :
        Summary of source IDs to use for the CMIP7 phase

        If the output is empty, no source IDs are available for this phase of CMIP7 yet.
    """
    phase_source_ids = cmip7_phases_source_ids[
        cmip7_phases_source_ids["cmip7_phase"] == cmip7_phase
    ]
    if phase_source_ids.empty or phase_source_ids["source_id"].isnull().all():
        # No valid source IDs
        return []

    out = []
    for _, row in phase_source_ids.sort_values("forcing_int_id").iterrows():
        if pd.isnull(row.source_id):
            out.append(f"1. {row.forcing}: No data available for this phase yet")
            continue

        # Check status in the database
        db_source_id_stub_rows = db_source[
            db_source["source_id"].str.contains(row.source_id_stub)
        ]

        # May need a more sophisticated sorting algorithm at some point
        source_ids_sorted = sorted(db_source_id_stub_rows["source_id"].unique())
        source_id_latest = source_ids_sorted[-1]
        if (not row.ok_if_not_latest) and row.source_id != source_id_latest:
            msg = (
                f"For {row.forcing=} and {row.cmip7_phase=}, {row.source_id=}."
                f"This is not the latest available source ID ({source_ids_sorted=}). "
                f"Given that {row.ok_if_not_latest=},"
                f"either update the source ID to the latest ({source_id_latest}) "
                f"or set `ok_if_not_latest` for {row.forcing=} to `True` "
                f"in {CMIP7_PHASES_SOURCE_IDS_CSV}. "
            )
            raise ValueError(msg)

        out.append(
            f"1. {row.forcing}: [{row.source_id}](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%22{row.source_id}%22%7D)"
        )

    return tuple(out)


# Potential generalisation to reduce duplication below
# def insert_content_in_section(
#     key_id_line_prefix: str,
#     line_to_insert_after: str,
#     end_line: str,
#     content_generator: Callable[[str], tuple[str, ...]],
# ) -> tuple[str, ...]:
#     pass


def add_cmip7_phase_source_id_summaries(raw_split: tuple[str, ...]) -> tuple[str, ...]:
    """
    Add the summaries of source IDs to use for each phase of CMIP7

    Parameters
    ----------
    raw_split
        Raw file contents, split into lines

    Returns
    -------
    :
        The updated lines, after the summary for the CMIP7 phases have been inserted
    """
    # Use tuples as input and output to avoid accidentally
    # modifying content between different function calls.
    out = []
    in_source_id_summmary = False
    cmip7_phase = None
    for line in raw_split:
        if line.startswith("<!--- begin-source-id-summary:"):
            in_source_id_summmary = True
            out.append(line)
            # Assumes no spaces in the summary target name
            cmip7_phase = line.split("begin-source-id-summary:")[-1].split(" ")[0]
            continue

        if line.startswith("<!--- end-source-id-summary"):
            in_source_id_summmary = False
            out.append(line)
            continue

        if in_source_id_summmary:
            if line.startswith("<!--- Do not edit this section"):
                out.append(line)

                source_id_summary = get_cmip7_phase_source_id_summary(
                    cmip7_phase=cmip7_phase
                )

                if source_id_summary:
                    out.extend(source_id_summary)

                else:
                    out.append(
                        "No source IDs are available for use in this phase of CMIP7 yet"
                    )

                continue

            else:
                # Ignore existing content
                continue

        else:
            out.append(line)

    return tuple(out)


def get_revision_history_for_source_id_stub(source_id_stub: str) -> tuple[str, ...]:
    """
    Get revision history for a given source ID stub

    A source ID stub is a part of a source ID.
    For example, "CR-CMIP" or "SOLARIS-HEPPA".
    All source IDs that include the stub are included in the revision history.

    Parameters
    ----------
    source_id_stub
        Source ID stub for which to create the revision history

    Returns
    -------
    :
        Revision history for the source ID stub.

        If the output is empty, no revisions have been made.
    """
    source_id_stub_rows = db_source[db_source["source_id"].str.contains(source_id_stub)]
    source_ids_in_history = source_id_stub_rows["source_id"].unique()

    out = []
    for source_id in sorted(source_ids_in_history)[::-1]:
        source_id_rows = source_id_stub_rows[
            source_id_stub_rows["source_id"] == source_id
        ]
        comments_post_publication = [
            c
            for c in source_id_rows["comment_post_publication"].unique()
            if c is not None
        ]
        if not comments_post_publication:
            continue

        if not out:
            out = ["## Revision history", ""]

        out.append(f"### {source_id}")
        out.append("")
        for txt in comments_post_publication:
            out.extend(textwrap.wrap(txt, width=100))
        out.append("")

    return tuple(out)


def add_revision_history(raw_split: tuple[str, ...]) -> tuple[str, ...]:
    """
    Insert the revision history in one of the docs

    Parameters
    ----------
    raw_split
        Raw file contents, split into lines

    Returns
    -------
    :
        The updated lines, after the revision history has been inserted
    """
    # Use tuples as input and output to avoid accidentally
    # modifying content between different function calls.
    out = []
    in_revision_history = False
    source_id_prefix = None
    for line in raw_split:
        if line.startswith("<!--- begin-revision-history:"):
            in_revision_history = True
            out.append(line)
            # Assumes no spaces in the ID of interest
            source_id_prefix = line.split("begin-revision-history:")[-1].split(" ")[0]
            continue

        if line.startswith("<!--- end-revision-history"):
            in_revision_history = False
            out.append(line)
            continue

        if in_revision_history:
            if line.startswith("<!--- Do not edit this section"):
                out.append(line)

                revision_history = get_revision_history_for_source_id_stub(
                    source_id_stub=source_id_prefix
                )

                if revision_history:
                    out.extend(revision_history)

                else:
                    out.append("<!--- No revisions, hence section is blank -->")

                continue

            else:
                # Ignore existing content
                continue

        else:
            out.append(line)

    return tuple(out)


for file in HERE.glob("*.md"):
    with open(file) as fh:
        raw = fh.read()

    out = tuple(raw.splitlines())

    if file.name == "index.md":
        out = add_cmip7_phase_source_id_summaries(out)

    else:
        out = add_revision_history(out)

    with open(file, "w") as fh:
        fh.write("\n".join(out))
        fh.write("\n")
