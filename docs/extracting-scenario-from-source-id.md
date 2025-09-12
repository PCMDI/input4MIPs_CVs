# Extracting the scenario from the source ID

As a result of the way the input4MIPs data is provided,
there is no other way to communicate scenario information easily
(for the discussion we had about changing the DRS to fix this
and why we ultimately didn't change,
see [input4MIPs_CVs #64](https://github.com/PCMDI/input4MIPs_CVs/discussions/64)).

Accordingly, here we provide guidance about how to extract the scenario
to which a source ID's data applies from the source ID value itself.
This is not trivial.
At the moment, this is in quite a state of flux.
For the latest information, please see the
`extract_scenario_from_source_id` function
in [docs/dataset-overviews/fill-out-auto-generated-sections.py](https://github.com/PCMDI/input4MIPs_CVs/blob/main/docs/dataset-overviews/fill-out-auto-generated-sections.py).

We have include a copy of this function as at 2025-09-12 below
so you can see the logic,
but this extract is not automatically updated so it could be out of date
by the time you are reading this.


```python
def extract_scenario_from_source_id(source_id: str) -> str | None:
    """
    Extract the scenario from a given source ID

    This is provided as there is no other way to communicate scenario information.
    For the discussion we had about changing the DRS to fix this
    and why we ultimately didn't change,
    see [input4MIPs_CVs #64](https://github.com/PCMDI/input4MIPs_CVs/discussions/64)

    Parameters
    ----------
    source_id
        Source ID from which to get the scenario

    Returns
    -------
    :
        The scenario extracted from `source_id`.
        `None` is returned if the source ID is not for scenarios
        i.e. `source_id` is for data related to historical or piControl

    Raises
    ------
    ValueError
        The source ID is not known to apply to historical or piControl
        and cannot be parsed to extract the scenario.
    """
    KNOWN_HISTORICAL_SOURCE_IDS = {
        "CEDS-CMIP-2024-07-08",
        "CEDS-CMIP-2024-07-08-supplemental",
        "CEDS-CMIP-2024-10-21",
        "CEDS-CMIP-2024-10-21-supplemental",
        "CEDS-CMIP-2024-11-25",
        "CEDS-CMIP-2024-11-25-supplemental",
        "CEDS-CMIP-2025-03-18",
        "CEDS-CMIP-2025-03-18-supplemental",
        "CEDS-CMIP-2025-04-18",
        "CEDS-CMIP-2025-04-18-supplemental",
        "CR-CMIP-0-2-0",
        "CR-CMIP-0-3-0",
        "CR-CMIP-0-4-0",
        "CR-CMIP-1-0-0",
        "DRES-CMIP-BB4CMIP7-1-0",
        "DRES-CMIP-BB4CMIP7-2-0",
        "DRES-CMIP-BB4CMIP7-2-1",
        "FZJ-CMIP-nitrogen-1-0",
        "FZJ-CMIP-ozone-1-0",
        "ImperialCollege-3-0",
        "MRI-JRA55-do-1-6-0",
        "PCMDI-AMIP-1-1-10",
        "PCMDI-AMIP-1-1-9",
        "PCMDI-AMIP-ERSST5-1-0",
        "PCMDI-AMIP-Had1p1-1-0",
        "PCMDI-AMIP-OI2p1-1-0",
        "PIK-CMIP-1-0-0",
        "SOLARIS-HEPPA-CMIP-4-1",
        "SOLARIS-HEPPA-CMIP-4-2",
        "SOLARIS-HEPPA-CMIP-4-3",
        "SOLARIS-HEPPA-CMIP-4-4",
        "SOLARIS-HEPPA-CMIP-4-5",
        "SOLARIS-HEPPA-CMIP-4-6",
        "UCLA-1-0-1",
        "UCLA-1-0-1-constant",
        "UCLA-1-0-1-decreasing",
        "UCLA-1-0-1-increasing",
        "UCLA-1-0-2",
        "UCLA-1-0-2-constant",
        "UCLA-1-0-2-decreasing",
        "UCLA-1-0-2-increasing",
        "UOEXETER-CMIP-0-1-0",
        "UOEXETER-CMIP-1-1-2",
        "UOEXETER-CMIP-1-1-3",
        "UOEXETER-CMIP-1-2-0",
        "UOEXETER-CMIP-1-3-0",
        "UOEXETER-CMIP-1-3-1",
        "UOEXETER-CMIP-2-0-0",
        "UOEXETER-CMIP-2-2-1",
        "UReading-CCMI-1-1",
        "UofMD-landState-3-0",
        "UofMD-landState-3-1",
        "UofMD-landState-3-1-1",
    }
    if source_id in KNOWN_HISTORICAL_SOURCE_IDS:
        return None

    KNOWN_SCENARIOS = {"vllo", "vlho", "l", "m", "ml", "h", "hl"}

    for known_prefix in ("PIK-",):
        if known_prefix in source_id:
            # Assume that scenario information is the first part of the hyphen-separated
            # source ID after the prefix.
            # e.g. we are assuming that for a prefix like "PIK-",
            # the source ID is of the form "PIK-scenarioname-other-stuff"
            # e.g. "PIK-vllo-0-1-0".
            scenario = source_id.split(known_prefix)[1].split("-")[0]
            if scenario in KNOWN_SCENARIOS:
                return scenario

    msg = f"Could not parse {source_id=} to find a known scenario"
    raise ValueError(msg)
```
