"""
Load the CVs with input4MIPs validation
"""

from __future__ import annotations

from pathlib import Path

from input4mips_validation.cvs import load_cvs

REPO_ROOT = Path(__file__).parents[1]


def main() -> None:
    cvs = load_cvs(str(REPO_ROOT / "CVs"))

    print(f"{cvs=}")


if __name__ == "__main__":
    main()
