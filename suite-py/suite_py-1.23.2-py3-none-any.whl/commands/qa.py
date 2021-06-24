# -*- coding: utf-8 -*-

import sys
import json
import copy

from rich.table import Table
from rich.console import Console
from suite_py.lib import logger
from suite_py.lib.handler import prompt_utils
from suite_py.lib.handler.qainit_handler import QainitHandler
from suite_py.lib.handler import git_handler as git
from suite_py.lib.handler.git_handler import GitHandler


class QA:
    def __init__(self, action, project, config, tokens, flags=None):
        self._action = action
        self._project = project
        self._flags = flags
        self._config = config
        self._tokens = tokens
        self._git = GitHandler(project, config)
        self._qainit = QainitHandler(project, config, tokens)

    def run(self):
        if self._action == "list":
            self._list()
        elif self._action == "create":
            self._create()
        elif self._action == "update":
            self._update()
        elif self._action == "delete":
            self._delete()
        elif self._action == "freeze":
            self._freeze()
        elif self._action == "unfreeze":
            self._unfreeze()
        elif self._action == "check":
            self._check()
        elif self._action == "describe":
            self._describe()
        elif self._action == "update-quota":
            self._update_quota()

    def _check(self):
        r = self._qainit.execute("GET", "/api/v1/user")
        logger.info(
            "Checking configuration. If there is an issue, check ~/.suite_py/config.yml file and execute: suite-py login"
        )
        logger.debug(json.dumps(r.json(), indent=2))

    def _list(self):
        # init empty table with column (useful for reset)
        empty_table = Table()
        empty_table.add_column("Name", style="purple")
        empty_table.add_column("Hash", style="green")
        empty_table.add_column("Card", style="white")
        empty_table.add_column("Created by", style="white")
        empty_table.add_column("Updated by", style="white")
        empty_table.add_column("Deleted by", style="white")
        empty_table.add_column("Status", style="white")
        table = copy.deepcopy(empty_table)
        console = Console()

        # add filtering
        filters = []
        status_values = '"created","creating","updated","updating","failed","frozen"'
        if len(self._flags["status"]) > 0:
            status_values = ",".join(
                [f'"{status}"' for status in self._flags["status"]]
            )
        filters.append(f"status=[{status_values}]")

        if self._flags["user"] is not None:
            filters.append(f"user={self._flags['user']}")

        if self._flags["card"] is not None:
            filters.append(f"card={self._flags['card']}")

        filters_string = "&".join(filters)

        # execute query with pagination and filtering
        page_number = 1
        while True:
            r = self._qainit.execute(
                "GET",
                f'/api/v1/qa?{filters_string}&page_size={self._config.qainit["table_size"]}&page={page_number}',
            )
            response = r.json()
            qa_list = response["list"]
            for qa in qa_list:
                table.add_row(
                    qa["name"],
                    qa["hash"],
                    qa["card"],
                    qa.get("created", {}).get("github_username", "/")
                    if qa["created"] is not None
                    else "/",
                    qa.get("updated", {}).get("github_username", "/")
                    if qa["updated"] is not None
                    else "/",
                    qa.get("deleted", {}).get("github_username", "/")
                    if qa["deleted"] is not None
                    else "/",
                    qa["status"],
                )
            console.print(table)

            # break conditions
            if response["page_number"] >= response["total_pages"]:
                break
            if not prompt_utils.ask_confirm(
                f"I found {response['total_entries']} results. Do you want to load a few more?",
                False,
            ):
                break
            page_number += 1
            # table reset
            table = copy.deepcopy(empty_table)

    def _describe(self):
        qa_hash = self._flags["qa_hash"]
        jsonify = self._flags["json"]

        r = self._qainit.execute(
            "GET",
            f"/api/v1/qa/{qa_hash}",
        )
        if jsonify:
            print(json.dumps(r.json(), sort_keys=True, indent=2))
        else:
            table = Table()
            table.add_column("Microservice", style="purple", no_wrap=True)
            table.add_column("Drone build")
            table.add_column("Branch", style="white")
            table.add_column("Status", style="white")

            dns_table = Table()
            dns_table.add_column("Name", style="purple", no_wrap=True)
            dns_table.add_column("Record", style="green")

            console = Console()

            try:
                resources_list = sorted(
                    r.json()["list"]["resources"], key=lambda k: k["name"]
                )
                for resource in resources_list:
                    if (
                        resource["type"] == "microservice"
                        or "service" in resource["name"]
                    ) and resource["dns"]:
                        for key, value in resource["dns"].items():
                            dns_table.add_row(key, value)
                    if resource["type"] == "microservice":
                        drone_url = (
                            "[blue][u]"
                            + "https://drone-1.prima.it/primait/"
                            + resource["name"]
                            + "/"
                            + resource["promoted_build"]
                            + "[/u][/blue]"
                        )
                        table.add_row(
                            resource["name"],
                            drone_url,
                            resource["ref"]
                            if resource["ref"] == "master"
                            else f"[green]{resource['ref']}[/green]",
                            resource["status"],
                        )

                console.print(dns_table)
                console.print(table)
            except TypeError:
                logger.error("Wrong hash")

    def _delete(self):
        qa_hash = self._flags

        r = self._qainit.execute(
            "DELETE",
            f"/api/v1/qa/{qa_hash}",
        )
        logger.info("QA deletion initiated")
        logger.debug(json.dumps(r.json(), indent=2))

    def _freeze(self):
        qa_hash = self._flags

        body = {"operation": "freeze"}
        logger.debug(json.dumps(body))
        r = self._qainit.execute("PUT", f"/api/v1/qa/{qa_hash}", body=json.dumps(body))
        logger.info("QA freezing initiated")
        logger.debug(json.dumps(r.json(), indent=2))

    def _unfreeze(self):
        qa_hash = self._flags

        body = {"operation": "unfreeze"}
        logger.debug(json.dumps(body))
        r = self._qainit.execute("PUT", f"/api/v1/qa/{qa_hash}", body=json.dumps(body))
        logger.info("QA unfreezing initiated")
        logger.debug(json.dumps(r.json(), indent=2))

    def _create(self):
        r = self._qainit.execute("GET", "/api/v1/user")
        r = r.json()
        if not r["quota"]["remaining"] > 0:
            logger.error("There's no remaining quota for you.")
            sys.exit("-1")
        if "staging" in self._qainit.url:
            qa_default_name = (
                f"staging_{git.get_username()}_{self._git.current_branch_name()}"
            )
        else:
            qa_default_name = f"{git.get_username()}_{self._git.current_branch_name()}"

        qa_name = prompt_utils.ask_questions_input(
            "Choose the QA name: ", default_text=qa_default_name
        )

        qa_card = prompt_utils.ask_questions_input(
            "Youtrack issue ID: ", default_text=""
        )

        srv_list = self._qainit.create_services_body(prj_list=self._flags)

        body = {"name": qa_name, "card": qa_card, "services": srv_list}
        logger.debug(json.dumps(body))
        r = self._qainit.execute(
            "POST",
            "/api/v1/qa",
            body=json.dumps(body),
        )
        logger.info(f"QA creation initiated. Your namespace hash: {r.json()['hash']}")
        logger.debug(json.dumps(r.json(), indent=2))

    def _update(self):
        qa_hash = self._flags[0]
        prj_list = self._flags[1:]

        srv_list = self._qainit.create_services_body(prj_list)

        body = {"services": srv_list}
        logger.debug(json.dumps(body))
        r = self._qainit.execute(
            "PUT",
            f"/api/v1/qa/{qa_hash}",
            body=json.dumps(body),
        )
        logger.info("QA update initiated")
        logger.debug(json.dumps(r.json(), indent=2))

    def _update_quota(self):
        username = prompt_utils.ask_questions_input("Insert GitHub username: ")
        quota = prompt_utils.ask_questions_input("Insert new quota value: ")

        body = {"github_username": f"{username}", "quota": f"{quota}"}
        logger.debug(json.dumps(body))
        r = self._qainit.execute(
            "POST",
            "/api/v1/user/quota",
            body=json.dumps(body),
        )

        logger.info("Quota updated.")
        logger.debug(json.dumps(r.json(), indent=2))
