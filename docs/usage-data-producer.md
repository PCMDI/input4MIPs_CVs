# Usage as a data producer

As a data producer, there are a few key steps.

## Register your institution ID

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
     [WCRP universe repository to note this](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=BLANK_ISSUE)
     and tag @znichollscr.

    b. if your organisation does have an ROR, please make an issue in the
     [WCRP universe repository to register your institution](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=add_institution.yml)
     The template should be straightforward.
     If there are any issues, just make the issue and tag @znichollscr.
     If you have any issues with this, feel free to
     [make a general issue](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=BLANK_ISSUE)
     and tag @znichollscr.

1. (optional, but recommend) if you supply your data as part of a consortium, then there is an extra step

  - firstly, make sure that all institutes in your consortium have registered their RORs in the WCRP universe
    in the same way that you did for your institute in the previous step.

  - then, please make an issue in the [WCRP universe repository to register your consortium](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=BLANK_ISSUE). 
    The data we will need will be the same as
    [what is here](https://github.com/WCRP-CMIP/WCRP-universe/blob/esgvoc/consortium/solaris-heppa.json).
    If you have any issues with this, feel free to [make a general issue](https://github.com/WCRP-CMIP/WCRP-universe/issues/new?template=BLANK_ISSUE)
    and tag @znichollscr.

## Register your source ID

The next step is to register your source ID.
This requires you to make a pull request 
that adds your information to `CVs/input4MIPs_source_id.json`.
The fields are generally self-explanatory.
If you have any questions, please tag @durack1 or @znichollscr in your pull request.

## Data validation

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

## Get your data to PCMDI

The first step here is to [create a new issue in this repository](https://github.com/PCMDI/input4MIPs_CVs/issues/new)
and tag @durack1 and @znichollscr so that they know that the data is being uploaded.

In terms of actually uploading the data, there isn't a strict process for this right now.
There are a few different options, which we list below in order of preference:

### Upload to PCMDI's FTP server (preferred)

The preferred option is to upload the data to PCMDI's FTP server.
The server's details are below:

- address: "ftp.llnl.gov"
- username: "anonymous"
- password: please use your email as the password, i.e. something like "me@institute.com"
- root directory for uploads: "incoming"

If it is helpful, input4MIPs validation provides a tool for this.
See [How to upload to an FTP server](https://input4mips-validation.readthedocs.io/en/latest/how-to-guides/how-to-upload-to-ftp/).

### Upload to somewhere else (not preferred)

Alternatively, you can upload your files to a cloud service (e.g. Google Drive, Amazon S3, a file transfer service).
Once you have done this, please paste the link 
from which to download your files in the issue related to uploading the data that you made previously.
Your files will be downloaded to PCMDI by someone else (likely @durack1).

## Publishing

This is not a step that you, as a data producer, will perform.
However, for completeness, once the data has been received and passed validation,
it will be published on the ESGF and into the [input4MIPs project](https://aims2.llnl.gov/search?project=input4MIPs).
Once this is done, the repository maintainers will add it to our database in `Database`.
This is not something that you, as a data producer, need to do.
However, feel free to check the records that have been made (see HTML links above)
and [make an issue](https://github.com/PCMDI/input4MIPs_CVs/issues/new)
if you see any problems.
