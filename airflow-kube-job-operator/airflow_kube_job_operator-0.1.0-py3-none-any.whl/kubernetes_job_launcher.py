import time
import logging
import tenacity
from kubernetes.client.rest import ApiException

# https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/BatchV1Api.md

from airflow_kjo.kubernetes_util import (
    get_kube_client,
    get_kube_job_client,
    get_kube_pod_client,
)


class KubernetesJobLauncherPodError(Exception):
    """
    Created Job ended in an errored pod state
    """

    pass


class KubeYamlValidationError(Exception):
    pass


class KubernetesJobLauncher:
    def __init__(
        self,
        kube_client=None,
        in_cluster=True,
        cluster_context=None,
        config_file=None,
        tail_logs_every=None,
        tail_logs_line_count=100,
        tail_logs_only_at_end=False,
    ):
        self.kube_client = kube_client or get_kube_client(
            in_cluster=in_cluster,
            cluster_context=cluster_context,
            config_file=config_file,
        )

        self.kube_job_client = get_kube_job_client(self.kube_client)
        self.kube_pod_client = get_kube_pod_client(self.kube_client)
        self.sleep_time = 5
        self.tail_logs_every = tail_logs_every
        self.tail_logs_line_count = tail_logs_line_count
        self.tail_logs_only_at_end = tail_logs_only_at_end

    @staticmethod
    def _validate_job_yaml(yaml_obj):
        """
        Ensure that the yaml obj passes some requirements,
        !. must have a name and namespace field in metadata block
        """
        try:
            metadata = yaml_obj["metadata"]
            metadata["name"]
            metadata["namespace"]
        except KeyError as error:
            raise KubeYamlValidationError(f"Kube yaml must include a {error}")

    def _get_name_namespace(self, yaml_obj):
        self._validate_job_yaml(yaml_obj)
        return yaml_obj["metadata"]["name"], yaml_obj["metadata"]["namespace"]

    def _tail_pod_logs(self, name, namespace, job):
        had_logs = False
        num_lines = self.tail_logs_line_count
        # can only get a log if pod is in one of these states
        logable_statuses = {"Running", "Failed", "Succeeded"}
        # get all pods for the job
        job_pods = self.kube_pod_client.list_namespaced_pod(
            namespace=namespace, label_selector=f"job-name={name}"
        )
        for pod in job_pods.items:
            pod_name = pod.metadata.name
            # only continue if pod is running, completed or errored
            pod_phase = pod.status.phase
            if pod_phase not in logable_statuses:
                continue
            # TODO should see if can use since_seconds in a good way
            # https://raw.githubusercontent.com/kubernetes-client/python/master/kubernetes/client/api/core_v1_api.py
            if bool(num_lines):
                read_log = self.kube_pod_client.read_namespaced_pod_log(
                    name=pod_name, namespace=namespace, tail_lines=num_lines
                )
                line_or_lines = "line" if num_lines == 1 else "lines"
                msg = f'Reading last {num_lines} {line_or_lines} from log for Pod "{pod_name}" in Namespace "{namespace}"'
            else:
                msg = f'Reading full logfile for Pod "{pod_name}" in Namespace "{namespace}"'
                # could this ever be too much data?
                read_log = self.kube_pod_client.read_namespaced_pod_log(
                    name=pod_name, namespace=namespace
                )
            lines = [line for line in read_log]
            str_lines = "".join(lines).strip()
            if str_lines:
                logging.info(msg)
                logging.info(f"Reading....\n{str_lines}")
                logging.info(f'End log for Pod "{pod_name}" in Namespace "{namespace}"')
                had_logs = True
        return had_logs

    @tenacity.retry(
        stop=tenacity.stop_after_attempt(3),
        wait=tenacity.wait_random_exponential(),
        reraise=True,
    )
    def apply(self, yaml_obj):
        self._validate_job_yaml(yaml_obj)
        _, namespace = self._get_name_namespace(yaml_obj)
        try:
            self.kube_job_client.create_namespaced_job(
                namespace=namespace, body=yaml_obj
            )
        except ApiException as error:
            return error.status == 409
        return True

    def watch(self, yaml_obj, running_timeout=None):
        name, namespace = self._get_name_namespace(yaml_obj)
        total_time = 0
        log_cycles = 1
        while True:
            job = self.kube_job_client.read_namespaced_job_status(
                name=name, namespace=namespace
            )
            completed = bool(job.status.succeeded)
            if completed:
                if bool(self.tail_logs_every) or self.tail_logs_only_at_end:
                    logging.info(f'Final log output for Job "{name}"')
                    self._tail_pod_logs(name, namespace, job)
                logging.info(f'Job "{name}" status is Completed')
                return True
            if running_timeout and total_time > running_timeout:
                pass  # running timeout exceeded, probably just a warning, would allow task to continue

            if bool(job.status.failed):
                if bool(self.tail_logs_every) or self.tail_logs_only_at_end:
                    self._tail_pod_logs(name, namespace, job)
                raise KubernetesJobLauncherPodError(
                    f'Job "{name}" in Namespace "{namespace}" ended in Error state'
                )
            if bool(self.tail_logs_every) and not self.tail_logs_only_at_end:
                if (
                    total_time > 0
                    and total_time % (self.tail_logs_every // self.sleep_time) == 0
                ):
                    logging.info(f"Beginning new log dump cycle :: {log_cycles}")
                    had_logs = self._tail_pod_logs(name, namespace, job)
                    no_logs_msg = (
                        ", no logs found to output this cycle" if not had_logs else ""
                    )
                    logging.info(f"Log dump cycle {log_cycles} complete{no_logs_msg}")
                    log_cycles += 1

            time.sleep(self.sleep_time)
            total_time += self.sleep_time

    def delete(self, yaml_obj):
        name, namespace = self._get_name_namespace(yaml_obj)
        self.kube_job_client.delete_namespaced_job(
            name=name, namespace=namespace, propagation_policy="Foreground"
        )
        return True
