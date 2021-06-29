# Copyright 2021 Element Analytics, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
from unify.sources import Sources
from unify.sources import Sources
import json
import os
import uuid
from tests import *
import os
from tempfile import mkstemp
from unify.generalutils import csv_to_json
from unify.WaitingLibrary import Wait


class TestSources(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sources = Sources(cluster_name, props)
        cls.dataset_name = 'test-{}'.format(str(uuid.uuid4()))
        result = cls.sources.create_api_data_set_with_content(
            name=cls.dataset_name,
            org_id=test_org,
            content='c1,c2\nf1,f2'
        )
        cls.dataset_id = result['data_set_id']

    def test_label(self):
        labels = ['python sdk test']
        raised = False
        try:
            self.sources.label(test_org, self.dataset_id, labels)
        except:
            raised = True
        self.assertFalse(raised, 'Exception raised in label dataset')

    def test_overwrite(self):
        file_dir, path = mkstemp(suffix=".csv")

        new_cont = 'c1,c2\nf3,f4'

        open(path, "w+").write(new_cont)

        response = self.sources.overwrite_dataset(
            org_id=test_org,
            data_set_id=self.dataset_id,
            file_path=path
        )
        os.close(file_dir)
        self.assertTrue("truncate" in response and "append" in response)

    def test_upload_big_dataset(self):

        new_cont = 'c1,c2\nf3,f4\nf5,f6'

        response = self.sources.upload_big_dataset(
            org_id=test_org,
            name="big_dataset",
            content=new_cont
        )

        self.assertTrue("create" in response and "append" in response)

    def test_create_api_data_set(self):

        new_cont = 'c1,c2\nf3,f4\nf5,f6'

        file_dir, path = mkstemp(suffix=".csv")

        open(path, "w+").write(new_cont)

        response = self.sources.create_api_data_set(
            org_id=test_org,
            file_path=path,
            name="api_dataset"
        )

        self.assertTrue(
            "group_id" in response and
            "data_set_id" in response and
            "commit_id" in response
        )
        os.close(file_dir)

    def test_create_api_data_set_with_content(self):

        new_cont = 'c1,c2\nf3,f4\nf5,f6'

        response = self.sources.create_api_data_set_with_content(
            org_id=test_org,
            content=new_cont,
            name="api_dataset"
        )

        self.assertTrue(
            "group_id" in response and
            "data_set_id" in response and
            "commit_id" in response
        )

    def test_download_dataset_content(self):

        new_cont = 'c1,c2\nf3,f4\nf5,f6'

        file_dir, path = mkstemp(suffix=".csv")

        open(path, "w+").write(new_cont)

        response = self.sources.static_file_upload(
            org_id=test_org,
            content=path,
            name="api_dataset"
        )

        content = self.sources.download_dataset_content(
            org_id=test_org,
            dataset_id=response["id"]
        )

        self.assertTrue(len(content) > 0)
        os.close(file_dir)
