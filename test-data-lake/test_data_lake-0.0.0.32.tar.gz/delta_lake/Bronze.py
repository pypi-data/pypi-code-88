from delta_lake.DataLake import DataLake
from delta.tables import DeltaTable


class Bronze(DataLake):
    """
    delta lake Bronze class
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
        self.storage_bronze = storage_bronze
        super().__init__(spark, storage_account_name, storage_account_access_key, storage_landing, storage_bronze,
                         storage_silver, input_data_param, mount_data_param, colums_validate_merge_param, new_name,
                         database, target, origin)
        self.initialize_variables()

    def merge(self):
        """
        method that creates the initial load of the table or that creates the merge for the landing step to bronze
        """
        try:
            if self.table_exist:
                deltaTable = DeltaTable.forPath(self.spark, self.mount_data)
                deltaTable.alias(self.target) \
                    .merge(self.events.alias(self.origin), self.string_validate_columns) \
                    .whenMatchedUpdateAll() \
                    .whenNotMatchedInsertAll() \
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
        :return: input_data (source), mount_data (target) and colums_validate_merge (source.id=target.id)
        """
        self.input_data = "{0}{1}".format(self.storage_landing, self.input_data_param)
        self.mount_data = "{0}{1}".format(self.storage_bronze, self.mount_data_param)
        self.colums_validate_merge = self.colums_validate_merge_param.split(',')

    def load_data(self, input_data):
        """
        method that loads parquet files
        :param input_data: path in the data lake of the file to load
        :return: the object with the file data in events
        """
        self.events = self.spark.read.parquet(input_data)

    def create_json_columns_pass(self):
        pass
