# CSV Formatter

## Description
The CSV Formatter is a versatile tool designed to format CSV files from various sources into a standardized format. It supports operations such as renaming columns, moving columns, and duplicating columns based on a provided mapping.

## Use Cases
The CSV Formatter can be used for a variety of tasks, including:
- Standardizing CSV files from different sources.
- Preparing CSV files for import into a database.
- Cleaning up CSV files for analysis.
- Automating repetitive tasks on CSV files.
- Telecom billing CDR (Call Detail Record) data processing.

## Requirements
In order to run the CSV Formatter, you need to have the following installed:
- Git
- Python 3.12.3 or higher

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/csv-formatter.git
    cd csv-formatter
    ```

## Usage
To format a CSV file, you need to provide an input file, a mapping name, and an output file. The mapping defines the actions to be performed on the columns of the input file. The mapping name should correspond to a mapping defined in the `mappings.json` file.

### Command
```sh
python format.py <input_file> <mapping_name> <output_file>
```

### Parameters
- <input_file>: Path to the input CSV file.
- <mapping_name>: Name of the mapping to be used for formatting.
- <output_file>: Path to the output CSV file.

### Example
Suppose you have an input file `input/data.csv` and you want to format it using the `example_mapping` mapping to produce `output/formatted_data.csv`. You would run:

```sh
python format.py input/data.csv example_mapping output/formatted_data.csv
```

## Mapping Example
A mapping defines the actions to be performed on the columns. Here is an example of a mapping, which can be found in the `mappings.json` file:
```json
{
    "name": "example_mapping",
    "actions": [
        {
            "name": "example_mapping",
            "actions": [
                {
                    "type": "move",
                    "originalColumnHeader": "ANI",
                    "destinationColumnNumber": 0,
                    "renameHeaderTo": "Origin Number"
                },
                {
                    "type": "insert",
                    "renameHeaderTo": "Billed Date",
                    "destinationColumnNumber": 1,
                    "value": ""
                },
                {
                    "type": "duplicate",
                    "originalColumnHeader": "Origin Number",
                    "destinationColumnNumber": 2,
                    "renameHeaderTo": "Number Billed"
                },
                {
                    "type": "delete_after",
                    "originalColumnNumber": 3
                }
            ]
        }
    ]
}
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure your code follows the existing style and includes appropriate tests.

For any issues or feature requests, please open an issue on GitHub.

## License
Distributed under the MIT License. See `LICENSE.md` for more information.
