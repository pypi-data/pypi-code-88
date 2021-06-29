from firstimpression.constants import APIS
from firstimpression.constants import TEMP_FOLDER
from firstimpression.constants import DUTCH_INDEX
from firstimpression.constants import LOCAL_INTEGRATED_FOLDER
from firstimpression.constants import NAMELEVEL
from firstimpression.file import update_directories_api
from firstimpression.file import check_too_old
from firstimpression.file import download_install_media
from firstimpression.file import write_root_to_xml_files
from firstimpression.time import parse_string_to_string
from firstimpression.time import change_language
from firstimpression.scala import log
from firstimpression.scala import variables
from firstimpression.text import remove_emoji
from firstimpression.api.request import request_json
import xml.etree.ElementTree as ET
import os
import glob

##################################################################################################
# CONSTANTS
##################################################################################################

NAME = APIS['facebook']

DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S'
DATETIME_FORMAT_NEW = '%d %B %Y'

URL = 'https://fiapi.nl:8080/facebook_post/'


##################################################################################################
# MAIN FUNCTIONS API
##################################################################################################

def run_api(api_key, page_name, max_minutes, max_characters, max_items):
    max_file_age = 60 * max_minutes
    filename = '{}.xml'.format(page_name.lower())
    xml_temp_path = os.path.join(TEMP_FOLDER, NAME, filename)

    headers = {
        'Authorization': 'Token {}'.format(api_key)
    }

    params = {
        'page_name': page_name,
        'number_of_posts': max_items
    }

    update_directories_api(NAME)
    change_language(DUTCH_INDEX)

    if check_too_old(xml_temp_path, max_file_age):
        response_json = request_json(URL, headers, params, False)

        root = ET.Element("root")

        for post in response_json:
            item = ET.SubElement(root, "item")
            ET.SubElement(item, "page_name").text = get_page_name(post)
            ET.SubElement(item, "likes").text = str(get_likes(post))
            ET.SubElement(item, "message").text = crop_message(remove_emoji(get_message(post)), max_characters)
            ET.SubElement(item, "created_time").text = parse_string_to_string(get_creation_date(post), DATETIME_FORMAT, DATETIME_FORMAT_NEW)

            thumbnail_url = get_thumbnail_url(post)
            if thumbnail_url is None:
                media_link = 'Content:\\placeholders\\img.png'
            else:
                thumbnail_url = thumbnail_url.split('?').pop(0)
                media_link = download_install_media(thumbnail_url, TEMP_FOLDER, NAME)
            
            ET.SubElement(item, "image").text = media_link

        write_root_to_xml_files(root, xml_temp_path, NAME)        
    else:
        log(NAMELEVEL['INFO'], 'File not old enough to download new info')

def check_api(page_name, max_minutes):
    svars = variables()

    max_file_age = 60 * max_minutes

    file_name = '{}*.xml'.format(page_name.lower())
    file_path = os.path.join(LOCAL_INTEGRATED_FOLDER, NAME, file_name)

    file_path = glob.glob(file_path)[0]

    if check_too_old(file_path, max_file_age):
        svars['skipscript'] = True
    else:
        svars['skipscript'] = False

##################################################################################################
# MEDIA FUNCTIONS
##################################################################################################


##################################################################################################
# GET FUNCTIONS
##################################################################################################

def get_page_name(post):
    return post['page_name']


def get_thumbnail_url(post):
    return post['thumbnail']


def get_likes(post):
    return post['likes']


def get_message(post):
    return post['message']


def get_creation_date(post):
    return post['created_at'][:-6]

##################################################################################################
# PARSE FUNCTIONS
##################################################################################################

def crop_message(text, max_length):
    if len(text) > max_length:
        return text[:max_length-3] + "...\nLees verder op Facebook"
    else:
        return text
