import os
import click
from jinja2 import Template
from pathlib import Path

DESKTOP_TEMPLATE = Path(__file__).parent / "desktop.jinja2"


@click.group()
def asapp():
    """Launch websites in app mode."""
    ...


@click.option(
    "--chrome", "-c",
    help="The chromium/google chrome binary to use.",
    default="chromium-browser",
)
@click.argument("url")
@asapp.command()
def open(chrome, url):
    """Open a url in app mode."""
    os.system(f"{chrome} --app={url}")


@click.option(
    "--chrome", "-c",
    help="The chromium/google chrome binary to use.",
    default="chromium-browser",
)
@click.option(
    "--icon", "-i",
    help="Path to an .ico file to use as the icon.",
    default="/usr/share/icons/locolor",
    type=click.Path(),
)
@click.option(
    "--name",
    prompt="What would you like to name the desktop entry?",
)
@click.argument("url")
@asapp.command()
def shortcut(chrome, url, icon, name):
    """Add a desktop entry for the app version of a given URL."""
    template = Template(DESKTOP_TEMPLATE.read_text())
    rendered = template.render(
        url=url,
        icon=icon,
        chrome=chrome,
        name=name,
    )

    filename = name.replace(" ", "_").lower()

    Path(
        f"~/.local/share/applications/{filename}.desktop"
    ).expanduser().write_text(rendered)

    click.secho(f"A desktop entry has been added for {url}", fg="green")
