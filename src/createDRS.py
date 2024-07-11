#!/bin/env python

"""
 This script takes a path, evaluates for netcdf files creating output directories based on file metadata

To run conversion:
$ durack1$ python createDRS.py $filePath

"""
"""2024
PJD  9 Jul 2024 - started
"""

# %% imports
import argparse
import datetime
import glob
import os
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
argDict = parser.parse_args()
filePath = argDict.filePath
# test path
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

# %% get registered info to check against
target_url = "https://raw.githubusercontent.com/PCMDI/input4MIPs_CVs/main/README.md"
txt = urlopen(target_url).read().decode("utf-8")

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
    "nominal_resolution",  # extra
    "realm",
    "source",
    "source_id",
    "source_version",
    "target_mip",
    "variable_id",
    "version",  # ESGF identifier
]

drsList = [
    ""
]

# match with file contents
for cnt1, fPath in enumerate(fileList):
    print("processing:", fPath)
    fH = xc.open_dataset(fPath)
    attDic = fH.attrs
    print(attDic)
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
solhep42 = {}
solhep42["nominal_resolution"] = "250 km"
solhep42["source_version"] = "4.2"
solhep42["version"] = datetime.datetime.strftime("%Y%m%d")


# %% take attributes, create DRS
