# Downloading data

Here we provide some examples of how to download data.
They are not meant to be exhaustive, but they may help.

## esgpull - commandline ESGF download software

It is possible to download datasets using [esgpull](https://esgf.github.io/esgf-download/).
The installation instructions are [here](https://esgf.github.io/esgf-download/installation/).

Having installed esgpull, make sure it is configured on your system with

```sh
esgpull self install
```

Then, we found that we had to set our data node correctly first
in order for esgpull to find input4MIPs data.

```sh
esgpull config api.index_node esgf-node.llnl.gov
```

Data can then be downloaded as shown below.
The key thing is to make sure that you are getting the source ID you are interested in.
(The below example uses the shell commands.
Obviously you can drive the shell in your programming language of choice,
which might be a more convenient option.)


```sh
CMIP7_VERSION_PROJECT="input4MIPs"
# The MIP era will need to be changed to "CMIP7" when the final data is published
# (for now, all testing data is published under "CMIP6Plus").
CMIP7_VERSION_MIP_ERA="CMIP6Plus"
# The source ID you're interested in.
CMIP7_VERSION_SOURCE_ID="CR-CMIP-0-4-0"
SEARCH_TAG="cmip7-${CMIP7_VERSION_SOURCE_ID}"

esgpull add --tag ${SEARCH_TAG} --track project:${CMIP7_VERSION_PROJECT} mip_era:${CMIP7_VERSION_MIP_ERA} source_id:${CMIP7_VERSION_SOURCE_ID}

esgpull update -y --tag ${SEARCH_TAG}

# Be careful before running this, it may download a lot of data.
# See below for how to restrict the search info.
esgpull download --tag ${SEARCH_TAG}
```

If you want to only download data of a specific type,
you can do that too.
For example, to only download global-, annual-mean greenhouse gas concentrations,
you can add the below.

```sh
GRID_LABEL="gn"
FREQUENCY="yr"
SEARCH_TAG="cmip7-${CMIP7_VERSION_SOURCE_ID}-${GRID_LABEL}-${FREQUENCY}"

esgpull add --tag ${SEARCH_TAG} --track project:${CMIP7_VERSION_PROJECT} mip_era:${CMIP7_VERSION_MIP_ERA} source_id:${CMIP7_VERSION_SOURCE_ID} grid_label:${GRID_LABEL} frequency:${FREQUENCY}

esgpull update -y --tag ${SEARCH_TAG}

esgpull download --tag ${SEARCH_TAG}
```

If you want to see this flow being used within a wider repository,
please see [https://github.com/climate-resource/CMIP6-vs-CMIP7-GHG-Concentrations]().

Unfortunately, there is no uniform set of flags that can be used across all datasets.
Please see the specific details of each dataset for details about each dataset.
For example, which grids and frequencies are available and what to use for the pre-industrial control experiments.
[The datasets overview page is here](../dataset-overviews/index.md).

## Directly from ESGF

The ESGF MetaGrid search interface (see [https://aims2.llnl.gov/search/input4MIPs]())
provides direct access to the ESGF-hosted datasets. 
This allows searching via search facets, 
e.g., `MIP Era`, `Target MIP` 
(where, for example, a target MIP of "CMIP" means the CMIP DECK activity, "ScenarioMIP" is the scenarios),
`Institution ID`, `Source ID`.

You can download directly by browsing down to file level.
Alternately, you can select a `wget` script which will download via the commandline 
- and will select all available files that comprise a dataset 
(a collection of files defined by a unique combination of the search facets).

By default, only the latest (non-deprecated, non-errata) data are listed in a search. 
In addition, you can also limit your search to a local ESGF node, 
for example `aims3.llnl.gov` or `esgf-data2.llnl.gov` on the West Coast of the USA, 
or `esgf1.dkrz.de` in Hamburg, Germany.
We are expecting more ESGF nodes to begin replicating these data as the project matures.
