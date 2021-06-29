from firstimpression.constants import APIS
from firstimpression.constants import LOCAL_INTEGRATED_FOLDER
from firstimpression.constants import NAMELEVEL
from firstimpression.file import update_directories_api
from firstimpression.file import check_too_old
from firstimpression.scala import variables
from firstimpression.scala import log
from firstimpression.api.request import request_json
import json
import os
import random

##################################################################################################
# CONSTANTS
##################################################################################################

PARAMS = {
    'firstName': 'firstname',
    'lastName': 'lastname',
    'exclude': ['explicit']
}

NAME = APIS['jokes']

JSON_FILENAME = 'jokes.json'
JSON_FILE_PATH = os.path.join(LOCAL_INTEGRATED_FOLDER, NAME, JSON_FILENAME)

URL = 'http://api.icndb.com/jokes/'

MAX_FILE_AGE = 60 * 60 * 24

##################################################################################################
# MAIN FUNCTIONS API
##################################################################################################

def run_api():
    update_directories_api(NAME)

    if check_too_old(JSON_FILE_PATH, MAX_FILE_AGE):
        with open(JSON_FILE_PATH, 'w') as file:
            json.dump(request_json(URL, params=PARAMS).get('value', [{}]), file)
    else:
        log(NAMELEVEL['INFO'], 'File not old enough to update')

def check_api():
    svars = variables()

    firstname = svars['firstname']
    lastname = svars['lastname']

    if check_too_old(JSON_FILE_PATH, MAX_FILE_AGE):
       svars['skipscript'] = True
       log(NAMELEVEL['WARNING'], 'File to old to run chuck_norris')
    else:
        svars['skipscript'] = False
        svars['joke'] = get_random_joke(firstname, lastname)


##################################################################################################
# MEDIA FUNCTIONS
##################################################################################################


##################################################################################################
# GET FUNCTIONS
##################################################################################################

def get_random_joke(firstname, lastname):
    jokes = [elem['joke'] for elem in json.load(open(JSON_FILE_PATH, 'r'))]

    return random.SystemRandom().choice(jokes).replace(PARAMS['firstName'], firstname).replace(PARAMS['lastName'], lastname)

##################################################################################################
# PARSE FUNCTIONS
##################################################################################################
