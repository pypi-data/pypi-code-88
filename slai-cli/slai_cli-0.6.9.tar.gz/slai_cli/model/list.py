from columnar import columnar

from slai.clients.project import get_project_client

from slai_cli import log
from slai_cli.decorators import requires_slai_project


@requires_slai_project
def list_models():
    project_client = get_project_client(project_name=None)
    models = project_client.list_models()

    headers = ["id", "name", "created", "updated", "version"]
    data = [
        [
            model["id"],
            model["name"],
            model["created"],
            model["updated"],
            model["model_version_id"],
        ]
        for model in models
    ]
    try:
        table = columnar(data, headers, no_borders=True)
        log.info(table)
    except IndexError:
        log.warn("No models found.")
        return
