#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 09:21:39 2024

This file extracts global attributes from target files

PJD 24 Jan 2024     - Started
PJD 24 Jan 2024     - Updating with unique % separator

@author: durack1
"""
# %% imports
import argparse
import datetime
import json
import os
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
if os.path.exists(outFile):
    os.remove(outFile)
oH = open(outFile, "w")
fmtTime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
ds = xc.open_mfdataset(inFile)
globAttList = ds.attrs.keys()
print(globAttList)
# iterate over dictionary and write to file
# iterDict(globAttList, oH)
iterDict(ds.attrs, oH)
# add inFile, timestamp, oH.close()
breadCrumbs(oH, inFile, fmtTime)

# terminate
inFile = None
if not inFile:
    sys.exit()

# %% code to extract input4MIPs-cmor-tables PCMDI-AMIP-1-1-9
inFile = "/Users/durack1/sync/git/input4MIPs-cmor-tables/input4MIPs_source_id.json"
with open(inFile, "r") as fH:
    js = json.load(fH)
    pcmdi = js["source_id"]["PCMDI-AMIP-1-1-9"]
    del js

oH = open("PCMDI-AMIP-1-1-9-CV.txt", "w")
fmtTime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
# iterate over dictionary and write to file
iterDict(pcmdi, oH)
# add inFile, timestamp, oH.close()
breadCrumbs(oH, inFile, fmtTime)

# %% code to extract ESGF index for PCMDI-AMIP-1-1-9
url = "https://esgf-node.llnl.gov/esg-search/search/?limit=1000&format=application%2Fsolr%2Bjson&source_id=PCMDI-AMIP-1-1-9&variable_id=tos&project=input4mips&project=input4MIPs&distrib=false&fields=*"
js = requests.get(url)
js_srcId = json.loads(js.text)
srcId = js_srcId["response"]["docs"][0]
oH = open("PCMDI-AMIP-1-1-9-ESGF.txt", "w")
fmtTime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
# iterate over dictionary and write to file
iterDict(srcId, oH)
# add inFile, timestamp, oH.close()
breadCrumbs(oH, "PCMDI-AMIP-1-1-9-ESGF", fmtTime)
