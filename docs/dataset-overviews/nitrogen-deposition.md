<!--- These values are used by `fill-out-auto-generated-sections.py` -->
<!--- forcing="nitrogen-deposition" -->
<!--- source_id_stub="FZJ-CMIP-nitrogen" -->
# Nitrogen deposition

## Key contacts

- Names: Michaela Hegglin
- Emails: m.i.hegglin@fz-juelich.de

## Summary

Nitrogen deposition forcing for the pre-industrial control and historical (and associated) simulations is available.

As a result of an issue being found ([#425](https://github.com/PCMDI/input4MIPs_CVs/issues/425)),
we're providing an updated dataset.
This resolves an apparent latitudinal shift found in the forcing
when moving from PI to historical forcing files.
The error was introduced due to aerosol properties being ingested into one of the historical simulations starting in 1950 instead of 1850
along with an issue in the averaging of the climatological file.
The implication of this error on existing simulations (and their predicted climate forcing)
is deemed to be small (due to compensating effects on N<sub>2</sub>O and CO<sub>2</sub> concentrations).
Therefore, existing model simulations based on `FZJ-CMIP-nitrogen-1-2`
do not need to be rerun if such a rerun is not possible.
Modelling teams that have not begun their simulations should, however,
use the latest version of the forcings as specified below.
Modelling teams should record the version of the forcing files they use following the CMIP7 guidance
(see the 5<sup>th</sup> dot point here https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Guidance_for_modellers/#1-requirements-expectations).

<!--- begin-cmip7-phases-source-ids -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->
### Source IDs for CMIP7 phases

The source ID that identifies the dataset to use in CMIP7 is given below.

#### DECK

##### CMIP7

For the DECK simulations in the production phase of CMIP7, use data with the source ID [FZJ-CMIP-nitrogen-2-0](https://esgf-node.ornl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22FZJ-CMIP-nitrogen-2-0%22%7D)

No DOIs are available for this data.

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

For pre-industrial control, please use the monthly climatology files (frequency value of `monC`).
Simply apply this forcing on repeat.

## Differences in format from CMIP6 or other previous versions

The data format is currently very similar, if not the same as CMIP6
(e.g. variable names are the same, dimensions are the same).
The only change is that we have cleaned up the format
to make it as close to being CF-compliant as possible.

<!--- begin-revision-history -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->
## Revision history

### FZJ-CMIP-nitrogen-1-2

A member of the community raised an issue with a discontinuity between the piControl climatology and
the historical nitrogen deposition in this version. The full discussion is at
https://github.com/PCMDI/input4MIPs_CVs/issues/425. FZJ-CMIP-nitrogen-2-0 fixes the underlying issue
(related to both timing of aerosol property ingestion and the averaging of the piControl climatology
files). If you have started or completed simulations with FZJ-CMIP-nitrogen-1-2, you do not need to
restart or re-run them. However, if you have not yet started simulations, please use
FZJ-CMIP-nitrogen-2-0.

### FZJ-CMIP-nitrogen-1-1

There were faulty N-deposition values in the 1930s across variables and the variable wetNOy was 50%
too high in both the PI and historical forcing fields due to double-counting of some wetNOy
components. They were hence retracted. If you have started simulations with FZJ-CMIP-nitrogen-1-1,
please restart them with the updated FZJ-CMIP-nitrogen-1-2 data. The original issue that identified
this is <a href="https://github.com/PCMDI/input4MIPs_CVs/issues/385">here</a>

### FZJ-CMIP-nitrogen-1-0

Multiple files shared the same tracking ID. They were hence retracted. This is fixed in
FZJ-CMIP-nitrogen-1-1. However, the data is unchanged so simulations do not need to be restarted.

<!--- end-revision-history -->
