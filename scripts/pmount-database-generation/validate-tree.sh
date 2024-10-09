#!/bin/bash
# Validate a tree of files
#
# To run this script, you need an environment with input4mips-validation==0.11.3 installed
# On nimbus, you can get into that with:
# - `mamba init && source /home/jovyan/.bashrc && mamba activate /shared/input4mips-validation-v0.11.3/`
#
# Usage:
# bash validate-tree.sh <dir-containing-files-to-validate> <glob-to-apply>
# <glob-to-apply> is optional, if not supplied, we use "*.nc"

dir_to_check=$1
rglob_input=${2:-'*.nc'}

timestamp=$(date +%s)

# Alter as you wish
# LOG_LEVEL="DEBUG"
LOG_LEVEL="INFO_FILE_ERROR"

input4mips-validation --logging-level $LOG_LEVEL \
	validate-tree \
	--cv-source "gh:main" \
	"${dir_to_check}" \
	--rglob-input "${rglob_input}" \
	--output-html "${timestamp}_validate-tree-output.html"

echo "Wrote HTML summary to ${timestamp}_validate-tree-output.html"
