"""
Update our HTML pages
"""

from __future__ import annotations

from typing import Annotated, Optional

import typer

from input4MIPs_CVs.cli.options import REPO_ROOT_DIR_OPTION
from input4MIPs_CVs.html_generation import generate_html_pages


def main(
    repo_root_dir: REPO_ROOT_DIR_OPTION,
    version: Annotated[
        Optional[str],
        typer.Option(
            help="""Version to apply to the repository

If not supplied, we retrieve the version from `VERSION`"""
        ),
    ] = None,
    check_unchanged: Annotated[
        bool,
        typer.Option(
            help="Should an error be raised if the database will change as a result of running this command?"
        ),
    ] = False,
) -> None:
    """
    Create the changes introduced by the PR

    Parameters
    ----------
    out_file
        Output file in which to write the changes
    """
    if version is None:
        with open(repo_root_dir / "VERSION") as fh:
            version = fh.read().strip()

    generate_html_pages(
        version=version, repo_root_dir=repo_root_dir, check_unchanged=check_unchanged
    )


if __name__ == "__main__":
    typer.run(main)
