from .hyperdata_client import HyperdataHttpClient, HyperdataUserAuth
import os
import pathlib
from typing import List
import pandas as pd


class HyperdataApi:
    def __init__(self):
        self.client = HyperdataHttpClient(hd_addr=os.environ["hyperdata_addr"])
        self.auth = HyperdataUserAuth(
            project_id=os.environ["project_id"], user_id=os.environ["user_id"], token=os.environ["token"]
        )
        if "serving_mount_path" in os.environ:
            # shutil.rmtree(os.environ["mount_path"])
            os.makedirs(os.path.dirname(os.environ["mount_path"]), exist_ok=True)
            os.symlink(os.environ["serving_mount_path"], os.environ["mount_path"])
        else:
            os.makedirs(self.get_experiment_path(), exist_ok=True)
            os.makedirs(self.get_workflow_path(), exist_ok=True)
            if "inference_id" in os.environ:
                os.makedirs(self.get_inference_path(), exist_ok=True)

    def download_train_csv(self) -> str:
        return self._download_csv(do_id=int(os.environ["do_id"]), data_rootpath=self.get_experiment_path(),)

    def download_retrain_csv(self) -> str:
        return self.download_train_csv()

    def download_inference_csv(self) -> str:
        return self._download_csv(do_id=int(os.environ["do_id"]), data_rootpath=self.get_inference_path(),)

    def get_workflow_id(self) -> int:
        return int(os.environ["workflow_id"])

    def get_inference_id(self) -> int:
        return int(os.environ["inference_id"])

    def _download_csv(self, do_id: int, data_rootpath: str) -> str:
        result, sep, line_delim = self.client.download_do_to_csv(self.auth, do_id)

        pathlib.Path(data_rootpath).mkdir(parents=True, exist_ok=True)
        csv_path = os.path.join(data_rootpath, "%d.csv" % do_id)

        csv_str = result.data.decode("utf-8")
        if line_delim != "\n":
            csv_str.replace(line_delim, "\n")
        with open(csv_path, "w") as f:
            f.write(csv_str)

        if sep != ",":
            data = pd.read_csv(csv_path, sep=sep)
            data.to_csv(csv_path, sep=",", index=False)

        return csv_path

    def get_experiment_path(self) -> str:
        return os.path.join(os.environ["mount_path"], os.environ["experiment_id"])

    def get_workflow_path(self) -> str:
        return os.path.join(os.environ["mount_path"], os.environ["experiment_id"], os.environ["workflow_id"])

    def get_prev_workflow_paths(self) -> List[str]:
        return [
            os.path.join(self.get_experiment_path(), str(workflow_id))
            for workflow_id in range(1, self.get_workflow_id())
        ]

    def get_inference_path(self):
        return os.path.join(
            os.environ["mount_path"],
            os.environ["experiment_id"],
            os.environ["workflow_id"],
            os.environ["inference_id"],
        )
