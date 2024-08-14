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

## Input4MIPs CVs v6.5.19 (2024-08-14)


### ⚠️ Breaking Changes

- Re-named "long_name" to "full_name" in `CVs/input4MIPs_target_mip.json` ([#78](https://github.com/PCMDI/Input4MIPs_CVs/pull/78))

### 🆕 Features

- Registered the "UOEXETER-CMIP-0-1-0" source ID.
  University of Exeter is providing volcanic eruption relevant variables (emissions and aerosol optical properties). ([#83](https://github.com/PCMDI/Input4MIPs_CVs/pull/83))
- - Added published SOLARIS-HEPPA-4-3 files.

  - Added support for the removal of dataset placeholders to our database updating tool.

  ([#84](https://github.com/PCMDI/Input4MIPs_CVs/pull/84))
- Added CR-CMIP-0-3-0 files to our database. ([#85](https://github.com/PCMDI/Input4MIPs_CVs/pull/85))

### 📚 Improved Documentation

- Fixed reference to how validation is performed using input4MIPs in the README ([#74](https://github.com/PCMDI/Input4MIPs_CVs/pull/74))
- Remove placeholder dataset entries from the files view (`docs/input4MIPs_files_CMIP6Plus.html`) ([#79](https://github.com/PCMDI/Input4MIPs_CVs/pull/79))
- Updated docs about updating the database and generating the HTML files. ([#84](https://github.com/PCMDI/Input4MIPs_CVs/pull/84))

### 🔧 Trivial/Internal Changes

- [#81](https://github.com/PCMDI/Input4MIPs_CVs/pull/81), [#83](https://github.com/PCMDI/Input4MIPs_CVs/pull/83), [#84](https://github.com/PCMDI/Input4MIPs_CVs/pull/84)


## Input4MIPs CVs v6.5.18 (2024-08-05)


No significant changes.


## Input4MIPs CVs v6.5.17 (2024-08-05)


No significant changes.


## Input4MIPs CVs v6.5.16 (2024-08-05)


No significant changes.


## Input4MIPs CVs v6.5.15 (2024-08-05)


No significant changes.


## Input4MIPs CVs v6.5.14 (2024-08-05)


No significant changes.


## Input4MIPs CVs v6.5.13 (2024-08-05)


### 🔧 Trivial/Internal Changes

- [#73](https://github.com/PCMDI/Input4MIPs_CVs/pull/73)


## Input4MIPs CVs v6.5.12 (2024-08-05)


No significant changes.


## Input4MIPs CVs v6.5.11 (2024-08-05)


### 🔧 Trivial/Internal Changes

- [#72](https://github.com/PCMDI/Input4MIPs_CVs/pull/72)
