# Land use

**All of the text below is a draft written by a non-expert to get things moving.**
**Please do not put any faith in its accuracy.**

## Key contacts

- Names: Louise Chini, George Hurtt
- Emails: lchini@umd.edu; gchurtt@umd.edu

## Summary

A first version of the land use data is
[available on the ESGF](https://aims2.llnl.gov/search?project=input4MIPs&activeFacets=%7B%22mip_era%22%3A%22CMIP6Plus%22%2C%22institution_id%22%3A%22UofMD%22%2C%22source_id%22%3A%22UofMD-landState-3-0%22%7D).
This version is for testing only, do not use it for any simluations you're not willing to throw away.
We are collecting bugs in [this discussion](https://github.com/PCMDI/input4MIPs_CVs/discussions/141).
If you find any other issues, please add them to
[the discussion](https://github.com/PCMDI/input4MIPs_CVs/discussions/141).
Full details on the dataset and all relevant links can be found
on the [LUH webpage](https://luh.umd.edu/).

## Navigating the data

### Recommendation for pre-industrial control

[TBD]

### Grids and frequencies provided

The data is provided on a 0.25-degree grid with an annual time step.
We use a noleap calendar for simplicity and for cf-compliance. 
However, don't let that confuse you. 
In all calendars, the transitions should be applied between 1 Jan of year X and 1 Jan of year X + 1.

### Variables provided

Variables are provided for land use state, land use management and land use transitions 
as well as a few static fields (such as cell areas).
\[TBD whether it is worth listing variables or just pointing people to relevant docs\]

### Uncertainty

A low and a high estimate of the variables are available.
These estimates can be used to quantify the spread in the value of each variable.
At present, only the best-estimate is published on input4MIPs
but we hope to change this in future.

## Differences from CMIP6 or other previous versions

### File formats and naming

There have been a few updates compared to CMIP6.

1. the file names have been updated to be in line with the input4MIPs DRS.
   The files now all begin with `multiple-<suffix>`, as each file contains more than one variable.
   The suffix then indicates what is contained in each file (states, transitions, management or static).
1. the time axis is now in days rather than in years.
   This fixes an issue with reading data with packages that don't recognise year as a unit
   (given that year is not exactly CF-compliant).
   If you require the data to be back in years,
   divide the time axis by 365 and you will be back to having years as your time axis
   (the noleap calendar is very simple).

### Data

[TBD statement of changes from CMIP6]
