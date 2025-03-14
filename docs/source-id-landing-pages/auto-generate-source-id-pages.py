"""
Auto-generate the source ID pages
"""

from __future__ import annotations

import json
from pathlib import Path

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

for source_id, info in source_id_entries.items():
    publication_status = (
        DB_SOURCE.loc[DB_SOURCE["source_id"] == source_id, "publication_status"]
        .unique()
        .tolist()
    )
    if all(v in ["never_published", "abandoned"] for v in publication_status):
        # Never published, don't need a landing page
        continue

    source_id_filename = f"{source_id}.md"
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
