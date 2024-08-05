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

from input4MIPs_CVs.cli.options import REPO_ROOT_DIR_OPTION
from input4MIPs_CVs.html_generation import generate_html_pages

app = typer.Typer()


def parse_version(version_str: str) -> packaging.version.Version:
    """
    Parse the version string

    Parameters
    ----------
    version_str
        Version string to parse

    Returns
    -------
    :
        Parsed version

    Raises
    ------
    ValueError
        The version string is not of the form X.Y.Z,
        where X, Y and Z are numbers.

        Note: The version string may optionally end with the pre-release
        marker "a1", e.g. "7.0.1a1" is a valid version string.
    """
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
    """
    Write the repository's version file

    Parameters
    ----------
    version
        Version to write

    repo_root_dir
        Root directory of the repository

    file_to_write
        File in which to write the version
    """
    with open(repo_root_dir / file_to_write, "w") as fh:
        fh.write(str(version))


def update_readme(
    version: packaging.version.Version,
    repo_root_dir: Path,
    file_to_update: Path = Path("README.md"),
) -> None:
    """
    Update the README's version information

    Parameters
    ----------
    version
        Version for which to write the version information

    repo_root_dir
        Root directory of the repository

    file_to_update
        README file to update
    """
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
    """
    Write the version information into a Python package's `pyproject.toml` file

    Parameters
    ----------
    version
        Version to write

    repo_root_dir
        Root directory of the repository

    file_to_write
        `pyproject.toml` file in which to write the version
    """
    pyproject_toml_file = repo_root_dir / file_to_write
    with open(pyproject_toml_file) as fh:
        raw = fh.read()

    old_version_line_regexp = r'version = "\d+\.\d+\.\d+(a1)?"'
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
    """
    Set the version consistently throughout the repository

    Parameters
    ----------
    version_str
        Version to apply

    repo_root_dir
        Root directory of the repository
    """
    version = parse_version(version_str)
    print(f"Applying {version=!r}. {version.is_prerelease=}")
    if not version.is_prerelease:
        print("Not a pre-release, make sure you tag the repository too")

    write_version_file(version, repo_root_dir=repo_root_dir)
    if not version.is_prerelease:
        update_readme(version, repo_root_dir=repo_root_dir)

    write_version_into_pyproject_toml(version, repo_root_dir=repo_root_dir)

    generate_html_pages(version=version, repo_root_dir=repo_root_dir)


def get_new_version(
    bump_rule: str,
    bump_to_pre_release: bool,
    repo_root_dir: Path,
    existing_version_file_rel_to_repo_root_dir: Path = Path("VERSION"),
) -> packaging.version.Version:
    with open(repo_root_dir / existing_version_file_rel_to_repo_root_dir) as fh:
        current_version_str = fh.read().strip()

    current_version = parse_version(current_version_str)

    if bump_rule == "no-pre-release":
        if bump_to_pre_release:
            msg = f"{bump_rule=} and {bump_to_pre_release=} is contradictory"
            raise ValueError(msg)

        if not current_version.is_prerelease:
            msg = f"Current version is not a pre-release ({current_version=})."
            raise ValueError(msg)

        new_version = packaging.version.Version(
            f"{current_version.major}.{current_version.minor}.{current_version.micro}"
        )

    else:
        if current_version.is_prerelease:
            msg = (
                f"Current version is a pre-release ({current_version=}). "
                "Run `bump no-pre-release` first before bumping the version to avoid ambiguity."
            )
            raise ValueError(msg)

        if bump_rule == "major":
            new_version = packaging.version.Version(f"{current_version.major + 1}.0.0")

        elif bump_rule == "minor":
            if current_version.is_prerelease:
                raise NotImplementedError

            new_version = packaging.version.Version(
                f"{current_version.major}.{current_version.minor + 1}.0"
            )

        elif bump_rule == "micro":
            if current_version.is_prerelease:
                raise NotImplementedError

            new_version = packaging.version.Version(
                f"{current_version.major}.{current_version.minor}.{current_version.micro + 1}"
            )

        else:
            raise NotImplementedError(bump_rule)

        if bump_to_pre_release:
            new_version = packaging.version.Version(
                f"{new_version.major}.{new_version.minor}.{new_version.micro}a1"
            )

    print(f"Will bump {current_version} to {new_version}")

    return new_version


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


@app.command(name="bump")
def bump_command(
    bump_rule: Annotated[
        str,
        typer.Argument(
            help="""Bump rule to use

Options: 'no-pre-release' - bump to the next release i.e. remove any pre-release marker from the version.
'major' - bump the major version i.e. the X in X.Y.Z.
'minor' - bump the minor version i.e. the Y in X.Y.Z.
'micro' - bump the micro version i.e. the Z in X.Y.Z."""
        ),
    ],
    repo_root_dir: REPO_ROOT_DIR_OPTION,
    pre_release: Annotated[
        bool,
        typer.Option(
            help="""Should we bump to a pre-release version?

For example,
if we are currently at 3.4.5 and do a micro release with this flag,
we will go to 3.4.6a1.
If we don't have this flag, we go straight to 3.4.6.""",
        ),
    ] = True,
):
    """
    Set the repository's version

    This applies the given version in all the relevant places in the repository.
    """
    new_version = get_new_version(
        bump_rule, bump_to_pre_release=pre_release, repo_root_dir=repo_root_dir
    )
    set_repository_version(
        str(new_version),
        repo_root_dir=repo_root_dir.absolute(),
    )


if __name__ == "__main__":
    app()
