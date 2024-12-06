<!--- These values are used by `fill-out-auto-generated-sections.py` -->
<!--- forcing="Anthropogenic short-lived climate forcer (SLCF) and CO<sub>2</sub> emissions" -->
<!--- source_id_stub="CEDS-CMIP" -->
# Anthropogenic short-lived climate forcer (SLCF) and CO<sub>2</sub> emissions

**This section is a work in progress.**
**For a first draft, see https://github.com/PCMDI/input4MIPs_CVs/pull/146**

## Key contacts

- Names: Rachel Hoesly, Steve Smith
- Emails: rachel.hoesly@pnnl.gov; ssmith@pnnl.gov

## Summary

CEDS data is available for testing (see the section below).
However, note that CEDS' testing data is published under multiple source IDs.
For everything except aircraft emissions, bulk NMVOCs and speciatated NMVOCs, 
use the source ID "CEDS-CMIP-2024-11-25".
For aircraft emissions and speciatated NMVOCs, use the source ID "CEDS-CMIP-2024-10-21".
It is also worth noting that solid biofuel emissions and speciatated NMVOCs 
have the suffix "-supplemental" added to their source ID
(to avoid inadvertent double counting).

<!--- begin-cmip7-phases-source-ids -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->
### Source IDs for CMIP7 phases

The source ID that identifies the dataset to use in the different phases of CMIP7 is given below.

#### Testing

For the testing of CMIP7, you will need data from the following source IDs:

- [CEDS-CMIP-2024-10-21](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%22CEDS-CMIP-2024-10-21%22%7D)
- [CEDS-CMIP-2024-11-25](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%22CEDS-CMIP-2024-11-25%22%7D).

Retrieving and only using valid data will require some care.
Please make sure you read the guidance given at the start of this Summary section
and process the data carefully.

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

<!--- placeholder for piControl recommendation -->
## Navigating the data

### Recommendation for pre-industrial control

Apply the 1850 values on repeat.

<!--- end of placeholder for piControl recommendation -->

<!--- begin-revision-history -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->
<!--- No revisions, hence section is blank -->
<!--- end-revision-history -->
