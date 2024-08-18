"""
Create a comment that shows the changes in the database introduced by a PR
"""

from __future__ import annotations

from pathlib import Path
from typing import Annotated, Union

import typer

from input4MIPs_CVs.db_changes import get_pr_db_changes_comment


def main(
    current_db: Annotated[Path, typer.Option(help="Path to the new database state")],
    out_file: Annotated[
        Path, typer.Option(help="File in which to write the changes")
    ] = Path("db-changes.md"),
    commit_id: Annotated[
        Union[str, None],
        typer.Option(
            help="""ID of the commit we're looking at.

If supplied, we use this to provide a clearer message about which diff we're looking at."""
        ),
    ] = None,
) -> None:
    """
    Create the changes introduced by the PR

    Parameters
    ----------
    out_file
        Output file in which to write the changes
    """
    changes_comment = get_pr_db_changes_comment(
        current_db_path=current_db, commit_id=commit_id
    )

    with open(out_file, "w") as fh:
        # Ensure newline at end of file
        fh.write(f"{changes_comment}\n")


if __name__ == "__main__":
    typer.run(main)
