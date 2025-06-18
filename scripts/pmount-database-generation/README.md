# input4MIPs database

This folder holds the scripts for our database management.
Given that the database already exists, we should only need:

- `db-add-tree.sh`: Add new files into our database
- `db-validate.sh`: Validate any files which have not yet been validated

It also contains some scripts for validating data, before it is added to the database:

- `validate-file.sh`: Validate a file using input4MIPs-validation
- `validate-tree.sh`: Validate a tree of files using input4MIPs-validation. 
                      This will write out an HTML summary of the validation.


## Adding new files

When new files are published to ESGF,
we also need to add them here.
The way this is currently set up assumes
that we have access to the actual files.
Then, we can run the `db-add-tree.sh` script to add files to our database.

### Nimbus

On nimbus, the command you need is something like

```sh
bash scripts/pmount-database-generation/db-add-tree.sh /p/user_pub/work/input4MIPs/CMIP7/CMIP/<institution-id>/<source-id>
```

### NERSC

On nersc, the command you need is something like

```sh
bash scripts/pmount-database-generation/db-add-tree.sh /global/cfs/projectdirs/<project-number>/gsharing/user_pub_work/input4MIPs/CMIP7/CMIP/<institution-id>/<source-id>
```
