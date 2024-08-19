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
