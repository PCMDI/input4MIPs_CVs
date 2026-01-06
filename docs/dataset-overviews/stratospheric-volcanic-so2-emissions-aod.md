<!--- These values are used by `fill-out-auto-generated-sections.py` -->
<!--- forcing="volcanic" -->
<!--- source_id_stub="UOEXETER" -->
# Stratospheric volcanic SO<sub>2</sub> emissions and aerosol optical properties

## Key contacts

- Names: Thomas Aubry
- Emails: t.aubry@exeter.ac.uk

The CMIP7 version of the volcanic forcing dataset has been released.
Documentation on the dataset is hosted
[externally](https://docs.google.com/document/d/1blX5kv0We1BteqWzMKs0OuhazAcAonay/edit?usp=sharing&ouid=104358532925985160745&rtpof=true&sd=true).
This contains a detailed dive into the data.
In contrast, this page provides an overview and some key, CMIP-specific information.

If you find any issues, please contribute to
[the discussion on GitHub](https://github.com/PCMDI/input4MIPs_CVs/discussions/175).

## Summary

<!--- begin-cmip7-phases-source-ids -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->
### Source IDs for CMIP7 phases

The source ID that identifies the dataset to use in CMIP7 is given below.

#### DECK

##### CMIP7

For the DECK simulations in the production phase of CMIP7, use data with the source ID [UOEXETER-CMIP-2-2-1](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22UOEXETER-CMIP-2-2-1%22%7D)

The data has the DOI: [10.25981/ESGF.input4MIPs.CMIP7/2522673](https://doi.org/10.25981/ESGF.input4MIPs.CMIP7/2522673).

This data is for use in CMIP7 production simulations.
All data sets for use in CMIP7 production simulations are published with a `mip_era` metadata value of 'CMIP7'.
This metadata value appears both in the file's global metadata as well as its metadata on ESGF.

If you find an issue, please
[create an issue on GitHub](https://github.com/PCMDI/input4MIPs_CVs/issues/new?template=data_issue.md)
so that the identification and resolution of this issue is publicly accessible.

##### Testing

For the DECK simulations in the testing phase of CMIP7, use data with the source ID [UOEXETER-CMIP-1-3-1](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22UOEXETER-CMIP-1-3-1%22%7D)

No DOIs are available for this data.

This data is for testing (both of the forcing data and of modelling workflows) only.
Production simulations should not be started based on any data that has a `mip_era` value equal to 'CMIP6Plus'.
(The `mip_era` metadata value appears both in each file's global attributes as well as its metadata on ESGF.)

If you have any feedback, please add it to the [relevant GitHub discussion](https://github.com/PCMDI/input4MIPs_CVs/discussions).

#### ScenarioMIP

##### CMIP7

For the ScenarioMIP simulations in the production phase of CMIP7, use data with the source ID [UOEXETER-ScenarioMIP-2-2-2](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22UOEXETER-ScenarioMIP-2-2-2%22%7D)

No DOIs are available for this data.

This data is for use in CMIP7 production simulations.
All data sets for use in CMIP7 production simulations are published with a `mip_era` metadata value of 'CMIP7'.
This metadata value appears both in the file's global metadata as well as its metadata on ESGF.

If you find an issue, please
[create an issue on GitHub](https://github.com/PCMDI/input4MIPs_CVs/issues/new?template=data_issue.md)
so that the identification and resolution of this issue is publicly accessible.

##### Testing

No data available for this phase yet.

<!--- end-cmip7-phases-source-ids -->

## Navigating the data

### Recommendation for pre-industrial control

There are dedicated pre-industrial control files for aerosol optical properties.
For aerosol optical properties, these are provided as climatologies
and hence have `monC` in their name
(they also have a time axis with only twelve points, so they're hard to miss).
There is no recommendation for teams who want to run pre-industrial control
with volcanic emissions as yet, that is still being developed
in collaboration with early testing teams who are interested in this application.

For full details, see
[the external documentation](https://docs.google.com/document/d/1blX5kv0We1BteqWzMKs0OuhazAcAonay/edit?usp=sharing&ouid=104358532925985160745&rtpof=true&sd=true).

### Grids and frequencies provided

The volcanic emissions are provided with daily resolution
alongside latitude, longitude and injection height information.

The aerosol optical properties are provided with monthly resolution
on a latitudinal, vertical and wavelength grid.
To facilitate use of our dataset in any radiative model,
we provide the community with scripts
(see [this associated Github repository](https://github.com/MetOffice/CMIP7_volcanic_aerosol_forcing/tree/main))
that can be used to interpolate the files we provide on ESGF on any list of wavelength inputted by the user.
These include a simple method to linearly interpolate to waveband midpoints
and a weighted averaging method that is more computationally expensive
but provides more representative averages, particularly for radiation schemes with broad wavebands.
We therefore recommend modelling groups use the latter method where possible.

### Variables provided

For the aerosol optical properties dataset,
the extinction, single scattering albedo, scattering asymmetry factor,
effective radius, surface area density and volume density are provided.
For emissions, the volcanic SO<sub>2</sub> injection time,
latitude, longitude, height, depth and mass are provided.
Further details are provided in
[the external documentation](https://docs.google.com/document/d/1blX5kv0We1BteqWzMKs0OuhazAcAonay/edit?usp=sharing&ouid=104358532925985160745&rtpof=true&sd=true)
(section III and IV).

### Uncertainty

There is considerable uncertainty in the magnitude
and height of volcanic SO<sub>2</sub> injection for the satellite era.
These uncertainties are even larger in the pre-satellite era,
for which there is considerable uncertainty
on the occurence, timing and location of volcanic SO<sub>2</sub> injections.
These uncertainties propagate to our aerosol optical properties dataset for the pre-satellite era.
Uncertainties are currently not reported in the dataset but they will be in the future.

## Differences from CMIP6 or other previous versions

### File formats and naming

The file formats are quite different from CMIP6
because the data is coming from a different provider.
The naming may also be different.
Overall, we would say that the data is more uniform now
and in line with other input4MIPs data and conventions.
We do not have a direct mapping/translation guide at this stage
(although there is some detail in
[the external documentation](https://docs.google.com/document/d/1blX5kv0We1BteqWzMKs0OuhazAcAonay/edit?usp=sharing&ouid=104358532925985160745&rtpof=true&sd=true)).

### Data

For a full dive into the changes from CMIP6, see
[the external documentation](https://docs.google.com/document/d/1blX5kv0We1BteqWzMKs0OuhazAcAonay/edit?usp=sharing&ouid=104358532925985160745&rtpof=true&sd=true).

<!--- begin-revision-history -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->
## Revision history

### UOEXETER-CMIP-2-0-0

v2.2.1 resolves issues with NaN values in v2.0.0 and updates a few other issues (notably the
latitudinal distrbution of the Agung eruption). These updates affect both the historical values and
the pre-industrial climatologies. As a result of this change, v2.0.0 is deprecated. Please restart
any simulations that used v2.0.0 and use v2.2.1 instead.

### UOEXETER-CMIP-1-3-1

v2.0.0 includes the following key updates: i) new H2SO4 number density variable replacing aerosol
number density; ii) correction to the 1920-1978 ice-core dataset, improving consistency with
pyrheliometer measurements and CMIP6. As a result of this change, the mean historical SAOD has
decreased a bit, but it is still higher than CMIP6. Hence v1.3.1 is deprecated.

### UOEXETER-CMIP-1-3-0

v1.3.1 does minor plus updates and adds the aerosol number density requested by some modelling
groups. Hence v1.3.0 is deprecated.

### UOEXETER-CMIP-1-2-0

v1.3.0 updates the handling of small eruptions in the pre-satellite era. Hence v1.2.0 is deprecated.

### UOEXETER-CMIP-1-1-3

v1.2.0 includes climatology data (for piControl simulations) and updates the handling of small
eruptions. Hence v1.1.3 is deprecated.

<!--- end-revision-history -->
