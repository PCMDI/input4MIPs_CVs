"""
Generate a set of direct download links

You can't run this anywhere, you need to be on a machine that has all the data replicated.
"""

from __future__ import annotations

import json
from pathlib import Path

import tqdm
import typer

HERE = Path(__file__).parents[0]


def main(
    tree_root: Path,
    out_file: Path = HERE / "direct-download-info.json",
) -> None:
    """
    Generate the direct download links
    """
    DOWNLOAD_LINK_ROOT = "https://esgf-node.ornl.gov/thredds/fileServer/user_pub_work"

    out = []
    for nc_file in tqdm.tqdm(tree_root.rglob("**/*.nc")):
        input4mips_idx = nc_file.parts.index("input4MIPs")

        parts_rel_to_input4mips = nc_file.parts[input4mips_idx:]
        path_rel_to_input4mips = "/".join(parts_rel_to_input4mips)
        download_link = f"{DOWNLOAD_LINK_ROOT}/{path_rel_to_input4mips}"

        tmp = {
            key: parts_rel_to_input4mips[i]
            for i, key in enumerate(
                [
                    "activity_id",
                    "mip_era",
                    "target_mip",
                    "institution_id",
                    "source_id",
                    "realm",
                    "frequency",
                    "variable_id",
                    "grid_label",
                    "version",
                ]
            )
        }
        tmp["version"] = tmp["version"].lstrip("v")
        tmp["download_link"] = download_link

        out.append(tmp)

    out_file.parent.mkdir(exist_ok=True)
    with open(out_file, "w") as fh:
        json.dump(out, fh)


if __name__ == "__main__":
    typer.run(main)
