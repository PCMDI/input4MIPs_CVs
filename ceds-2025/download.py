import urllib.request
from pathlib import Path

LINKS_FILE = "CEDS_release-v_2025_03_18.txt"
OUT_DIR = Path("ceds-2025-03-18")

with open(LINKS_FILE) as fh:
    links = fh.readlines()

total = len(links)
for i, link in enumerate(links):
    if "BC" not in link:
        continue

    print(f"{i} / {total}")
    link_s = link.strip()
    filename = link_s.split("/")[-1]
    out_file = OUT_DIR / filename
    if out_file.exists():
        print(f"{out_file} exists")
        continue

    out_file.parent.mkdir(exist_ok=True, parents=True)
    print(f"Downloading {link_s}")
    urllib.request.urlretrieve(link_s, out_file)
    # break
