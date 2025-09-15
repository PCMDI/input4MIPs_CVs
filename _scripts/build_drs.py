from pprint import pprint
import json


def create_project_specs():
    # input find https://github.com/PCMDI/input4MIPs_CVs/blob/main/CVs/input4MIPs_DRS.json: 
    input4MIPs_DRS = {
    "directory_path_example":"input4MIPs/CMIP6Plus/CMIP/PCMDI/PCMDI-AMIP-1-1-9/ocean/mon/tos/gn/v20230512/",
    "directory_path_template":"<activity_id>/<mip_era>/<target_mip>/<institution_id>/<source_id>/<realm>/<frequency>/<variable_id>/<grid_label>/v<version>",
    "filename_example":"tos_input4MIPs_SSTsAndSeaIce_CMIP_PCMDI-AMIP-1-1-9_gn_187001-202212.nc",
    "filename_template":"<variable_id>_<activity_id>_<dataset_category>_<target_mip>_<source_id>_<grid_label>[_<time_range>].nc"
}

    output = {
        "project_id": "input4mip",
        "description": "TODO?",
        "drs_specs": []
    }

    drs_directory = {
        "type" : "directory",
        "separator" :"/",
            "parts" : []

    }
    drs_filename ={
        "type" : "filename",
        "separator" : "_",
        "properties": {"extension": "nc", "extension_separator": "."},
        "parts" : []

                  
    }
    
    for collection in input4MIPs_DRS["directory_path_template"].split("/"):
        drs_directory["parts"].append({
            "collection_id": collection[1:-1] if not collection.startswith("v") else collection[2:-1],
            "is_required" : True,
            "kind": "collection"

        })

    for collection in input4MIPs_DRS["filename_template"].split(">_<"):
        col = collection if not collection.startswith("<") else collection[1:]
        
        
        if col == "grid_label>[_<time_range>].nc": 
            drs_filename["parts"].append({
            "collection_id": "grid_label",
            "id_required" : True,
            "kind": "collection"
            })
            drs_filename["parts"].append(
            {
            "collection_id": "time_range",
            "id_required" : False,
            "kind": "collection"
            }) # UGLY BUT WORKS (good enough gor this script)

        else:
            drs_filename["parts"].append({
            "collection_id": col,
            "id_required" : True,
            "kind": "collection"

            })

    output["drs_specs"].append(drs_directory)
    output["drs_specs"].append(drs_filename)
    
    with open("project_specs.json", "w") as file:
        json.dump(output, file, indent=4)  # indent=4 makes it pretty-printed
        
if __name__ == "__main__":
    create_project_specs()
