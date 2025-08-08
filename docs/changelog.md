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

## input4MIPs CVs v6.6.41 (2025-08-08)


### 🆕 Features

- Added data for CMIP7 AMIP boundary conditions: PCMDI-AMIP-1-1-10 ([#312](https://github.com/PCMDI/input4MIPs_CVs/pull/312))

### 🐛 Bug Fixes

- Fixed a logic error in how we determined publication status. This fixes the status of a number of datasets which were erroneously marked as retracted. ([#313](https://github.com/PCMDI/input4MIPs_CVs/pull/313))

### 📚 Improved Documentation

- Registered PCMDI-AMIP-1-1-10 in anticipation for new data publication for CMIP7
  Fixed PIK-CMIP-1-0-0 dataset_category type ([#305](https://github.com/PCMDI/input4MIPs_CVs/pull/305))
- Updated to indicate that PCMDI-AMIP-1-1-10 will be the source ID to use for CMIP7 ([#309](https://github.com/PCMDI/input4MIPs_CVs/pull/309))

### 🔧 Trivial/Internal Changes

- [#301](https://github.com/PCMDI/input4MIPs_CVs/pull/301)


## input4MIPs CVs v6.6.40 (2025-08-01)


### 🆕 Features

- Updated the ESGF scrape to reflect the shutdown of the LLNL node ([#285](https://github.com/PCMDI/input4MIPs_CVs/pull/285))


## input4MIPs CVs v6.6.39 (2025-07-16)


### 📚 Improved Documentation

- Updated the scrape of ESGF. The entries for PCMDI-AMIP-1-1-9 now point at esgf-node.ornl.gov, the non-replica datasets on ESGF (previously they pointed at eagle.alcf.anl.gov, which was a replica). ([#279](https://github.com/PCMDI/input4MIPs_CVs/pull/279))

### 🔧 Trivial/Internal Changes

- [#279](https://github.com/PCMDI/input4MIPs_CVs/pull/279)


## input4MIPs CVs v6.6.38 (2025-07-15)


### 🔧 Trivial/Internal Changes

- [#276](https://github.com/PCMDI/input4MIPs_CVs/pull/276), [#277](https://github.com/PCMDI/input4MIPs_CVs/pull/277), [#278](https://github.com/PCMDI/input4MIPs_CVs/pull/278)


## input4MIPs CVs v6.6.37 (2025-07-10)


### 📚 Improved Documentation

- Updated expected delivery date for ozone and nitrogen deposition forcings ([#274](https://github.com/PCMDI/input4MIPs_CVs/pull/274))


## input4MIPs CVs v6.6.36 (2025-07-09)


### 🆕 Features

- Added new source_id PIK-CMIP-1-0-0 in preparation for population data submission ([#258](https://github.com/PCMDI/input4MIPs_CVs/pull/258))
- Added information to the database for the population datasets ([#272](https://github.com/PCMDI/input4MIPs_CVs/pull/272))

### 🎉 Improvements

- Switched to scraping the ESGF index using a public API and updated the ESGF scrape in the process ([#264](https://github.com/PCMDI/input4MIPs_CVs/pull/264))

### 🐛 Bug Fixes

- Fixed CVs for population source ID (the authors had one list level too many) ([#272](https://github.com/PCMDI/input4MIPs_CVs/pull/272))

### 📚 Improved Documentation

- - Updated documentation for the population dataset 
  - Updated contributor documentation to reflect new workflows now that the the ESGF poll uses a public API ([#264](https://github.com/PCMDI/input4MIPs_CVs/pull/264))

  ([#270](https://github.com/PCMDI/input4MIPs_CVs/pull/270))
- - Updated the contributing docs to better reflect NERSC based workflows, point to the newly added environment file and add in the need to check `docs/dataset-info/delivery-summary.json` when adding a new source ID
  - Updated `docs/database-views/input4MIPs_delivery-summary_CMIP6Plus.html` so it is a simple redirect to `docs/database-views/input4MIPs_delivery-summary.html`

  ([#272](https://github.com/PCMDI/input4MIPs_CVs/pull/272))

### 🔧 Trivial/Internal Changes

- [#272](https://github.com/PCMDI/input4MIPs_CVs/pull/272)


## input4MIPs CVs v6.6.35 (2025-06-19)


### 🆕 Features

- Added high-resolution emissions data (published under source ID CEDS-CMIP-2025-04-18 with grid label "gr") ([#256](https://github.com/PCMDI/input4MIPs_CVs/pull/256))


## input4MIPs CVs v6.6.34 (2025-06-18)


### 🆕 Features

- Added CO2 isotopes data under source ID ImperialCollege-3-0 ([#240](https://github.com/PCMDI/input4MIPs_CVs/pull/240))


## input4MIPs CVs v6.6.33 (2025-06-18)


### 🆕 Features

- Release the next version of the biomass burning forcing (source ID: DRES-CMIP-BB4CMIP7-2-1).
  This version fixes a bug in NMVOC bulk for 2023 only.
  No other time slices are affected,
  hence any CMIP7 historical runs which use DRES-CMIP-BB4CMIP7-2-0 are fine and can be used 
  (because the data for DRES-CMIP-BB4CMIP7-2-0 and DRES-CMIP-BB4CMIP7-2-1 
  are identical for the period of the CMIP7 historical simulations i.e. for all of 1850-2021 inclusive). ([#248](https://github.com/PCMDI/input4MIPs_CVs/pull/248))


## input4MIPs CVs v6.6.32 (2025-06-17)


### 🆕 Features

- Updated to the next version of the volcanic forcing (source ID: UOEXETER-CMIP-2-2-1). ([#244](https://github.com/PCMDI/input4MIPs_CVs/pull/244))


## input4MIPs CVs v6.6.31 (2025-06-17)


### ⚠️ Breaking Changes

- Updated to the latest scrape of the ESGF.
  Users: note that we are having issues with the scrape.
  The links to ESGF in the pages remain correct.
  However our database views will be out of date until this is fixed
  so please do not rely on them for checking data availability, go to ESGF directly. ([#254](https://github.com/PCMDI/input4MIPs_CVs/pull/254))


## input4MIPs CVs v6.6.30 (2025-06-17)


### 🔧 Trivial/Internal Changes

- [#253](https://github.com/PCMDI/input4MIPs_CVs/pull/253)


## input4MIPs CVs v6.6.29 (2025-05-23)


### 🆕 Features

- Added new version of the simple plumes based on the latest release of the CEDS data ([#241](https://github.com/PCMDI/input4MIPs_CVs/pull/241))


## input4MIPs CVs v6.6.28 (2025-05-23)


### 📚 Improved Documentation

- Updated the latest CEDS source ID in the delivery summary page ([#245](https://github.com/PCMDI/input4MIPs_CVs/pull/245))


## input4MIPs CVs v6.6.27 (2025-05-05)


### 🆕 Features

- Added new version of anthropogenic emissions (CEDS) data. The previous version contained a bug in gridding of 2022 and 2023 data, so any piControl and historical simulations which have been started do not need to be restarted, but if you haven't started yet, please use this new version. ([#239](https://github.com/PCMDI/input4MIPs_CVs/pull/239))


## input4MIPs CVs v6.6.26 (2025-04-16)


### 🆕 Features

- Added the smoothed biomass burning dataset ([#237](https://github.com/PCMDI/input4MIPs_CVs/pull/237))


## input4MIPs CVs v6.6.25 (2025-04-03)


### 📚 Improved Documentation

- Updated the volcanic forcing documentation ([#234](https://github.com/PCMDI/input4MIPs_CVs/pull/234))


## input4MIPs CVs v6.6.24 (2025-04-03)


### 📚 Improved Documentation

- Updated the solar forcings documentation ([#232](https://github.com/PCMDI/input4MIPs_CVs/pull/232))


## input4MIPs CVs v6.6.23 (2025-04-02)


### 📚 Improved Documentation

- Updated the GHG concentration documentation ([#236](https://github.com/PCMDI/input4MIPs_CVs/pull/236))


## input4MIPs CVs v6.6.22 (2025-04-02)


### 🔧 Trivial/Internal Changes

- [#233](https://github.com/PCMDI/input4MIPs_CVs/pull/233)


## input4MIPs CVs v6.6.21 (2025-03-28)


### 🐛 Bug Fixes

- Updated the database after republication of CEDS data ([#230](https://github.com/PCMDI/input4MIPs_CVs/pull/230))


## input4MIPs CVs v6.6.20 (2025-03-27)


### 📚 Improved Documentation

- Cleaned up the README ([#206](https://github.com/PCMDI/input4MIPs_CVs/pull/206))


## input4MIPs CVs v6.6.19 (2025-03-27)


### 🆕 Features

- Added CEDS-CMIP-2025-03-18 and CEDS-CMIP-2025-03-18-supplemental source ID and data ([#228](https://github.com/PCMDI/input4MIPs_CVs/pull/228))


## input4MIPs CVs v6.6.18 (2025-03-26)


### 🆕 Features

- Added UofMD-landState-3-1-1 source ID and associated data ([#229](https://github.com/PCMDI/input4MIPs_CVs/pull/229))


## input4MIPs CVs v6.6.17 (2025-03-24)


### 🆕 Features

- Added UofMD-landState-3-1 source ID and associated land-use data. ([#213](https://github.com/PCMDI/input4MIPs_CVs/pull/213))

### 🐛 Bug Fixes

- Fixed the licence ID of the DRES-CMIP-BB4CMIP7-2-0 entries in the database (too late for the files). ([#213](https://github.com/PCMDI/input4MIPs_CVs/pull/213))


## input4MIPs CVs v6.6.16 (2025-03-20)


### 📚 Improved Documentation

- Added landing pages for all source IDs (except source IDs that were never published) in `docs/source-id-landing-pages`.
  These can then be linked up with ESGF's metadata using the citation info that is placed next to these landing pages. ([#225](https://github.com/PCMDI/input4MIPs_CVs/pull/225))


## input4MIPs CVs v6.6.15 (2025-03-18)


### 📚 Improved Documentation

- Removed any mention of the AR7 fast track. It has now been clarified ([#222](https://github.com/PCMDI/input4MIPs_CVs/issues/222)) that there is only one set of DECK simulations, hence we only need to mention CMIP7 in our docs, not CMIP7 and a separate AR7 fast track. ([#223](https://github.com/PCMDI/input4MIPs_CVs/pull/223))


## input4MIPs CVs v6.6.14 (2025-03-18)


### 📚 Improved Documentation

- Update links to point to input4mips-cvs.readthedocs.io rather than the now deactivated input4mips-controlled-vocabularies-cvs.readthedocs.io. Note that turning off input4mips-controlled-vocabularies-cvs.readthedocs.io did break the further_info_url value in the volcanic files. Please use the new domain instead. ([#226](https://github.com/PCMDI/input4MIPs_CVs/pull/226))


## input4MIPs CVs v6.6.13 (2025-03-13)


### 📚 Improved Documentation

- Updated documentation for how to use the volcanic forcing. ([#217](https://github.com/PCMDI/input4MIPs_CVs/pull/217))

### 🔧 Trivial/Internal Changes

- [#217](https://github.com/PCMDI/input4MIPs_CVs/pull/217)


## input4MIPs CVs v6.6.12 (2025-03-13)


### 🆕 Features

- Added UCLA-1-0-2 source ID and associated data. ([#194](https://github.com/PCMDI/input4MIPs_CVs/pull/194))
- Added DRES-CMIP-BB4CMIP7-2-0 and CR-CMIP-1-0-0 source IDs and associated data. ([#197](https://github.com/PCMDI/input4MIPs_CVs/pull/197))
- Added the UOEXETER-CMIP-2-0-0 source ID and associated data. ([#204](https://github.com/PCMDI/input4MIPs_CVs/pull/204))

### 🐛 Bug Fixes

- Fix DOI associated with Uni. Exeter publications ([#205](https://github.com/PCMDI/input4MIPs_CVs/pull/205))

### 📚 Improved Documentation

- Updated the documentation for biomass burning emissions and greenhouse gas concentrations based on the CMIP7 data releases. ([#197](https://github.com/PCMDI/input4MIPs_CVs/pull/197))
- Add DOI information to the database views. ([#205](https://github.com/PCMDI/input4MIPs_CVs/pull/205))


## input4MIPs CVs v6.6.11 (2025-02-26)


### 🆕 Features

- Added the "authors" field to each source ID. This field provides a machine-readable set of information about the author of the dataset identified by each source ID. ([#195](https://github.com/PCMDI/input4MIPs_CVs/pull/195))

### 🎉 Improvements

- Added an "authors" field to the source ID entries to allow DOI entries to be auto-generated (underlying discussion: https://github.com/PCMDI/input4MIPs_CVs/issues/177). ([#195](https://github.com/PCMDI/input4MIPs_CVs/pull/195))
- Update the source ID CVs so they contain all information required for creating DOIs. ([#200](https://github.com/PCMDI/input4MIPs_CVs/pull/200))

### 🐛 Bug Fixes

- Fixed up incorrect MIP era entry for SOLARIS-HEPPA-CMIP-4-6 in the `CVs/input4MIPs_source_id.json` ([#198](https://github.com/PCMDI/input4MIPs_CVs/pull/198))

### 📚 Improved Documentation

- Fixed minor bugs in the docs (incorrect cross-reference in the CHANGELOG and incorrect information about what version of simple plumes to use for testing). ([#193](https://github.com/PCMDI/input4MIPs_CVs/pull/193))
- - Added database views for the CMIP7 mip era (previous views were CMIP6Plus only).
  - Fixed up the source ID for SOLARIS-HEPPA in the CVs and the delivery summary view.

  ([#199](https://github.com/PCMDI/input4MIPs_CVs/pull/199))


## input4MIPs CVs v6.6.10 (2025-02-24)


### 🆕 Features

- Added SOLARIS-HEPPA 4.6, the first CMIP7 AR7 fast-track dataset. ([#183](https://github.com/PCMDI/input4MIPs_CVs/pull/183))

### 📚 Improved Documentation

- - Put the datasets to use for AR7 CMIP7 fast track first in docs. For datasets which don't have AR7 CMIP7 datasets yet, the testing datasets are still in the docs, they're just further down now (because these docs are less relevant).
  - Directed users to use [the new issue template](https://github.com/PCMDI/input4MIPs_CVs/issues/new?template=data_issue.md) for creating issues that report issues with datasets to help streamline things and capture key information.

  ([#183](https://github.com/PCMDI/input4MIPs_CVs/pull/183))

### 🔧 Trivial/Internal Changes

- [#190](https://github.com/PCMDI/input4MIPs_CVs/pull/190)


## input4MIPs CVs v6.6.9 (2025-02-14)


### 🆕 Features

- Added UCLA-1-0-1 and associated data, source IDs and institution ID to the CVs. ([#164](https://github.com/PCMDI/input4MIPs_CVs/pull/164))


## input4MIPs CVs v6.6.8 (2025-02-14)


### 🗑️ Deprecations

- Deprecated UOEXETER-CMIP-1-3-0 data. ([#180](https://github.com/PCMDI/input4MIPs_CVs/pull/180))

### 🆕 Features

- Added UOEXETER-CMIP-1-3-1 data. ([#180](https://github.com/PCMDI/input4MIPs_CVs/pull/180))

### 🔧 Trivial/Internal Changes

- [#180](https://github.com/PCMDI/input4MIPs_CVs/pull/180), [#185](https://github.com/PCMDI/input4MIPs_CVs/pull/185)


## input4MIPs CVs v6.6.7 (2025-02-07)


### 📚 Improved Documentation

- Updated expected delivery dates for ozone and nitrogen deposition forcing. ([#179](https://github.com/PCMDI/input4MIPs_CVs/pull/179))

### 🔧 Trivial/Internal Changes

- [#179](https://github.com/PCMDI/input4MIPs_CVs/pull/179)


## input4MIPs CVs v6.6.6 (2025-02-03)


### 🆕 Features

- Added UOEXETER-CMIP-1-3-0, i.e. the next release of the volcanic forcing. ([#178](https://github.com/PCMDI/input4MIPs_CVs/pull/178))

### 🔧 Trivial/Internal Changes

- [#178](https://github.com/PCMDI/input4MIPs_CVs/pull/178)


## input4MIPs CVs v6.6.5 (2025-01-09)


### 🆕 Features

- Added source ID UOEXETER-CMIP-1-2-0 to the CVs and associated data to the database. ([#174](https://github.com/PCMDI/input4MIPs_CVs/pull/174))

### 🐛 Bug Fixes

- Added uoexeter to the institution IDs CVs. ([#174](https://github.com/PCMDI/input4MIPs_CVs/pull/174))

### 📚 Improved Documentation

- - Added the link to the [external volcanic forcing documentation](https://docs.google.com/document/d/1blX5kv0We1BteqWzMKs0OuhazAcAonay/edit?usp=sharing&ouid=104358532925985160745&rtpof=true&sd=true)
  - Fixed the ESGF link in the greenhouse gas concentrations overview

  ([#174](https://github.com/PCMDI/input4MIPs_CVs/pull/174))


## input4MIPs CVs v6.6.4 (2025-01-07)


### 📚 Improved Documentation

- Updated anthropogenic emissions, i.e. CEDS, documentation. ([#169](https://github.com/PCMDI/input4MIPs_CVs/pull/169))


## input4MIPs CVs v6.6.3 (2024-12-20)


### 📚 Improved Documentation

- Updated simple plume info in the delivery summary. ([#170](https://github.com/PCMDI/input4MIPs_CVs/pull/170))


## input4MIPs CVs v6.6.2 (2024-12-19)


### 🆕 Features

- Added guidance for aerosol optical properties, i.e. MAC simple plumes users. ([#165](https://github.com/PCMDI/input4MIPs_CVs/pull/165))

### 📚 Improved Documentation

- Added basic examples of how to download data from ESGF. ([#166](https://github.com/PCMDI/input4MIPs_CVs/pull/166))
- Fixed up delivery summary for anthropogenic emissions (CEDS). ([#167](https://github.com/PCMDI/input4MIPs_CVs/pull/167))


## input4MIPs CVs v6.6.1 (2024-12-18)


### 🗑️ Deprecations

- Captured retractions of parts of the CEDS-CMIP-2024-10-21 data. ([#159](https://github.com/PCMDI/input4MIPs_CVs/pull/159))
- - Retracted CR-CMIP-0-3-0.
  - Retracted bulk NMVOC from CEDS-CMIP-2024-11-25.

  ([#162](https://github.com/PCMDI/input4MIPs_CVs/pull/162))

### 🆕 Features

- Added the SOLARIS-HEPPA-CMIP-4-5 dataset. ([#159](https://github.com/PCMDI/input4MIPs_CVs/pull/159))
- Added CEDS-CMIP-2024-11-25 and CEDS-CMIP-2024-11-25-supplemental data. ([#161](https://github.com/PCMDI/input4MIPs_CVs/pull/161))
- Added the CR-CMIP-0-4-0 dataset. ([#162](https://github.com/PCMDI/input4MIPs_CVs/pull/162))

### 📚 Improved Documentation

- Added information about which source ID to use for which phase of CMIP7 in the [dataset overviews](dataset-overviews) section. ([#151](https://github.com/PCMDI/input4MIPs_CVs/pull/151))
- Simplified the description of the testing phase in the dataset overview pages and renamed 'AR7 fast track' to 'CMIP7 AR7 fast track' to avoid confusion. ([#157](https://github.com/PCMDI/input4MIPs_CVs/pull/157))
- - Fixed up the broken "Database views homepage" link in the database views pages
  - Updated the delivery summary view to include a link to our internal documentation pages
  - Updated the greenhouse gas concentration data overview to include the mapping between CMIP6, CMIP7 and 'normal' names

  ([#160](https://github.com/PCMDI/input4MIPs_CVs/pull/160))

### 🔧 Trivial/Internal Changes

- [#160](https://github.com/PCMDI/input4MIPs_CVs/pull/160)


## input4MIPs CVs v6.6.0 (2024-11-12)


### 🆕 Features

- - Added preliminary CEDS data to the database. See the docs (specifically dataset overviews) for details.
  - Added preliminary CEDS data source IDs: "CEDS-CMIP-2024-10-21" and "CEDS-CMIP-2024-10-21-supplemental".

  ([#156](https://github.com/PCMDI/input4MIPs_CVs/pull/156))

### 🎉 Improvements

- Re-validated database with the new version of input4mips-validation.
  The validation status should be more sensible now. ([#155](https://github.com/PCMDI/input4MIPs_CVs/pull/155))

### 📚 Improved Documentation

- Updated expected anthropogenic emissions delivery date. ([#148](https://github.com/PCMDI/input4MIPs_CVs/pull/148))
- - Improved the [usage documentation for users][usage-as-a-data-user]
  - Added an [overview of the GHG concentrations][greenhouse-gas-concentrations]
  - Added an [overview of the solar data][solar]
  - Added placeholder docs for all other data providers in [the dataset overviews][dataset-overviews]
  - Fixed up sub-scripts in docs and related HTML files
  - Fixed a typo in the post-publication comment for "SOLARIS-HEPPA-CMIP-4-3"

  ([#150](https://github.com/PCMDI/input4MIPs_CVs/pull/150))
- Added google analytics to the docs. ([#153](https://github.com/PCMDI/input4MIPs_CVs/pull/153))
- - Marked placeholder CEDS source IDs "CEDS-CMIP-2024-07-08" and "CEDS-CMIP-2024-07-08-supplemental" as never published.
  - Updated the usage instructions in `scripts/pmount-database-generation/db-add-tree.sh`
  - Updated the HTML generation to handle data sets that have multiple source IDs.

  ([#156](https://github.com/PCMDI/input4MIPs_CVs/pull/156))

### 🔧 Trivial/Internal Changes

- [#145](https://github.com/PCMDI/input4MIPs_CVs/pull/145)


## input4MIPs CVs v6.5.23 (2024-10-22)


### 🆕 Features

- Added SOLARIS-HEPPA-CMIP-4-4 dataset ([#137](https://github.com/PCMDI/input4MIPs_CVs/pull/137))

### 📚 Improved Documentation

- - Updated SOLARIS-HEPPA-CMIP-4-3 status (this dataset has been retracted)
  - Fixed missing license_id for UofMD-landState-3-0
  - Fixed missing license_id for DRES-CMIP-BB4CMIP1-1-0

  ([#137](https://github.com/PCMDI/input4MIPs_CVs/pull/137))


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
