#!/bin/env python

"""
This script takes two paths, evaluates for netcdf files with required global
attributes, creates output directories based on file metadata/global attributes
and copies files to these locations

To run conversion:
$ durack1$ python createDRS.py $filePath $destPath

"""
"""2024
PJD  9 Jul 2024 - started
PJD 18 Jul 2024 - working for SOLARIS-HEPPA-CMIP-4-2 data
"""

# %% imports
import argparse
import copy
import datetime
import glob
import json
import os
import pdb
import shutil
import sys
import xcdat as xc
from urllib.request import urlopen

# %% Argparse extract
parser = argparse.ArgumentParser()
parser.add_argument(
    "filePath",
    type=str,
    help="Provide a path where files exist",
)
parser.add_argument(
    "destPath",
    type=str,
    help="Provide a path where new directories should be created",
)
argDict = parser.parse_args()
# filePath
filePath = argDict.filePath
# test filePath
if os.path.exists(filePath):
    print("filePath:", filePath)
else:
    print("Not valid filePath:", filePath)
    sys.exit()
# test for valid files
fileList = glob.glob(os.path.join(filePath, "*.nc"))
if fileList:
    print("fileList:", fileList)
else:
    print("No valid files, exiting")
    sys.exit()

# destPath
destPath = argDict.destPath
# test destPath
if os.path.exists(destPath):
    print("destPath:", destPath)
else:
    print("Not valid destPath:", destPath)
    sys.exit()

# %% function defs


# %% get registered info to check against
target_url = "https://raw.githubusercontent.com/PCMDI/input4MIPs_CVs/main/CVs/input4MIPs_DRS.json"
txt = urlopen(target_url)
DRS = json.load(txt)
DRSPath = DRS["directory_path_template"]
print("DRSPath:", DRSPath)

# %% interrogate each file for valid global attributes

# create attribute list for searching
attList = [
    "activity_id",
    "contact",
    "dataset_category",
    "frequency",
    "further_info_url",
    "grid_label",
    "institution_id",
    "mip_era",
    "nominal_resolution",
    "realm",
    "source",
    "source_id",
    "source_version",
    "target_mip",
    "variable_id",
]
#    "version",  # ESGF identifier

drsList = [
    "activity_id",
    "mip_era",
    "target_mip",
    "institution_id",
    "source_id",
    "realm",
    "frequency",
    "variable_id",
    "grid_label",
]
# version assigned by this script

# match with file contents
for cnt1, fPath in enumerate(fileList):
    print("processing:", fPath)
    fH = xc.open_dataset(fPath)
    attDic = fH.attrs
    # print(attDic)
    fH.close()

    # create checklist
    fileAttList = list(attDic.keys())
    print(fileAttList)

    # process
    for att in attList:
        if att not in fileAttList:
            print("**att:", att, "not included, skipping")
            continue
        vars()[att] = attDic[att]
        print(att, ":", eval(att))

    # catch custom entries/fixes
    # solhep42 = {}
    # solhep42["nominal_resolution"] = "250 km"
    # solhep42["source_version"] = "4.2"

    # %% take attributes, create DRS
    drs = DRSPath
    version = datetime.datetime.now().strftime("%Y%m%d")
    print()
    print("drs:", drs)
    attList2 = copy.deepcopy(attList)
    attList2.append("version")
    for att in attList2:
        attSwitch = "".join(["<", att, ">"])
        print("switching:", attSwitch, eval(att))
        drs = drs.replace(attSwitch, eval(att))
    print("drs:", drs)
    print("fPath:", fPath)
    print("destPath:", destPath)
    # test for existing directory and create
    destFullPath = os.path.join(destPath, drs)
    print("destFullPath:", destFullPath)
    os.makedirs(destFullPath, exist_ok=True)
    destFullPathAndFile = os.path.join(destPath, drs, fPath.split("/")[-1])
    shutil.copy(fPath, destFullPathAndFile)
