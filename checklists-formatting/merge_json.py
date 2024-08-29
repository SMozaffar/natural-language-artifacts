import os
import json
from collections import defaultdict

def merge_json_files(input_folder, output_folder):
    """Merge JSON files with similar names into a single file in a separate output directory."""
    files_to_merge = defaultdict(list)

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Group files by their common prefix
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.json'):
            prefix = file_name.rsplit('-', 1)[0]  # Split on the last '-' and take the first part
            files_to_merge[prefix].append(file_name)

    # Merge and save files
    for prefix, file_list in files_to_merge.items():
        merged_data = []
        for file_name in file_list:
            with open(os.path.join(input_folder, file_name), 'r') as json_file:
                data = json.load(json_file)
                merged_data.extend(data)

        # Save merged data to a new JSON file in the output directory
        output_file_path = os.path.join(output_folder, prefix + '_merged.json')
        with open(output_file_path, 'w') as output_file:
            json.dump(merged_data, output_file, indent=4)

# Replace with the paths to your input and output folders
input_folder_path = '/Users/shawyan/Downloads/format_checklist'
output_folder_path = '/Users/shawyan/Downloads/merged_checklists'
merge_json_files(input_folder_path, output_folder_path)
