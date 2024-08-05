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

.PHONY: update-database
update-database:  ## run our database update script
	venv/bin/python python-packages/input4MIPs-CVs/src/input4MIPs_CVs/cli/update-database.py --repo-root-dir .


.PHONY: set-version
set-version:  ## set the repository's version to the value of the environment variable VERSION
	venv/bin/python python-packages/input4MIPs-CVs/src/input4MIPs_CVs/cli/version.py set --version $(VERSION) --repo-root-dir .

.PHONY: update-html-pages
update-html-pages:  ## update our html pages
	venv/bin/python python-packages/input4MIPs-CVs/src/input4MIPs_CVs/cli/update-html-pages.py --repo-root-dir .

.PHONY: virtual-environment
virtual-environment:  ## update virtual environment, create a new one if it doesn't already exist
	python3 -m venv venv
	venv/bin/pip install --upgrade pip
	venv/bin/pip install -e python-packages/input4MIPs-CVs
