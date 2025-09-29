<!--- These values are used by `fill-out-auto-generated-sections.py` -->
<!--- forcing="ghg_concentrations" -->
<!--- source_id_stub="CR" -->
# Greenhouse gas concentrations

## Key contacts

- Names: Zebedee Nicholls, Malte Meinshausen
- Emails: zebedee.nicholls@climate-resource.com; malte.meinshausen@climate-resource.com

## Summary

The CMIP7 version of the greenhouse gas concentration dataset
for the DECK simulations has been released.
**Test** data is available for the ScenarioMIP simulations.
If you find any problems,
please [raise an issue](https://github.com/PCMDI/input4MIPs_CVs/issues/new?template=data_issue.md).
Discussions on this version can be found in
[https://github.com/PCMDI/input4MIPs_CVs/discussions/235](https://github.com/PCMDI/input4MIPs_CVs/discussions/235).

<!--- begin-cmip7-phases-source-ids -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->
### Source IDs for CMIP7 phases

The source ID that identifies the dataset to use in CMIP7 is given below.

#### DECK

##### CMIP7

For the DECK simulations in the production phase of CMIP7, use data with the source ID [CR-CMIP-1-0-0](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22CR-CMIP-1-0-0%22%7D)

The data has the DOI: [https://doi.org/10.5281/zenodo.14892947](https://doi.org/10.5281/zenodo.14892947).

This data is for use in CMIP7 production simulations.
All data sets for use in CMIP7 production simulations are published with a `mip_era` metadata value of 'CMIP7'.
This metadata value appears both in the file's global metadata as well as its metadata on ESGF.

If you find an issue, please
[create an issue on GitHub](https://github.com/PCMDI/input4MIPs_CVs/issues/new?template=data_issue.md)
so that the identification and resolution of this issue is publicly accessible.

##### Testing

For the DECK simulations in the testing phase of CMIP7, use data with the source ID [CR-CMIP-0-4-0](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22CR-CMIP-0-4-0%22%7D)

The data has the DOI: [10.5281/zenodo.13365838](https://doi.org/10.5281/zenodo.13365838).

This data is for testing (both of the forcing data and of modelling workflows) only.
Production simulations should not be started based on any data that has a `mip_era` value equal to 'CMIP6Plus'.
(The `mip_era` metadata value appears both in each file's global attributes as well as its metadata on ESGF.)

If you have any feedback, please add it to the [relevant GitHub discussion](https://github.com/PCMDI/input4MIPs_CVs/discussions).

#### ScenarioMIP

##### CMIP7

No data available for this phase yet.

##### Testing

For the scenariomip simulations in the testing phase of CMIP7, you will need data from the following source IDs:

- [CR-vllo-0-1-0](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22CR-vllo-0-1-0%22%7D)
- [CR-vlho-0-1-0](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22CR-vlho-0-1-0%22%7D)
- [CR-l-0-1-0](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22CR-l-0-1-0%22%7D)
- [CR-ml-0-1-0](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22CR-ml-0-1-0%22%7D)
- [CR-m-0-1-0](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22CR-m-0-1-0%22%7D)
- [CR-hl-0-1-0](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22CR-hl-0-1-0%22%7D)
- [CR-h-0-1-0](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22CR-h-0-1-0%22%7D).


The data has the DOI: [dev-test](https://doi.org/dev-test).

This data is for testing (both of the forcing data and of modelling workflows) only.
Production simulations should not be started based on any data that has a `mip_era` value equal to 'CMIP6Plus'.
(The `mip_era` metadata value appears both in each file's global attributes as well as its metadata on ESGF.)

If you have any feedback, please add it to the [relevant GitHub discussion](https://github.com/PCMDI/input4MIPs_CVs/discussions).

<!--- end-cmip7-phases-source-ids -->

## Navigating the data

### Recommendation for pre-industrial control

Use the 1850 value, apply this as a constant
(which will be a single value if you use annual-mean data
and will include a seasonal cycle if you use monthly-mean data).

### Grids and frequencies provided

We provided five combinations of grids and frequencies.
These are all available on the ESGF.

1. global-, annual-mean concentrations (grid label, `gm`, frequency, `yr`)
1. global-, monthly-mean concentrations (grid label, `gm`, frequency, `mon`)
1. hemispheric-, annual-mean concentrations (grid label, `gr1z`, frequency, `yr`)
1. hemispheric-, monthly-mean concentrations (grid label, `gr1z`, frequency, `mon`)
1. 15-degree latitudinal, monthly-mean concentrations (grid label, `gnz`, frequency, `mon`)

We are also able to produce a 0.5-degree latitudinal grid.
If this is something that would be of interest, 
please [raise an issue](https://github.com/PCMDI/input4MIPs_CVs/issues/new)
and tag `@znichollscr`.

### Species provided

We provide concentrations for 43 greenhouse gas concentrations and species,
as well as three equivalent species.

#### Equivalence species

For most models, you will not use all 43 species.
As a result, we provide equivalence species too.
There are two options if you don't want to use all 43 species in your model.

##### Option 1

Use CO<sub>2</sub>, CH<sub>4</sub>, N<sub>2</sub>O and CFC12 directly in your model.
Use CFC11eq (i.e. CFC11-equivalent) to capture the radiative effect of all other species.

##### Option 2

Use CO<sub>2</sub>, CH<sub>4</sub> and N<sub>2</sub>O directly in your model.
Use CFC12eq (i.e. CFC12-equivalent) to capture the radiative effect of all ozone depleting substances (ODSs)
and HFC134aeq (i.e. HFC134a-equivalent) to capture the radiative effect of all other fluorinated gases.

### Uncertainty

At present, we provide no analysis of the uncertainty associated with these datasets.
In radiative forcing terms, the uncertainty in these concentrations 
is very likely to be small compared to other uncertainties in the climate system,
but this statement is not based on any robust analysis 
(rather it is based on expert judgement).
It is also worth noting that the uncertainty increases as we go further back in time,
particularly as we shift from using surface flasks to relying on ice cores instead.

### Examples of working with the data

If helpful, we show how the historical data can be downloaded from ESGF
and compared to CMIP6 here:
[https://github.com/climate-resource/CMIP6-vs-CMIP7-GHG-Concentrations](https://github.com/climate-resource/CMIP6-vs-CMIP7-GHG-Concentrations).

## Differences from CMIP6 or other previous versions

### File formats and naming

The file formats are generally close to CMIP6.
There are three key changes:

1. we have split the global-mean and hemispheric-mean data into separate files.
   In CMIP6, this data was in the same file (with a grid label of `GMNHSH`).
   We have split this for two reasons: 
   a) `GMNHSH` is not a grid label recognised in the CMIP CVs and
   b) having global-mean and hemispheric-mean data in the same file required us to introduce a 'sector' coordinate,
      which was confusing and does not follow the CF-conventions.
1. we have split the files into different time components.
   One file goes from year 1 to year 999 (inclusive).
   The next file goes from year 1000 to year 1749 (inclusive).
   The last file goes from year 1750 to year 2022 (inclusive).
   This simplifies handling and allows groups to avoid loading data
   they are not interested in (for CMIP, this generally means data pre-1750).
1. we have simplified the names of all the variables.
   They are now simply the names of the gases,
   for example we now use "co2" rather than "mole_fraction_of_carbon_dioxide".
   A full mapping is provided below .
   (but, a word of warning: this mapping is hard to check within the scope of this repo 
   so please be careful when using it)

There is one more minor change.
The data now starts in year one, rather than year zero.
We do this because year zero doesn't exist in most calendars
(and we want to avoid users of the data having to hack around this 
when using standard data analysis tools).

#### Variable name mapping

```python
CMIP6_TO_CMIP7_VARIABLE_MAP = {
    # name in CMIP6: name in CMIP7
    "mole_fraction_of_carbon_dioxide_in_air": "co2",
    "mole_fraction_of_methane_in_air": "ch4",
    "mole_fraction_of_nitrous_oxide_in_air": "n2o",
    "mole_fraction_of_c2f6_in_air": "c2f6",
    "mole_fraction_of_c3f8_in_air": "c3f8",
    "mole_fraction_of_c4f10_in_air": "c4f10",
    "mole_fraction_of_c5f12_in_air": "c5f12",
    "mole_fraction_of_c6f14_in_air": "c6f14",
    "mole_fraction_of_c7f16_in_air": "c7f16",
    "mole_fraction_of_c8f18_in_air": "c8f18",
    "mole_fraction_of_c_c4f8_in_air": "cc4f8",
    "mole_fraction_of_carbon_tetrachloride_in_air": "ccl4",
    "mole_fraction_of_cf4_in_air": "cf4",
    "mole_fraction_of_cfc11_in_air": "cfc11",
    "mole_fraction_of_cfc113_in_air": "cfc113",
    "mole_fraction_of_cfc114_in_air": "cfc114",
    "mole_fraction_of_cfc115_in_air": "cfc115",
    "mole_fraction_of_cfc12_in_air": "cfc12",
    "mole_fraction_of_ch2cl2_in_air": "ch2cl2",
    "mole_fraction_of_methyl_bromide_in_air": "ch3br",
    "mole_fraction_of_ch3ccl3_in_air": "ch3ccl3",
    "mole_fraction_of_methyl_chloride_in_air": "ch3cl",
    "mole_fraction_of_chcl3_in_air": "chcl3",
    "mole_fraction_of_halon1211_in_air": "halon1211",
    "mole_fraction_of_halon1301_in_air": "halon1301",
    "mole_fraction_of_halon2402_in_air": "halon2402",
    "mole_fraction_of_hcfc141b_in_air": "hcfc141b",
    "mole_fraction_of_hcfc142b_in_air": "hcfc142b",
    "mole_fraction_of_hcfc22_in_air": "hcfc22",
    "mole_fraction_of_hfc125_in_air": "hfc125",
    "mole_fraction_of_hfc134a_in_air": "hfc134a",
    "mole_fraction_of_hfc143a_in_air": "hfc143a",
    "mole_fraction_of_hfc152a_in_air": "hfc152a",
    "mole_fraction_of_hfc227ea_in_air": "hfc227ea",
    "mole_fraction_of_hfc23_in_air": "hfc23",
    "mole_fraction_of_hfc236fa_in_air": "hfc236fa",
    "mole_fraction_of_hfc245fa_in_air": "hfc245fa",
    "mole_fraction_of_hfc32_in_air": "hfc32",
    "mole_fraction_of_hfc365mfc_in_air": "hfc365mfc",
    "mole_fraction_of_hfc4310mee_in_air": "hfc4310mee",
    "mole_fraction_of_nf3_in_air": "nf3",
    "mole_fraction_of_sf6_in_air": "sf6",
    "mole_fraction_of_so2f2_in_air": "so2f2",
    "mole_fraction_of_cfc11eq_in_air": "cfc11eq",
    "mole_fraction_of_cfc12eq_in_air": "cfc12eq",
    "mole_fraction_of_hfc134aeq_in_air": "hfc134aeq",
}
```

### Data

The analysis of the differences in historical data from CMIP6 is done in 
[this repository](https://github.com/climate-resource/CMIP6-vs-CMIP7-GHG-Concentrations).
At present, the changes from CMIP6 are minor,
with the maximum difference in effective radiative forcing terms being 0.05 W / m^2
(and generally much smaller than this, particularly after 1850).
For reference, the CMIP6 data can be found 
[on the ESGF under the "CMIP6" project and source ID "UoM-CMIP-1-2-0"](https://aims2.llnl.gov/search?project=input4MIPs&activeFacets=%7B%22source_id%22%3A%22UoM-CMIP-1-2-0%22%2C%22mip_era%22%3A%22CMIP6%22%7D).

<!--- begin-revision-history -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->
## Revision history

### CR-CMIP-0-4-0

CR-CMIP-1-0-0 switches to much more conventional naming for gases. The affected gases are: c2f6
(previously pfc116), c3f8 (pfc218), c4f10 (pfc3110), c5f12 (pfc4112), c6f14 (pfc5114), c7f16
(pfc6116), c8f18 (pfc7118), cc4f8 (pfc318) and ch3ccl3 (hcc140a). A DOI is now also included in each
file. Please use it so we can track usage of these files. In terms of science, CR-CMIP-1-0-0 updates
to the latest ice core and AGAGE data, as well as using better data sources for HFC23, CF4, C2F6 and
C3F8 than CR-CMIP-0-4-0. CR-CMIP-1-0-0 also provides a smoother transition from ice core based
records to more recent records (i.e. flask and in-situ samples) and more sensible pre-industrial
values for gases with non-zero pre-industrial concentrations. It also uses the Scripps CO2 record to
handle the period from 1959  to the start of the flask and in-situ samples from other networks. The
CR-CMIP-1-0-0 dataset also provides much better information about the original data sources. As a
result, CR-CMIP-0-4-0 is deprecated. For the full CHANGELOG, see
[here](https://github.com/climate-resource/CMIP-GHG-Concentration-Generation/blob/main/CHANGELOG.md).
For basic analysis of the changes between versions, see [this
repo](https://github.com/climate-resource/CMIP6-vs-CMIP7-GHG-Concentrations).

### CR-CMIP-0-3-0

A number of bugs were identified in v0.3.0, see
[https://github.com/PCMDI/input4MIPs_CVs/discussions/144](). As far as we are aware, v0.4.0 fixes
all major bugs identified in v0.3.0. For the full list of updates since v0.3.0 (and before), see
[https://github.com/climate-resource/CMIP-GHG-Concentration-Generation/blob/main/CHANGELOG.md]().
For further analysis of the changes between versions, see
[https://github.com/climate-resource/CMIP6-vs-CMIP7-GHG-Concentrations]().

<!--- end-revision-history -->
