import mlflow
from mlflow.entities import ViewType
from mlflow.store.tracking.file_store import FileStore
from uuid import uuid4
from operator import attrgetter
from datetime import datetime

class ProjectStore(FileStore):
    def __init__(self, root_directory=None, artifact_root_uri=None):
        """
        Create a new FileStore with the given root directory and a given default artifact root URI.
        """

        # uriから`project://` 部分を削除して使う
        if root_directory.startswith('project://'):
            root_directory = root_directory[10:]
        super().__init__(root_directory, artifact_root_uri)

    def create_experiment(self, name, artifact_location=None):
        self._check_root_dir()
        self._validate_experiment_name(name)
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        experiment_id = f"{timestamp}-{str(uuid4())}"
        return self._create_experiment_with_id(name, experiment_id, artifact_location)


def get_project_store(store_uri, artifact_uri):
    return ProjectStore(root_directory=store_uri, artifact_root_uri=artifact_uri)
