# Database views

Here we provide different views of our database.
The full database contains more information than is needed for most use cases.
Hence, we provide views with less data that are tailored to common use cases.
You can also, of course, make your own view 
by simply reading the database file in 
`Database/input4MIPs_db_file_entries.json` yourself.

- [Source ID-level view](input4MIPs_source-id_CMIP6Plus.html):
  Provides information about the status of different source IDs.
  In essence, this is the status at the dataset provider level.
  There are (or will be) of order twenty entries in this view.
- [Dataset-level view](input4MIPs_datasets_CMIP6Plus.html):
  Provides information at the level of a dataset,
  i.e. the information is disaggregated
  with one row for each variable
  (essentially) in the database.
  There are (or will be) of order one thousand entries in this view.
- [File-level view](input4MIPs_files_CMIP6Plus.html):
  Provides information at the level of individual files.
  There is one row per file.
  This view also includes every column in our database.
  Hence, it contains all information in the database.
  It is much more difficult to navigate than the other views
  because it contains too much information for most use cases.
