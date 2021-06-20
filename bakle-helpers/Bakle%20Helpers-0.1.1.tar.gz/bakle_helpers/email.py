import re
import os
import random

class Email:

    @staticmethod
    def is_valid(email):
        regex = re.compile("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", re.IGNORECASE)
        return regex.search(email) != None

    @staticmethod
    def random():
        file = open(os.path.dirname(__file__) + '/support/emails.txt', 'r')
        result = file.readlines()[random.randint(0, 499)].strip()
        file.close()
        return result