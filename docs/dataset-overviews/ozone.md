<!--- These values are used by `fill-out-auto-generated-sections.py` -->
<!--- forcing="ozone" -->
<!--- source_id_stub="FZJ-CMIP-ozone" -->
# Ozone

## Key contacts

- Names: Michaela Hegglin
- Emails: m.i.hegglin@fz-juelich.de

## Summary

Ozone data is now available.

<!--- begin-cmip7-phases-source-ids -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->
### Source IDs for CMIP7 phases

The source ID that identifies the dataset to use in CMIP7 is given below.

#### DECK

##### CMIP7

For the DECK simulations in the production phase of CMIP7, use data with the source ID [FZJ-CMIP-ozone-1-2](https://esgf-node.ornl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22FZJ-CMIP-ozone-1-2%22%7D)

The data has the DOI: [10.25981/ESGF.input4MIPs.CMIP7/2584173](https://doi.org/10.25981/ESGF.input4MIPs.CMIP7/2584173).

This data is for use in CMIP7 production simulations.
All data sets for use in CMIP7 production simulations are published with a `mip_era` metadata value of 'CMIP7'.
This metadata value appears both in the file's global metadata as well as its metadata on ESGF.

If you find an issue, please
[create an issue on GitHub](https://github.com/PCMDI/input4MIPs_CVs/issues/new?template=data_issue.md)
so that the identification and resolution of this issue is publicly accessible.

##### Testing

No data available for this phase yet.

#### ScenarioMIP

##### CMIP7

No data available for this phase yet.

##### Testing

No data available for this phase yet.

<!--- end-cmip7-phases-source-ids -->

## Navigating the data

### Recommendation for pre-industrial control

For pre-industrial control, there are two options.
The first is the monthly climatology file (frequency value of `monC`).
This dataset averages over a longer simulation, essentially removing variability like the QBO.
If you wish to use this forcing for your piControl,
simply apply it on repeat.

The second is a transient file which has a time range equal to `182901-184912` in the filename.
This file is found in the same directory as the historical forcing
so please be careful to only use it for piControl and do not include it in historical forcing.
This transient piControl forcing includes the QBO signal
but uses average solar forcing and repeating 1850 emissions.
If you wish to use this forcing for your piControl,
simply apply it on repeat.

### Data

At present, only a historical forcing which **includes** the QBO signal is provided.
If you would like a historical forcing without the QBO signal,
please comment on [this discussion](https://github.com/PCMDI/input4MIPs_CVs/discussions/22),
specifically [this thread](https://github.com/PCMDI/input4MIPs_CVs/discussions/22#discussioncomment-14174159).

There are also `zmta` (temperature) files available.
These provide the temperature output that is consistent with the provided ozone files.
This may be useful for those wishing to post-process the ozone forcings into other forms
(e.g. https://github.com/PCMDI/input4MIPs_CVs/discussions/378).

## Differences in format from CMIP6 or other previous versions

The data format is currently very similar, if not the same as CMIP6
(e.g. variable names are the same, dimensions are the same).
The only change is that we have cleaned up the format to make it as close to being CF-compliant as possible
(although it is not fully compliant because of a bounds issue for latitudes,
please [raise an issue](https://github.com/PCMDI/input4MIPs_CVs/issues/new?template=data_issue.md)
if these bounds errors are an insurmountable problem).

<!--- begin-revision-history -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->
## Revision history

### FZJ-CMIP-ozone-1-1

A spurious large value was found in the climatology data related to this dataset, see <a
href="https://github.com/PCMDI/input4MIPs_CVs/issues/373">here</a>. In addition, the latitudinal
bounds in this file were not correct. Both of these issues are corrected in FZJ-CMIP-ozone-1-2.

### FZJ-CMIP-ozone-1-0

The fill value attribute was missing in these files. They were hence retracted  (although, if you're
very careful, they are still usable, you just have to set the fill value manually). The original
issue that identified this is <a href="https://github.com/PCMDI/input4MIPs_CVs/issues/373">here</a>

<!--- end-revision-history -->
