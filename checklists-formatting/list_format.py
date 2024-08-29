import os
import csv
import json

def map_label(label_str):
    """Map string labels to numeric labels."""
    
    return {'entailment': 0, 'neutral': 1, 'contradiction': 2}.get(label_str, -1)

def process_tsv_file(file_path, output_folder):
    """Process a single TSV file and save the transformed data as JSON."""
    
    transformed_data = []
    with open(file_path, 'r') as file:
        tsv_reader = csv.reader(file, delimiter='\t')
        for row in tsv_reader:
            if len(row) == 3:
                label, premise, hypothesis = row
                numeric_label = map_label(label)
                if numeric_label != -1:
                    transformed_data.append({
                        'premise': premise,
                        'hypothesis': hypothesis,
                        'label': numeric_label
                    })

    output_file_path = os.path.join(output_folder, os.path.splitext(os.path.basename(file_path))[0] + '.json')
    with open(output_file_path, 'w') as json_file:
        json.dump(transformed_data, json_file, indent=4)

def process_all_tsv_files(input_folder, output_folder):
    """Process all TSV files in the specified folder and save JSONs in a different folder."""
    
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        if file_name.endswith('.tsv'):
            file_path = os.path.join(input_folder, file_name)
            process_tsv_file(file_path, output_folder)

input_folder_path = '/Users/shawyan/Downloads/data'
output_folder_path = '/Users/shawyan/Downloads/new_data'

process_all_tsv_files(input_folder_path, output_folder_path)
