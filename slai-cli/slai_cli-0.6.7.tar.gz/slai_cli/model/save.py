import time

from pathlib import Path
from slai.clients.cli import get_cli_client
from slai.modules.notebook_utils import generate_trainer_from_template, parse_notebook
from slai_cli import log
from slai_cli.init.local_config_helper import LocalConfigHelper


def save_model(model_name):
    log.action(f"Saving current model notebook state on {time.ctime()}")

    cli_client = get_cli_client()
    local_config_helper = LocalConfigHelper()
    local_config_helper.check_local_config()

    local_config = local_config_helper.get_local_config()
    model_version_id = local_config["models"][model_name]["model_version_id"]
    model_version = cli_client.retrieve_model_version_by_id(
        model_version_id=model_version_id
    )

    cwd = Path.cwd()
    notebook_path = f"{cwd}/models/{model_name}/{model_version['name']}/notebook.ipynb"

    imports, trainer = parse_notebook(notebook_path)
    trainer_source = generate_trainer_from_template(
        model_name=model_name,
        imports=imports,
        trainer=trainer,
        model_version_id=model_version_id,
    )

    cwd = Path.cwd()
    with open(
        f"{cwd}/models/{model_name}/{model_version['name']}/trainer.py", "w"
    ) as f_out:
        f_out.write(trainer_source)

    log.action("Done.\n")
