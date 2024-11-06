# Greenhouse gas concentrations

## Key contacts

- Names: Zebedee Nicholls, Malte Meinshausen
- Emails: zebedee.nicholls@climate-resource.com; malte.meinshausen@climate-resource.com

## Summary

A first version of the greenhouse gas concentrations is 
[available on the ESGF](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22CR-CMIP-0-3-0%22%7D).
This version is for testing only, do not use it for any simluations you're not willing to throw away.
We are collecting bugs in [this discussion](https://github.com/PCMDI/input4MIPs_CVs/discussions/144)
and aim to release a new version which addresses these bugs in December 2025.
If you find any other issues, please add them to
[the discussion](https://github.com/PCMDI/input4MIPs_CVs/discussions/144).

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
and compared to CMIP6 here: https://github.com/climate-resource/CMIP6-vs-CMIP7-GHG-Concentrations.

## Differences from CMIP6 or other previous versions

### File formats and naming

The file formats are generally close to CMIP6.
There are two key changes:

1. we have split the global-mean and hemispheric-mean data into separate files.
   In CMIP6, this data was in the same file (with a grid label of `GMNHSH`).
   We have split this for two reasons: 
   a) `GMNHSH` is not a grid label recognised in the CMIP CVs and
   b) having global-mean and hemispheric-mean data in the same file required us to introduce a 'sector' co-ordinate, 
      which was confusing and does not follow the CF-conventions.
1. we have simplified the names of all the variables.
   They are now simply the names of the gases,
   for example we now use "co2" rather than "mole_fraction_of_carbon_dioxide"
   (if helpful, a full mapping is here: https://github.com/climate-resource/CMIP6-vs-CMIP7-GHG-Concentrations/blob/main/notebooks/100_compare-global-annual-means.py)

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

### Data

At present, there are a number of changes from CMIP6.
The CMIP6 data can be found 
[on the ESGF under the "CMIP6" project and source ID "UoM-CMIP-1-2-0"](https://aims2.llnl.gov/search?project=input4MIPs&activeFacets=%7B%22source_id%22%3A%22UoM-CMIP-1-2-0%22%2C%22mip_era%22%3A%22CMIP6%22%7D).
As we fix the various issues, we expect these changes to reduce.
From [the analysis done to date](https://github.com/climate-resource/CMIP6-vs-CMIP7-GHG-Concentrations),
there are small changes in CO<sub>2</sub>, CH<sub>4</sub> and N<sub>2</sub>O
(the most radiatively active species alongside CFC12)
so we expect only small differences in the radiative impact of these changes in forcings.
We will expand this section as we do more analysis 
and create new versions of the dataset between now and the end of 2024.

<!--- begin-revision-history:CR-CMIP -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->
<!--- No revisions, hence section is blank -->
<!--- end-revision-history -->
