# Solar

**All of the text below is a draft written by a non-expert to get things moving.**
**Please do not put any faith in its accuracy.**

## Key contacts

- Names: Bernd Funke
- Emails: bernd@iaa.es

## Summary

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
\[TBD whether uncertainty gets bigger as you go back/forward in time.\]

### Examples of working with the data

[TBD]

## Differences from CMIP6 or other previous versions

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
The CMIP6 data can be found on the ESGF under the "CMIP6" project and source ID "SOLARIS-HEPPA-3-2": 
[pre-filled search here](https://aims2.llnl.gov/search?project=input4MIPs&activeFacets=%7B%22mip_era%22%3A%22CMIP6%22%2C%22source_id%22%3A%22SOLARIS-HEPPA-3-2%22%7D).
[Funke et al., GMD 2024](https://doi.org/10.5194/gmd-17-1217-2024)
provides a detailed analysis of the changes from earlier versions.
\[TODO: consider whether there's a short summary we can give\]
[TODO: get the link to slides from Bernd which dive into this]

<!--- begin-revision-history:SOLARIS-HEPPA-CMIP -->
<!--- Do not edit this section, it is automatically updated when the docs are filled out -->
## Revision history

### SOLARIS-HEPPA-CMIP-4-3

Hence v4.3 is retracted. The change between v4.3 and v4.4 results in a 179 ppm increase of TSI and
SSI compared to version 4.3. The preliminary TSI/SSI version in 4.3 had adapted the TSI scale from
the CTIM instrument alone, the newer TSI scale is based on a TSIS-1 and CTIM composite (Coddington
and Lean, 2024). This composite is also consistent with the TSI 'community consensus' composite
(spot.colorado.edu/~koppg/TSI/TSI_Composite-SIST.txt). The original comment from the data provider
is <a href="https://github.com/PCMDI/input4MIPs_CVs/issues/66#issuecomment-2422882167">here</a>. For
further information, see <a href="https://solarisheppa.geomar.de/cmip7">SOLARIS-HEPPA release
notes</a>.

### SOLARIS-HEPPA-CMIP-4-2

An issue was encountered with the proton ionization data in v4.2. It was hence retracted. The
original comment from the data provider is <a
href="https://github.com/PCMDI/input4MIPs_CVs/issues/17#issuecomment-2255378927">here</a>.

<!--- end-revision-history -->
