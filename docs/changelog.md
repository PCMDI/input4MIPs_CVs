# Changelog

The version number takes the form X.Y.Z, but does not completely follow semantic versioning.
The major number, X, is the CMIP generation we are targeting.
At the moment, this is 6, soon (hopefully Jan 2025) it will be 7.
The minor number, Y, is incremented for breaking changes to the CVs.
The patch number, Z, is incremented for all other changes.

Backward incompatible (breaking) changes will only be introduced in major or minor versions.


<!--
You should *NOT* be adding new changelog entries to this file, this
file is managed by towncrier. See changelog/README.md.

You *may* edit previous changelogs to fix problems like typo corrections or such.
To add a new changelog entry, please see
https://pip.pypa.io/en/latest/development/contributing/#news-entries,
noting that we use the `changelog` directory instead of news, md instead
of rst and use slightly different categories.
-->

<!-- towncrier release notes start -->

## input4MIPs CVs v6.5.22 (2024-10-18)


### 📚 Improved Documentation

- - Added a placeholder for population inputs.
  - Increased the default number of entries shown on the table views to 25 to accomodate the new dataset.

  ([#132](https://github.com/PCMDI/input4MIPs_CVs/pull/132))
- - Updated DRES-CMIP-BB4CMIP7-1-0 dataset status.
  - Added scripts/pmount-database-generation/db-add-tree-bb-workaround.sh to deal with <variable_id> format inconsistency for 4 DRES datasets.

  ([#134](https://github.com/PCMDI/input4MIPs_CVs/pull/134))

### 🔧 Trivial/Internal Changes

- [#129](https://github.com/PCMDI/input4MIPs_CVs/pull/129), [#130](https://github.com/PCMDI/input4MIPs_CVs/pull/130), [#131](https://github.com/PCMDI/input4MIPs_CVs/pull/131)


## input4MIPs CVs v6.5.21 (2024-10-04)


### ⚠️ Breaking Changes

- Re-named the ESGF scrape from `Database/input-data/esgf.json` to `Database/input-data/esgf-input4MIPs.json`. ([#113](https://github.com/PCMDI/input4MIPs_CVs/pull/113))

### 🆕 Features

- Added the UOEXETER-CMIP-1-1-2 source ID. ([#117](https://github.com/PCMDI/input4MIPs_CVs/pull/117))
- Added source IDs for the anthropogenic emissions data. ([#119](https://github.com/PCMDI/input4MIPs_CVs/pull/119))
- Added the published volcanic University of Exeter (UOEXETER-CMIP-1-1-3) entries ([#120](https://github.com/PCMDI/input4MIPs_CVs/pull/120))
- Registered the "UofMD-landState-3-0" source ID. University of Maryland is providing land-use change relevant variables. ([#121](https://github.com/PCMDI/input4MIPs_CVs/pull/121))

### 📚 Improved Documentation

- Moved most of the `README`'s content into the docs.
  This helps avoid broken links in future,
  because links don't always play nice with GitHub's homepage rendering. ([#109](https://github.com/PCMDI/input4MIPs_CVs/pull/109))
- Added a delivery summary view to our docs.
  This provides information about when different datasets are expected to be delivered. ([#111](https://github.com/PCMDI/input4MIPs_CVs/pull/111))
- Update the delivery status view of the datasets. ([#119](https://github.com/PCMDI/input4MIPs_CVs/pull/119))
- Updated the status of dataset publication. ([#126](https://github.com/PCMDI/input4MIPs_CVs/pull/126))
- - Added land-use change information now that it's published on ESGF.
  - Clarified the ESGF publication status in the delivery summary view.

  ([#127](https://github.com/PCMDI/input4MIPs_CVs/pull/127))

### 🔧 Trivial/Internal Changes

- [#108](https://github.com/PCMDI/input4MIPs_CVs/pull/108), [#116](https://github.com/PCMDI/input4MIPs_CVs/pull/116), [#119](https://github.com/PCMDI/input4MIPs_CVs/pull/119), [#122](https://github.com/PCMDI/input4MIPs_CVs/pull/122), [#127](https://github.com/PCMDI/input4MIPs_CVs/pull/127)


## input4MIPs CVs v6.5.20 (2024-08-19)


### 🆕 Features

- Added post-publication note that explains why SOLARIS-HEPPA-CMIP-4-2 was deprecated. ([#91](https://github.com/PCMDI/input4MIPs_CVs/pull/91))
- Added the "never_published" publication status. Applied this to the SOLARIS-HEPPA-4-1 dataset. ([#95](https://github.com/PCMDI/input4MIPs_CVs/pull/95))

### 🐛 Bug Fixes

- Manually added a fix to the licence ID for `MRI-JRA55-do-1-6-0`, `PCMDI-AMIP-1-1-9`, `SOLARIS-HEPPA-CMIP-4-2` and `SOLARIS-HEPPA-CMIP-4-3`.
  Note that this fix appears in the database only.
  The underlying file entries in `Database/input-data/pmount` still reflect the files as they appear on disk. ([#94](https://github.com/PCMDI/input4MIPs_CVs/pull/94))

### 📚 Improved Documentation

- Added the post-publication comment to the datasets view. ([#91](https://github.com/PCMDI/input4MIPs_CVs/pull/91))
- Added a source ID level HTML table view. See `docs/input4MIPs_source-id_CMIP6Plus.html`. ([#92](https://github.com/PCMDI/input4MIPs_CVs/pull/92))
- Added links to our different database views to our README and as the header of our HTML pages.
  Also made the "latest" column more obvious in our database views.
  Also tried to use "input4MIPs" rather than "Input4MIPs" throughout. ([#95](https://github.com/PCMDI/input4MIPs_CVs/pull/95))
- Add Read the Docs build of the docs. ([#105](https://github.com/PCMDI/input4MIPs_CVs/pull/105))

### 🔧 Trivial/Internal Changes

- [#69](https://github.com/PCMDI/input4MIPs_CVs/pull/69), [#103](https://github.com/PCMDI/input4MIPs_CVs/pull/103), [#104](https://github.com/PCMDI/input4MIPs_CVs/pull/104), [#106](https://github.com/PCMDI/input4MIPs_CVs/pull/106)


## input4MIPs CVs v6.5.19 (2024-08-14)


### ⚠️ Breaking Changes

- Re-named "long_name" to "full_name" in `CVs/input4MIPs_target_mip.json` ([#78](https://github.com/PCMDI/input4MIPs_CVs/pull/78))

### 🆕 Features

- Registered the "UOEXETER-CMIP-0-1-0" source ID.
  University of Exeter is providing volcanic eruption relevant variables (emissions and aerosol optical properties). ([#83](https://github.com/PCMDI/input4MIPs_CVs/pull/83))
- - Added published SOLARIS-HEPPA-4-3 files.

  - Added support for the removal of dataset placeholders to our database updating tool.

  ([#84](https://github.com/PCMDI/input4MIPs_CVs/pull/84))
- Added CR-CMIP-0-3-0 files to our database. ([#85](https://github.com/PCMDI/input4MIPs_CVs/pull/85))

### 📚 Improved Documentation

- Fixed reference to how validation is performed using input4MIPs in the README ([#74](https://github.com/PCMDI/input4MIPs_CVs/pull/74))
- Remove placeholder dataset entries from the files view (`docs/input4MIPs_files_CMIP6Plus.html`) ([#79](https://github.com/PCMDI/input4MIPs_CVs/pull/79))
- Updated docs about updating the database and generating the HTML files. ([#84](https://github.com/PCMDI/input4MIPs_CVs/pull/84))

### 🔧 Trivial/Internal Changes

- [#81](https://github.com/PCMDI/input4MIPs_CVs/pull/81), [#83](https://github.com/PCMDI/input4MIPs_CVs/pull/83), [#84](https://github.com/PCMDI/input4MIPs_CVs/pull/84)


## input4MIPs CVs v6.5.18 (2024-08-05)


No significant changes.


## input4MIPs CVs v6.5.17 (2024-08-05)


No significant changes.


## input4MIPs CVs v6.5.16 (2024-08-05)


No significant changes.


## input4MIPs CVs v6.5.15 (2024-08-05)


No significant changes.


## input4MIPs CVs v6.5.14 (2024-08-05)


No significant changes.


## input4MIPs CVs v6.5.13 (2024-08-05)


### 🔧 Trivial/Internal Changes

- [#73](https://github.com/PCMDI/input4MIPs_CVs/pull/73)


## input4MIPs CVs v6.5.12 (2024-08-05)


No significant changes.


## input4MIPs CVs v6.5.11 (2024-08-05)


### 🔧 Trivial/Internal Changes

- [#72](https://github.com/PCMDI/input4MIPs_CVs/pull/72)
