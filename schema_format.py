import json
import os
from helpers import SchemaTypes


def generate_schema(input_file, output_file):
    # Get the current working directory to avoid file not found issues
    cwd = os.getcwd()
    input_path = os.path.join(cwd, input_file)
    output_path = os.path.join(cwd, output_file)

    # Read the JSON file
    with open(input_path, 'r') as f:
        data = json.load(f)

    schema = {"type": "array", "tag": "", "description": "", "required": False}

    schema_types = SchemaTypes(None)

    def process_data(data, schema):
        for key, value in data.items():
            schema_types.value = value
            if isinstance(value, str):
                schema[key] = schema_types.detect_string()
            elif isinstance(value, int):
                schema[key] = schema_types.detect_integer()
            elif isinstance(value, bool):
                schema[key] = schema_types.detect_boolean()
            elif isinstance(value, list):
                # when we have strings in a list
                if all(isinstance(item, str) for item in value):
                    schema[key] = schema_types.detect_enum()
                # when we have JSON objects in the list
                elif all(isinstance(item, dict) for item in value):
                    item_type = schema_types.detect_array({"type": "array"})
                    schema[key] = item_type
                # since JSON objects also takes an array
            elif isinstance(value, dict):
                schema[key] = {"type": "array", "tag": "",
                               "description": "", "required": False}
                process_data(value, schema[key])
                
        # return the value
        # return

    # Process the message part to generate the schema
    message = data.get('message', {})
    process_data(message, schema)

    # Write the schema to the output file
    with open(output_path, 'w') as f:
        json.dump(schema, f, indent=2)


# Example
generate_schema("data/data_1.json", "schema/schema_1.json")
