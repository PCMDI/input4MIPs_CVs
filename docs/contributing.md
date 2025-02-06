# Contributing

Contributing to the repository beyond the instructions above
is currently a dark art.
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

In `Database/input-data` there are two components:

1. The file `esgf-input4MIPs.json`
1. The directory `Database/input-data/pmount`

`Database/input-data/esgf-input4MIPs.json` is a scrape of information from the ESGF index.
This captures the latest set of information we have queried from the ESGF index database.
It is generated with `scripts/pollESGF.py`.
However, the API it queries only allows certain IP addresses,
so you will only be able to run this if you have been given access.
We hope to switch to automated generation of this file in future
(see [#69](https://github.com/PCMDI/input4MIPs_CVs/issues/69)).

To update this file, simply copy the latest output from the poll script into this repository.
On nimbus, the command is:

```sh
cp /p/user_pub/work/input4MIPs/esgf-input4MIPs.json Database/input-data/esgf-input4MIPs.json
```

`Database/input-data/pmount` contains a number of JSON files.
Each file contains information about one file
from the raw netCDF files in the input4MIPs project.
The raw netCDF files are stored elsewhere.
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

## Generating the HTML pages

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

## Summary of steps required to update this repository when a new data source is published on ESGF

This is based on the sections above.
The paths assume you are working on nimbus.
If you are working elsewhere, you may need to modify the paths slightly.

1. Checkout a new branch from main
1. Update the ESGF scrape: `cp /p/user_pub/work/input4MIPs/esgf-input4MIPs.json Database/input-data/esgf-input4MIPs.json`
1. Activate an environment in which `input4mips-validation` is installed
1. Update the database by adding the tree you're interested in. Do this by running the following command from the root of this repository: `bash scripts/pmount-database-generation/db-add-tree.sh <root-of-tree-to-add>` e.g. `bash scripts/pmount-database-generation/db-add-tree.sh /p/user_pub/work/input4MIPs/CMIP6Plus/CMIP/UofMD/`
1. (Not compulsory, but recommended because it makes it easier to see changes later) Commit the changes to the database
1. If needed, add the source ID entry for the new files to `CVs/input4MIPs_source_id.json`
1. Activate an environment which has the local `input4IMPs-CVs` package installed (see intructions on how to create such an environment in the sections above)
1. Update the database: `python python-packages/input4MIPs-CVs/src/input4MIPs_CVs/cli/update-database.py --repo-root-dir .`
1. Update the HTML pages: `python python-packages/input4MIPs-CVs/src/input4MIPs_CVs/cli/update-html-pages.py --repo-root-dir .`
    - If you get an error about a retracted publication status, you'll need to edit the latest source ID being used for a given dataset. Use the python traceback to help you identify where this is. (TODO: move things into a standalone file so it is easier to see what to edit)
1. Check that the HTML has updated as expected (e.g. the summary view has updated as expected, new datasets are in the datasets view, new files are in the files view)
1. Commit everything
1. Build the docs: `mkdocs build --strict`
1. Check that the docs updated as expected.
   A few of the auto-generated components are worth checking here:

    - are the source IDs for the dataset up to date?
      E.g. do we need to update the source IDs to be used for the various CMIP7 phases in
      `docs/dataset-info/cmip7-phases-source-ids.json`?
    - did the revision history come through correctly? If not, there is an issue.

1. Commit everything
1. Push
1. Make a pull request
1. Request a review from @znichollscr and/or @durack1
1. Update based on review
1. Merge
1. Tag @eleanororourke and @vnaik60 so they know a new update is live (e.g. "Hi @eleanororourke @vnaik60 just making sure you've seen this, thanks!")
1. Celebrate

## Relationship to input4MIPs validation

This repository contains the database and controlled vocabularies.
The [input4MIPs validation](https://github.com/climate-resource/input4mips_validation)
package implements the logic for validating data, based on the CVs.
The two are deliberately decoupled, to allow the logic captured within
input4IMPs validation to potentially be reused in other parts of the CMIP universe in future.
We have a CI job which checks that the CVs in this repository can be loaded using input4MIPs validation.
If this job fails, it is ok to still merge the merge requests.
It is just a reminder to us that we have to update input4MIPs validation
to support whatever changes to the CVs have been made.
