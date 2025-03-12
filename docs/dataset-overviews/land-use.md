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

Apply the 1850 land-use state as a constant.
Do not apply any land-use change or other management.

<!--- end of placeholder for piControl recommendation -->

<!--- begin-revision-history -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->
## Revision history

### UofMD-landState-3-0

v3.0 contains a number of spurious spikes post-1950. These have been addressed in v3.1. As a result,
v3.0 has been retracted.

<!--- end-revision-history -->
