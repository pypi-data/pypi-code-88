import logging
from typing import Any, AnyStr, Dict, Optional
from urllib.parse import urljoin

import requests

from ruleau.decorators import api_request
from ruleau.exceptions import APIException
from ruleau.process import Process
from ruleau.rule import Rule

logger = logging.getLogger(__name__)


class ApiAdapter:
    base_url: AnyStr
    base_path: AnyStr
    api_key: Optional[AnyStr]

    def __init__(
        self,
        base_url: AnyStr,
        api_key: Optional[AnyStr] = None,
    ):
        """
        :param base_url: Base URL of the ruleau API
        :param api_key: (Optional) API key to authenticate with the API
        """
        self.base_url = base_url
        self.base_path = "/api/v1/"
        self.api_key = api_key

    @api_request
    def sync_case(self, case_id: AnyStr, process_id: AnyStr, payload: Dict) -> Dict:
        """
        Synchronise case with API
        :param case_id: The ID of the case being executed
        :param process_id: The ID of the process
        :param payload: Case payload to execute on
        :return:
        """
        response = requests.get(
            urljoin(
                self.base_url, f"{self.base_path}processes/{process_id}/cases/{case_id}"
            )
        )

        if response.status_code == 200:
            response = requests.patch(
                urljoin(
                    self.base_url,
                    f"{self.base_path}processes/{process_id}/cases/{case_id}",
                ),
                json={
                    "id": case_id,
                    "payload": payload,
                    "status": "OPEN",
                },
            )
            if response.status_code != 200:
                raise APIException(f"Failed to update case: {response.text}")

        elif response.status_code == 404:
            response = requests.post(
                urljoin(self.base_url, f"{self.base_path}processes/{process_id}/cases"),
                json={
                    "id": case_id,
                    "payload": payload,
                    "process": process_id,
                    "status": "OPEN",
                },
            )
            if response.status_code != 201:
                raise APIException(f"Failed to create case: {response.text}")

        else:
            raise APIException(f"Failed to check case: {response.text}")

        return response.json()

    @api_request
    def sync_process(self, process: Process):
        response = requests.post(
            urljoin(self.base_url, f"{self.base_path}processes"),
            json=process.parse(),
        )

        if response.status_code != 201:
            raise APIException(f"Unable to save rules: {response.text}")

        return response.json()

    @api_request
    def create_result(
        self,
        case_id: AnyStr,
        rule: Rule,
        process: Process,
    ) -> Dict:
        """
        Update rule result after its execution
        :param case_id: The ID of the case being executed
        :param rule: The Rule object that the result relates to
        :param process: The Process object that the rule is a child of
        :return:
        """
        # Update the rule results
        response = requests.post(
            urljoin(
                self.base_url,
                f"{self.base_path}processes/{process.id}/cases/"
                f"{case_id}/rules/{rule.id}/results",
            )
        )
        if response.status_code != 201:
            raise APIException(
                f"Failed to create result {case_id}@{rule.id}: {response.text}"
            )
        return response.json()

    @api_request
    def update_result(
        self,
        case_id: AnyStr,
        rule: Rule,
        api_result: Dict[AnyStr, Any],
        execution_result: "ExecutionResult",  # noqa: F821
    ) -> Dict:
        """
        Update rule result after its execution
        :param case_id:
        :param rule:
        :param api_result:
        :param execution_result:
        :return:
        """
        # Update the rule results
        response = requests.patch(
            urljoin(
                self.base_url,
                f"{self.base_path}processes/{execution_result.process.id}/cases/"
                f"{case_id}/rules/{rule.id}/results/{api_result['id']}",
            ),
            json={
                "result": execution_result.result,
                "payload": execution_result.payload.accessed,
                "override": execution_result.override,
                "original_result": execution_result.original_result,
            },
        )
        if response.status_code != 200:
            raise APIException(
                f"Failed to store rule result {case_id}@{rule.id}: {response.text}"
            )
        return response.json()

    @api_request
    def fetch_override(
        self, case_id: AnyStr, process_id: AnyStr, rule_id: AnyStr
    ) -> Optional[Dict[AnyStr, Any]]:
        """
        Fetch rule overrides
        :param case_id: client ID that identifies a previously established case
        :param process_id: The ID of the process that the case is being run against
        :param rule_id: The ID of the Rule to fetch overrides for
        :return: a ruleau overrides Optional[Dict[AnyStr, Any]]
        """
        response = requests.get(
            urljoin(
                self.base_url,
                f"{self.base_path}processes/{process_id}/"
                f"cases/{case_id}/overrides/search",
            ),
            params={"rule_id": rule_id},
        )
        if response.status_code != 200:
            return {}
        return response.json()
