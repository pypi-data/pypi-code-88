from firstimpression.constants import APIS
from firstimpression.constants import LOCAL_INTEGRATED_FOLDER
from firstimpression.constants import TEMP_FOLDER
from firstimpression.constants import DUTCH_INDEX
from firstimpression.constants import PICTURE_FORMATS
from firstimpression.constants import TAGS_TO_REMOVE
from firstimpression.constants import REPLACE_DICT
from firstimpression.file import update_directories_api
from firstimpression.file import check_too_old
from firstimpression.file import write_root_to_xml_files
from firstimpression.file import download_media
from firstimpression.file import list_files_dir
from firstimpression.file import xml_to_root
from firstimpression.time import change_language
from firstimpression.time import parse_string_to_string
from firstimpression.rss import get_feed
from firstimpression.xml import get_attrib_from_element
from firstimpression.scala import install_content
from firstimpression.scala import variables
from firstimpression.text import replace_html_entities
from firstimpression.text import remove_tags_from_string
import xml.etree.ElementTree as ET
import glob
import os

##################################################################################################
# CONSTANTS
##################################################################################################

NAME = APIS['nu']

DATETIME_FORMAT = "%a, %d %b %Y %H:%M:%S "
DATETIME_ABREVIATION_FORMAT = '%d %b %Y %H:%M'
DATETIME_FULL_FORMAT = '%d %B %Y %H:%M'

MAX_ITEMS = 10
MAX_FILE_AGE = 60 * 10

LOCAL_PATH = os.path.join(LOCAL_INTEGRATED_FOLDER, NAME)

BASE_URL = 'http://www.nu.nl/rss/'

TAGS = {
    'item': 'channel/item',
    'title': 'title',
    'descr': 'description',
    'pubDate': 'pubDate'
}

##################################################################################################
# MAIN FUNCTIONS API
##################################################################################################

def run_api(news_categories, minimal_items):
    minimal_items = MAX_ITEMS if minimal_items > MAX_ITEMS else minimal_items
    
    update_directories_api(NAME)
    change_language(DUTCH_INDEX)

    for news_category in news_categories:
        if news_category == '' or news_category is None:
            continue

        category = news_category.lower()

        url = BASE_URL + category

        xml_temp_path = os.path.join(TEMP_FOLDER, NAME, '{}.xml'.format(category))

        if check_too_old(xml_temp_path, MAX_FILE_AGE):
            root = ET.Element("root")

            feed = get_feed(url)

            for news_item in feed.findall(TAGS['item']):
                item = ET.SubElement(root, "item")
                ET.SubElement(item, "title").text = replace_html_entities(REPLACE_DICT, get_title(news_item))
                ET.SubElement(item, "descr").text = remove_tags_from_string(TAGS_TO_REMOVE, get_description(news_item))
                ET.SubElement(item, "pubDate").text = parse_string_to_string(get_publication_date(news_item), DATETIME_FORMAT, DATETIME_ABREVIATION_FORMAT)
                ET.SubElement(item, "fullMonthPubDate").text = parse_string_to_string(get_publication_date(news_item), DATETIME_FORMAT, DATETIME_FULL_FORMAT)

                media_link_full = install_picture_content_wrap('fullscreen', os.path.join(NAME, category), TEMP_FOLDER, news_item, 'enclosure', 'url')
                media_link_sqr = install_picture_content_wrap('square', os.path.join(NAME, category), TEMP_FOLDER, news_item, 'enclosure', 'url')

                if media_link_full is None and media_link_sqr is None:
                    media_link_full = media_link_sqr = 'Content:\\placeholders\\img.png'
                elif media_link_sqr is None:
                    media_link_sqr = media_link_full
                elif media_link_full is None:
                    media_link_full = media_link_sqr
                
                ET.SubElement(item, "picorg").text = media_link_full
                ET.SubElement(item, "picsqr").text = media_link_sqr

                if len(root) == MAX_ITEMS:
                    break

            if len(root) >= minimal_items:
                write_root_to_xml_files(root, xml_temp_path, NAME)

def check_api():
    svars = variables()

    count_categories = 0

    for elem in svars['categories']:
        if elem != '':
            count_categories += 1

    svars['total_categories'] = count_categories

    for file in list_files_dir(LOCAL_PATH):
        if 'xml' in file:
            file_path = os.path.join(LOCAL_PATH, file)
            if check_too_old(file_path, MAX_FILE_AGE):
                svars['skipscript'] = True
                break
            else:
                svars['skipscript'] = False

                amount_items = len(xml_to_root(file_path))

                if amount_items == 0:
                    svars['skipscript'] = True
                    break
                
                svars['total_items'] = amount_items


##################################################################################################
# MEDIA FUNCTIONS
##################################################################################################


##################################################################################################
# GET FUNCTIONS
##################################################################################################

def get_title(news_item):
    return news_item.findtext(TAGS['title'], '')

def get_description(news_item):
    return news_item.findtext(TAGS['descr'], '')

def get_publication_date(news_item):
    time = news_item.findtext(TAGS['pubDate'], None)
    if time is None:
        return ''
    else:
        return time[:-5]

##################################################################################################
# PARSE FUNCTIONS
##################################################################################################

def install_picture_content_wrap(picture_format, subdirectory, temp_folder, element, tag, attrib):
    # Installs content to LocalIntegratedContent folder and returns mediapath
    if not picture_format in PICTURE_FORMATS:
        return None

    media_link = get_attrib_from_element(element, tag, attrib).replace("_sqr256", "")

    if picture_format == 'square':
        media_link = media_link.replace('.jpg', '_sqr512.jpg')

    media_path = download_media(PICTURE_FORMATS[picture_format] + media_link, subdirectory, temp_folder)

    install_content(media_path, subdirectory)

    media_filename = media_path.split('\\').pop()

    return os.path.join('Content:\\', subdirectory, media_filename)
