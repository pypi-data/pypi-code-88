from kubernetes.client.api import AppsV1Api, CoreV1Api
from kubernetes.client.exceptions import ApiException
from kubernetes.client.models import V1Namespace

from .base import ModelBase


class Namespace(ModelBase):
    apply_class = CoreV1Api().create_namespace
    object_class = V1Namespace

    def apply(self, dry_run=None):
        try:
            self.apply_class(self.get_object(), dry_run=dry_run)
        except ApiException as err:
            return self.clean_error(err)


class ListK8sObjects:
    limit = 50
    timeout_seconds = 15
    namespace = None
    label_selector = None

    def __init__(self, namespace, label_selector=None):
        self.namespace = namespace
        label_selector = label_selector

    def filter(self, data):
        filtered_data = []
        items = data.to_dict()
        for obj in items.get('items'):
            filtered_data.append(obj["metadata"]["name"])
        return filtered_data

    def deployments(self, _continue=None):
        data = AppsV1Api().list_namespaced_deployment(
            self.namespace,
            limit=self.limit,
            _continue=_continue,
            timeout_seconds=self.timeout_seconds)
        return self.filter(data)

    def pods(self, _continue=None):
        data = CoreV1Api().list_namespaced_pod(
            self.namespace,
            limit=self.limit,
            _continue=_continue,
            timeout_seconds=self.timeout_seconds)
        return self.filter(data)
