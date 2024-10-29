# Open biomass burning emissions

## Summary

**All of the text below is a draft written by a non-expert to get things moving.**
**Please do not put any faith in its accuracy.**

A first version of the open biomass burning emissions is
[available on the ESGF](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22DRES-CMIP-BB4CMIP7-1-0%22%7D).
This version is for testing only, do not use it for any simluations you're not willing to throw away.
We are collecting bugs in [this discussion](https://github.com/PCMDI/input4MIPs_CVs/discussions/138).
If you find any other issues, please add them to
[the discussion](https://github.com/PCMDI/input4MIPs_CVs/discussions/138).
Full details on the dataset and all relevant links can be found
on the [GFED webpage](https://www.globalfiredata.org/).

## Navigating the data

### Recommendation for pre-industrial control

[TBD, unclear whether we should be smoothing 
or keeping internal variability in the data, over what time period etc.]

### Grids and frequencies provided

The data is all provided on a 0.25-degree grid
with a monthly frequency (except for cell areas, which are fixed).

### Variables provided

Data is provided for 
BC, CO, CO<sub>2</sub>, H<sub>2</sub>, NH<sub>3</sub>, NMVOC (see the `NMVOC_bulk` variable), NO<sub>x</sub>, N<sub>2</sub>O, OC and SO<sub>2</sub>.
There is also data for volatile organic compounds individually.
[Add anything else which is missing]

### Uncertainty

[TBD]

### Examples of working with the data

The [emission harmonisation team's notebooks](https://github.com/iiasa/emissions_harmonization_historical/)
may be of interest.

## Differences from CMIP6

### File formats and naming

The file formats are generally similar to CMIP6,
with a number of things being cleaned up.
The naming is very similar, 
except we have attempted to remove all hyphens and underscores from the variable names 
because these can cause issues for packages working with the data.

### Data

The data is an extension of the CMIP6 data i.e. there is no change in the data pre-2015.
An update to the entire timeseries is planned with the release of GFED5,
but it is not expected that this will happen on the CMIP7 fast track timeline.
