"""
Auto-generate the index and nav pages
"""

from __future__ import annotations

from pathlib import Path

HERE = Path(__file__).parent


def write_index(pages_sorted: list[Path], out_file: Path) -> None:
    content_l = [
        "# Forcings email archive",
        "",
        "Here we provide an archive of emails with updates about the forcings sent by the CMIP International Project Office (IPO).",
        "",
    ]

    for page in pages_sorted:
        content_l.append(f"- [{page.stem}]({page.name})")

    content = "\n".join(content_l)
    with open(out_file, "w") as fh:
        fh.write(content)

    return


def write_nav(pages_sorted: list[Path], out_file: Path) -> None:
    content_l = [
        "- [Overview](index.md)",
    ]

    for page in pages_sorted:
        content_l.append(f"- [{page.stem}]({page.name})")

    content = "\n".join(content_l)
    with open(out_file, "w") as fh:
        fh.write(content)

    return


def main() -> None:
    pages = [f for f in HERE.glob("*.md") if f.name not in ["index.md", "SUMMARY.md"]]
    pages_sorted = sorted(pages, key=lambda x: x.name, reverse=True)

    write_index(pages_sorted=pages_sorted, out_file=HERE / "index.md")
    write_nav(pages_sorted=pages_sorted, out_file=HERE / "SUMMARY.md")


# # Can't use this here as not called as main, hence the below
# if __name__ == "__main__":
#     main()
#
main()
