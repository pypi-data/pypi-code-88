def parse_formatted_table(table_data, table_name):
    end_data_index = table_data.index(('', None, None))
    clean_table = table_data[1:end_data_index]
    parsed_table = [table_name, []]

    for row in clean_table:
        parsed_table[1].append([row[0], row[1]])

    return parsed_table
