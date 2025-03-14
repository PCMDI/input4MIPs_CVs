<!--- These values are used by `fill-out-auto-generated-sections.py` -->
<!--- forcing="amip-ssts" -->
<!--- source_id_stub="PCMDI-AMIP" -->
# AMIP sea-surface temperature and sea-ice boundary forcing

## Key contacts

- Names: Paul J. Durack
- Emails: durack1@llnl.gov

## Summary

<!--- begin-cmip7-phases-source-ids -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->
### Source IDs for CMIP phases

The source ID that identifies the dataset to use is given below.

#### CMIP7

**an issue has been identified in the PCMDI-AMIP-1-1-9 sea ice field for the dataset last month (2022-12).
A resolution is currently being investigated, and a revised dataset `PCMDI-AMIP-1-1-10` will be made available
in April with this issue resolved. No other data changes are planned. The `mip_era` will be incremented
to `CMIP7`.**

<!--
For CMIP7, use data with the source ID [PCMDI-AMIP-1-1-9](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22PCMDI-AMIP-1-1-9%22%5D%7D)
-->
The PCMDI-AMIP-1-1-9 dataset provides temporal coverage 1850-01 through 2022-12, and maintains consistency
with the previous CMIP6 dataset versions [(versions 1.1.0 through 1.1.8](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22mip_era%22%3A%22CMIP6%22%2C%22institution_id%22%3A%22PCMDI%22%7D)).

Upstream data used to produce the PCMDI-AMIP data product was discontinued in February 2023 (NOAA-OISST v2.0).
Work is underway to identify a replacement SST and sea ice dataset providing updated temporal coverage to near
real-time. This new data will break the consistent link with past AMIP simulations that used the HadISST v1.0
(1870-01 to 1981-10) and NOAA OISST v2.0 (1981-11 to 2022-12), and so will be labeled v2.0.x to demarc this
change. Work underway shows that a subset of existing CMIP6-contributing models are sensitive to the SST and
sea ice changes that will occur in the v1.0.x -> 2.0.x dataset update.

Once the v2.0.x dataset is generated, we anticipate regular 6-monthly updates capturing temporal extensions
will be made available through input4MIPs (just like was done with the v1.1.0 through v1.1.8 versions in CMIP6).

The `mip_era` metadata value of 'CMIP7', is contained in the netcdf file global attributes, and is also
a `Target MIP List` search facet within the ESGF input4MIPs project page [here](https://aims2.llnl.gov/search/input4MIPs)

If you find a problem related to this dataset, please
[create an issue on GitHub](https://github.com/PCMDI/input4MIPs_CVs/issues/new?template=data_issue.md)
so that the identification and resolution of the problem is publicly accessible.

If you have a question related to this dataset, please
[create a discussion on GitHub](https://github.com/PCMDI/input4MIPs_CVs/discussions)
so that the identification and resolution of the problem is publicly accessible.

#### CMIP6Plus: Testing and feedback

For the testing phase, CMIP6Plus, use data with the source ID [PCMDI-AMIP-1-1-9](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22PCMDI-AMIP-1-1-9%22%5D%7D)

This data is for testing (both of the forcing data and of modelling workflows) only.
CMIP7 production simulations should not be started based on any data that has a `mip_era` value equal to 'CMIP6Plus'.

If you have feedback, please create or add to the [relevant GitHub discussion](https://github.com/PCMDI/input4MIPs_CVs/discussions).

<!--- end-cmip7-phases-source-ids -->

<!--- placeholder for piControl recommendation -->
## Navigating the data

### Recommendation for pre-industrial control (piControl)

This data is only used for the DECK AMIP experiment (CMIP:amip). As it is not used for the piControl
experiment hence there is no recommendation.

<!--- end of placeholder for piControl recommendation -->

<!--- begin-revision-history -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->
<!--- No revisions, hence section is blank -->
<!--- end-revision-history -->
