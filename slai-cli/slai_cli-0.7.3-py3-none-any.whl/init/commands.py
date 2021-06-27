import click

from slai.modules.runtime import detect_runtime, detect_credentials
from slai.exceptions import NoCredentialsFound
from slai_cli import log
from slai_cli.init import project_generator
from slai_cli.exceptions import ProjectExistsException, InvalidApiKey


@click.command()
@click.argument("name")
@click.option("--profile", required=False, default="default", help="Profile to use")
def init(name, profile):
    """Create a new slai project."""

    runtime = detect_runtime()

    try:
        credentials = detect_credentials(runtime=runtime, profile_name=profile)
    except NoCredentialsFound:
        log.warn("Invalid credentials.")
        return

    try:
        pg = project_generator.ProjectGenerator(
            project_name=name,
            credentials=credentials,
        )
    except ProjectExistsException:
        log.warn(f"Project '{name}' already exists.")
        return
    except InvalidApiKey:
        log.warn("Invalid credentials.")
        return

    pg.create_new_project()
