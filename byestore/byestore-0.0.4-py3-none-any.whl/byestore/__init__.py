import logging

# Creating logger
byelogs = logging.getLogger(__name__)
byelogs.setLevel(logging.DEBUG)

# Handler - 1
file = logging.FileHandler("ByeStore_Logs.log")
fileformat = logging.Formatter("%(asctime)s [%(levelname)s] - [%(filename)s > %(funcName)s() > %(lineno)s] - %(message)s", datefmt="%H:%M:%S")
file.setLevel(logging.INFO)
file.setFormatter(fileformat)

# Handler - 3
stream = logging.StreamHandler()
streamformat = logging.Formatter("%(levelname)s:%(module)s:%(message)s")
stream.setLevel(logging.DEBUG)
stream.setFormatter(streamformat)

# Adding all handlers to the logs
byelogs.addHandler(file)
byelogs.addHandler(stream)


class ErrorHandle():  # Error Handling
    errors = {0: "Unknown", 9: "NoConfig", 24: "InvalidErrID", 666: "DirtyHacker"}

    def ErrorHandler(ERROR_ID=0, FAILEDERR_ID=0, NO_RUN=True):
        try:
            errorfriendly = ErrorHandle.errors[ERROR_ID]
            if errorfriendly[0] == 'A' or 'E' or 'I' or 'O' or 'U':
                byelogs.error('ByeStore ran into an {} error. Error ID: {}'.format(errorfriendly, ERROR_ID))
            else:
                byelogs.error('ByeStore ran into an {} error. Error ID: {}'.format(errorfriendly, ERROR_ID))
        except KeyError:
            ErrorHandle.ErrorMessageGenerator(24, ERROR_ID)

        if NO_RUN == True:
            byelogs.info('NO_RUN was set to True, so nothing happened')
        else:
            if ERROR_ID == 666:
                ErrorHandle.DirtyHacker(quit=False)
            elif ERROR_ID == 0:
                return
            elif ERROR_ID == 9:
                config = ErrorHandle.NoConfig()
                return config
            elif ERROR_ID == 24:
                logging.critical('Invalid Error ID given to the ErrorDebugger, please look into this as fast as possible. ERR_ID = {}'.format(FAILEDERR_ID))

    def NoConfig():
        import json
        configload = open('config.json', 'wt')
        configload.write('{}')
        configload.close()
        configload = open('config.json', 'rt')
        configstr = configload.read()
        configload.close()
        config = json.loads(configstr)
        configstr = None
        return config

    def DirtyHacker(quit=True):  # Joke Error handling, 
        print('...')
        import time
        time.sleep(10)
        print('h- how?')
        time.sleep(9)
        print('Just... how do you NOT open a file???')
        time.sleep(8)
        print('you must be a dirty hacker...')
        time.sleep(7)
        print('you can\'t do something like this normally...')
        time.sleep(6)
        print('you can\'t escape..')
        time.sleep(5)
        print('i can feel it.')
        time.sleep(4)
        print('you want to read these all... don\'t you?')
        time.sleep(3)
        print('you can\'t')
        time.sleep(2)
        print('you\'re nearly out of time')
        time.sleep(1)
        print('you can\'t take it.')
        time.sleep(0.5)
        print('goodbye.')
        time.sleep(2)
        if quit == True:
            import sys
            sys.exit()

class Dynamic():
    def getOS(friendly=True, friendlyxtra=False):
        '''Gets current os, and returns it to the program (use like a variable)
friendly = Boolian
    Used for friendly output for, say, printing directly to a terminal'''
        import platform
        if friendly == True:
            OS_LIST = {"Windows": "Windows", "Linux": "Linux", "Darwin": "macOS"}
            if friendlyxtra == True:
                return OS_LIST[platform.system()] + ' (' + platform.system() + ') '
            else:
                return OS_LIST[platform.system()]
        elif friendly == False:
            return platform.system()
        elif friendlyxtra == True:
            return 'Error: friendly needs to be True for friendlyxtra to be used as True, please enable/disable as needed'
        else:
            ErrorHandle.DirtyHacker()


class Store():
    def GetCatalogue():
        print('Getting catalogue...')
        import requests, json
        get_cat = requests.get('https://apps.byemc.xyz/api/v1/catalogue.json')
        cat_json = json.get_cat()
        return cat_json
        
    def LoadConfigFile():
        import json
        try:
            configload = open('config.json', 'rt')
            configstr = configload.read()
            configload.close()
            config = json.loads(configstr)
            configstr = None
        except json.JSONDecodeError:
            config = ErrorHandle.ErrorHandler(9)
        except FileNotFoundError:
            config = ErrorHandle.ErrorHandler(9)
        return config




class Egg():
    '''YO! GET AWAY FROM THE EASTER EGGS!!!'''

    egglist = "hehehehehe"
    doit = '8D38BD04002A34CC82110880B878C75602AC3A5C5B70F1DEFCFFA97F20C3D9E7'
    makeit = 'SHA256'
    thisisalist = ['MakeHacker']

    def MakeHacker():
        '''
        Haha you hacker now go brrr.
        '''
        import os
        while True:
            os.system('color 0a')
            os.system('dir')
            os.system('ls')
            os.system('ping google.com')
            os.system('http apps.byemc.xyz')
            os.system('echo No Escape')



if __name__ == "__main__":
    print('please note: don\'t run this as a file. you\'re gonna have a bad time.')
