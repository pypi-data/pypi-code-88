# Copyright 2021 Chainopt LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import click

from rio.utilities import utils as rio_utils


@click.command()
@click.option("-l", "--local", is_flag=True, type=bool, help="Undeploy local package")
@click.option("--all", is_flag=True, type=bool, help="Undeploy All")
@click.option("-p", "--package_name", type=str, help="Name of package")
def cli(local, package_name, all):
    """
    Undeploy a Package or all packages.
    If the package is running, you will be asked if you want to stop and delete it.
    """
    rio_utils.undeploy(local, package_name, all)
    return
