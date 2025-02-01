#!/bin/bash
# Re-write files in the DRS
#
# To run this script, you need an environment with input4mips-validation==0.19.0 installed
# On nimbus, you can get into that with:
# - `mamba init && source /home/jovyan/.bashrc && mamba activate /shared/input4mips-validation-v0.19.0/`
#
# Usage:
# bash rewrite-files-in-drs.sh <target-root-dir-for-rewrite> <files-to-rewrite>

rewrite_target=$1
shift

echo "Re-writing files into ${rewrite_target}"

# Alter as you wish
LOG_LEVEL="DEBUG"
# LOG_LEVEL="INFO_FILE_ERROR"

for file_to_rewrite in "$@"
do
    input4mips-validation --logging-level $LOG_LEVEL \
    	validate-file \
    	--cv-source ./CVs \
        --write-in-drs "${rewrite_target}" \
    	"${file_to_rewrite}"
    	# --cv-source "gh:main" \
        # --allow-cf-checker-warnings \
done
