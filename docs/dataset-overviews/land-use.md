<!--- These values are used by `fill-out-auto-generated-sections.py` -->
<!--- forcing="land_use" -->
<!--- source_id_stub="UofMD-landState" -->
# Land use

## Key contacts

- Names: Louise Chini, George Hurtt
- Emails: lchini@umd.edu; gchurtt@umd.edu

## Summary

<!--- begin-cmip7-phases-source-ids -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->
### Source IDs for CMIP7 phases

The source ID that identifies the dataset to use in CMIP7 is given below.

#### CMIP7

For the CMIP7 AR7 fast track phase of CMIP7, use data with the source ID [UofMD-landState-3-1](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22UofMD-landState-3-1%22%5D%7D)

#### Testing

For the testing phase of CMIP7, use data with the source ID [UofMD-landState-3-0](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22UofMD-landState-3-0%22%5D%7D)

This data is for testing (both of the forcing data and of modelling workflows) only.
Production simulations should not be started based on any data that has a `mip_era` value equal to 'CMIP6Plus'.
(The `mip_era` metadata value appears both in each file's global attributes as well as its metadata on ESGF.)

If you have any feedback, please add it to the [relevant GitHub discussion](https://github.com/PCMDI/input4MIPs_CVs/discussions).

<!--- end-cmip7-phases-source-ids -->

<!--- placeholder for piControl recommendation -->
## Navigating the data

### Recommendation for pre-industrial control

Apply the 1850 land-use state on repeat.

### Grids and frequencies provided

We provide 4 data files, each spanning a global domain. 

1.	multiple-states: annual fractions of 0.25 degree grid-cells occupied by each of 13 different land-use states 
2.	multiple-transitions: annual fractions of 0.25 degree grid-cells transitioning 
    from each of the 13 different land-use states to the other 12 land-use states, as well as wood harvest
3.	multiple-management: annual information, at 0.25 degree spatial resolution, 
    about multiple different land-management variables
4.	multiple-static: supporting information that does not vary with time, at 0.25 degree spatial resolution

### Variables provided

#### States

We provide gridded information about 13 different land-use states:

- 5 crop functional types: C3 annuals (c3ann), C4 annuals (c4ann), C3 perennials (c3per), C4 perennials (c4per), and C3 nitrogen-fixers (c3nfx)
- 2 grazing land types: managed pasture (pastr) and rangeland (range)
- Urban land (urban)
- 2 primary land types: primary forest (primf) and primary non-forest (primn)
- 2 secondary land types: secondary forest (secdf) and secondary non-forest (secdn)
- Forest plantations (pltns): note that for LUH3 V1 this variable contains zeros only. We anticipate that additional information about historical plantations will be provided in subsequent updates.

In addition, the multiple-states file also provides gridded information 
for secondary mean age (secma) and secondary mean biomass density (secmb).

#### Transitions

Annual, gridded land-use transitions are provided between all combinations of land-use states. 
In addition, 6 types of wood harvest transitions are provided separately, 
both in terms of harvested area and harvested biomass/carbon:

- Primary forest harvest area (primf_harv) and biomass (primf_bioh)
- Primary non-forest harvest area (primn_harv) and biomass (primn_bioh)
- Secondary mature forest harvest area (secmf_harv) and biomass (secmf_bioh)
- Secondary young forest harvest area (secyf_harv) and biomass (secyf_bioh)
- Secondary non-forest harvest area (secnf_harv) and biomass (secnf_bioh)
- Plantation forest harvest area (pltns_harv) and biomass (pltns_bioh)

#### Gridded Management

- Irrigated fraction of cropland area, by croptype (irrig_c3ann, irrig_c4ann, irrig_c3per, irrig_c4per, irrig_c3nfx) 
- Fertilizer application rates, by croptype (fertl_c3ann, fertl_c4ann, fertl_c3per, fertl_c4per, fertl_c3nfx) 
- Flooded fraction of C3 annuals area (flood)
- Fraction of each croptype used for first-generation biofuel crops (cpbf1_c3ann, cpbf1_c4ann, cpbf1_c3per, cpbf1_c4per, cpbf1_c3nfx)
- Fraction of each croptype used for second-generation biofuel crops (cpbf2_c3ann, cpbf2_c4ann, cpbf2_c3per, cpbf2_c4per, cpbf2_c3nfx)
- Fraction of plantations area used for second-generation biofuel crops (pltns_bfuel)
- Fraction of wood harvest carbon used for industrial roundwood (rndwd), fuelwood (fulwd), and commercial biofuels (combf)
- Fraction of forested and non-forest vegetation areas that are protected from direct human activity (prtct_primf, prtct_primn, prtct_secdf, prtct_secdn, prtct_pltns)
- Added tree cover for afforestation (addtc)

#### Static

- Country codes (ccode)
- Grid-cell area (carea)
- Potential biomass density of natural vegetation (ptbio)
- Forest/non-forest mask for potential vegetation type (fstnf)
- Ice/water fraction of each grid-cell (icwtr)

### Uncertainty

Uncertainty is difficult to quantify for these land-use variables 
and at present we provide no analysis of the uncertainty associated with these datasets. 
For previous dataset releases we have provided alternative historical land-use reconstructions 
based on “high” or “low” assumptions about human land-use needs. 
Those alternative datasets can still be used to help quantify a "reasonable range" of land-use activity over the historical period.
It is also worth noting that the uncertainty in these reconstructions increases as we go further back in time, 
as we start to rely increasingly on simple assumptions about per capita land-use needs and estimates of historical populations.

## Differences from CMIP6 or other previous versions

### File formats and naming

The file formats are generally similar to those provided for CMIP6. 
The spatial and temporal resolution remains the same. 
The data begins in the year 850, as it did in the CMIP6 version. 
Variable names within each file remain the same, with a few key exceptions:

1. There is a new land-use variable/state (pltns) in this version that represents plantation forests. 
   The land-use transitions file also provides all transitions into and out-of this state, along with wood harvest of plantations. 
   However, for now all plantations-related variables in the historical period contain only zeros since these variables 
   are just placeholders for future updates and to harmonize with those variables in future scenarios from ScenarioMIP.
2. For CMIP7, the management variables related to biofuel crops are 
   cpbf1_c3ann, cpbf1_c4ann, crpbf1_c3per, cpbf1_c4per, cpbf1_c3nfx 
   (providing the fraction of each crop type used for first-generation biofuel crops) 
   as well as cpbf2_c3ann, cpbf2_c4ann, crpbf2_c3per, cpbf1_c4per, cpbf1_c3nfx 
   (providing the fraction of each crop type used for second-generation biofuel crops). 
   In addition the variable pltns_bfuel provides the area of forest plantations used for biofuels. 
   These variables differ from the previously-provided management variables for CMIP6, 
   which included crpbf_c3ann, crpbf_c4ann, crpbf_c3per, crpbf_c4per, crpbf_c3nfx 
   (representing the fraction of each crop type used for first-generation biofuel crops), 
   as well as crpbf_total, which provided the fraction of total cropland area used for second-generation biofuel crops. 
3. There are also some additional new land management variables for LUH3/CMIP7, 
   including addtc (which provides the area of added tree cover for afforestation), 
   and several variables that give the fraction of land-use area, by land-use type, 
   protected from future human activity (prtct_primf, prtct_primn, prtct_secdf, prtct_secdn, prtct_pltns).
4. The time dimension now provides days since 0850-01-01 00:00:00 
   so those values are likely to be different to those in previous versions of LUH
   (which was in years since 0850).

### Data

The LUH3 data for CMIP7 Fast Track is very similar to the LUH2 data provided for CMIP6. 
Since LUH3 is built upon the recent land-use dataset created for Global Carbon Budget (i.e. LUH2-GCB2024), 
it has considerable similarity with that product, especially for the years prior to 1950. 
Aside from the file format and variable differences listed above, 
there are a few some notable differences in the land-use information between LUH3 and LUH2:

1. LUH3 for CMIP7 fast track uses new land-use inputs from the HYDE 3.4 dataset (https://landuse.sites.uu.nl/hyde-project/). 
   This includes new remote sensing data for regions of importance for the carbon cycle such as Brazil, Indonesia, and China.
2. Although the new HYDE data contains several important updates and improvements, 
   the new annual temporal resolution results in large inter-annual fluctuations in land-use transitions. 
   To reduce the impacts of these fluctuations, we have resampled the HYDE data every 10 years from 1700 to present day, 
   and then linearly interpolated between those sampled points to generate annual values. 
   This is consistent with the approach used in LUH2 for data years prior to 2000 
   and also provides a more consistent treatment of time resolution through-out the dataset.
3. New FAO data is used to specify national wood harvest demands. 
   This results in slightly different spatial patterns of wood harvesting.

<!--- end of placeholder for piControl recommendation -->

<!--- begin-revision-history -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->
## Revision history

### UofMD-landState-3-0

v3.0 contains a number of spurious spikes post-1950. These have been addressed in v3.1. As a result,
v3.0 has been retracted.

<!--- end-revision-history -->
