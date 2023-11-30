#!/bin/env python

"""
To run conversion:
(base) ml-9953350:src durack1$ python jsonToHtml.py 6.5.0.0

"""
"""2023
PJD 29 Nov 2023 - copied from https://github.com/WCRP-CMIP/CMIP6_CVs/blob/138a089499cd2a9418186fb27cd184063f2d34da/src/jsonToHtml.py
PJD 29 Nov 2023 - first prototype completes
"""

# This script takes the json file and turns it into a nice jquery/data-tabled html doc
import argparse

# from collections import defaultdict
import json
import os
import re
import sys

# %% Create generic header
header = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<meta name="author" content="Paul J. Durack" />
<meta name="description" content="Controlled vocabulary for input4MIPs" />
<meta name="keywords" content="HTML, CSS, JavaScript" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<link rel="stylesheet" type="text/css" charset="utf-8" href="https://pcmdi.github.io/assets/dataTables/jquery.dataTables.min.css" />
<script type="text/javascript" charset="utf-8" src="https://pcmdi.github.io/assets/jquery/jquery.slim.min.js"></script>
<script type="text/javascript" charset="utf-8" src="https://pcmdi.github.io/assets/dataTables/jquery.dataTables.min.js"></script>
<!-- Global site tag (gtag.js) - Google Analytics -->
<script type="text/javascript" src="https://pcmdi.github.io/assets/google/googleAnalyticsTag.js" ></script>
<script type="text/javascript">
//<![CDATA[
$(document).ready( function () {
    $('#table_id').DataTable();
    } );
//]]>
</script>\n"""

# %% Argparse extract
# Matching version format 6.2.11.2
# verTest = re.compile(r'[6][.][2][.][0-9]+[.][0-9]+')
verTest = re.compile(r"[6][.][5][.][0-9]+[.][0-9]")
parser = argparse.ArgumentParser()
parser.add_argument(
    "ver",
    metavar="str",
    type=str,
    help="For e.g. '6.2.11.2' as a command line argument will ensure version information is written to the html output",
)
argDict = parser.parse_args()
if re.search(verTest, argDict.ver):
    version = argDict.ver  # 1 = make files
    print("** HTML Write mode - ", version, " will be written **")
else:
    print("** Version: ", version, " invalid, exiting")
    sys.exit()

# %% Set global arguments
destDir = "../docs/"

# %% Process source_id
infile = "../input4MIPs_source_id.json"
f = open(infile)
exp_dict = json.load(f)
exp_dict1 = exp_dict.get("source_id")  # Fudge to extract duplicate level
# exp_dict2 = exp_dict.get("version")
# print(exp_dict2)
# print(dict.keys())
fout = "".join([destDir, infile[:-4].replace("../", ""), "html"])
if os.path.exists(fout):
    os.remove(fout)
print("processing", fout)
fo = open(fout, "w")

# print >> fo, ''.join([header, """
fo.write(
    "".join(
        [
            header,
            "<title>input4MIPs source_id values</title>\n</head>\n<body>",
            "<p><h1>PCMDI input4MIPs_CVs version: ",
            version,
            "</h1></p>",
            '<table id="table_id" class="display compact" style="width:100%">\n',
        ]
    )
)

"""
../input4MIPs_source_id.json
"ACCESS1-3-rcp85-1-0":{
    "_timestamp":"2021-04-22T19:05:37.327Z",
    "contact":"ISMIP6 Steering Team (ismip6@gmail.com)",
    "data_node":"esgf-data2.llnl.gov",
    "dataset_category":"surfaceFluxes",
    "datetime_start":"1950-07-01T00:00:00Z",
    "datetime_stop":null,
    "frequency":"yrC",
    "institution_id":"NASA-GSFC",
    "latest":true,
    "mip_era":"CMIP6",
    "realm":"landIce",
    "replica":false,
    "source_id":"ACCESS1-3-rcp85-1-0",
    "source_version":"1.0",
    "target_mip":"ISMIP6",
    "version":"20210422",
    "xlink":"http://cera-www.dkrz.de/WDCC/meta/CMIP6/input4MIPs.CMIP6.ISMIP6.NASA-GSFC.ACCESS1-3-rcp85-1-0.ocean.yrC.thetao.grg.v20210422.json|Citation|citation"
"""
dictOrderK = [  # html target
    "institution_id",
    "mip_era",
    "target_mip",
    "datetime_start",
    "datetime_stop",
    "dataset_category",
    "realm",
    "contact",
    "latest",
    "source_version",
    "version",
    "_timestamp",
]

first_row = False
for exp in exp_dict1.keys():
    exp_dict = exp_dict1[exp]
    # Create table columns
    if not first_row:
        ids = dictOrderK  # Overwrite ordering
        for hf in ["thead", "tfoot"]:
            fo.write("<%s>\n<tr>\n<th>source_id</th>\n" % hf)
            for i in ids:
                i = i.replace("_", " ")  # Remove '_' from table titles
                fo.write("<th>%s</th>\n" % i)
            fo.write("</tr>\n</%s>\n" % hf)
    first_row = True
    fo.write("<tr>\n<td>%s</td>\n" % exp)
    # Fill columns with values
    for k in ids:
        # Deal with embeds
        st = exp_dict[k]
        if isinstance(st, (list, tuple)):
            st = " ".join(st)
        if (st is None) or (type(st) is bool):
            pass
            # print(st, type(st))
        elif "@" in st:
            st = st.replace("@", " at ")
        fo.write("<td>%s</td>\n" % st)
    fo.write("</tr>\n")
fo.write("</table>")
fo.write("""\n</body>\n</html>\n""")
