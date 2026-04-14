"""
Check API types
"""

import requests


def main():
    url = "https://esgf-node.ornl.gov/esgf-1-5-bridge"

    for source_id in ["PIK-CMIP-1-0-0"]:
        params = dict(
            replica=False,
            activity_id="input4MIPs",
            type="Dataset",
            facets="source_id",
            source_id=source_id,
        )

        r = requests.get(url, params=params)
        r_json = r.json()

        timestamp_vs = [v["_timestamp"] for v in r_json["response"]["docs"]]

        print(f"{source_id=}")
        print(f"{timestamp_vs=}")
        print()


if __name__ == "__main__":
    main()
