from subprocess import run, PIPE

from kubehelm import settings


class RunScript:
    scripts_base_path = settings.BASE_DIR / "scripts"
    script_name = None

    def run_script(self, *args):
        assert self.script_name
        path = "%s/%s" % (self.scripts_base_path, self.script_name)
        script = "%s %s %s" % (path, settings.BASE_DIR, " ".join(args))
        sub_pro = run([script], shell=True, stdout=PIPE, stderr=PIPE)
        if sub_pro.stderr:
            raise RunScriptError(sub_pro.stderr.decode())
        return sub_pro.stdout.decode()


class RunAppScript(RunScript):
    allowed_methods = ["install", "update", "delete"]

    def __init__(self, **kwargs):
        pass

    def install(self):
        if "install" in self.allowed_methods:
            return self.run_script("install")

    def update(self, *args):
        if "update" in self.allowed_methods:
            return self.run_script("update")

    def delete(self, *args):
        if "delete" in self.allowed_methods:
            return self.run_script("delete")


class RunScriptError(SyntaxError):
    pass
