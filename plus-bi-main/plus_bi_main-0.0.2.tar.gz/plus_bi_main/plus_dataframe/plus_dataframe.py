from typing import Type
from numpy import isin
import ast
import pandas as pd
import logging
from helper import plus_helper
from datetime import datetime, date
from pandas.core.base import DataError

class PlusDataFrame():
    def __init__(self, df, raw=False):
        self.df = df
        if raw:
            self.is_raw = True
            self.headers_cleaned = False
            self.headers_renamed = False
            self.default_values_applied = False
            self.unwanted_columns_removed = False
            self.empty_records_removed = False

            self.unwanted_columns=[]
            self.empty_records_columns=[]
            self.header_rename_dict={} 
            self.default_values_dict={}
            self.datatypes_dict={}
        else:
            self.is_raw = False                   
    
    @plus_helper.measure_runtime
    def clean_header_names(self):        
        self.df.columns = self.df.columns.str.replace('%', '')            
        self.df.columns = self.df.columns.str.replace(' ', '')            
        self.df.columns = self.df.columns.str.replace('/', '')            
        self.df.columns = self.df.columns.str.replace('\n', '')            
        self.df.columns = self.df.columns.str.replace('\u00eb', 'e')            
        self.df.columns = self.df.columns.str.replace('\u00e9', 'e')            
        self.df.columns = self.df.columns.str.replace('-', '')            
        self.df.columns = self.df.columns.str.replace('.', '')            
        self.df.columns = self.df.columns.str.replace('_', '')
 

    @plus_helper.measure_runtime
    def remove_unwanted_columns(self):
        if not isinstance(self.unwanted_columns, (list, str)):
            logging.info('Variable "unwanted_columns" is expected to be of type list or string')
            raise TypeError(f'"columns" variable is of type {type(self.unwanted_columns)}, should be of type list or string.')

        #expecting a list or string in the environment variable
        #columns = os.environ['plus_bi_columns_to_be_removed'].split(';')        
        for col in self.unwanted_columns:
            try:
                self.df.drop(col, axis=1, inplace=True)
            except Exception as e:
                logging.info(f'Exception raised: {e}')    

    @plus_helper.measure_runtime
    def remove_empty_records(self):
        #Removal of values should be performed on preferably the Primary Key of the dataset, this can be 1 or many columns.
        
        if not isinstance(self.empty_records_columns, (list, str)):
            logging.info('Variable "columns" is expected to be of type list or string')
            raise TypeError(f'"columns" variable is of type {type(self.empty_records_columns)}, should be of type list or string.')
        
        #expecting a list or string in the environment variable
        #columns = ast.literal_eval(os.environ["plus_bi_excel_column_for_empty_record_removal"])
        #The value(s) should be the original headername(s).

        try:
            if isinstance(self.empty_records_columns, str):
                self.df.dropna(subset=[self.empty_records_columns], inplace=True)
            else:
                self.df.dropna(subset=self.empty_records_columns, inplace=True)
        except Exception as e:
            logging.info(f'Column with name {self.empty_records_columns} not found; not filtering on empty records.\nError message: {e}')

    @plus_helper.measure_runtime
    def rename_headers(self):
        #Expected dict-format: {Old-name : New-name} ie. {wnknr : Winkelnummer}
        if not isinstance(self.header_rename_dict, dict):     
            raise TypeError(f'Type of variable "header_dict" should be of type dict. Provided type: {type(self.header_rename_dict)}.')
        
        #expecting a dict in the environment variable
        #header_dict = ast.literal_eval(os.environ["plus_bi_excel_new_header_names"])

        #first we check if all columns are present.
        for expected_column, v in self.header_rename_dict.items():
            try:
                if not expected_column in self.df.columns:                
                    raise AssertionError(f"Did not find column: {expected_column}")
            except Exception as e:
                    logging.error(f'Exception raised: {e}')

        logging.info('All columns present, renaming them.')
        self.df.rename(columns=self.header_rename_dict, inplace=True)

    def add_default_values(self):
        #Expected dict-format: {New-column-name : default_value} ie. {Winkelnummer : 0}
        #You can also add columns that do not exist yet, for example MessageVersion for non-POS dataflows.
        if not isinstance(self.default_values_dict, dict):     
            raise TypeError(f'Type of variable "default_values_dict" should be of type dict. Provided type: {type(self.default_values_dict)}.')

        #expecting a dict in the environment variable with the following format:
        #var_dict = var_dict = {'Date' : 'datetime.date.today()', 'DateTime' : 'datetime.datetime.now()' , 'Integer' : '0', 'Float' : '0.0', 'String' : 'Something'}
        #!!NOTE: for date(time) use the functions used in the example.
        try:            
            for attr, default_value in self.default_values_dict.items():
                try:
                    #first we check if the string can be evaluated as another Class 
                    try:
                        self.df[attr].fillna(ast.literal_eval(default_value), inplace=True)
                    except KeyError:
                        self.df[attr] = ast.literal_eval(default_value)
                    self.df[attr] = self.df[attr].astype(type(ast.literal_eval(default_value)))
                except Exception as e:
                    try:
                        #next we check if the default is a function
                        try:
                            self.df[attr].fillna(eval(default_value), inplace=True)
                        except KeyError:
                            self.df[attr] = eval(default_value)
                        self.df[attr] = self.df[attr].astype(eval(default_value))
                    except Exception as e:
                        #last we type it from the value itself (mainly str)
                        try:
                            self.df[attr].fillna(default_value, inplace=True)
                        except KeyError:
                            self.df[attr] = default_value
                        self.df[attr] = self.df[attr].astype(default_value)
        except Exception as e:
            logging.error(f'Unable to apply default value: {e}') 

    def set_datatypes(self):
        #Expected dict-format: {New-column-name : datatype} ie. {Winkelnummer : 'int'}
        #NOTE: ALL columns should be included in this dict.
        if not isinstance(self.datatypes_dict, dict):     
            raise TypeError(f'Type of variable "datatypes_dict" should be of type dict. Provided type: {type(self.datatypes_dict)}.')

        #expecting a dict in the environment variable with the following format:
        #var_dict = var_dict = {'CreatieDatum' : 'date' , 'BonDatumTijd' : 'datetime', 'Bedrag' : 'float', 'Aantal' : 'int', 'Omschrijving' : 'str'}
        try:            
            self.df = self.df.astype(self.datatypes_dict)
        except Exception as e:
            logging.error(f'Something went wrong datatyping the dataframe.\nError: {e}') 
            raise RuntimeError("Couldn't datatype the dataframe, see previous errors...")

    @plus_helper.measure_runtime
    def clean_raw_dataframe(self):
        try:
            if self.is_raw:
                if not self.headers_cleaned:
                    self.clean_header_names()
                    self.headers_cleaned = True
                
                if not self.unwanted_columns_removed:
                    if len(self.unwanted_columns) > 0:
                        self.remove_unwanted_columns()
                    self.unwanted_columns_removed = True                

                if not self.empty_records_removed:
                    if len(self.empty_records_columns) > 0:
                        self.remove_empty_records()
                    self.empty_records_removed = True
                
                if not self.headers_renamed:
                    if len(self.header_rename_dict) > 0:
                        self.rename_headers()
                    self.headers_renamed = True

                if not self.default_values_applied:
                    if len(self.default_values_dict) > 0:
                        self.add_default_values()
                    self.default_values_applied = True
                
                if not self.datatyped:
                    if len(self.datatypes_dict) > 0:
                        self.set_datatypes()
                        self.datatyped = True
                    else:
                        raise DataError(f'No key-value pairs in Datatype dict detected.')
                logging.info('All cleaning operations successful, dataframe is clean.')
                self.is_raw = False
            else:
                logging.info('Dataframe is already cleaned.')

        except Exception as ex:
            logging.error(f'Something went wrong while cleaning the dataframe.')
            logging.error(f'Error message: {ex}')
            raise RuntimeError(f'Error during cleaning of dataframe, see previous errors...')

        
        


