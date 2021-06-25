import re


def find_between_quotations(s, q='"'):
    try:
        if q == '"':
            return re.findall('"([^"]*)"', str(s))[0]
        elif q == "'":
            return re.findall("'([^']*)'", str(s))[0]
    except IndexError:
        return print('No match')


def find_number(s):
    return re.findall(r'\d+', s)


def tuple_to_equal(a):
    chars = r"()"
    for c in chars:
        if c in a:
            a = a.replace(c, "")
    return a.replace(", ", " = ")
