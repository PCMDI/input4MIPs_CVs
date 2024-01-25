#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 09:21:39 2024

This file extracts global attributes from target files

PJD 24 Jan 2024     - Started
PJD 24 Jan 2024     - Updating with unique % separator
PJD 24 Jan 2024     - Updating to extract ESGF index info across CMIP6, 5, 3, input4MIPs and obs4MIPs

@author: durack1
"""
# %% imports
import argparse
import datetime
import json
import os
import platform
import requests
import sys
import xcdat as xc

# %% function defs


def breadCrumbs(fileHandle, inFile, fmtTime):
    output = "".join(["\ninFile% ", inFile, "\n"])
    fileHandle.write(output)
    output = "".join(["time% ", fmtTime])
    fileHandle.write(output)
    fileHandle.close()


def iterDict(dic, fileHandle):
    for key in dic.keys():
        val = dic[key]
        print(val, type(val))
        if isinstance(val, list):
            val = val[0]
        output = "".join(["% ".join([key, str(val)]), "\n"])
        print(output)
        fileHandle.write(output)


def openFile(outFileName):
    if os.path.exists(outFileName):
        os.remove(outFileName)
    oH = open(outFileName, "w")
    return oH


# %% get inFile path and name from argparse
parser = argparse.ArgumentParser(description="Filename and complete path")
parser.add_argument("-f", "--file", help="Filename and complete path", required=True)
args = vars(parser.parse_args())
inFile = args["file"]
print("inFile:", inFile)
fileName = inFile.split("/")[-1]
print("fileName:", fileName)
filePath = inFile.replace(fileName, "")
print("filePath:", filePath)

# read file, collect global attributes and write to outFile
outFile = fileName.replace(".nc", ".txt")
oH = openFile(outFile)
fmtTime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
ds = xc.open_mfdataset(inFile)
globAttList = ds.attrs.keys()
print(globAttList)
# iterate over dictionary and write to file
# iterDict(globAttList, oH)
iterDict(ds.attrs, oH)
# add inFile, timestamp, oH.close()
breadCrumbs(oH, inFile, fmtTime)

# terminate if not durack1/Darwin
if platform.system() != "Darwin":
    sys.exit()

# %% code to extract input4MIPs-cmor-tables PCMDI-AMIP-1-1-9
inFile = "/Users/durack1/sync/git/input4MIPs-cmor-tables/input4MIPs_source_id.json"
with open(inFile, "r") as fH:
    js = json.load(fH)
    pcmdi = js["source_id"]["PCMDI-AMIP-1-1-9"]
    del js

oH = openFile("PCMDI-AMIP-1-1-9-CV.txt")
fmtTime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
# iterate over dictionary and write to file
iterDict(pcmdi, oH)
# add inFile, timestamp, oH.close()
breadCrumbs(oH, inFile, fmtTime)

# %% code to extract ESGF index across all key projects
dic = {
    "CMIP6-ACCESS-CM2-historical-Omon-tos": "https://esgf-node.llnl.gov/esg-search/search/?limit=1000&format=application%2Fsolr%2Bjson&source_id=ACCESS-CM2&project=CMIP6&table_id=Omon&variable_id=tos&member_id=r1i1p1f1&experiment_id=historical&data_node=esgf-data1.llnl.gov&distrib=false&fields=*",
    "CMIP5-ACCESS-1-3-historical-Omon-wfo": "https://esgf-node.llnl.gov/esg-search/search/?limit=1000&format=application%2Fsolr%2Bjson&model=ACCESS1.3&project=CMIP5&&cmor_table=Omon&variable=wfo&ensemble=r1i1p1&experiment=historical&distrib=false&fields=*",
    "CMIP3-MPI-ECHAM5-amip-Amon-hus": "https://esgf-node.llnl.gov/esg-search/search/?limit=1000&format=application%2Fsolr%2Bjson&model=mpi_echam5&project=CMIP3&project=cmip3&time_frequency=mon&ensemble=run2&variable=hus&experiment=amip&distrib=false&fields=*",
    "input4MIPs-PCMDI-AMIP-1-1-9-Omon-tos": "https://esgf-node.llnl.gov/esg-search/search/?limit=1000&format=application%2Fsolr%2Bjson&source_id=PCMDI-AMIP-1-1-9&variable_id=tos&project=input4mips&project=input4MIPs&distrib=false&fields=*",
    "obs4MIPs-CERES-EBAF-4-2-rlds": "https://esgf-node.llnl.gov/esg-search/search/?limit=1000&format=application%2Fsolr%2Bjson&source_id=CERES-EBAF-4-2&activity_id=obs4MIPs&activity_id=obs4mips&frequency=mon&variable_id=rlds&distrib=false&fields=*",
}
for key in dic.keys():
    url = dic[key]
    outFile = ".".join([key, "txt"])
    js = requests.get(url)
    js_srcId = json.loads(js.text)
    srcId = js_srcId["response"]["docs"][0]
    oH = openFile(outFile)
    fmtTime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    # iterate over dictionary and write to file
    iterDict(srcId, oH)
    # add inFile, timestamp, oH.close()
    breadCrumbs(oH, key, fmtTime)
