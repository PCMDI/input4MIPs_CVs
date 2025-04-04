<!--- These values are used by `fill-out-auto-generated-sections.py` -->
<!--- forcing="solar" -->
<!--- source_id_stub="SOLARIS-HEPPA" -->
# Solar

## Key contacts

- Names: Bernd Funke
- Emails: bernd@iaa.es

## Summary

The CMIP7 version of the solar dataset has been released.
If you find any problems,
please [raise an issue](https://github.com/PCMDI/input4MIPs_CVs/issues/new?template=data_issue.md).
Discussions on this and earlier versions can be found in
[https://github.com/PCMDI/input4MIPs_CVs/discussions/19](https://github.com/PCMDI/input4MIPs_CVs/discussions/19).

<!--- begin-cmip7-phases-source-ids -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->
### Source IDs for CMIP7 phases

The source ID that identifies the dataset to use in CMIP7 is given below.

#### CMIP7

For the CMIP7 phase of CMIP7, use data with the source ID [SOLARIS-HEPPA-CMIP-4-6](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22SOLARIS-HEPPA-CMIP-4-6%22%5D%7D)

This data is for use in CMIP7 production simulations.
All data sets for use in CMIP7 production simulations are published with a `mip_era` metadata value of 'CMIP7'.
This metadata value appears both in the file's global metadata as well as its metadata on ESGF.

If you find an issue, please
[create an issue on GitHub](https://github.com/PCMDI/input4MIPs_CVs/issues/new?template=data_issue.md)
so that the identification and resolution of this issue is publicly accessible.

#### Testing

For the testing phase of CMIP7, use data with the source ID [SOLARIS-HEPPA-CMIP-4-5](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22SOLARIS-HEPPA-CMIP-4-5%22%5D%7D)

This data is for testing (both of the forcing data and of modelling workflows) only.
Production simulations should not be started based on any data that has a `mip_era` value equal to 'CMIP6Plus'.
(The `mip_era` metadata value appears both in each file's global attributes as well as its metadata on ESGF.)

If you have any feedback, please add it to the [relevant GitHub discussion](https://github.com/PCMDI/input4MIPs_CVs/discussions).

<!--- end-cmip7-phases-source-ids -->

## Navigating the data

### Recommendation for pre-industrial control

There is a dedicated pre-industrial control file.
See the files with `fx` in their name
(`fx` stands for fixed, which is used
because the pre-industrial control file is a fixed field,
custom for the pre-industrial control experiment).

### Grids and frequencies provided

The data is provided on a wavelength, pressure level and latitudinal grid.
The data is provided with two frequencies: monthly and daily.

### Species provided

Multiple variables are provided, please see the files for the full list and information.
Of particular interest for many is total solar irradiance (`tsi`),
which provides the total solar irradiance at 1 AU.

### Uncertainty

At present, we provide no analysis of the uncertainty associated with these datasets.
This is a work in progress, we hope to provide that data when it is available.

<!---
### Examples of working with the data

[TBD]
-->

## Differences from CMIP6 or other previous versions

### File formats and naming

The file formats are generally close to CMIP6.
The key change is in the file naming.
The files are now named according to the DRS, 
but this does make it harder to tell which file is which at first glance.
The pre-industrial control file is a fixed field, hence has `fn` in the filename
(although even this is not 100% accurate, but we have avoided changing it to minimise downstream headaches,
for details, see [https://github.com/PCMDI/input4MIPs_CVs/issues/184](https://github.com/PCMDI/input4MIPs_CVs/issues/184)).
The two different frequencies are also distinguished in the filename,
`mon` for monthly data and `day` for daily data.

### Data

There are some changes from CMIP6.
The CMIP6 data can be found 
[on the ESGF under the "CMIP6" project and source ID "SOLARIS-HEPPA-3-2"](https://aims2.llnl.gov/search?project=input4MIPs&activeFacets=%7B%22mip_era%22%3A%22CMIP6%22%2C%22source_id%22%3A%22SOLARIS-HEPPA-3-2%22%7D).
[Funke et al., GMD 2024](https://doi.org/10.5194/gmd-17-1217-2024)
provides a detailed analysis of the changes from earlier versions.
<!---
\[TODO: consider whether there's a short summary we can give\]
[TODO: get the link to slides from Bernd which dive into this]
-->

<!--- begin-revision-history -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->
## Revision history

### SOLARIS-HEPPA-CMIP-4-4

v4.5 resolves issues with MEE short-term variability. Hence v4.4 is retracted. There are no changes
to SSI/TSI (so, if you have used v4.4 for SSI/TSI, you do not need to restart). The original comment
from the data provider is <a
href="https://github.com/PCMDI/input4MIPs_CVs/issues/139#issuecomment-2493311999">here</a>. For
further information, see <a href="https://solarisheppa.geomar.de/cmip7">SOLARIS-HEPPA release
notes</a>.

### SOLARIS-HEPPA-CMIP-4-3

v4.4 uses the final, absolute TSI scale (in consonance with NNL1) which should be used in CMIP7.
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
