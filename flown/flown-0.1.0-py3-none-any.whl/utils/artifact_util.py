import mlflow
from flown.utils import merge_html
from mlflow.store.artifact.artifact_repository_registry import _artifact_repository_registry
from mlflow.tracking import MlflowClient
from mlflow.entities import Run
import os
from mlflow.models.model import MLMODEL_FILE_NAME
# from mlflow.projects._project_spec import MLPROJECT_FILE_NAME
from flown.utils.image_util import image_file_to_base64

TEXT_EXTENSIONS = [
    "txt",
    "log",
    "yaml",
    "yml",
    "json",
    "js",
    "py",
    "csv",
    "tsv",
    "md",
    "rst",
    MLMODEL_FILE_NAME,
    # MLPROJECT_FILE_NAME,
]


def download_artifact(run: Run, path: str):
    artifact_repo = _artifact_repository_registry.get_artifact_repository(run.info.artifact_uri)
    filename = os.path.abspath(artifact_repo.download_artifacts(path))
    return filename


def artifact_viewer_html(run: Run, artifact: dict):
    filename = download_artifact(run, artifact.get('path'))
    extension = os.path.splitext(filename)[-1].replace(".", "").lower()
    file_content = None
    if extension in TEXT_EXTENSIONS:
        with open(filename, 'r', encoding='UTF-8') as f:
            file_content = f.read()
        return merge_html('artifact_viewer.html', dict(artifact=artifact, text_content=file_content, file_extension=extension))
    else:
        file_content = image_file_to_base64(filename)
        return merge_html('artifact_viewer.html', dict(artifact=artifact, image_content=file_content, file_extension=extension))
        # return send_file(filename, as_attachment=True)

# print(get_artifact_handler(run_id='24bffa9c5c2e46e087dd87ebc5d4c36c', path='test.txt'))

"""
<p>path : <span>{{ artifact.artifact_path }}</span>, size : <span>{{ artifact.file_size }}</span></p>
<hr/>

{{content_html | safe}}
"""