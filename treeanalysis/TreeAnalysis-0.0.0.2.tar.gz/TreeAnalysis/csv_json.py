import csv,json,logging
import pandas as pd
from pprint import pprint

#See logging
logging.basicConfig(level=logging.INFO)


#Takes the list of dictionaries and will group them by a common key in each dict.
def get_mapping(flat_data:list, key:str):
    mapping = {}
    for obj in flat_data:
        index = obj[key]
        if index not in mapping:
            mapping[index] = [obj]
        else:
            mapping[index].append(obj)
    return mapping

#Finds the intersection of all keys within a list of dictionaries.
def get_property_keys(mapping):
    property_keys = None
    for _,values in mapping.items():
        #Instantiate all keys
        if property_keys is None: property_keys = set(values[0].keys())

        #Find intersection of values
        property_values = set.intersection(*map(set,[v.values() for v in values]))

        #Revese map to their keys
        keys = set(key for key,value in values[0].items() if value in property_values)
        
        #Intersect with global propety_keys
        property_keys = property_keys & keys
    return property_keys,keys

#Converts a csv file with a one to many relationship into a json format.
#Collects the keys in which to restructure the csv.
#obj = {key: value.strip().strip() for key,value in values[0].items() if key in property_keys}
def get_structure(flat_data,columns,used_keys=set()):
    if isinstance(columns,str): columns = [columns]
    else:
        column = columns[0]
        columns = columns[1:]
        if ':' in column:
            column,key = column.split(':')
        elif '=' in column:
            column,key = column.split('=')
        else:
            key = "results"

    try:
        mapping = get_mapping(flat_data,column)
    except KeyError:
        return []
    
    property_keys,keys = get_property_keys(mapping)
    if len(columns) == 0:
        remaining_keys = keys-used_keys-property_keys
        return [property_keys,remaining_keys]

    new_flat_data = []
    for _,values in mapping.items():
        new_flat_datum = [{key: value for key,value in v.items() if key not in property_keys} for v in values]
        new_flat_data += new_flat_datum
    return [property_keys] + get_structure(new_flat_data, columns, used_keys|property_keys)

def apply_structure(flat_data,columns,structure):
    if len(structure) == 0: return None
    layer = structure[0] #Pull out this layer's structure
    structure = structure[1:] #Remove it from the list
    #Do the same for the column index
    if isinstance(columns,str): columns = [columns]
    elif len(columns)==0:
        return [{k:v.strip() for k,v in obj.items() if k in layer} for obj in flat_data]
    else:
        column = columns[0]
        if ':' in column:
            column,key = column.split(':')
        elif '=' in column:
            column,key = column.split('=')
        else:
            key = "results"
        columns = columns[1:]
    #Organize the data in a mapping again.
    try:
        mapping = get_mapping(flat_data,column)
    except KeyError:
        return []

    output = []
    #Loop through objects and only keep objects in this layer's structure
    for _,values in mapping.items():
        #Intersect with this layer's keys
        obj = {key: value.strip() for key,value in values[0].items() if key in layer}
        
        #Next layer
        results = apply_structure(values,columns,structure)
        if results is not None:
            obj[key] = results
        output.append(obj)
    return output

def csv_to_json(reader,columns):
    logging.info("Getting Structure")
    reader = csv.DictReader(open(args.filename),quotechar='"',quoting=csv.QUOTE_ALL,delimiter=',',skipinitialspace=True)
    structure = get_structure(reader,args.columns)
    reader = csv.DictReader(open(args.filename),quotechar='"',quoting=csv.QUOTE_ALL,delimiter=',',skipinitialspace=True)
    logging.info("Applying Structure")
    data = apply_structure(reader,args.columns,structure)
    return data

if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Convert csv to json. (Family tree now data)')
    parser.add_argument("filename",type=str,help="Path to input csv file.")
    parser.add_argument("columns",nargs='+', type=str,help="Sucessive columns to join by.")
    args = parser.parse_args()
    logging.info(f"Opening {args.filename}")
    data = csv_to_json(args.filename,args.columns)
    logging.info("Writing")
    json.dump(data,open(args.filename.replace('.csv','.json'),'w+'),indent=2)
