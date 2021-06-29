import importlib.metadata
import os
import shlex
import shutil
import subprocess
import tempfile
from pathlib import Path

# BEFORE importing distutils, remove MANIFEST. distutils doesn't properly
# update it when the contents of directories change.
if os.path.exists('MANIFEST'):
    os.remove('MANIFEST')

from setuptools import Command
# Note: distutils must be imported after setuptools
from distutils import log
from setuptools.command.develop import develop as _develop
from wheel.bdist_wheel import bdist_wheel as _bdist_wheel


class build_extjs_sources(Command):
    user_options = []
    _docker_image = "diracgrid/dirac-distribution:latest"
    _available_exes = [
        "docker",
        "singularity",
    ]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def get_inputs(self):
        return []

    def get_outputs(self):
        return []

    def run(self):
        if "DIRAC_WEBAPP_NO_COMPILE" in os.environ:
            log.warn("Skipping webapp compilation as DIRAC_WEBAPP_NO_COMPILE is set")
            return

        cmd = self._cmd
        log.info('> %s', shlex.join(cmd))
        subprocess.check_call(cmd)

    @property
    def _pkg_name(self):
        if not hasattr(self, "__name"):
            packages = [x for x in self.distribution.packages if "." not in x]
            if len(packages) != 1:
                raise NotImplementedError(f"Failed to find the package name: {packages}")
            self.__name = packages[0]
        return self.__name

    @property
    def _path(self):
        return os.path.abspath(os.getcwd())

    @property
    def _cmd(self):
        for self._exe in self._available_exes:
            full_exe = shutil.which(self._exe)
            if full_exe is not None:
                break
        else:
            raise NotImplementedError("Unable to find a suitable command")

        cmd = [full_exe]
        cmd += getattr(self, f"_{self._exe}_args")
        cmd += ["-D=/opt", f"-n={self._pkg_name}", "--py3-style"]
        return cmd

    def _bind_mounts(self):
        for entrypoint in importlib.metadata.entry_points().get('dirac', []):
            if self._pkg_name == entrypoint.module:
                # Don't consider the current package
                continue
            metadata = entrypoint.load()()
            if metadata.get("web_resources", {}).get("static"):
                spec = importlib.util.find_spec(entrypoint.module)
                module_path = Path(spec.origin).parent
                log.info("Found WebApp module %s at %s", entrypoint.module, module_path)
                yield entrypoint.module, module_path

    @property
    def _docker_args(self):
        cmd = [
            "run",
            "--rm",
        ]
        for name, path in self._bind_mounts():
            cmd += [f"-v={path}:/opt/{name}:ro"]
        cmd += [f"-v={self._path}/src/{self._pkg_name}:/opt/{self._pkg_name}"]
        cmd += [
            "-w=/tmp",
            f"-u={os.getuid()}:{os.getgid()}",
            self._docker_image,
            "/dirac-webapp-compile.py",
        ]
        return cmd

    @property
    def _singularity_args(self):
        cmd = [
            "run",
            "--writable",
            "--containall",
        ]
        # In order to make a writable container with singularity bound
        # directories must already exist. To ensure this make a fake /opt
        # directory which contains the required folders and mount it before
        # any other bind mounts
        self._tmpdir = tempfile.TemporaryDirectory()
        tmpdir = Path(self._tmpdir.__enter__())
        cmd += [f"--bind={tmpdir}:/opt"]
        # Add any dependencies to the container
        for name, path in self._bind_mounts():
            (tmpdir / name).mkdir()
            cmd += [f"--bind={path}:/opt/{name}:ro"]
        # Add the current package to the container
        (tmpdir / self._pkg_name).mkdir()
        cmd += [f"--bind={self._path}/src/{self._pkg_name}:/opt/{self._pkg_name}"]
        # Add the remaining arguments
        cmd += [
            f"docker://{self._docker_image}",
            "/dirac-webapp-compile.py",
        ]
        return cmd


class develop(_develop):
    def run(self):
        self.run_command("build_extjs_sources")
        super().run()


class bdist_wheel(_bdist_wheel):
    def run(self):
        self.run_command("build_extjs_sources")
        super().run()


extjs_cmdclass = {
    "develop": develop,
    "bdist_wheel": bdist_wheel,
    "build_extjs_sources": build_extjs_sources,
}
