"""
Update the publication status of some files in our database
"""

from __future__ import annotations

from pathlib import Path

import json

import pandas as pd

import typer


def main() -> None:
    """
    Update the publication status

    This is a script, so tweak the logic as you wish.

    Note that this will update the database file.
    However, it's tracked with Git,
    so we don't have to worry too much.
    """
    DB_FILE = (
        Path(__file__).parents[2] / "DatasetsDatabase" / "input4MIPs_datasets.json"
    )

    with open(DB_FILE) as fh:
        db_raw = json.load(fh)

    db = pd.DataFrame(db_raw)

    # Here is where custom modifications go
    db.loc[(db["source_id"] == "PCMDI-AMIP-1-1-9"), "publication_status"] = "published"
    db.loc[(db["source_id"] == "MRI-JRA55-do-1-6-0"), "publication_status"] = (
        "published"
    )

    with open(DB_FILE, "w") as fh:
        json.dump(
            db.to_dict(orient="records"),
            fh,
            ensure_ascii=True,
            sort_keys=True,
            indent=4,
            separators=(",", ":"),
        )

    print(f"Update {DB_FILE}")


if __name__ == "__main__":
    typer.run(main)
