""" 
obsinfo information file routines, contained in superclass OBSMetadata for generality
"""
# Standard library modules
import json
import pprint
from pathlib import Path, PurePath 
import sys
import pkg_resources
import re
from urllib.parse import urlparse
from urllib.parse import unquote

# Non-standard modules
import jsonschema
import jsonref
import yaml


# Local modules
from ..misc import yamlref
from ..misc.yamlref import JsonLoader
from ..misc.remoteGitLab import gitLabFile

root_symbol = "#"
VALID_FORMATS = ["JSON", "YAML"]
VALID_TYPES = [
    "campaign",
    "network",
    "station",
    "instrumentation",
    "datalogger",
    "preamplifier",
    "sensor",
    "response",
    "stage",
    "filter",
]

class ObsMetadata(dict):
    
    def __init__(self, *args, **kwargs):
        """
        Constructor, simply create a dict
        """
        
        super().__init__(*args, **kwargs)
        #self.convert_to_obsmetadata()
        
    def convert_to_obsmetadata(self):
        """
        Make all contained dictionaries ObsMetadata
        """
        for key, value in self.items():
            if isinstance(value, dict):
                self[key] = self.__class__(value)
                self[key].convert_to_obsmetadata()
            elif isinstance(value, list):
                for x in value:
                   if isinstance(x, dict):
                      x = self.__class__(x)
                      x.convert_to_obsmetadata()    
        
    def list_valid_types():
        """
        Returns a list of valid information file types
        """
        return VALID_TYPES


    def get_information_file_type(filename):
        """
        Determines the type of a file, assuming that the filename is "*.{TYPE}.{SOMETHING}
        """
    
        #the_type = filename.split(".")[-2].split("/")[-1].lower()
        stem_file = PurePath(filename).stem
        the_type = (PurePath(stem_file).suffix)[1:]
        
        if the_type in VALID_TYPES:
            return the_type
        print(f"Unknown type: {the_type}")
        sys.exit(1)
    
    
    def validate(self, datapath, filename, format=None, type=None, verbose=False,
                 schema_file=None, quiet=False):
        """
        Validates a YAML or JSON file against schema
        type: "network", "datalogger", "preamplifier", "sensor", "response", "filter"
        format: "JSON" or "YAML"
        
        if type and/or format are not provided, tries to figure them out from the
        filename, which should be "*{TYPE}.{FORMAT}
        """
    
        if quiet:
            verbose = False
    
        if not type and not schema_file:
            type = ObsMetadata.get_information_file_type(filename)
    
        if verbose:
            print(f"instance = {filename}")
        
        instance = ObsMetadata.read_json_yaml_ref_local(filename, datapath, format=format)
        # instance = read_json_yaml(filename, format=format)
        
        base_file = (type if not schema_file else schema_file) + ".schema.json" 
            
        home = Path("").resolve()
        
        schema_file = PurePath(datapath).joinpath(base_file)
            
        base_uri = unquote(PurePath(schema_file).as_uri())
       
        print(f'in validate {base_uri}')
        with open(schema_file, "r") as f:
            try:
                schema = yamlref.loads(f.read(), base_uri=base_uri, jsonschema=True, 
                                       datapath=datapath, recursive=False)
                
            except json.decoder.JSONDecodeError as e:
                print(f"JSONDecodeError: Error loading JSON schema file: {schema_file}")
                print(str(e))
                return False
            except:
                print(f"Error loading JSON schema file: {schema_file}")
                print(sys.exc_info()[1])
                return False
               
        # Lazily report all errors in the instance
        # ASSUMES SCHEMA IS DRAFT-04 (I couldn't get it to work otherwise)
    
        try:
            
            if verbose:
                print(f"schema =   {schema_file.name}")
                print("\tTesting schema ...", end="")
             
            # Check schema first    
            jsonschema.Draft4Validator.check_schema(schema)
            
            if verbose:
                print("OK")
                print("\tTesting instance ...", end="")
    
            v = jsonschema.Draft4Validator(schema)
    
            if not v.is_valid(instance):
                print("")
                for error in sorted(v.iter_errors(instance), key=str):
                    print("\t\t", end="")
                    for elem in error.path:
                        print(f"['{elem}']", end="")
                    print(f": {error.message}")
                print("\tFAILED")
                return False
            else:
                if verbose:
                    print("OK")
                return True
        except jsonschema.ValidationError as e:
            print("\t" + e.message)
            return False
    
    
    def get_information_file_format(filename):
        """
        Determines if the information file is in JSON or YAML format
        
        Assumes that the filename is "*.{FORMAT}
        """
        suffix = PurePath(filename).suffix
        format = suffix[1:].upper()
        if format in VALID_FORMATS:
            return format
        print(f'Unknown format: {format}')
        sys.exit(1)
    
    
    def read_json_yaml(filename, format=None, debug=False):
        """ Reads a JSON or YAML file.  Does NOT use jsonReference """
        if not format: #validate format is legal. Otherwise program will exit
            format = ObsMetadata.get_information_file_format(filename)
    
        with open(filename, "r") as f:
            if format == "YAML":
                try:
                    element = yaml.safe_load(f)
                except:
                    print(f"Error loading YAML file: {filename}")
                    print(sys.exc_info()[1])
                    return
            else:
                try:
                    element = json.load(f)
                except JSONDecodeError as e:
                    print(f"JSONDecodeError: Error loading JSON file: {filename}")
                    print(str(e))
                    return
                except:
                    print(f"Error loading JSON file: {filename}")
                    print(sys.exc_info()[1])
                    return
    
        return element
    
    def read_json_yaml_ref(filename, datapath, format=None, debug=False):
        """ 
        Reads a JSON or YAML file using jsonReference 
        """
        
        if not format:
            format = ObsMetadata.get_information_file_format(filename)
    
        #home = Path("")
        #base_path = PurePath.joinpath(home,filename).resolve()
        #base_path = datapath.build_datapath(filename).resolve()
 
        bu = unquote(filename)
         
        if gitLabFile.isRemote(bu):
            base_uri = unquote(urlparse(bu).path)
            loader = JsonLoader()
            jsonstr = loader.get_remote_json(bu, base_uri=base_uri, datapath=datapath)
            return yamlref.loads(jsonstr, base_uri=base_uri, datapath=datapath)
        else:
            base_uri = Path(bu).as_uri()
            with open(unquote(filename), "r") as f:
                return yamlref.load(f, base_uri=base_uri, datapath=datapath)
            
    def read_json_yaml_ref_local(filename, format=None, debug=False):
        """ 
        Reads a JSON or YAML file using jsonReference
        Like read_json_yaml_ref, but does not look for files in OBSINFO_DATAPATH 
        """
        if not format:
            format = ObsMetadata.get_information_file_format(filename)
    
        home = Path("")
        base_path = PurePath.joinpath(home.resolve(),filename)
        base_uri = base_path.as_uri()
        #base_uri = f"file:{base_path}/"
        # print(f'read_json_yaml_ref: base_uri={base_uri}')
        with open(filename, "r") as f:
            return yamlref.load(f, base_uri=base_uri)
    

    
    @staticmethod
    def read_info_file(filename, datapath, format=None):
        """
        Reads an information file
        """

        dict = ObsMetadata.read_json_yaml_ref(filename, datapath, format)
        # Create an ObsMedatada object, which is a dir with some added methods
        return ObsMetadata(dict)
                
    def _validate_script(argv=None):
        """
        Validate an obsinfo information file
    
        Validates a file named *.{TYPE}.json or *.{TYPE}.yaml against the 
        obsinfo schema.{TYPE}.json file.
    
        {TYPE} can be campaign, network, instrumentation, instrument_components or
        response
        """
        from argparse import ArgumentParser
    
        parser = ArgumentParser(prog="obsinfo-validate", description=__doc__)
        parser.add_argument("info_file", help="Information file")
        parser.add_argument(
            "-t", "--type", choices=VALID_TYPES, default=None,
            help="Forces information file type (overrides interpreting from filename)",
        )
        parser.add_argument(
            "-f", "--format", choices=VALID_FORMATS, default=None,
            help="Forces information file format (overrides interpreting from filename)",
        )
        parser.add_argument(
            "-s", "--schema", default=None,
            help="Schema file (overrides interpreting from filename)",
        )
        parser.add_argument(
            "-v", "--verbose", action="store_true", help="increase output verbosity"
        )
        args = parser.parse_args()
    
        validate(args.info_file, format=args.format, type=args.type,
                schema_file=args.schema, verbose=args.verbose)
        
    
    def get_configured_element(self, key, channel_modification={}, selected_configuration={}, default=None): 
        """
        First converts any possible dictionary into an ObsMetadata object to be able to use
        this method recursively
        Returns the value corresponding to key in the following way:
        a) If key present in channel_modification, return the corresponding value
        b) Else if key present in selected_configuration, return the corresponding value
        c) Else if not and key present in self, return the corresponding value (this means config overrides info_dict(
        d) Else if key not present in either, return default 
        """
        
        value = self.get(key, default) #If no original value, use default step (c)

        # Use selected_configuration if present, else use original_value (which may be default) (a) and (b)
        # if here is for validation only
        if isinstance(selected_configuration, (dict, ObsMetadata)):
            value = selected_configuration.get(key, value)
        # Use channel_modification if present, else use original_value (which may be default) (a) and (b)
        # Cchannel modifications override selected configurations which override self which overrides default
        # but ONLY at the lowest (leaf) level, so we check whethere the value is a dictionary. If so, it won't be
        # substituted. This does not happen with configurations as they are complete substitutions of things such as
        # response stages or sample rates    
        if isinstance(channel_modification, (dict, ObsMetadata)):
            val = channel_modification.get(key, value)
            # Do not assign value if this is a dictionary, so it's not a leaf in the hierarchy
            if not isinstance(val, (dict, ObsMetadata)):
               value = val 

        if isinstance(value, dict): #Convert to ObsMetadata any dictionaries
            value = ObsMetadata(value)
            
        return value   
    
    def validate_dates(dates):
        
        if dates == None or not isinstance(dates, list):
            return []
        
        return [ObsMetadata.validate_date(dt) for dt in dates]
       
    def validate_date(date):
        
        if date == None or date == 0: #This is sometimes the default, the epoch date, 1/1/1970
            return 0
         
        regexp_date_UTC = re.compile("^[0-9]{4}[\-\/][0-9]{1,2}[\-\/]{1,2}")
        regexp_date_and_time_UTC = re.compile("^[0-9]{4}[\-\/][0-9]{1,2}[\-\/]{1,2}T[0-2][0-9]:[0-6][0-9]:[0-2]{0,1}[0-9]{0,1}Z{0.1}\.{0,1]0*")
        if re.match(regexp_date_UTC, date) or re.match(regexp_date_and_time_UTC, date): # Year starts string, everything OK
            return date
        else: #Assume it's a regular date
            warnings.warn(f'Date {date} is not UTC format, assuming regular dd/mm/yyyy format')
            regexp_date_normal = re.compile("[\-\/]")
            date_elements = re.split(regexp_date_normal, date)
            if len(date_elements) != 3:
                raise ValueError("Unrecognizable date, must either be UTC or dd/mm/yyyy or dd/mm/yy. Dashes can be used as separators")
            if len(date_elements[2]) == 2:
                date_elements[2] = "20" + date_elements[2] # Assume 21st century
                warnings.warn(f'Date {date} is two digits, assuming 21st century')
    
            return date_elements [2] + "-" + date_elements [1] + "-" + date_elements [0]
            
            
            
            
            
            