from __future__ import absolute_import, division, print_function

import os
import re
import shutil
import subprocess
import sys
from typing import List
import zipfile

from setuptools import Distribution, find_packages, setup
from setuptools.command.develop import develop
from setuptools.command.install import install
from setuptools.command.sdist import sdist as sdist_orig


# mypy: ignore-errors


def find_version(path):
    with open(path) as f:
        match = re.search(
            r"^__version__ = ['\"]([^'\"]*)['\"]", f.read(), re.MULTILINE,
        )
        if match:
            return match.group(1)
        raise RuntimeError("Unable to find version string.")


def move_file(filename):
    # TODO(rkn): This feels very brittle. It may not handle all cases. See
    # https://github.com/apache/arrow/blob/master/python/setup.py for an
    # example.
    source = filename

    destination = os.path.join(os.path.dirname(__file__), filename)
    # Create the target directory if it doesn't already exist.
    parent_directory = os.path.dirname(destination)
    if not os.path.exists(parent_directory):
        os.makedirs(parent_directory)
    if not os.path.exists(destination):
        print("Copying {} to {}.".format(source, destination))
        shutil.copy(source, destination, follow_symlinks=True)


def download_and_copy_files(url: str, files_to_copy: List[str]) -> None:
    """
    Downloads an archive from S3, unzips it and then copies the file to the anyscale folder.
    """
    import io
    import tempfile

    import requests

    work_dir = tempfile.mkdtemp()
    try:
        content = requests.get(url).content
        archive = zipfile.ZipFile(io.BytesIO(content))
        archive.extractall(pwd=work_dir.encode())
        for f in files_to_copy:
            destination = os.path.join("anyscale", f)
            # Remove the file if it already exists to make sure old
            # versions get removed.
            try:
                os.remove(destination)
            except OSError:
                pass
            shutil.copy2(f, destination)
            os.chmod(destination, 0o755)
            move_file(destination)
    finally:
        shutil.rmtree(work_dir)


def download_and_copy_fswatch():
    download_and_copy_files(
        "https://anyscale-dev.s3-us-west-2.amazonaws.com/fswatch-1.14.0-2.zip",
        ["fswatch-linux", "fswatch-darwin", "libfswatch.11.dylib"],
    )


class SdistCommand(sdist_orig):
    def run(self):
        download_and_copy_fswatch()
        # run original sdist
        super().run()


class BinaryDistribution(Distribution):
    def is_pure(self):
        return True

    def has_ext_modules(self):
        return True


RAY_VERSION = "1.4.0"
RAY_RELEASED_COMMIT = "3a09c82fbfce8f00533234844729e6d99fb0f24c"
COMMON_RAY_PREFIX = (
    "https://s3-us-west-2.amazonaws.com/ray-wheels/releases/"
    f"{RAY_VERSION}/{RAY_RELEASED_COMMIT}/"
    f"ray-{RAY_VERSION}"
)
# NOTE The suffix should begin with '-' (i.e. -cp38)

RAY_WHEELS = {
    "linux": {
        "3.8": f"{COMMON_RAY_PREFIX}-cp38-cp38-manylinux2014_x86_64.whl",
        "3.7": f"{COMMON_RAY_PREFIX}-cp37-cp37m-manylinux2014_x86_64.whl",
        "3.6": f"{COMMON_RAY_PREFIX}-cp36-cp36m-manylinux2014_x86_64.whl",
    },
    "darwin": {
        "3.8": f"{COMMON_RAY_PREFIX}-cp38-cp38-macosx_10_13_x86_64.whl",
        "3.7": f"{COMMON_RAY_PREFIX}-cp37-cp37m-macosx_10_13_intel.whl",
        "3.6": f"{COMMON_RAY_PREFIX}-cp36-cp36m-macosx_10_13_intel.whl",
    },
    "win32": {
        "3.8": f"{COMMON_RAY_PREFIX}-cp38-cp38-win_amd64.whl",
        "3.7": f"{COMMON_RAY_PREFIX}-cp37-cp37m-win_amd64.whl",
        "3.6": f"{COMMON_RAY_PREFIX}-cp36-cp36m-win_amd64.whl",
    },
}


def install_private_ray(anyscale_path):
    platform = sys.platform
    py_version = "{0}.{1}".format(*sys.version_info[:2])

    matching_wheel = None
    for target_platform, wheel_map in RAY_WHEELS.items():
        print(f"Evaluating os={target_platform}, python={list(wheel_map)}")
        if platform.startswith(target_platform):
            if py_version in wheel_map:
                matching_wheel = wheel_map[py_version]
                break
        print("Not matched.")

    if matching_wheel is None:
        raise Exception(
            "Unable to identify a matching Ray wheel for Platform: {}, Python: {}".format(
                platform, py_version
            )
        )

    cmd = [
        sys.executable,
        "-m",
        "pip",
        "install",
        "--target={}".format(os.path.join(anyscale_path, "anyscale", "anyscale_ray")),
        "-U",
        matching_wheel,
    ]
    print(f"Running: {' '.join(cmd)}.")
    subprocess.check_call(cmd)  # noqa: B1


def install_private_official_release_ray(anyscale_path):
    cmd = [
        sys.executable,
        "-m",
        "pip",
        "install",
        "--target={}".format(os.path.join(anyscale_path, "anyscale", "anyscale_ray")),
        "-U",
        f"ray=={RAY_VERSION}",
    ]
    print(f"Running: {' '.join(cmd)}.")
    subprocess.check_call(cmd)  # noqa: B1


class PostDevelopCommand(develop):
    def run(self):
        develop.run(self)
        print("Installing private version of Ray")
        download_and_copy_fswatch()
        install_private_official_release_ray(os.path.dirname(__file__))


class PostInstallCommand(install):
    def run(self):
        install.run(self)
        print("Installing private version of Ray")
        install_private_official_release_ray(self.install_lib)


# If adding new webterminal deps,
# Update backend/server/services/application_templates_service.py
# to prevent users from uninstalling them.
extras_require = {"backend": ["terminado==0.10.1", "tornado"]}


def package_files(directory):
    paths = []
    for (path, _, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join("..", path, filename))
    return paths


setup(
    name="anyscale",
    version=find_version("anyscale/__init__.py"),
    author="Anyscale Inc.",
    description=("Command Line Interface for Anyscale"),
    packages=[*find_packages(exclude="tests")],
    cmdclass={
        "sdist": SdistCommand,
        "develop": PostDevelopCommand,
        "install": PostInstallCommand,
    },
    distclass=BinaryDistribution,
    setup_requires=["setuptools_scm"],
    data_files=[
        (
            "generated",
            [
                "anyscale/fswatch-linux",
                "anyscale/fswatch-darwin",
                "anyscale/libfswatch.11.dylib",
            ],
        ),
    ],
    package_data={
        "": [
            "*.yaml",
            "*.json",
            *package_files("anyscale/client"),
            *package_files("anyscale/sdk"),
        ],
    },
    install_requires=[
        "boto3==1.16.52",
        "aiobotocore[boto3]==1.2.2",
        "botocore==1.19.52",
        "aiohttp==3.7.4.post0",
        "aiohttp_middlewares",
        "certifi",
        "conda-pack",
        "Click>=7.0",
        "colorama",
        "expiringdict",
        "GitPython",
        "jinja2",
        "jsonpatch",
        "jsonschema",
        "packaging",
        "pathspec==0.8.1",
        "python-dateutil",
        "requests",
        "sentry_sdk",
        "six >= 1.10",
        "tabulate",
        "urllib3 >= 1.15",
        "wrapt",
        "pyyaml",
    ],
    extras_require=extras_require,
    entry_points={"console_scripts": ["anyscale=anyscale.scripts:main"]},
    include_package_data=True,
    zip_safe=False,
)
