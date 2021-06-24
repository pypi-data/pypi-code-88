import sys
import json
from six import iteritems


def delete_key(data, deletion_key):
    if deletion_key in list(data.keys()):
        del data[deletion_key]
    for key, value in iteritems(data):
        if type(value) is dict:
            data[key] = delete_key(value, deletion_key)
    return data


def main(path, deletion_key):
    with open(path, 'r') as json_file:
        data = json.load(json_file)
        data = delete_key(data, deletion_key)
    prefix, file_type = path.rsplit(".", 1)
    new_file_name = prefix + ".min." + file_type
    with open(new_file_name, "w") as json_file:
        json.dump(data, json_file, indent=2)


if __name__ == '__main__':
    """
    sys.argv[1]: Path to the file
    sys.argv[2]: key to be deleted
    for e.g.: > python reduce_model_file.py /path/to/json.json SomeKey

    Recursively traverse in the JSON file and delete the requested key from file.
    Output stored in file with `.min` appended before file type.
    e.g. fileabc.json --> fileabc.min.json
    """
    sys.exit(main(sys.argv[1], sys.argv[2]))
