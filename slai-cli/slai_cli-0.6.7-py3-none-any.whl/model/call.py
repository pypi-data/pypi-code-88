import time
import slai

from slai.clients.project import get_project_client
from slai_cli import log


def call_model(*, model_name, input):
    project_client = get_project_client()

    project_name = project_client.get_project()["name"]

    _model = slai.model(f"{project_name}/{model_name}")

    for i in range(100):
        start = time.time()
        response = _model(weight=1.0, age=0.1, height=67.0)
        elapsed = time.time() - start

        log.info(str(response))
        log.info(f"inference time: {elapsed}")
