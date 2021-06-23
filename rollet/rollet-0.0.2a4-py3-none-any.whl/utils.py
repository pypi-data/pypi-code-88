
import re

def rfinditem(obj, key):
    """
    Find key recursively in dict
    obj: Dict
    key: str
    :return: None or dict item
    """
    if key in obj: return obj[key]
    for k, v in obj.items():
        if isinstance(v, dict):
            item = rfinditem(v, key)
            if item is not None:
                return item


def lookup(term, zipped):
    """
    Find in zipped term's value if match pattern
    term: str
    zipped: list of tuples
    :return: None or value
    """
    for pattern, value in zipped:
        if re.search(pattern, term):
            return value
    return None