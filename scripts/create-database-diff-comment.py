"""
Create a comment that shows the changes in the database introduced by a PR
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import pandas_diff as pd_diff
import typer


def get_changes_comment() -> str:
    """
    Get the changes comment to post
    """
    return "Comment TBC"


def main(out_file: Path = Path(".")) -> None:
    """
    Create the changes introduced by the PR

    Parameters
    ----------
    out_file
        Output file in which to write the changes
    """
    changes_comment = get_changes_comment()

    with open(out_file, "w") as fh:
        fh.write(changes_comment)


if __name__ == "__main__":
    typer.run(main)
