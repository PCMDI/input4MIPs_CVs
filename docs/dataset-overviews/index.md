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

### DECK

DECK (Diagnostic, Evaluation and Characterization of Klima) simulations
i.e. key model characterisation experiments.
In practice, when we talk about the DECK,
the forcings task team just focusses on forcings for the pre-industrial control (piControl) and historical experiments,
as if we provide these, then we provide forcings required for all DECK experiments
(the other DECK experiments all build on relatively trivial modifications of the piControl and historical forcings).

#### CMIP7

<!--- begin-source-id-summary:deck-cmip7 -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->

This data is for use in CMIP7 production simulations.
All data sets for use in CMIP7 production simulations are published with a `mip_era` metadata value of 'CMIP7'.
This metadata value appears both in the file's global metadata as well as its metadata on ESGF.

If you find an issue, please
[create an issue on GitHub](https://github.com/PCMDI/input4MIPs_CVs/issues/new?template=data_issue.md)
so that the identification and resolution of this issue is publicly accessible.

##### Source IDs for use in this phase

1. *Anthropogenic short-lived climate forcer (SLCF) and CO<sub>2</sub> emissions:* [CEDS-CMIP-2025-04-18; CEDS-CMIP-2025-04-18-supplemental](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22CEDS-CMIP-2025-04-18%22%2C%22CEDS-CMIP-2025-04-18-supplemental%22%7D) (DOIs: [10.5281/zenodo.15127477](https://doi.org/10.5281/zenodo.15127477), [10.5281/zenodo.15001546](https://doi.org/10.5281/zenodo.15001546).)
1. *Open biomass burning emissions:* [DRES-CMIP-BB4CMIP7-2-0](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22DRES-CMIP-BB4CMIP7-2-0%22%7D) (DOI: [10.25981/ESGF.input4MIPs.CMIP7/2524040](https://doi.org/10.25981/ESGF.input4MIPs.CMIP7/2524040).)
1. *Land use:* [UofMD-landState-3-1-1](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22UofMD-landState-3-1-1%22%7D) (DOI: [10.25981/ESGF.input4MIPs.CMIP7/2521499](https://doi.org/10.25981/ESGF.input4MIPs.CMIP7/2521499).)
1. *Greenhouse gas concentrations:* [CR-CMIP-1-0-0](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22CR-CMIP-1-0-0%22%7D) (DOI: [https://doi.org/10.5281/zenodo.14892947](https://doi.org/10.5281/zenodo.14892947).)
1. *CO<sub>2</sub> isotopes:* [ImperialCollege-3-0](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22ImperialCollege-3-0%22%7D) (DOI: [10.25981/ESGF.input4MIPs.CMIP7/2583902](https://doi.org/10.25981/ESGF.input4MIPs.CMIP7/2583902).)
1. *Stratospheric volcanic SO<sub>2</sub> emissions and aerosol optical properties:* [UOEXETER-CMIP-2-2-1](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22UOEXETER-CMIP-2-2-1%22%7D) (DOI: [10.25981/ESGF.input4MIPs.CMIP7/2522673](https://doi.org/10.25981/ESGF.input4MIPs.CMIP7/2522673).)
1. *Ozone concentrations:* [FZJ-CMIP-ozone-1-0](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22FZJ-CMIP-ozone-1-0%22%7D) (DOI: [10.25981/ESGF.input4MIPs.CMIP7/2584173](https://doi.org/10.25981/ESGF.input4MIPs.CMIP7/2584173).)
1. *Nitrogen deposition:* No data available for this phase yet
1. *Solar:* [SOLARIS-HEPPA-CMIP-4-6](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22SOLARIS-HEPPA-CMIP-4-6%22%7D) (DOI: [10.25981/ESGF.input4MIPs.CMIP7/2522675](https://doi.org/10.25981/ESGF.input4MIPs.CMIP7/2522675).)
1. *AMIP sea-surface temperature and sea-ice boundary forcing:* [PCMDI-AMIP-1-1-10](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22PCMDI-AMIP-1-1-10%22%7D) (DOI: [10.25981/ESGF.input4MIPs.CMIP7/2575015](https://doi.org/10.25981/ESGF.input4MIPs.CMIP7/2575015).)
1. *Aerosol optical properties/MACv2-SP*: This is not managed via ESGF. Please see the [aerosol optical properties/MACv2-SP specific page](aerosol-optical-properties-macv2-sp) for details.
1. *Population density:* [PIK-CMIP-1-0-1](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22PIK-CMIP-1-0-1%22%7D) (No DOI provided)
<!--- end-source-id-summary -->

#### Testing

<!--- begin-source-id-summary:deck-testing -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->

This data is for testing (both of the forcing data and of modelling workflows) only.
Production simulations should not be started based on any data that has a `mip_era` value equal to 'CMIP6Plus'.
(The `mip_era` metadata value appears both in each file's global attributes as well as its metadata on ESGF.)

If you have any feedback, please add it to the [relevant GitHub discussion](https://github.com/PCMDI/input4MIPs_CVs/discussions).

##### Source IDs for use in this phase

1. *Anthropogenic short-lived climate forcer (SLCF) and CO<sub>2</sub> emissions:* [CEDS-CMIP-2024-11-25; CEDS-CMIP-2024-11-25-supplemental; CEDS-CMIP-2024-10-21; CEDS-CMIP-2024-10-21-supplemental](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22CEDS-CMIP-2024-11-25%22%2C%22CEDS-CMIP-2024-11-25-supplemental%22%2C%22CEDS-CMIP-2024-10-21%22%2C%22CEDS-CMIP-2024-10-21-supplemental%22%7D) (DOIs: [10.5281/zenodo.13952845](https://doi.org/10.5281/zenodo.13952845), [10.5281/zenodo.14145000](https://doi.org/10.5281/zenodo.14145000).)
1. *Open biomass burning emissions:* [DRES-CMIP-BB4CMIP7-1-0](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22DRES-CMIP-BB4CMIP7-1-0%22%7D) (No DOI provided)
1. *Land use:* [UofMD-landState-3-0](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22UofMD-landState-3-0%22%7D) (No DOI provided)
1. *Greenhouse gas concentrations:* [CR-CMIP-0-4-0](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22CR-CMIP-0-4-0%22%7D) (DOI: [10.5281/zenodo.13365838](https://doi.org/10.5281/zenodo.13365838).)
1. *CO<sub>2</sub> isotopes:* No data available for this phase yet
1. *Stratospheric volcanic SO<sub>2</sub> emissions and aerosol optical properties:* [UOEXETER-CMIP-1-3-1](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22UOEXETER-CMIP-1-3-1%22%7D) (No DOI provided)
1. *Ozone concentrations:* No data available for this phase yet
1. *Nitrogen deposition:* No data available for this phase yet
1. *Solar:* [SOLARIS-HEPPA-CMIP-4-5](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22SOLARIS-HEPPA-CMIP-4-5%22%7D) (No DOI provided)
1. *AMIP sea-surface temperature and sea-ice boundary forcing:* [PCMDI-AMIP-1-1-9](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22PCMDI-AMIP-1-1-9%22%7D) (DOI: [10.25981/ESGF.input4MIPs.CMIP6Plus/2583903](https://doi.org/10.25981/ESGF.input4MIPs.CMIP6Plus/2583903).)
1. *Aerosol optical properties/MACv2-SP*: This is not managed via ESGF. Please see the [aerosol optical properties/MACv2-SP specific page](aerosol-optical-properties-macv2-sp) for details.
1. *Population density:* No data available for this phase yet
<!--- end-source-id-summary -->

### ScenarioMIP

ScenarioMIP scenario simulations
i.e. exploration of the climate under a selected range of possible futures.
As a result of the way that input4MIPs forcings are distributed,
the different scenarios are identified as part of the source ID of each forcing.
As a result, each forcing will have multiple source IDs, one for each scenario to run.
This leads to a lot of source IDs.
We considered changing this (see [discussion #64](https://github.com/PCMDI/input4MIPs_CVs/discussions/64)),
but ultimately decided that would be too disruptive given the time available.
For advice on how to extract the scenario information from the source ID,
see [extracting scenario from the source ID](extracting-scenario-from-source-id).

#### CMIP7

<!--- begin-source-id-summary:scenariomip-cmip7 -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->

This data is for use in CMIP7 production simulations.
All data sets for use in CMIP7 production simulations are published with a `mip_era` metadata value of 'CMIP7'.
This metadata value appears both in the file's global metadata as well as its metadata on ESGF.

If you find an issue, please
[create an issue on GitHub](https://github.com/PCMDI/input4MIPs_CVs/issues/new?template=data_issue.md)
so that the identification and resolution of this issue is publicly accessible.

##### Source IDs for use in this phase

1. *Anthropogenic short-lived climate forcer (SLCF) and CO<sub>2</sub> emissions:* No data available for this phase yet
1. *Open biomass burning emissions:* No data available for this phase yet
1. *Land use:* No data available for this phase yet
1. *Greenhouse gas concentrations:* No data available for this phase yet
1. *CO<sub>2</sub> isotopes:* No data available for this phase yet
1. *Stratospheric volcanic SO<sub>2</sub> emissions and aerosol optical properties:* [UOEXETER-ScenarioMIP-2-2-1](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22UOEXETER-ScenarioMIP-2-2-1%22%7D) (No DOI provided)
1. *Ozone concentrations:* No data available for this phase yet
1. *Nitrogen deposition:* No data available for this phase yet
1. *Solar:* No data available for this phase yet
1. *AMIP sea-surface temperature and sea-ice boundary forcing:* No data available for this phase yet
1. *Aerosol optical properties/MACv2-SP*: This is not managed via ESGF. Please see the [aerosol optical properties/MACv2-SP specific page](aerosol-optical-properties-macv2-sp) for details.
1. *Population density:* No data available for this phase yet
<!--- end-source-id-summary -->

#### Testing

<!--- begin-source-id-summary:scenariomip-testing -->
<!--- Do not edit this section, it is automatically updated when the docs are built -->

This data is for testing (both of the forcing data and of modelling workflows) only.
Production simulations should not be started based on any data that has a `mip_era` value equal to 'CMIP6Plus'.
(The `mip_era` metadata value appears both in each file's global attributes as well as its metadata on ESGF.)

If you have any feedback, please add it to the [relevant GitHub discussion](https://github.com/PCMDI/input4MIPs_CVs/discussions).

##### Source IDs for use in this phase

1. *Anthropogenic short-lived climate forcer (SLCF) and CO<sub>2</sub> emissions:* No data available for this phase yet
1. *Open biomass burning emissions:* No data available for this phase yet
1. *Land use:* No data available for this phase yet
1. *Greenhouse gas concentrations:* [CR-vllo-0-1-0; CR-vlho-0-1-0; CR-l-0-1-0; CR-ml-0-1-0; CR-m-0-1-0; CR-hl-0-1-0; CR-h-0-1-0](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22CR-vllo-0-1-0%22%2C%22CR-vlho-0-1-0%22%2C%22CR-l-0-1-0%22%2C%22CR-ml-0-1-0%22%2C%22CR-m-0-1-0%22%2C%22CR-hl-0-1-0%22%2C%22CR-h-0-1-0%22%7D) (DOI: [dev-test](https://doi.org/dev-test).)
1. *CO<sub>2</sub> isotopes:* No data available for this phase yet
1. *Stratospheric volcanic SO<sub>2</sub> emissions and aerosol optical properties:* No data available for this phase yet
1. *Ozone concentrations:* No data available for this phase yet
1. *Nitrogen deposition:* No data available for this phase yet
1. *Solar:* No data available for this phase yet
1. *AMIP sea-surface temperature and sea-ice boundary forcing:* No data available for this phase yet
1. *Aerosol optical properties/MACv2-SP*: This is not managed via ESGF. Please see the [aerosol optical properties/MACv2-SP specific page](aerosol-optical-properties-macv2-sp) for details.
1. *Population density:* [PIK-vllo-0-2-0; PIK-vlho-0-2-0; PIK-l-0-2-0; PIK-ml-0-2-0; PIK-m-0-2-0; PIK-hl-0-2-0; PIK-h-0-2-0](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22PIK-vllo-0-2-0%22%2C%22PIK-vlho-0-2-0%22%2C%22PIK-l-0-2-0%22%2C%22PIK-ml-0-2-0%22%2C%22PIK-m-0-2-0%22%2C%22PIK-hl-0-2-0%22%2C%22PIK-h-0-2-0%22%7D) (No DOI provided)
<!--- end-source-id-summary -->

## CMIP7 input4MIPs data licensing

It was decided at the June 2025 CMIP Core Panel meeting that:

> CMIP7 DECK forcings data licensing:
> data should be licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) 
> or No Rights Reserved (CC0) license.
> This is to enable open access to CMIP7 products.

Almost all data providers have complied with this in a way that is easily queriable.
If you have doubts, please double check the `license_id` and `license` attributes
in files' global attributes or look at the pages which show this metadata:

- [Dataset-level view CMIP7](../database-views/input4MIPs_datasets_CMIP7.html)
- [File-level view CMIP7](../database-views/input4MIPs_files_CMIP7.html)
