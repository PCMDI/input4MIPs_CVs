# input4MIPs_CVs [![Current version](https://img.shields.io/badge/Current%20version-6.5.2-brightgreen.svg)](https://github.com/PCMDI/input4MIPs_CVs/releases/tag/6.5.2) [![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.12629796.svg)](https://doi.org/10.5281/zenodo.12629796)

Controlled Vocabularies (CVs) for use in input4MIPs

### THIS REPOSITORY IS CURRENTLY UNDER ACTIVE DEVELOPMENT

To see information regarding forcing dataset development for the Coupled Model Intercomparison Project (CMIP) activities, please see the [CMIP Forcing Task Team homepage](https://wcrp-cmip.org/cmip7-task-teams/forcings/).

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
for validating files (see also [](#data-validation)).
Where the CVs make use of other conventions, we make this as clear as possible.
However, this is also a work in progress.

(overview-datasets-database)=
### Datasets database

The second key piece of information is a database of datasets.
This database provides a record of the datasets being managed in the input4MIPs project,
given that the ESGF index is not publicly queriable 
(nor perfectly suited to input4MIPs data, 
which does not always conform to the ESGF's data model, 
e.g. sometimes there is more than one variable in a file).

The database is stored as a JSON file within this repository.
However, we also provide an HTML table in `docs/input4MIPs_datasets.html` 
which may be an easier format to work with.

## Usage

### As a data user

As a data user, the key source of information will be the datasets database.
As discussed in [](#overview-datasets-database), 
this provides a record of all the datasets being managed in the input4MIPs project.
You will likely wish to search these records to find the datasets of interest to you,
then use their ESGF links to download them.
[TODO: instructions on how to go from a search here to downloading via ESGF easily once we know how that will work]

It is unlikely that you will need to use the CVs directly,
although they may be helpful for understanding what the different terms mean
(and this metadata capturing and clarity will improve over time 
as we make greater and greater use of 
[json-ld](https://json-ld.org/)).

### As a data producer

As a data producer, there are a few key steps.

#### Register your institution ID

The first step is to register your institution ID.
This means the following steps:

1. make a pull request that adds your institution's ID to `CVs/input4MIPs_institution_id.json`.
   The basic rules for IDs generally, which includes institution IDs,
   is that they must only contain alphanumeric characters and hyphens 
   (i.e. the characters a-z, A-Z, 0-9 and -).
   In your pull request, please tag @durack1 and @znichollscr.
   If you have any issues with this, feel free to [make a general issue](https://github.com/PCMDI/input4MIPs_CVs/issues/new)
   and tag @znichollscr.

1. (optional, but recommend) check if your institution has a research organisation registry (ROR) ID
   ([ROR search can be done here](https://ror.org/)).

  - if your organisation does not have an ROR, 
    please make an issue in the [MIP CMOR tables repository to note this](https://github.com/pcmdi/mip-cmor-tables/issues/new?assignees=&labels=&projects=&template=default.md&title=No+ROR+for+institute+X)
    and tag @znichollscr.

  - if your organisation does have an ROR,
    please make an issue in the [MIP CMOR tables repository to register your institute](https://github.com/PCMDI/mip-cmor-tables/issues/new?assignees=&labels=add_institution&projects=&template=add-Institution.md&title=New+Institution).
    The template should be straightforward.
    If there are any issues, just make the issue and tag @znichollscr.
    If you have any issues with this, feel free to [make a general issue](https://github.com/pcmdi/mip-cmor-tables/issues/new?assignees=&labels=&projects=&template=default.md&title=Help+needed+to+register+ROR+for+institute+X)
    and tag @znichollscr.

1. (optional, but recommend) if you supply your data as part of a consortium, then there is an extra step

  - firstly, make sure that all institutes in your consortium have registered their RORs in the MIP CMOR tables
    in the same way that you did for your institute in the previous step.

  - then, please make an issue in the [MIP CMOR tables repository to register your consortium](https://github.com/PCMDI/mip-cmor-tables/issues/new?assignees=&labels=add_consortium&projects=&template=add-consortium.md&title=New+Consortium). 
    The template should be straightforward.
    If there are any issues, just make the issue and tag @znichollscr.
    If you have any issues with this, feel free to [make a general issue](https://github.com/pcmdi/mip-cmor-tables/issues/new?assignees=&labels=&projects=&template=default.md&title=Help+needed+to+register+ROR+for+institute+X)
    and tag @znichollscr.

#### Register your source ID

The next step is to register your source ID.
This requires you to make a pull request 
that adds your information to `CVs/input4MIPs_source_id.json`.
The fields are generally self-explanatory.
If you have any questions, please tag @durack1 or @znichollscr in your pull request.

(data-validation)=
#### Data validation

This is not strictly a step that you, as a data producer, have to perform.
However, it will be performed, so you will have to pass validation eventually
(the iteration time is just slower if you don't run the validation yourself).

For validating the data, we use [input4mips-validation](https://github.com/climate-resource/input4mips_validation).
This checks the data's metadata against the CVs, 
makes sure that the data can be loaded with the common python tools 
[xarray](https://docs.xarray.dev/en/stable/index.html) 
and [iris](https://scitools-iris.readthedocs.io/en/stable/index.html)
and also runs the data through the [cfchecker](https://github.com/cedadev/cf-checker).
Any issues that are found will be reported in the data upload issue that you made previously.

[TODO: update all of the below once input4mips-validation is set up properly]
If you wish to run this yourself, please follow [the installation instructions](https://input4mips-validation.readthedocs.io/en/latest/#installation).
An example of the data validation process can be found in [the data validation demo notebook](www.tbd.invalid).
If you have any issues, 
please [raise them in the input4mips-validation repository](https://github.com/climate-resource/input4mips_validation/issues/new/choose).

#### Get your data to PCMDI

The first step here is to [create a new issue in this repository](https://github.com/PCMDI/input4MIPs_CVs/issues/new)
and tag @durack1 and @znichollscr so that they know that the data is being uploaded.

In terms of actually uploading the data, there isn't a strict process for this right now.
There are a few different options, which we list below in order of preference:

##### Upload to PCMDI's FTP server

The preferred option is to upload the data to PCMDI's FTP server.
The server's details are below:

- address: "ftp.llnl.gov"
- username: "anonymous"
- password: please use your email as the password, i.e. something like "me@institute.com"
- root directory for uploads: "incoming"

If it is helpful, @znichollscr has a script which they use for uploads 
[here](https://github.com/climate-resource/CMIP-GHG-Concentration-Generation/blob/main/scripts/upload-to-ftp-server.py).
Feel free to copy that (or use it as is) to upload your own files.

##### Upload to somewhere else

Alternately, you can upload your files to a cloud service (e.g. Google Drive, Amazon S3, a file transfer service).
Once you have done this, please paste the link 
from which to download your files in the issue related to uploading the data that you made previously.
Your files will be downloaded to the relevant place by someone else (likely @durack1).

#### Publishing

This is not a step that you, as a data producer, will perform.
However, for completeness, once the data has been received and passed validation,
it will be published on the ESGF.
Once this is done, this repository's maintainers will add it to our database in `DatasetsDatabase`.
This is not something that you, as a data producer, need to do.
However, feel free to check the records that have been made
and [make an issue](https://github.com/PCMDI/input4MIPs_CVs/issues/new)
if you see any problems.

## Contributors

[![Contributors](https://contrib.rocks/image?repo=PCMDI/input4MIPs_CVs)](https://github.com/PCMDI/input4MIPs_CVs/graphs/contributors)

Thanks to our contributors!

## Acknowledgement

The repository content has been collected from many contributors representing the input datasets for Model Intercomparison Projects (input4MIPs), including those from climate modeling groups and model intercomparison projects (MIPs) worldwide. The structure of content and tools required to maintain it was developed by climate and computer scientists from the Program for Climate Model Diagnosis and Intercomparison ([PCMDI](https://pcmdi.llnl.gov/)) at Lawrence Livermore National Laboratory ([LLNL](https://www.llnl.gov/)), and the Coupled Model Intercomparison Project International Project Office ([CMIP-IPO](https://wcrp-cmip.org/cmip-governance/project-office/)), with assistance from a large and expanding international community.

This work is sponsored by the Regional and Global Model Analysis ([RGMA](https://climatemodeling.science.energy.gov/program/regional-global-model-analysis)) program of the Earth and Environmental Systems Sciences Division ([EESSD](https://science.osti.gov/ber/Research/eessd)) in the Office of Biological and Environmental Research ([BER](https://science.osti.gov/ber)) within the Department of Energy's ([DOE](https://www.energy.gov/)) Office of Science ([OS](https://science.osti.gov/)). The work at PCMDI is performed under the auspices of the U.S. Department of Energy by Lawrence Livermore National Laboratory under Contract DE-AC52-07NA27344.

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
    >
</p>
