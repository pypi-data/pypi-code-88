import re
import random
import string
from .helper_exceptions import HelperExceptions

class Str:

    @staticmethod
    def is_a_string(data):
        return type(data) == str

    @staticmethod
    def ends_with(data, ending, ignoreCase = False):
        
        if not Str.is_a_string(data) or not Str.is_a_string(ending):
            HelperExceptions.raise_for_not_a_string()

        case = 0
        if(ignoreCase == True):
            case = re.IGNORECASE
        
        regex = re.compile(str(ending) + '$', case)

        return regex.search(str(data)) != None

    @staticmethod
    def starts_with(data, start, ignoreCase = False):

        if not Str.is_a_string(data) or not Str.is_a_string(start):
            HelperExceptions.raise_for_not_a_string()

        case = 0
        if(ignoreCase == True):
            case = re.IGNORECASE
        
        regex = re.compile('^' + str(start), case)

        return regex.search(str(data)) != None

    @staticmethod
    def after(string, limit):

        if not Str.is_a_string(string) or not Str.is_a_string(limit):
            HelperExceptions.raise_for_not_a_string()

        if limit.strip() == '':
            return string

        stringToList = string.split(limit, 2)
        stringToList.reverse()
        
        return stringToList[0].strip()

    @staticmethod
    def before(string, limit):

        if not Str.is_a_string(string) or not Str.is_a_string(limit):
            HelperExceptions.raise_for_not_a_string()

        if limit.strip() == '':
            return string

        return string.split(limit, 2)[0].strip()

    @staticmethod
    def contains(string, search, ignoreCase = False):

        if not Str.is_a_string(string) or not Str.is_a_string(search):
            HelperExceptions.raise_for_not_a_string()

        case = 0
        if(ignoreCase == True):
            case = re.IGNORECASE
        regex = re.compile(str(search), case)

        return regex.search(str(string)) != None


    @staticmethod
    def limit(string, limit, ellipses = True):

        if not Str.is_a_string(string):
            HelperExceptions.raise_for_not_a_string()

        if Str.__is_not_an_integer(limit):
            HelperExceptions.raise_for_not_an_integer(limit)

        if len(string) <= limit:
            return string

        result = string[:limit]

        if ellipses == True:
            result += '...'

        return result

    @staticmethod
    def random(length):   

        if Str.__is_not_an_integer(length):
            HelperExceptions.raise_for_not_an_integer(length)

        return ''.join(random.choices(string.ascii_letters, k = length))    

    @staticmethod
    def __is_not_an_integer(integer):
        return type(integer) != int