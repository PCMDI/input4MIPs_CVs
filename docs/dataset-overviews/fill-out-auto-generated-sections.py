"""
Fill out the auto-generated sections in our overview files

If we need to add any more to this, we should probably refactor first
as it is on the edge of incomprehensible.
"""

from __future__ import annotations

import json
import textwrap
from collections.abc import Iterable
from pathlib import Path

import pandas as pd
from packaging.version import Version

HERE = Path(__file__).parent

# Could open this up in future to avoid hard-coded name.
# Fine for now.
REPO_ROOT = HERE.parents[1]
CURRENT_DB_PATH = REPO_ROOT / "Database" / "input4MIPs_db_file_entries.json"
CMIP7_PHASES_SOURCE_IDS_JSON = (
    REPO_ROOT / "docs" / "dataset-info" / "cmip7-phases-source-ids.json"
)
DATASET_INFO_JSON = REPO_ROOT / "docs" / "dataset-info" / "dataset-info.json"

PHASES_COMMON_TEXT: dict[str, str] = {
    "testing": (
        "This data is for testing (both of the forcing data and of modelling workflows) only.\n"
        "Production simulations should not be started based on any data "
        "that has a `mip_era` value equal to 'CMIP6Plus'.\n"
        "(The `mip_era` metadata value appears both in each file's global attributes "
        "as well as its metadata on ESGF.)\n"
        "\n"
        "If you have any feedback, please add it to the "
        "[relevant GitHub discussion](https://github.com/PCMDI/input4MIPs_CVs/discussions)."
    ),
    "cmip7": (
        "This data is for use in CMIP7 production simulations.\n"
        "All data sets for use in CMIP7 production simulations "
        "are published with a `mip_era` metadata value of 'CMIP7'.\n"
        "This metadata value appears both in the file's global metadata "
        "as well as its metadata on ESGF.\n"
        "\n"
        "If you find an issue, please\n"
        "[create an issue on GitHub](https://github.com/PCMDI/input4MIPs_CVs/issues/new?template=data_issue.md)\n"
        "so that the identification and resolution of this issue is publicly accessible."
    ),
}

with open(CURRENT_DB_PATH) as fh:
    DB_SOURCE = pd.DataFrame(json.load(fh))

with open(CMIP7_PHASES_SOURCE_IDS_JSON) as fh:
    CMIP7_PHASES_SOURCE_IDS = json.load(fh)

with open(DATASET_INFO_JSON) as fh:
    DATASET_INFO = json.load(fh)


def get_esgf_search_url(source_ids: list[str]) -> str:
    """
    Get an ESGF search URL which points to selected source IDs

    Parameters
    ----------
    source_ids
        Source IDs to search for

    Returns
    -------
    :
        URL search
    """
    source_id_search = "%22%2C%22".join(source_ids)
    return (
        "https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&"
        f"activeFacets=%7B%22source_id%22%3A%5B%22{source_id_search}%22%5D%7D"
    )


def sort_source_ids(source_ids: tuple[str, ...], cmip7_phase: str) -> str:
    # breakpoint()
    raise NotImplementedError


def get_cmip7_phase_source_id_summary(
    cmip7_phase: str, source_id_stubs: dict[str, str]
) -> tuple[str, ...]:
    """
    Get the summary of source IDs to use for a given phase of CMIP7

    Parameters
    ----------
    cmip7_phase
        CMIP7 phase for which to create the source ID summary

    source_id_stubs
        Mapping from forcings to the source ID stub to use to check that things are up to date

    Returns
    -------
    :
        Summary of source IDs to use for the CMIP7 phase

        If the output is empty, no source IDs are available for this phase of CMIP7 yet.
    """
    out = [None] * len(DATASET_INFO)
    for forcing_id, info in CMIP7_PHASES_SOURCE_IDS.items():
        idx = DATASET_INFO[forcing_id]["dataset_number"] - 1

        if forcing_id == "simple-plumes":
            # The simple plumes exception
            out[idx] = (
                "1. *Aerosol optical properties/MACv2-SP*: "
                "This is not managed via ESGF. "
                "Please see the "
                "[aerosol optical properties/MACv2-SP specific page](aerosol-optical-properties-macv2-sp) "
                "for details."
            )
            continue

        phase_info = info[cmip7_phase]
        description_html = DATASET_INFO[forcing_id]["description_html"]

        if phase_info is None:
            out[idx] = f"1. *{description_html}:* No data available for this phase yet"
            continue

        source_ids = phase_info["source_ids"]
        # Make sure all source IDs are in the DB
        missing_from_db = [
            sid for sid in source_ids if sid not in DB_SOURCE["source_id"].tolist()
        ]
        if missing_from_db:
            msg = f"These source IDs are not in our database ({CURRENT_DB_PATH}): {missing_from_db}"
            raise ValueError(msg)

        # Check status in the database
        db_source_id_stub_rows = DB_SOURCE[
            DB_SOURCE["source_id"].str.contains(source_id_stubs[forcing_id])
        ]
        if "source_id_stub_ignore" in phase_info:
            # The CEDS clause
            db_source_id_stub_rows = db_source_id_stub_rows[
                ~db_source_id_stub_rows["source_id"].str.contains(
                    phase_info["source_id_stub_ignore"]
                )
            ]

        # May need a more sophisticated sorting algorithm at some point
        if any(v.startswith("PCMDI-AMIP") for v in phase_info["source_ids"]):
            all_source_ids = tuple(db_source_id_stub_rows["source_id"].unique())
            version_ids = tuple(
                v.split("PCMDI-AMIP-")[-1].replace("-", ".") for v in source_ids
            )
            pairs = list(zip(all_source_ids, version_ids))[::-1]
            pairs.sort(key=lambda x: Version(x[1]))
            source_ids_sorted = [v[0] for v in pairs]

        else:
            source_ids_sorted = sorted(db_source_id_stub_rows["source_id"].unique())

        source_ids_sorted = sort_source_ids(
            tuple(db_source_id_stub_rows["source_id"].unique()),
            cmip7_phase=cmip7_phase,
        )

        source_id_latest = source_ids_sorted[-1]

        ok_if_not_latest = (
            "ok_if_not_latest" in phase_info and phase_info["ok_if_not_latest"]
        )
        if not ok_if_not_latest and any(
            v != source_id_latest for v in phase_info["source_ids"]
        ):
            msg = [
                f"For {forcing_id=} and {cmip7_phase=}, {phase_info['source_ids']=}. "
                f"This is not the latest available source ID ({source_ids_sorted=}). "
            ]

            if "ok_if_not_latest" in phase_info:
                msg.extend(
                    [
                        f"Given that {phase_info['ok_if_not_latest']=},"
                        f"either update the source ID to the latest ({source_id_latest}) "
                        f"or set `ok_if_not_latest` to `True` for the info "
                        f"in {CMIP7_PHASES_SOURCE_IDS_JSON}. "
                    ]
                )
            else:
                msg.extend(
                    [
                        f"Either update the source ID to the latest ({source_id_latest}) "
                        f"or set `ok_if_not_latest` to `True` for the info "
                        f"in {CMIP7_PHASES_SOURCE_IDS_JSON}. "
                    ]
                )

            raise ValueError(msg)

        db_source_id = DB_SOURCE[DB_SOURCE["source_id"].isin(source_ids)]
        dois_l = db_source_id["doi"].dropna().unique().tolist()
        if len(dois_l) > 0:
            dois_md = ", ".join((f"[{doi}]({get_doi_link(doi)})" for doi in dois_l))
            if len(dois_l) > 1:
                doi_s = "DOIs"
            else:
                doi_s = "DOI"

            doi_line = f"{doi_s}: {dois_md}."

        else:
            doi_line = "No DOI provided"

        source_id_show = "; ".join(source_ids)
        out[idx] = (
            f"1. *{description_html}:* [{source_id_show}]({get_esgf_search_url(source_ids)}) ({doi_line})"
        )

    if all("No data available" in v for v in out):
        # No valid source IDs
        return []

    return tuple(out)


def add_cmip7_phase_source_id_summaries(
    raw_split: tuple[str, ...], source_id_stubs: dict[str, str]
) -> tuple[str, ...]:
    """
    Add the summaries of source IDs to use for each phase of CMIP7

    Parameters
    ----------
    raw_split
        Raw file contents, split into lines

    source_id_stubs
        Mapping from forcings to the source ID stub to use to check that things are up to date

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

                out.append("")
                out.append(PHASES_COMMON_TEXT[cmip7_phase.split("-")[-1]])
                out.append("")

                out.append("##### Source IDs for use in this phase")
                out.append("")

                source_id_summary = get_cmip7_phase_source_id_summary(
                    cmip7_phase=cmip7_phase, source_id_stubs=source_id_stubs
                )

                if source_id_summary:
                    out.extend(source_id_summary)

                else:
                    out.append(
                        "No source IDs are available for use in this phase of CMIP7 yet."
                    )

                continue

            else:
                # Ignore existing content
                continue

        else:
            out.append(line)

    return tuple(out)


def get_doi_link(doi: str) -> str:
    """
    Get DOI link that can be used in markdown
    """
    if not doi.startswith("https://doi.org/"):
        return f"https://doi.org/{doi}"

    return doi


def get_cmip7_phases_source_id_summary_for_forcing(forcing: str) -> tuple[str, ...]:
    """
    Get the summary of the source IDs to use for each phase of CMIP7 for a given forcing

    Parameters
    ----------
    forcing
        Forcing for which to get the source IDs to use for each CMIP7 phase

    Returns
    -------
    :
        Summary of source IDs to use for the CMIP7 phases for the given forcing
    """
    out = [
        "### Source IDs for CMIP7 phases",
        "",
        "The source ID that identifies the dataset to use in CMIP7 is given below.",
        "",
    ]
    for mip in ("deck", "scenariomip"):
        if mip == "deck":
            mip_display = "DECK"

        elif mip == "scenariomip":
            mip_display = "ScenarioMIP"

        else:
            raise NotImplementedError(mip)

        out.append(f"#### {mip_display}")
        out.append("")

        for step in (
            "cmip7",
            "testing",
        ):
            phase = f"{mip}-{step}"

            info = CMIP7_PHASES_SOURCE_IDS[forcing][phase]

            if step == "testing":
                cmip7_step_pretty_title = "Testing"
                prod_or_testing_phase_str = "testing"

            elif step == "cmip7":
                cmip7_step_pretty_title = "CMIP7"
                prod_or_testing_phase_str = "production"

            else:
                raise NotImplementedError(step)

            out.append(f"##### {cmip7_step_pretty_title}")
            out.append("")

            if info is None:
                out.append("No data available for this phase yet.")
                out.append("")

            else:
                source_ids = info["source_ids"]

                if len(source_ids) == 1:
                    source_id = source_ids[0]
                    out.append(
                        f"For the {mip_display} simulations in the {prod_or_testing_phase_str} phase of CMIP7, "
                        "use data with the source ID "
                        f"[{source_id}]({get_esgf_search_url(source_ids)})"
                    )

                else:
                    # Multiple source IDs
                    source_id_sep = "\n- "
                    source_id_str = source_id_sep.join(
                        [f"[{sid}]({get_esgf_search_url([sid])})" for sid in source_ids]
                    )
                    out.append(
                        f"For the {mip} simulations in the {prod_or_testing_phase_str} phase of CMIP7, "
                        f"you will need data from the following source IDs:\n{source_id_sep}{source_id_str}.\n\n"
                        "Retrieving and only using valid data will require some care.\n"
                        "Please make sure you read the guidance given at the start of the Summary section\n"
                        "and process the data carefully."
                    )

                db_source_id = DB_SOURCE[DB_SOURCE["source_id"].isin(source_ids)]
                dois_l = db_source_id["doi"].dropna().unique().tolist()
                if len(dois_l) > 0:
                    dois_md = ", ".join(
                        (f"[{doi}]({get_doi_link(doi)})" for doi in dois_l)
                    )
                    if len(dois_l) > 1:
                        doi_s = "DOIs"
                    else:
                        doi_s = "DOI"

                    doi_line = f"The data has the {doi_s}: {dois_md}."

                else:
                    doi_line = "No DOIs are available for this data."

                out.append("")
                out.append(doi_line)
                out.append("")

                out.append(PHASES_COMMON_TEXT[phase.split("-")[-1]])
                out.append("")

    return tuple(out)


def add_cmip7_phase_source_ids(
    raw_split: tuple[str, ...], forcing: str
) -> tuple[str, ...]:
    """
    Add the source IDs to use for each phase of CMIP7

    Parameters
    ----------
    raw_split
        Raw file contents, split into lines

    forcing
        Forcing for which to generate the info

    Returns
    -------
    :
        The updated lines, after the source IDs to use for each phase of CMIP7 have been inserted
    """
    # Use tuples as input and output to avoid accidentally
    # modifying content between different function calls.
    out = []
    in_source_id_summmary = False
    for line in raw_split:
        if line.startswith("<!--- begin-cmip7-phases-source-ids"):
            in_source_id_summmary = True
            out.append(line)
            continue

        if line.startswith("<!--- end-cmip7-phases-source-ids"):
            in_source_id_summmary = False
            out.append(line)
            continue

        if in_source_id_summmary:
            if line.startswith("<!--- Do not edit this section"):
                out.append(line)

                source_id_summary = get_cmip7_phases_source_id_summary_for_forcing(
                    forcing=forcing
                )

                if source_id_summary:
                    out.extend(source_id_summary)

                else:
                    out.append(
                        "No source IDs are available for use in this phase of CMIP7 yet."
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
    source_id_stub_rows = DB_SOURCE[DB_SOURCE["source_id"].str.contains(source_id_stub)]
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
            out.extend(
                textwrap.wrap(
                    txt, width=100, break_on_hyphens=False, break_long_words=False
                )
            )
        out.append("")

    return tuple(out)


def add_revision_history(
    raw_split: tuple[str, ...], source_id_stub: str
) -> tuple[str, ...]:
    """
    Insert the revision history in one of the docs

    Parameters
    ----------
    raw_split
        Raw file contents, split into lines

    source_id_stub
        Stub which indicates the source IDs that should be included in the revision history.

        If a source ID includes this stub, it is included in the revision history.

    Returns
    -------
    :
        The updated lines, after the revision history has been inserted
    """
    # Use tuples as input and output to avoid accidentally
    # modifying content between different function calls.
    out = []
    in_revision_history = False
    for line in raw_split:
        if line.startswith("<!--- begin-revision-history"):
            in_revision_history = True
            out.append(line)
            continue

        if line.startswith("<!--- end-revision-history"):
            in_revision_history = False
            out.append(line)
            continue

        if in_revision_history:
            if line.startswith("<!--- Do not edit this section"):
                out.append(line)

                revision_history = get_revision_history_for_source_id_stub(
                    source_id_stub=source_id_stub
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


def get_file_info(raw_split: Iterable[str]) -> dict[str, str]:
    """
    Get the key info for the file

    This extracts values out of the lines at the top of the file.

    Parameters
    ----------
    raw_split
        Raw file contents, split into lines

    Returns
    -------
    :
        Extracted file information.
    """
    res = {}
    for line in raw_split:
        if line.startswith(
            "<!--- These values are used by `fill-out-auto-generated-sections.py`"
        ):
            continue

        if line.startswith("#"):
            # Up to title, can exit
            break

        info_raw = line.split("<!--- ")[1].split(" -->")[0]
        key, value = info_raw.split("=")
        value = value.strip('"')

        res[key] = value

    return res


def main() -> None:
    file_raw = {}
    file_info = {}
    for file in HERE.glob("*.md"):
        with open(file) as fh:
            raw = fh.read()

        tmp = tuple(raw.splitlines())

        file_raw[file] = tmp
        if file.name == "index.md":
            continue

        file_info[file] = get_file_info(tmp)

    for file in HERE.glob("*.md"):
        out = file_raw[file]

        if file.name == "index.md":
            source_id_stubs = {
                v["forcing"]: v["source_id_stub"] for v in file_info.values()
            }
            out = add_cmip7_phase_source_id_summaries(out, source_id_stubs)

        else:
            info = get_file_info(out)
            out = add_cmip7_phase_source_ids(out, forcing=info["forcing"])
            out = add_revision_history(out, source_id_stub=info["source_id_stub"])

        with open(file, "w") as fh:
            fh.write("\n".join(out))
            fh.write("\n")


# # Can't use this here as not called as main, hence the below
# if __name__ == "__main__":
#     main()
#
main()
