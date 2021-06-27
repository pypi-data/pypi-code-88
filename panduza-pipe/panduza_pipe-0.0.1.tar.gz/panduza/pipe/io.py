import json
from .alias import Alias
import requests
import json
import logging

# Module logger
mogger = logging.getLogger("pza.pipe.io")


class Io:

    ###########################################################################
    ###########################################################################
    
    def __init__(self, url=None, alias=None) -> None:
        """
        """
        if url:
            self.url = url
        elif alias:
            self.url = Alias.GetUrl(alias)
        else:
            raise Exception("bad config")

    ###########################################################################
    ###########################################################################

    def writeDirection(self, direction):
        """
        """
        # Prepare url & payload
        url = self.url + '/direction'
        payload = { "direction": direction }
        # Debug
        mogger.debug("writeDirection [%s] to [%s]", json.dumps(payload), url)

        # Send request
        r = requests.put( url, json=payload )
        mogger.debug("response %s", r)

        # Manage errors
        if(r.status_code != 200):
            raise Exception("write direction failure [" + repr(r) + "]")

    ###########################################################################
    ###########################################################################

    def readDirection(self):
        """
        """
        r = requests.get(self.url + '/direction')

        # Manage http errors
        if(r.status_code != 200):
            raise Exception("read direction failure [" + repr(r) + "]")

        # Manage payload errors
        body = r.json()
        if "direction" not in body:
            raise Exception("response has no 'direction'")

        return body["direction"]

    ###########################################################################
    ###########################################################################

    def writeValue(self, value):
        """
        """
        r = requests.put(self.url + '/value', json={ "value": value } )
        pass

    ###########################################################################
    ###########################################################################
    
    def readValue(self):
        """
        """
        r = requests.get(self.url + '/value')

        # Manage http errors
        if(r.status_code != 200):
            raise Exception("read value failure [" + repr(r) + "]")

        # Manage payload errors
        body = r.json()
        if "value" not in body:
            raise Exception("response has no 'value'")

        return body["value"]

    ###########################################################################
    ###########################################################################
    