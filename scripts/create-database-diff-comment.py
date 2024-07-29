"""
Create a comment that shows the changes in the database introduced by a PR
"""

from __future__ import annotations

from pathlib import Path

import typer

from input4MIPs_CVs.db_changes import get_pr_db_changes_comment


def main(out_file: Path = Path(".")) -> None:
    """
    Create the changes introduced by the PR

    Parameters
    ----------
    out_file
        Output file in which to write the changes
    """
    changes_comment = get_pr_db_changes_comment()

    with open(out_file, "w") as fh:
        fh.write(changes_comment)


if __name__ == "__main__":
    typer.run(main)
