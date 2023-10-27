import json
import os
from helpers import *

def generate_schema(input_file, output_file):
    # Get the current working directory to avoid file not found issues
    cwd = os.getcwd()
    input_path = os.path.join(cwd, input_file)
    output_path = os.path.join(cwd, output_file)

    # Read the JSON file
    with open(input_path, 'r') as f:
        data = json.load(f)

    # Initialize an empty schema
    schema = {"type": "array", "tag": "", "description": "", "required": False}

    def process_data(data, schema):
        for key, value in data.items():
            if isinstance(value, str):
                schema[key] = detect_string(value)
            elif isinstance(value, int):
                schema[key] = detect_integer(value)
            elif isinstance(value, bool):
                schema[key] = detect_boolean(value)
            elif isinstance(value, list):
                if all(isinstance(item, str) for item in value):
                    schema[key] = detect_enum(value)
                elif all(isinstance(item, dict) for item in value):
                    item_type = {"type": "array"}
                    schema[key] = detect_array(value, item_type)
            elif isinstance(value, dict):
                schema[key] = {"type": "array", "tag": "", "description": "", "required": False}
                # Recursively process nested dictionaries
                process_data(value, schema[key])

    # Process the message part to generate the schema
    message = data.get('message', {})
    process_data(message, schema)

    # Write the schema to the output file
    with open(output_path, 'w') as f:
        json.dump(schema, f, indent=2)

# Example
# generate_schema("data/data_1.json", "schema/schema_1.json")
