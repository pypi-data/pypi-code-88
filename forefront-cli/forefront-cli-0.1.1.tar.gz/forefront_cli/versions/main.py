import click
from ..api import API
from prettytable import PrettyTable
from halo import Halo
from forefront_cli.common import bcolors


@click.group()
def versions():
    pass


@versions.command()
@click.option("--delete", "-d", type=str, help="Id of version to delete")
def versions(delete):
    """Interact with model versions"""
    api = API()

    if api.key is None or api.key == '':
        print(bcolors.FAIL +
              'You are not logged in. Run the `init` command to log in.' + bcolors.ENDC)
        return

    if api.project_id is None or api.project_id == '':
        print(bcolors.FAIL +
              'You are not connected to a project. Please run the `init` command.')
        return

    if delete:
        delete_spinner = Halo(text=f"Attempting to delete version {delete}",
                              spinner='dots', text_color="blue")
        delete_spinner.start()
        req = api.delete_version(delete)
        delete_spinner.stop()
        if req == 204:
            print(bcolors.OKGREEN +
                  f"🗑 Removed version {delete}" + bcolors.OKGREEN)

        else:
            print(bcolors.FAIL +
                  f"Version {delete} not found" + bcolors.ENDC)

    else:
        versions = api.get_versions()
        t = PrettyTable(['title', 'id', 'url', 'file', 'created_at'])
        for v in versions:
            if v['endpointId'] == api.project_id:
                t.add_row([v['title'], v['_id'], v['endpointUrl'],
                           v['file'], v['createdAt']])
        print(t)
        # print('You have no versions created for this project')
