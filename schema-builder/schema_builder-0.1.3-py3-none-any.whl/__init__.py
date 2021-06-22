import json
import os
import logging
from schema_builder.builder_ddl import open_ddl_file, clean_data
from schema_builder.builder_table_list import parse_formatted_table


def build_json_schema(source_type, file=None, data=None, table_name=None):
    if source_type == 'ddl':
        return schema_from_ddl(file)
    elif source_type == 'table':
        return schema_from_table(data, table_name)
    else:
        return "Please enter a valid source type [ddl, table]."


def schema_from_ddl(file):
    if file == None:
        return "Please enter a valid file path."

    raw_table_data = open_ddl_file(file)
    clean_table_data = clean_data(raw_table_data)
    table_name = clean_table_data[0]
    table_dict = create_table_dict(clean_table_data)
    json_schema_dict = create_json_schema_dict(table_dict)

    return create_json_schema_file(json_schema_dict, table_name)


def schema_from_table(data, table_name):
    if data == None:
        return "Please provide data from a SQL DESCRIBE FORMATTED query."
    
    if table_name == None:
        return "Please provide a table name."

    clean_table_data = parse_formatted_table(data, table_name)
    table_dict = create_table_dict(clean_table_data)
    json_schema_dict = create_json_schema_dict(table_dict)

    return create_json_schema_file(json_schema_dict, table_name)


def create_table_dict(data):
    table_dict = {}
    table_columns = data[1]

    for row in table_columns:
        data_type = find_data_type(row[1])
        table_dict[row[0]] = data_type

    return table_dict


def find_data_type(data):
    lowercase_data = data.lower()

    if 'int' in lowercase_data:
        return {"type": ["integer", "null"]}
    elif 'bigint' in lowercase_data:
        return {"type": ["integer", "null"]}
    elif 'decimal' in lowercase_data:
        return {"type": ["number", "null"]}
    elif 'varchar' in lowercase_data:
        return {"type": ["string", "null"]}
    elif 'char' in lowercase_data:
        return {"type": ["string", "null"]}
    elif 'string' in lowercase_data:
        return {"type": ["string", "null"]}
    elif 'timestamp' in lowercase_data:
        return {"type": ["string", "null"]}
    elif 'offset_date_time' in lowercase_data:
        return {"type": ["string", "null"]}
    elif 'date' in lowercase_data:
        return {"type": ["string", "null"]}


def create_json_schema_dict(data):
    json_schema = {
        "type": ["object", "null"],
        "properties": data
    }

    return json_schema


def create_json_schema_file(data, table_name):
    json_schema = json.dumps(data, indent=4)
    path = os.getcwd()

    try:
        os.mkdir(f'{path}/json_schemas')
    except FileExistsError:
        logging.info('/json_schemas directory already exists.')

    with open(f"{path}/json_schemas/{table_name}_schema.json", "w") as schema:
        schema.write(json_schema)

    return f"{table_name}_schema.json created successfully."

