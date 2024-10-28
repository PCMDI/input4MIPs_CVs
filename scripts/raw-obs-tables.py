"""
Create some tables showing our dependencies on raw observations
"""

from __future__ import annotations

import pandas as pd

pd.set_option("display.width", 10000)
pd.set_option("display.max_colwidth", 10000)


raw = pd.read_csv("raw-obs.csv")

print(raw)

print(
    raw[["funder_id", "obs_id", "forcing"]]
    .set_index(["funder_id", "obs_id"])
    .sort_index()
)
print(raw[["funder_id", "obs_id", "forcing"]].set_index(["forcing"]).sort_index())
