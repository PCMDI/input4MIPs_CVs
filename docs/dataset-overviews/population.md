<!--- These values are used by `fill-out-auto-generated-sections.py` -->
<!--- forcing="population" -->
<!--- source_id_stub="tbd" -->
# Population density

**This section is a work in progress.**

## Key contacts

- Names: Dominik Paprotny, Laurence Hawker
- Emails: dominik.paprotny@pik-potsdam.de, laurence.hawker@bristol.ac.uk

## Summary

<!--- begin-cmip7-phases-source-ids -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->
### Source IDs for CMIP7 phases

The source ID that identifies the dataset to use in CMIP7 is given below.

#### CMIP7

For the CMIP7 phase of CMIP7, use data with the source ID [PIK-CMIP-1-0-0] for the historical period (1850-2025).
For the future scenario (2026-2100) use [PIK-h-1-0-0], [PIK-hl-1-0-0], [PIK-m-1-0-0], [PIK-ml-1-0-0], 
[PIK-l-1-0-0], [PIK-vllo-1-0-0], [PIK-vlho-1-0-0].
This data is for use in CMIP7 production simulations.
All data sets for use in CMIP7 production simulations are published with a `mip_era` metadata value of 'CMIP7'.
This metadata value appears both in the file's global metadata as well as its metadata on ESGF.

If you find an issue, please
[create an issue on GitHub](https://github.com/PCMDI/input4MIPs_CVs/issues/new?template=data_issue.md)
so that the identification and resolution of this issue is publicly accessible.

#### Testing

No data available for this phase yet.

<!--- end-cmip7-phases-source-ids -->

<!--- placeholder for piControl recommendation -->
## Navigating the data

### Recommendation for pre-industrial control

Apply the 1850 value as a constant.

### Grids and frequencies provided

We provide annual data (1850-2100) on a regular 0.25 ('gn') and 0.5 degree ('gr') grid. 
Please notify the authors if you would need other resolutions for your simulations. 

### Variables provided

The dataset contains total population (mid-year estimate) per square kilometer of the grid cell area (pop_dens).

### Uncertainty

The dataset contains many sources of uncertainty that are difficult to quantify at grid-cell level.

### Data

This dataset was created by joint effort of Horizon Europe project [COMPASS](https://compass-climate.eu/) 
and project [WorldPop](https://www.worldpop.org/). The data was created at high resolution (30 arc seconds, ~1 km)
and upscaled to 0.25 degree. The following steps were followed:
(1) WorldPop [gridded constrained global population data for 2015-2025](https://www.worldpop.org/blog/beta-test-our-new-global-population-data-2015-to-2030/) 
were combined with FuturePop projections based on SSP v3.2 trajectories.
(2) The WorldPop gridded population was extrapolated back to 1975 using [Global Human Settlement Layer](https://human-settlement.emergency.copernicus.eu/)
(3) Data were further extrapolated back to 1850 using [HYDE 3.2](https://geo.public.data.uu.nl/vault-hyde/HYDE%203.2%5B1710494848%5D/original/)
(4) The data were adjusted to match annual national timeseries of population:
(a) 1850-1949 from a new compilation of historical population, adjusted to modern country borders made in [COMPASS D3.1](https://zenodo.org/records/14892500)
(b) 1950-2023 from United Nations [World Population Prospects 2024](https://population.un.org/wpp/) with minor adjustments made in [COMPASS D3.1](https://zenodo.org/records/14892500).
(c) 2025-2100 extrapolated from 2020 with gap-filled SSP v3.2 data, and 2024 interpolated between 2023 and 2025.
(5) The population counts were converted to population density based on the size of grid-cells converted from their latitude.

Full documentation of the data will be available soon.

<!--- end of placeholder for piControl recommendation -->

<!--- begin-revision-history -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->
<!--- No revisions, hence section is blank -->
<!--- end-revision-history -->
