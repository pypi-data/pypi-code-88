import json
from datetime import datetime, timedelta
from types import SimpleNamespace
from typing import Union, List, Tuple, Optional

from github.ContentFile import ContentFile
from github.Repository import Repository

from helix_catalog_sdk.data_source import DataSource

from github import Github

from helix_catalog_sdk.enums import HelixEnvironment


class Catalog:
    def __init__(self, repo: str, access_token: str):
        self._github_client: Github = Github(login_or_token=access_token)
        self._repo = self.get_repo(repo)
        self._last_updated_data_source_dttm: datetime = datetime.utcnow() + timedelta(
            days=-1
        )
        self._all_data_sources: List[Tuple[DataSource, str]] = []
        self._all_data_sources = self.get_all_data_sources()

    def get_repo(self, repo: str) -> Repository:
        return self._github_client.get_repo(repo)

    def get_data_source(
        self, data_source: str, environment: HelixEnvironment
    ) -> Tuple[DataSource, str]:
        decoded_contents, sha = self.get_contents_as_string(data_source)
        contents: SimpleNamespace = json.loads(
            decoded_contents, object_hook=lambda d: SimpleNamespace(**d)
        )
        return DataSource(data_source, contents, environment), sha

    def update_data_source_resource(
        self, path: str
    ) -> Optional[Tuple[DataSource, str]]:
        data_sources = self.get_all_data_sources()

        data_source_to_update: Tuple[DataSource, str]
        for data_source in data_sources:
            for resource_item in data_source[0].resources:
                if resource_item.full_path_slug in path:
                    index: int = path.find(resource_item.path_slug)
                    resource_item.path = path[index:]
                    data_source_to_update = data_source
                    del data_source_to_update[0].base_connection_formatted
                    for resource in data_source_to_update[0].resources:
                        del resource.full_path_slug
                        del resource.full_path

                    updated_contents = data_source_to_update[0].to_json()
                    self.update_data_source(
                        data_source_to_update[0].name,
                        updated_contents,
                        data_source_to_update[1],
                    )
                    return data_source_to_update
        return None

    def update_data_source(
        self, data_source_name: str, updated_contents: str, data_source_sha: str
    ) -> None:
        self._repo.update_file(
            data_source_name,
            "updated by helix-catalog",
            updated_contents,
            data_source_sha,
        )

    def get_all_data_sources(self) -> List[Tuple[DataSource, str]]:
        commits = self._repo.get_commits(
            path="catalog", since=self._last_updated_data_source_dttm
        )
        self._last_updated_data_source_dttm = datetime.utcnow()
        if commits.totalCount > 0 or len(self._all_data_sources) == 0:
            print("getting all data sources")
            catalog_contents = self._repo.get_contents("catalog/raw")
            data_sources: List[Tuple[DataSource, str]] = []
            while catalog_contents:
                file_content = catalog_contents.pop(0)  # type: ignore
                if file_content.type == "dir":
                    catalog_contents.extend(self._repo.get_contents(file_content.path))  # type: ignore
                else:
                    data_sources.append(
                        self.get_data_source(
                            file_content.path, HelixEnvironment.PRODUCTION
                        )
                    )
            self._all_data_sources = data_sources
            return data_sources
        else:
            print("returning cached data sources")
            return self._all_data_sources

    def get_contents_as_string(self, data_source: str) -> Tuple[str, str]:
        contents: Union[List[ContentFile], ContentFile] = self._repo.get_contents(
            data_source
        )
        decoded_contents: str = contents.decoded_content.decode("utf-8")  # type: ignore
        return decoded_contents, contents.sha  # type: ignore
