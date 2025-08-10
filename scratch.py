"""

Notes for doing this via STAC API:
https://hamedalemo.github.io/advanced-geo-python/lectures/earth_search_tutorial.html

Really good example
Can test with https://api.stac.ceda.ac.uk/
"""

import json

import httpx
import pandas as pd

with open("Database/input4MIPs_db_file_entries.json") as fh:
    db = json.load(fh)


dbdf = pd.DataFrame(db)
# print(dbdf["data_node"].dropna().unique())

from esgpull import Esgpull

esgp = Esgpull()
index_nodes_to_try = [
    "ceda.ac.uk",
    "eagle.alcf.anl.gov",
    "esg-dn1.nsc.liu.se",
    "esgdata.gfdl.noaa.gov",
    "esgf-data.dkrz.de",
    "esgf-data.nersc.gov",
    "esgf-data2.llnl.gov",
    "esgf-node.ipsl.upmc.fr",
    "esgf-node.llnl.gov",
    "esgf-node.ornl.gov",
    "esgf-node.ornl.gov/esgf-1-5-bridge",
    "esgf.nci.org.au",
]
print(sorted(index_nodes_to_try))
for index_node in index_nodes_to_try:
    esgp.config.api.index_node = index_node
    print(f"{index_node=}")
    try:
        print(esgp.fetch_index_nodes())

    except IndexError as e:
        print(f"Failed: {e}")

    try:
        index_node_search = (
            f"{index_node}/esg-search/search"
            if "bridge" not in index_node
            else index_node
        )
        r = httpx.get(
            # f"https://{index_node_search}?source_id=CR-CMIP-1-0-0&format=application%2Fsolr%2Bjson"
            # f"https://{index_node_search}?source_id=CR-CMIP-1-0-0&format=application/solr+json"
            f"https://{index_node_search}",
            params=dict(
                source_id="CR-CMIP-1-0-0",
                format="application/solr+json",
                distrib=True,
                limit=1000,
            ),
            # params=dict(source_id="CR-CMIP-1-0-0", format="application%2Fsolr%2Bjson"),
        )
        r.raise_for_status()
        print(r.text[:140])
        js = r.json()
        print(f'{js["response"]["numFound"]=}')
        print(f'{set([v["data_node"] for v in js["response"]["docs"]])=}')

    except Exception as e:
        print(f"Search failed: {e}")

    print()
explode

import globus_sdk
import pandas as pd
import tqdm.auto as tqdm

pd.options.display.max_rows = None
pd.options.display.max_columns = None

esgf_uuid = "a8ef4320-9e5a-4793-837b-c45161ca1845"

# # Hmm doesn't work - can't seem to get token
# app = globus_sdk.UserApp(client_id=esgf_uuid)
# print(f"{app.login_required()=}")
#
# transferer = globus_sdk.TransferClient(app=app)
# for page in transferer.paginated.endpoint_search(
#     query_params={"activity_id": "input4MIPs"}
# ):
#     for res in page:
#         print("Endpoint ID: {}".format(res["id"]))
#     breakpoint()


searcher = globus_sdk.SearchClient()
sr = searcher.search(esgf_uuid, "")
res = []

data_search = dict(
    q="*",
    filters=[
        {
            "type": "match_any",
            "field_name": facet,
            "values": values,
        }
        for facet, values in [
            ("activity_id", ["input4MIPs"]),
            ("mip_era", ["CMIP7"]),
            ("type", ["Dataset"]),
            ("source_id", ["CR-CMIP-1-0-0"]),
            ("replica", ["true"]),
        ]
    ],
)
search_res = searcher.post_search(esgf_uuid, data=data_search)
scroll_res = searcher.paginated.scroll(esgf_uuid, data=data_search)
for i, page in tqdm.tqdm(
    enumerate(tqdm.tqdm(scroll_res, total=search_res.data["total"]))
):
    content = [e["content"] for v in page.data["gmeta"] for e in v["entries"]]
    res.extend(content)

res_df = pd.DataFrame(res)
breakpoint()
for c in res_df:
    if res_df.loc[:, c].iloc[0] != res_df.loc[:, c].iloc[1]:
        print(c)
        print(res_df.loc[:, c].iloc[:2].tolist())


# Can then use URLs etc. to actually download stuff
# Can use pandas to avoid duplication etc.
