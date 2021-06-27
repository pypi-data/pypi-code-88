# standard imports
import os
import stat
import logging

# external imports
from hexathon import valid as valid_hex

# local imports
from .base import LevelDir

logg = logging.getLogger(__name__)


class HexDir(LevelDir):

    def __init__(self, root_path, key_length, levels=2, prefix_length=0):
        super(HexDir, self).__init__(root_path, levels, key_length + prefix_length)
        #self.path = root_path
        self.key_length = key_length
        self.prefix_length = prefix_length
        self.__levels = levels + 2


    def add(self, key, content, prefix=b''):
        l = len(key)
        if l != self.key_length:
            raise ValueError('expected key length {}, got {}'.format(self.key_length, l))
        l = len(prefix)
        if l != self.prefix_length:
            raise ValueError('expected prefix length {}, got {}'.format(self.prefix_length, l))
        if not isinstance(content, bytes):
            raise ValueError('content must be bytes, got {}'.format(type(content).__name__))
        if prefix != None and not isinstance(prefix, bytes):
            raise ValueError('prefix must be bytes, got {}'.format(type(content).__name__))
        key_hex = key.hex()
        entry_path = self.to_filepath(key_hex)

        c = self.count()

        os.makedirs(os.path.dirname(entry_path), exist_ok=True)
        f = open(entry_path, 'wb')
        f.write(content)
        f.close()

        f = open(self.master_file, 'ab')
        if prefix != None:
            f.write(prefix)
        f.write(key)
        f.close()

        logg.info('created new entry {} idx {} in {}'.format(key_hex, c, entry_path)) 
    
        return (c, entry_path)


    def __cursor(self, idx):
        return idx * (self.prefix_length + self.key_length)


    def set_prefix(self, idx, prefix):
        l = len(prefix)
        if l != self.prefix_length:
            raise ValueError('expected prefix length {}, got {}'.format(self.prefix_length, l))
        if not isinstance(prefix, bytes):
            raise ValueError('prefix must be bytes, got {}'.format(type(content).__name__))
        cursor = self.__cursor(idx)
        f = open(self.master_file, 'rb+')
        f.seek(cursor)
        f.write(prefix)
        f.close()


    def get(self, idx):
        cursor = self.__cursor(idx)
        f = open(self.master_file, 'rb')
        f.seek(cursor)
        prefix = f.read(self.prefix_length)
        key = f.read(self.key_length)
        f.close()
        return (prefix, key) 


    def to_subpath(self, hx):
        lead = ''
        for i in range(0, self.__levels, 2):
            lead += hx[i:i+2] + '/'
        return lead.upper()


    def to_dirpath(self, hx):
        sub_path = self.to_subpath(hx)
        return os.path.join(self.path, sub_path)


    def to_filepath(self, hx):
        dir_path = self.to_dirpath(hx)
        file_path = os.path.join(dir_path, hx.upper())
        return file_path


    def __verify_directory(self):
        fi = stat(self.path)
        if not stat.S_ISDIR(fi.st_mode):
            raise ValueError('{} is not a directory'.format(self.path))
        #f = os.listdir(self.path)
        #os.listdir(self.path)
        #f.close()
        return True


    @staticmethod
    def __prepare_directory(path):
        os.makedirs(path, exist_ok=True)
        state_file = os.path.join(path, 'master')
        f = open(state_file, 'w')
        f.close()

