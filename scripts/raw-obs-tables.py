"""
Create some tables showing our dependencies on raw observations
"""

from __future__ import annotations

import pandas as pd

pd.set_option("display.width", 10000)
pd.set_option("display.max_colwidth", 10000)


raw = pd.read_csv("raw-obs.csv")

print(raw)

funder_n = raw[["funder_id", "forcing"]].drop_duplicates()["funder_id"].value_counts()
print(funder_n)
single_source_funders = funder_n[funder_n < 2].index.values
print(", ".join(sorted(single_source_funders)))
print(
    raw[["funder_id", "forcing", "obs_id"]]
    .set_index(["funder_id", "forcing"])
    .sort_index()
)
print(raw[["funder_id", "obs_id", "forcing"]].set_index(["forcing"]).sort_index())
