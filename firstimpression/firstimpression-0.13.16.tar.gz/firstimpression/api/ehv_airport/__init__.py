from firstimpression.constants import APIS
from firstimpression.constants import TEMP_FOLDER
from firstimpression.constants import LOCAL_INTEGRATED_FOLDER
from firstimpression.constants import NAMELEVEL
from firstimpression.file import update_directories_api
from firstimpression.file import check_too_old
from firstimpression.file import write_root_to_xml_files
from firstimpression.scala import log 
from firstimpression.scala import variables
from firstimpression.api.request import request
import xml.etree.ElementTree as ET
import os
import glob
import lxml.html


##################################################################################################
# CONSTANTS
##################################################################################################

NAME = APIS['eindhoven']
URL = 'https://www.eindhovenairport.nl/nl/vertrektijden'

XML_FILENAME = 'flights.xml'
XML_FILENAME_CONTENT = 'flights*.xml'
XML_TEMP_PATH = os.path.join(TEMP_FOLDER, NAME, XML_FILENAME)
XML_LOCAL_PATH = os.path.join(LOCAL_INTEGRATED_FOLDER, NAME, XML_FILENAME_CONTENT)
MAX_FILE_AGE = 60 * 10

TABLE_FLIGHTS_XPATH = '//div[@id="skyguide"]/div/table'

##################################################################################################
# MAIN FUNCTIONS API
##################################################################################################

def run_api():

    update_directories_api(NAME)

    if check_too_old(XML_TEMP_PATH, MAX_FILE_AGE):
        root = ET.Element("root")

        response = lxml.html.fromstring(request(URL).text)

        table = response.xpath(TABLE_FLIGHTS_XPATH)[0]

        for row in table.xpath('tr'):
            item = ET.Element("item")
            store = False
            column_number = 1

            for column in row.xpath('td'):
                column_text = column.xpath('text()')

                if len(column_text) == 0:
                    column_text.append('')
                
                if column_number == 1:
                    ET.SubElement(item, "departure_time").text = column_text[0]
                elif column_number == 2:
                    ET.SubElement(item, "flight_number").text = column_text[0]
                elif column_number == 3:
                    ET.SubElement(item, "route").text = column_text[0]
                elif column_number == 4:
                    ET.SubElement(item, "status").text = column_text[0]
                    if not "Vertrokken" in column_text[0]:
                        store = True
                elif column_number == 5:
                    pass
                
                column_number += 1
            
            if store:
                root.append(item)
        
        write_root_to_xml_files(root, XML_TEMP_PATH, NAME)
    else:
        log(NAMELEVEL['INFO'], 'File not old enough to update')

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


##################################################################################################
# PARSE FUNCTIONS
##################################################################################################
