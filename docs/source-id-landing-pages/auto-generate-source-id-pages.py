"""
Auto-generate the source ID pages
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pandas as pd

HERE = Path(__file__).parent
# Could open this up in future to avoid hard-coded name.
# Fine for now.
REPO_ROOT = HERE.parents[1]
CURRENT_DB_PATH = REPO_ROOT / "Database" / "input4MIPs_db_file_entries.json"
SOURCE_ID_CVS = REPO_ROOT / "CVs" / "input4MIPs_source_id.json"

with open(CURRENT_DB_PATH) as fh:
    DB_SOURCE = pd.DataFrame(json.load(fh))

with open(SOURCE_ID_CVS) as fh:
    source_id_entries = json.load(fh)


def get_assumed_unique_value(invs: list[Any]) -> Any:
    if len(invs) != 1:
        # breakpoint()
        raise AssertionError(invs)

    return invs[0]


def get_doi_link(doi: str) -> str:
    if not doi.startswith("https://doi.org/"):
        return f"https://doi.org/{doi}"

    return doi


for source_id, info in source_id_entries.items():
    db_source_id = DB_SOURCE.loc[DB_SOURCE["source_id"] == source_id, :]
    dois_l = db_source_id["doi"].dropna().unique().tolist()
    if len(dois_l) > 0:
        dois_md = ";".join((f"[{doi}]({get_doi_link(doi)})" for doi in dois_l))
    else:
        dois_md = "Not provided"

    publication_status = db_source_id["publication_status"].unique().tolist()
    if all(v in ["never_published", "abandoned"] for v in publication_status):
        # Never published, don't need a landing page
        continue

    if all(v in ["registered"] for v in publication_status):
        # Only registered, don't need a landing page yet
        continue

    source_id_filename = f"{source_id}.md"
    source_id_citation_info_filename = f"{source_id}.json"
    esgf_url = f"https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22{source_id}%22%5D%7D"
    author_info_lines = []
    for i, author in enumerate(info["authors"]):
        orcid_info = f"[ORCID {author['orcid']}](https://orcid.org/{author['orcid']})"
        affiliation_info = [f"    - {v}" for v in author["affiliations"]]
        author_lines = [
            f"{i + 1}. {author['name']} ({orcid_info})",
            *affiliation_info,
            "",
        ]

        author_info_lines.extend(author_lines)

    to_write = [
        f"# {source_id}",
        "",
        f"*ESGF link*: [{esgf_url}]({esgf_url})",
        "",
        f"*DOI(s)*: {dois_md}",
        "",
        "## Authors",
        "",
        *author_info_lines,
        "",
        "## Basic metadata",
        "",
        f"- source_id: {source_id}",
        f"- contact: {info['contact']}",
        f"- further_info_url: {info['further_info_url']}",
    ]
    with open(HERE / source_id_filename, "w") as fh:
        fh.write("\n".join(to_write))

    citation_info = {}
    contributors_l = []
    creators_l = []
    for author in info["authors"]:
        first_name, last_name = author["name"].split(" ", maxsplit=1)

        contributors_l.append(
            {
                "contributorName": f"{last_name}, {first_name}",
                "contributorType": "ContactPerson",
                "givenName": first_name,
                "familyName": last_name,
                "email": author["email"],
                "affiliation": ". ".join(author["affiliations"]),
                "nameIdenfitier": {
                    "schemeURI": "https://orcid.org/",
                    "nameIdenfitierScheme": "ORCID",
                    "pid": author["orcid"],
                },
            }
        )

        creators_l.append(
            {
                "creatorName": f"{last_name}, {first_name}",
                "givenName": first_name,
                "familyName": last_name,
                "email": author["email"],
                "affiliation": ". ".join(author["affiliations"]),
                "nameIdenfitier": {
                    "schemeURI": "https://orcid.org/",
                    "nameIdenfitierScheme": "ORCID",
                    "pid": author["orcid"],
                },
            }
        )

    citation_info["creators"] = creators_l
    creation_years = (
        db_source_id["creation_date"]
        .dropna()
        .map(lambda x: int(x.split("-")[0]))
        .unique()
        .tolist()
    )
    if creation_years:
        creation_year = max(creation_years)
    else:
        raise NotImplementedError

    creation_dates = (
        db_source_id["creation_date"]
        .map(lambda x: "-".join(x.split("T")[0].split("-")[:3]))
        .unique()
        .tolist()
    )

    # Hard-coding like this isn't ideal, but ok.
    drs_id = get_assumed_unique_value(
        db_source_id["esgf_dataset_master_id"]
        .apply(lambda x: ".".join(x.split(".")[:5]))
        .unique()
        .tolist()
    )

    # # Urgh CEDS has multiple, just use the first
    # doi = get_assumed_unique_value(db_source_id["doi"].unique().tolist())
    doi = db_source_id["doi"].unique().tolist()[0]

    license_ids = db_source_id["license_id"].dropna().unique().tolist()
    if license_ids:
        license_id = get_assumed_unique_value(license_ids)
    else:
        license_id = None

    mip_era = get_assumed_unique_value(db_source_id["mip_era"].unique().tolist())

    citation_info["dates"] = [
        {
            "dateType": "Created",
            "date": cd,
        }
        for cd in creation_dates
    ]
    # Could probably do a better job of this, but ok
    citation_info["descriptions"] = [
        {
            "descriptionType": "Abstract",
            "text": (
                "CMIP forcing dataset (input4MIPs).\n"
                f"This is all data published under the unique ID (known as a source ID) {source_id}."
            ),
        }
    ]
    citation_info["formats"] = [{"format": "application/x-netcdf"}]
    citation_info["fundingReferences"] = []
    if doi is not None:
        citation_info["identifier"] = {
            "identifierType": "DOI",
            "id": doi,
        }
    else:
        # No DOI
        citation_info["identifier"] = {}

    citation_info["language"] = "en"
    citation_info["publication_year"] = creation_year
    citation_info["publisher"] = "Earth System Grid Federation"
    # Could maybe automate this better, but for now don't worry about it
    citation_info["relatedIdentifiers"] = []
    citation_info["resourceType"] = {
        "resourceTypeGeneral": "Dataset",
        "resourceType": "Digital",
    }
    if license_id is not None and license_id != "CC BY 4.0":
        # if license_id is None, assume CC BY 4.0
        raise AssertionError(license_id)

    citation_info["rightsList"] = [
        {
            "rightsURI": "http://creativecommons.org/licenses/by/4.0/",
            "rights": "Creative Commons Attribution 4.0 International License (CC BY 4.0)",
        }
    ]
    citation_info["subjects"] = [
        {
            "subject": drs_id,
            "subjectScheme": "DRS",
        },
        {"subject": "forcing data"},
        {"subject": "climate"},
        {"subject": mip_era},
    ]
    citation_info["titles"] = f"{source_id} data provided as part of input4MIPs"

    with open(HERE / source_id_citation_info_filename, "w") as fh:
        json.dump(citation_info, fh, indent=2, sort_keys=True)
