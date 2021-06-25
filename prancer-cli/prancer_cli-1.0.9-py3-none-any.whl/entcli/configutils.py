"""Enterprise Configuration utilities"""
import configparser
import base64
import os
from cli_enterprise.entcli.fileutils import exists_file, exists_dir, homedir, mkdir_path

CONFIGDIR = '.prancer'
CONFIGFILE = 'config'


def parseint(value, default=0):
    intvalue = default
    try:
        intvalue = int(value)
    except:
        pass
    return intvalue


def parsebool(val, defval=False):
    "Parse boolean from the input value"
    retval = defval
    if val:
        if isinstance(val, str) and val.lower() in ['false', 'true']:
            retval = True if val.lower() == 'true' else False
        else:
            retval = bool(parseint(val))
    return retval


def configdir():
    userhome = homedir()
    configprancer = '%s%s%s' % (userhome, os.path.sep, CONFIGDIR)
    if not exists_dir(configprancer):
        mkdir_path(configprancer)
    return configprancer


def prancer_config():
    prancerdir = configdir()
    configfile = '%s%s%s' % (prancerdir, os.path.sep, CONFIGFILE)
    return configfile
    
    
def get_config_data():
    """Return config data from the config file."""
    config_data = None
    config_file = prancer_config()
    if exists_file(config_file):
        config_data = configparser.ConfigParser(allow_no_value=True)
        config_data.read(config_file)
    return config_data


def config_value(section, key, default=None):
    """Get value for the key from the given config section"""
    config_data = get_config_data()
    if config_data and section in config_data:
        return config_data.get(section, key, fallback=default)
    return default


def make_config():
    config_data = configparser.ConfigParser(allow_no_value=True)
    f = prancer_config()
    config_data.write(open(f, 'w'))

def set_config_value(section, key, value):
    """Set value for the key from the given config section"""
    config_data = get_config_data()
    if config_data and section in config_data:
        config_data.set(section, key, value)
        with open(prancer_config(), 'w') as f:
            config_data.write(f)

def encode_b64(val):
    if val:
        return base64.b64encode(val.encode("ascii")).decode('ascii')
    return None

def decode_b64(val):
    if val:
        return base64.b64decode(val.encode('ascii')).decode('ascii')
    return None