# Database views

Here we provide different views of our database.
The full database contains more information than is needed for most use cases.
Hence, we provide views with less data that are tailored to common use cases.
You can also, of course, make your own view 
by simply reading the database file in 
`Database/input4MIPs_db_file_entries.json` yourself.

Before continuing, it is important to note that we distinguish between two different MIP eras.
The CMIP6Plus MIP era is the label used for all data that is to be used for testing purposes.
No data in the CMIP6Plus MIP era should be used for production simulations.
The CMIP7 MIP era is the label used for data that is suitable to use for CMIP7 production simulations.

- [Delivery summary view](input4MIPs_delivery-summary.html):
  Provides information about the expected delivery time of the different datasets.
  This provides very little information about the data,
  but does provide the key information about when data will be made available.
  If you are a data user, this is probably the view to bookmark.
  As data becomes available, you can then dive into the other views
  to get more detail about what the data actually contains.
  There are (or will be) of order twenty entries in this view.
- [Source ID-level view](input4MIPs_source-id_CMIP7.html):
  Provides information about the status of different source IDs
    (for the most relevant, i.e. CMIP7, collection).
  In essence, this is the status at the dataset provider level.
  There are (or will be) of order twenty entries in this view.
- [Dataset-level view](input4MIPs_datasets_CMIP7.html):
  Provides information at the level of a dataset,
  i.e. the information is disaggregated
  with one row for each variable
  (essentially) in the database.
  There are (or will be) of order one thousand entries in this view.
- [File-level view](input4MIPs_files_CMIP7.html):
  Provides information at the level of individual files.
  There is one row per file.
  This view also includes every column in our database.
  Hence, it contains all information in the database.
  It is much more difficult to navigate than the other views
  because it contains too much information for most use cases.
- [Source ID-level view CMIP6Plus](input4MIPs_source-id_CMIP6Plus.html):
  Provides information about the status of different source IDs in the CMIP6Plus collection.
  In essence, this is the status at the dataset provider level.
  There are (or will be) of order twenty entries in this view.
- [Dataset-level view CMIP6Plus](input4MIPs_datasets_CMIP6Plus.html):
  Provides information at the level of a dataset for the CMIP6Plus collection,
  i.e. the information is disaggregated
  with one row for each variable
  (essentially) in the database.
  There are (or will be) of order one thousand entries in this view.
- [File-level view CMIP6Plus](input4MIPs_files_CMIP6Plus.html):
  Provides information at the level of individual files for the CMIP6Plus collection.
  There is one row per file.
  This view also includes every column in our database.
  Hence, it contains all information in the database.
  It is much more difficult to navigate than the other views
  because it contains too much information for most use cases.

If there is another view that you would find helpful,
please feel free to [raise an issue](https://github.com/PCMDI/input4MIPs_CVs/issues/new)
to discuss.
