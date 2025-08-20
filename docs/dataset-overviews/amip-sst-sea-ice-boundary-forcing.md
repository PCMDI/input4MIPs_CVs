<!--- These values are used by `fill-out-auto-generated-sections.py` -->
<!--- forcing="amip-ssts" -->
<!--- source_id_stub="PCMDI-AMIP-1" -->
# AMIP sea-surface temperature and sea-ice boundary forcing

## Key contacts

- Names: Paul J. Durack
- Emails: durack1@llnl.gov

## Summary

Once the v2.0.x dataset is generated, we anticipate regular 6-monthly updates capturing temporal extensions
will be made available through input4MIPs (just like was done with the v1.1.0 through v1.1.8 versions in CMIP6).

When it is ready, the CMIP7 dataset will be released
with a `mip_era` metadata value of 'CMIP7'.
This metadata is contained in the netCDF file global attributes, 
and is also available as use as a search facet (with label `Target MIP List`)
within the ESGF input4MIPs project page [here](https://aims2.llnl.gov/search/input4MIPs).

If you find a problem related to this dataset, please
[create an issue on GitHub](https://github.com/PCMDI/input4MIPs_CVs/issues/new?template=data_issue.md)
so that the identification and resolution of the problem is publicly accessible.

If you have a question related to this dataset, please
[create a discussion on GitHub](https://github.com/PCMDI/input4MIPs_CVs/discussions)
so that the identification and resolution of the problem is publicly accessible.

<!--- begin-cmip7-phases-source-ids -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->
### Source IDs for CMIP7 phases

The source ID that identifies the dataset to use in CMIP7 is given below.

#### CMIP7

For the CMIP7 phase of CMIP7, use data with the source ID [PCMDI-AMIP-1-1-10](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22PCMDI-AMIP-1-1-10%22%5D%7D)

The data has the DOI: [10.25981/ESGF.input4MIPs.CMIP7/2575015](https://doi.org/10.25981/ESGF.input4MIPs.CMIP7/2575015).

This data is for use in CMIP7 production simulations.
All data sets for use in CMIP7 production simulations are published with a `mip_era` metadata value of 'CMIP7'.
This metadata value appears both in the file's global metadata as well as its metadata on ESGF.

If you find an issue, please
[create an issue on GitHub](https://github.com/PCMDI/input4MIPs_CVs/issues/new?template=data_issue.md)
so that the identification and resolution of this issue is publicly accessible.

#### Testing

For the testing phase of CMIP7, use data with the source ID [PCMDI-AMIP-1-1-9](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22PCMDI-AMIP-1-1-9%22%5D%7D)

No DOIs are available for this data.

This data is for testing (both of the forcing data and of modelling workflows) only.
Production simulations should not be started based on any data that has a `mip_era` value equal to 'CMIP6Plus'.
(The `mip_era` metadata value appears both in each file's global attributes as well as its metadata on ESGF.)

If you have any feedback, please add it to the [relevant GitHub discussion](https://github.com/PCMDI/input4MIPs_CVs/discussions).

<!--- end-cmip7-phases-source-ids -->

<!--- placeholder for piControl recommendation -->
## Navigating the data

### Recommendation for pre-industrial control (piControl)

This data is only used for the DECK AMIP experiment (CMIP:amip).
As it is not used for the piControl experiment hence there is no recommendation.

<!--- end of placeholder for piControl recommendation -->

<!--- begin-revision-history -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->
<!--- No revisions, hence section is blank -->
<!--- end-revision-history -->
