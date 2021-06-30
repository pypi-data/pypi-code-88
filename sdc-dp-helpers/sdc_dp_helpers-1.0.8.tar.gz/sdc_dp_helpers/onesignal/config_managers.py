from datetime import datetime


def date_to_unix(date_string, fmt='%Y-%m-%d'):
    """
    Takes a standard date string and converts it into unix timestamp.
    """
    date = datetime.strptime(date_string, fmt)
    return date.strftime("%s")
