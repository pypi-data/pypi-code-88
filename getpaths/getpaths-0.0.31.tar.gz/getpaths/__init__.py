'''
'''

import os
from copy import deepcopy
import inspect


# find path of the file doing the importing
importing_dir = None
for frame in inspect.stack()[1:]:
    if frame.filename[0] != '<':
        importing_dir = frame.filename
        break
if importing_dir == None:
    # TODO: fix pathing for interactive terminals
    importing_dir = '/jupyter.txt'

class getpath(str):
    '''
# IMPORTING

from getpaths import getpath


# USING CURRENT FILE PATH

current_dir = getpath() # current file's path


# USER-SPECIFIED PATH

custom_dir = getpath('a','b',custom=True)
print(custom_dir)
# /a/b


# ADD FILES

custom_dir/'example.txt'
# /a/b/example.txt

custom_dir.add('/a/example.txt')
# /a/b/example.txt


#  GO UP THE DIRECTORY

custom_dir = getpath('a','b',custom=True)

custom_dir/'..'
# /a

custom_dir.add('..')
# /a

custom_dir.up(1)
# /a


# LIST EXISTING FILES AND FOLDERS

custom_dir.ls()
# /a/b/example.txt
# throws error if path does not exist

    '''
    def __new__(cls, *args, custom=False):
        if custom:
            paths = []
        else:
            paths = [os.path.dirname(importing_dir)]
        
        for arguments in args:
            if arguments == '..':
                paths[0] = os.path.split(paths[0])[0]
            else:
                paths.append(arguments)
        
        path = os.sep.join(paths)
        return str.__new__(cls, path)
    
    def __init(self):
        super().__init__(self)
    
    def add(self, *args):
        paths = []
        for arguments in args:
            paths.append(arguments)
        
        path = os.sep.join([self.__str__(), os.sep.join(paths)])
        return getpath(path, custom=True)
    
    def __truediv__(self, *args):
        current_path = deepcopy(self.__str__())

        paths = [current_path]
        
        for arguments in args:
            if arguments == '..':
                paths[0] = os.path.split(paths[0])[0]
            else:
                paths.append(arguments)
        
        path = os.sep.join(paths)
        return getpath(path, custom=True)
    
    def ls(self, *args):
        paths = []
        for arguments in args:
            paths.append(arguments)
        
        path = os.sep.join([self.__str__(), os.sep.join(paths)])

        files_and_stuff = os.listdir(path)
        
        return files_and_stuff
    
    def up(self, num, *args):
        paths = []
        for arguments in args:
            paths.append(arguments)
        
        path = os.sep.join([self.__str__(), os.sep.join(paths)])

        times_up = ['..' for i in range(num+1)]
        return getpath(path, *times_up, custom=True)