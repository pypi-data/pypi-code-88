from firstimpression.constants import APIS
from firstimpression.constants import TEMP_FOLDER
from firstimpression.constants import LOCAL_INTEGRATED_FOLDER
from firstimpression.file import update_directories_api
from firstimpression.file import check_too_old
from firstimpression.file import write_root_to_xml_files
from firstimpression.xml import get_xml
from firstimpression.scala import variables
import xml.etree.ElementTree as ET
import os
import glob

##################################################################################################
# CONSTANTS
##################################################################################################

NAME = APIS['trends']

XML_FILE_NAME = 'trends.xml'
XML_FILE_NAME_CONTENT = 'trends*.xml'
XML_TEMP_PATH = os.path.join(TEMP_FOLDER, NAME, XML_FILE_NAME)
XML_LOCAL_PATH = os.path.join(LOCAL_INTEGRATED_FOLDER, NAME, XML_FILE_NAME_CONTENT)

URL = 'https://trends.google.nl/trends/hottrends/atom/feed?pn=p17'

NAMESPACE = {
    'atom': 'http://www.w3.org/2005/Atom',
    'ht': 'https://trends.google.nl/trends/trendingsearches/daily'
}

TAGS = {
    'item': 'channel/item',
    'title': 'title',
    'traffic': 'ht:approx_traffic',
    'url': 'link'
}

MAX_FILE_AGE = 60 * 30


##################################################################################################
# MAIN FUNCTIONS API
##################################################################################################

def run_api():

    update_directories_api(NAME)

    if check_too_old(XML_TEMP_PATH, MAX_FILE_AGE):
        root = get_xml(URL)
        new_root = ET.Element("root")

        for elem in root.findall(TAGS['item']):
            item = ET.SubElement(new_root, "item")
            ET.SubElement(item, "title").text = get_title(elem)
            ET.SubElement(item, "traffic").text = str(get_traffic(elem))
            ET.SubElement(item, "url").text = get_url(elem)
        
        write_root_to_xml_files(new_root, XML_TEMP_PATH, NAME)

def check_api():
    svars = variables()

    file_path = glob.glob(XML_LOCAL_PATH)[0]

    if check_too_old(file_path, MAX_FILE_AGE):
        svars['skipscript'] = True
    else:
        svars['skipscript'] = False
            

##################################################################################################
# MEDIA FUNCTIONS
##################################################################################################


##################################################################################################
# GET FUNCTIONS
##################################################################################################

def get_title(elem):
    return elem.findtext(TAGS['title'], '')

def get_traffic(elem):
    return elem.findtext(TAGS['traffic'], '', NAMESPACE)

def get_url(elem):
    return elem.findtext(TAGS['url'], '')

##################################################################################################
# PARSE FUNCTIONS
##################################################################################################
