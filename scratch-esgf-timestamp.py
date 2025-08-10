"""
Get ESGF records updated after a given timestamp
"""

from __future__ import annotations

import datetime as dt

import httpx
import tqdm.auto as tqdm


def main():
    get_after = dt.datetime.strptime("2025-08-09", "%Y-%m-%d")

    url = "https://esgf-node.ornl.gov/esgf-1-5-bridge"

    all_by_timestamp_r = httpx.get(
        url,
        params=dict(facets="_timestamp"),
    )
    all_by_timestamp_r.raise_for_status()
    all_by_timestamp_d = all_by_timestamp_r.json()

    tmp = all_by_timestamp_d["facet_counts"]["facet_fields"]["_timestamp"]
    timestamp_counts = {
        timestamp: count for timestamp, count in zip(tmp[::2], tmp[1::2])
    }
    dt_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    timestamps = [dt.datetime.strptime(v, dt_format) for v in timestamp_counts.keys()]
    timestamps_of_interest = [v for v in timestamps if v > get_after]
    for ts in tqdm.tqdm(timestamps_of_interest):
        ts_s = dt.datetime.strftime(ts, dt_format)
        # Reduce back to 3 digits for microsecond
        ts_s = f"{ts_s[:-4]}Z"
        n_res = timestamp_counts[ts_s]
        if n_res > 10_000:
            msg = "Scrolling support for large numbers of results not implemented"
            raise NotImplementedError(msg)

        # This doesn't work: can't query by timestamp like this
        ts_r = httpx.get(
            url,
            params=dict(_timestamp=ts_s),
        )
        ts_r.raise_for_status()
        ts_d = ts_r.json()


if __name__ == "__main__":
    main()
