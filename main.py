from schema_format import generate_schema 

def main(input_files, output_files):
    for input_file, output_file in zip(input_files, output_files):
        generate_schema(input_file, output_file)

if __name__ == "__main__":
    input_files = ["data/data_1.json", "data/data_2.json"]
    output_files = ["schema/schema_1.json", "schema/schema_2.json"] 
    main(input_files, output_files)
