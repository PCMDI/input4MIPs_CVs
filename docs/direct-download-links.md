# Direct download links

There have been some issues accessing the data via metagrid.
Here we demonstrate how direct download links can be obtained from the links provided in
[github.com/PCMDI/input4MIPs_CVs/blob/main/direct-download-info/direct-download-info.json](https://github.com/PCMDI/input4MIPs_CVs/blob/main/direct-download-info/direct-download-info.json).
We will attempt to keep this file up-to-date as files are published
as a backup to finding files via metagrid
or globus (see [https://app.globus.org/file-manager?origin_id=904ff241-867c-404e-b355-64b701ba6ac1&origin_path=%2Fuser_pub_work%2Finput4MIPs%2FCMIP7%2F](https://app.globus.org/file-manager?origin_id=904ff241-867c-404e-b355-64b701ba6ac1&origin_path=%2Fuser_pub_work%2Finput4MIPs%2FCMIP7%2F)).

To get your direct download links, a script like the following will work.

```python
import json
import urllib.request

direct_download_info_url = "https://raw.githubusercontent.com/PCMDI/input4MIPs_CVs/refs/heads/direct-download-links/direct-download-info/direct-download-info.json"
with urllib.request.urlopen(direct_download_info_url) as response:
    raw_response = response.read()
    direct_download_info = json.loads(raw_response)

data_of_interest = [
    v for v in direct_download_info if v["source_id"] == "FZJ-CMIP-ozone-vl-1-0"
]
download_links = [v["download_link"] for v in data_of_interest]
print("You can then download the links with your tool of choice")
for dl in download_links:
    print(f"- {dl}")
```

At the time of writing, this produced the following output

```sh
You can then download the links with your tool of choice
- https://esgf-node.ornl.gov/thredds/fileServer/user_pub_work/input4MIPs/CMIP7/ScenarioMIP/FZJ/FZJ-CMIP-ozone-vl-1-0/atmos/mon/zmta/gn/v20260409/zmta_input4MIPs_ozone_ScenarioMIP_FZJ-CMIP-ozone-vl-1-0_gn_202201-210012.nc
- https://esgf-node.ornl.gov/thredds/fileServer/user_pub_work/input4MIPs/CMIP7/ScenarioMIP/FZJ/FZJ-CMIP-ozone-vl-1-0/atmos/mon/vmro3/gn/v20260409/vmro3_input4MIPs_ozone_ScenarioMIP_FZJ-CMIP-ozone-vl-1-0_gn_206001-210012.nc
- https://esgf-node.ornl.gov/thredds/fileServer/user_pub_work/input4MIPs/CMIP7/ScenarioMIP/FZJ/FZJ-CMIP-ozone-vl-1-0/atmos/mon/vmro3/gn/v20260409/vmro3_input4MIPs_ozone_ScenarioMIP_FZJ-CMIP-ozone-vl-1-0_gn_202201-205912.nc
```

If you're familiar with [pandas](https://pandas.pydata.org/),
you can also make your data exploration slightly more straightforward
with code like the below

```python
import pandas as pd

# Building on the code above
# (you can also initialise the DataFrame directly from the URL if you wish)
direct_download_info_df = pd.DataFrame(direct_download_info)

# For example
direct_download_info_df[
    (direct_download_info_df["source_id"] == "CR-vl-1-1-0")
    & (direct_download_info_df["variable_id"] == "co2")
]
direct_download_info_df[
    (direct_download_info_df["source_id"] == "CR-vl-1-1-0")
    & (direct_download_info_df["frequency"] == "yr")
    & (direct_download_info_df["variable_id"] == "co2")
    & (direct_download_info_df["grid_label"] == "gm")
]
```
