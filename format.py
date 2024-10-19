import os
import shutil
import sys
import json
from utils import *

MAPPING_FILE = "mappings.json"

def move(output_file, column_name, new_position, rename_to=None):
    move_csv_column(output_file, column_name, new_position)
    if rename_to is not None:
        rename_csv_column(output_file, column_name, rename_to)

def rename(output_file, old_column_name, new_column_name):
    rename_csv_column(output_file, old_column_name, new_column_name) 

def insert(output_file, column_name, value, index):
    insert_csv_column(output_file, column_name, value, index)

def duplicate(output_file, column_name, new_position, rename_to):
    duplicate_csv_column(output_file, column_name, rename_to)
    move_csv_column(output_file, rename_to, new_position)

def delete_after(output_file, column_number):
    remove_all_columns_starting_from_index(output_file, column_number)

def format_file(input_file, mapping_name, output_file):
    # check that file is a csv file
    if not input_file.endswith(".csv"):
        print(f"Error: File {input_file} is not a CSV. Exiting...")
        sys.exit(1)

    # check that the output path exsists if not, create it
    if not os.path.exists(os.path.dirname(output_file)):
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # check that the output file exists, if not, create it
    if not os.path.exists(output_file):
        with open(output_file, "w") as f:
            pass # create the file

    # copy the input file to the output file
    shutil.copy(input_file, output_file)

    print("Formatting file "  + \
          f"from {input_file} using mapping {mapping_name} to {output_file}")

    # clean up the CSV file
    clean_csv_file(input_file)

    # Read the mappings from the JSON file
    with open(MAPPING_FILE) as f:
        config = json.load(f)

    # get the mappings attribute (which is an array of mappings) from the config
    # and find the mapping with the provided name
    mapping = next(
        (m for m in config["mappings"] if m["name"] == mapping_name), None)

    # Check if the mapping exists
    if mapping is None:
        print(f"Error: Mapping {mapping_name} not found in {MAPPING_FILE}")
        sys.exit(1)

    # iterate over the actions
    for action in mapping["actions"]:
        # call the appropriate function based on the action type
        if action["type"] == "move":
            move(output_file, action["originalColumnHeader"],
                 action["destinationColumnNumber"],
                 action.get("renameHeaderTo", None))
        elif action["type"] == "rename":
            rename(output_file,
                   action["originalColumnHeader"], action["renameHeaderTo"])
        elif action["type"] == "insert":
            insert(output_file, action["renameHeaderTo"], action["value"],
                   action["destinationColumnNumber"])
        elif action["type"] == "duplicate":
            duplicate(output_file, action["originalColumnHeader"],
                      action["destinationColumnNumber"],
                      action["renameHeaderTo"])
        elif action["type"] == "delete_after":
            delete_after(output_file, action["originalColumnNumber"])
        else:
            print(f"Error: Unknown action type {action['type']}")
            sys.exit(1)

    

if __name__ == "__main__":
    # Check if all 3 parameters are provided
    if len(sys.argv) != 4:
        print("Error: Please provide the input file path, mapping name, and" + \
              "output file path as command line arguments.")
        print("Usage: " + \
              "python format.py <input_file> <mapping_name> <output_file>")
        sys.exit(1)

    # Get the command line arguments
    input_file = sys.argv[1]
    mapping_name = sys.argv[2]
    output_file = sys.argv[3]

    # Call the format_cdr function with the provided arguments
    format_file(input_file, mapping_name, output_file)
