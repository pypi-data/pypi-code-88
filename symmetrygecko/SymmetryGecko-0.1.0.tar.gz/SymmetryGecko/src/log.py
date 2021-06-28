import datetime
from .. import config

def prettify_list(data):
    """ returns list as pretty sting """
    result = "[\n"
    for d in data:
        result += "\t" + str(d) + ",\n"
    result += "]"
    return result

def log(message, filename, add_prefix=True):
    """" add_prefix = True adds timestamp as prefix """
    filepath = config.FOLDERPATH_LOG() + datetime.datetime.now().strftime("%B %d, %Y") + "-" + filename
    if not add_prefix: filepath = config.FOLDERPATH_LOG() + filename

    with open(filepath, "w+") as f:
        f.write( str(message))