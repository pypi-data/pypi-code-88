import sys
import pandas as pd

class DictionaryManager:
    """
    Custom Table Management module for Cassandra
    :param clsuter: Cassandra cluster
    """
    def __init__(self, cluster):
        print("Installing Cluster...")
        self.cluster = cluster
        self.list_tables = []
        self.tables_info = []
        self._acquire_table_names()
        self._acquire_table_info()
        print("Cluster Acquired !")
        
    def _acquire_table_names(self):
        list_tables = self.cluster.session.execute(f"SELECT * FROM system_schema.tables WHERE keyspace_name='{self.cluster.keyspace}'")
        self.list_tables = pd.DataFrame(list_tables.all())[['table_name']].table_name.values.tolist()
        
    def _acquire_table_info(self):
        self.tables_info = pd.DataFrame(self.cluster.session.execute(f"SELECT * FROM system_schema.columns WHERE keyspace_name='{self.cluster.keyspace}'").all())
        
    def get_table_info(self, table_name):
        return self.tables_info[self.tables_info.table_name == table_name]
        
    def check_column(self, column_name, table_name):
        r_info = pd.DataFrame(self.cluster.session.execute(f"SELECT * FROM system_schema.columns WHERE keyspace_name='{self.cluster.keyspace}' AND table_name='{table_name}'").all())
        return {
            'keyspace': self.cluster.keyspace,
            'table_name': table_name,
            'column_name': column_name,
            'is_present': r_info[r_info.column_name == column_name].shape[0]
        }

    def check_column_all(self, column_name):
        res = []
        for table_name in self.list_tables:
            current_r = self.check_column(column_name, table_name)
            res.append(current_r)
        return pd.DataFrame(res)
    
    def add_column(self, column_name, column_type, table_name):
        r_info = self.cluster.session.execute(f"ALTER TABLE {self.cluster.keyspace}.{table_name} ADD '{column_name}' '{column_type}'")
        return self.check_column(column_name, table_name)

    def add_column_all(self, column_name, column_type):
        res = []
        for table_name in self.list_tables:
            current_r = self.add_column(column_name, column_type, table_name)
            res.append(current_r)
        return pd.DataFrame(res)

    def drop_column(self, column_name, table_name):
        r_info = self.cluster.session.execute(f"ALTER TABLE {self.cluster.keyspace}.{table_name} DROP '{column_name}'")
        return self.check_column(column_name, table_name)

    def drop_column_all(self, column_name):
        res = []
        for table_name in self.list_tables:
            current_r = self.add_column(column_name, column_type, table_name)
            res.append(current_r)
        return pd.DataFrame(res)
