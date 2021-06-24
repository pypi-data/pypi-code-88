# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['webship']

package_data = \
{'': ['*']}

install_requires = \
['fabric2>=2.5.0,<3.0.0']

entry_points = \
{'console_scripts': ['webship = webship:program.run']}

setup_kwargs = {
    'name': 'webship',
    'version': '0.1.2',
    'description': 'Tools to deploy python web application',
    'long_description': 'Tools to deploy python web application. The build process is run in container\nusing podman so make sure you have podman properly setup on the build machine.\n\n## Install\n\n    pipx install webship\n\n## Usage\n\nCreate directory to hold the deploy project:-\n\n    mkdir -p myapp_deploy\n\nCreate `webship.ini` to hold configuration about the deploy:-\n\n```\n[fetch]\nrepo = git@github.com:xoxzoeu/myapp.git\nclone_args = recursive\n\n[deploy]\npath = /app/myapp\nhosts =\n    127.0.0.1\n    127.0.0.2\n```\n\nTo build the app:-\n\n    webship fetch\n    webship build myapp 1.0.1 --docker_image=myapp\n\nThat will generate the release tarball in `build/myapp-1.0.1.tar.gz`. Before\ndeploying the release tarball, we can test it first to make sure everything\nis working as expected:-\n\n    webship run build/myapp-1.0.1.tar.gz ".venv/bin/myapp manage runserver 0.0.0.0:8000" --env-file=/home/kamal/python/myapp_deploy/env \n\nTo deploy:-\n\n    webship deploy build/myapp-1.0.1.tar.gz\n\nDeploy directory structure is like below:-\n\n```\n    deploy_path (default to /app/<project_name>)\n        releases/\n        current --> releases/<project_name>-0.0.1\n```\n\nActive release will be `/app/<project_name>/current` which is a symlink to active version. This\nstructure will allow multiple apps to be deployed on the same server.\n',
    'author': 'kamal',
    'author_email': 'kamal@xoxzo.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/xoxzo/webship',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
