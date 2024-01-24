#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 09:21:39 2024

This file extracts global attributes from target files

PJD 24 Jan 2024     - Started

@author: durack1
"""
# %% imports
import argparse
import datetime
import xcdat as xc
import os

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

# %% read file, collect global attributes and write to outFile
outFile = fileName.replace(".nc", ".txt")
if os.path.exists(outFile):
    os.remove(outFile)
oH = open(outFile, "w")
fmtTime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
ds = xc.open_mfdataset(inFile)
globAttList = ds.attrs.keys()
for count, key in enumerate(globAttList):
    val = ds.attrs[key]
    output = "".join([": ".join([key, val]), "\n"])
    print(output)
    oH.write(output)

# add inFile
output = "".join(["\ninFile: ", inFile, "\n"])
oH.write(output)
output = "".join(["time: ", fmtTime])
oH.write(output)
oH.close()
