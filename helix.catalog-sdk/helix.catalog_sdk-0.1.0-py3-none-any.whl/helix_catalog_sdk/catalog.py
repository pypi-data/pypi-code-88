import json
from datetime import datetime, timedelta
from types import SimpleNamespace
from typing import List, Optional, Tuple


from helix_catalog_sdk.data_source import DataSource


from helix_catalog_sdk.enums import HelixEnvironment
from helix_catalog_sdk.repo import BaseRepo


class Catalog:
    def __init__(self, repo: BaseRepo):
        self._repo = repo
        self._last_updated_data_source_dttm: datetime = datetime.utcnow() + timedelta(
            days=-1
        )
        self._all_data_sources: List[Tuple[str, DataSource]] = []
        self._all_data_sources = self.get_all_data_sources()

    def get_data_source(
        self, data_source: str, environment: HelixEnvironment
    ) -> Optional[DataSource]:
        decoded_contents = self._repo.read_file(data_source)
        contents: SimpleNamespace = json.loads(
            decoded_contents, object_hook=lambda d: SimpleNamespace(**d)
        )

        # Currently only data_sources of type "file" are working in the catalog.
        if getattr(contents, "connection_type", None) != "file":
            return None

        return DataSource(data_source, contents, environment)

    def update_data_source_resource(self, file_path: str) -> Optional[DataSource]:
        for data_source_path, data_source in self._all_data_sources:
            if data_source.matches_path(file_path):
                data_source.update_path_with_latest_file(file_path)
                self.update_data_source(data_source_path, data_source.to_json())
                return data_source
        return None

    def update_data_source(self, data_source_name: str, updated_contents: str) -> None:
        self._repo.update_file(data_source_name, updated_contents)

    def get_all_data_sources(
        self, base_path: str = "catalog"
    ) -> List[Tuple[str, DataSource]]:
        last_repo_update = self._repo.last_update(base_path)
        needs_update = (
            last_repo_update is None
            or last_repo_update > self._last_updated_data_source_dttm
        )
        self._last_updated_data_source_dttm = datetime.utcnow()
        if needs_update or len(self._all_data_sources) == 0:
            print("getting all data sources")
            catalog_contents = self._repo.list_items(base_path)
            data_sources: List[Tuple[str, DataSource]] = []
            while catalog_contents:
                file_path = catalog_contents.pop(0)
                if self._repo.is_dir(file_path):
                    catalog_contents.extend(self._repo.list_items(file_path))
                elif file_path.endswith(".json"):
                    data_source = self.get_data_source(
                        file_path, HelixEnvironment.PRODUCTION
                    )
                    if data_source:
                        data_sources.append((file_path, data_source))
            self._all_data_sources = data_sources
            return data_sources
        else:
            print("returning cached data sources")
            return self._all_data_sources
