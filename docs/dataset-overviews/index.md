# Dataset overviews

Here we provide an overview of the datasets provided within input4MIPs.
These overviews do not replace or duplicate the papers and documentation provided by the dataset providers elsewhere.
Instead, they are intended to supplement these sources of information
with information that is targeted at users of input4MIPs data
(who can be very different from users who get this data via other means),
in particular models participating in [CMIP](https://www.wcrp-climate.org/wgcm-cmip).

1. [Anthropogenic short-lived climate forcer (SLCF) and CO<sub>2</sub> emissions](anthropogenic-slcf-co2-emissions.md)
1. [Open biomass burning emissions](open-biomass-burning-emissions.md)
1. [Land use](land-use.md)
1. [Greenhouse gas concentrations](greenhouse-gas-concentrations.md)
1. [CO<sub>2</sub> isotopes](co2-isotopes.md)
1. [Stratospheric volcanic SO<sub>2</sub> emissions and aerosol optical properties](stratospheric-volcanic-so2-emissions-aod.md)
1. [Ozone concentrations](ozone.md)
1. [Nitrogen deposition](nitrogen-deposition.md)
1. [Solar](solar.md)
1. [AMIP sea-surface temperature and sea-ice boundary forcing](amip-sst-sea-ice-boundary-forcing.md)
1. [Aerosol optical properties/MACv2-SP](aerosol-optical-properties-macv2-sp.md)
1. [Population density](population.md)

## Which data sets should I be using for CMIP7?

### CMIP7

<!--- begin-source-id-summary:cmip7 -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->

This data is for use in CMIP7 production simulations.
All data sets for use in CMIP7 production simulations are published with a `mip_era` metadata value of 'CMIP7'.
This metadata value appears both in the file's global metadata as well as its metadata on ESGF.

If you find an issue, please
[create an issue on GitHub](https://github.com/PCMDI/input4MIPs_CVs/issues/new?template=data_issue.md)
so that the identification and resolution of this issue is publicly accessible.

#### Source IDs for use in this phase

1. *Anthropogenic short-lived climate forcer (SLCF) and CO<sub>2</sub> emissions:* [CEDS-CMIP-2025-04-18; CEDS-CMIP-2025-04-18-supplemental](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22CEDS-CMIP-2025-04-18%22%2C%22CEDS-CMIP-2025-04-18-supplemental%22%5D%7D)
1. *Open biomass burning emissions:* [DRES-CMIP-BB4CMIP7-2-0](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22DRES-CMIP-BB4CMIP7-2-0%22%5D%7D)
1. *Land use:* [UofMD-landState-3-1-1](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22UofMD-landState-3-1-1%22%5D%7D)
1. *Greenhouse gas concentrations:* [CR-CMIP-1-0-0](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22CR-CMIP-1-0-0%22%5D%7D)
1. *CO<sub>2</sub> isotopes:* No data available for this phase yet
1. *Stratospheric volcanic SO<sub>2</sub> emissions and aerosol optical properties:* [UOEXETER-CMIP-2-0-0](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22UOEXETER-CMIP-2-0-0%22%5D%7D)
1. *Ozone concentrations:* No data available for this phase yet
1. *Nitrogen deposition:* No data available for this phase yet
1. *Solar:* [SOLARIS-HEPPA-CMIP-4-6](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22SOLARIS-HEPPA-CMIP-4-6%22%5D%7D)
1. *AMIP sea-surface temperature and sea-ice boundary forcing:* No data available for this phase yet
1. *Aerosol optical properties/MACv2-SP*: This is not managed via ESGF. Please see the [aerosol optical properties/MACv2-SP specific page](aerosol-optical-properties-macv2-sp) for details.
1. *Population density:* No data available for this phase yet
<!--- end-source-id-summary -->

### Testing

<!--- begin-source-id-summary:testing -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->

This data is for testing (both of the forcing data and of modelling workflows) only.
Production simulations should not be started based on any data that has a `mip_era` value equal to 'CMIP6Plus'.
(The `mip_era` metadata value appears both in each file's global attributes as well as its metadata on ESGF.)

If you have any feedback, please add it to the [relevant GitHub discussion](https://github.com/PCMDI/input4MIPs_CVs/discussions).

#### Source IDs for use in this phase

1. *Anthropogenic short-lived climate forcer (SLCF) and CO<sub>2</sub> emissions:* [CEDS-CMIP-2024-11-25; CEDS-CMIP-2024-11-25-supplemental; CEDS-CMIP-2024-10-21; CEDS-CMIP-2024-10-21-supplemental](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22CEDS-CMIP-2024-11-25%22%2C%22CEDS-CMIP-2024-11-25-supplemental%22%2C%22CEDS-CMIP-2024-10-21%22%2C%22CEDS-CMIP-2024-10-21-supplemental%22%5D%7D)
1. *Open biomass burning emissions:* [DRES-CMIP-BB4CMIP7-1-0](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22DRES-CMIP-BB4CMIP7-1-0%22%5D%7D)
1. *Land use:* [UofMD-landState-3-0](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22UofMD-landState-3-0%22%5D%7D)
1. *Greenhouse gas concentrations:* [CR-CMIP-0-4-0](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22CR-CMIP-0-4-0%22%5D%7D)
1. *CO<sub>2</sub> isotopes:* No data available for this phase yet
1. *Stratospheric volcanic SO<sub>2</sub> emissions and aerosol optical properties:* [UOEXETER-CMIP-1-3-1](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22UOEXETER-CMIP-1-3-1%22%5D%7D)
1. *Ozone concentrations:* No data available for this phase yet
1. *Nitrogen deposition:* No data available for this phase yet
1. *Solar:* [SOLARIS-HEPPA-CMIP-4-5](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22SOLARIS-HEPPA-CMIP-4-5%22%5D%7D)
1. *AMIP sea-surface temperature and sea-ice boundary forcing:* [PCMDI-AMIP-1-1-9](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22PCMDI-AMIP-1-1-9%22%5D%7D)
1. *Aerosol optical properties/MACv2-SP*: This is not managed via ESGF. Please see the [aerosol optical properties/MACv2-SP specific page](aerosol-optical-properties-macv2-sp) for details.
1. *Population density:* No data available for this phase yet
<!--- end-source-id-summary -->
