# Solar

## Summary

**All of the text below is a draft written by a non-expert to get things moving.**
**Please do not put any faith in its accuracy.**

The solar dataset is rapidly approaching a final version and is
[available on the ESGF](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22SOLARIS-HEPPA-CMIP-4-4%22%7D).
This version is for testing only, do not use it for any simluations you're not willing to throw away.
We are collecting bugs in [this discussion](https://github.com/PCMDI/input4MIPs_CVs/discussions/19)
and aim to release a new version which addresses these bugs in December 2025.
If you find any other issues, please add them to
[the discussion](https://github.com/PCMDI/input4MIPs_CVs/discussions/19).

## Navigating the data

### Recommendation for pre-industrial control

There is a dedicated pre-industrial control file.

### Grids and frequencies provided

The data is provided on a wavelength, pressure level and latitudinal grid.
The data is provided with two frequencies: monthly and daily.

### Species provided

Multiple variables are provided, including total solar irradiance (`tsi`),
which provides the total solar irradiance at 1 AU.

### Uncertainty

At present, we provide no analysis of the uncertainty associated with these datasets.
This is a work in progress, we hope to provide that data when it is available.
[TBD size of uncertainty in radiative forcing terms, seems relatively large?]
[TBD whether uncertainty gets bigger as you go back/forward in time.]

### Examples of working with the data

[TBD]

## Differences from CMIP6

### File formats and naming

The file formats are generally close to CMIP6.
The key change is in the file naming.
The files are now named according to the DRS, 
but this does make it harder to tell which file is which at first glance.
The pre-industrial control file is a fixed field, hence has `fn` in the filename
The two different frequencies are also distinguished in the filename,
`mon` for monthly data and `day` daily data.

### Data

There are some changes from CMIP6.
[Funke et al., GMD 2024](https://doi.org/10.5194/gmd-17-1217-2024)
provides a detailed analysis.
[TODO: get the link to slides from Bernd which dive into this]
[TODO: consider whether there's a short summary we can give]
