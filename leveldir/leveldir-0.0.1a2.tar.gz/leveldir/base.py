# standard imports
import os


class LevelDir:

    def __init__(self, root_path, levels, entry_length):
        self.path = root_path
        self.levels = levels 
        self.entry_length = entry_length
        fi = None
        try:
            fi = os.stat(self.path)
            self.__verify_directory()
        except FileNotFoundError:
            LevelDir.__prepare_directory(self.path)
        self.master_file = os.path.join(self.path, 'master')


    def count(self):
        fi = os.stat(self.master_file)
        c = fi.st_size / self.entry_length
        r = int(c)
        if r != c: # TODO: verify valid for check if evenly divided
            raise IndexError('master file not aligned')
        return r


    @staticmethod
    def __prepare_directory(path):
        os.makedirs(path, exist_ok=True)
        state_file = os.path.join(path, 'master')
        f = open(state_file, 'w')
        f.close()
