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

## Generating the database

In `Database/input-data` there are two components:

1. The file `esgf-input4IMPs.json`
1. The directory `Database/input-data/pmount`

`Database/input-data/esgf-input4IMPs.json` is a scrape of information from the ESGF index.
This captures the latest set of information we have queried from the ESGF index database.
It is automatically updated on nimbus using `scripts/pollESGF.py`.
The latest scrape from nimbus can be turned into a merge request using
`scripts/check-esgf-scrape.sh`
(for the script to run to completion,
you need to have logged in with GitHub,
if you don't do that,
you can just make the merge request by hand).

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
