import pytest
import json
from delta_lake.DataLake import DataLake
from delta_lake.Util import Util
import delta_lake.const as const


class TestDataLake:
    """

    """
    def __init__(self, spark, storage_account_name, storage_account_access_key, storage_landing, storage_bronze,
                 storage_silver, input_data_param, mount_data_param, colums_validate_merge_param, new_name, database,
                 target, origin):
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
        self.delta_lake = DataLake(spark, storage_account_name, storage_account_access_key, storage_landing,
                                   storage_bronze, storage_silver, input_data_param, mount_data_param,
                                   colums_validate_merge_param, new_name, database, target, origin)
        self.delta_lake.colums_validate_merge = self.delta_lake.colums_validate_merge_param.split(',')
        self.util = Util()

    def test_initialize_config_storage(self):
        """
        method that validates the connection with the delta lake, lists the directories and validates that if it
        returns information
        """
        self.delta_lake.initialize_config_storage()
        list_folder = self.util.list_folder_delta_lake("{0}{1}".format(self.delta_lake.storage_landing, const.test))
        assert len(list_folder) != 0

    def test_validate_tables(self):
        """
        a test table is created it is validated that it exists
        """
        self.delta_lake.spark.sql("CREATE TABLE IF NOT EXISTS {0}.{1}".format(self.delta_lake.database,
                                                                              self.delta_lake.new_name))
        self.delta_lake.validate_tables()
        assert self.delta_lake.table_exist
        self.delta_lake.spark.sql("DROP TABLE {0}.{1}".format(self.delta_lake.database, self.delta_lake.new_name))

    def test_create_colums_merge(self):
        """
        the creation of the columns to validate in the merge is validated
        """
        self.delta_lake.create_colums_merge()
        assert self.delta_lake.string_validate_columns == "{0}.{2} = {1}.{2}".format(self.delta_lake.origin,
                                                                                     self.delta_lake.target,
                                                                                     self.delta_lake.new_name)

