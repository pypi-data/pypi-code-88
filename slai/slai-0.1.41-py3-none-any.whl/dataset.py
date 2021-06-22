import json
import subprocess
import os


class DataSet:
    def __init__(self, model, model_version):
        self.model_name = model["name"]
        self.model_id = model["id"]
        self.model_version = model_version
        self.s3_prefix = f"{self.model_name}/{self.model_version}/"

    def add_file(self, path, dir=None):
        pass

    def add_files(self, files, dir=None):
        pass

    def add_directory(self, path):
        pass

    def ls(self):
        pass

    def local_path(self):
        """
        Return the local path to the dataset
        """
        pass

    def changes(self):
        """
        Return local changes to dataset, to be used before calling
        """

    def save(self):
        """
        Back up dataset to s3
        """
