from firstimpression import api
from firstimpression import file
from firstimpression import rss
from firstimpression import scala
from firstimpression import text
from firstimpression import time
from firstimpression import xml
from firstimpression import json

from firstimpression import constants

from os.path import join

file.create_directories(
    [join(constants.LOCAL_INTEGRATED_FOLDER, api_name) for api_name in constants.APIS])
file.create_directories([join(constants.TEMP_FOLDER, api_name)
                        for api_name in constants.APIS])
