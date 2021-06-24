import os
import json
import datetime
import calendar
import base64
import binascii
from uuid import uuid4
from sys import version_info

DDB_LOCAL = bool(os.environ.get('INTEG_TEST_DDB_LOCAL'))
TABLE_PREFIX = os.environ.get('INTEG_TEST_TABLE_PREFIX')

SET_TYPES = {'SS', 'NS', 'BS'}


def resolve_table_name(name):
    if TABLE_PREFIX:
        if name.startswith(TABLE_PREFIX):
            return name
        py_version = "py" + str(version_info[0]) + str(version_info[1])
        return TABLE_PREFIX + '-' + py_version + '-' + name
    else:
        return name


def fixup_testcase(obj, ctx, is_response=False):
    ''' Implement a JSON object hook to perform various fixups on the testcases to make comparisons easier. '''
    # Try to base64 decode blob objects
    if 'B' in obj and not isinstance(obj['B'], dict):
        if not isinstance(obj['B'], (bytearray, bytes)):
            try:
                data = base64.b64decode(obj['B'])
            except binascii.Error:
                pass
            else:
                obj['B'] = data

    if 'BS' in obj and not isinstance(obj['BS'], dict):
        for i in range(len(obj['BS'])):
            if obj['BS'][i] and not isinstance(obj['BS'][i], (bytearray, bytes)):
                try:
                    data = base64.b64decode(obj['BS'][i])
                except binascii.Error:
                    pass
                else:
                    obj['BS'][i] = data

    for key in obj:
        # Remove any date-related stuff
        if key.endswith('DateTime'):
            obj[key] = 0

        # Sort the contents of sets
        if key in SET_TYPES:
            # There might be attributes named one of the SET_TYPES
            if isinstance(obj[key], list):
                # key allows all None(s) to be at the end of the list.
                obj[key] = sorted(obj[key], key=lambda x: (x is None, x))

    if 'ClientRequestToken' in obj:
        # There might be multiple requests with same ClientRequestToken. Randomize this.
        obj['ClientRequestToken'] = str(uuid4())
    # Remove variable result fields
    if is_response:
        # Not present in the test data, but possibly in the responses
        obj.pop('ItemCollectionMetrics', None)

    if DDB_LOCAL:
        obj.pop('ConsumedCapacity', None)
    else:
        # Keep ConsumedCapacity from DDB but set CapacityUnits to 0.0
        if "CapacityUnits" in obj:
            obj["CapacityUnits"] = 0.0

        # Sort by table name for comparisons
        if 'ConsumedCapacity' in obj and isinstance(obj['ConsumedCapacity'], list):
            obj['ConsumedCapacity'].sort(key=lambda cc: cc['TableName'])

    if 'TableName' in obj:
        obj['TableName'] = resolve_table_name(obj['TableName'])

    # Resolve table names for BatchGet/BatchWrite
    if 'RequestItems' in obj:
        req_items = obj['RequestItems']
        new_req_items = {}
        table_names = list(obj['RequestItems'].keys())
        for table_name in table_names:
            new_table_name = resolve_table_name(table_name)
            new_req_items[new_table_name] = req_items[table_name]

        obj['RequestItems'] = new_req_items

    # Sort responses so that they compare consistently
    if 'Responses' in obj:
        if isinstance(obj['Responses'], list):
            # transact-get-items response don't need fixup. Skip this step
            pass
        else:
            # batch-get-items
            ordered_responses = {}
            for table, responses in obj['Responses'].items():
                ordered_responses[resolve_table_name(table)] = sorted(responses, key=flatten_dict)
            obj['Responses'] = ordered_responses

    # Sort Scan/Query items so that they compare consistently
    if 'Items' in obj:
        obj['Items'] = sorted(obj['Items'], key=flatten_dict)

    # Deal with COUNT queries
    # Only do this for testcases, not responses
    if not is_response:
        # Keep track of if this is a COUNT Query
        if 'Select' in obj and obj['Select'] == 'COUNT':
            ctx['is_count'] = True

    return obj


def fixup_response(response):
    ''' Make sure a response obeys the same rules as the expected response. '''
    response.pop('ResponseMetadata', None)  # If using DDB directly

    # Round-trip through JSON so that the same object_hook can be applied as the testcase
    fixup_ctx = {}
    return json.loads(
        json.dumps(response, default=encode_unknown, sort_keys=True),
        object_hook=lambda obj: fixup_testcase(obj, fixup_ctx, is_response=True))


def encode_unknown(obj):
    if isinstance(obj, (bytes, bytearray)):
        return base64.b64encode(obj).decode('ascii')

    if isinstance(obj, datetime.datetime):
        return calendar.timegm(obj.timetuple())

    raise TypeError()


def flatten_dict(d):
    ''' Flatten a dict into lists of tuples so that it is comparable. '''
    if isinstance(d, dict):
        return sorted([(k, flatten_dict(v)) for k, v in d.items()], key=flatten_dict)
    elif isinstance(d, list):
        return sorted([flatten_dict(e) for e in d], key=flatten_dict)
    else:
        return d
