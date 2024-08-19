# Versioning

The easiest place to find the repository's version is currently `VERSION`.
The version string from this file should be consistent with the rest of the repository.
If you see a place where this is not applied consistently,
please [raise an issue](https://github.com/PCMDI/input4MIPs_CVs/issues/new)
to let us know.

The version number takes the form X.Y.Z, but does not completely follow semantic versioning.
The major number, X, is the CMIP generation we are targeting.
At the moment, this is 6, soon (hopefully Jan 2025) it will be 7.
The minor number, Y, is incremented for breaking changes to the CVs.
The patch number, Z, is incremented for all other changes.
All releases will have a unique version number and be tagged in the repository.
For all commits except tagged commits,
we append the version with "a1" to indicate 
that this state of the repository is not an official release,
instead, it is a work in progress pre-release.
Please treat these pre-release versions with more care,
because their version number does not correspond to a unique commit.
