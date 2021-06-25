from firstimpression.api.request import request_json
from firstimpression.time import parse_string_to_date, parse_string_time_to_minutes, parse_date_to_string, parse_string_to_string


def get_response(url, headers, params):
    response_json = request_json(url, headers, params)

    if response_json.get('statusCode', None) == 429:
        raise Exception('Rate limit exceeded')

    return response_json


def get_departures(response_json):
    return response_json['payload']['departures']


def get_departure_time(departure):
    return departure['plannedDateTime'][:-5]


def get_actual_departure_time(departure):
    return departure['actualDateTime'][:-5]


def get_departure_number(departure):
    return departure['product']['number']


def get_destination(departure):
    return departure['direction']


def get_train_category(departure):
    return departure['product']['longCategoryName']


def get_route_text(departure):
    # Returns string with stations on route in this format: '{station}, {station}, {station}'
    return ', '.join([station['mediumName'] for station in departure['routeStations']])


def get_operator(departure):
    return departure['product']['operatorName']


def get_planned_track(departure):
    if get_actual_track(departure) == '':
        return departure['plannedTrack']
    else:
        return get_actual_track(departure)


def get_actual_track(departure):
    return departure.get('actualTrack', '')


def get_delay(departure, date_format):
    try:
        if departure['cancelled'] == True:
            return 'Rijdt niet'
    except KeyError:
        pass

    planned_departure_time = parse_string_to_date(
        get_departure_time(departure), date_format)
    actual_departure_time = parse_string_to_date(
        get_actual_departure_time(departure), date_format)

    if planned_departure_time < actual_departure_time:
        delayed_time = actual_departure_time - planned_departure_time
        delayed_minutes = parse_string_time_to_minutes(str(delayed_time))
        return ''.join(['+', str(delayed_minutes), ' min'])
    else:
        return ''


def get_message(departure):
    try:
        message = departure.get('messages', False)
        if message:
            msg = message[0]['message']
        else:
            msg = ''
    except KeyError:
        msg = ''
    return msg


def get_parsed_departures(response_json, date_format):
    departures = get_departures(response_json)
    parsed_departures = list()
    for departure in departures:
        parsed_departure = dict()
        parsed_departure['departure_number'] = get_departure_number(departure)
        parsed_departure['departure_time'] = parse_string_to_string(get_departure_time(departure), date_format, '%H:%M')
        parsed_departure['destination'] = get_destination(departure)
        parsed_departure['train_category'] = get_train_category(departure)
        parsed_departure['route_text'] = get_route_text(departure)
        parsed_departure['operator'] = get_operator(departure)
        parsed_departure['planned_track'] = get_planned_track(departure)
        parsed_departure['delay'] = get_delay(departure, date_format)
        parsed_departure['message'] = get_message(departure)
        parsed_departures.append(parsed_departure)

    return parsed_departures
