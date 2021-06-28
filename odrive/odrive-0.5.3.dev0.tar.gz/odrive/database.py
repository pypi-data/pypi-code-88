





"""

"""

import json
import jsonschema
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
db_dir = os.path.join(os.path.dirname(os.path.dirname(script_dir)), 'data')

def load(validate = False):
    """
    validate: Validates all JSON files that are being loaded against their schema.
    Requires jsonschema to be installed.
    """
    db = {
        'odrives': {},
        'drvs': {}
    }

    if validate:
        with open(os.path.join(db_dir, "schema.json")) as fp:
            schema = json.load(fp)
        odrive_validator = jsonschema.Draft4Validator({**schema, **{"$ref": "#/$defs/odrive"}})
        drv_validator = jsonschema.Draft4Validator({**schema, **{"$ref": "#/$defs/drv"}})

    for file in os.listdir(db_dir):
        name, ext = os.path.splitext(file)
        file = os.path.join(db_dir, file)
        if os.path.isfile(file) and ext.lower() == '.json':
            if name.startswith("odrive-"):
                with open(file) as fp:
                    data = json.load(fp)
                if validate:
                    try:
                        odrive_validator.validate(data)
                    except jsonschema.exceptions.ValidationError as ex:
                        raise Exception("error while processing " + file) from ex
                db['odrives'][name.partition("odrive-")[-1]] = data

            elif name.startswith("drv-"):
                with open(file) as fp:
                    data = json.load(fp)
                if validate:
                    try:
                        drv_validator.validate(data)
                    except jsonschema.exceptions.ValidationError as ex:
                        raise Exception("error while processing " + file) from ex
                db['drvs'][name.partition("drv-")[-1]] = data

            elif name == "schema" or name.startswith("schema-"):
                pass # ignore
            else:
                pass # unknown file

    for odrive in db['odrives'].values():
        for inv in odrive['inverters']:
            if len(inv['drv'].keys()) == 1 and '$ref' in inv['drv'].keys():
                inv['drv'] = db['drvs'][inv['drv']['$ref']]

    return db

def get(typename, name):
    """
    Loads the data for a particular device.
    Parameters:
    type: The type of the device, e.g. "odrive", "motor", "encoder", ...
    name: The name or version of the device, e.g. "v3.6", "D6374_150KV", ...
    """
    return db[typename + 's'][name]
    
def try_get(typename, name, default):
    if name in db[typename + 's']:
        return db[typename + 's'][name]
    else:
        return default

db = load()
