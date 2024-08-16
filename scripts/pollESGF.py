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
import argparse
import json
import numpy as np
import os
import pdb
import requests
import sys

# %% function defs


def is_pathname_valid(pathname: str) -> bool:
    """
    `True` if the passed pathname is a valid pathname for the current OS;
    `False` otherwise.
    """
    # If this pathname is either not a string or is but is empty, this pathname
    # is invalid.
    # https://stackoverflow.com/questions/9532499/check-whether-a-path-is-valid-in-python-without-creating-a-file-at-the-paths-ta
    try:
        if not isinstance(pathname, str) or not pathname:
            return False

        # Strip this pathname's Windows-specific drive specifier (e.g., `C:\`)
        # if any. Since Windows prohibits path components from containing `:`
        # characters, failing to strip this `:`-suffixed prefix would
        # erroneously invalidate all valid absolute Windows pathnames.
        _, pathname = os.path.splitdrive(pathname)

        # Directory guaranteed to exist. If the current OS is Windows, this is
        # the drive to which Windows was installed (e.g., the "%HOMEDRIVE%"
        # environment variable); else, the typical root directory.
        root_dirname = (
            os.environ.get("HOMEDRIVE", "C:")
            if sys.platform == "win32"
            else os.path.sep
        )
        assert os.path.isdir(root_dirname)  # ...Murphy and her ironclad Law

        # Append a path separator to this directory if needed.
        root_dirname = root_dirname.rstrip(os.path.sep) + os.path.sep

        # Test whether each path component split from this pathname is valid or
        # not, ignoring non-existent and non-readable path components.
        for pathname_part in pathname.split(os.path.sep):
            try:
                os.lstat(root_dirname + pathname_part)
            # If an OS-specific exception is raised, its error code
            # indicates whether this pathname is valid or not. Unless this
            # is the case, this exception implies an ignorable kernel or
            # filesystem complaint (e.g., path not found or inaccessible).
            #
            # Only the following exceptions indicate invalid pathnames:
            #
            # * Instances of the Windows-specific "WindowsError" class
            #   defining the "winerror" attribute whose value is
            #   "ERROR_INVALID_NAME". Under Windows, "winerror" is more
            #   fine-grained and hence useful than the generic "errno"
            #   attribute. When a too-long pathname is passed, for example,
            #   "errno" is "ENOENT" (i.e., no such file or directory) rather
            #   than "ENAMETOOLONG" (i.e., file name too long).
            # * Instances of the cross-platform "OSError" class defining the
            #   generic "errno" attribute whose value is either:
            #   * Under most POSIX-compatible OSes, "ENAMETOOLONG".
            #   * Under some edge-case OSes (e.g., SunOS, *BSD), "ERANGE".
            except OSError as exc:
                if hasattr(exc, "winerror"):
                    if exc.winerror == ERROR_INVALID_NAME:
                        return False
                elif exc.errno in {errno.ENAMETOOLONG, errno.ERANGE}:
                    return False
    # If a "TypeError" exception was raised, it almost certainly has the
    # error message "embedded NUL character" indicating an invalid pathname.
    except TypeError as exc:
        return False
    # If no exception was raised, all path components and hence this
    # pathname itself are valid. (Praise be to the curmudgeonly python.)
    else:
        return True


def is_path_creatable(pathname: str) -> bool:
    """
    `True` if the current user has sufficient permissions to create the passed
    pathname; `False` otherwise.
    """
    # Parent directory of the passed path. If empty, we substitute the current
    # working directory (CWD) instead.
    dirname = os.path.dirname(pathname) or os.getcwd()
    return os.access(dirname, os.W_OK)


def is_path_exists_or_creatable(pathname: str) -> bool:
    """
    `True` if the passed pathname is a valid pathname for the current OS _and_
    either currently exists or is hypothetically creatable; `False` otherwise.

    This function is guaranteed to _never_ raise exceptions.
    """
    try:
        # To prevent "os" module calls from raising undesirable exceptions on
        # invalid pathnames, is_pathname_valid() is explicitly called first.
        return is_pathname_valid(pathname) and (
            os.path.exists(pathname) or is_path_creatable(pathname)
        )
    # Report failure on non-fatal filesystem complaints (e.g., connection
    # timeouts, permissions issues) implying this path to be inaccessible. All
    # other exceptions are unrelated fatal issues and should not be caught here.
    except OSError:
        return False


# %% get destination path and validate write perms
parser = argparse.ArgumentParser("simple_example")
parser.add_argument(
    "destPath",
    help="A local system path where an output json file will be written",
    type=str,
)
args = parser.parse_args()
if not is_path_exists_or_creatable(args.destPath):
    print("Destination path:", args.destPath, "does not exist, exiting")


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
oF = os.path.join(args.destPath, "esgf-input4MIPs.json")
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
