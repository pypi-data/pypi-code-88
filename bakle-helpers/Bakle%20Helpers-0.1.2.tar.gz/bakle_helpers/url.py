import re
import os
import random

class Url:

    @staticmethod
    def is_valid(url):
        regex = re.compile(
        r'^(?:http|ftp)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        return regex.search(url) != None

    @staticmethod
    def random():        
        file = open(os.path.dirname(__file__) + '/support/urls.txt', 'r')
        result = file.readlines()[random.randint(0, 499)].strip()
        file.close()
        return result