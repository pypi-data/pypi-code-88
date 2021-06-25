import click
from PyInquirer import prompt
from prompt_toolkit.validation import Validator, ValidationError
from halo import Halo
import json
from ..common import bcolors, get_user_token, set_user_token, get_project_id, set_project_id
from ..api import fetch_projects, create_project, base_dashboard_url


@click.group()
def init():
    pass


class StringValidator(Validator):
    '''Validates input is a string'''

    def validate(self, document):
        try:
            str(document.text)
        except ValueError:
            raise ValidationError(message="Please enter a valid string",
                                  cursor_position=len(document.text))


def login_prompt():
    '''Interactive prompt to supply auth token'''
    questions = [
        {
            'type': "input",
            "name": "token",
            "message": "Paste your auth token",
            "validate": StringValidator,
            "filter": lambda val: str(val)
        }]
    token = prompt(questions)
    return token['token']


def select_project_prompt(projects):
    '''Interactive prompt to select a project'''
    choices = ['Create a new project']
    for p in json.loads(projects):
        choices.append(f"{p['title']} ({p['_id']})")

    return {
        "type": "list",
        "name": "project_selection",
        "message": "Select a project",
        "choices": choices
    }


def create_project_prompt():
    '''Interactive prompt to specify project details'''
    questions = [
        {
            'type': "input",
            "name": "title",
            "message": "Enter a name for you project",
            "validate": StringValidator,
            "filter": lambda val: str(val)
        },
        {
            'type': "input",
            "name": "description",
            "message": "Optional: Provide a description for your project",
            "validate": StringValidator,
            "filter": lambda val: str(val)
        }
    ]
    project = prompt(questions)
    # print(project)
    create_spinner = Halo(text='Creating project',
                          spinner='dots', text_color="blue")
    create_spinner.start()
    project_id = create_project(project['title'], project['description'])
    project_id = json.loads(project_id)
    create_spinner.stop()

    set_project_id(project_id['endpointId'])
    print('Project created sucessfully')
    return {'project_selection': project_id['endpointId']}


def auth_interaction():
    '''Checks for user auth key or prompts user to get auth token'''
    auth_spinner = Halo(text='Check authentication',
                        spinner='dots', text_color="blue")
    auth_spinner.start()
    token = get_user_token()
    auth_spinner.stop()

    if token is None or token == '':
        print(bcolors.FAIL + 'No authentication found' + bcolors.ENDC)
        print(bcolors.OKBLUE +
              f"Open {base_dashboard_url}/cli and paste auth token into terminal" + bcolors.ENDC)
        token = login_prompt().strip()
        set_user_token(token)

        print(bcolors.OKBLUE + 'Authentication token set' + bcolors.ENDC)

    else:
        print(bcolors.OKBLUE + 'Authentication token found' + bcolors.ENDC)
    return token


def project_selection(token):
    '''Prompts user to select or create a project'''
    project_spinner = Halo(text=f"Fetching user projects\n",
                           spinner='dots', text_color='blue')
    project_spinner.start()
    projects = fetch_projects()
    project_spinner.stop()

    if projects is None:
        print('No projects found.')
        return
    project_prompt = select_project_prompt(projects)
    selection = prompt(project_prompt)

    if selection['project_selection'] != "Create a new project":
        project = selection['project_selection'].split('(')[1].split(')')[
            0].strip()

        set_project_id(project)
        print('✅ You are now logged in to Forefront')
        print(
            f"ℹ️ CLI is configured to use project {get_project_id()}")

    else:
        create_project_prompt()
        # print(bcolors.FAIL +
        #       "Projects can only be created from the UI at this time." + bcolors.ENDC)
    return get_project_id()


@ init.command()
def init():
    """Log in to forefront and connect to a project"""
    token = auth_interaction()
    project_selection(token)


# @cloudflare.command()
# @click.argument("tz")
# @click.option("--repeat", "-r", default=1, type=int, help="Number of times to repeat")
# @click.option("--interval", "-i", default=3, type=int, help="Interval at which to print output")
# def greet(tz, repeat=1, interval=3):
#     """Parse a timezone and greet a location a number of times."""
#     for i in range(repeat):
#         if i > 0:  # no delay needed on first round
#             time.sleep(interval)
#         now = arrow.now(tz)
#         friendly_time = now.format("h:mm a")
#         seconds = now.format("s")
#         location = tz.split("/")[-1].replace("_", " ")
#         print(f"Hey there, {location}!")
#         print(f"The time is {friendly_time} and {seconds} seconds.\n")
