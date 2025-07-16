"""
Show the updates to the ESGF JSON
"""

import json
from pathlib import Path

import requests


def main():
    base_commit = "b70bdf7bdbfc955de7e776bc69795a0fd673403c"
    base_commit = "main"

    esgf_json = Path("Database/input-data/esgf-input4MIPs.json")

    with open(esgf_json) as fh:
        scrape_latest = json.load(fh)

    if base_commit == "main":
        base_url_to_hit = f"https://raw.githubusercontent.com/PCMDI/input4MIPs_CVs/refs/heads/main/{str(esgf_json)}"

    else:
        base_url_to_hit = f"https://raw.githubusercontent.com/PCMDI/input4MIPs_CVs/{base_commit}/{str(esgf_json)}"

    scrape_base_r = requests.get(base_url_to_hit)
    scrape_base_r.raise_for_status()
    scrape_base = scrape_base_r.json()

    only_in_latest = set(scrape_latest.keys()) - set(scrape_base.keys())
    print(f"{only_in_latest=}")

    only_in_base = set(scrape_base.keys()) - set(scrape_latest.keys())
    print(f"{only_in_base=}")
    print()

    for master_id, entry_latest in scrape_latest.items():
        if master_id in only_in_latest:
            continue

        entry_base = scrape_base[master_id]

        only_in_latest_entry = set(entry_latest.keys()) - set(entry_base.keys())
        if only_in_latest_entry:
            print(f"{master_id=}")
            print(f"{only_in_latest_entry=}")
            print()

        only_in_base_entry = set(entry_base.keys()) - set(entry_latest.keys())
        if only_in_base_entry:
            print(f"{master_id=}")
            print(f"{only_in_base_entry=}")
            print()

        # if (
        #     entry_latest["data_node"] == "esgf-node.ornl.gov"
        #     and entry_base["data_node"] == "esgf-data2.llnl.gov"
        # ):
        #     continue

        if (
            entry_latest["data_node"] == "esgf-node.ornl.gov"
            and entry_base["data_node"] == "eagle.alcf.anl.gov"
        ):
            continue

        if (
            entry_latest["data_node"] == "esgf-node.ornl.gov"
            and entry_base["data_node"] == "aims3.llnl.gov"
        ):
            continue

        if (
            entry_latest["data_node"] == "esgf-node.ornl.gov"
            and entry_base["data_node"] == "esgf-data.nersc.gov"
        ):
            continue

        for key, latest_value in entry_latest.items():
            if key in only_in_latest_entry:
                continue

            base_value = entry_base[key]

            if latest_value != base_value:
                print(f"{master_id=}")
                print(f"{key=}")
                print(f"{latest_value=}")
                print(f"{base_value=}")
                print()


if __name__ == "__main__":
    main()
