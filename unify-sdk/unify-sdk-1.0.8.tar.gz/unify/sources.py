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

"""
Contains methods to interact with Unify datasets api
"""
import json
import time
import uuid
import os
from tempfile import mkstemp

from unify.properties import Properties, ClusterSetting
from .apirequestsmng import ApiRequestManager
from .generalutils import csv_to_json
from .generalutils import json_to_csv
from .generalutils import create_schema_dataset
from .generalutils import stream_iterable
from .WaitingLibrary import Wait


class Sources(ApiRequestManager):
    """
    Class to interact with dataset endpoints
    """

    def __init__(self, cluster=None, props=Properties(ClusterSetting.KEY_RING)):
        """
        Class constructor

        :param cluster: Hostname
        :type cluster: str
        :param props: Instantiated Properties class
        :type props: class:`unify.properties.Properties`
        """

        super().__init__(cluster=cluster, props=props)

        self.epoch_time = int(time.time())
        self.pi_tag_export_limit = {"piTagExportLimit": 999}
        self.expiry = {"expiry": 999}

        try:

            self.list_templates_uri = 'api/assetTemplates'
            self.upload_content_type_header = {"Content-Type": "multipart/form-data"}
            self.delete_content_type_header = {"Content-Type": "application/json"}

            self.epoch_time = int(time.time())
            self.sources_url = self.props.get_remote(self.cluster) + "io/v1/org/{}/sources"

            self.agents_url = self.props.get_remote(self.cluster) + "agents/v2/"

            self.piwebapi_test_url = self.agents_url + "piwebapi/org/{}/test"

            self.piwebapi_create_url = self.agents_url + \
                "piwebapi/org/{}/create?modeldata_only=true"

            self.piconfig_upload_url = self.agents_url + "piconfig/org/{}/model/?name=&serverName="

            self.piconfig_upload_url_no_params = self.agents_url + "piconfig/org/{}/model/"

            self.staticfile_upload_url = self.agents_url + "staticfile/org/{}/model"

            self.delete_source_url = self.sources_url + "/{}"

            self.delete_evergreening_source_url = self.agents_url + "piwebapi/org/{}/source/{}"

            self.stage_file_url = self.props.get_remote(self.cluster) + "datasets/v1/stage/file"

            self.post_data_set_schema_url = self.props.get_remote(
                self.cluster) + "datasets/v1/dataset"

            self.commit_data_set_url = self.props.get_remote(
                self.cluster) + "datasets/v1/dataset/{}/commit"

            self.labeling_sources = self.props.get_remote(
                self.cluster) + "datasets/v1/labeling"

            self.labeling_sources_2 = self.props.get_remote(
                self.cluster) + "datasets/v1/labeling/query"

            self.labeling_sources_facets_url = self.props.get_remote(
                self.cluster) + "datasets/v1/labeling/facets"

            self.append_url = self.props.get_remote(
                self.cluster) + "agents/v2/staticfile/org/{}/model/{}/append"

            self.download_dataset_url = self.props.get_remote(
                self.cluster) + "tags/org/{}/datasets/{}/download"

            self.get_commit = self.commit_data_set_url + "/{}"

        except Exception as error:
            raise error

    def get_status(self, org_id, dataset_id, commit_id):
        """
        Retrieves the status of the given commit id

        :param org_id: Org where the commit has occurred
        :type org_id: int or str
        :param dataset_id: Datasets id of whom the commit belongs to
        :type dataset_id: str
        :param commit_id: Commit id to be retrieved
        :type commit_id: str
        :return:
        """
        return self.get_commit_status(org_id=org_id, data_set_id=dataset_id, commit_id=commit_id)[0]

    def accert_status(self, org_id, dataset_id, commit_id, expected):
        """
        Accerts that the status of a given commit is what is expected

        :param org_id: Org where the commit has occurred
        :type org_id: int or str
        :param dataset_id: Dataset id of whom the commit belongs to
        :type dataset_id: str
        :param commit_id: Commit id to be retrieved
        :type commit_id: str
        :param expected: Expected status
        :type expected: str
        :return:
        """
        status = self.get_status(org_id=org_id, dataset_id=dataset_id, commit_id=commit_id)

        if "status" in status:

            tipe = status["status"]

            if "$type" in tipe:
                return expected in tipe["$type"]

        return False

    def is_commit_completed(self, org_id, dataset_id, commit_id):
        """
        Verifies that the status of the commit is completed

        :param org_id: Org where the commit has occurred
        :type org_id: int or str
        :param dataset_id: Dataset id of whom the commit belongs to
        :type dataset_id: str
        :param commit_id: Commit id to be asserted
        :type commit_id: str
        :return:
        """
        return self.accert_status(
            org_id=org_id,
            dataset_id=dataset_id,
            commit_id=commit_id,
            expected="Completed"
        )

    def upload_big_dataset(
            self, name, org_id, content, format="csv",
            convert_to_parquet="false", encoding='UTF-8',chunks=10000):
        """
        Upload a dataset through the static route. This method should be used when
        uploading a big file. It will split the file into
        smaller chunks and upload them sequentially.

        :param name: Dataset name to be cerated
        :type name: str
        :param org_id: Org where the dataset will be created
        :type org_id: int or str
        :param content: Dataset content
        :type content: str
        :param format: File format. Accepts "CSV" or "TSV"
        :type format: str, optional
        :param convert_to_parquet: Flag to convert file to parquet
        :type convert_to_parquet: bool, optional
        :param encoding: File encoding
        :type encoding: str, optional
        :param chunks: Number of chunks to split the file
        :type chunks: int
        :return:
        """

        data = content.encode(encoding)

        jdata = csv_to_json(data)

        first = True

        dataset_data = {
            "create": {},
            "append": []
        }
        for aux_file in stream_iterable(container=jdata, chunk=chunks):

            if first:

                first = False

                file_dir, path = mkstemp(suffix=".csv")

                open(path, "w+").write(json_to_csv(aux_file))

                dataset_data["create"] = self.create_api_data_set(
                    name=name,
                    org_id=org_id,
                    file_path=path,
                    format=format,
                    convert_to_parquet=convert_to_parquet,
                    encoding=encoding
                )

                Wait().until(
                    self.is_commit_completed,
                    "commit {} never completed".format(dataset_data["create"]["data_set_id"]),
                    org_id,
                    dataset_data["create"]["data_set_id"],
                    dataset_data["create"]["commit_id"]
                )

                os.close(file_dir)

            else:

                file_dir, path2 = mkstemp(suffix=".csv")

                open(path2, "wb").write(json_to_csv(aux_file).encode(encoding))

                try:
                    added_data = self.add_data_to_existing_source(
                        name="{} {}".format(name, str(uuid.uuid4())[:4]),
                        org_id=org_id,
                        data_set_id=dataset_data["create"]["data_set_id"],
                        file_path=path2,
                        group_id=dataset_data["create"]["group_id"]
                    )

                    Wait().until(
                        self.is_commit_completed,
                        "commit {} never completed".format(dataset_data["create"]["data_set_id"]),
                        org_id,
                        dataset_data["create"]["data_set_id"],
                        added_data["commit_id"]
                    )

                    dataset_data["append"].append(added_data)

                    os.close(file_dir)

                except Exception as err:
                    print(err)
                    open("fail_{} {}.csv".format(name, str(uuid.uuid4())[:4]), "wb").write(
                        json_to_csv(aux_file).encode("utf-8"))

        return dataset_data

    def create_api_data_set(
            self, name, org_id, file_path, format="csv",
            convert_to_parquet="false", encoding="UTF-8"):
        """
        Creates a dataset through the static file route.

        :param name: Name to of the new dataset
        :type name: str
        :param org_id: Org id where the dataset will be stored
        :type org_id: int or str
        :param file_path: Directory file path where the dataset contents are
        :type file_path: str
        :param format: File format. Accepts "CSV" or "TSV"
        :type format: str, optional
        :param convert_to_parquet: Flag to convert to parquet
        :type convert_to_parquet: bool, optional
        :param encoding: Source file encoding
        :type encoding: str, optional
        :return:
        """

        content = open(file_path, "r+").read()

        return self.create_api_data_set_with_content(
            name,
            org_id,
            content,
            format,
            convert_to_parquet,
            encoding
        )

    def create_api_data_set_with_content(
            self,
            name,
            org_id,
            content,
            format="csv",
            convert_to_parquet="false",
            encoding="UTF-8"):
        """
        Creates a dataset through the static file route.

        :param name: Name of the new dataset
        :type name: str
        :param org_id: Org id where the dataset will be stored
        :type org_id: int or str
        :param content: dataset content in csv or tsv format
        :type content: str
        :param format: Content format. Accepts "CSV" or "TSV"
        :type format: str, optional
        :param convert_to_parquet: Flag to convert to parquet
        :type convert_to_parquet: bool, optional
        :param encoding: Content encoding
        :type encoding: str, optional
        :return:
        """
        results = {}

        stage_result = self.stage_file_with_content(
            name=name,
            org_id=org_id,
            file_data=content,
            format=format,
            convert_to_parquet=convert_to_parquet,
            encoding=encoding
        )

        results["group_id"] = stage_result

        schema = create_schema_dataset(
            csv_data=content,
            name=name
        )
        initial_commit = self.post_file_schema(
            org_id=org_id,
            schema_data=json.dumps(schema),
        )

        results["data_set_id"] = initial_commit["id"]

        second_commit = self.append_command(
            org_id=org_id,
            data_set_id=results["data_set_id"],
            name=name,
            group_id=results["group_id"]
        )

        results.update(second_commit)

        return results

    def get_commit_status(self, org_id, data_set_id, commit_id):
        """
        Retrieves the status of the given commit id.

        :param org_id: Org id where the commit has occurred
        :type org_id: int or str
        :param dataset_id: Datasets id of whom the commit belongs to
        :type dataset_id: str
        :param commit_id: Commit id to be retrieved
        :type commit_id: str
        :return:
        """
        header = self.build_header(
            aut_token=self.props.get_auth_token(cluster=self.cluster),
            org_id=org_id,
            others={"'Content-Type'": "application/data"}
        )

        url = self.get_commit.format(data_set_id, commit_id)

        test_request = self.session.get(url, headers=header)

        return json.loads(test_request.content.decode('utf8')), test_request.status_code

    def download_dataset_content(self, org_id, dataset_id):
        """
        Downloads the content of a given dataset.

        :param org_id: Org id where the dataset exists
        :type org_id: int or str
        :param dataset_id: Dataset id to be retrieved
        :type dataset_id: str
        :return:
        """
        header = self.build_header(
            aut_token=self.props.get_auth_token(cluster=self.cluster),
            org_id=org_id
        )

        get_source_request = self.session.get(
            self.download_dataset_url.format(org_id, dataset_id),
            headers=header
        )

        if get_source_request.status_code == 200:
            return get_source_request.content

        raise Exception(repr(get_source_request.content))

    def create_export_dataset(self, org_id, dataset_ids):
        """
        Create the content needed to export a dataset.
        This is usually used when using the import dataset.

        :param org_id: Org id where the dataset exists
        :type org_id: int or str
        :param dataset_ids: List containing the dataset ids
        :type dataset_ids: list of str
        :return:
        """
        datasets = self.get_sources(org_id=org_id)

        id_to_type = {}

        for dataset in datasets:
            id_to_type[dataset["id"]] = dataset

        all_datasets = []
        for dataset_id in dataset_ids:

            if dataset_id not in id_to_type:
                continue

            info = id_to_type[dataset_id]

            source_type = "Upload"

            if "ean.source_type" in info["fields"]:
                source_type = info["fields"]["ean.source_type"]

            get_source_request = self.download_dataset_content(org_id=org_id, dataset_id=dataset_id)

            result = {
                "component": None,
                "id": dataset_id,
                "schema": info["fields"]["schema"],
                "name": id_to_type[dataset_id]["name"],
                "type": source_type,
                "file_content": csv_to_json(csv_data=get_source_request)
            }

            all_datasets.append(result)

        return json.dumps(all_datasets)

    def add_data_to_existing_source(
            self, name, org_id, file_path,
            data_set_id, group_id, format="csv"):
        """
        Helper function to append data to existing dataset

        :param name: Name of the current file, used for staging the file
        :type name: str
        :param org_id: Org id where the target dataset exists
        :type org_id: int or str
        :param file_path: Directory file path that contains the data to be appended
        :type file_path: str
        :param data_set_id: Dataset id where the content will be appended
        :type data_set_id: int or str
        :param group_id: Group identification that the dataset belongs
        :type group_id: str
        :param format: File format. Accepts "CSV" or "TSV"
        :type format: str, optional
        :return:
        """
        results = {}

        second_stage = self.stage_data(
            name=name,
            org_id=org_id,
            file_path=file_path,
            group_id=group_id,
            format=format
        )

        results["group_id"] = second_stage

        final_commit = self.append_command(
            org_id=org_id,
            data_set_id=data_set_id,
            name=name,
            group_id=results["group_id"]
        )

        results.update(final_commit)

        return results

    def overwrite_dataset(
            self, org_id, data_set_id, file_path, group_id=None,
            format="csv", convert_to_parquet="false"):

        """
        Overwrites the contents of the given dataset with new content.

        :param org_id: Org id where the target dataset exists
        :type org_id: int or str
        :param data_set_id: Dataset id that its content will be overwritten
        :type data_set_id: str
        :param file_path: Directory file path that contains the data to be appended
        :type file_path: str
        :param group_id: Group identification that the dataset belongs
        :type group_id: str, optional
        :param format: File format. Accepts "CSV" or "TSV"
        :type format: str, optional
        :param convert_to_parquet: Flag to convert file to parquet
        :type convert_to_parquet: bool, optional
        :return:
        """
        response = {}

        response["truncate"] = self.truncate_data_set(
            org_id=org_id,
            data_set_id=data_set_id
        )

        name = "overwirte{}".format(int(time.time()))

        response["stage"] = self.stage_file(
            name=name,
            org_id=org_id,
            file_path=file_path,
            group_id=group_id,
            format=format,
            convert_to_parquet=convert_to_parquet
        )

        response["append"] = self.append_command(
            org_id=org_id,
            data_set_id=data_set_id,
            group_id=response["stage"],
            name=name
        )

        return response


    def _commit_dataset_command(self, org_id, data_set_id, command):
        header = self.build_header(
            aut_token=self.props.get_auth_token(cluster=self.cluster),
            org_id=org_id,
            others={"'Content-Type'": "application/data"}
        )
        headers = dict(header.items())
        request = self.session.post(
            self.commit_data_set_url.format(data_set_id),
            headers=headers,
            json=command
        )

        if request.status_code in [200, 202]:
            return json.loads(request.content)
        else:
            raise Exception(repr(request.content))

    def truncate_data_set(self, org_id, data_set_id):
        """
        Truncates the dataset content.

        :param org_id: Org where the target dataset exists
        :type org_id: int or str
        :param data_set_id: Dataset id where which contents will be truncated
        :type data_set_id: str
        :return:
        """
        command = {"commands": [{"$type": "truncate", "cause": []}]}
        return self._commit_dataset_command(org_id, data_set_id, command)


    def append_dataset(self, org_id, data_set_id, content):
        """
        Appends data to existing dataset.

        :param org_id: Org where the target dataset exists
        :type org_id: int or str
        :param data_set_id: Dataset id where the content will be appended
        :type data_set_id: str
        :param content: Data content that will be added to the dataset
        :type content: str
        :return:
        """
        file_dir, path = mkstemp(suffix=".csv")

        open(path, "wb").write(content.encode())

        os.close(file_dir)

        headers = self.build_header(
            aut_token=self.props.get_auth_token(cluster=self.cluster),
            org_id=org_id
        )

        files = {'file': open(path, "rb")}

        post_upload_file = self.session.post(
            self.append_url.format(org_id, data_set_id),
            headers=headers,
            files=files
        )

        if post_upload_file.status_code in [200, 201, 202]:
            response = json.loads(post_upload_file.content)

            return response

        raise Exception(repr(post_upload_file.content))

    def label(self, org_id, data_set_id, labels):
        command = {
            "commands":
                [
                    {
                        "$type": "text-label-group",
                        "key": "ean.facets",
                        "values": labels,
                        "cause": [],
                    }
                ]
        }
        return self._commit_dataset_command(org_id, data_set_id, command)

    def append_command(self, org_id, data_set_id, group_id, name):
        """
        Executes append command to a staged file on a group id.

        :param org_id: Org where the target dataset exists
        :type org_id: int or str
        :param data_set_id: Dataset id to be appended
        :type data_set_id: str
        :param group_id: Group identification that the dataset belongs
        :type group_id: str
        :param name: Name of the staged file
        :type name: str
        :return:
        """
        command = {
            "commands":
                [
                    {
                        "$type": "append",
                        "name": repr(name),
                        "group": group_id.decode(),
                        "cause": []
                    }
                ]
        }
        return self._commit_dataset_command(org_id, data_set_id, command)


    def stage_data(
            self, name, org_id, file_path, group_id=None, format="csv",
            convert_to_parquet="false", encoding='UTF-8', encode=False):
        """
        Stages data to a given org and group id.

        :param name: Name of the staged file
        :type name: str
        :param org_id: Org where the target dataset exists
        :type org_id: int or str
        :param file_path: Directory file path with files to be staged
        :type file_path: str
        :param group_id: Group identification that the dataset belongs
        :type group_id: str, optional
        :param format: File format. Accepts "CSV" or "TSV"
        :type format: str, optional
        :param convert_to_parquet: Flag to convert to parquet
        :type convert_to_parquet: bool, optional
        :param encoding: Dataset file encoding
        :type encoding: str, optional
        :param encode: Encode the dataset with given encoding
        :type encode: bool, optional
        :return:
        """
        header = self.build_header(
            aut_token=self.props.get_auth_token(cluster=self.cluster),
            org_id=org_id
        )

        header.update({"'Content-Type'": "application/octet-stream"})

        headers = dict(header.items())

        if group_id is None:
            payload_data = {
                "name": repr(name),
                "convertToParquet": convert_to_parquet,
                "format": format
            }
        else:
            payload_data = {
                "name": repr(name),
                "convertToParquet": convert_to_parquet,
                "format": format,
                "groupId": group_id
            }

        file_data = open(file_path, "r").read().encode(encoding)

        test_request = self.session.post(
            self.stage_file_url,
            headers=headers,
            data=file_data,
            params=payload_data
        )

        return test_request.content

    def stage_file(self, name, org_id, file_path, group_id=None, format="csv",
                   convert_to_parquet="false", encoding='UTF-8', encode=False):
        """
        Stage data from file to a given org and group id.

        :param name: Name of the staged file
        :type name: str
        :param org_id: Org where the target dataset exists
        :type org_id: int or str
        :param file_path: Directory file path with files to be staged
        :type file_path: str
        :param group_id: Group identification that the dataset belongs
        :type group_id: str, optional
        :param format: File format. Accepts "CSV" or "TSV"
        :type format: str, optional
        :param convert_to_parquet: Flag to convert to parquet
        :type convert_to_parquet: bool, optional
        :param encoding: Dataset file encoding
        :type encoding: str, optional
        :param encode: Encode the dataset with given encoding
        :type encode: bool, optional
        :return:
        """

        file_data = open(file_path, "r").read().encode(encoding)

        return self.stage_file_with_content(
            name=name,
            org_id=org_id,
            file_data=file_data,
            group_id=group_id,
            format=format,
            convert_to_parquet=convert_to_parquet,
            encoding=encoding,
            encode=encode
        )

    def stage_file_with_content(
            self, name, org_id, file_data, group_id=None,
            format="csv", convert_to_parquet="false", encoding='UTF-8', encode=False
    ):
        """
        Stage data from content to a given org and group id.

        :param name: Name of the staged file
        :type name: str
        :param org_id: Org where the target dataset exists
        :type org_id: int or str
        :param file_data: Content with data to be staged
        :type file_data: str
        :param group_id: Group identification that the dataset belongs
        :type group_id: str, optional
        :param format: File format. Accepts "CSV" or "TSV"
        :type format: str, optional
        :param convert_to_parquet: Flag to convert to parquet.
        :type convert_to_parquet: bool, optional
        :param encoding: File encoding
        :type encoding: str, optional
        :param encode: Encode the dataset with given encoding
        :type encode: bool, optional
        :return:
        """
        header = self.build_header(
            aut_token=self.props.get_auth_token(cluster=self.cluster),
            org_id=org_id
        )

        header.update({"'Content-Type'": "application/octet-stream"})

        headers = dict(header.items())

        if group_id is None:

            payload_data = {
                "name": repr(name),
                "convertToParquet": convert_to_parquet,
                "format": format
            }
        else:
            payload_data = {
                "name": repr(name),
                "convertToParquet": convert_to_parquet,
                "format": format,
                "groupId": group_id
            }

        test_request = self.session.post(
            self.stage_file_url,
            headers=headers,
            data=file_data,
            params=payload_data
        )

        return test_request.content

    def post_file_schema(self, org_id, schema_data, encoding='UTF-8'):
        """
        Posts the schema of a file to be staged.

        :param org_id: Org where the file is going to be staged
        :type org_id: int or str
        :param schema_data: File schema
        :type schema_data: dict
        :param encoding: File encoding
        :type encoding: str, optional
        :return:
        """

        header = self.build_header(
            aut_token=self.props.get_auth_token(cluster=self.cluster),
            org_id=org_id,
            others={"'Content-Type'": "application/data"}
        )

        headers = dict(header.items())

        schema_request = self.session.post(
            self.post_data_set_schema_url,
            headers=headers,
            data=schema_data
        )

        if schema_request.status_code == 200:
            return json.loads(schema_request.content)

        raise Exception(repr(schema_request.content))

    def pi_config_upload(self, name, server_name, file_path, org_id):
        """
        DEPRECATED - Use static_file_upload instead! This method may be removed
        in the future on a major version bump.

        Uploads PI-CONFIG dataset.

        :param name: Dataset name
        :type name: str
        :param server_name: PI-Config data archive server name
        :type server_name: str
        :param file_path: Directory file path with files to be uploaded
        :type file_path: str
        :param org_id: Org where the dataset will be created
        :type org_id: int or str
        :return:
        """

        headers = self.build_header(
            aut_token=self.props.get_auth_token(cluster=self.cluster),
            org_id=org_id
        )

        upload_file = {'file': open(file_path, "rb")}

        query_strings = {"name": str(name), "serverName": str(server_name)}

        post_upload_pitag = self.session.post(
            self.piconfig_upload_url_no_params.format(org_id),
            params=query_strings,
            headers=headers,
            files=upload_file
        )

        if post_upload_pitag.status_code == 200:
            return json.loads(post_upload_pitag.content)

        raise Exception(repr(post_upload_pitag.content))

    def static_file_upload(self, name, content, org_id):
        """
        Uploads a static file with content.

        :param name: Dataset name to be created
        :type name: str
        :param content: Dataset content stored in a variable
        :type content: str
        :param org_id: Org where the dataset will be created
        :type org_id: str
        :return:
        """

        static_file_upload_url = self.staticfile_upload_url

        query_strings = {"name": str(name)}

        headers = self.build_header(
            aut_token=self.props.get_auth_token(cluster=self.cluster),
            org_id=org_id
        )

        files = {'file': open(content, "rb")}

        post_upload_file = self.session.post(
            static_file_upload_url.format(org_id),
            headers=headers,
            files=files,
            params=query_strings
        )

        if post_upload_file.status_code == 200:
            return json.loads(post_upload_file.content)

        raise Exception(repr(post_upload_file.content))

    def get_sources(self, org_id):
        """
        Retrieves all the metadata of datasets on an org.

        :param org_id: Org to be queried
        :type org_id: int or str
        :return:
        """

        header = self.build_header(
            aut_token=self.props.get_auth_token(cluster=self.cluster),
            org_id=org_id,
            others=self.delete_content_type_header
        )

        if self.evergreen_enabled:

            query_strings = {
                "ean.orgs": org_id,
                "_fields": "schema,ean.ready,ean.source_type"
            }

            get_sources_request = self.session.get(
                self.labeling_sources_2,
                headers=header,
                params=query_strings
            )

            content = json.loads(get_sources_request.content.decode('utf8'))
        else:

            get_sources_request = self.session.get(self.sources_url.format(org_id), headers=header)

            content = json.loads(get_sources_request.content)

        if get_sources_request.status_code == 200:
            return content

        raise Exception(repr(get_sources_request.content))

    def get_sources_by_labels(self, org_id, facets):
        """
        Retieves all datasets that matches given labels.

        :param org_id: Org id
        :type org_id: int or str
        :param facets: List of dataset labels. Example: ["label1", "label2"]
        :type facets: list of str
        :return:
        """

        header = self.build_header(
            aut_token=self.props.get_auth_token(cluster=self.cluster),
            org_id=org_id,
            others=self.delete_content_type_header
        )

        query_strings = {
            "facet": facets
        }

        get_sources_request = self.session.get(
            self.labeling_sources_facets_url,
            headers=header,
            params=query_strings
        )

        content = json.loads(get_sources_request.content)

        if get_sources_request.status_code == 200:
            return content

        raise Exception(repr(get_sources_request.content))
