<!--- These values are used by `fill-out-auto-generated-sections.py` -->
<!--- forcing="simple-plumes" -->
<!--- source_id_stub="tbd" -->
# Aerosol optical properties/MACv2-SP

## Key contacts

- Names: Stephanie Fiedler
- Emails: stephanie.fiedler@uni-heidelberg.de

## Summary

The aerosol optical properties, simple plumes data set does not follow the usual practice for input4MIPs datasets.
The reason is that these files are directly used by Fortran forcing routines,
so making them fit the usual specification helps no-one.
As a result, the information provided here is limited.
For questions, please use the contact information at the top of this page.

That said, we can offer some pointers.
The methods used for producing this data are stable 
(see [Stevens et al., 2017](https://gmd.copernicus.org/articles/10/433/2017/)).
However, the data is entirely dependent on the emissions
(both biomass burning and anthropogenic),
so this dataset can only be considered stable once these input emissions are stable.

### Datasets for CMIP7 phases

#### CMIP7

For CMIP7, please use the data at this zenodo record:
[TBD](TBD).

#### Testing

For testing, please use the data at this zenodo record:
[https://doi.org/10.5281/zenodo.14512962](https://doi.org/10.5281/zenodo.14512962).

## Navigating the data

### Recommendation for pre-industrial control

Use the same approach as is used for anthropogenic emissions.

### Grids and frequencies provided

The aerosol optical properties provides scaling factors/parameters 
to calculate aerosol plumes associated with aerosol emissions
for models that do not calculate this themselves.
The provided data is only parameters.
As a data user, you have to calculate gridded data/input yourself using the relevant Fortran routines.
For details, see the Zenodo records provided.
