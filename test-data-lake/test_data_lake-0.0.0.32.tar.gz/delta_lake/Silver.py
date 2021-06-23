from delta_lake.DataLake import DataLake
from delta.tables import DeltaTable
import json


class Silver(DataLake):
    """
    delta lake Silver class
    """
    def __init__(self, spark, storage_account_name, storage_account_access_key, storage_landing, storage_bronze,
                 storage_silver, input_data_param, mount_data_param, colums_validate_merge_param, new_name, database,
                 target, origin, colums_silver):
        """

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
        :param colums_silver: columns to lead to silver
        """
        self.colums_silver = colums_silver
        super().__init__(spark, storage_account_name, storage_account_access_key, storage_landing, storage_bronze,
                         storage_silver, input_data_param, mount_data_param, colums_validate_merge_param, new_name,
                         database, target, origin)
        self.initialize_variables()

    def merge(self):
        """
        method that creates the initial load of the table or that creates the merge for the bronze step to silver
        """
        try:
            if self.table_exist:
                deltaTable = DeltaTable.forPath(self.spark, self.mount_data)
                deltaTable.alias(self.target) \
                    .merge(self.events.alias(self.origin), self.string_validate_columns) \
                    .whenMatchedUpdate(set=self.json_load_insert_values) \
                    .whenNotMatchedInsert(values=self.json_load_insert_values) \
                    .execute()
                deltaTable.vacuum()
            else:
                self.events.write.format("delta").save(self.mount_data)
                self.spark.sql("CREATE TABLE IF NOT EXISTS {0}.{1} USING DELTA LOCATION '{2}'".format(self.database,
                                                                                                      self.table_name,
                                                                                                      self.mount_data))
        except Exception as e:
            print("Error update or create table: " + self.table_name + " explain: " + str(e))

    def initialize_variables(self):
        """
        method that initializes variables to merge from source to destination
        :return: input_data (source), mount_data (target), colums_validate_merge (source.id=target.id) and
        colums_silver_array (Id, Name,....)
        """
        self.input_data = "{0}{1}".format(self.storage_bronze, self.mount_data_param)
        self.mount_data = "{0}{1}".format(self.storage_silver, self.mount_data_param)
        self.colums_validate_merge = self.colums_validate_merge_param.split(',')
        self.colums_silver_array = self.colums_silver.split(',')

    def load_data(self, input_data):
        """
        method that loads parquet files
        :param input_data: path in the data lake of the file to load
        :return: the object with the file data in events
        """
        self.events = self.spark.read.format("delta").load("{0}".format(input_data))

    def create_json_columns_pass(self):
        """
        method returns json with columns to pass from source to destination
        :return: json with the columns to pass silver in json_load_insert_values
        """
        insert_values = "{"
        for item in self.colums_silver_array:
            if item is not "":
                insert_values = "{0}{1}".format(insert_values, '"{0}":"{1}.{0}", '.format(item, self.origin))

        insert_values = insert_values[0: len(insert_values) - 2] + '}'

        self.json_load_insert_values = json.loads(insert_values)
        print(self.json_load_insert_values)