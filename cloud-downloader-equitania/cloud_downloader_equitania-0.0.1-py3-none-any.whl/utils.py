# -*- coding: utf-8 -*-
# Copyright 2014-now Equitania Software GmbH - Pforzheim - Germany
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
import requests


def download_from_link(link, output_name):
    download = requests.get(link, allow_redirects=True)
    open(output_name, 'wb').write(download.content)


def format_sharepoint_link(link):
    if "?" in link:
        link = link[:link.index('?')+1] + "Download=1"
    else:
        link += "?Download=1"
    return link


def format_hidrive_link(link):
    hidrive_id = link[link.rindex('/')+1:]
    hidrive_api_link = "https://my.hidrive.com/api/sharelink/download?id="
    return hidrive_api_link + hidrive_id


def format_dropbox_link(link):
    link = link[:-1] + "1"
    return link


def format_gdrive_link(link):
    base_direct_link = "https://drive.google.com/uc?export=download&id="
    download_id = link.split("/")[5]
    return base_direct_link + download_id

