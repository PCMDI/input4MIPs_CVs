import json
import os


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


def create_variable_json_files(variable_ids, output_dir):
    """Create individual JSON files for each variable_id."""
    os.makedirs(output_dir, exist_ok=True)

    for var_id in variable_ids:
        json_content = {
            "@context": "000_context.jsonld",
            "id": var_id.lower(),
            "type": "variable",
        }

        filename = f"{var_id.lower()}.json"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, "w") as f:
            json.dump(json_content, f, indent=4)

        print(f"Created: {filepath}")


if __name__ == "__main__":
    json_file = "CVs/jsonDB/input4MIPs_db_file_entries.json"
    output_directory = "input4MIPs_variable_id"

    unique_ids = extract_unique_variable_ids(json_file)

    print(f"Found {len(unique_ids)} unique variable_id values:")
    for var_id in unique_ids:
        print(var_id)

    print(f"\nCreating JSON files in {output_directory}/ directory...")
    create_variable_json_files(unique_ids, output_directory)
