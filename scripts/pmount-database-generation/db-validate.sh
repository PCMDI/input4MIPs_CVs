#!/bin/bash
# Validate a database
#
# To run this script, you need an environment with input4mips-validation==0.19.0 installed
# On nimbus, you can get into that with:
# - `mamba init && source /home/jovyan/.bashrc && mamba activate /shared/input4mips-validation-v0.19.0/`
#
# Usage:
# Needs to be run from the root of the repository for hte paths to work
#   bash scripts/pmount-database-generation/db-validate.sh

DATABASE_DIR=Database/input-data/pmount
# Use local CVs for validation
CV_SOURCE="CVs/"

# Use DEBUG for full info. I would use INFO to start,
# then go up to INFO_INDIVIDUAL_CHECK before going to debug
LOG_LEVEL="INFO"
LOG_LEVEL="INFO_INDIVIDUAL_CHECK"
# LOG_LEVEL="DEBUG"

input4mips-validation --logging-level $LOG_LEVEL \
    db validate \
    --db-dir ${DATABASE_DIR} \
    --cv-source ${CV_SOURCE} \
    --allow-cf-checker-warnings \
    --n-processes 6
