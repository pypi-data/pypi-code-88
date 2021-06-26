from pydoc import locate


def get_all_fields(fields: list, rest: dict) -> list:
    for key in rest:
        fields.append(key)
    return fields


def str_to_class(path):
    try:
        my_class = locate(path)
    except ImportError:
        raise ValueError('Module does not exist')
    return my_class or None
