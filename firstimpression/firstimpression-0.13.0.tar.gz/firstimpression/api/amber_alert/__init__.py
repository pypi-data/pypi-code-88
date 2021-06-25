from firstimpression.constants import TEMP_FOLDER, APIS
from firstimpression.file import download_install_media
import xml.etree.ElementTree as ET
import os

NAME = APIS['amber']
XML_FILENAME = 'amber_alert.xml'
URL = 'https://media.amberalert.nl/xml/combined/index.xml'
XML_TEMP_PATH = os.path.join(TEMP_FOLDER, NAME, XML_FILENAME)
URL_LOGO = 'http://fimp.nl/narrowcasting/amberalert.png'

MAX_FILE_AGE = 60 * 10

NAMESPACE_XML = {
    'NP': 'http://www.netpresenter.com'
}

TAGS = {
    'alert': 'NP:Alert',
    'soort': 'NP:AlertLevel',
    'status': 'NP:Status',
    'type': 'NP:Type',
    'message': 'NP:Message/NP:Common/NP:ISource',
    'name': 'NP:Title',
    'description': 'NP:Description',
    'readmore': 'NP:Readmore_URL',
    'amberlink': 'NP:Media_URL',
    'image': 'NP:Media/NP:Image'
}

def download_install_logo():
    download_install_media(URL_LOGO, TEMP_FOLDER, NAME)

def download_photo_child(url):
    return download_install_media(url, TEMP_FOLDER, NAME)

def get_alerts(root):
    return root.findall(TAGS['alert'], NAMESPACE_XML)

def get_alert_soort(alert):
    if alert.findtext(TAGS['soort'], '0', NAMESPACE_XML) == '10':
        return 'Amber Alert'
    else:
        return 'Vermist kind'

def get_alert_status(alert):
    return alert.findtext(TAGS['status'], 'Onbekend', NAMESPACE_XML)

def get_alert_type(alert):
    return alert.findtext(TAGS['type'], 'Onbekend', NAMESPACE_XML)

def get_alert_message(alert):
    return alert.find(TAGS['message'], NAMESPACE_XML)

def get_name_child(message):
    return message.findtext(TAGS['name'], 'Onbekend', NAMESPACE_XML)

def get_message_description(message):
    return message.findtext(TAGS['description'], '', NAMESPACE_XML)

def get_more_info_url(message):
    return message.findtext(TAGS['readmore'], '', NAMESPACE_XML)

def get_amber_url(message):
    return message.findtext(TAGS['amberlink'], '', NAMESPACE_XML)

def get_photo_child(message):
    media_url = message.findtext(TAGS['image'], None, NAMESPACE_XML)

    if media_url is None:
        return 'Content:\\placeholders\\img.png'
    else:
        return download_photo_child(media_url)

def parse_alert(alert):
    item = ET.Element("item")
    ET.SubElement(item, "soort").text = get_alert_soort(alert)
    ET.SubElement(item, "status").text = get_alert_status(alert)
    ET.SubElement(item, "type").text = get_alert_type(alert)

    message = get_alert_message(alert)

    ET.SubElement(item, "naam").text = get_name_child(message)
    ET.SubElement(item, "description").text = get_message_description(message)
    ET.SubElement(item, "readmore").text = get_more_info_url(message)
    ET.SubElement(item, "amberlink").text = get_amber_url(message)
    ET.SubElement(item, "image").text = get_photo_child(message)

    return item
