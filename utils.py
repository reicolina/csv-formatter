import csv

def clean_csv_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    with open(file_path, 'w') as file:
        for line in lines:
            columns = line.split(',')
            first_column = columns[0]
            num_characters = len(first_column)
            if len(columns) >= 2 and num_characters > 0 and num_characters < 100:
                file.write(line)
            else:
                print(f"Info: Line in file {file_path} is not formatted correctly. Deleting this line...")

def delete_csv_column(file_path, header_name):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        header_index = headers.index(header_name)

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)

        for row in reader:
            del row[header_index]
            writer.writerow(row)

    print(f"Info: Column '{header_name}' deleted from file {file_path}")

def rename_csv_column(file_path, old_column_name, new_column_name):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        rows = list(reader)  # Read all rows into memory

    column_index = headers.index(old_column_name)
    headers[column_index] = new_column_name

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)

        for row in rows:
            writer.writerow(row)

    print(f"Info: Column '{old_column_name}' renamed to '{new_column_name}' in file {file_path}")

def move_csv_column(file_path, column_name, new_position):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        rows = list(reader)  # Read all rows into memory

    column_index = headers.index(column_name)
    headers.insert(new_position, headers.pop(column_index))

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)

        for row in rows:
            row.insert(new_position, row.pop(column_index))
            writer.writerow(row)

    print(f"Info: Column '{column_name}' moved to position {new_position} in file {file_path}")

def duplicate_csv_column(file_path, column_name, new_column_name):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        rows = list(reader)  # Read all rows into memory

    column_index = headers.index(column_name)
    headers.insert(column_index + 1, new_column_name)  # Insert new column next to the original

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)

        for row in rows:
            row.insert(column_index + 1, row[column_index])
            writer.writerow(row)

    print(f"Info: Column '{column_name}' duplicated as '{new_column_name}' in file {file_path}")

def insert_csv_column(file_path, header_name, default_value, position):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        rows = list(reader)  # Read all rows into memory

    headers.insert(position, header_name)

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)

        for row in rows:
            row.insert(position, default_value)
            writer.writerow(row)

    print(f"Info: Column '{header_name}' inserted at position {position} in file {file_path}")

def remove_all_columns_starting_from_index(file_path, start_index):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        rows = list(reader)  # Read all rows into memory

    headers = headers[:start_index]

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)

        for row in rows:
            row = row[:start_index]
            writer.writerow(row)

    print(f"Info: Columns starting from index {start_index} removed from file {file_path}")

def remove_rows_containing_sting_in_column(file_path, column_name, string):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        rows = list(reader)  # Read all rows into memory

    column_index = headers.index(column_name)

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)

        for row in rows:
            if string not in row[column_index]:
                writer.writerow(row)

    print(f"Info: Rows containing '{string}' in column '{column_name}' removed from file {file_path}")
    