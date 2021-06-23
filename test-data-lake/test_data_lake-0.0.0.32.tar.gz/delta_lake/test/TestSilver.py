import pytest
import json
from delta_lake import const
from delta_lake.Util import Util
from delta_lake.Silver import Silver


class TestSilver:

    def __init__(self, spark, storage_account_name, storage_account_access_key, storage_landing, storage_bronze,
                 storage_silver, input_data_param_v1, input_data_param_v2, input_data_param_v3, mount_data_param, colums_validate_merge_param, new_name, database,
                 target, origin, colum_filter, value_filter, colum_validate_data, value_validate_data,
                 number_items_valide_v1, number_items_valide_v2, colums_silver):
        """
        set object variables
        :param spark:
        :param storage_account_name: storage account azure
        :param storage_account_access_key: storage access key azure
        :param storage_landing: storage account landing
        :param storage_bronze: storage account bronze
        :param storage_silver: storage account silver
        :param input_data_param_v1: path and filename in the source data lake v1
        :param input_data_param_v2: path and filename in the source data lake v2
        :param input_data_param_v3: path and filename in the source data lake v3
        :param mount_data_param: path and filename in the destination data lake
        :param colums_validate_merge_param: columns representing single record separated by comma (Id,)
        :param new_name: new table name in destination
        :param database: source database
        :param target: information destination
        :param origin: origin of the information
        :param colum_filter:
        :param value_filter:
        :param colum_validate_data:
        :param value_validate_data:
        :param number_items_valide_v1:
        :param number_items_valide_v2:
        :param colums_silver:
        """
        self.spark = spark
        self.util = Util()
        self.colum_filter = colum_filter
        self.value_filter = value_filter
        self.colum_validate_data = colum_validate_data
        self.value_validate_data = value_validate_data
        self.number_items_valide_v1 = number_items_valide_v1
        self.number_items_valide_v2 = number_items_valide_v2
        self.delta_lake_v1 = Silver(self.spark, storage_account_name, storage_account_access_key, storage_landing,
                                    storage_bronze, storage_silver, input_data_param_v1, mount_data_param,
                                    colums_validate_merge_param, new_name, database, target, origin, colums_silver)
        self.delta_lake_v2 = Silver(self.spark, storage_account_name, storage_account_access_key, storage_landing,
                                    storage_bronze, storage_silver, input_data_param_v2, mount_data_param,
                                    colums_validate_merge_param, new_name, database, target, origin, colums_silver)
        self.delta_lake_v3 = Silver(self.spark, storage_account_name, storage_account_access_key, storage_landing,
                                    storage_bronze, storage_silver, input_data_param_v3, mount_data_param,
                                    colums_validate_merge_param, new_name, database, target, origin, colums_silver)

    def load_data_v1(self):
        """
        the process of taking the data from bronze to silver is carried out
        :return: validation of matching items
        """
        self.delta_lake_v1.initialize_config_storage()
        self.delta_lake_v1.validate_tables()
        self.delta_lake_v1.create_colums_merge()
        self.delta_lake_v1.create_json_columns_pass()
        self.delta_lake_v1.load_data(self.delta_lake_v1.input_data)
        self.delta_lake_v1.merge()
        df = self.delta_lake_v1.spark.sql("select * from {0}.{1}".format(self.delta_lake_v1.database,
                                                                         self.delta_lake_v1.table_name))
        assert df.count() == self.number_items_valide_v1

    def load_data_v2(self):
        """
        the process of taking the data from bronze to silver is carried out
        :return: validation of matching items
        """
        self.delta_lake_v2.initialize_config_storage()
        self.delta_lake_v2.validate_tables()
        self.delta_lake_v2.create_colums_merge()
        self.delta_lake_v2.create_json_columns_pass()
        self.delta_lake_v2.load_data(self.delta_lake_v2.input_data)
        self.delta_lake_v2.merge()

        df = self.delta_lake_v2.spark.sql("select * from {0}.{1}".format(self.delta_lake_v2.database,
                                                                         self.delta_lake_v2.table_name))
        assert df.count() == self.number_items_valide_v2

    def load_data_v3(self):
        """
        The process of taking the data from landing to bronze is carried out and information is changed to a
        record and this is validated if it was updated correctly
        :return: validation of matching items
        """
        self.delta_lake_v3.initialize_config_storage()
        self.delta_lake_v3.validate_tables()
        self.delta_lake_v3.create_colums_merge()
        self.delta_lake_v3.create_json_columns_pass()
        self.delta_lake_v3.load_data(self.delta_lake_v3.input_data)
        self.delta_lake_v3.merge()
        df = self.delta_lake_v3.spark.sql("select {0} From {1}.{2} where {3}={4}".format(self.colum_validate_data,
                                                                                         self.delta_lake_v3.database,
                                                                                         self.delta_lake_v3.table_name,
                                                                                         self.colum_filter,
                                                                                         self.value_filter))
        value = df.collect()
        assert value[0][self.colum_validate_data] == self.value_validate_data

    def restart_enviroment(self):
        """
        the objects created in the data lake and database are deleted
        """
        self.delta_lake_v1.spark.sql("DROP TABLE {0}.{1}".format(self.delta_lake_v1.database,
                                                                 self.delta_lake_v1.table_name))
        list_file = self.util.list_folder_delta_lake(self.delta_lake_v1.mount_data)
        for item in list_file:
            self.util.delete_file_delta_lake(item.path)

    def test_create_json_columns_pass(self):
        """
        method to validate the creation of the json with the columns to pass
        """
        self.delta_lake.create_json_columns_pass()
        assert self.delta_lake.json_load_insert_values == json.loads(const.json_colum_test)
