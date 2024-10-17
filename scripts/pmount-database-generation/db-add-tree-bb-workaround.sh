#!/bin/bash
# Workaround to deal with the biomass burning data that has underscores in the variable_id.

DATABASE_DIR=Database/input-data/pmount
CV_SOURCE="gh:main"

# Use DEBUG for full info. I would use INFO to start,
# then go up to INFO_INDIVIDUAL_CHECK before going to debug
LOG_LEVEL="INFO"
# LOG_LEVEL="INFO_INDIVIDUAL_CHECK"
# LOG_LEVEL="DEBUG"

TREE_TO_ADD_FROM=/p/user_pub/work/input4MIPs/CMIP6Plus/CMIP/DRES/DRES-CMIP-BB4CMIP7-1-0/atmos/mon/fx
input4mips-validation --logging-level $LOG_LEVEL \
	db add-tree $TREE_TO_ADD_FROM \
	--db-dir ${DATABASE_DIR} \
	--cv-source ${CV_SOURCE} \
	--n-processes 6

TREE_TO_ADD_FROM=/p/user_pub/work/input4MIPs/CMIP6Plus/CMIP/DRES/DRES-CMIP-BB4CMIP7-1-0/atmos/mon

for folder in "${TREE_TO_ADD_FROM}"/*; do
	echo "${folder}"
	variable_id="${folder##*/}"
	if [[ "${variable_id}" == *"_"* ]]; then
		echo "Underscore in folder name, skipping"

	else
		input4mips-validation --logging-level $LOG_LEVEL \
			db add-tree "${folder}" \
			--db-dir ${DATABASE_DIR} \
			--cv-source ${CV_SOURCE} \
			--n-processes 6

	fi

done
