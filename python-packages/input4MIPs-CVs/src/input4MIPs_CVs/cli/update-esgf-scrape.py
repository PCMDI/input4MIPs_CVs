"""
Update our scrape of the ESGF index
"""

from __future__ import annotations

import json
from functools import partial
from pathlib import Path
from typing import Annotated, Any

import requests
import requests.adapters
import typer
from tqdm.contrib.concurrent import thread_map

COMMON_PARAMS = dict(
    replica=False,
    activity_id="input4MIPs",
    type="Dataset",
)


def get_source_id_result(
    source_id: str, session: requests.Session
) -> requests.models.Response:
    url = "https://esgf-node.ornl.gov/esgf-1-5-bridge"
    params = dict(
        # hacky, but whatever
        **COMMON_PARAMS,
        limit=10_000,
        facets="source_id",
        source_id=source_id,
    )
    # print(f"Pinging {url=} with {params=}")
    r_source_id = session.get(url, params=params)

    return r_source_id


def get_esgf_info(n_threads: int) -> dict[str, Any]:
    session = requests.Session()
    retries = requests.adapters.Retry(
        # Just in case flaky
        total=10,
        backoff_factor=0.1,
        status_forcelist=[401, 429],
    )
    session.mount("https://", requests.adapters.HTTPAdapter(max_retries=retries))

    url = "https://esgf-node.ornl.gov/esgf-1-5-bridge"
    params = dict(
        # hacky, but whatever
        **COMMON_PARAMS,
        limit=0,
        facets="source_id",
    )
    print(f"Pinging {url=} with {params=}")
    r_source_ids = session.get(
        url,
        params=params,
        # Long timeout just in case
        timeout=100,
    )
    r_source_ids.raise_for_status()

    source_ids = []
    for source_id, n_results_str in zip(
        r_source_ids.json()["facet_counts"]["facet_fields"]["source_id"][::2],
        r_source_ids.json()["facet_counts"]["facet_fields"]["source_id"][1::2],
    ):
        n_results = int(n_results_str)
        if n_results > 10_000:
            msg = f"The API is limited to returning 10 000 results, but {source_id} has {n_results}"
            raise AssertionError(msg)

        source_ids.append(source_id)

    search_results = thread_map(
        partial(get_source_id_result, session=session),
        source_ids,
        max_workers=n_threads,
    )
    res = {}
    failures = []
    for sr in search_results:
        try:
            sr.raise_for_status()
        except requests.exceptions.HTTPError:
            failures.append([sr.url, sr.json()])
            continue

        sr_json = sr.json()
        for ds in sr_json["response"]["docs"]:
            res[ds["instance_id"]] = ds

    if failures:
        failure_status_counts = {}
        for f in failures:
            status = f[1]["status"]
            try:
                failure_status_counts[status] += 1
            except KeyError:
                failure_status_counts[status] = 1

        detail_lines = "\n".join(
            [
                f"{v[0]}\n    {json.dumps(v[1], sort_keys=True, indent=4)}\n"
                for v in failures
            ]
        )
        msg = f"Detail:\n{detail_lines}\nThere were {len(failures)} failures, {failure_status_counts=}"
        raise AssertionError(msg)

    return res


def main(
    out_file: Annotated[Path, typer.Option(help="File in which to write the result")],
    n_threads: Annotated[
        int, typer.Option(help="Number of parallel threads to use")
    ] = 8,
) -> None:
    """
    Scrape information from ESGF
    """
    esgf_info = get_esgf_info(n_threads=n_threads)

    with open(out_file, "w") as fh:
        json.dump(
            esgf_info,
            fh,
            ensure_ascii=True,
            sort_keys=True,
            indent=4,
            separators=(",", ":"),
        )

    print(f"Wrote {out_file}")


if __name__ == "__main__":
    typer.run(main)
