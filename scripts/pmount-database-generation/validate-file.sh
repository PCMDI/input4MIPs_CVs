#!/bin/bash
# Validate a file
#
# To run this script, you need an environment with input4mips-validation==0.19.0 installed
# On nimbus, you can get into that with:
# - `mamba init && source /home/jovyan/.bashrc && mamba activate /shared/input4mips-validation-v0.19.0/`
#
# Usage:
# bash validate-file.sh <path-to-file-to-validate>

file_to_check=$1

# Alter as you wish
LOG_LEVEL="DEBUG"
# LOG_LEVEL="INFO_FILE_ERROR"

input4mips-validation --logging-level $LOG_LEVEL \
	validate-file \
	--cv-source "gh:main" \
	"${file_to_check}"

