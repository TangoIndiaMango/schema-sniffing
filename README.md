# JSON Schema Generator

This program reads a JSON file, analyzes the schema of the "message" part, and generates a JSON schema file.

## Usage

1. Make sure you have Python installed.

2. Create your input JSON file in the `data` directory.

3. Run the program with the following command:

```bash
   python main.py
```

- Replace your_input.json with your input file name and your_output.json with your desired output file name.

1. Find your generated JSON schema in the schema directory.
### Expected Data Types
- `string`: Detected as a Python string.
- `integer`: Detected as a Python integer.
- `enum`: Detected when values in an array are strings.
- `array`: Detected when values in an array are either dictionaries or strings.
- `boolean`: Detected as a Python boolean.

### Example
- For an example input JSON file data/your_input.json, you'll find the generated schema in schema/your_output.json.

## Dependencies
- This program requires Python 3.10.11

## Note
if  you would  like to run with other files. Youcan  supply your  input and output file as args

```bash
   python main.py data/your_input.json schema/your_output.json
```