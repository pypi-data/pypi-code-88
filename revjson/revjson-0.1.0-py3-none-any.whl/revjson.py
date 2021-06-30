import json


def load_from_file(filename, encode_format="utf-8"):
    """Load a JSON file"""

    return json.load(open(filename, "r", encoding=encode_format))


def save_to_file(json_obj, filename, indent=4, encode_format="utf-8"):
    """Save a JSON file"""

    json.dump(
        json_obj,
        open(filename, "w", encoding=encode_format),
        indent=indent,
        ensure_ascii=False,
    )


def print_json(json_obj, indent=4):
    """Display a formatted dict"""

    print(json.dumps(json_obj, indent=indent, ensure_ascii=False))


def json_from_str(text):
    """Convert JSON string to dict"""

    return json.loads(text)


def json_to_str(json_obj):
    """Convert dict to JSON string"""

    return json.dumps(json_obj, separators=(",", ":"), ensure_ascii=False)
