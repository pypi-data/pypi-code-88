# -*- encoding: utf-8 -*-
import sys
import requests

from github.GithubException import UnknownObjectException
from halo import Halo
from suite_py.lib.handler.github_handler import GithubHandler
from suite_py.lib.handler.git_handler import GitHandler
from suite_py.lib.handler import prompt_utils
from suite_py.lib import logger


class QainitHandler:

    scope_mapping = {
        "admin": [
            "update:user-quota",
            "delete:others-qa",
            "create:qa",
            "delete:qa",
            "describe:qa",
            "describe:others-qa",
            "update:qa",
            "update:others-qa",
            "list:qa",
            "list:others-qa",
        ],
        "dev": [
            "create:qa",
            "delete:qa",
            "describe:qa",
            "describe:others-qa",
            "update:qa",
            "update:others-qa",
            "list:qa",
            "list:others-qa",
        ],
        "external": ["create:qa", "delete:qa", "describe:qa", "list:qa", "update:qa"],
    }

    def __init__(self, project, config, tokens):
        self._project = project
        self._token = tokens.drone
        self._config = config
        self.url = self._config.qainit["url"]
        self.auth0_token = self._config.get_cache("auth0_token")
        self._github = GithubHandler(tokens)
        self._git = GitHandler(project, config)

        if "url" not in config.qainit:
            self.usage()
            sys.exit(-1)

    def usage(self):
        logger.warning(
            "Unable to use QA commands: missing qainit config in ~/.suite_py/config.yml"
        )
        logger.warning(
            "Update your config.yml as: https://github.com/primait/suite_py/blob/master/.config.yml.dist"
        )

    def create_services_body(self, prj_list):
        srv_list = []
        ref = self._git.current_branch_name()
        for prj in prj_list:
            with Halo(text="Loading branches...", spinner="dots", color="magenta"):
                choices = [
                    {"name": branch.name, "value": branch.name}
                    for branch in self._github.get_branches(prj)
                ]
            if choices:
                choices.sort(key=lambda x: x["name"])
                ref = prompt_utils.ask_choices(
                    f"Select branch for project - {prj}: ", choices, default_text=ref
                )
            try:
                self._github.get_raw_content(prj, ref, ".service.yml")
            except UnknownObjectException:
                logger.error(
                    f".service.yml missing for project: {prj}, can't add microservice to QA"
                )
                sys.exit(-1)
            srv_list.append(
                {
                    "name": prj,
                    "ref": ref,
                }
            )

        return srv_list

    def execute(self, request_method, api_endpoint, body=None):
        api_url = self.url + api_endpoint
        auth0_token = self._config.get_cache("auth0_token")

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + auth0_token,
        }
        logger.debug(request_method)
        logger.debug(api_url)
        logger.debug(headers)
        logger.debug(body)
        r = requests.request(request_method, api_url, headers=headers, data=body)

        if 200 <= r.status_code <= 299:
            logger.debug("Call to qainit-evo executed successfully")
        else:
            logger.error("Some issue during call to qainit-evo: ")
            logger.error(f"Status code: {r.status_code}, response: {r.text}")
            logger.error(api_endpoint)
            sys.exit(-1)

        return r
