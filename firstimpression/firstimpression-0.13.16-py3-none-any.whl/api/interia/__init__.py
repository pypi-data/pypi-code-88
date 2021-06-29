from firstimpression.constants import APIS
from firstimpression.constants import TEMP_FOLDER
from firstimpression.constants import LOCAL_INTEGRATED_FOLDER
from firstimpression.constants import PICTURE_FORMATS
from firstimpression.constants import TAGS_TO_REMOVE
from firstimpression.constants import REPLACE_DICT
from firstimpression.file import update_directories_api
from firstimpression.file import check_too_old
from firstimpression.file import write_root_to_xml_files
from firstimpression.file import list_files_dir
from firstimpression.file import download_media
from firstimpression.file import xml_to_root
from firstimpression.rss import get_feed
from firstimpression.text import remove_tags_from_string
from firstimpression.xml import get_attrib_from_element
from firstimpression.scala import variables
from firstimpression.scala import install_content
import xml.etree.ElementTree as ET
import os
import glob


##################################################################################################
# CONSTANTS
##################################################################################################

NAME = APIS['news_polish']

RSSFEED_URL = {
    'sport': 'https://sport.interia.pl/feed',
    'polska': 'https://wydarzenia.interia.pl/polska/feed',
    'kultura': 'https://wydarzenia.interia.pl/kultura/feed'
}

TAGS = {
    'item': 'channel/item',
    'title': 'title',
    'description': 'description'
}

LOCAL_PATH = os.path.join(LOCAL_INTEGRATED_FOLDER, NAME)

MAX_ITEMS = 4
MAX_FILE_AGE = 60 * 10

##################################################################################################
# MAIN FUNCTIONS API
##################################################################################################

def run_api(news_categories, minimal_items):

    update_directories_api(NAME)

    minimal_items = MAX_ITEMS if minimal_items > MAX_ITEMS else minimal_items

    for news_category in news_categories:
        if news_category == '' or news_category is None:
            continue

        category = news_category.lower()
        url = RSSFEED_URL[category]
        xml_temp_path = os.path.join(TEMP_FOLDER, NAME, '{}.xml'.format(category))

        if check_too_old(xml_temp_path, MAX_FILE_AGE):
            root = ET.Element("root")
            feed = get_feed(url)

            for news_item in feed.findall(TAGS['item']):
                item = ET.SubElement(root, "item")
                ET.SubElement(item, "title").text = get_title(news_item)
                ET.SubElement(item, "description").text = get_description(news_item)

                media_link = install_picture_content_wrap('square', os.path.join(NAME, category), TEMP_FOLDER, news_item, 'enclosure', 'url')

                if not media_link:
                    media_link = 'Content:\\placeholders\\img.png'

                ET.SubElement(item, "picsqr").text = media_link

                if len(root) == MAX_ITEMS:
                    break
            
            if len(root) >= minimal_items:
                write_root_to_xml_files(root, xml_temp_path, NAME)
            else:
                #TODO log
                pass

def check_api(news_categories):
    svars = variables()

    for category in news_categories:
        file_path = glob.glob(os.path.join(LOCAL_INTEGRATED_FOLDER, NAME, '{}*.xml'.format(category.lower())))[0]
        if check_too_old(file_path):
            svars['skipscript'] = True
            break
        else:
            svars['skipscript'] = False

            svars['total_items'] = len(xml_to_root(file_path))

    
    svars['total_categories'] = len(news_categories)
    

##################################################################################################
# MEDIA FUNCTIONS
##################################################################################################

def install_picture_content_wrap(picture_format, subdirectory, temp_folder, element, tag, attrib):
    # Installs content to LocalIntegratedContent folder and returns mediapath
    if not picture_format in PICTURE_FORMATS:
        return None

    media_link = get_attrib_from_element(element, tag, attrib).replace("_sqr256", "")

    media_path = download_media(PICTURE_FORMATS[picture_format] + media_link, subdirectory, temp_folder)

    install_content(media_path, subdirectory)

    media_filename = media_path.split('\\').pop()

    return os.path.join('Content:\\', subdirectory, media_filename)

##################################################################################################
# GET FUNCTIONS
##################################################################################################

def get_title(news_item):
    return news_item.findtext(TAGS['title'], '')

def get_description(news_item):
    return remove_tags_from_string(TAGS_TO_REMOVE, news_item.findtext(TAGS['description'], ''))

##################################################################################################
# PARSE FUNCTIONS
##################################################################################################

