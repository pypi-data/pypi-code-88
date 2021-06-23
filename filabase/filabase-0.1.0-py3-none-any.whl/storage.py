import json
import pathlib
import os


class Storage(object):
    """
        Storage
    """
    def __init__(self, db_path):
        super(Storage, self).__init__()
        self.db_path = pathlib.Path(db_path).expanduser()

    def persist(self, record_type, records):
        """
            Writes a representation of the records in a designated file for
            record_type.
            Creates the persistance directory if it does not exist.

            parameters:
            record_type - a string description of the records which need to
                be persisted. Please follow file naming convention of your OS.
            records - a list of dictionaries
        """
        if not self.db_exists():
            self.init_datadir()
        datafile = self.compose_datapath(record_type)
        data = self.serialize(records)
        return self.write_data(datafile, data)

    def write_data(self, datafile, data):
        with open(datafile, 'a+') as handle:
            return handle.write(data)

    def db_exists(self):
        """checks if the persistence directory exists"""
        return self.db_path.exists()

    def compose_datapath(self, record_type):
        """docstring for compose_datapath"""
        return self.db_path.joinpath(record_type)

    def db_file_exists(self, record_type):
        return self.compose_datapath(record_type).exists()

    def init_datadir(self):
        """creates a new persistence directory"""
        return self.db_path.mkdir()

    def extract(self, record_type):
        """
            Given the type of records requested, reads all the records of the
            type and returns a list of dictionaries.

            record_type - String identifier of the type
            returns list of dictionaries from the record_type persistence file
        """
        if self.db_file_exists(record_type):
            return self.deserialize(self.read_datafile(record_type))
        else:
            return []

    def delete_data(self, record_type, filter_by=None):
        """
            removes all records of type record_type that match the conditions
            in the filter_by dictionary
        """
        records = self.extract(record_type)
        for key, value in filter_by.items():
            records = list(
                        filter(lambda record: record[key] != value, records))
        self.persist(record_type, records)

    def read_datafile(self, record_type):
        datafile = self.compose_datapath(record_type)
        records = []
        with open(datafile, 'r') as handle:
            for record in handle:
                records.append(record)
        return records

    def deserialize(self, records):
        """
            converts json-like strings to dictionaries.
            Returns a list containing the result.
        """
        dictionaries = []
        for record in records:
            dictionaries.append(json.loads(record))
        return dictionaries

    def serialize(self, records):
        """
            turns records into a string, ready for writing into a text file
        """
        serialized = []
        for record in records:
            serialized.append(json.dumps(record))
        return os.linesep.join(serialized) + os.linesep
