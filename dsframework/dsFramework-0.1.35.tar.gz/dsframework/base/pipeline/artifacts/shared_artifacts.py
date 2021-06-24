#!/usr/bin/env python
# coding: utf-8

from typing import List, Any
import os
import json
import csv
import pickle
from dsframework.base.common import functions

class ZIDS_SharedArtifacts():

    def __init__(self) -> None:
        self.base_dir = os.path.dirname(os.getcwd())
        self.load_config_json()
        self.load_vocabs()
        self.load_artifacts()

    def load_config_json(self):
        if os.path.exists('config.json'):
            data = functions.load_json('config.json')
            for item in data:
                setattr(self, item, data[item])

    def load_vocabs(self):
        if hasattr(self, 'vocabs'):
            for item in self.vocabs:
                self.load_file(item)

    def load_artifacts(self):
        if hasattr(self, 'artifacts'):
            for item in self.artifacts:
                self.load_file(item)

    def load_file(self, item):
        file_type = item['type']
        path = item['path']
        name = item['name']
        if path:
            absolute_path = self.base_dir + '/' + path
            if file_type == 'json':
                self.load_json(absolute_path, name)
            elif file_type == 'csv':
                self.load_csv(absolute_path, name)
            elif file_type == 'pickle':
                self.load_csv(absolute_path, name)

    def load_json(self, path, name):
        with open(path) as json_file:
            setattr(self, name, json.load(json_file))

    def load_csv(self, path, name):
        with open(path) as csv_file:
            setattr(self, name, functions.flatten_list(list(csv.reader(csv_file))))

    def load_pickle(self, path, name):
        with open(path, 'rb') as pickle_file:
            setattr(self, name, pickle.load(pickle_file))

    def get(self, key, default=None):
        if key in self.__dict__:
            return self.__dict__[key]
        return default
