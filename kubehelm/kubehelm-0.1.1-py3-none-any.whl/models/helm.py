from json import loads as json_loads

from kubehelm.contexts import Context

from kubehelm.scripts import RunScript


class Helm(Context, RunScript):
    script_name = "helm.bash"
    chart_name = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        super().__init__(**kwargs)

    def get_args(self):
        assert self.chart_name
        return [
            self.cleaned_data["app_name"],
            self.cleaned_data["namespace"],
            self.chart_name]

    def as_dict(self, text):
        as_dict = json_loads(text)
        info = as_dict.get('info')
        return {
            'name': as_dict.get('name'),
            'namespace': as_dict.get('namespace'),
            'version': as_dict.get('version'),
            'first_deployed': info.get('first_deployed'),
            'last_deployed': info.get('last_deployed'),
            'description': info.get('description'),
            'status': info.get('status'),
            'deleted': info.get('deleted'),
        }

    def install(self, **kwargs):
        return self.as_dict(self.execute("install", **kwargs))

    def update(self, **kwargs):
        return self.as_dict(self.execute("update", **kwargs))

    def delete(self, **kwargs):
        return self.execute("delete", **kwargs)

    def execute(self, instruction, **kwargs):
        args = self.get_args()
        if kwargs.get("dry_run", None):
            args.append("--dry-run")
        getattr(self, "pre_%s" % instruction)()
        return self.run_script(instruction, *args)

    def pre_install(self, **kwargs):
        pass

    def pre_update(self, **kwargs):
        pass

    def pre_delete(self, **kwargs):
        pass
