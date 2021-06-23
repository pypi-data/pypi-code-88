from kubernetes.client.exceptions import ApiException
from kubernetes.client.models import V1ObjectMeta
from json import loads as json_loads


class ModelBase:
    apply_class = None
    update_class = None
    delete_class = None
    object_class = None
    spec_class = None
    namespace = None
    name = None
    component = None
    version = None
    managed_by = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def clean_error(self, error):
        body = json_loads(error.body)
        return "%s[%s]: %s" % (error.reason, error.status, body.get('message'))

    def get_labels(self):
        labels = {
            "app.kubernetes.io/name": self.name,
            "app.kubernetes.io/instance": self.name,
            "app.kubernetes.io/part-of": self.name,
        }
        if self.component:
            labels["app.kubernetes.io/component"] = self.component
        if self.version:
            labels["app.kubernetes.io/version"] = self.version
        if self.managed_by:
            labels["app.kubernetes.io/managed-by"] = self.managed_by
        return labels

    def get_metadata(self):
        return V1ObjectMeta(
            namespace=self.namespace,
            name=self.name,
            labels=self.get_labels())

    def get_spec(self):
        if self.spec_class:
            return self.spec_class()

    def get_object(self):
        if not self.object_class:
            raise NotImplementedError(
                'subclasses of ModelBase must set object_class attribute')
        return self.object_class(metadata=self.get_metadata(), spec=self.get_spec())

    def apply(self, dry_run=None):
        if not self.apply_class:
            raise NotImplementedError(
                'subclasses of ModelBase must set apply_class attribute before calling apply')
        try:
            return self.apply_class(self.namespace, self.get_object(), dry_run=dry_run)
        except ApiException as err:
            return self.clean_error(err)

    def update(self, dry_run=None):
        if not self.update_class:
            raise NotImplementedError(
                'subclasses of ModelBase must set update_class attribute before calling update')
        try:
            return self.update_class(self.name, self.namespace, self.get_object(), dry_run=dry_run)
        except ApiException as err:
            return self.clean_error(err)

    def delete(self, dry_run=None):
        if not self.delete_class:
            raise NotImplementedError(
                'subclasses of ModelBase must set delete_class attribute before calling delete')
        try:
            return self.delete_class(self.name, self.namespace, self.get_object(), dry_run=dry_run)
        except ApiException as err:
            return self.clean_error(err)
