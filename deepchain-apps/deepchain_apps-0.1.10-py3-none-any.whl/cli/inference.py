"""deploy modules helps for the deployment of application on deepchain"""
import json
from argparse import ArgumentParser

import requests
from deepchain import log
from deepchain.cli import BaseCLICommand
from deepchain.cli.cli_utils import get_config_url

from .apps_utils import get_configuration


def inference_command_factory(args):
    return InferenceCommand(args.action, args.sequences_file, args.result_id)


class InferenceCommand(BaseCLICommand):
    def __init__(self, action: str, sequences_file: str, result_id: str):
        self.sequences_file = sequences_file
        self.action = action
        self.result_id = result_id

    @staticmethod
    def register_subcommand(parser: ArgumentParser) -> None:
        inference_parser = parser.add_parser(name="inference", help="run inference on DeepChain ")
        inference_parser.add_argument(
            "action",
            action="store",
            type=str,
            help='"run" for  running a new sequences inference  or "download" for downloading embeddings',
            choices=["download", "run"],
        )
        inference_parser.add_argument(
            "-f",
            "--sequences_file",
            action="store",
            type=str,
            help="json file with all sequences ",
        )
        inference_parser.add_argument(
            "-r",
            "--result_id",
            action="store",
            type=str,
            help="result reference",
        )

        inference_parser.set_defaults(func=inference_command_factory)

    def run(self) -> None:
        """
        run inference
        """
        url = get_config_url()
        configuration = get_configuration()
        pat = configuration["pat"]
        if self.action == "run":
            self.run_inference(url, pat)
        elif self.action == "download":
            self.download(url, pat, self.result_id)

    @staticmethod
    def download(base_url: str, pat: str, result_id: str) -> None:
        result = requests.get(
            url=f"{base_url}/apps/xxx/embedding-inferences/{result_id}/download-url",
            headers={"authorisation": pat},
        )
        if result.status_code >= 300:
            log.debug(result.content)
            exit(-1)
        result = requests.get(result.content)
        if result.status_code >= 300:
            log.debug("%s:%s" % (result.status_code, result.content))
            exit(1)
        file = open(f"{result_id}.npy", "wb")
        file.write(result.content)
        file.close()

    def run_inference(self, base_url: str, pat: str) -> None:
        selected_model = self.select_model(base_url)
        result = requests.post(
            url=f"{base_url}/apps/xxx/embedding-inferences",
            headers={"authorisation": pat},
            data={"model-name": selected_model},
            files={"file": open(self.sequences_file, "rb")},
        )
        if result.status_code >= 300:
            log.debug(result.content)
            log.error("Error when uploading sequence file.")
        else:
            log.info("Inference started, you will be notified by email when embeddings are ready.")

    @staticmethod
    def select_model(base_url) -> str:
        models = [
            {"id": str(i), "name": m}
            for i, m in enumerate(InferenceCommand.fetch_available_models(base_url))
        ]
        s = "\n".join([f"{m['id']} for \t{m['name']}" for m in models])

        selected_model = input(f"Please select from this available models:\n{s}\n")
        while selected_model not in [m["id"] for m in models]:
            selected_model = input(f"Please select from this available models:\n{s}\n")
        return list(filter(lambda m: m["id"] == selected_model, models))[0]["name"]

    @staticmethod
    def fetch_available_models(base_url: str):
        result = requests.get(url=f"{base_url}/inference-models")
        if result.status_code >= 300:
            log.debug(result.content)
            log.warning("Error occurred")
            exit(1)
        models = json.loads(result.content)
        return models
