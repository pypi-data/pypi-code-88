from abc import ABC, abstractmethod
from pyspark.sql.functions import *
import json


class DataLake(ABC):
    """
    base class, contains generic methods
    """
    events = None
    string_validate_columns = ""
    input_data = ""
    mount_data = ""
    json_load_insert_values = {}
    colums_validate_merge = []
    colums_silver_array = []

    def __init__(self, spark, storage_account_name, storage_account_access_key, storage_landing, storage_bronze,
                 storage_silver, input_data_param, mount_data_param, colums_validate_merge_param, new_name, database, target, origin):
        """
        set object variables
        :param spark: spark instance
        :param storage_account_name: storage account azure
        :param storage_account_access_key: storage access key azure
        :param storage_landing: storage account landing
        :param storage_bronze: storage account bronze
        :param storage_silver: storage account silver
        :param input_data_param: path and filename in the source data lake
        :param mount_data_param: path and filename in the destination data lake
        :param colums_validate_merge_param: columns representing single record separated by comma (Id,)
        :param new_name: new table name in destination
        :param database: source database
        :param target: information destination
        :param origin: origin of the information
        """
        self.spark = spark
        self.storage_account_name=storage_account_name
        self.storage_account_access_key=storage_account_access_key
        self.storage_landing = storage_landing
        self.storage_bronze = storage_bronze
        self.storage_silver = storage_silver
        self.input_data_param = input_data_param
        self.mount_data_param = mount_data_param
        self.colums_validate_merge_param = colums_validate_merge_param
        self.new_name = new_name
        self.table_name = new_name
        self.table_exist = False
        self.database = database
        self.target = target
        self.origin = origin

    abstractmethod
    def merge(self):
        pass

    abstractmethod
    def initialize_variables(self):
        pass

    abstractmethod
    def load_data(self):
        pass

    def initialize_config_storage(self):
        """
        connection with the data lake is created
        :return: connected object
        """
        self.spark.conf.set(
            "fs.azure.account.key." + self.storage_account_name + ".blob.core.windows.net",
            self.storage_account_access_key)

    def validate_tables(self):
        """
        it is validated if a table exists in the database
        :return: True if the table exists or False if it doesn't exist in table_exist
        """
        list_tables = self.spark.catalog.listTables(self.database)
        self.table_exist = False
        for item in list_tables:
            print(item)
            print(type(item))
            print(item.name)
            self.table_exist = item.name.lower() == self.table_name.lower()
            if self.table_exist:
                break

    def load_data_csv(self, input_data):
        """
        method that loads csv files
        :param input_data: path in the data lake of the file to load
        :return: the object with the file data in events
        """
        self.events = self.spark.read.format("csv").option("header", "true").load(input_data)

    def create_colums_merge(self):
        """
        method creates the condition to perform the merge with an array of fields containing the registry keys
        :return: condition to perform the merge in string_validate_columns
        """
        self.string_validate_columns = ""
        string_and = "and"
        for item in self.colums_validate_merge:
            condition = "{0}.{2} = {1}.{2}".format(self.origin, self.target, item)
            if item is not "":
                if self.string_validate_columns is "":
                    self.string_validate_columns = condition
                else:
                    self.string_validate_columns = "{0} {1} {2}".format(self.string_validate_columns, string_and, condition)
        print(self.string_validate_columns)

    def create_json_columns_pass(self):
        """
        method that creates json with the columns to pass to the next zone
        :return: json with columns to pass in json_load_insert_values
        """
        insert_values = "{"
        for item in self.colums_silver_array:
            if item is not "":
                insert_values = "{0}{1}".format(insert_values, '"{0}":"{1}.{0}", '.format(item, self.origin))

        insert_values = insert_values[0: len(insert_values) - 2] + '}'

        self.json_load_insert_values = json.loads(insert_values)
        print(self.json_load_insert_values)

    abstractmethod
    def create_json_columns_pass(self):
        pass