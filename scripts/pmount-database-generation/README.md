# input4MIPs database

This folder holds the scripts for our database management.
Given that the database already exists, we should only need:

- `db-add-tree.sh`: Add new files into our database
- `db-validate.sh`: Validate any files which have not yet been validated

It also contains some scripts for validating data, before it is added to the database:

- `validate-file.sh`: Validate a file using input4MIPs-validation
- `validate-tree.sh`: Validate a tree of files using input4MIPs-validation. 
                      This will write out an HTML summary of the validation.
