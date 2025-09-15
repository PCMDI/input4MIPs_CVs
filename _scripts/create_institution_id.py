import json
import os
from pathlib import Path
import requests
import esgvoc.api as ev
# URLs of the JSON files on GitHub
json_url = 'https://raw.githubusercontent.com/PCMDI/input4MIPs_CVs/refs/heads/main/CVs/input4MIPs_institution_id.json'

# Directory where the JSON files will be saved
save_dir = 'input4MIPs_institution_id'

# Create the directory if it doesn't exist
os.makedirs(save_dir, exist_ok=True)

# Function to fetch and load JSON data from a URL
def fetch_json(url):
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors
    return response.json()

data = fetch_json(json_url)

known_institutions_in_universe = ev.get_all_terms_in_data_descriptor("institution")

for item in data:
    found_inst = None
    for inst in known_institutions_in_universe:
        if inst.drs_name == item:
            found_inst = inst
            break
    if found_inst is None:
        for consor in ev.get_all_terms_in_data_descriptor("consortium"):
            if consor.drs_name == item.upper():
                found_inst = consor
                break
    if found_inst is None:
        for orga in ev.get_all_terms_in_data_descriptor("organisation"):
            if orga.drs_name == item:
                found_inst = orga
                break


    if found_inst is None:
        print(item, "not found in universe")
    else : 
    # Create json file 
        dict_to_save = {
            "@context": "000_context.jsonld",
            "id": found_inst.id,
            "type": found_inst.type
        }
        # print(dict_to_save)
        with open(Path(save_dir) / f"{found_inst.id}.json","w") as f:
            json.dump(dict_to_save,f,indent=4)



    
