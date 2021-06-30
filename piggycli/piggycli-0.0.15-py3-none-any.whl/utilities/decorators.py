from functools import wraps
from app.controllers.status_controller import StatusController
from app.controllers.credentials_controller import CredentialsController
import boto3
import os
import click
from string import ascii_uppercase


def check_status(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        controller = StatusController(credentials=kwargs['credentials'])

        status = controller.show()
        if status == 'Piggy is sleeping':
            click.echo()
            click.secho(
                'Please run piggy status -wake before running this command', fg='red')
            click.echo()
            quit()
        elif status == 'Piggy is waking up':
            click.echo()
            click.secho(
                'Please wait unitl piggy status is Active before running this command', fg='red')
            click.echo()
            quit()
        else:
            pass

        return f(*args, **kwargs)
    return wrapper


def creds(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if kwargs.get('credentials_file_path') is None:

            path = '/Volumes/Piggy'
            if os.path.isdir(path) is False:
                creds_not_found()
            else:
                dirs = [d for d in os.listdir(
                    path) if os.path.isdir(os.path.join(path, d))]
                clusters = [c for c in dirs if 'cluster' in c]
                if len(clusters) == 0:
                    creds_not_found()
                elif len(clusters) > 1:
                    cluster = which_cluster(clusters=clusters)
                else:
                    cluster = clusters[0]

                credentials_file_path = os.path.join(
                    path, cluster, 'credentials.json')
        else:
            credentials_file_path = kwargs['credentials_file_path']

        if os.path.exists(credentials_file_path) is False:
            creds_not_found()

        try:
            controller = CredentialsController()
            credentials = controller.create_from_file(
                credentials_file_path=credentials_file_path)

        except Exception as e:
            creds_not_found()

        del kwargs['credentials_file_path']
        kwargs['credentials'] = credentials

        return f(*args, **kwargs)
    return wrapper


def creds_not_found():
    click.echo()
    click.secho(
        'Piggy could not find or your credentials.json file is not valid.', fg='red')
    click.echo()
    click.secho(
        'Please check your credentials.json file and run command with the -creds option.', fg='red')
    click.echo()
    quit()


def which_cluster(clusters):
    click.echo()
    click.secho('Piggy found multiple clusters.', fg='green')
    click.echo()
    choices = []
    for index, cluster in enumerate(clusters):
        click.secho(f'{ascii_uppercase[index]} - {cluster}', fg='green')
        choices.append(index+1)
    click.echo()
    choice = click.prompt('Please select a cluster:',
                          type=click.Choice(ascii_uppercase[:len(clusters)], case_sensitive=False))
    i = ascii_uppercase.index(choice)
    cluster = clusters[i]
    return cluster


class PiggyNotActive(Exception):
    pass
