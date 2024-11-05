"""
Write the revision history sections in our overview files
"""

from __future__ import annotations

import json
import textwrap
from pathlib import Path

import pandas as pd

HERE = Path(__file__).parent

# Could open this up in future to avoid hard-coded name.
# Fine for now.
current_db_path = HERE.parents[1] / "Database" / "input4MIPs_db_file_entries.json"

with open(current_db_path) as fh:
    db_source = pd.DataFrame(json.load(fh))


def get_revision_history_for_source_id_stub(source_id_stub: str) -> list[str]:
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

    return out


for file in HERE.glob("*.md"):
    if file.name == "index.md":
        continue

    with open(file) as fh:
        raw = fh.read()

    out = []
    in_revision_history = False
    source_id_prefix = None
    for line in raw.splitlines():
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

    with open(file, "w") as fh:
        fh.write("\n".join(out))
