"""
Options that are common across our CLI
"""

from pathlib import Path
from typing import Annotated

import typer

REPO_ROOT_DIR_OPTION = Annotated[
    Path, typer.Option(help="Root directory of the repository")
]
