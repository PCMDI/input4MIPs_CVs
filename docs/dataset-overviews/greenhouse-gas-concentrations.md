<!--- These values are used by `fill-out-auto-generated-sections.py` -->
<!--- forcing="ghg_concentrations" -->
<!--- source_id_stub="CR-CMIP" -->
# Greenhouse gas concentrations

## Key contacts

- Names: Zebedee Nicholls, Malte Meinshausen
- Emails: zebedee.nicholls@climate-resource.com; malte.meinshausen@climate-resource.com

## Summary

Testing versions of the greenhouse gas concentrations are
[available on the ESGF](https://aims2.llnl.gov/search?project=input4MIPs&activeFacets=%7B%22mip_era%22%3A%22CMIP6Plus%22%2C%22dataset_category%22%3A%22GHGConcentrations%22%7D).
These versions are for testing only, do not use them for any simluations you're not willing to throw away.
If you find any issues, please 
[create an issue](https://github.com/PCMDI/input4MIPs_CVs/issues/new).

<!--- begin-cmip7-phases-source-ids -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->
### Source IDs for CMIP7 phases

The source ID that identifies the dataset to use in the different phases of CMIP7 is given below.

#### CMIP7 AR7 fast track

For the CMIP7 AR7 fast track phase of CMIP7, use data with the source ID [CR-CMIP-1-0-0](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22CR-CMIP-1-0-0%22%5D%7D)

This data is for the CMIP7 AR7 fast track.
All data sets for use in the fast track are published with a `mip_era` metadata value of 'CMIP7'.
This metadata value appears in both the file's global metadata as well as its metadata on ESGF.

If you find an issue, please
[create an issue on GitHub](https://github.com/PCMDI/input4MIPs_CVs/issues/new?template=data_issue.md)
so that the identification and resolution of this issue is publicly accessible.

#### Testing

For the testing phase of CMIP7, use data with the source ID [CR-CMIP-0-4-0](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22CR-CMIP-0-4-0%22%5D%7D)

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

We are also able to produce a 5-degree latitudinal grid.
If this is something that would be of interest, 
please [raise an issue](https://github.com/PCMDI/input4MIPs_CVs/issues/new)
and tag `@znichollscr`.

### Species provided

We provide concentrations for 43 greenhouse gas concentrations and species.

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

If helpful, we show how the data can be downloaded from ESGF
and compared to CMIP6 here: [https://github.com/climate-resource/CMIP6-vs-CMIP7-GHG-Concentrations]().

## Differences from CMIP6 or other previous versions

### File formats and naming

The file formats are generally close to CMIP6.
There are three key changes:

1. we have split the global-mean and hemispheric-mean data into separate files.
   In CMIP6, this data was in the same file (with a grid label of `GMNHSH`).
   We have split this for two reasons: 
   a) `GMNHSH` is not a grid label recognised in the CMIP CVs and
   b) having global-mean and hemispheric-mean data in the same file required us to introduce a 'sector' co-ordinate, 
      which was confusing and does not follow the CF-conventions.
1. we have split the files into different time components.
   One file goes from year 1 to year 999 (inclusive).
   The next file goes from year 1000 to year 1749 (inclusive).
   The last file goes from year 1750 to year 2022 (inclusive).
1. we have simplified the names of all the variables.
   They are now simply the names of the gases,
   for example we now use "co2" rather than "mole_fraction_of_carbon_dioxide"
   A full mapping is provided below 
   (but, a word of warning: this mapping is hard to check within the scope of this repo 
   so please be careful when using it)

There is one more minor change.
The data now starts in year one, rather than year zero.
We do this because year zero doesn't exist in most calendars
(and we want to avoid users of the data having to hack around this 
when using standard data analysis tools).
In a future version, 
we will also split our data into multiple files
(see [this comment](https://github.com/climate-resource/CMIP-GHG-Concentration-Generation/issues/29#issuecomment-2126359264)).
so if you don't care about data pre-1750, you don't need to load it from disk
(or worry about any of the calendard headaches that pre-1750 data introduces).

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

```python
CMIP7_TO_NORMAL_VARIABLE_MAP = {
    # name in CMIP7: 'normal' name
    # For CMIP7, we try to make use of CF-conventions standard names
    # as much as possible.
    # For ozone-depleting substances in particular, these are not 'normal' names
    # (e.g. CF-conventions uses hcc140a, most peoply call this ch3ccl3).
    'co2': 'co2',
    'ch4': 'ch4',
    'n2o': 'n2o',
    'pfc116': 'c2f6',
    'pfc218': 'c3f8',
    'pfc3110': 'c4f10',
    'pfc4112': 'c5f12',
    'pfc5114': 'c6f14',
    'pfc6116': 'c7f16',
    'pfc7118': 'c8f18',
    'pfc318': 'cc4f8',
    'ccl4': 'ccl4',
    'cf4': 'cf4',
    'cfc11': 'cfc11',
    'cfc113': 'cfc113',
    'cfc114': 'cfc114',
    'cfc115': 'cfc115',
    'cfc12': 'cfc12',
    'ch2cl2': 'ch2cl2',
    'ch3br': 'ch3br',
    'hcc140a': 'ch3ccl3',
    'ch3cl': 'ch3cl',
    'chcl3': 'chcl3',
    'halon1211': 'halon1211',
    'halon1301': 'halon1301',
    'halon2402': 'halon2402',
    'hcfc141b': 'hcfc141b',
    'hcfc142b': 'hcfc142b',
    'hcfc22': 'hcfc22',
    'hfc125': 'hfc125',
    'hfc134a': 'hfc134a',
    'hfc143a': 'hfc143a',
    'hfc152a': 'hfc152a',
    'hfc227ea': 'hfc227ea',
    'hfc23': 'hfc23',
    'hfc236fa': 'hfc236fa',
    'hfc245fa': 'hfc245fa',
    'hfc32': 'hfc32',
    'hfc365mfc': 'hfc365mfc',
    'hfc4310mee': 'hfc4310mee',
    'nf3': 'nf3',
    'sf6': 'sf6',
    'so2f2': 'so2f2',
    'cfc11eq': 'cfc11eq',
    'cfc12eq': 'cfc12eq',
    'hfc134aeq': 'hfc134aeq',
}
```

### Data

The analysis of the differences from CMIP6 is done in 
[this repository](https://github.com/climate-resource/CMIP6-vs-CMIP7-GHG-Concentrations).
At present, the changes from CMIP6 are minor,
with the maximum difference in effective radiative forcing terms being 0.02 W / m^2.
For reference, the CMIP6 data can be found 
[on the ESGF under the "CMIP6" project and source ID "UoM-CMIP-1-2-0"](https://aims2.llnl.gov/search?project=input4MIPs&activeFacets=%7B%22source_id%22%3A%22UoM-CMIP-1-2-0%22%2C%22mip_era%22%3A%22CMIP6%22%7D).

<!--- begin-revision-history -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->
## Revision history

### CR-CMIP-0-3-0

A number of bugs were identified in v0.3.0, see
[https://github.com/PCMDI/input4MIPs_CVs/discussions/144](). As far as we are aware, v0.4.0 fixes
all major bugs identified in v0.3.0. For the full list of updates since v0.3.0 (and before), see
[https://github.com/climate-resource/CMIP-GHG-Concentration-Generation/blob/main/CHANGELOG.md]().
For further analysis of the changes between versions, see
[https://github.com/climate-resource/CMIP6-vs-CMIP7-GHG-Concentrations]().

<!--- end-revision-history -->
