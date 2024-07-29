# Makefile to help automate key steps

.DEFAULT_GOAL := help

# A helper script to get short descriptions of each target in the Makefile
define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([\$$\(\)a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-30s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT


.PHONY: help
help:  ## print short description of each target
	@python3 -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

.PHONY: generate-web-pages
generate-web-pages:  ## generate our web pages
	venv/bin/python generate-html-pages.py --version "0.1.0"

.PHONY: update-database
update-database:  ## run our database update script
	venv/bin/python update-database.py

.PHONY: virtual-environment
virtual-environment:  ## update virtual environment, create a new one if it doesn't already exist
	python3 -m venv venv
	venv/bin/pip install --upgrade pip
	venv/bin/pip install 'pandas==2.2.2' 'pandas_diff==1.4.7' 'tqdm==4.66.4' 'typer==0.12.3'
