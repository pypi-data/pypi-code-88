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
Contains support methods for export and import workflows
"""
import json
import os.path
import uuid

from tempfile import mkstemp

from unify.properties import ClusterSetting
from unify.orgadmin import OrgAdmin
from unify.properties import Properties
from unify.templates import Templates
from unify.pipelines import Pipelines
from unify.sources import Sources
from unify.generalutils import json_to_csv
from unify.generalutils import csv_to_json
from unify.apiutils import remove_special
from unify.assetaccess import AssetAccess


class ApiManager:
    """
    Class to interact with import and export dataset methods
    """

    def __init__(self, cluster=None, props=Properties(ClusterSetting.KEY_RING)):
        try:

            self.properties = props

            self.evergreen_enabled = self.properties.get_asset_sync(cluster=cluster)

            self.orgs = OrgAdmin(cluster=cluster, props=self.properties)

            self.templates = Templates(cluster=cluster, props=self.properties)

            self.pipelines = Pipelines(cluster=cluster, props=self.properties)

            self.sources = Sources(cluster=cluster, props=self.properties)

            self.cluster = cluster

            self.sources.evergreen_enabled = self.evergreen_enabled

            self.pipelines.evergreen_enabled = self.evergreen_enabled

        except Exception as error:
            raise error

    def import_source(self, content, orgid, name, type, encoding="UTF-8", chunks=10000):
        """
        Creates a new dataset with content. Option to chunk the amount of lines that the file will be partitioned

        :param content: CSV or TSV file content
        :type content: str
        :param orgid: Org where the source will be imported
        :type orgid: int or str
        :param name: Name to be given to the datasource
        :type name: str
        :param type: Type of the dataset. Accepts "external" or "generic"
        :type type: str
        :param encoding: File encoding
        :type encoding: str
        :param chunks: Number of chunks to split a large dataset,
        :type chunks: int
        :return:
        """
        if type == "external":

            file_dir, path = mkstemp(suffix=".csv")

            open(path, "wb").write(content.encode())

            new_source = self.sources.static_file_upload(
                name=name,
                content=path,
                org_id=orgid
            )

            os.close(file_dir)

            if "sourceMetadata" in new_source:
                del new_source["sourceMetadata"]

            return new_source

        elif type == "generic":

            return self.sources.upload_big_dataset(
                name=name,
                org_id=orgid,
                content=content,
                encoding=encoding,
                chunks=chunks
            )

        else:
            raise Exception("Unsupported type of source to be imported")

    def export_source(self, org_id, dataset_ids):
        """
        Retrieves the content of a dataset

        :param org_id: org id where the dataset is located
        :type org_id: int or str
        :param dataset_ids: dataset id to be retrieved
        :type dataset_ids: list of str
        :return:
        """
        return self.sources.create_export_dataset(
            org_id=org_id,
            dataset_ids=dataset_ids
        )

    def append_data(self, content, orgid, dataset_id):
        """
        Appends content to a dataset

        :param content: dataset comntent to be appended
        :type content: str
        :param orgid: org id where the target dataset lives
        :type orgid: int or str
        :param dataset_id: dataset id
        :type dataset_id: str
        :return:
        """
        return self.sources.append_dataset(
            org_id=orgid,
            data_set_id=dataset_id,
            content=content
        )

    def dataset_list(self, org_id):
        """
        Retrieves metadata for all datasets on a given org

        :param org_id: ORG id to be queried
        :type org_id: ORG id to be queried
        :return:
        """
        try:
            sources = self.sources.get_sources(org_id=org_id)

            for source in sources:
                if "fields" in source:
                    if "schema" in source["fields"]:
                        del source["fields"]["schema"]
            return sources
        except Exception as error:
            raise error

    def pipeline_list(self, org_id):
        """
        Retrieves metadata for all pipelines on a given org

        :param org_id: ORG id to be queried
        :type org_id: ORG id to be queried
        :return:
        """
        try:
            sources = self.pipelines.get_pipelines_v2(org_id=org_id)

            return sources["pipelineSummaries"]

        except Exception as error:
            raise error

    def execute_query(self, query, orgid, format):
        """
        Executes the given sql query through Unify Access on a given org

        :param query: Query
        :type query: str
        :param orgid: Org id to query
        :type orgid: int or str
        :param format: Result format. Accepts "CSV".
        :type format: str
        :return:
        """

        access = AssetAccess(cluster=self.cluster, orgid=orgid, props=self.properties)

        result = access.execute_query(query=query)

        if format == "csv":
            return json_to_csv(result, io_format=False)

        return result

    def export_function(self, org_id, function):
        """
        Create a json structure with all the components needed
        to import a function
        :param org_id:
        :param function:
        :return:
        """
        return self.create_pipeline_export_data(
            org_id=org_id,
            pipeline_id=function,
            skip=[]
        )

    def assethub_access_tables(self, orgid):
        """
        Retrieves all Unify Access tables on the given org

        :param orgid: Org id to query the asset access tables
        :type orgid: int or str
        :return:
        """
        access = AssetAccess(cluster=self.cluster, orgid=orgid, props=self.properties)

        return access.get_all_tables()

    def import_sources(self, org_id, pipeline_id, content, handleduplicates="clone", update_pipeline=True):
        """
        Import the datasets, this method is used on the wf import pipelines

        :param org_id: Org id where the sources are going to be imported
        :type org_id: int or str
        :param pipeline_id: In case the sources that are imported and a pipeline used then
        :type pipeline_id: int or str
        :param content: Content file has all the data.
        :type content: str
        :param handleduplicates: In case there is a dataset with the same name. Accept "clone"
        :type handleduplicates: str, optional
        :param update_pipeline: Flag to update the pipeline
        :type update_pipeline: bool, optional
        :return:
        """

        try:
            data = json.loads(content)

            non_evergreen_conversion_type = {
                "JsonPiConfigFileSourceMetaData": "piconfig",
                "JsonFileSourceMetadata": "external",
                "JsonPiWebApiSourceMetadata": "web",
                "PI_Upload": "piconfig",
                "Upload": "external",
                "api_dataset": "api_dataset",
                "PiWeb": "web"
            }

            needed_keys = {"id", "component", "schema", "type", "file_content", "name"}

            already_created_by_name = {}

            for source_to_import in data:

                if needed_keys.issubset(source_to_import.keys()):

                    which_type = None

                    if self.evergreen_enabled:

                        which_type = non_evergreen_conversion_type[source_to_import["type"]]

                        if which_type in ["external", "api_dataset"]:

                            file_dir, path = mkstemp(suffix=".csv")

                            open(path, "wb").write(
                                json_to_csv(
                                    source_to_import["file_content"],
                                    io_format=False
                                ).encode()
                            )

                            new_source = self.sources.static_file_upload(
                                name=source_to_import["name"],
                                content=path,
                                org_id=org_id
                            )

                            source_to_import["new_source_id"] = new_source["id"]

                            already_created_by_name[source_to_import["name"]] = new_source["id"]

                            os.close(file_dir)
                            try:
                                os.remove(path)
                            except OSError:
                                pass

                        if which_type in ["piconfig", "web"]:

                            file_dir, path = mkstemp(suffix=".csv")

                            server_name = remove_special(
                                out_file=path,
                                data_array=source_to_import["file_content"]
                            )

                            if server_name is None:
                                server_name = "PITAGCONFIGFILESERVER"

                            new_source = self.sources.pi_config_upload(
                                name=source_to_import["name"],
                                server_name=server_name,
                                file_path=path,
                                org_id=org_id
                            )

                            source_to_import["new_source_id"] = new_source["id"]

                            already_created_by_name[source_to_import["name"]] = new_source["id"]

                            os.close(file_dir)
                            try:
                                os.remove(path)
                            except OSError:
                                pass

                    else:
                        which_type = non_evergreen_conversion_type[source_to_import["type"]]

                        if source_to_import["name"] in already_created_by_name:

                            source_to_import["new_source_id"] = already_created_by_name[
                                source_to_import["name"]
                            ]

                        else:
                            if which_type in ["external", "web"]:

                                file_dir, path = mkstemp(suffix=".csv")

                                open(path, "wb").write(
                                    json_to_csv(
                                        source_to_import["file_content"],
                                        io_format=False
                                    ).encode()
                                )

                                new_source = self.sources.static_file_upload(
                                    name=source_to_import["name"],
                                    content=path,
                                    org_id=org_id
                                )

                                source_to_import["new_source_id"] = new_source["id"]

                                already_created_by_name[source_to_import["name"]] = new_source["id"]

                                os.close(file_dir)

                                try:
                                    os.remove(path)
                                except OSError:
                                    pass
                            if which_type == "piconfig":

                                file_dir, path = mkstemp(suffix=".csv")

                                server_name = remove_special(
                                    out_file=path,
                                    data_array=source_to_import["file_content"]
                                )

                                if server_name is None:
                                    server_name = "PITAGCONFIGFILESERVER"

                                new_source = self.sources.pi_config_upload(
                                    name=source_to_import["name"],
                                    server_name=server_name,
                                    file_path=path,
                                    org_id=org_id
                                )

                                source_to_import["new_source_id"] = new_source["id"]
                                already_created_by_name[source_to_import["name"]] = new_source["id"]

                                os.close(file_dir)

                                try:
                                    os.remove(path)
                                except OSError:
                                    pass



                else:
                    raise Exception("Missing export data {} ".format(
                        needed_keys.difference(source_to_import.keys()))
                    )

            if update_pipeline:

                pipeline_info = self.pipelines.get_pipeline(
                    org_id=org_id,
                    pipeline_id=pipeline_id
                )

                for component in pipeline_info["pipeline"]["data"]["components"]:

                    if component["jsonClass"] == "JsonSourceRef":

                        for modified_source in data:

                            if modified_source["component"] == component["id"]:
                                component["sourceId"] = modified_source["new_source_id"]

                self.pipelines.update_pipeline_from_json(
                    org_id=org_id,
                    update_payload=pipeline_info["pipeline"]["data"],
                    pipeline_id=pipeline_id,
                    pipeline_name=pipeline_info["pipeline"]["data"]["name"]
                )

                return json.dumps(pipeline_info)

            return "Data sets imported successfully"

        except Exception as error:
            raise error

    def use_existing_datasets(self, org_id, pipeline_id, content):
        """
        Method to use the existing datasets in the pipeline to be imported

        :param org_id: Destination org where datasets live
        :type org_id: int or str
        :param pipeline_id: Pipeline which is being exported
        :type pipeline_id: int or str
        :param content: Contents
        :type content: str
        :return:
        """
        try:
            errors = set()
            pipeline_info = self.pipelines.get_pipeline(
                org_id=org_id,
                pipeline_id=pipeline_id
            )

            data = json.loads(content)

            sources = self.sources.get_sources(org_id=org_id)

            current_name_to_id = {}

            for source in sources:
                current_name_to_id[source["name"]] = source["id"]

            import_id_to_name = {}
            for source_to_import in data:
                import_id_to_name[source_to_import["id"]] = source_to_import["file_content"]

            for component in pipeline_info["pipeline"]["data"]["components"]:
                if component["jsonClass"] == "JsonSourceRef":

                    for modified_source in data:

                        if modified_source["component"] == component["id"]:
                            if import_id_to_name[component["sourceId"]] in current_name_to_id:

                                component["sourceId"] = current_name_to_id[
                                    import_id_to_name[component["sourceId"]]
                                ]

                            else:
                                errors.add(
                                    "No dataset with name {} was found".format(
                                        import_id_to_name[component["sourceId"]]
                                    )
                                )

                                component["sourceId"] = str(uuid.uuid4())

                self.pipelines.update_pipeline_from_json(
                    org_id=org_id,
                    update_payload=pipeline_info["pipeline"]["data"],
                    pipeline_id=pipeline_id,
                    pipeline_name=pipeline_info["pipeline"]["data"]["name"]
                )

        except Exception as err:
            raise err

        return list(errors)

    def create_export_source_file(self, org_id, pipeline_id, skip):
        """
        This methods creates the export file

        :param org_id: Org id to export the dataset
        :type org_id: int or str
        :param pipeline_id: Pipeline id
        :type pipeline_id: int or str
        :param skip: skip
        :type skip: bool
        :return:
        """

        sources = self.sources.get_sources(org_id=org_id)

        source_id_to_data = {}

        result_data = []

        for source in sources:
            if self.evergreen_enabled:
                source_id_to_data[source["id"]] = source
            else:
                source_id_to_data[source["id"]] = source

        pipeline_info = self.pipelines.get_pipeline(org_id=org_id, pipeline_id=pipeline_id)

        for component in pipeline_info["pipeline"]["data"]["components"]:
            if component["jsonClass"] == "JsonSourceRef":
                source_data = {
                    "id": component["sourceId"],
                    "component": component["id"]
                }

                if component["sourceId"] in source_id_to_data:

                    if self.evergreen_enabled:

                        source_data["schema"] = source_id_to_data[source_data["id"]]["fields"]["schema"]

                        source_data["name"] = source_id_to_data[source_data["id"]]["name"]

                        if "ean.source_type" in source_id_to_data[source_data["id"]]["fields"]:
                            source_data["type"] = source_id_to_data[source_data["id"]]["fields"]["ean.source_type"]
                        else:
                            source_data["type"] = "api_dataset"

                    else:
                        source_data["name"] = source_id_to_data[source_data["id"]]["name"]
                        source_data["schema"] = source_id_to_data[source_data["id"]]["schema"]
                        source_data["type"] = source_id_to_data[source_data["id"]]["sourceMetadata"]["jsonClass"]

                    if skip:
                        source_data["file_content"] = source_id_to_data[source_data["id"]]["name"]
                    else:
                        source_original_data = self.sources.download_dataset_content(
                            org_id=org_id,
                            dataset_id=component["sourceId"]
                        )
                        source_data["file_content"] = csv_to_json(csv_data=source_original_data)

                    result_data.append(source_data)

        return json.dumps(result_data)

    def create_pipeline_export_data(self, org_id, pipeline_id, skip):
        """
        Create all the necessary data to export a pipeline

        :param org_id: Org id where the pipeline to be migrated is located
        :type org_id: int or str
        :param pipeline_id: Pipeline id to be exported
        :type pipeline_id: int or str
        :param skip: List of assets tp export, datasets and templates
        :type skip: list of str
        :return:
        """
        try:
            results = {}

            pipeline_info = self.pipelines.get_pipeline(org_id=org_id, pipeline_id=pipeline_id)

            templates_used = []
            aux_list = self.templates.list_asset_templates(org_id=org_id)

            mapped_templates = []

            results["map_attributes"] = {}

            results["functions"] = {}

            for component in pipeline_info["pipeline"]["data"]["components"]:

                if component["jsonClass"] == "JsonMapTemplates":

                    for mapped_value in component["values"]:
                        mapped_templates.append(mapped_value[1])

                if component["jsonClass"] == "JsonMapAttributes":
                    results["map_attributes"][component["id"]] = csv_to_json(
                        csv_data=self.pipelines.download_map_attributes(
                            org_id=org_id,
                            pipeline_id=pipeline_id,
                            component_id=component["id"]
                        )
                    )

                if component["jsonClass"] == "JsonFunctionApply":
                    func_id = "{}.{}.{}".format(pipeline_id, component["id"], component["pipelineId"])
                    results["functions"][func_id] = json.loads(
                        self.create_pipeline_export_data(
                            org_id=org_id,
                            pipeline_id=func_id,
                            skip=skip
                        )
                    )


            used_templates = []
            template_id_to_name = {}

            for temp in aux_list:

                if str(temp["id"]) in mapped_templates:
                    used_templates.append(temp["id"])
                    template_id_to_name[str(temp["id"])] = temp["name"]
                    if "updatedBy" in temp:
                        del temp["updatedBy"]
                    if "updated" in temp:
                        del temp["updated"]
                    templates_used.append(temp)

            results["pipeline"] = pipeline_info

            results["sources"] = json.loads(
                self.create_export_source_file(
                    org_id=org_id,
                    pipeline_id=pipeline_id,
                    skip="datasets" in skip
                )
            )

            if "templates" in skip:

                results["pipeline"], _ = self.change_template_ids_to_names(
                    pipeline_data=results["pipeline"],
                    templates_data=template_id_to_name
                )

                results["templates"] = []

                results["template_values"] = []

            else:

                results["templates"] = templates_used
                results["template_values"] = []
                if len(used_templates) > 0:
                    results["template_values"] = json.loads(
                        self.templates.download_given_templates(
                            org_id=org_id,
                            template_list=used_templates,
                            format="json")
                    )

            return json.dumps(results)

        except Exception as error:
            raise error

    def change_template_ids_to_names(self, pipeline_data, templates_data):
        """
        Changes the templates ids to its name

        :param pipeline_data: Pipeline json blob where templates are used
        :type pipeline_data: json
        :param templates_data: Templates data to be used
        :type templates_data: List of str
        :return:
        """

        errors = set()

        for component in pipeline_data["pipeline"]["data"]["components"]:

            if component["jsonClass"] == "JsonMapTemplates":

                if "values" in component:
                    new_val = []
                    for value in component["values"]:
                        row_vale = value[0]
                        template_id = value[1]
                        if template_id in templates_data:
                            new_val.append(
                                [
                                    row_vale,
                                    templates_data[template_id]
                                ]
                            )
                        else:
                            errors.add("{} not found".format(row_vale))

                    component["values"] = new_val

        return pipeline_data, list(errors)

    def change_tempate_names_to_ids(self, pipeline_data, templates_data):
        """
        Change the templates names to its ids

        :param pipeline_data: Pipeline json blob where templates are used
        :type pipeline_data: int or str
        :param templates_data: Templates data to be used
        :type templates_data: List of str
        :return:
        """

        errors = set()

        for component in pipeline_data["pipeline"]["pipeline"]["data"]["components"]:

            if component["jsonClass"] == "JsonMapTemplates":

                if "values" in component:
                    new_val = []
                    for value in component["values"]:
                        row_vale = value[0]
                        template_name = value[1]
                        if template_name in templates_data:
                            new_val.append(
                                [
                                    row_vale,
                                    str(templates_data[template_name])
                                ]
                            )
                        else:
                            errors.add("{} not found".format(template_name))

                    component["values"] = new_val

        return pipeline_data, list(errors)

    def proceses_importing_pipeline_file(self, org_id, content, skip, handleduplicates="clone", function=False,
                                         loaded=False):
        """
        Process pipeline importing.

        :param org_id: Target org id where the pipelien will be imported
        :type org_id: int or str
        :param content: Pipeline import content
        :type content: str
        :param skip: variable to skip datasets or templates
        :type skip: bool
        :param handleduplicates: Boolean variable to decide what to do with duplicate pipeline
        :type handleduplicates: bool, optional
        :return:
        """
        try:
            errors = []
            if not loaded:
                data = json.loads(content)
            else:
                data = content

            if handleduplicates == "clone":

                temp_name = data["pipeline"]["pipeline"]["data"]["name"]

                if self.pipelines.pipeline_exists(org_id=org_id, pipeline_name=temp_name):
                    data["pipeline"]["pipeline"]["data"]["name"] = "{}_{}".format(
                        temp_name,
                        str(uuid.uuid4())[:5]
                    )

            if "pipeline" not in data:
                raise Exception("Pipeline data was not found")

            pipeline_info = data["pipeline"]

            migrated_funcs = {}
            if "functions" in data:
                for func_id, func_content in data["functions"].items():
                    exists = self.pipelines.verify_if_pipeline_exists_and_get_id(
                        org_id=org_id,
                        pipeline_name=func_content["pipeline"]["pipeline"]["data"]["name"]
                    )
                    keys = func_id.split(".")

                    if exists["pipeline_id"] is not None:

                        migrated_funcs[keys[-1]] = exists["pipeline_id"]

                    if func_id not in migrated_funcs and exists["pipeline_id"] is None:

                        resp = json.loads(
                            self.proceses_importing_pipeline_file(
                                org_id=org_id,
                                content=func_content,
                                skip=skip,
                                handleduplicates=handleduplicates,
                                function=True,
                                loaded=True
                            )
                        )

                        migrated_funcs[keys[-1]] = resp["pipeline_id"]

            if function:
                pipeline_info["pipeline"]["data"]["pipelineType"] = "function"
            else:
                if "pipelineType" in pipeline_info["pipeline"]["data"]:
                    del pipeline_info["pipeline"]["data"]["pipelineType"]

            if "templates" not in data:
                raise Exception("Template data was not found")

            if "template_values" not in data:
                raise Exception("Template definitions was not found")

            if len(data["template_values"]) > 0:
                try:

                    self.templates.upload_string_content_file(
                        content=json_to_csv(
                            data_array=data["template_values"],
                            io_format=False
                        ),
                        org_id=org_id
                    )

                except Exception as error:
                    errors.append("Exporting many templates can cause issues!")

            template_info = data["templates"]

            templates = self.templates.list_asset_templates(org_id=org_id)

            current_id_name_map = {}
            prev_id_name_map = {}

            for template in template_info:
                prev_id_name_map[str(template["id"])] = template["name"]

            for template in templates:
                current_id_name_map[template["name"]] = template["id"]

            if "templates" in skip:
                data, err = self.change_tempate_names_to_ids(
                    pipeline_data=data,
                    templates_data=current_id_name_map
                )

                errors.extend(err)

            attributes_name_to_id = {}

            data["map_recipes"] = {}

            for used_template in data["templates"]:

                current_temp_id = current_id_name_map[used_template["name"]]

                attrs = self.templates.get_attributes(
                    org_id=org_id,
                    template_id=current_temp_id
                )

                attributes_name_to_id[current_temp_id] = {}

                for item in attrs["items"]:
                    attributes_name_to_id[current_temp_id][item["name"]] = item["id"]

            for component in pipeline_info["pipeline"]["data"]["components"]:

                if component["jsonClass"] == "JsonMapTemplates":
                    if "templates" not in skip:
                        for mapped_value in component["values"]:
                            if mapped_value[1] in prev_id_name_map:
                                inside = prev_id_name_map[mapped_value[1]]
                                if inside in current_id_name_map:
                                    mapped_value[1] = str(
                                        current_id_name_map[inside]
                                    )
                                else:
                                    errors.append(
                                        ("Template {} was deleted and "
                                         "is still mapped".format(mapped_value[1]))
                                    )
                            else:
                                errors.append(
                                    ("Template {} was deleted and "
                                     "is still mapped".format(mapped_value[1]))
                                )

                if component["jsonClass"] == "JsonMapAttributes":
                    data["map_recipes"][component["id"]] = data["map_attributes"][component["id"]]

                if component["jsonClass"] == "JsonFunctionApply":
                    component["pipelineId"] = migrated_funcs[str(component["pipelineId"])]

            pipeline = self.pipelines.create_pipeline(
                org_id=org_id,
                name=data["pipeline"]["pipeline"]["data"]["name"],
                function=function
            )

            created_pipeline_id = pipeline['pipeline']['id']

            self.pipelines.update_pipeline_from_json(
                org_id=org_id,
                update_payload=data["pipeline"]["pipeline"]["data"],
                pipeline_id=created_pipeline_id,
                pipeline_name=data["pipeline"]["pipeline"]["data"]["name"]
            )

            for component_id, recipe in data["map_recipes"].items():
                self.pipelines.upload_map_attributes_from_json(
                    org_id=org_id,
                    component_id=component_id,
                    pipeline_id=created_pipeline_id,
                    json_data=recipe
                )

            if "sources" in data:
                if "datasets" not in skip:
                    self.import_sources(
                        org_id=org_id,
                        pipeline_id=created_pipeline_id,
                        content=json.dumps(data["sources"]),
                        handleduplicates=handleduplicates,
                    )

                else:
                    err = self.use_existing_datasets(
                        org_id=org_id,
                        pipeline_id=created_pipeline_id,
                        content=json.dumps(data["sources"]),
                    )
                    errors.append(err)

            results = {
                "pipeline_id": created_pipeline_id,
                "org_id": org_id,
                "url": "{}#/org/{}/pipelines/{}".format(
                    self.properties.get_remote(self.cluster),
                    org_id,
                    created_pipeline_id
                ),
                "warnings": errors
            }

            return json.dumps(results)
        except Exception as error:
            raise error
