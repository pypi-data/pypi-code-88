import os
import time
import imghdr
import shutil
import requests
from bs4 import BeautifulSoup
from firstimpression.scala import install_content
from firstimpression.api.request import request
import xml.etree.ElementTree as ET


def create_directories(directories):
    for dirpath in directories:
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)


def get_age(filepath):
    return time.time() - os.path.getmtime(filepath)


def check_too_old(filepath, max_age):
    try:
        file_age = get_age(filepath)
    except WindowsError:
        return True

    if file_age > max_age:
        return True
    else:
        return False


def check_valid_jpeg(filepath):
    return imghdr.what(filepath) == 'jpeg' or imghdr.what(filepath) == 'jpg'


def download_media(media_link, subdirectory, temp_folder):
    # Downloads and returns path of media
    media_filename = media_link.split('/').pop()
    media_path = os.path.join(temp_folder, subdirectory, media_filename)

    if not os.path.exists(media_path):
        response = requests.get(media_link, stream=True)
        with open(media_path, 'wb') as writefile:
            shutil.copyfileobj(response.raw, writefile)
    return media_path


def install_media(media_link, subdirectory):
    install_content(media_link, subdirectory)
    return os.path.join('Content:\\', subdirectory, media_link.split('\\').pop())


def purge_directories(directories, max_days):
    # Remove all files from directory that are older than max_days
    for directory in directories:
        files = os.listdir(directory)
        for file in files:

            filepath = os.path.join(directory, file)
            file_age = get_age(filepath)

            if file_age > max_days * 86400:
                os.remove(filepath)


def write_root_to_xml_files(root, path, subfolder=None):
    tree = ET.ElementTree(root)
    tree.write(path)
    install_content(path, subfolder)


def xml_to_root(path):
    tree = ET.parse(path)
    root = tree.getroot()
    return root

def list_files(url, extensions):
    response = request(url).text
    soup = BeautifulSoup(response, 'html.parser')
    all_elements = [elem.get('href') for elem in soup.find_all('a')]
    select_elements = [elem for elem in all_elements if '.' + elem.split('.')[-1] in extensions]
    return select_elements

