# Usage as a data user

The most important thing:
if there is something that isn't clear to you,
please [raise an issue](https://github.com/PCMDI/input4MIPs_CVs/issues/new)
(if you don't know who else to tag, please tag `@durack1` and `@znichollscr`).
If you have a question, it is very likely that someone else is asking the same thing
so please don't hesitate to ask.

## The datasets

An overview of each dataset, with links to further information,
can be found in [dataset overviews](../dataset-overviews/index.md).

## Navigating the database

The database tracks all of the files[^1] being managed in the input4MIPs project[^2].
In general, as a user, you won't be interested in information at the level of individual files,
hence we provide different views.
An overview of these is given in the
[database views homepage](../database-views/index.md).
Here we provide some more targeted guidance for users of the data.

[^1]: At the moment, just data from the 'CMIP6Plus' era, but we hope to expand this out to data from the CMIP6 era in future, and early in 2025 toward the final datasets for CMIP7 usage.
[^2]: Yes, this does somewhat duplicate the point of the ESGF index, but the ESGF index isn't publically accessible/queriable and doesn't have all the information we want right now, so here we are.

If you want to know about the latest status of each dataset,
have a look at [the delivery summary](../database-views/input4MIPs_delivery-summary_CMIP6Plus.html).
This page provides, for each forcing dataset:

- its current status (see the `Status` column)
- the unique identifier of its latest version (see the `Source ID` column)
- if the data has been published on ESGF (see the `ESGF publication status` column), 
  a hyperlink to a pre-filled search on the ESGF is included 
  (just click on the information in this column).
  The pre-filled search can help with downloading data and knowing what to search for on the ESGF.
- if the dataset has an external URL which provides more information,
  this is provided as a hyperlink on the forcing dataset's name
  (see the `Forcing dataset` column),
  i.e. if you can click on the forcing dataset's name,
  it will take you to that forcing dataset's home page, where ever that is.

### How can I get more information about each dataset?

Beyond the overviews above, you can also use the different views of our database.
If you are interested in the status of different versions of a particular dataset,
then it is worth looking at [the source ID level view](../database-views/input4MIPs_source-id_CMIP6Plus.html).
Within this view, the search bar can be used to filter just for the dataset you're interested in.
Once this filtering is done, a few columns are particularly relevant:

- `source_id` shows you the different versions of this dataset that have been released
- `latest` tells you whether the source ID is the latest version of this dataset or not
  (only one version can be latest)
- `publication_status` summarises the publication status of the version of the dataset.
  Data which is "published" is data which is still available for use
  (so, even if data is not latest, if it is published, 
  you can assume that no major errors have been identified yet).
  All other states indicate data which should no longer be used
  (either because it was never been published or because it has been retracted post-publication).

If you wish to dive even further, you can use
[the dataset level view](../database-views/input4MIPs_datasets_CMIP6Plus.html)
to get information at the level of individual datasets (generally, variable-level)
and [the file level view](../database-views/input4MIPs_files_CMIP6Plus.html)
to get information at the level of individual files (unlikely to be of use in the majority of cases).

### How can I provide feedback on an existing dataset?

We welcome comments and feedback on existing datasets, such analysis and review will uncover issues
that we are yet to identify, and once we know about an issue, it is far more likely it will get
attention and a resolution (and a shiny new dataset) will likely be generated to solve the issue.

To open a new issue, browse to the [input4MIPs_CVs issue page](https://github.com/PCMDI/input4MIPs_CVs/issues)
and open a new issue, preferably with a descriptive title that identifies the problem dataset by `source_id`
(e.g., PCMDI-AMIP-1-1-9). Alternatively, you can open a discussion [input4MIPs discussion page](https://github.com/PCMDI/input4MIPs_CVs/discussions)
to connect with the data providers, and other users about usage questions or other topics that don't warrant
an `issue` to be raised, yet - we can always convert a discussion to an issue if required.

To-date, we have already identified issues, and resolved problems with earlier versions of data,
and these previously existing issues are briefly described on the [input4MIPs source_id view](https://input4mips-cvs.readthedocs.io/en/latest/database-views/input4MIPs_source-id_CMIP6Plus.html)
search for `retracted` (top right hand search box), or some other criteria that caught issues
before data was made available on ESGF.

### How can I get informed when new data is published or errors with the data are identified?

You can "subscribe" to get notified of changes to content presented in this input4MIPs_CVs repository.
On the [homepage](https://github.com/PCMDI/input4MIPs_CVs/), there is a button titled "Watch", this
enables you to control the granularity of your notifications regarding changes to the repository
content. If you want more information, take a peek at the [Configuring Notifications](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications)
page on GitHub.

## input4MIPs Controlled Vocabularies (CVs)

It is unlikely that you will need to use the CVs directly,
although they may be helpful for understanding what the different terms mean
(and this metadata capturing and clarity will improve over time 
as we make greater and greater use of 
[json-ld](https://json-ld.org/) following the work by the central CMIP team).
