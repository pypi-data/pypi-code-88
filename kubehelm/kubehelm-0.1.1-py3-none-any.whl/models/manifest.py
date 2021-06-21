from yaml import safe_load_all

from kubehelm.contexts import Context, Template

from .mixin import APIFunctionsMixin


class Manifest(APIFunctionsMixin, Context, Template):

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        super().__init__(**kwargs)

    def get_manifest_as_list(self):
        data = self.render(self.cleaned_data)
        manifest = list(safe_load_all(data))
        return [obj for obj in manifest if obj.get("kind") != "Namespace"]

    def install(self, dry_run=False):
        return self.execute("create", self.get_manifest_as_list(), dry_run=dry_run)

    def update(self, dry_run=False):
        return self.execute("patch", self.get_manifest_as_list(), dry_run=dry_run)

    def delete(self, dry_run=False):
        return self.execute("delete", self.get_manifest_as_list(), dry_run=dry_run)
