# Contributing

Contributing to the repository beyond the instructions above is currently a dark art.
A start is the description below.
We hope to improve these docs over time.

## Updating the version

We use the `bump` GitHub action to control the updating of our repository's version.
As a result, you shouldn't need to update the repository's version information by hand.
Under the hood, this action uses the command-line tool in
`python-packages/input4MIPs-CVs/src/input4MIPs_CVs/cli/version.py`.
This command-line tool ensures that the version is applied to all relevant places in the repository
and also provides an interface to bump the version.

## The database

In `Database/input-data` there are three components:

1. The file `esgf-input4MIPs.json`
1. The directory `Database/input-data/pmount`
1. The file `Database/input-data/supplementary-source-id-info.yaml`

`Database/input-data/esgf-input4MIPs.json` is a scrape of information from the ESGF index.
This captures the latest set of information we have queried from the ESGF index database.
It is generated with `scripts/pollESGF.py` (the process is auto-run every 6-hrs on perlmutter).
We hope to switch to automated generation of this file in the future
(see [#69](https://github.com/PCMDI/input4MIPs_CVs/issues/69)).

If running on perlmutter, to update this file, simply copy the latest output into this repository.
On perlmutter, the command is:

```sh
cp /PATH-TO-DATA-ROOT/input4MIPs/esgf-input4MIPs.json Database/input-data/esgf-input4MIPs.json
/PATH-TO-DATA-ROOT/ = /global/cfs/projectdirs/m4931/gsharing/user_pub_work/input4MIPs
```

To update the file locally, simply run the script.
you may need to have an environment activated with needed dependencies
(e.g. `requests` before you can run this).
The command is:

```sh
python scripts/pollESGF.py Database/input-data/esgf-input4MIPs.json
```

`Database/input-data/pmount` contains a number of JSON files.
Each file contains information about one file
from the raw netCDF files in the input4MIPs project.
The raw netCDF files are stored elsewhere.
The database entries are managed using the scripts in
`scripts/pmount-database-generation`.
See `scripts/pmount-database-generation/README.md`
for further details.

`Database/input-data/supplementary-source-id-info.yaml`
contains supplementary information about our data.
This is data that cannot be scraped from ESGF or the files,
usually because it is only known after publication of the data
(e.g. reasons for later deprecation of the data).
At the moment, the fixes are applied at the source ID level.
If you need finer-grained control, add in a new source.

At present, we are tracking all of these inputs as part of this repository.
This is ok for now, as the data is relatively small.
This may not scale, so if we get to a certain size, we may have to pick a different approach.

The data from these three inputs, plus information from the Controlled Vocabularies (CVs),
gets combined to create `Database/input4MIPs_db_file_entries.json`.
This combination is done using `python-packages/input4MIPs-CVs/src/input4MIPs_CVs/cli/update-database.py`.
In order to run this script, you should:

1. Make a virtual environment (e.g. `python3 -m venv venv`)
2. Activate the virtual environment (e.g. `source venv/bin/activate` - be careful not to activate multiple envs at once!)
3. Install the requirements into the environment
   (e.g. `pip install -r dev-requirements.txt`)
4. Run the script e.g. `python python-packages/input4MIPs-CVs/src/input4MIPs_CVs/cli/update-database.py --repo-root-dir .`

## Generating the HTML pages

Having generated the database, we can then generate the HTML views of it.
Currently, the HTML pages are generated using 
`python-packages/input4MIPs-CVs/src/input4MIPs_CVs/cli/update-html-pages.py`.
In order to run this script, you should:

1. Reuse the existing `venv` environment (see above), or remake one (e.g. `python3 -m venv venv`)
2. Activate the virtual environment (e.g. `source venv/bin/activate`)
3. Install the requirements into the environment
   (e.g. `pip install -r dev-requirements.txt`)
4. Run the script 
   e.g. `python python-packages/input4MIPs-CVs/src/input4MIPs_CVs/cli/update-html-pages.py --repo-root-dir .`

The version is automatically read out of the `VERSION` file if it is not directly specified.

## Summary of steps required to update this repository when a new data source is published on ESGF

This is based on the sections above.
The paths assume you are working on perlmutter.
If you are working elsewhere, you may need to modify the paths slightly.

1. Checkout a new branch from main
1. Update the ESGF scrape: `python scripts/pollESGF.py Database/input-data/esgf-input4MIPs.json`
    - you may need to have an environment activated with needed requirements (e.g. `requests` before you can run this)
    - alternatively on perlmutter copy the existing file: `cp /PATH-TO-DATA-ROOT/input4MIPs/esgf-input4MIPs.json Database/input-data/esgf-input4MIPs.json`
1. Activate an environment in which `input4mips-validation` is installed
1. Update the database by adding the tree you're interested in. 
   Do this by running the following command from the root of this repository: 
   `bash scripts/pmount-database-generation/db-add-tree.sh <root-of-tree-to-add>` 
   e.g. `bash scripts/pmount-database-generation/db-add-tree.sh /PATH-TO-DATA-ROOT/input4MIPs/CMIP6Plus/CMIP/UofMD/`
1. (Not compulsory, but recommended because it makes it easier to see changes later) 
   Commit the changes to the database
1. If needed, add the source ID entry for the new files to `CVs/input4MIPs_source_id.json`
1. Activate an environment which has the local requirements installed
    - Make a virtual environment (e.g. `python3 -m venv venv`)
    - Activate the virtual environment (e.g. `source venv/bin/activate` - be careful not to activate multiple envs at once!)
    - Install the requirements into the environment (e.g. `pip install -r dev-requirements.txt`)
1. Update the database: `python python-packages/input4MIPs-CVs/src/input4MIPs_CVs/cli/update-database.py --repo-root-dir .`
    - If needed, add a reason for the retraction/deprecation of the previous data set in `Database/input-data/supplementary-source-id-info.yaml`
1. Update the HTML pages: `python python-packages/input4MIPs-CVs/src/input4MIPs_CVs/cli/update-html-pages.py --repo-root-dir .`
    - If you get an error about a retracted publication status, you'll need to edit the latest source ID being used for a given dataset. Use the python traceback to help you identify where this is. (TODO: move things into a standalone file so it is easier to see what to edit)
1. Check that the HTML has updated as expected 
   (e.g. the summary view has updated as expected, new datasets are in the datasets view, new files are in the files view)
1. Commit everything
1. Build the docs: `mkdocs build --strict`
1. Check that the docs updated as expected.
   A few of the auto-generated components are worth checking here:

    - are the source IDs for the dataset up to date?
      E.g. do we need to update the source IDs to be used for the various CMIP7 phases in
      `docs/dataset-info/cmip7-phases-source-ids.json`
      or the delivery summary in `docs/dataset-info/delivery-summary.json`?
    - did the relevant documentation page (e.g. `docs/dataset-overviews/population.md`) update correctly?
      If yes, there is an issue. Check the page carefully e.g. the `source_id_stub` at the top of the page
      (figuring out the logic here will likely require stepping through the python as it is still an evolving process).
    - did the revision history come through correctly? If not, there is an issue.

1. Commit everything
1. Push
1. Make a pull request
1. Request a review from @znichollscr and/or @durack1
1. Update based on review
1. Merge
1. Tag @eleanororourke and @vnaik60 so they know a new update is live (e.g. "Hi @eleanororourke @vnaik60 just making sure you've seen this, thanks!")
1. Celebrate
1. Begin work on your update on v-next

## Relationship to input4MIPs validation

This repository contains the database and Controlled Vocabularies (CVs).
The [input4MIPs validation](https://github.com/climate-resource/input4mips_validation)
package implements the logic for validating data, based on the CVs.
The two are deliberately decoupled, to allow the logic captured within
input4IMPs validation to potentially be reused in other parts of the CMIP universe in future.
We have a CI job which checks that the CVs in this repository can be loaded using input4MIPs validation.
If this job fails, it is ok to still merge the merge requests.
It is just a reminder to us that we have to update input4MIPs validation
to support whatever changes to the CVs have been made.
