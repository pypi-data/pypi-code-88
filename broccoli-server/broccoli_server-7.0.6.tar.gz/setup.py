import os
import shutil
import subprocess
from os import path
from setuptools.command.sdist import sdist
from setuptools import setup, find_packages

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

install_requires = [
    'jinja2==2.11.3',
    'flask==1.0.3',
    'pika==1.0.1',
    'pymongo==3.8.0',
    'flask-cors==3.0.9',
    'flask-jwt-extended==3.25.0',
    'dnspython==1.16.0',
    'jsonschema==3.0.1',
    'apscheduler==3.6.0',
    'sentry-sdk==0.14.3',
    'redis==3.5.3',
    # contrib
    'oauthlib==3.1.0',
    'requests==2.22.0',
    'python-twitter==3.5'
]

VERSION = "7.0.6"

tests_require = [
    'mongomock==3.17.0',
]


WEB_ARTIFACT_PATH = os.path.join("broccoli_server", "web")


def build_web():
    # check executables which are required to build web
    if not shutil.which("node"):
        raise RuntimeError("node is not found on PATH")
    if not shutil.which("yarn"):
        raise RuntimeError("yarn is not found on PATH")

    # build web
    subprocess.check_call(["yarn", "install"], cwd="web")
    subprocess.check_call(["yarn", "build"], cwd="web")

    # move built artifact
    if os.path.exists(WEB_ARTIFACT_PATH):
        print("removing old web artifact")
        shutil.rmtree(WEB_ARTIFACT_PATH)
    shutil.move(os.path.join("web", "build"), WEB_ARTIFACT_PATH)


class SdistCommand(sdist):
    def run(self):
        build_web()
        sdist.run(self)


setup(
    name='broccoli_server',
    version=VERSION,
    description='A Python framework to build web scraping applications.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/k-t-corp/broccoli-server',
    author='KTachibanaM',
    author_email='whj19931115@gmail.com',
    license_files=('LICENSE',),
    packages=find_packages(),
    # this is important for including web when building wheel
    include_package_data=True,
    # this is important for including web when building wheel
    package_data={
        "broccoli_server": ["web"]
    },
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite="broccoli_server.tests",
    cmdclass={
        'sdist': SdistCommand
    }
)
