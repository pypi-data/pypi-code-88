from forefront_cli.common import bcolors, set_project_id
import click
from ..api import API
from prettytable import PrettyTable
from halo import Halo


@click.group()
def projects():
    pass


@projects.command()
@click.option("--delete", "-d", type=str, help="Id of endpoint to delete")
def projects(delete):
    """Interact with projects"""
    api = API()

    if api.key is None or api.key == '':
        print(bcolors.FAIL +
              'You are not logged in. Run the `init` command to log in.' + bcolors.ENDC)
        return

    if delete:
        if delete == api.project_id:
            print(bcolors.OKBLUE + 'You are deleting the endpoint you are currently connected to. You will need to run `ff init` to create or connect to a new project.' + bcolors.ENDC)
            set_project_id('')
        delete_spinner = Halo(text=f"Attempting to delete project {delete}",
                              spinner='dots', text_color="blue")
        delete_spinner.start()
        req = api.delete_endpoint(delete)
        delete_spinner.stop()
        if req == 204:
            print(bcolors.OKGREEN +
                  f"🗑 Removed endpoint {delete}" + bcolors.OKGREEN)

        else:
            print(bcolors.FAIL +
                  f"Project {delete} not found" + bcolors.ENDC)

    else:
        projects = api.get_projects()
        t = PrettyTable(['title', 'id',
                        'root url',  'created_at'])
        for e in projects:
            t.add_row([e['title'], e['_id'], e['liveUrl'],
                       e['createdAt']])
        print(t)
