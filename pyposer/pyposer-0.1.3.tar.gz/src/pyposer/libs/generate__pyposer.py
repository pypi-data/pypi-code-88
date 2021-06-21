import os
import subprocess
import json
import inquirer
from . import colors
from .install__libs import install

_GIT_DIR = os.path.exists('.git')
_SHELL = os.environ['SHELL'].split('/')[-1]


def createPyposer(click, default=False):
    if default:
        name = os.path.abspath(os.getcwd()).split('/')[-1]
        version = "1.0.0"
        main = "__main__.py"
        if _GIT_DIR:
            remote = subprocess.Popen(
                "git remote get-url origin",
                shell=True,
                stdout=subprocess.PIPE).stdout.read().decode().replace(
                    '\n', '')
            username = subprocess.Popen(
                "git config --get user.name",
                shell=True,
                stdout=subprocess.PIPE).stdout.read().decode()
            email = subprocess.Popen(
                "git config --get user.email",
                shell=True,
                stdout=subprocess.PIPE).stdout.read().decode()
            author = f"{username} <{email}>".replace('\n', '')

            license_type = "MIT"
            scripts = {"teste": "echo 'teste'"}
            dependencies = {}
            devDependencies = {}

            pyposer = {
                "name": name,
                "version": version,
                "main": main,
                "remote": remote,
                "author": author,
                "license": license_type,
                "scripts": scripts,
                "dependencies": dependencies,
                "devDependencies": devDependencies
            }

        else:
            license_type = "MIT"
            scripts = {"teste": "echo 'teste'"}
            dependencies = {}
            devDependencies = {}

            pyposer = {
                "name": name,
                "version": version,
                "main": main,
                "license": license_type,
                "scripts": scripts,
                "dependencies": dependencies,
                "devDependencies": devDependencies
            }

        click.echo(
            f"{colors.YELLOW}warning{colors.ENDC} The yes flag has been set. This will automatically answer yes to all questions"
        )
        with open('pyposer.json', 'w') as file:
            try:
                file.write(json.dumps(pyposer, indent=2))
                click.echo(
                    f"{colors.GREEN}success{colors.ENDC} Saved pyposer.json")
            except Exception as e:
                return click.echo(f"{colors.RED}error{colors.ENDC} {e}")
    else:
        questions = [
            inquirer.Text('name',
                          message="Name",
                          default=os.path.abspath(os.getcwd()).split('/')[-1]),
            inquirer.Text('version', message="Version", default="0.1.0"),
            inquirer.Text('description', message="Description"),
            inquirer.Text('main', message="Main file", default="__main__.py"),
            inquirer.Text('author', message="Author"),
            inquirer.Text('license', message="License", default="MIT"),
        ]
        answers = inquirer.prompt(questions)

        pyposer = {
            "name": answers['name'],
            "version": answers['version'],
            "main": answers['main'],
            "description": answers['description'],
            "author": answers['author'],
            "license": answers['license'],
            "scripts": {
                "teste": "echo 'teste'"
            },
            "dependencies": {},
            "devDependencies": {}
        }
        with open('pyposer.json', 'w') as file:
            try:
                file.write(json.dumps(pyposer, indent=2))
                click.echo(
                    f"{colors.GREEN}success{colors.ENDC} Saved pyposer.json")
            except Exception as e:
                return click.echo(f"{colors.RED}error{colors.ENDC} {e}")
