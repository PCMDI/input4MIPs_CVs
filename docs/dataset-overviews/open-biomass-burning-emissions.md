<!--- These values are used by `fill-out-auto-generated-sections.py` -->
<!--- forcing="biomass_burning_emms" -->
<!--- source_id_stub="DRES-CMIP-BB4CMIP7" -->
# Open biomass burning emissions

**This section is a work in progress.**
**For a first draft, see https://github.com/PCMDI/input4MIPs_CVs/pull/146**

## Key contacts

- Names: Margreet van Marle, Guido van der Werf
- Emails: Margreet.vanMarle@Deltares.nl; Guido.vanderWerf@wur.nl

## Summary

<!--- begin-cmip7-phases-source-ids -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->
### Source IDs for CMIP7 phases

The source ID that identifies the dataset to use in the different phases of CMIP7 is given below.

#### CMIP7 AR7 fast track

For the CMIP7 AR7 fast track phase of CMIP7, use data with the source ID [DRES-CMIP-BB4CMIP7-2-0](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22DRES-CMIP-BB4CMIP7-2-0%22%5D%7D)

This data is for the CMIP7 AR7 fast track.
All data sets for use in the fast track are published with a `mip_era` metadata value of 'CMIP7'.
This metadata value appears in both the file's global metadata as well as its metadata on ESGF.

If you find an issue, please
[create an issue on GitHub](https://github.com/PCMDI/input4MIPs_CVs/issues/new?template=data_issue.md)
so that the identification and resolution of this issue is publicly accessible.

#### Testing

For the testing phase of CMIP7, use data with the source ID [DRES-CMIP-BB4CMIP7-1-0](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22DRES-CMIP-BB4CMIP7-1-0%22%5D%7D)

This data is for testing (both of the forcing data and of modelling workflows) only.
Production simulations should not be started based on any data that has a `mip_era` value equal to 'CMIP6Plus'.
(The `mip_era` metadata value appears both in each file's global attributes as well as its metadata on ESGF.)

If you have any feedback, please add it to the [relevant GitHub discussion](https://github.com/PCMDI/input4MIPs_CVs/discussions).

#### CMIP7

No data available for this phase yet.

This data will be for CMIP7.
All data sets for use in CMIP7 will be published with a `mip_era` metadata value of 'CMIP7'.
This metadata value will appear both in the file's global metadata as well as its metadata on ESGF.

Further details will follow after the fast track is underway
(including details about how updates to this data will be handled over the lifetime of CMIP7).

<!--- end-cmip7-phases-source-ids -->

<!--- placeholder for piControl recommendation -->
## Navigating the data

This documentation supports the Open Biomass Burning Emissions dataset 
developed for the Coupled Model Intercomparison Project (CMIP7) simulations. 
The dataset consists of:

* Monthly estimates of open biomass burning emissions (forests, grasslands, agricultural waste burning on fields, peatlands)
* Emission species: BC, OC, CO2, SO2, N2O, NOx, NH3, CH4, CO, NMVOC, H2
* NMVOC consists of the sum of: 
  C2H6, CH3OH, C2H5OH, C3H8, C2H2, C2H4, C3H6, C5H8, C10H16, C7H8, C6H6, C8H10, 
  Toluenelump, HigherAlkenes, HigherAlkanes, CH2O, C2H4O, C3H6O, C2H6S, HCN, HCOOH, CH3COOH, MEK, CH3COCHO, HOCH2CHO. 
  These NMVOCs are also provided separately.
* Partitioning of bulk emissions related to different sectoral emissions. 
  The different sectors are: SAVA (Savanna, grassland, and shrubland fires), 
  BORF (Boreal forest fires), 
  TEMF (Temperature forest fires), 
  DEFO (Tropical forest fires [deforestation and degradation]), 
  PEAT (Peat fires), 
  AGRI (Agricultural waste burning)

### Data sources

The BB4CMIP historic biomass burning emissions dataset 
starting from January 1750 merges satellite records with several existing proxies (visibility, charcoal data) 
and utilizes the average of six models from the Fire Model Intercomparison Project (FireMIP) protocol 
to estimate emissions when proxy coverage is limited. 
Figure 1 and Figure 2 provide more information on which proxies were used in various basis regions to construct the full time series. 
This has been further explained in Van Marle et al. (2017, https://doi.org/10.5194/gmd-10-3329-2017).

[TODO figures here]

### Recommendation for pre-industrial control

Apply the 1850 values on repeat.

<!--- end of placeholder for piControl recommendation -->

<!--- begin-revision-history -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->
## Revision history

### DRES-CMIP-BB4CMIP7-1-0

DRES-CMIP-BB4CMIP7-2-0 extends DRES-CMIP-BB4CMIP7-1-0 to 2023. Hence DRES-CMIP-BB4CMIP7-1-0 is
retracted.

<!--- end-revision-history -->
