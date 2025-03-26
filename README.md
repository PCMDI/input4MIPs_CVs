<!--- --8<-- [start:header] -->
# input4MIPs Controlled Vocabularies (CVs)

[![Latest release](https://img.shields.io/badge/Latest%20release-v6.6.18-brightgreen.svg)](https://github.com/PCMDI/input4MIPs_CVs/releases/tag/v6.6.18)
[![DOI (all versions)](https://zenodo.org/badge/doi/10.5281/zenodo.12629796.svg)](https://zenodo.org/doi/10.5281/zenodo.12629796)
[![Docs](https://readthedocs.org/projects/input4mips-cvs/badge/?version=latest)](https://input4mips-cvs.readthedocs.io)

### THIS REPOSITORY IS CURRENTLY UNDER ACTIVE DEVELOPMENT

Controlled Vocabularies (CVs) for use in input4MIPs.
Full documentation can be found at: [input4mips-cvs.readthedocs.io](https://input4mips-cvs.readthedocs.io).

For further information regarding forcing dataset development
for the Coupled Model Intercomparison Project (CMIP) activities,
please see the
[CMIP Forcing Task Team homepage](https://wcrp-cmip.org/cmip7-task-teams/forcings/).

<!--- --8<-- [end:header] -->

<!--- 
    Note: different link here compared to in `docs/` 
    so that the link renders correctly on the GitHub homepage 
-->
For different, pre-prepared views of the database,
see 
[database views](https://input4mips-cvs.readthedocs.io/en/latest/database-views/).

## Usage

<!--- 
    Note: point to rendered docs 
    to avoid link rendering issues on the GitHub homepage 
-->

For information about how to use this repository,
see 
[usage as a data user](https://input4mips-cvs.readthedocs.io/en/latest/usage-data-user/#usage-as-a-data-user)
and [usage as a data producer](https://input4mips-cvs.readthedocs.io/en/latest/usage-data-user/#usage-as-a-data-producer).

<!--- --8<-- [start:repository-overview] -->
## Repository overview

The repository captures two key pieces of information.

### Controlled vocabularies

The first is the controlled vocabularies (CVs) used within the input4MIPs project.
The CVs define the allowed terms which can be used for various pieces of metadata.
The precise rules are still somewhat fuzzy 
and these CVs should be considered a work in progress,
however they do provide much more structure than nothing.
These live in the `CVs` directory.

These CVs are specific to the input4MIPs project.
They supplement the 'global' CVs, which can be found in 
[the MIP CMOR tables repository](https://github.com/PCMDI/mip-cmor-tables).
As much as possible, we rely on the 'global' CVs
and attempt to avoid duplicating information.
However, the 'global' CVs are currently under heavy development,
so there is some duplication at the moment.
We hope to reduce this over time.
When in doubt, the CVs in this repository will be the source of truth for the input4MIPs project.

Finally, the CVs also have some reliance on other conventions.
The most notable is the [CF metadata conventions](https://cfconventions.org/).
We also use [cfchecker](https://github.com/cedadev/cf-checker)
for validating files.
Where the CVs make use of other conventions, we make this as clear as possible.
However, this is also a work in progress.

### Files database

The second key piece of information is a database of the files we know about within the input4MIPs project.
At the moment, this database is stored as a JSON file within this repository,
`Database/input4MIPs_db_file_entries.json`
(although this may change in future, if this solution doesn't scale well).
This database provides a record of the files known to the input4MIPs project,
given that the ESGF index is not publicly queriable 
(nor perfectly suited to input4MIPs data, 
which does not always conform to the ESGF's data model, 
e.g. sometimes there is more than one variable in a file).

To ease exploration of the database, 
we provide a few pre-prepared views of the database,
see [database views](https://input4mips-cvs.readthedocs.io/en/latest/database-views/).
<!--- --8<-- [end:repository-overview] -->

## Contributors

<!--- --8<-- [start:contributors] -->
[![Contributors](https://contrib.rocks/image?repo=PCMDI/input4MIPs_CVs)](https://github.com/PCMDI/input4MIPs_CVs/graphs/contributors)

Thanks to our contributors!
<!--- --8<-- [end:contributors] -->

## Acknowledgement

<!--- --8<-- [start:acknowledgement] -->
The repository content has been collected from many contributors representing the input datasets for Model Intercomparison Projects (input4MIPs), including those from climate modeling groups and model intercomparison projects (MIPs) worldwide. The structure of content and tools required to maintain it was developed by climate and computer scientists from the Program for Climate Model Diagnosis and Intercomparison ([PCMDI](https://pcmdi.llnl.gov/)) at Lawrence Livermore National Laboratory ([LLNL](https://www.llnl.gov/)), [Climate Resource](https://www.climate-resource.com/), and the Coupled Model Intercomparison Project International Project Office ([CMIP-IPO](https://wcrp-cmip.org/cmip-governance/project-office/)), with assistance from a large and expanding international community.

This work is sponsored by the Regional and Global Model Analysis ([RGMA](https://climatemodeling.science.energy.gov/program/regional-global-model-analysis)) program of the Earth and Environmental Systems Sciences Division ([EESSD](https://science.osti.gov/ber/Research/eessd)) in the Office of Biological and Environmental Research ([BER](https://science.osti.gov/ber)) within the Department of Energy's ([DOE](https://www.energy.gov/)) Office of Science ([OS](https://science.osti.gov/)). The work at PCMDI is performed under the auspices of the U.S. Department of Energy by Lawrence Livermore National Laboratory under Contract DE-AC52-07NA27344.
<!--- --8<-- [end:acknowledgement] -->

<!--- 
    Note: different link here compared to in `docs/` 
    so that the link renders correctly on the GitHub homepage 
-->
<p>
    <img src="https://pcmdi.github.io/assets/PCMDI/100px-PCMDI-Logo-NoText-square-png8.png"
         width="65"
         style="margin-right: 30px"
         title="Program for Climate Model Diagnosis and Intercomparison"
         alt="Program for Climate Model Diagnosis and Intercomparison"
    >&nbsp;
    <img src="https://pcmdi.github.io/assets/DOE/480px-DOE_Seal_Color.png"
         width="65"
         style="margin-right: 30px"
         title="United States Department of Energy"
         alt="United States Department of Energy"
    >&nbsp;
    <img src="https://pcmdi.github.io/assets/LLNL/212px-LLNLiconPMS286-WHITEBACKGROUND.png"
         width="65"
         style="margin-right: 30px"
         title="Lawrence Livermore National Laboratory"
         alt="Lawrence Livermore National Laboratory"
    >&nbsp;
    <img src="https://pcmdi.github.io/assets/CMIP/100px-CMIP_Logo_RGB_Positive-square-96dpi.png"
         width="65"
         style="margin-right: 30px"
         title="Couple Model Intercomparison Project International Project Office"
         alt="Couple Model Intercomparison Project International Project Office"
    >&nbsp;
    <img src="https://raw.githubusercontent.com/PCMDI/input4MIPs_CVs/main/docs/assets/CR_Logo%20_Square_400x400.png"
         width="65"
         style="margin-right: 30px"
         title="Climate Resource"
         alt="Climate Resource"
    >
</p>
