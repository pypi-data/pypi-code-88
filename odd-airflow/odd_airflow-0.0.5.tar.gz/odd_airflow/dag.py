import requests
import sqlparse
from sqlparse.sql import T, TokenList, Parenthesis, Identifier, IdentifierList
from sqlparse.tokens import Punctuation
from pkg_resources import parse_version

import airflow.models
from airflow.version import version as AIRFLOW_VERSION

from .settings import CATALOG_URL
from .utils import *
from .oddrn.airflow import get_transformer_oddrn, get_transformer_run_oddrn

if parse_version(AIRFLOW_VERSION) >= parse_version("1.10.11"):
    from airflow import LoggingMixin
else:
    # Corrects path of import for Airflow versions below 1.10.11
    from airflow.utils.log.logging_mixin import LoggingMixin


class DAG(airflow.models.DAG, LoggingMixin):
    def create_dagrun(self, *args, **kwargs):
        self.log.debug(f"ODD create_dagrun")
        dagrun = super(DAG, self).create_dagrun(*args, **kwargs)
        data = []
        for task_id, task in self.task_dict.items():
            if hasattr(task, "sql"):
                data.extend([self._add_run(task, dagrun), self._add_transformer(task)])
        self._send_data(data)
        return dagrun

    def handle_callback(self, *args, **kwargs):
        self.log.debug(f"ODD handle_callback({args}, {kwargs})")
        try:
            dagrun = args[0]
            transformer_runs = []
            for task_id, task in self.task_dict.items():
                transformer_runs.append(self._add_run(task, dagrun))
            self._send_data(transformer_runs)
        except Exception as e:
            self.log.error(
                f'Failed to record dagrun callback: {e} '
                f'dag_id={self.dag_id}',
                exc_info=True
            )

        return super().handle_callback(*args)

    def _send_data(self, data):
        self.log.info(f"REQUEST DATA: {data}")
        r = requests.post(CATALOG_URL, json=data)
        if r.status_code == 200:
            self.log.error(f"Data transfer success")
        else:
            self.log.error(f"Error on catalog request. Code: {r.status_code}, Message: {r.text}")

    def _add_transformer(self, task) -> dict:
        sql_parser = Parser(task)
        dag = task.dag
        inputs, outputs = sql_parser.get_response()
        data = {
            "oddrn": get_transformer_oddrn(dag.dag_id, task.task_id),
            "name": get_transformer_name(dag.dag_id, task.task_id),
            "description": "desc",
            "owner": dag.owner,
            "data_transformer": {
                "source_code_url": "source",
                "sql": task.sql,
                "inputs": inputs,
                "outputs": outputs
            },
            "metadata": {}
        }
        return data

    def _add_run(self, task, dagrun) -> dict:
        dag = dagrun.dag
        data = {
            "oddrn": get_transformer_run_oddrn(dag.dag_id, task.task_id, dagrun.run_id),
            "name": get_transformer_run_name(dagrun.run_id, task.task_id),
            "description": "",
            "owner": dag.owner,
            "data_transformer_run": {
                "transformer_oddrn": get_transformer_oddrn(dag.dag_id, task.task_id),
                "start_time": dagrun.start_date,
                "end_time": dagrun.end_date,
                "status": "OTHER", # map status,
                "status_reason": "" # get status reason?
            },
            "metadata": {}
        }
        return data

