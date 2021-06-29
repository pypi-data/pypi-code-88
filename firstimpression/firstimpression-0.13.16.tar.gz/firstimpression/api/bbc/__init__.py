from firstimpression.constants import APIS
from firstimpression.constants import TEMP_FOLDER
from firstimpression.constants import ENGLISH_INDEX
from firstimpression.constants import REPLACE_DICT
from firstimpression.constants import TAGS_TO_REMOVE
from firstimpression.constants import LOCAL_INTEGRATED_FOLDER
from firstimpression.constants import NAMELEVEL
from firstimpression.file import update_directories_api
from firstimpression.file import xml_to_root
from firstimpression.file import check_too_old
from firstimpression.file import write_root_to_xml_files
from firstimpression.file import list_files_dir
from firstimpression.text import replace_html_entities
from firstimpression.text import remove_tags_from_string
from firstimpression.rss import get_feed
from firstimpression.scala import log
from firstimpression.scala import variables
from firstimpression import time
import xml.etree.ElementTree as ET
import os

##################################################################################################
# CONSTANTS
##################################################################################################

NAME = APIS['bbc']
LOCAL_PATH = os.path.join(LOCAL_INTEGRATED_FOLDER, NAME)

DATETIME_FORMAT = "%a, %d %b %Y %H:%M:%S GMT"
DATETIME_ABREVIATION_FORMAT = '%b %d %Y %H:%M'
DATETIME_FULL_FORMAT = '%B %d %Y %H:%M'

MAX_ITEMS = 10
MAX_FILE_AGE = 60 * 10

TAGS = {
    'item': 'channel/item',
    'title': 'title',
    'descr': 'description',
    'pubDate': 'pubDate'
}

##################################################################################################
# MAIN FUNCTIONS API
##################################################################################################

def run_api(news_category, minimal_items):
    xml_temp_path = os.path.join(TEMP_FOLDER, NAME, '{}.xml'.format(news_category))
    url = 'http://feeds.bbci.co.uk/news/{}/rss.xml'.format(news_category)
    minimal_items = MAX_ITEMS if minimal_items > MAX_ITEMS else minimal_items

    update_directories_api(NAME)
    time.change_language(ENGLISH_INDEX)

    if check_too_old(xml_temp_path, MAX_FILE_AGE):
        root = ET.Element("root")
        feed = get_feed(url)

        for news_item in get_news_items(feed):
            root.append(parse_news_item(news_item))
            
            if len(root) == MAX_ITEMS:
                break
        
        if len(root) >= minimal_items:
            write_root_to_xml_files(root, xml_temp_path, NAME)
        else:
            log(NAMELEVEL['WARNING'], 'root contains less than minimum amount of news items required')
    else:
        log(NAMELEVEL['INFO'], 'file not old enough to update')

def check_api():
    svars = variables()

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

def get_news_items(root):
    return root.findall(TAGS['item'])

def get_news_title(news_item):
    return replace_html_entities(REPLACE_DICT, news_item.findtext(TAGS['title'], ''))

def get_news_description(news_item):
    return remove_tags_from_string(TAGS_TO_REMOVE, news_item.findtext(TAGS['descr'], ''))

def get_short_date(news_item):
    return time.parse_string_to_string(news_item.findtext(TAGS['pubDate'], ''), DATETIME_FORMAT, DATETIME_ABREVIATION_FORMAT)

def get_full_date(news_item):
    return time.parse_string_to_string(news_item.findtext(TAGS['pubDate'], ''), DATETIME_FORMAT, DATETIME_FULL_FORMAT)

##################################################################################################
# PARSE FUNCTIONS
##################################################################################################

def parse_news_item(news_item):
    item = ET.Element("item")
    ET.SubElement(item, "title").text = get_news_title(news_item)
    ET.SubElement(item, "descr").text = get_news_description(news_item)
    ET.SubElement(item, "pubDate").text = get_short_date(news_item)
    ET.SubElement(item, "fullMonthPubDate").text = get_full_date(news_item)

    return item