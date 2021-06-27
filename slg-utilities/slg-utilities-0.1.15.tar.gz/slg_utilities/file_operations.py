import os
import os.path
import json
from .helpers import *
import re
import pickle
from slg_utilities.decorators.files import get_filename
from slg_utilities.decorators.logging import log_error


class FileOperations:

    '''
    Working directory defaults to the current working directory

    If sub_directory == True, then the write folder is found as a subdirectory of the current working directory

    If start_home == True, then start from the home directory in order to find the working_directory
        (this clearly negates sub_directory, however sub_directory has prio if True is passed for both)

    Working directory can be set again with self.set_working_directory(*args)

    Methods will default to writing to the default_filename if their filename is not declared. Same for directory
    '''

    def __init__(self, working_directory='', sub_directory=False,
                 start_home=False, default_filename=None):

        self.set_working_directory(
            working_directory, sub_directory, start_home)

        self.default_filename = default_filename

        if self.default_filename != None:
            self.default_filename_with_path = self.working_directory + '/' + self.default_filename

            # try to create file so we dont get any errors
            try:
                open(self.default_filename_with_path, 'x')
            except:
                pass

        # self.create directory if dir doesnt exist - this is a todo item, naming not immediately evident

    def set_working_directory(
            self, working_directory='', sub_directory=False, start_home=False):

        if not working_directory.startswith('/') and working_directory:
            working_directory = '/' + working_directory

        if sub_directory:
            self.working_directory = os.getcwd() + working_directory
        elif start_home:
            self.working_directory = os.environ.get('HOME') + working_directory
        else:
            self.working_directory = working_directory or os.getcwd()

    # @get_filename('.json')
    def write_json(self, data: dict, filename=None):
        '''
        writes json to directory <self.working_directory> with name <filename>
        '''
        filename = filename or self.default_filename
        with open(f"{self.working_directory}/{filename}", 'w') as outfile:
            json.dump(data, outfile)

    def read_json(self, filename=None):
        filename = filename or self.default_filename
        with open(f"{self.working_directory}/{filename}") as f:
            output = json.load(f)
        return output

    def update_json(self, updated_entries: dict, filename=None) -> dict:
        filename = filename or self.default_filename
        json_obj = self.read_json(filename)
        for key in updated_entries:
            json_obj[key] = updated_entries[key]
        self.write_json(json_obj, filename)
        return json_obj

    # @get_filename('.pickle')

    def write_pickle(self, data, filename=None):
        if not filename:
            filename = self.default_filename
        with open(f"{self.working_directory}/{filename}", "wb") as file_:
            pickle.dump(data, file_)

    def read_pickle(self, filename=None):
        if not filename:
            filename = self.default_filename
        with open(f"{self.working_directory}/{filename}", "rb") as file_:
            output = pickle.load(file_)
        return output

    # @get_filename('.txt')
    def write_text(self, data, filename, method='a+'):
        with open(f"{self.working_directory}/{ filename }", method) as file_:
            file_.write(data)

    def append_lines(self, filename, lines):
        with open(f"{self.working_directory}/{ filename }", 'a+') as file_:
            for line in lines:
                file_.write(f'\n{line}')

    def append_line(self, filename, line):
        with open(f"{self.working_directory}/{ filename }", 'a+') as file_:
            file_.write(f'\n{line}')

    # @get_filename('.txt')
    # @log_error('file_operations.log', True)
    def read_text(self, filename):
        with open(f"{self.working_directory}/{ filename }", 'r') as f:
            lines = [line.strip() for line in f.readlines()]
        return lines

    def get_file_parts(self, file_):
        '''
        file needs appropriate path headed

        returns filename, file_extension
        '''
        return os.path.splitext(file_)

    def delete_file(self, file_):
        try:
            os.remove(f"{self.working_directory}/{file_}")
        except:
            print('No file to delete')

    def append_text(self, text, file_with_path=None):

        pass

    def verify_defaults(self):

        pass

    def get_files_in_directory(
            self, directory=None, recurse=False, full_path=False):
        '''
        recursion not handled yet
        '''

        directory = directory or self.working_directory

        files = []

        for root, directories, filenames in os.walk(directory):
            for filename in filenames:
                if full_path == False:
                    file_ = filename
                else:
                    file_ = os.path.join(root, filename)

                files.append(file_)

        return files

    def regex_sub_files(self, regex, files, sub='', count=1):
        '''
        calls a regex sub for each file in files

        TODO: make it so that if sub == 'index' or 'idx' (not sure which), then we can substitute in the index of the file in files

        includes check to make sure returned filename is acceptable and requires input
        '''
        pattern = re.compile(regex)
        new_filenames = []

        for idx, file_ in enumerate(files):

            new_filename = pattern.sub(
                sub, self.get_file_parts(file_)[0],
                count=count)

            if idx == 0:
                while True:
                    ans = input(
                        f"{new_filename} is your new filename, is this acceptable? (y/n)")
                    if ans.lower() == 'y':
                        break
                    elif ans.lower() == 'n':
                        print('Sorry to hear your regex failed, stupid dum dum.')
                        return
                    else:
                        pass
            new_filenames.append(new_filename + self.get_file_parts(file_)[1])
            os.rename(
                f"{self.working_directory}/{file_}",
                f"{self.working_directory}/{new_filename + self.get_file_parts(file_)[1]}")

        print('Your new filenames: \n')
        for file_ in new_filenames:
            print(file_)
