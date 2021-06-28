def int_value_or_none(possible_int):
    try:
        return int(possible_int)
    except ValueError:
        return None
