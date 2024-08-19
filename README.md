<!--- --8<-- [start:description] -->
# input4MIPs Controlled Vocabularies (CVs)

[![Latest release](https://img.shields.io/badge/Latest%20release-v6.5.20-brightgreen.svg)](https://github.com/PCMDI/input4MIPs_CVs/releases/tag/v6.5.20)
[![DOI (all versions)](https://zenodo.org/badge/doi/10.5281/zenodo.12629796.svg)](https://zenodo.org/doi/10.5281/zenodo.12629796)
[![Docs](https://readthedocs.org/projects/input4mips-controlled-vocabularies-cvs/badge/?version=latest)](https://input4mips-controlled-vocabularies-cvs.readthedocs.io)

Controlled Vocabularies (CVs) for use in input4MIPs.
Full documentation can be found at: [input4mips-controlled-vocabularies-cvs.readthedocs.io](https://input4mips-controlled-vocabularies-cvs.readthedocs.io).

### THIS REPOSITORY IS CURRENTLY UNDER ACTIVE DEVELOPMENT

To see further information regarding forcing dataset development
for the Coupled Model Intercomparison Project (CMIP) activities,
please see the
[CMIP Forcing Task Team homepage](https://wcrp-cmip.org/cmip7-task-teams/forcings/).

For different, pre-prepared views of the database,
see 
[database views](https://input4mips-controlled-vocabularies-cvs.readthedocs.io/en/latest/database-views/).

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
see [database views](https://input4mips-controlled-vocabularies-cvs.readthedocs.io/en/latest/database-views/).

## Versioning

The easiest place to find the repository's version is currently `VERSION`.
The version string from this file should be consistent with the rest of the repository.
If you see a place where this is not applied consistently,
please [raise an issue](https://github.com/PCMDI/input4MIPs_CVs/issues/new)
to let us know.

The version number takes the form X.Y.Z, but does not completely follow semantic versioning.
The major number, X, is the CMIP generation we are targeting.
At the moment, this is 6, soon (hopefully Jan 2025) it will be 7.
The minor number, Y, is incremented for breaking changes to the CVs.
The patch number, Z, is incremented for all other changes.
All releases will have a unique version number and be tagged in the repository.
For all commits except tagged commits,
we append the version with "a1" to indicate 
that this state of the repository is not an official release,
instead, it is a work in progress pre-release.
Please treat these pre-release versions with more care,
because their version number does not correspond to a unique commit.

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
   is that they must only contain alphanumeric characters and hyphens only 
   (i.e. the characters a-z, A-Z, 0-9 and -).
   In your pull request, please tag @durack1 and @znichollscr.
   If you have any issues with this, feel free to [make a general issue](https://github.com/PCMDI/input4MIPs_CVs/issues/new)
   and tag @znichollscr.

1. (optional, but recommend) check if your institution has a research organisation registry (ROR) ID
   ([ROR search can be done here](https://ror.org/)).

    a. if your organisation does not have an ROR, please make an issue in the
     [MIP CMOR tables repository to note this](https://github.com/pcmdi/mip-cmor-tables/issues/new?assignees=&labels=&projects=&template=default.md&title=No+ROR+for+institute+X)
     and tag @znichollscr.

    b. if your organisation does have an ROR, please make an issue in the
     [MIP CMOR tables repository to register your institute](https://github.com/PCMDI/mip-cmor-tables/issues/new?assignees=&labels=add_institution&projects=&template=add-Institution.md&title=New+Institution).
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

If you wish to run this yourself, please follow 
[the how-to guide for preparing files for publication on ESGF](https://input4mips-validation.readthedocs.io/en/latest/how-to-guides/#how-can-i-prepare-my-input4mips-files-for-publication-on-esgf).
If you have any issues, 
please [raise them in the input4MIPs validation repository](https://github.com/climate-resource/input4mips_validation/issues/new/choose).

#### Get your data to PCMDI

The first step here is to [create a new issue in this repository](https://github.com/PCMDI/input4MIPs_CVs/issues/new)
and tag @durack1 and @znichollscr so that they know that the data is being uploaded.

In terms of actually uploading the data, there isn't a strict process for this right now.
There are a few different options, which we list below in order of preference:

##### Upload to PCMDI's FTP server (preferred)

The preferred option is to upload the data to PCMDI's FTP server.
The server's details are below:

- address: "ftp.llnl.gov"
- username: "anonymous"
- password: please use your email as the password, i.e. something like "me@institute.com"
- root directory for uploads: "incoming"

If it is helpful, input4MIPs validation provides a tool for this.
See [How to upload to an FTP server](https://input4mips-validation.readthedocs.io/en/latest/how-to-guides/how-to-upload-to-ftp/).

##### Upload to somewhere else (not preferred)

Alternatively, you can upload your files to a cloud service (e.g. Google Drive, Amazon S3, a file transfer service).
Once you have done this, please paste the link 
from which to download your files in the issue related to uploading the data that you made previously.
Your files will be downloaded to PCMDI by someone else (likely @durack1).

#### Publishing

This is not a step that you, as a data producer, will perform.
However, for completeness, once the data has been received and passed validation,
it will be published on the ESGF and into the [input4MIPs project](https://aims2.llnl.gov/search?project=input4MIPs).
Once this is done, the repository maintainers will add it to our database in `Database`.
This is not something that you, as a data producer, need to do.
However, feel free to check the records that have been made (see HTML links above)
and [make an issue](https://github.com/PCMDI/input4MIPs_CVs/issues/new)
if you see any problems.

## Contributing

Contributing to the repository beyond the instructions above
is currently a dark art.
A start is the description below.
We hope to improve these docs over time.

### Updating the version

We use the `bump` GitHub action to control the updating of our repository's version.
As a result, you shouldn't need to update the repository's version information by hand.
Under the hood, this action uses the command-line tool in
`python-packages/input4MIPs-CVs/src/input4MIPs_CVs/cli/version.py`.
This command-line tool ensures that the version is applied to all relevant places in the repository
and also provides an interface to bump the version.

### Generating the database

In `Database/input-data` there are two components:

1. The file `esgf.json`
1. The directory `Database/input-data/pmount`

`Database/input-data/esgf.json` is a scrape of information from the ESGF index.
This captures the latest set of information we have queried from the ESGF index database.
It is generated with `scripts/pollESGF.py`.
However, the API it queries only allows certain IP addresses,
so you will only be able to run this if you have been given access.
We hope to switch to automated generation of this file in future
(see [#69](https://github.com/PCMDI/input4MIPs_CVs/issues/69)).

`Database/input-data/pmount` contains a number of JSON files.
Each file contains information about one file
from the actual files in the input4MIPs project.
The actual files are stored elsewhere.
The database entries are managed using the scripts in
`scripts/pmount-database-generation`.
See `scripts/pmount-database-generation/README.md`
for futher details.

At present, we are tracking both of these inputs as part of this repository.
This is ok for now, as the data is relatively small.
This may not scale, so if we get to a certain size, we may have to pick a different approach.

The data from these two inputs, plus information from the CVS,
gets combined to create `Database/input4MIPs_db_file_entries.json`.
This combination is done using `python-packages/input4MIPs-CVs/src/input4MIPs_CVs/cli/update-database.py`.
In order to run this script, you should:

1. Make a virtual environment (e.g. `python3 -m venv venv`)
2. Activate the virtual environment (e.g. `source venv/bin/activate`)
3. Install the local `input4MIPs-CVs` package into the environment
   (e.g. `pip install -e python-packages/input4MIPs-CVs`)
4. Run the script e.g. `python python-packages/input4MIPs-CVs/src/input4MIPs_CVs/cli/update-database.py --repo-root-dir .`

### Generating the HTML pages

Having generated the database, we can then generate the HTML views of it.
Currently, the HTML pages are generated using 
`python-packages/input4MIPs-CVs/src/input4MIPs_CVs/cli/update-html-pages.py`.
In order to run this script, you should:

1. Make a virtual environment (e.g. `python3 -m venv venv`)
2. Activate the virtual environment (e.g. `source venv/bin/activate`)
3. Install the local `input4MIPs-CVs` package into the environment
   (e.g. `pip install -e python-packages/input4MIPs-CVs`)
4. Run the script e.g. `python python-packages/input4MIPs-CVs/src/input4MIPs_CVs/cli/update-html-pages.py --repo-root-dir .`

The version is automatically read out of the `VERSION` file if it is not directly specified.

## Contributors

[![Contributors](https://contrib.rocks/image?repo=PCMDI/input4MIPs_CVs)](https://github.com/PCMDI/input4MIPs_CVs/graphs/contributors)

Thanks to our contributors!

## Acknowledgement

The repository content has been collected from many contributors representing the input datasets for Model Intercomparison Projects (input4MIPs), including those from climate modeling groups and model intercomparison projects (MIPs) worldwide. The structure of content and tools required to maintain it was developed by climate and computer scientists from the Program for Climate Model Diagnosis and Intercomparison ([PCMDI](https://pcmdi.llnl.gov/)) at Lawrence Livermore National Laboratory ([LLNL](https://www.llnl.gov/)), [Climate Resource](https://www.climate-resource.com/), and the Coupled Model Intercomparison Project International Project Office ([CMIP-IPO](https://wcrp-cmip.org/cmip-governance/project-office/)), with assistance from a large and expanding international community.

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
    >&nbsp;
    <img src="https://raw.githubusercontent.com/PCMDI/input4MIPs_CVs/main/docs/assets/CR_Logo%20_Square_400x400.png"
         width="65"
         style="margin-right: 30px"
         title="Climate Resource"
         alt="Climate Resource"
    >
</p>
<!--- --8<-- [end:description] -->
