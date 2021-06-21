import datetime
import time
from firstimpression.xml import get_text_from_element


def get_datetime_object_from_element(element, name, format):
    """ Gets the datetime object of an element (xml) based on name and format

    :param element: the element from which the date needs to be grabbed
    :type element: xml.etree.ElementTree.Element

    :param name: name of the element in xml which contains date
    :type name: str

    :param format: the format of the datetime in the element
    :type format: str

    :returns: time and date in the right format
    :rtype: date
     """
    unparsed_pubdate = get_text_from_element(element, name)

    created_at = parse_string_to_time(element, format)
    return parse_timestamp_to_date(created_at)


def parse_string_to_time(element, format):
    """ Gets the timestamp of an string in specific format

    :param element: string with the time in it
    :type element: str

    :param format: string with the format devined
    :type format: str

    :returns: time as timestamp
    :rtype: float """
    return parse_date_to_time(parse_string_to_date(element, format))


def parse_date_to_time(date_object):
    return time.mktime(date_object.timetuple())


def parse_string_to_date(element, format):
    return datetime.datetime.strptime(element, format)


def parse_timestamp_to_date(timestamp):
    """ Change timestamp to date object

    :param timestamp: the time in POSIX timestamp
    :type timestamp: float

    :returns: the time as a date
    :rtype: date """
    return datetime.datetime.fromtimestamp(timestamp)


def parse_date_to_string(date_object, format):
    return datetime.datetime.strftime(date_object, format)


def parse_string_time_to_minutes(element):
    [hours, minutes, seconds] = element.split(':')

    minutes = int(minutes)

    if int(seconds) > 30:
        minutes += 1

    minutes += int(hours) * 60

    return minutes

def parse_string_to_string(element, format, new_format):
    return parse_date_to_string(parse_string_to_date(element, format), new_format)

def get_month_text(month_number, month_index, language_index=1):
    return{
        1: [['Jan', 'January'], ['jan', 'januari']],
        2: [['Feb', 'February'], ['feb', 'februari']],
        3: [['Mar', 'March'], ['maart', 'maart']],
        4: [['Apr', 'April'], ['apr', 'april']],
        5: [['May', 'May'], ['mei', 'mei']],
        6: [['June', 'June'], ['juni', 'juni']],
        7: [['July', 'July'], ['juli', 'juli']],
        8: [['Aug', 'August'], ['aug', 'augustus']],
        9: [['Sept', 'September'], ['sept', 'september']],
        10: [['Oct', 'October'], ['okt', 'oktober']],
        11: [['Nov', 'November'], ['nov', 'november']],
        12: [['Dec', 'December'], ['dec', 'december']]
    }[month_number][language_index][month_index]


def parse_date_to_string_full_day_month(date_object, month_type):
    day = str(date_object.day)
    month = get_month_text(date_object.month, month_type, 1)
    return ' '.join([day, month, parse_date_to_string(date_object, '%Y %H:%M')])


def parse_date_to_string_full_month_day(date_object, month_type):
    day = str(date_object.day)
    month = get_month_text(date_object.month, month_type, 0)
    return ' '.join([month, day, parse_date_to_string(date_object, '%Y %H:%M')])

def parse_date_to_string_full(date_object, month_type, language_index):
    if language_index == 1:
        return parse_date_to_string_full_day_month(date_object, month_type)
    else:
        return parse_date_to_string_full_month_day(date_object, month_type)
