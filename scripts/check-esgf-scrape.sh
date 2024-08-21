#!/bin/bash
# Check our scrape of ESGF
#
# If the scrape has changed,
# automatically generate a new PR.

# To run this script, you need an environment with GitHub's CLI installed
# On nimbus, you can get into that with:
# - `mamba init && source /home/jovyan/.bashrc && mamba activate /shared/mamba-gh/`
#
# You will also have needed to either have logged in using GitHub's CLI
# or set the `GH_TOKEN` variable using a GitHub API authentication token.

AUTO_GENERATED_PATH="/p/user_pub/work/input4MIPs/esgf-input4MIPs.json"
REPO_PATH="Database/input-data/esgf-input4MIPs.json"

cp $AUTO_GENERATED_PATH $REPO_PATH

git add $REPO_PATH
git diff-index --cached --quiet HEAD

if [ $? -eq 0 ]; then
    echo "No changes after grabbing the latest scrape"
    exit 0
fi


TIMESTAMP=$(date +%Y-%m-%d_%H-%M-%S)
BRANCH_NAME="${TIMESTAMP}_esgf-input4mips-json-update"
git checkout -b "${BRANCH_NAME}"
git commit -m "Update ESGF input4MIPs JSON file"
git push --set-upstream origin "${BRANCH_NAME}"
gh pr create --title "Bot: ${TIMESTAMP} update ESGF JSON" --body "Created from nimbus bot" --label "esgf-json-update" --reviewer znichollscr #--reviewer durack1