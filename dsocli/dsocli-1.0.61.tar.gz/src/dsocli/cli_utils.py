
import json
import yaml
import csv
from .logger import Logger
from .exceptions import DSOException
from .constants import *

###--------------------------------------------------------------------------------------------

def print_list(items):
    if len(items):
        for item in items:
            print(item, flush=True)

###--------------------------------------------------------------------------------------------

def format_data(data, query, format):

    if not data: return ''

    if query:
        import jmespath
        result = jmespath.search(query, data)
    else:
        result = data

    if not result: return ''

    if format == 'json':
        import json
        return json.dumps(result, sort_keys=False, indent=2)

    elif format == 'yaml':
        import yaml
        return yaml.dump(result, sort_keys=False, indent=2)

    ### expects list(dict), or a dict, otherwise best-effort
    elif format in 'csv':
        import io
        import csv
        output = io.StringIO()
        writer = csv.writer(output)
        if isinstance(result, list) and len(result):
            if isinstance(result[0], dict):
                writer.writerow(result[0].keys())
                for item in result:
                    writer.writerow(item.values())
            else:
                writer.writerow(result)
        elif isinstance(result, dict) and len(result):
            keys = list(result.keys())
            ### if data is dictionary with single key whose value is a list, process the child list instead
            if len(keys) == 1:
                childList = result[keys[0]]
                if isinstance(childList, list) and len(childList):
                    if isinstance(childList[0], dict):
                        writer.writerow(childList[0].keys())
                        for item in childList:
                            writer.writerow(item.values())
                    else:
                        writer.writerow(childList)
                else:
                    writer.writerow(keys)
                    writer.writerow(result.values())
            elif len(keys) > 1:
                writer.writerow(keys)
                writer.writerow(result.values())
        else:
            writer.writerow(result)
        
        return output.getvalue()

    ### tab delimilted with no headers
    ### expects list(dict), or a dict, otherwise best-effort
    elif format == 'raw':
        outputStream = ''
        if isinstance(result, list):
            for i in range(0, len(result)):
                item = result[i]
                if isinstance(item, dict):
                    valuesStr = '\t'.join(map(str, list(item.values())))
                else:
                    valuesStr = str(item)
                outputStream += f"{valuesStr}"
                if i < len(result)-1: outputStream += '\n'
        elif isinstance(result, dict):
            keys = list(result.keys())
            ### if data is dictionary with single key whose value is a list, process the child list instead
            if len(keys) == 1:
                childList = result[keys[0]]
                if isinstance(childList, list):
                    for i in range(0, len(childList)):
                        item = childList[i]
                        if isinstance(item, dict):
                            valuesStr = '\t'.join(map(str, list(item.values())))
                        else:
                            valuesStr = str(item)
                        outputStream += f"{valuesStr}"
                        if i < len(childList)-1: outputStream += '\n'
                else:
                    outputStream = '\t'.join(map(str, list(result.values())))
            elif len(keys) > 1:
                outputStream = '\t'.join(map(str, list(result.values())))
        else:
            outputStream += str(result)
        
        return outputStream

    ### expects list(dict), or a dict
    ### take first key as name and second key as value, and form name=value
    elif format == 'shell':

        def quote(value):
            import re
            ### no quoting numbers
            if re.match(r"^[1-9][0-9]*$", value) or re.match(r"^[0-9]*\.[0-9]*$", value):
                return value
            ### double quote if contains single quote
            elif re.match(r"^.*[']+.*$", value):
                return f'"{value}"'
            ### sinlge quote by default
            else:
                return f"'{value}'"

        outputStream = ''
        if isinstance(result, list) and len(result):
            if isinstance(result[0], dict):
                if len(result[0].keys()) < 2:
                    raise DSOException(f"Unable to format data as it is incompatible with the 'shell' format.")
                for item in result:
                    key = item[list(item.keys())[0]]
                    value = quote(item[list(item.keys())[1]])
                    outputStream += f"{key}={value}\n"
            else:
                raise DSOException(f"Unable to format data as it is incompatible with the 'shell' format.")
        elif isinstance(result, dict):
            keys = list(result.keys())
            ### if data is dictionary with single key whose value is a list, process the child list instead
            if len(keys) == 1:
                childList = result[keys[0]]
                if isinstance(childList, list) and len(childList):
                    if len(childList[0].keys()) < 2:
                        raise DSOException(f"Unable to format data as it is incompatible with the 'shell' format.")
                    for item in childList:
                        key = item[list(item.keys())[0]]
                        value = quote(item[list(item.keys())[1]])
                        outputStream += f"{key}={value}\n"
                else:
                    outputStream = '\t'.join(map(str, list(result.values())))
            elif len(keys) > 1:
                outputStream = '\t'.join(map(str, list(result.values())))


        else:
            raise DSOException(f"Unable to format data as it is incompatible with the 'shell' format.")
        
        return outputStream

    else:
        raise DSOException(f"Output format '{format}' is not supported.")

###--------------------------------------------------------------------------------------------

def read_data(input, parent_key, keys, format):
    result = []
    if format == 'json':
        try:
            if parent_key:
                data = json.load(input)[parent_key]
            else:
                data = json.load(input)
        # except json.JSONDecodeError as e:
        except:
            raise DSOException(CLI_MESSAGES['InvalidFileFormat'].format(format))

        if not len(data): return []

        for key in keys:
            if not key in data[0].keys():
                raise DSOException(CLI_MESSAGES['MissingField'].format(key))

        for row in data:
            record = {}
            for key in keys:
                record[key] = row[key]
            result.append(record)

    elif format == 'yaml':
        try:
            if parent_key:
                data = yaml.load(input, yaml.SafeLoader)[parent_key]
            else:
                data = yaml.load(input, yaml.SafeLoader)
        # except yaml.YAMLError as e:
        except:
            raise DSOException(CLI_MESSAGES['InvalidFileFormat'].format(format))

        if not len(data): return []

        for key in keys:
            if not key in data[0].keys():
                raise DSOException(CLI_MESSAGES['MissingField'].format(key))

        for row in data:
            record = {}
            for key in keys:
                record[key] = row[key]
            result.append(record)
            
    elif format == 'csv':
        try:
            data = list(csv.reader(input))
        except:
            raise DSOException(CLI_MESSAGES['InvalidFileFormat'].format(format))

        if not len(data): return []

        header = data[0]
        if len(header) < len(keys):
            raise DSOException(CLI_MESSAGES['InvalidFileFormat'].format(format))

        for i in range(0, len(keys)):
            key = keys[i]
            if not key == header[i]:
                raise DSOException(CLI_MESSAGES['MissingField'].format(key))

        for row in data[1:]:
            record = {}
            for i in range(0, len(keys)):
                record[keys[i]] = row[i]
            result.append(record)

    elif format == 'raw':
        data = input.readlines()
        try:
            for row in data:
                record = {}
                for i in range(0, len(keys)):
                    record[keys[i]] = row.split('\t')[i].strip()
                result.append(record)
        except:
            raise DSOException(CLI_MESSAGES['InvalidFileFormat'].format(format))

    elif format == 'shell':
        data = input.readlines()
        try:
            for row in data:
                record = {}
                for i in range(0, len(keys)):
                    record[keys[i]] = row.split('=')[i].strip()
                result.append(record)
        except:
            raise DSOException(CLI_MESSAGES['InvalidFileFormat'].format(format))

    
    return result