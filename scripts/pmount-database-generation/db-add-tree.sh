#!/bin/bash
# Add missing files to the database.
#
# Any file in the tree that is not in the database
# will be added to the database.
#
# To run this script, you need an environment with input4mips-validation==0.19.0 installed
# On nimbus, you can get into that with:
# - `mamba init && source /home/jovyan/.bashrc && mamba activate /shared/input4mips-validation-v0.19.0/`
#
# Usage:
# This must be run from the root of the repository for the paths to work
#   bash scripts/pmount-database-generation/db-add-tree.sh <tree-to-add-from>

TREE_TO_ADD_FROM=$1
echo "Adding data from the tree with root: ${TREE_TO_ADD_FROM}"
# print the input4mips-validation version too, can't hurt
# and makes sure that input4mips-validation is available
input4mips-validation --version

DATABASE_DIR=Database/input-data/pmount
CV_SOURCE="gh:main"

# Use DEBUG for full info. I would use INFO to start,
# then go up to INFO_INDIVIDUAL_CHECK before going to debug
LOG_LEVEL="INFO"
# LOG_LEVEL="INFO_INDIVIDUAL_CHECK"
# LOG_LEVEL="DEBUG"

input4mips-validation --logging-level $LOG_LEVEL \
    db add-tree $TREE_TO_ADD_FROM \
    --db-dir ${DATABASE_DIR} \
    --cv-source ${CV_SOURCE} \
    --n-processes 6
