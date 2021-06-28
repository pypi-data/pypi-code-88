# -*- coding: utf-8 -*-
# Copyright 2014-now Equitania Software GmbH - Pforzheim - Germany
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from .utils import format_sharepoint_link, format_hidrive_link, format_dropbox_link, format_gdrive_link, download_from_link
import click


cloud_services = {
    "sharepoint": format_sharepoint_link,
    "hidrive": format_hidrive_link,
    "dropbox": format_dropbox_link,
    "google": format_gdrive_link,
}


def welcome():
    click.echo("Welcome to the cloud_downloader!")


@click.command()
@click.option("--link",
              help="Link to file", prompt="Link to file")
@click.option("--filename",
              help="Name of file output", prompt="Name of file output")
def start_cloud_downloader(link, filename):
    direct_link = None
    try:
        for cloud_service, format_function in cloud_services.items():
            if cloud_service in link:
                direct_link = format_function(link)
                break
        if direct_link:
            download_from_link(direct_link, filename)
        else:
            print("No valid link")
    except Exception as e:
        print("No valid link")
        print(e)


if __name__ == "__main__":
    welcome()
    start_cloud_downloader()