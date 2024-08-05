"""
Manipulation of the repository's version number

This allows us to apply the version consistently throughout the repository.
There is probably already tooling that exists for this.
However, our use case didn't immediately fit any pattern that I knew,
and this tooling is pretty easy to build and understand, so here we are.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Annotated

import packaging.version
import typer

from input4MIPs_CVs.html_generation import generate_html_pages

app = typer.Typer()

REPO_ROOT_DIR_OPTION = Annotated[
    Path, typer.Option(help="Root directory of the repository")
]


def parse_version(version_str: str) -> packaging.version.Version:
    if not re.match(r"^\d+\.\d+\.\d+(a1)?$", version_str):
        msg = (
            "Version string must be of the form X.Y.Z, where X, Y and Z are numbers. "
            "It may optionally end with 'a1'. "
            f"Received {version_str=}"
        )
        raise ValueError(msg)

    return packaging.version.Version(version_str)


def write_version_file(
    version: packaging.version.Version,
    repo_root_dir: Path,
    file_to_write: Path = Path("VERSION"),
) -> None:
    with open(repo_root_dir / file_to_write, "w") as fh:
        fh.write(str(version))


def update_readme(
    version: packaging.version.Version,
    repo_root_dir: Path,
    file_to_update: Path = Path("README.md"),
) -> None:
    readme_file = repo_root_dir / file_to_update
    with open(readme_file) as fh:
        raw = fh.read()

    old_latest_version_line_regexp = "".join(
        [
            re.escape("[!"),
            re.escape("[Latest release]"),
            re.escape("(https://img.shields.io/badge/Latest%20release-"),
            r"v\d+\.\d+\.\d+",
            re.escape("-brightgreen.svg)"),
            re.escape("]"),
            re.escape("(https://github.com/PCMDI/input4MIPs_CVs/releases/tag/"),
            r"v\d+\.\d+\.\d+",
        ]
    )
    new_latest_version_line = (
        "[!"
        "[Latest release]"
        f"(https://img.shields.io/badge/Latest%20release-v{version}-brightgreen.svg)"
        "]"
        f"(https://github.com/PCMDI/input4MIPs_CVs/releases/tag/v{version})"
    )
    new_readme = re.sub(
        pattern=old_latest_version_line_regexp,
        repl=new_latest_version_line,
        string=raw,
    )

    with open(readme_file, "w") as fh:
        fh.write(new_readme)


def write_version_into_pyproject_toml(
    version: packaging.version.Version,
    repo_root_dir: Path,
    file_to_write: Path = Path("python-packages") / "input4MIPs-CVs" / "pyproject.toml",
) -> None:
    pyproject_toml_file = repo_root_dir / file_to_write
    with open(pyproject_toml_file) as fh:
        raw = fh.read()

    old_version_line_regexp = 'version = "\d+\.\d+\.\d+(a1)?"'
    new_version_line = f'version = "{version}"'

    new_pyproject_toml = re.sub(
        pattern=old_version_line_regexp,
        repl=new_version_line,
        string=raw,
    )

    with open(pyproject_toml_file, "w") as fh:
        fh.write(new_pyproject_toml)


def set_repository_version(
    version_str: str,
    repo_root_dir: str,
) -> None:
    version = parse_version(version_str)
    print(f"Applying {version=!r}. {version.is_prerelease=}")
    if not version.is_prerelease:
        print("Not a pre-release, make sure you tag the repository too")

    write_version_file(version, repo_root_dir=repo_root_dir)
    if not version.is_prerelease:
        update_readme(version, repo_root_dir=repo_root_dir)

    write_version_into_pyproject_toml(version, repo_root_dir=repo_root_dir)

    generate_html_pages(version=version, repo_root_dir=repo_root_dir)


@app.callback()
def cli():
    """
    Entrypoint for the command-line interface defined by this module
    """


@app.command(name="set")
def set_command(
    version: Annotated[str, typer.Option(help="Version to apply to the repository")],
    repo_root_dir: REPO_ROOT_DIR_OPTION,
):
    """
    Set the repository's version

    This applies the given version in all the relevant places in the repository.
    """
    set_repository_version(version, repo_root_dir=repo_root_dir.absolute())


if __name__ == "__main__":
    app()
