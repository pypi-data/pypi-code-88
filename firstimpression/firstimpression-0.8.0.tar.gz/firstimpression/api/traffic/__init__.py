from geopy import distance
import xml.etree.ElementTree as ET

METER_TO_KILOMETER_DIVIDER = 1000
KILOMETER_APPENDIX = ' km'
UNKNOWN_JAM_DISTANCE_MESSAGE = 'onbekend'


def get_road_type(circumstance):
    try:
        return circumstance['roadNumber'][0]
    except KeyError:
        return False


def get_road(circumstance):
    try:
        return circumstance['roadNumber']
    except KeyError:
        return False


def get_road_number(circumstance):
    # Get road number (without A or N)
    try:
        return circumstance['roadNumber'][1:]
    except KeyError:
        return False


def get_from(circumstance):
    from_location = circumstance['directionText'].split(' - ')[0]
    return from_location


def get_to(circumstance):
    to_location = circumstance['directionText'].split(' - ')[1]
    return to_location


def get_length(circumstance):
    total_length = circumstance.get('total_length', None)
    if total_length is None:
        return ''
    else:
        return int(total_length)


def get_length_string(circumstance):
    length = circumstance.get('total_length', '')
    if length:
        return ''.join([str(int(length / METER_TO_KILOMETER_DIVIDER)), KILOMETER_APPENDIX])
    else:
        return UNKNOWN_JAM_DISTANCE_MESSAGE


def get_reason(circumstance):
    return circumstance.get('cause', '')


def get_area_detail(circumstance):
    return circumstance.get('locationText', '')


def get_event(circumstance):
    return circumstance.get('title', '')


def get_description(circumstance):
    return circumstance.get('description', '')


def get_type(circumstance):
    return circumstance.get('obstructionType', 0)


def get_total_delay_string(circumstance):
    # returns string with delay in minutes or False

    total_delay = circumstance.get('delay', '')

    if total_delay:
        # Round up minutes
        return '+{} min'.format(total_delay)
    else:
        return ''


def get_coordinates(circumstance):
    try:
        return {'longitude': circumstance['longitude'],
                'latitude': circumstance['latitude']
                }
    except KeyError:
        return False


def get_distance_to_circumstance(from_coordinates, to_coordinates):
    # Calculates distance from one coordinate to another (WATCH OUT: straight line, so no roads taken into account)
    if not from_coordinates or not to_coordinates:
        return ''

    coords_1 = (from_coordinates['latitude'], from_coordinates['longitude'])
    coords_2 = (to_coordinates['latitude'], to_coordinates['longitude'])

    return distance.distance(coords_1, coords_2).km


def parse_circumstance(circumstance, own_coordinates):
    # Parses JSON from API to own format. Junk data is removed.
    parsed_circumstance = dict()

    parsed_circumstance['road_type'] = get_road_type(circumstance)
    parsed_circumstance['road'] = get_road(circumstance)
    parsed_circumstance['road_number'] = get_road_number(circumstance)
    parsed_circumstance['from'] = get_from(circumstance)
    parsed_circumstance['to'] = get_to(circumstance)
    parsed_circumstance['length'] = get_length(circumstance)
    parsed_circumstance['length_string'] = ''
    parsed_circumstance['reason'] = get_reason(circumstance)
    parsed_circumstance['area_detail'] = get_area_detail(circumstance)
    parsed_circumstance['event'] = get_event(circumstance)
    parsed_circumstance['description'] = get_description(circumstance)
    parsed_circumstance['type'] = get_type(circumstance)
    parsed_circumstance['total_delay'] = get_total_delay_string(circumstance)
    parsed_circumstance['coordinates'] = get_coordinates(circumstance)

    parsed_circumstance['distance_to_circumstance'] = get_distance_to_circumstance(
        own_coordinates, parsed_circumstance['coordinates'])

    return parsed_circumstance


def parse_circumstances(circumstances, own_coordinates):
    parsed_circumstances = list()
    for circumstance in circumstances:
        parsed_circumstances.append(
            parse_circumstance(circumstance, own_coordinates))
    return parsed_circumstances


def parse_circumstances_to_XML(circumstances, exclude_items):
    # Parses list of json objects to XML
    root = ET.Element("root")
    for circumstance in circumstances:
        item = ET.SubElement(root, 'item')
        for attribute in circumstance:
            if attribute not in exclude_items:
                ET.SubElement(item, attribute).text = str(
                    circumstance[attribute])

    return root


def sort_longest_jams(jams):
    # Sorts longest jams starting with longest to shortest
    return sorted(jams, key=lambda i: i['length'], reverse=True)


def sort_closest_jams(jams):
    # Sorts jams that are closest to own location
    return sorted(jams, key=lambda i: i['distance_to_circumstance'])


def get_jams(circumstances, jam_type):
    # Filters jams from all possible circumstances which could be f.e. road works and/or police controls
    jams = list()
    for circumstance in circumstances:
        if circumstance['type'] == jam_type:
            jams.append(circumstance)
    return jams


def get_total_jam_length(circumstances):
    return circumstances['totalLengthOfJams'] / METER_TO_KILOMETER_DIVIDER


def get_total_jams_delay(jams):
    total_delay = 0
    for jam in jams:
        try:
            total_delay += int(jam['total_delay'].split(' ').pop(0))
        except (TypeError, ValueError):
            continue
    if total_delay > 60:
        return '{}+ uur'.format(int(total_delay / 60))
    else:
        return '{} min'.format(int(total_delay))


def get_total_length_string(total_length):
    return '{}{}'.format(total_length, KILOMETER_APPENDIX)


def get_only_highways(circumstances):
    specific_circumstances = list()
    for circumstance in circumstances:
        if circumstance['road_type'] == 'A':
            specific_circumstances.append(circumstance)
    return specific_circumstances
