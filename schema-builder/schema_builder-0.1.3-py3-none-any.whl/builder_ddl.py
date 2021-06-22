def open_ddl_file(file):
    with open(f"{file}") as table:
        table_data = table.readlines()

        return table_data


def clean_data(data):
    step1 = remove_unnecessary_items(data)
    step2 = remove_new_lines(step1)
    table_schema = set_schema_name(step2)

    return table_schema


def remove_unnecessary_items(data):
    clean_data = data[4:-1]

    return clean_data


def remove_new_lines(data):
    new_line_list = []

    for line in data:
        stripped_line = line.strip()

        if line == data[0]:
            new_line_list.append(stripped_line[:-2])
        elif line == data[-1]:
            new_line_list.append(stripped_line.split(' '))
        else:
            new_line_list.append(stripped_line[:-1].split(' '))

    return new_line_list


def set_schema_name(data):
    table_name = data[0].split('.')[1]
    table = [table_name, data[1:]]

    return table

