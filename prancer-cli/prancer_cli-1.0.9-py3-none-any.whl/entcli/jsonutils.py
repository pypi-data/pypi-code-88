""" Utility functions for json."""

import re
import json
import time
import glob
from collections import OrderedDict
from cli_enterprise.entcli.fileutils import exists_file, exists_dir, mkdir_path


def save_json_to_file(indata, outfile):
    """Save json data to the file"""
    if indata is not None:
        try:
            instr = json.dumps(indata, indent=2, default=json_util.default)
            with open(outfile, 'w') as jsonwrite:
                jsonwrite.write(instr)
        except:
            pass


def json_from_string(json_str):
    """Get json from the string."""
    try:
        jsondata = json.loads(json_str)
        return jsondata
    except:
        logger.debug('Failed to load json data: %s', json_str)
    return None


def json_from_file(jsonfile, escape_chars=None):
    """ Get json data from the file."""
    jsondata = None
    try:
        if exists_file(jsonfile):
            file_data = None
            try:
                with open(jsonfile) as infile:
                    file_data = infile.read()
            except UnicodeDecodeError:
                with open(jsonfile, 'r', encoding='utf-8') as infile:
                    file_data = infile.read()

            if escape_chars and isinstance(escape_chars, list):
                for escape_char in escape_chars:
                    file_data = file_data.replace(escape_char, '\\\%s' % escape_char)
            jsondata = json.loads(file_data, object_pairs_hook=OrderedDict)
    except Exception as ex:
        logger.debug('Failed to load json from file: %s, exception: %s', jsonfile, ex)
    return jsondata


def valid_json(json_input):
    """ Checks validity of the json """
    try:
        _ = json.loads(json_input)
        return True
    except:
        print('Not a valid json: %s' % json_input)
    return False


def check_field_exists(data, parameter):
    """Utility to check json field is present."""
    present = False
    if data and parameter:
        fields = parameter.split('.')
        curdata = data
        if fields:
            allfields = True
            for field in fields:
                if curdata:
                    if field in curdata and isinstance(curdata, dict):
                        curdata = curdata[field]
                    else:
                        allfields = False
            if allfields:
                present = True
    return present


def get_field_value_with_default(data, parameter, defval):
    """get json value for a nested attribute, else return default value."""
    retval = get_field_value(data, parameter)
    return retval if retval else defval


def get_field_value(data, parameter):
    """get json value for a nested attribute."""
    retval = None
    parameter = parameter[1:] if parameter and parameter.startswith('.') else parameter
    fields = parameter.split('.') if parameter else None
    if data and fields:
        retval = data
        for field in fields:
            match = re.match(r'(.*)\[(\d+)\]', field, re.I)
            if match:
                field, index = match.groups()
                retval = retval[field] if retval and field in retval and isinstance(retval, dict) else None
                i = int(index)
                retval = retval[i] if retval and isinstance(retval, list) and i < len(retval) else None
            else:
                retval = retval[field] if retval and field in retval and isinstance(retval, dict) else None
    return retval


def put_value(json_data, field, value):
    """Put the value for a multiple depth key."""
    data = json_data
    field = field[1:] if field and field.startswith('.') else field
    fields = field.split('.') if field else []
    for idx, fld in enumerate(fields):
        if idx == len(fields) - 1:
            data[fld] = value
        else:
            if fld not in data or not isinstance(data[fld], dict):
                data[fld] = {}
        data = data[fld]


def parse_boolean(val):
    """String to boolean type."""
    return True if val and val.lower() == 'true' else False


def set_timestamp(json_data, fieldname='timestamp'):
    """Set the current timestamp for the object."""
    if not isinstance(json_data, dict):
        return False
    timestamp = int(time.time() * 1000)
    json_data[fieldname] = timestamp
    return True

