import requests
import json
import yaml
from .hyperdata_client import HyperdataHttpClient, HyperdataUserAuth
from time import sleep
import uuid


class PreCheck:
    def __init__(self, server_config_path: str, image_config_path: str):
        server_config = yaml.safe_load(open(server_config_path))
        image_config = yaml.safe_load(open(image_config_path))
        try:
            self.hyperdata_addr = server_config["hyperdata_addr"]
            self.automl_addr = server_config["automl_addr"]
            self.proauth_addr = server_config["proauth_addr"]
            self.user_id = server_config["user_id"]
            self.user_password = server_config["user_password"]
            self.project_name = server_config["project_name"]
            self.train_do_name = server_config["train_do_name"]
            self.inference_do_name = server_config["inference_do_name"]
        except KeyError as e:
            print(f'Cannot found "{str(e)}" in server_config.yaml')
            exit(1)

        try:
            self.train_input_columns = image_config["train"]["train_input_columns"]
            self.inference_input_columns = image_config["train"]["inference_input_columns"]
        except KeyError as e:
            print(f'Cannot found "{str(e)}" in image_config.yaml')
            exit(1)

        self.hyperdata_client = HyperdataHttpClient(self.hyperdata_addr)

    def _print_header(self, msg: str):
        print("#" * len(msg))
        print(msg)
        print("#" * len(msg))

    def _check_hyperdata_proauth_server_connect(self):
        self._print_header(f'check proauth server "{self.proauth_addr}" connection.')
        res = requests.post(
            url=self.proauth_addr + "/proauth/oauth/authenticate",
            headers={"Content-Type": "application/json;charset=UTF-8"},
            data=json.dumps({"user_id": self.user_id, "password": self.user_password}),
        )
        if res.status_code != 200:
            print(
                "cannot connect to %s. proauth server returns status code %d"
                % (self.proauth_addr, res.status_code)
            )
            raise Exception(res)

        self.access_token = json.loads(res.text)["token"]
        self.hyperdata_request_header = {"Authorization": self.access_token}
        print("check proauth server connection end.\n")

    def _check_hyperdata_project(self):
        self._print_header(f'check is hyperdata project "{self.project_name}" exist.')

        project_get_url = self.hyperdata_addr + "/hyperdata/web-service/projects"
        res = requests.get(project_get_url, headers=self.hyperdata_request_header)
        if res.status_code != 200:
            print(
                "cannot connect to %s. hyperdata server returns status code %d"
                % (self.hyperdata_addr, res.status_code)
            )
            raise Exception(res)

        project_infos = json.loads(res.text)["dto"]["project"]
        project_id = None
        for project_info in project_infos:
            if project_info["name"] == self.project_name:
                project_id = project_info["id"]
                break
        if project_id is None:
            print(f"Cannot found project {self.project_name}. Please check hyperdata.")
            raise Exception("_check_hyperdata_project failed.")
        else:
            self.project_id = project_id

        print("check hyperdata server connection end.\n")

    def _check_automl_server_connect(self):
        self._print_header(f'check automl server "{self.automl_addr}" connection.')
        res = requests.get(self.automl_addr)
        if res.status_code != 200:
            print(
                "cannot connect to %s. automl server returns status code %d"
                % (self.automl_addr, res.status_code)
            )
            raise Exception(res)
        self.automl_request_header = {
            "Project-Id": str(self.project_id),
            "Token": self.access_token,
            "User-Id": self.user_id,
        }
        print("check automl server connection end.\n")

    def _check_train_do_exist(self):
        self._print_header(f'check is train do "{self.train_do_name}" exist.')
        self.auth = HyperdataUserAuth(
            project_id=self.automl_request_header["Project-Id"],
            token=self.automl_request_header["Token"],
            user_id=self.automl_request_header["User-Id"],
        )
        res = self.hyperdata_client.get_do_list(self.auth)
        if res.status_code != 200:
            print(
                "cannot connect to %s. hyperdata server returns status code %d"
                % (self.hyperdata_addr, res.status_code)
            )
            raise Exception(res)

        result_data = res.data["dto"]["dataObjectInfoList"]
        for data in result_data:
            if data["name"] == self.train_do_name:
                res = self.hyperdata_client.get_do_detail_info(self.auth, data["id"])
                data_columns = [col_info["name"] for col_info in res.data["dto"]["colInfoList"]]
                if len(data_columns) == len(self.train_input_columns) and len(
                    list(set(data_columns) & set(self.train_input_columns))
                ) == len(data_columns):
                    print("check is train do exist end.\n")
                    self.train_do_id = data["id"]
                    return
                else:
                    print("train input columns are not matching with train_do.")
                    print(f"train input columns: {str(self.train_input_columns)}")
                    print(f"train do columns: {str(data_columns)}")
                    raise Exception()

        print(f"cannot found train do")
        exit(1)

    def _check_inference_do_exist(self):
        self._print_header(f'check is inference do "{self.inference_do_name}" exist.')
        res = self.hyperdata_client.get_do_list(self.auth)
        if res.status_code != 200:
            print(
                "cannot connect to %s. hyperdata server returns status code %d"
                % (self.hyperdata_addr, res.status_code)
            )
            raise Exception(res)

        result_data = res.data["dto"]["dataObjectInfoList"]
        for data in result_data:
            if data["name"] == self.inference_do_name:
                res = self.hyperdata_client.get_do_detail_info(self.auth, data["id"])
                data_columns = [col_info["name"] for col_info in res.data["dto"]["colInfoList"]]
                if len(data_columns) == len(self.inference_input_columns) and len(
                    list(set(data_columns) & set(self.inference_input_columns))
                ) == len(data_columns):
                    print("check is inference do exist end.\n")
                    self.inference_do_id = data["id"]
                    return
                else:
                    print("inference input columns are not matching with inference_do.")
                    print(f"inference input columns: {str(self.inference_input_columns)}")
                    print(f"inference do columns: {str(data_columns)}")
                    raise Exception()

        print(f"cannot found inference do")
        exit(1)

    def run(self):
        self._check_hyperdata_proauth_server_connect()
        self._check_hyperdata_project()
        self._check_automl_server_connect()
        self._check_train_do_exist()
        self._check_inference_do_exist()


class PredefinedAITemplateTest:
    def __init__(self, server_config_path: str, image_config_path: str):
        # replace test params
        server_config = yaml.safe_load(open(server_config_path))
        self.pre_check = PreCheck(server_config_path, image_config_path)
        self.pre_check.run()

        self.automl_addr = server_config["automl_addr"]
        self.proauth_addr = server_config["proauth_addr"]
        self.user_id = server_config["user_id"]
        self.user_password = server_config["user_password"]
        self.project_id = self.pre_check.project_id
        self.train_do_id = self.pre_check.train_do_id
        self.inference_do_id = self.pre_check.inference_do_id
        self.image_config = yaml.safe_load(open(image_config_path))
        self.experiment_id = None

    def _get_access_token(self):
        res = requests.post(
            url=self.proauth_addr + "/proauth/oauth/authenticate",
            headers={"Content-Type": "application/json;charset=UTF-8"},
            data=json.dumps({"user_id": self.user_id, "password": self.user_password}),
        )
        access_token = json.loads(res.text)["token"]
        self.request_header = {
            "Project-Id": str(self.project_id),
            "Token": access_token,
            "User-Id": self.user_id,
        }

    def _print_train_logs(self, experiment_id, workflow_id):
        self.pre_check._print_header("train log start")
        log_url = self.automl_addr + "/predefinedai/v2/log/train"
        log_url += "?experiment_id=" + str(experiment_id)
        log_url += "&workflow_id=" + str(workflow_id)
        res = requests.get(log_url, headers=self.request_header)
        logs = json.loads(res.text)
        for log in logs:
            print(f"##########{log['name']}##########")
            print(log["log"])
            print("\n")

    def _print_inference_logs(self, experiment_id, inference_id):
        self.pre_check._print_header("inference log start")
        log_url = self.automl_addr + "/predefinedai/v2/log/inference"
        log_url += "?experiment_id=" + str(experiment_id)
        log_url += "&inference_id=" + str(inference_id)
        res = requests.get(log_url, headers=self.request_header)
        print(res.text)
        logs = json.loads(res.text)
        for log in logs:
            print(f"##########{log['name']}##########")
            print(log["log"])
            print("\n")

    def _train(self):
        self.pre_check._print_header("train start")
        experiment_url = self.automl_addr + "/predefinedai/v2/experiments"
        create_experiment_data = self.image_config["train"]
        create_experiment_data["do_id"] = self.train_do_id
        """
        create_experiment_data = {
            "name": "experiment_sa_test21",
            "model": "Sentiment Analysis",
            "target_column": "sentiment",
            "metric": "accuracy",
            "do_id": self.train_do_id,
            # 사용할 데이터셋의 column 순서도 일치햐아 합니다.
            # ["id", "review"] (x), ["review", "id"] (o)
            "inference_input_columns": ["review", "id"],
            "inference_target_columns": ["review", "sentiment", "id"],
            "pipeline_image_info": {
                "name": "Sentiment Analysis",
                "task_type": "Sentiment Analysis",
                "image": "localhost:5000/hyperdata/sentimentanalysis_base:20210611_v1",
                "image_pull_policy": "Always",
                "cpu": "1",
                "memory": "1Gi",
                "gpu": "0",
                "working_dir": "/root/sentiment_analysis",
                "command": ["python", "train.py"],
                "args": {
                    "seed": 5,
                    "vocab-size": 25000,
                    "embedding-dim": 100,
                    "hidden-dim": 256,
                    "output-dim": 1,
                    "learning-rate": 1e-3,
                    "batch-size": 64,
                    "epoch": 5,
                },
                "envs": {},
            },
        }
        """
        create_experiment_data["name"] = create_experiment_data["model"] + "_" + str(uuid.uuid4())
        res = requests.get(experiment_url, headers=self.request_header)
        if res.status_code != 200:
            raise Exception(f"Get experiment info failed. " f"reason: {res.text}")

        print(f"experiment_name: {create_experiment_data['name']}")
        print(
            "send create experiment request to automl server. After creating experiments,"
            + "training will start."
        )
        res = requests.post(experiment_url, json=create_experiment_data, headers=self.request_header)
        if res.status_code != 200:
            raise Exception(f"create experiment failed. reason: {res.text}")
        else:
            print("wait until train finished.")

            # set experiment id for retraining
            self.experiment_id = json.loads(res.text)["experiment_id"]
            experiment_url_get = experiment_url + "?experiment_id=" + str(self.experiment_id)
            while True:
                res = requests.get(experiment_url_get, headers=self.request_header)
                experiment_info = json.loads(res.text)

                current_workflow_infos = experiment_info["workflows"][-1]
                if current_workflow_infos["status"] == "Failed":
                    self._print_train_logs(self.experiment_id, current_workflow_infos["id"])
                    raise Exception("train failed.")
                elif current_workflow_infos["status"] == "Succeeded":
                    break
                sleep(5)
            print("train succeeded.\n")

    # 재학습은 내부적으로 학습 시에 사용했던 DO와 같은 DO를 사용하도록 되어 있습니다.
    # 따라서 do_id를 전송하지 않습니다.
    def _retrain(self):
        self.pre_check._print_header("retrain start")
        experiment_url = self.automl_addr + "/predefinedai/v2/experiments"
        retrain_experiment_data = self.image_config["retrain"]
        retrain_experiment_data["experiment_id"] = self.experiment_id
        # retrain_experiment_data = {
        #    "experiment_id": self.experiment_id,
        # }
        # 덮어쓰기 가능한 목록
        # retrain_experiment_data = {
        #    "experiment_id": self.experiment_id,
        #    "pipeline_image_info": {
        #        "cpu": "2",
        #        "memory": "2Gi",
        #        "gpu": "0",
        #        "args": {
        #            "seed": 6
        #        },
        #        "envs": {}
        #    }
        # }
        print("send retrain experiment request to automl server.")
        res = requests.put(experiment_url, json=retrain_experiment_data, headers=self.request_header)
        if res.status_code != 200:
            raise Exception(f"retrain failed. reason: {res.text}")
        else:
            print("wait until retrain finished.")

            experiment_url_get = experiment_url + "?experiment_id=" + str(self.experiment_id)
            while True:
                res = requests.get(experiment_url_get, headers=self.request_header)
                if res.status_code != 200:
                    raise Exception(f"Get experiment info failed. " f"reason: {res.text}",)

                experiment_info = json.loads(res.text)
                current_workflow_infos = experiment_info["workflows"][-1]
                if current_workflow_infos["status"] == "Failed":
                    self._print_train_logs(self.experiment_id, current_workflow_infos["id"])
                    raise Exception("retrain failed.")
                elif current_workflow_infos["status"] == "Succeeded":
                    # set workflow info for next inference
                    self.workflow_id = current_workflow_infos["id"]
                    break
                sleep(5)
            print("retrain succeeded.\n")

    def _inference(self):
        self.pre_check._print_header("inference start")
        inference_url = self.automl_addr + "/predefinedai/v2/inferenceservice"
        inference_data = self.image_config["inference"]
        inference_data["experiment_id"] = self.experiment_id
        inference_data["workflow_id"] = self.workflow_id
        inference_data["input_do_id"] = self.inference_do_id
        inference_data["is_truncated"] = False
        # inference_data = {
        #    "experiment_id": self.experiment_id,
        #    "workflow_id": self.workflow_id,
        #    "input_do_id": self.inference_do_id,
        #    "is_truncated": True,
        # }
        # 덮어쓰기 가능한 목록
        # inference_data = {
        #    "experiment_id": self.experiment_id,
        #    "workflow_id": self.workflow_id,
        #    "input_do_id": self.inference_do_id,
        #    "is_truncated": True,
        #    "pipeline_image_info": {
        #        "cpu": "2",
        #        "memory": "2Gi",
        #        "gpu": "0",
        #        "args": {
        #            "seed": 7
        #        },
        #        "envs": {}
        #    }
        # }
        print("send inference request to automl server.")
        res = requests.post(inference_url, json=inference_data, headers=self.request_header)
        if res.status_code != 200:
            raise Exception(f"inference failed. reason: {res.text}")
        else:
            print("wait until inference finished.")

            self.inference_id = json.loads(res.text)["inference_id"]
            inference_url_get = (
                inference_url
                + "?experiment_id="
                + str(self.experiment_id)
                + "&inference_id="
                + str(self.inference_id)
            )
            while True:
                res = requests.get(inference_url_get, headers=self.request_header)
                if res.status_code != 200:
                    raise Exception(f"Get inference info failed. " f"reason: {res.text}")

                res_json = json.loads(res.text)
                inference_status = res_json["inference_status"]
                if inference_status == "Failed":
                    self._print_inference_logs(self.experiment_id, res_json["inference_id"])
                    raise Exception("inference failed.")
                elif inference_status == "Finished":
                    break
                sleep(5)
            print("inference succeeded.\n")

    def _inference_download(self):
        self.pre_check._print_header("inference download start")
        inference_download_url = self.automl_addr + "/predefinedai/v2/inferenceservice"
        inference_download_url += "?action=Download"
        inference_download_url += "&experiment_id=" + str(self.experiment_id)
        inference_download_url += "&inference_id=" + str(self.inference_id)
        res = requests.get(inference_download_url, headers=self.request_header, stream=True)
        if res.status_code == 200:
            print("inference download succeeded.\n")
        else:
            raise Exception(f"inference download failed. reason: {res.text}")

    def _serving(self):
        self.pre_check._print_header("serving start")
        serving_url = self.automl_addr + "/predefinedai/v2/serving"
        # kfserving works based on knative.
        # and knative uses docker image digest instead of tag
        # refer. https://knative.dev/docs/serving/tag-resolution/
        # https://docs.google.com/presentation/d/e/2PACX-1vTgyp2lGDsLr_bohx3Ym_2mrTcMoFfzzd6jocUXdmWQFdXydltnraDMoLxvEe6WY9pNPpUUvM-geJ-g/pub?resourcekey=0-FH5lN4C2sbURc_ds8XRHeA&slide=id.p
        # docker image digest can find using docker pull command.
        # --example--
        # user> docker pull 127.0.0.1:5000/hyperdata/sentimentanalysis_base:20210322_v1
        # 20210322_v1: Pulling from hyperdata/sentimentanalysis_base
        # Digest: sha256:40618baabd44864647460d43721dbf548a43e5b20406e66d58fafd11b3ac02c3
        # Status: Image is up to date for 127.0.0.1:5000/hyperdata/sentimentanalysis_base:20210322_v1
        # 127.0.0.1:5000/hyperdata/sentimentanalysis_base:2021-0322_v1
        serving_data = self.image_config["serving"]
        serving_data["experiment_id"] = self.experiment_id
        serving_data["workflow_id"] = self.workflow_id
        # serving_data = {
        #    "experiment_id": self.experiment_id,
        #    "workflow_id": self.workflow_id,
        # }
        # 덮어쓰기 가능한 목록
        # serving_data = {
        #    "experiment_id": self.experiment_id,
        #    "workflow_id": self.workflow_id,
        #    "serving_image_info": {
        #        "requests_cpu": "1",
        #        "limits_cpu": "2",
        #        "requests_memory": "1Gi",
        #        "limits_memory": "2Gi",
        #        "requests_gpu": "0",
        #        "limits_gpu": "0",
        #        "min_replicas": "1",
        #        "max_replicas": "1",
        #        "args": {},
        #        "envs": {},
        #    },
        # }
        print("send start serving server request to automl server.")
        res = requests.post(serving_url, json=serving_data, headers=self.request_header)
        if res.status_code != 200:
            raise Exception(f"serving failed. reason: {res.text}")
        else:
            print("wait until serving server is start.")
            while True:
                serving_url_get = (
                    serving_url
                    + "?experiment_id="
                    + str(self.experiment_id)
                    + "&workflow_id="
                    + str(self.workflow_id)
                )
                res = requests.get(serving_url_get, headers=self.request_header)
                if res.status_code not in [200, 503, 404]:
                    raise Exception(f"Get serving info failed. " f"reason: {res.text}")

                res_json = json.loads(res.text)
                if res_json["serve_status"] == "Possible":
                    service_host_name = res_json["service_host_name"]
                    url = res_json["url"]

                    # ref. https://github.com/kubeflow/kfserving/tree/release-0.4#test-kfserving-installation
                    # kfserving request header
                    headers = {"Host": service_host_name}
                    # kfserving input

                    result = self.pre_check.hyperdata_client.get_do_samples(
                        self.pre_check.auth, self.inference_do_id, 10
                    )
                    result_data = json.loads(result.data["dto"]["tableString"])
                    response_data = {
                        "columns": list(result_data[0].keys()),
                        "rows": [],
                    }
                    for data_dict in result_data:
                        response_data["rows"].append(list(map(str, list(data_dict.values()))))

                    request_json = {"instances": []}
                    for row in response_data["rows"]:
                        instance = {}
                        for idx, val in enumerate(row):
                            instance[response_data["columns"][idx]] = val
                        request_json["instances"].append(instance)
                    print("In test, serving uses inference input data as serving input data.")
                    print("serving_input_data: ", request_json)
                    try_cnt = 0
                    while try_cnt < 10:
                        res = requests.post(url, headers=headers, data=json.dumps(request_json))
                        if res.status_code == 200:
                            print("serving_output_data: ", res.text)
                            print("serving succeeded.")
                            return
                        sleep(5)
                        try_cnt += 1
                    raise Exception(f"serving failed. reason: {res.text}")
                sleep(5)

    def _delete_experiment(self):
        print("unittest finished.")
        if self.experiment_id is not None:
            print("delete experiment.")
            experiment_url = self.automl_addr + "/predefinedai/v2/experiments"
            delete_experiment_data = {"experiment_id": self.experiment_id}
            res = requests.delete(experiment_url, data=delete_experiment_data, headers=self.request_header)
            if res.status_code != 200:
                print(f"delete experiment failed. reason:{res.text}")

    def run(self):
        self._get_access_token()
        try:
            self._train()
            self._retrain()
            self._inference()
            self._inference_download()
            self._serving()
        except Exception as e:
            if self.experiment_id is not None:
                self._delete_experiment()
            raise e
