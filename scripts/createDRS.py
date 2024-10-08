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
PJD 28 Aug 2024 - switched out logic, so DRS generation depends on drsList, rather
                  than broader list
PJD  8 Oct 2024 - add back in check for tracking_id and creation_date format
"""

# %% imports
import argparse
import copy
import datetime
import glob
import json
import os
import re
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


def checkCreationDate(creationDate):
    """
    Validate creation_date entry matches format that ESGF publisher expects
    creation_date = 2023-05-12T13:46:40Z
    """
    creationDateFormat = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")
    if not creationDateFormat.fullmatch(creationDate):
        print()
        print("** creation_date:", creationDate, "format mismatch **")
        print()


def checkTrackingId(trackingId):
    """
    Validate tracking_id entry matches format ESGF publisher expects
    tracking_id = hdl:21.14100/b52e19fb-de3f-301d-96f3-8b4b16ff8646
    """
    trackingIdFormat = re.compile(
        r"hdl:21\.14100\/[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}"
    )
    if not trackingIdFormat.fullmatch(trackingId):
        print()
        print("** tracking_id:", trackingId, "format mismatch **")
        print()


# %% get registered info to check against
target_url = "https://raw.githubusercontent.com/PCMDI/input4MIPs_CVs/main/CVs/input4MIPs_DRS.json"
txt = urlopen(target_url)
DRS = json.load(txt)
DRSPath = DRS["directory_path_template"]
print("DRSPath:", DRSPath)

# %% interrogate each file for valid global attributes

# absolutely essential attribute list from CMIP6
# https://docs.google.com/document/d/1pU9IiJvPJwRvIgVaSDdJ4O0Jeorv_2ekEtted34K9cA/edit#bookmark=id.xfvfxbc88ali
absEssAttList = [
    "Conventions",
    "activity_id",
    "contact",
    "creation_date",
    "dataset_category",
    "frequency",
    "further_info_url",
    "grid_label",
    "institution",
    "institution_id",
    "mip_era",
    "nominal_resolution",
    "realm",
    "source",
    "source_id",
    "source_version",
    "target_mip",
    "title",
    "tracking_id",
    "variable_id",
]

# ESGF attributes required by publisher
esgfAttList = ["creation_date", "tracking_id"]
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

# preallocate tracking_id list to catch duplicates
trackingIdList = []

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

    # process absolutely essential list
    for att in absEssAttList:
        if att not in fileAttList:
            print("** att:", att, "not included, skipping **")
            continue
        vars()[att] = attDic[att]
        print(att, ":", eval(att))

    # process ESGF publisher required
    for att in esgfAttList:
        if att not in fileAttList:
            print("** att:", att, "not included, exiting **")
            sys.exit()
        # capture tracking_id
        if att == "tracking_id":
            trackingIdList.append(attDic[att])
        # test trackingIdList for duplicates
        if len(trackingIdList) != set(trackingIdList):
            print("** att:", att, "duplicate found, exiting **")
            sys.exit()
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
    drsList2 = copy.deepcopy(drsList)
    drsList2.append("version")
    for att in drsList2:
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
