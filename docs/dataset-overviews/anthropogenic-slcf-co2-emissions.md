<!--- These values are used by `fill-out-auto-generated-sections.py` -->
<!--- forcing="slcf_co2_emms" -->
<!--- source_id_stub="CEDS-CMIP" -->
# Anthropogenic short-lived climate forcer (SLCF) and CO<sub>2</sub> emissions

## Key contacts

- Names: Rachel Hoesly, Steve Smith
- Emails: rachel.hoesly@pnnl.gov; ssmith@pnnl.gov

## Summary

CEDS data is available.
Emissions data are provided for SO<sub>2</sub>, NOx, BC, OC, NH<sub>3</sub>, NMVOC,  CO, CO<sub>2</sub> from 1750 - 2023.
Emissions data for CH<sub>4</sub> and N<sub>2</sub>O are provided from 1970 - 2023
(although extensions back to 1750 are available in the "supplemental" source ID).

When handling this data, solid biofuel emissions and speciated NMVOCs 
have the suffix "-supplemental" added to their source ID to avoid inadvertent double counting.

For documentation of the underlying data,
please keep an eye on https://github.com/JGCRI/CEDS,
which will be updated with more documentation soon. 

This data is derived from CEDS' aggregate emissions releases.
<!--- Aggregate data by country and sector for this release is also available in units of kilo-tonne (kt) per year and can be found [here](https://zenodo.org/records/12803197). -->
<!--- Note that country totals in these summary files do not include international shipping or aircraft emissions, which are reported under the "global" iso. -->

Full details on the dataset and all relevant links can be found on the [CEDS GitHub page](https://github.com/JGCRI/CEDS). A summary of differences between the CMIP7 and previous versions of the dataset can be found on https://github.com/JGCRI/CEDS/tree/master/documentation

<!--- begin-cmip7-phases-source-ids -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->
### Source IDs for CMIP7 phases

The source ID that identifies the dataset to use in CMIP7 is given below.

#### CMIP7

For the CMIP7 phase of CMIP, you will need data from the following source IDs:

- [CEDS-CMIP-2025-04-18](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22CEDS-CMIP-2025-04-18%22%5D%7D)
- [CEDS-CMIP-2025-04-18-supplemental](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22CEDS-CMIP-2025-04-18-supplemental%22%5D%7D).

Retrieving and only using valid data will require some care.
Please make sure you read the guidance given at the start of the Summary section
and process the data carefully.

The data has the DOIs: [10.5281/zenodo.15127477](https://doi.org/10.5281/zenodo.15127477), [10.5281/zenodo.15001546](https://doi.org/10.5281/zenodo.15001546).

This data is for use in CMIP7 production simulations.
All data sets for use in CMIP7 production simulations are published with a `mip_era` metadata value of 'CMIP7'.
This metadata value appears both in the file's global metadata as well as its metadata on ESGF.

If you find an issue, please
[create an issue on GitHub](https://github.com/PCMDI/input4MIPs_CVs/issues/new?template=data_issue.md)
so that the identification and resolution of this issue is publicly accessible.

#### Testing

For the testing phase of CMIP7, you will need data from the following source IDs:

- [CEDS-CMIP-2024-11-25](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22CEDS-CMIP-2024-11-25%22%5D%7D)
- [CEDS-CMIP-2024-11-25-supplemental](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22CEDS-CMIP-2024-11-25-supplemental%22%5D%7D)
- [CEDS-CMIP-2024-10-21](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22CEDS-CMIP-2024-10-21%22%5D%7D)
- [CEDS-CMIP-2024-10-21-supplemental](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22CEDS-CMIP-2024-10-21-supplemental%22%5D%7D).

Retrieving and only using valid data will require some care.
Please make sure you read the guidance given at the start of the Summary section
and process the data carefully.

The data has the DOIs: [10.5281/zenodo.13952845](https://doi.org/10.5281/zenodo.13952845), [10.5281/zenodo.14145000](https://doi.org/10.5281/zenodo.14145000).

This data is for testing (both of the forcing data and of modelling workflows) only.
Production simulations should not be started based on any data that has a `mip_era` value equal to 'CMIP6Plus'.
(The `mip_era` metadata value appears both in each file's global attributes as well as its metadata on ESGF.)

If you have any feedback, please add it to the [relevant GitHub discussion](https://github.com/PCMDI/input4MIPs_CVs/discussions).

<!--- end-cmip7-phases-source-ids -->

## Navigating the data

### Recommendation for pre-industrial control

Repeat the 1850 values.

### Grids and frequencies provided

CEDS emissions are provided at monthly resolution, on a 0.5 degree grid (grid ID of "gn"),
with 50-years per data file. 
A 0.1° grid for recent decades is also available under grid ID of "gr". 
Emissions are relatively smooth over the early portion of this time period, but annual data is supplied for consistency across the dataset. 
The files are in netcdf v4 (HDFv5) format with CF-compliant and ESGF-compliant metadata.

Gridded aircraft emissions are also supplied in a separate file with 25 vertical layers 
(using the CMIP5 historical emissions Lamarque et al. 2010, as drawn from Lee et al., as a template). 
Note that aircraft emissions are zero in early years, but files are provided for all years for consistency.

The gridded emissions incorporate a monthly seasonal cycle by sector drawing largely from the 
[ECLIPSE project](https://iiasa.ac.at/models-tools-data/global-emission-fields-of-air-pollutants-and-ghgs), 
[Carbon Tracker](https://carbontracker.org/), and [EDGAR](https://edgar.jrc.ec.europa.eu/).

VOC speciation is provided at the 23 species resolution from [EDGAR](https://edgar.jrc.ec.europa.eu/).

### Variables provided

Subsequent CEDS data releases since August 2016 are in a format of one variable per data file, with the sectors included as a dimension of the variable's data.

The sectors in the netCDF files (other than aviation) are:

| Sector | Description                                                             |
|--------|-------------------------------------------------------------------------|
| 0: AGR | Non-combustion agricultural sector                                      |
| 1: ENE | Energy transformation and extraction                                    |
| 2: IND | Industrial combustion and processes                                     |
| 3: TRA | Surface Transportation (Road, Rail, Other)                              |
| 4: RCO | Residential, commercial, and other                                      |
| 5: SLV | Solvents                                                                |
| 6: WST | Waste disposal and handling                                             |
| 7: SHP | International shipping (including VOCs from oil tanker loading/leakage) |

Within the netCDF files the sector ids are:

`sector:ids = "0: Agriculture; 1: Energy; 2: Industrial; 3: Transportation; 4: Residential, Commercial, Other; 5: Solvents production and application; 6: Waste; 7: International Shipping" ;`

### Supplementary Data

For use in setting aerosol size distribution and additional speciation (if desired), 
an auxiliary dataset providing emissions from solid biomass combustion is also provided. 
Note that these are a subset of emissions in the main files. 
These data, therefore, should NOT be added to the emissions in the main files. 
(Note that no data files for CO2 emissions from solid biomass are released, as CO2 emissions from CEDS are from fossil fuels only.)

<!---
Supplementary checking `.csv` text files that provide total global mass for each sector, month, and year 
are also available as well as global seasonal diagnostic plots can be found [here](https://zenodo.org/records/14145000).
-->

### Gridding Methodology

Emissions were first estimated at the level of country, sector, and fuel. 
Emissions by sector were then mapped to spatial grids by country and sector 
(several intermediate gridded sectors were combined to form the final release sectors for CMIP7). 
Grid cells that contain more than one country can have portions of emissions from each country.

For recent decades, emissions were mapped to the grid level largely using the distribution of emissions from EDGAR within each country and gridding sector 
(usually using year-specific EDGAR grids from 1970 forward). 
For some sectors, the emissions distribution varies over time, while for other sectors it was held constant. 
For most emission species, residential combustion is the dominant source by 1850, 
so emissions from the RCO sector were distributed using HYDE population distributions by 1900 
(with blended spatial distributions between 1900 and 1970). 
For other sectors the emissions distribution within each country was held fixed before 1970.

Because of the simplifying assumptions, emissions distributions, particularly in earlier years, should not be taken literally. 
Overall, however, anthropogenic emissions become small relative to either natural sources or mid-to-late 20th century emissions 
so we anticipate that these assumptions are not likely to have major impacts on global or regional modeling results.

In this release, large SO2 point sources, along with any co-emitted species, are explicitly represented 
- largely through use of a SO2 point source catalog developed by [Fioletov et al 2023](https://doi.org/10.5194/essd-15-75-2023). 
Remaining emissions for any country/sector are distributed using EDGAR or other proxies as described above 
(after removing any point sources now explicitly represented)>

More details on the use of point sources in gridding methodology can be found [here](https://zenodo.org/records/6949566/files/CEDS_Point_Source_Documentation.pdf).

For more details on the gridding methodology see:
Feng, L., Smith, S. J., Braun, C., Crippa, M., Gidden, M. J., Hoesly, R., Klimont, Z., van Marle, M., van den Berg, M., and van der Werf, G. R.: The generation of gridded emissions data for CMIP6, Geosci. Model Dev., 13, 461–482, https://doi.org/10.5194/gmd-13-461-2020, 2020.

For more details on the underlying emissions data see:
Hoesly, R. M., Smith, S. J., Feng, L., Klimont, Z., Janssens-Maenhout, G., Pitkanen, T., Seibert, J. J., Vu, L., Andres, R. J., Bolt, R. M., Bond, T. C., Dawidowski, L., Kholod, N., Kurokawa, J.-I., Li, M., Liu, L., Lu, Z., Moura, M. C. P., O'Rourke, P. R., and Zhang, Q. (2018) Historical (1750–2014) anthropogenic emissions of reactive gases and aerosols from the Community Emissions Data System (CEDS), Geosci. Model Dev., 11, 369-408. doi: 10.5194/gmd-11-369-2018.


### Uncertainty

At present, uncertainties are not quantified.
Uncertainties in recent years (most recent 2-3 years) 
are higher due to delays in reporting data and common revision of data point in recent years 
(as documented [here](https://iopscience.iop.org/article/10.1088/1748-9326/aaebc3)). 
Uncertainties farther back in time are also higher, especially the spatial distribution. 
However, the importance of anthropogenic emissions compared to natural sources also become less significant in these early years. 
In between (roughly between 1970 and 5 years before now) the uncertainties can be smaller.

### Examples of working with the data

See the [CEDS GitHub page](https://github.com/JGCRI/CEDS).
The [emission harmonization team's notebooks](https://github.com/iiasa/emissions_harmonization_historical/)
may also be of interest.

<!---
### Differences from CMIP6 or other previous versions

Comparison figures showing CMIP6 vs CMIP6Plus data sets by aggregate region and sector can be found [here](https://github.com/JGCRI/CEDS/blob/master/documentation/Version_comparison_figures_v_2024_07_08_vs_2016_07_16(CMIP6).pdf).
-->

### File formats and naming

The file formats are identical to CMIP6.

#### Emissions Data file name format

Bulk gridded emissions: 

- `[em_species]-em-anthro_input4MIPs_emissions_CMIP_[source_id]_gn_YYYY01-ZZZZ12.nc`,
  where `YYYY` is the starting year contained in this file and `ZZZZ` is the ending year.
- netCDF variable name: `[em_species]_em_anthro`.

Gridded aircraft emissions: 

- `[em_species]-em-AIR-anthro_input4MIPs_emissions_CMIP_[source_id]_gn_YYYY01-ZZZZ12.nc`,
  where `YYYY` is the starting year contained in this file and `ZZZZ` is the ending year.
- netCDF variable name: `[em_species]_em_AIR_anthro`

#### Supplemental emissions Data file name format

Gridded biomass emissions: 

- `[em_species]-em-SOLID-BIOFUEL-anthro_input4MIPs_emissions_CMIP_[source_id]_gn_YYYY01-ZZZZ12.nc`,
  where `YYYY` is the starting year contained in this file and `ZZZZ` is the ending year.
- netCDF variable name: `[em_species]_em_SOLID_BIOFUEL_anthro`

VOC speciation grids: 

- `VOC01-alcohols-em-speciated-VOC-anthro_input4MIPs_emissions_CMIP_[source_id]_gn_YYYY01-ZZZZ12.nc`,
  where `YYYY` is the starting year contained in this file and `ZZZZ` is the ending year.
- netCDF variable name: `VOC01_alcohols_em_speciated_VOC_anthro`

There is a separate README file with further information on VOC speciation -- see the CEDS project web site. 
Note there is a variable naming inconsistency for these file - described in the VOC README.


<!--- begin-revision-history -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->
## Revision history

### CEDS-CMIP-2025-03-18-supplemental

A bug was found in gridding of data for that led to spurious emissions for CO, CO2, and NOx, for the
industrial (IND) and energy (ENE) sectors. These spurious emissions span 1961 - 2021. Globally, the
differences represent less than 0.001% of annual emissions, but sometimes individual grid cell
changes can sometimes represent a factor of 2 change (for small emissions).

### CEDS-CMIP-2025-03-18

A bug was found in gridding of data for that led to spurious emissions for CO, CO2, and NOx, for the
industrial (IND) and energy (ENE) sectors. These spurious emissions span 1961 - 2021. Globally, the
differences represent less than 0.001% of annual emissions, but sometimes individual grid cell
changes can sometimes represent a factor of 2 change (for small emissions).

### CEDS-CMIP-2024-11-25-supplemental

A number of updates have been made in CEDS-CMIP-2025-03-18*. These are significantly different from
this dataset, hence it has been retracted.

### CEDS-CMIP-2024-11-25

A number of updates have been made in CEDS-CMIP-2025-03-18*. These are significantly different from
this dataset, hence it has been retracted.

### CEDS-CMIP-2024-10-21-supplemental

A number of updates have been made in CEDS-CMIP-2025-03-18*. These are significantly different from
this dataset, hence it has been retracted.

<!--- end-revision-history -->
