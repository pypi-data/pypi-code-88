import json
import logging
import requests


# Module logger
mogger = logging.getLogger("pza.pipe.server")


class Server:

    ###########################################################################
    ###########################################################################
    
    def __init__(self, url) -> None:
        """
        """
        self.url = url

    ###########################################################################
    ###########################################################################
    
    def interfaces(self):
        """
        """
        r = requests.get(self.url + '/interfaces')
        return r.json()

