"""
Searching globus by timestamp
"""

import globus_sdk
import pandas as pd

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

for time_start, time_end in [
    # "2025-08-08",
    ("2024-08-01", "2024-08-31"),
    ("2025-02-01", "2025-02-28"),
    ("2025-08-09", "*"),
]:
    time_search = dict(
        q="*",
        filters=[
            {
                "type": "range",
                "field_name": "_timestamp",
                "values": [{"from": time_start, "to": time_end}],
            },
            {
                "type": "match_any",
                "field_name": "type",
                "values": ["Dataset"],
            },
        ],
    )
    search_res = searcher.post_search(esgf_uuid, data=time_search, limit=10_000)
    print(f"{time_start} - {time_end}")
    print(search_res.data["total"])

    if search_res.data["total"] > 10_000:
        msg = "Use scroll API - will be very slow"
        raise NotImplementedError(msg)
        res = []
    else:
        res = [e["content"] for v in search_res.data["gmeta"] for e in v["entries"]]

    res_df = pd.DataFrame(res)
    if res_df.empty:
        print("Nothing published")
        continue

    print(f"{res_df.shape=}")
    print(f"{res_df['master_id'].unique()=}")
    print(res_df["_timestamp"].unique())
    try:
        # TODO: report that source_id is a list rather than string
        source_ids = flat_list = [
            sid for sid_list in res_df["source_id"] for sid in sid_list
        ]
        print(set(source_ids))
    except KeyError:
        print(
            f"No source_id column in result, available columns: {sorted(res_df.columns)}"
        )
    print()


# Can then use URLs etc. to actually download stuff
# Can use pandas to avoid duplication etc.
