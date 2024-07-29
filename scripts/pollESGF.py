#!/bin/env python

"""
This script queries the ESGF SOLR index and pulls out all
input4MIPs/project entries
"""

"""2024
PJD 25 Jul 2024 - started
PJD 25 Jul 2024 - 1216 372 Datasets returned, 350 Files
PJD 26 Jul 2024 - update to write to ../DatasetsDatabase/input-data/ (was ./)
"""

# %% imports
import json
import numpy as np
import os
import requests

# %% get SOLR source_id entries
activityId = "input4MIPs"

# Dataset search (type:File search is also possible)
inputsD = (
    "https://esgf-node.llnl.gov/solr/datasets/select?q=*:*&"
    "rows=0&wt=json&facet=true&"
    "fq=type:Dataset&fq=replica:false&fq=activity_id:"
    + activityId
    + "&facet.field=source_id"
)
print("inputsD:", inputsD)
js = requests.get(inputsD, timeout=5)
js_mipsD = json.loads(js.text)

# File search - does not return deprecated files
inputsF = (
    "https://esgf-node.llnl.gov/solr/files/select?q=*:*&"
    "rows=0&wt=json&facet=true&"
    "fq=type:File&fq=replica:false&fq=activity_id:"
    + activityId
    + "&facet.field=source_id"
)
print("inputsF:", inputsF)
js = requests.get(inputsF, timeout=5)
js_mipsF = json.loads(js.text)

# %% query results - 240725 1159 (latest data SOLARIS-HEPPA-CMIP-4-2

# print Dataset source_id entry count, should be >372
dicInpmD = js_mipsD["facet_counts"]["facet_fields"]["source_id"]
print("len(dicInpmD):", len(dicInpmD))

# print File source_id entry count, should be >350
dicInpmF = js_mipsF["facet_counts"]["facet_fields"]["source_id"]
print("len(dicInpmF):", len(dicInpmF))

# datasets
srcIdLen = len(dicInpmD)
print("srcIdDLen:", srcIdLen)
els = np.arange(0, srcIdLen, 2)
srcIdDDict = {}
srcIds = dicInpmD  # reset to generic variable name
counts = 0
for cnt, srcId in enumerate(els.tolist()):
    srcIdDDict[srcIds[srcId]] = srcIds[srcId + 1]
    counts += int(srcIds[srcId + 1])

print("len(srcIdDDict.keys()):", len(srcIdDDict.keys()))
print("dataset counts:", counts)
# sort dictionary
srcIdDDictList = list(sorted(srcIdDDict.keys()))

# files
srcIdLen = len(dicInpmF)
print("srcIdFLen:", srcIdLen)
els = np.arange(0, srcIdLen, 2)
srcIdFDict = {}
srcIds = dicInpmF  # reset to generic variable name
counts = 0
for cnt, srcId in enumerate(els.tolist()):
    srcIdFDict[srcIds[srcId]] = srcIds[srcId + 1]
    counts += int(srcIds[srcId + 1])

print("len(srcIdFDict.keys()):", len(srcIdFDict.keys()))
print("dataset counts:", counts)
# sort dictionary
srcIdFDictList = list(sorted(srcIdFDict.keys()))

# determine missing/inconsistent
print(
    "Search results: Dataset includes, excluded from File ",
    "searches (likely latest:false):",
)
print(set(srcIdDDictList).difference(srcIdFDictList))

# %% using source_id entries from Dataset search build and write a library
solrQry = (
    "https://esgf-node.llnl.gov/esg-search/search/?limit=1000&"
    "format=application%2Fsolr%2Bjson&source_id="
    "PLACEHOLDER" + "&project=input4mips&project=input4MIPs&"
    "distrib=false&fields=*"
)  # all fields
mstrJson = {}  # create catch dictionary
oF = "tmp.json"
for count, srcId in enumerate(srcIdDDict.keys()):
    # print(count, srcId)
    qryStr = solrQry.replace("PLACEHOLDER", srcId)
    js = requests.get(qryStr, timeout=5)
    js_srcId = json.loads(js.text)
    # write to placeholder to test
    srcIdLen = len(js_srcId["response"]["docs"])
    # https://stackoverflow.com/questions/24816237/ipython-notebook-clear-cell-output-in-code
    print("len(js_srcId):", "{:03d}".format(srcIdLen), srcId)
    for entry in np.arange(0, srcIdLen):
        a = js_srcId["response"]["docs"][entry]
        instId = a["instance_id"]
        mstrJson[instId] = a
        if os.path.exists(oF):
            os.remove(oF)
        fH = open(oF, "w", encoding="utf-8")
        json.dump(
            a,
            fH,
            ensure_ascii=True,
            sort_keys=True,
            indent=4,
            separators=(",", ":"),
        )
        fH.close()
print("All done")
# cleanup
os.remove(oF)  # cleanup
# Write all out
oF = "../Database/input-data/esgf.json"
if os.path.exists(oF):
    os.remove(oF)
fH = open(oF, "w", encoding="utf-8")
json.dump(
    mstrJson,
    fH,
    ensure_ascii=True,
    sort_keys=True,
    indent=4,
    separators=(",", ":"),
)
fH.close()
