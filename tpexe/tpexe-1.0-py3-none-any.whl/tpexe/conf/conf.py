import os
import sys
import yaml

class GetConfig(object):

    def __init__(self, conf):
        self.conf = conf 
        self.f = open(self.conf, 'r', encoding='utf8')

    def get_yaml_conf_data(self):
        ydata = yaml.load(self.f.read(), Loader=yaml.FullLoader)
        return ydata
