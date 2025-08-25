import json


def extract_unique_variable_ids(json_file_path):
    """Extract unique variable_id values from JSON database."""
    with open(json_file_path, "r") as f:
        data = json.load(f)

    variable_ids = set()
    for entry in data:
        if "variable_id" in entry:
            if entry["variable_id"] is not None:
                variable_ids.add(entry["variable_id"])

    return sorted(list(variable_ids))


if __name__ == "__main__":
    json_file = "input4MIPs_db_file_entries.json"
    unique_ids = extract_unique_variable_ids(json_file)

    print(f"Found {len(unique_ids)} unique variable_id values:")
    for var_id in unique_ids:
        print(var_id)

