import datetime as dt


"""
datetime manipulations
"""


def string_to_datetime(dates, fmt='%Y-%m-%d'):
    """
    :param dates: List of dates in string format
    :param fmt: Date format in the date strings
    :return: List of dates in datetime format
    """
    if not(isinstance(dates, list)):
        dates = [dates]
    return [dt.datetime.strptime(d, fmt).date() for d in dates]


def datetime_to_string(dt_objs, fmt='%Y-%m-%d'):
    """
    :param dt_objs: List of dates in datetime format
    :param fmt: Date format to create date strings
    :return: List of dates in string format, following the given format
    """
    if not(isinstance(dt_objs, list)):
        dt_objs = [dt_objs]
    return [dt.datetime.strftime(d, fmt) for d in dt_objs]


def datetime_to_days(dates, year_0=1979):
    """
    :param dates: List of dates in datetime format
    :param year_0: Year from which dates are referenced (literally "year 0")
    :return: List of dates in number of days since "year 0"
    """
    _d = []
    for date in datetime_to_string(dates):
        d = str(date).split('-')
        d = (float(d[0])-year_0)*365 + float(d[1])*30 + float(d[2])
        _d.append(d)
    return _d
