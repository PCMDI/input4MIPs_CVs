"""
Validate the volcanic emissions

This is a special case because the time axis is not contiguous.

To run this script, you need an environment with input4mips-validation==0.19.0 installed
On nimbus, you can get into that with:
- `mamba init && source /home/jovyan/.bashrc && mamba activate /shared/input4mips-validation-v0.19.0/`
"""
from pathlib import Path

import iris

from input4mips_validation.cvs.loading import load_cvs
from input4mips_validation.cli import setup_logging, validate_file
from input4mips_validation.inference.from_data import (
    BoundsInfo,
    FrequencyMetadataKeys,
    infer_time_start_time_end_for_filename,
)
from input4mips_validation.xarray_helpers.iris import ds_from_iris_cubes
from input4mips_validation.xarray_helpers.variables import (
    XRVariableHelper,
)

setup_logging(
            enable=True, logging_level="DEBUG"
        )

xr_variable_processor = XRVariableHelper(
        bounds_coord_indicators=("bnds", "bounds")
    )
frequency_metadata_keys = FrequencyMetadataKeys(
        frequency_metadata_key="frequency",
        no_time_axis_frequency="fx",
    )
bounds_info = BoundsInfo(
        time_bounds="time_bnds",
        bounds_dim="bnds",
        )

file=Path("/shared/uoexeter-CMIP-1-3-0/utsvolcemis_input4MIPs_emissions_CMIP_UOEXETER-CMIP-1-3-0_gn_17500101-20231120.nc")
cv_source=Path("./CVs")
time_dimension="time"
write_in_drs=Path("./volc-rewritten")

cvs = load_cvs(cv_source=cv_source)

ds = ds_from_iris_cubes(
    iris.load(file),
    xr_variable_processor=xr_variable_processor,
    raw_file=file,
    time_dimension=time_dimension,
)

time_start, time_end = infer_time_start_time_end_for_filename(
    ds=ds,
    frequency_metadata_key=frequency_metadata_keys.frequency_metadata_key,
    no_time_axis_frequency=frequency_metadata_keys.no_time_axis_frequency,
    time_dimension=time_dimension,
)

full_file_path = cvs.DRS.get_file_path(
    root_data_dir=write_in_drs,
    available_attributes=ds.attrs,
    time_start=time_start,
    time_end=time_end,
)
print(f"{full_file_path=}")
print(f"{file=}")
print(f"{file==full_file_path=}")
print(f"{file.name==full_file_path.name=}")

# Fails because we can't handle the non-continuous time axis
validate_file(
        file=file,
        cv_source=cv_source,
        write_in_drs=None,
        xr_variable_processor=xr_variable_processor,
        frequency_metadata_keys=frequency_metadata_keys,
        bounds_info=bounds_info,
        time_dimension=time_dimension,
        allow_cf_checker_warnings=False,
        )
