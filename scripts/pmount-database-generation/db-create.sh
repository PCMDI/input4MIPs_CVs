#!/bin/bash
# Create the database

# To run this script, you need an environment with input4mips-validation==0.11.3 installed
# On nimbus, you can get into that with:
# - `mamba init && source /home/jovyan/.bashrc && mamba activate /shared/input4mips-validation-v0.11.3/`

DATABASE_DIR=Database/input-data/pmount
TREE_TO_CREATE_FROM=/p/user_pub/work/input4MIPs/CMIP6Plus/
CV_SOURCE="gh:main"

# Use DEBUG for full info. I would use INFO to start,
# then go up to INFO_INDIVIDUAL_CHECK before going to debug
LOG_LEVEL="INFO"
# LOG_LEVEL="INFO_INDIVIDUAL_CHECK"
# LOG_LEVEL="DEBUG"

input4mips-validation --logging-level $LOG_LEVEL \
    db create $TREE_TO_CREATE_FROM \
    --db-dir ${DATABASE_DIR} \
    --cv-source ${CV_SOURCE} \
    --n-processes 6
