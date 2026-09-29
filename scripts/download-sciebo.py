"""
Download all the files in a public sciebo share

Sciebo is ownCloud/Nextcloud based,
so public shares can be accessed over WebDAV
using the share token as the username and an empty password.
"""

from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlparse

import requests
import typer

WEBDAV_PREFIX = "/public.php/webdav"
DAV_NS = {"d": "DAV:"}


def list_files(
    session: requests.Session, base_url: str, path: str = ""
) -> list[tuple[str, int]]:
    """
    List all files in the share, recursing into sub-directories

    Returns a list of (path relative to the share root, size in bytes)
    """
    resp = session.request(
        "PROPFIND", f"{base_url}{WEBDAV_PREFIX}/{path}", headers={"Depth": "1"}
    )
    resp.raise_for_status()

    out = []
    for response in ET.fromstring(resp.content).findall("d:response", DAV_NS):
        rel_path = unquote(response.findtext("d:href", namespaces=DAV_NS))
        rel_path = rel_path.removeprefix(WEBDAV_PREFIX).strip("/")
        if rel_path == path.strip("/"):
            # The directory itself
            continue

        prop = response.find("d:propstat/d:prop", DAV_NS)
        if prop.find("d:resourcetype/d:collection", DAV_NS) is not None:
            out.extend(list_files(session, base_url, f"{rel_path}/"))
        else:
            size = int(prop.findtext("d:getcontentlength", namespaces=DAV_NS))
            out.append((rel_path, size))

    return out


def download_file(
    session: requests.Session, url: str, out_file: Path, size: int
) -> None:
    """
    Download a file, resuming a previous partial download if there is one
    """
    if out_file.exists() and out_file.stat().st_size == size:
        print(f"Already downloaded, skipping: {out_file}")
        return

    out_file.parent.mkdir(parents=True, exist_ok=True)
    part_file = out_file.with_name(f"{out_file.name}.part")
    have = part_file.stat().st_size if part_file.exists() else 0

    headers = {"Range": f"bytes={have}-"} if have else {}
    with session.get(url, headers=headers, stream=True) as resp:
        resp.raise_for_status()
        if have and resp.status_code != requests.codes.partial_content:
            # Server ignored the range request, start again
            have = 0

        print(f"Downloading {out_file} ({size / 1e6:.1f} MB)")
        with open(part_file, "ab" if have else "wb") as fh:
            for chunk in resp.iter_content(chunk_size=2**20):
                fh.write(chunk)

    if part_file.stat().st_size != size:
        msg = (
            f"Size mismatch for {out_file}: "
            f"got {part_file.stat().st_size}, expected {size}"
        )
        raise ValueError(msg)

    part_file.rename(out_file)


def main(
    share_url: str = typer.Argument(
        help="Sciebo share link e.g. https://fz-juelich.sciebo.de/s/trMCrbsJGgn6qgZ"
    ),
    out_dir: Path = typer.Argument(help="Directory in which to save the files"),
) -> None:
    """
    Download all the files in a public sciebo share
    """
    parsed = urlparse(share_url)
    base_url = f"{parsed.scheme}://{parsed.netloc}"
    # Links look like https://<host>/s/<token>
    token = parsed.path.rstrip("/").removesuffix("/download").split("/")[-1]

    session = requests.Session()
    session.auth = (token, "")

    files = list_files(session, base_url)
    total_size = sum(size for _, size in files)
    print(f"Found {len(files)} files ({total_size / 1e9:.2f} GB)")

    for rel_path, size in files:
        download_file(
            session,
            f"{base_url}{WEBDAV_PREFIX}/{rel_path}",
            out_dir / rel_path,
            size,
        )


if __name__ == "__main__":
    typer.run(main)

