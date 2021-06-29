# -*- coding: utf-8 -*-
# Load libraries ---------------------------------------------

import os
import configparser
import hashlib

# ------------------------------------------------------------


class APILoginController(object):
    
    def __init__(self):
        pass
    
    @staticmethod
    def login(user, password):
        
        config = configparser.ConfigParser()
        config.read(os.path.join("config", "parameters.ini"))
        m = hashlib.md5()
        m.update(password)
        if (user != config["api"]["user"]) or (m.hexdigest() != config["api"]["password"]):
            return False
        else: 
            return True
