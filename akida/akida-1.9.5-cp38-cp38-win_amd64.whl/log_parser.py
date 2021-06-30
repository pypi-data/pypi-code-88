import struct

ina_event = {
    'id': 16,
    'name': 'ina_measure',
    'type': {
        'voltage': {
            'offset': 0,
            'type': 'int'
        },
        'current': {
            'offset': 4,
            'type': 'int'
        }
    }
}
event_defs = {"16": ina_event}


def decode_event_data_object(event_def, data):
    obj = {}
    if isinstance(event_def['type'], str):  # This is not a struct
        return obj

    # If needed, convert to bytes
    values = data
    if isinstance(values, list):
        values = bytes(data)

    for name in event_def['type'].keys():
        desc = event_def['type'][name]
        value = None
        if desc['type'] == 'int':
            value = struct.unpack("I",
                                  values[desc['offset']:desc['offset'] + 4])[0]
        obj[name] = value

    return obj


def decode_event(event_id, data):
    """ Decode event data and return its object representation

    Args:
        event_id (int): a numpy.ndarray
        data (list): a list of bytes.

    Returns:
        :dict: a dictionary of event properties.

    """
    content = None
    if str(event_id) in event_defs:
        event = event_defs[str(event_id)]
        if len(data) > 0:
            content = decode_event_data_object(event, data)
    return content
