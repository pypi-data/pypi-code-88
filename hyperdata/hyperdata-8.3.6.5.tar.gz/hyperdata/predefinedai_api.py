from .hyperdata_api import HyperdataApi
import os
import requests
from typing import Dict
import json
import pandas as pd


class PredefinedAIApi:
    def __init__(self):
        if not os.environ["webserver_addr"]:
            self.is_local = True
        else:
            self.is_local = False
            self.hd_api = HyperdataApi()

            self.server_addr = os.path.join(os.environ["webserver_addr"], "predefinedai", "v2")
            self.headers = {
                "Content-Type": "application/json",
                "Project-Id": os.environ["project_id"],
                "Token": os.environ["token"],
                "User-Id": os.environ["user_id"],
            }

    def get_model_infos(self):
        if not self.is_local:
            res = requests.get(
                os.path.join(
                    self.server_addr, "model", "?experiment_id=" + str(os.environ["experiment_id"]),
                ),
                headers=self.headers,
                verify=False,
            )
            return json.loads(res.text)

    def insert_model_info(
        self, model_name: str, algorithm: str, metric: str, metric_result: str, model_json: Dict,
    ) -> Dict:
        if not self.is_local:
            input_json = {
                "experiment_id": os.environ["experiment_id"],
                "workflow_id": os.environ["workflow_id"],
                "model_name": model_name,
                "algorithm": algorithm,
                "metric": metric,
                "metric_result": metric_result,
                "model_json": json.dumps(model_json),
            }
            res = requests.post(
                os.path.join(self.server_addr, "models"),
                headers=self.headers,
                data=json.dumps(input_json),
                verify=False,
            )
            if res.status_code != 200:
                raise Exception(f"status code {res.status_code} failed. {res.text}")
            return json.loads(res.text)
        else:
            print("Current mode is local, Do Nothing.")

    def insert_visualizations(self, model_id: int, type: str, result: str) -> None:
        if not self.is_local:
            input_json = {
                "experiment_id": os.environ["experiment_id"],
                "model_id": model_id,
                "type": type,
                "result": result,
            }
            res = requests.post(
                os.path.join(self.server_addr, "visualization"),
                headers=self.headers,
                data=json.dumps(input_json),
                verify=False,
            )
            if res.status_code != 200:
                raise Exception(f"status code {res.status_code} failed. {res.text}")
        else:
            print("Current mode is local, Do Nothing.")

    def get_inference_csv_path(self):
        if not self.is_local:
            return os.path.join(self.hd_api.get_inference_path(), "inference.csv")
        else:
            print("Current mode is local, Do Nothing")
            return ""

    def upload_inference_csv(self):
        if not self.is_local:
            if int(os.environ["target_do_id"]) == 0:
                print("target do id not selected. skip upload inference csv")
                return

            df = pd.read_csv(self.get_inference_csv_path(), index=False)
            df_json = df.to_json(orient="split")

            inf_data = {
                "columns": df_json["columns"],
                "data": df_json["data"],
                "experiment_id": os.environ["experiment_id"],
                "target_do_id": os.environ["target_do_id"],
                "is_truncated": os.environ["is_truncated"],
            }
            res = requests.post(
                url=os.path.join(self.server_addr, "inference"),
                headers=self.headers,
                data=json.dumps(inf_data),
                verify=False,
            )
            if res.status_code != 200:
                raise Exception(f"status code {res.status_code} failed. {res.text}")
        else:
            print("Current mode is local, Do Nothing")
            return ""
