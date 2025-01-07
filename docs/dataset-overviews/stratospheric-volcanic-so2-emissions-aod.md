<!--- These values are used by `fill-out-auto-generated-sections.py` -->
<!--- forcing="Stratospheric volcanic SO<sub>2</sub> emissions and aerosol optical properties" -->
<!--- source_id_stub="UOEXETER-CMIP" -->
# Stratospheric volcanic SO<sub>2</sub> emissions and aerosol optical properties

**This section is a work in progress.**
**For a first draft, see https://github.com/PCMDI/input4MIPs_CVs/pull/146**

## Key contacts

- Names: Thomas Aubry
- Emails: t.aubry@exeter.ac.uk

Testing versions of the stratospheric volcanic SO<sub>2</sub> emissions
and aerosol optical properties are
[available on the ESGF](https://aims2.llnl.gov/search?project=input4MIPs&activeFacets=%7B%22mip_era%22%3A%22CMIP6Plus%22%2C%22institution_id%22%3A%22uoexeter%22%7D).
These versions are for testing only, do not use them for any simluations you're not willing to throw away.

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

The source ID that identifies the dataset to use in the different phases of CMIP7 is given below.

#### Testing

For the testing phase of CMIP7, use data with the source ID [UOEXETER-CMIP-1-2-0](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%22UOEXETER-CMIP-1-2-0%22%7D)

This data is for testing (both of the forcing data and of modelling workflows) only.
Production simulations should not be started based on any data that has a `mip_era` value equal to 'CMIP6Plus'.
(The `mip_era` metadata value appears both in each file's global attributes as well as its metadata on ESGF.)

If you have any feedback, please add it to the [relevant GitHub discussion](https://github.com/PCMDI/input4MIPs_CVs/discussions).

#### CMIP7 AR7 fast track

No data available for this phase yet.

This data will be for the CMIP7 AR7 fast track.
All data sets for use in the fast track will be published with a `mip_era` metadata value of 'CMIP7'.
This metadata value will appear both in the file's global metadata as well as its metadata on ESGF.

Further details will follow in early 2025.

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

There are dedicated pre-industrial control files.
These files have `fx` in their name
(`fx` stands for fixed, which is used
because the pre-industrial control file is a fixed field,
custom for the pre-industrial control experiment).

### Grids and frequencies provided

The volcanic emissions are provided with daily resolution
alongside latitude, longitude and injection height information.

The aerosol optical properties are provided with monthly resolution
on a latitudinal grid.

### Variables provided

The mass of SO<sub>2</sub> associated with eruptions of different volcanoes is provided.

Alongside the emissions information, aerosol optical properties are also provided.
For example, extinction coeffecients and aerosol optical depth.

### Uncertainty

There is considerable uncertainty in the magnitude of eruptions,
particularly before the satellite era.
This uncertainty is not reported in the data, but could be in future.
The uncertainty in the magnitude of eruptions is still relatively large,
even in surface temperature terms,
where it could be up to 20% of the anthropogenic warming (so roughly around 0.2K).

## Differences from CMIP6 or other previous versions

### File formats and naming

The file formats are quite different from CMIP6 
because the data is coming from a different provider.
The naming may also be different.
Overall, we would say that the data is more uniform now
and in line with other input4MIPs data and conventions.

### Data

For a full dive into the changes from CMIP6, see 
[the external documentation](https://docs.google.com/document/d/1blX5kv0We1BteqWzMKs0OuhazAcAonay/edit?usp=sharing&ouid=104358532925985160745&rtpof=true&sd=true).

<!--- begin-revision-history -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->
## Revision history

### UOEXETER-CMIP-1-1-3

v1.2.0 includes climatology data (for piControl simulations) and updates the handling of small
eruptions.Hence v1.1.3 is retracted.

<!--- end-revision-history -->
