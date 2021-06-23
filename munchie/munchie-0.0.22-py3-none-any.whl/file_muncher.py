# import libraries
import configparser
import csv
import json
import pendulum
import platform
import os
import shutil
import stat
import yaml

from munchie.util import (
    _rich_util,
    _validation_util
)
from datetime import datetime
from json.decoder import JSONDecodeError
from pathlib import Path
from typing import Any, Dict, List, NoReturn, Union
from yaml.parser import ParserError
from yaml.scanner import ScannerError

# the following libraries help resolve directory and file ownership on non-windows platforms
if platform.system() != 'Windows':
    from grp import getgrgid
    from pwd import getpwuid


class FileMuncher:
    """
    Class object to manage creating, reading, removing, storing, and writing files and directories.

    Attributes:
        base_dir (Path): path to the current working directory
        home_dir (Path): path to the current user home directory

    Functions:
        create_new_directory: create a new directory
        create_new_file: create a new file
        get_directory_contents: get the immediate contents of a directory or all the contents directory recusively
        get_path_stats: get the filesystem details of a directory or a file path
        read_file: read in a file and get the contents
        remove_directory: remove a directory and all of its contents
        remove_file: remove a file
        rotate_files: remove files from a directory older than the specified days
        update_path: add a new attribute to the Files object and store a Path value or update an existing path
        write_file: update or create a new file with contents. Supports the following file types
    """

    def __init__(self):
        """Initialize a Files instance."""

        self.base_dir = Path.cwd()   # current working directory
        self.home_dir = Path.home()  # user home folder
        self.custom_path = {}        # placeholder to store custom paths

    def _convert_path_type(self, path_to_convert: Union['Path', str]) -> 'Path':
        """
        Convert a sting type path to a Path type.

        This function is not meant to be accessed directly but users but instead
        meant as a utility for validating other library functionality.

        Args:
            path_to_convert (str): path to file or directory

        Returns:
            (Path): provided path converted to Path type
        """

        if isinstance(path_to_convert, str):         # if the path is a string type
            path_to_convert = Path(path_to_convert)  # convert the path to a Path class type

        return path_to_convert                       # return the path as a Path

    @staticmethod
    def _get_file_extension(path_to_file: 'Path', verify_only: bool = False) -> Union[None, str, NoReturn]:
        """
        Get the extention of the file.

        * csv: .csv
        * ini: .cfg, .conf, .ini
        * json: .json
        * txt: .nfo, .text, .txt
        * yaml: .yaml, .yml

        Args:
            path_to_file (Path): path the the file to get the extension for

        Returns:
            (str): extension of the file

        Raises:
            AttributeError: file path has no extension specified
            TypeError: unsupported extension type
        """

        # mapping of supported file types
        supported_file_extensions = {
            'csv': ['csv'],                                                           # return csv if extension == csv
            'ini': ['cfg', 'conf', 'ini'],                                            # return ini if extension == cfg | conf | ini
            'json': ['json'],                                                         # return json if extension == json
            'txt': ['nfo', 'text', 'txt'],                                            # return txt if extension == nfo | text | txt
            'yaml': ['yaml', 'yml']                                                   # return yaml if extension == yaml | yml
        }

        file_extension = path_to_file.suffix[1:]                                      # get the extension and remove the '.' from the name
        if file_extension == '':                                                      # if the path has no extension
            raise AttributeError(f'No extension provided for path {file_extension}')  # raise the error

        if verify_only:                                                               # if only verifying
            return                                                                    # return here with nothing

        for std_type, alt_types in supported_file_extensions.items():                 # begin check against alt_types
            if file_extension in alt_types:                                           # if the file_extension is one of the alt_types
                return std_type                                                       # return the normlaized std_typeß

        raise TypeError(f"File extension '{file_extension}' is not supported.")       # if no conditions are met then return error

    @staticmethod
    def _get_path_owner(owner_id: int, id_type: str) -> Union[int, None, NoReturn, str]:
        """
        Convert user and group uid to a name. Only works for non-Windows platforms.

        Args:
            owner_id (str): the uid as reported by os.stat
            id_type (str): the type of id to resolve. user or group

        Returns:
            (str): the translated owner id. if the platform is Windows then the uid will be returned back
        """

        if platform.system() == 'Windows':                               # if running on a Windows machine
            return owner_id                                              # return back the id

        else:                                                            # if anything other than Windows
            owner_name = {
                'user': lambda: getpwuid(owner_id).pw_name,              # user owner of the path
                'group': lambda: getgrgid(owner_id).gr_name              # group owner of the path
            }.get(id_type, lambda: None)()                               # check for the id_type or return None

            if owner_name is None:                                       # if the owner_name not in the map
                raise KeyError(f'{id_type} is not a valid owner type.')  # raise an error

            return owner_name                                            # return the translated owner name

    @staticmethod
    def _read_csv_file(path_to_file: Union['Path', str], options: Dict[str, Any] = dict()) -> Union[List[Union[dict[str, str], List[str]]], NoReturn]:
        """
        Read in the contents of a .csv file and return as a list of dictionaries.

        Args:
            path_to_file (Path | str): path to json file

        Optional Args:
            options (dict): options to control the way a csv file is read; default: no options set
                Available Options:
                    no_headers: set to True if the csv does not have headers

        Returns:
            (list): default is list of dictionaries
                (list of dicts) returns list of dictionaries if no_headers option is not set or is False
                (list of lists) return list of lists if no_headers option is set to True

        """

        if not options:                                                    # if no options specified then create default
            options = {
                'no_headers': False                                        # require headers by default
            }

        index = int(0)                                                     # index used to validate headers only one time
        contents = []                                                      # place holder for all csv contents
        with open(path_to_file, encoding='utf-8') as infile:               # open the file
            csvReader = csv.DictReader(infile)                             # read the csv file

            for rows in csvReader:                                         # begin loop over all csv rows
                if index == 0:
                    index += 1                                             # increment the index so we dont check again
                    if None in rows.keys() and not options['no_headers']:  # check that all columns have a header
                        # if a column has no header then raise the error
                        raise IndexError(f'Column header not defined for all columns. File: {path_to_file}')

                    elif options['no_headers']:                              # if no_headers is True
                        contents.append([value for value in rows.keys()])    # rows.keys is equal to the values from row one
                        contents.append([value for value in rows.values()])  # rows.values is equal to the values from the second row
                        continue                                             # skip to row 3

                if options['no_headers']:                                  # if no_headers is True
                    contents.append([value for value in rows.values()])    # append the values only

                else:
                    contents.append(rows)                                  # add the row to content
        infile.close()                                                     # close the file

        return contents                                                    # return

    @staticmethod
    def _read_ini_file(path_to_file: Union['Path', str]) -> dict[str, dict[str, str]]:
        """
        Read in the contents of an .ini file and return as a dictionaries.

        Args:
            path_to_file (Path | str): path to ini file

        Returns:
            (dict): ini contents read in as a dictionary
        """

        config = configparser.ConfigParser()               # define config object
        try:
            config.read(path_to_file)                      # read in the config file

            contents = {}                                  # place holder to store results
            for section in config.sections():              # begin to loop over the sectionn
                contents[section] = {}                     # store the section as a dictionary key
                contents[section].update(config[section])  # store the contents of each section in the section key

            return contents                                # return

        except configparser.ParsingError as error:         # if invalid ini format
            raise error                                    # raise error

    @staticmethod
    def _read_json_file(path_to_file: Union['Path', str]) -> Union[Any, NoReturn]:
        """
        Read in the contents of a json file and return a dictionary.

        Args:
            path_to_file (Path | str): path to json file

        Returns:
            (dict): json contents read in as a dictionary

        Raises:
            JSONDecodeError: invalid JSON format
        """

        try:
            with open(path_to_file, 'r') as infile:  # read in file
                contents = json.load(infile)         # load contents as json
            infile.close()                           # close the file

            return contents                          # return

        except JSONDecodeError as error:             # if the contents are not in valid json format
            raise error                              # raise the error

    @staticmethod
    def _read_txt_file(path_to_file: Union['Path', str]) -> list[str]:
        """
        Read in the contents of a .txt file and return each line as a string in a list.

        Args:
            path_to_file (Path | str): path to txt file

        Returns:
            (dict): list of strings
        """

        with open(path_to_file, 'r') as infile:                 # open the file
            contents = infile.readlines()                       # read in all the lines from the file
            contents = [line.strip('\n') for line in contents]  # trim newline characters from each line
        infile.close()                                          # close the file

        return contents                                         # return

    @staticmethod
    def _read_yaml_file(path_to_file: Union['Path', str]) -> Any:
        """
        Read in the contents of a .yaml file and return the contents as a dictionary.

        Args:
            path_to_file (Path | str): path to yaml file

        Returns:
            (dict): yaml contents read in as a dictionary
        """

        try:
            with open(path_to_file, 'r') as infile:                   # open the file
                contents = yaml.load(infile, Loader=yaml.FullLoader)  # load the contents as json
            infile.close()                                            # close the file

            return contents                                           # return

        except ScannerError as error:                                 # if invalid yaml format
            raise error                                               # raise error

        except ParserError as error:                                  # if invalid yaml format
            raise error                                               # raise error

    def _verify_path_exists(self, path_to_verify: 'Path') -> Union[bool, NoReturn]:
        """
        Validate if the given path exists.

        This function is not meant to be accessed directly but users but instead
        meant as a utility for validating other library functionality.

        Args:
            path_to_verify (Path): pathlib.Path to validate

        Returns:
            (bool): defaults to False
                True: return True if the path exists
                False: return False if the path does not exist

        Raises:
            FileNotFoundError: not a valid path
        """

        if path_to_verify.exists():  # if the path is valid
            return True              # return true

        else:                        # else - raise error
            raise FileNotFoundError(f"'{path_to_verify}' is not a valid path")

    def _verify_path_size(self, path_to_verify: 'Path') -> Union[bool, NoReturn]:
        """
        Verify that the path is a file and has contents.

        Args:
            path_to_verify (Path | str): path to the file to verify

        Returns:
            (bool): returns True if the path has contents

        Raises:
            EOFError: no contents to read
        """

        if os.stat(path_to_verify).st_size > 0:  # if the size of the file is greater than 0
            return True                          # return true

        else:                                    # else - raise error
            raise EOFError(f"'{path_to_verify}' does not contain any contents.")

    @staticmethod
    def _write_csv_file(contents: Any, path_to_outfile: Union['Path', str]) -> None:
        """
        Write the contents to csv file.

        Args:
            contents (Any): contents to write to the file
            path_to_outfile (Path | str): path to the file to write contents to

        Raises:
            JSONDecodeError: invalid JSON format
        """

        try:                                          # begin verification of the contents
            if isinstance(contents, dict):            # if the contents are of type dict
                contents = [contents]                 # then wrap the dictionary into a list

            elif isinstance(contents, list):          # if the contents are of type list
                for record in contents:               # begin to check each record in the list
                    if not isinstance(record, dict):  # if the record is not of type dict
                        json.loads(record)            # verify the contents are a valid json format

            else:                                     # if not of type dict or list
                json.loads(contents)                  # verify the contents are a valid json format

        except JSONDecodeError as error:              # if the contents are not in valid json format
            raise error                               # raise the error

        with open(path_to_outfile, 'w') as outfile:   # open the file for writing
            csv_writer = csv.writer(outfile)          # create the csv writer object

            index = int(0)                            # index placeholder
            for record in contents:                   # being checking each record from contents
                if index == 0:                        # if checking the first record
                    header = record.keys()            # set the headers equal to the keys of the first record
                    csv_writer.writerow(header)       # write the headers to the csv writer object
                    index += 1                        # increment the index

                csv_writer.writerow(record.values())  # write the values of each record to the csv writer object

        outfile.close()                               # close the file

    @staticmethod
    def _write_ini_file(contents: Any, path_to_outfile: Union['Path', str]) -> None:
        """
        Write the contents to ini file.

        Args:
            contents (Any): contents to write to the file
            path_to_outfile (Path | str): path to the file to write contents to

        Raises:
            JSONDecodeError: invalid JSON format
        """

        try:
            if not isinstance(contents, dict):       # if the contents are not of type dict
                json.loads(contents)                 # verify the contents are still a valid json format

        except JSONDecodeError as error:             # if the contents are not in valid json format
            raise error                              # raise the error

        config = configparser.ConfigParser()         # create config object
        config.update(contents)                      # load the contents into the config object

        with open(path_to_outfile, 'w') as outfile:  # open the file for writing
            config.write(outfile)                    # write contents to the file
        outfile.close()                              # close the file

    @staticmethod
    def _write_json_file(contents: Any, path_to_outfile: Union['Path', str]) -> None:
        """
        Write the contents to json file.

        Args:
            contents (Any): contents to write to the file
            path_to_outfile (Path | str): path to the file to write contents to

        Raises:
            JSONDecodeError: invalid JSON format
        """

        try:                                                                       # begin format verification
            if not isinstance(contents, dict) and not isinstance(contents, list):  # if the contents are of type dict or type list
                json.loads(contents)                                               # verify the contents are of valid json format

        except JSONDecodeError as error:                                           # if the contents are not in valid json format
            raise error                                                            # raise the error

        with open(path_to_outfile, 'w') as outfile:                                # open the file for writing
            json.dump(contents, outfile, indent=4)                                 # write the dictionary to the file
        outfile.close()                                                            # close the file

    @staticmethod
    def _write_txt_file(contents: Any, path_to_outfile: Union['Path', str]) -> None:
        """
        Write the contents to txt file.

        Args:
            contents (Any): contents to write to the file
            path_to_outfile (Path | str): path to the file to write contents to

        Raises:
            TypeError: contents is not a string or list of strings
        """

        if not isinstance(contents, str) and not isinstance(contents, list):   # if the contents are not a string or list of strings
            raise TypeError('Text is not a valid string or list of strings.')  # raise the error

        if isinstance(contents, str):                                          # if the contents are a string
            contents = contents.split('\n')                                    # then split the contents by newlines

        with open(path_to_outfile, 'w') as outfile:                            # open th file for writing
            for line in contents:                                              # begin looping over each line
                outfile.write(line)                                            # write the line to the file
                outfile.write('\n')                                            # write a new line
        outfile.close()                                                        # close the file

    @staticmethod
    def _write_yaml_file(contents: Any, path_to_outfile: Union['Path', str]) -> None:
        """
        Write the contents to yaml file.

        Args:
            contents (Any): contents to write to the file
            path_to_outfile (Path | str): path to the file to write contents to
        """

        with open(path_to_outfile, 'w') as outfile:  # open the file for writing
            yaml.dump(contents, outfile)             # write the contents to the file
        outfile.close()                              # close the file

    def create_new_directory(self, dir_to_create: Union['Path', str]) -> None:
        """
        Create a new directory.

        Args:
            dir_to_create (Path | str): path to the directory to create
        """

        dir_to_create = self._convert_path_type(dir_to_create)  # normalize the path
        dir_to_create.mkdir(parents=True, exist_ok=True)        # create the directory

    def create_new_file(self, file_to_create: Union['Path', str]) -> None:
        """
        Create a new file.

        Args:
            file_to_create (Path | str): path to the file to create
        """

        file_to_create = self._convert_path_type(file_to_create)    # normalize the path
        self._get_file_extension(file_to_create, verify_only=True)  # verify the file path has an extension
        file_to_create.touch(exist_ok=True)                         # create the file

    def get_directory_contents(self, path_to_directory: Union['Path', str], recursive: bool = False) -> Dict[str, Any]:
        """
        List the contents of a single directory or all directories recursively.

        Args:
            path_to_directory (Path | str): path to the directory
            recursive (bool): set to True to recursively list all contents of each directory in and under the given path; defaults to False

        Returns:
            (dict): dictionary of the folders and files
        """

        path_to_directory = self._convert_path_type(path_to_directory)                  # normalize the path

        contents = {                                                                    # create the contents container
            path_to_directory.name: {                                                   # use the path name as parent key
                'directories': [] if recursive is False else {},                        # if recursive is False the list directories else create a dict to gather the contents
                'files': []                                                             # store file names in a list
            }
        }

        if self._verify_path_exists(path_to_directory) and path_to_directory.is_dir():  # if the path exists and the path is a directory
            for item in path_to_directory.iterdir():                                    # check each item in the directory
                sub_name = 'files'                                                      # default sub_name to files
                if item.is_dir():                                                       # is the current item a directory?
                    sub_name = 'directories'                                            # if yes then change sub_name to directory

                    if recursive:                                                       # if the item is a directory and recursive is True
                        contents[path_to_directory.name][sub_name] = self.get_directory_contents(item, recursive)  # get the contents of the current directory
                        continue

                contents[path_to_directory.name][sub_name].append(item.name)            # add the file name to the list

        return contents                                                                 # return the contents

    def get_path_stats(self, filepath: Union['Path', str], timezone: str = 'UTC') -> dict[str, str]:
        """
        Get additional file system details about a directory or file.

        Example timezones:
            * 'America/New_York'
            * 'US/Western'
            * 'Europe/London'
            * 'Australia/Adelaide'
            * 'Africa/Johannesburg'

        Args:
            filepath (Path | str): path to the directory or file
            timezone (str): specific timezone for date and timestamps; default is UTC

        Returns:
            (dict): file system details about the path provided
                {
                    type: file or directory
                    st_mode: read|write|execute permissions
                    st_uid: user owner of the path
                    st_gid: group owner of the path
                    st_size: size in bytes
                    st_atime: time of most recent access in seconds
                    st_mtime: time of most recent content modification in seconds
                    st_ctime: time of most recent metadata change on Unix and creation time on Windows in seconds
                }
        """

        converted_path = self._convert_path_type(filepath)                                                # normalize from str to Path
        self._verify_path_exists(converted_path)                                                          # verify the path is valid
        stats = converted_path.stat()                                                                     # get the filesystem stats of the path

        file_stats = {
            'type': 'file' if converted_path.is_file() else 'directory',                                  # file or directory
            'st_mode': stat.filemode(stats.st_mode),                                                      # read|write|execute permissions
            'st_uid': self._get_path_owner(stats.st_uid, 'user'),                                         # user owner of the path
            'st_gid': self._get_path_owner(stats.st_gid, 'group'),                                        # group owner of the path
            'st_size': stats.st_size,                                                                     # size in bytes
            'st_atime': pendulum.from_timestamp(stats.st_atime, timezone).format('YYYY-MM-DD HH:MM:SS'),  # time of most recent access in seconds
            'st_mtime': pendulum.from_timestamp(stats.st_atime, timezone).format('YYYY-MM-DD HH:MM:SS'),  # time of most recent content modification in seconds
            'st_ctime': pendulum.from_timestamp(stats.st_atime, timezone).format('YYYY-MM-DD HH:MM:SS')   # time of most recent metadata change on Unix and creation time on Windows in seconds
        }

        return file_stats                                                                                 # return

    def read_file(self, file_to_read: Union['Path', str], options: Dict[str, Any] = {}) -> Any:
        """
        Read in a file and get the contents. Supports the following file types:

        * .csv
        * .cfg, .conf, .ini
        * .json
        * .nfo, .text, .txt
        * .yaml, .yml

        Args:
            file_to_read (Path | str): path to the file to get contents from

        Returns:
            * csv: list of dicts
                * no_headers (option): list of lists
            * cfg, conf, ini: dict
            * json: dict
            * nfo, text, txt: list
            * yaml, yml: dict

        Raises:
            FileNotFoundError: file does not exist
            TypeError: the path is not to a file
        """

        file_to_read = self._convert_path_type(file_to_read)                      # normalize from str to Path

        if self._verify_path_exists(file_to_read):                                # confirm the path is valid
            if file_to_read.is_file():                                            # confirm the path is a file
                if self._verify_path_size(file_to_read):                          # confirm the file has contents
                    file_extension = str(self._get_file_extension(file_to_read))  # get the extension of the file

                    contents = {                                                  # -- extension to function map --
                        'csv': lambda: self._read_csv_file(file_to_read, options),    # read csv contents
                        'ini': lambda: self._read_ini_file(file_to_read),             # read ini contents
                        'json': lambda: self._read_json_file(file_to_read),           # read json contents
                        'txt': lambda: self._read_txt_file(file_to_read),             # read txt contents
                        'yaml': lambda: self._read_yaml_file(file_to_read)            # read yaml contents
                    }.get(file_extension)()                                       # trigger the appropriate read method based on the file extension

                    return contents                                               # return the contents

            else:                                                                 # if the path is not a file
                raise TypeError(f"'{file_to_read}' is not a file.")               # raise error
        else:                                                                     # if the path does not exist
            raise FileNotFoundError(f"'{file_to_read}' does not exist.")          # raise error

    def remove_directory(self, dir_to_rm: Union['Path', str], force: bool = False) -> None:
        """
        Remove a directory and all of its contents.

        Args:
            dir_to_rm (Path | str): path to directory

        Optional Args:
            force (bool): do not prompt for confirmation; defaults to False
        """

        dir_to_rm = self._convert_path_type(dir_to_rm)                        # normalize from str to Path
        self._verify_path_exists(dir_to_rm)                                   # confirm the path exists

        if dir_to_rm.is_dir():                                                # confrim the path is a directory
            confirmation = None                                               # place holder for confirmation
            if not force:                                                     # check for force flag
                while isinstance(confirmation, type(None)):                   # loop until confirmation is not None
                    # prompt for user input
                    user_input = input(f"Remove '{dir_to_rm}' and all of its contents? (q to quit) [y/n]: ")
                    confirmation = _validation_util._validate_confirmation_inputs(user_input)            # validate the user input

            if force or confirmation:                                                                    # if force flag exists or confirmation is True
                shutil.rmtree(dir_to_rm)                                                                 # remove the directory
                _rich_util.console_log(f"Remove directory: '{dir_to_rm}' successful.", 'informational')  # print the deletion to the console

    def remove_file(self: 'FileMuncher', file_to_rm: Union['Path', str], force: bool = False) -> None:
        """
        Remove a file.

        Args:
            file_to_rm (Path | str): path to file

        Optional Args:
            force (bool): do not prompt for confirmation; defaults to False
        """

        file_to_rm = self._convert_path_type(file_to_rm)                                  # normalize from str to Path
        self._verify_path_exists                                                          # confirm the path exists

        if file_to_rm.is_file():                                                          # confirm the path is a file
            confirmation = None                                                           # place holder for confirmation
            if not force:                                                                 # check for force flag
                while isinstance(confirmation, type(None)):                               # loop until confirmation is not None
                    user_input = input(f"Remove '{file_to_rm}'? (q to quit) [y/n]: ")     # prompt for user input
                    confirmation = _validation_util._validate_confirmation_inputs(user_input)  # validate the user input

            if force or confirmation:                                                                # if force flag exists or confirmation is True
                os.remove(file_to_rm)                                                                # remove the file
                _rich_util.console_log(f"Remove file: '{file_to_rm}' successful.", 'informational')  # print the deletion to the console

    def rotate_files(self, directory_to_clean: Union['Path', str], days_old: int = 14, force: bool = False) -> None:
        """
        Remove files from a directory older than the specified days.
        Files older than the days_old parameters will be removed.

        Args:
            directory_to_clean (Path | str): path to directory to remove files from

        Optional Args:
            days_old (int): number of days worth of files to keep; defaults to 14 days
            force (bool): do not prompt for confirmation; defaults to False
        """

        directory_to_clean = self._convert_path_type(directory_to_clean)                  # normalize from str to Path
        self._verify_path_exists(directory_to_clean)                                      # confirm the path exists

        today = datetime.today()                                                          # get today's date
        all_files_to_remove = list()                                                      # place holder for old files
        for sub_file in directory_to_clean.iterdir():                                     # begin loop through the provided directory
            if sub_file.is_file():                                                        # confirm sub_file is a file
                modified_date = datetime.fromtimestamp(os.path.getmtime(sub_file))        # get the lat modified date from the sub file
                file_age = today - modified_date                                          # calculate the file age

                if file_age.days > days_old:                                              # if the file is older than (14) days
                    all_files_to_remove.append(                                           # add the old file to the list of files to remove
                        (sub_file.name, str(modified_date))                               # add name and last modified date as a tuple
                    )

                elif days_old == 0:                                                       # if days old is 0 add all files
                    all_files_to_remove.append(                                           # add each file to the list of files to remove
                        (sub_file.name, str(modified_date))                               # add name and last modified date as a tuple
                    )

        if len(all_files_to_remove) > 0:                                                  # if old files were found
            confirmation = None                                                           # place holder for confirmation
            if not force:                                                                 # check for force flag
                _rich_util.console_log('-- FILES TO REMOVE --', 'warning')                # print header to connsole
                _rich_util.console_log(f'Source path: {directory_to_clean}')              # print source path to console
                # print the files to remove as a table
                _rich_util.print_table(sorted(all_files_to_remove, reverse=True), ['File Name', 'Last Modified Date'], len(all_files_to_remove))

                while isinstance(confirmation, type(None)):                                     # loop until confirmation is not None
                    user_input = input('The above files will be removed. Continue? [y/n] (q to quit): ')  # prompt for user input
                    confirmation = _validation_util._validate_confirmation_inputs(user_input)             # validate the user input

            elif force or confirmation:                                                         # if force flag exists or confirmation is True
                while _rich_util.task_processing('Cleaning up old files'):                      # show processing spinner and message
                    for old_file in all_files_to_remove:                                        # begin loop over each file to delete
                        self.remove_file(Path.joinpath(directory_to_clean, old_file[0]), True)  # delete the old file
                    break                                                                       # break the loop and stop the spinner

        else:
            _rich_util.console_log(f'No files older than {days_old} days old found. Nothing to remove.', 'informational')

    def update_path(self, attribute_name: str, attribute_path: Union['Path', str], is_dir: bool = False, is_file: bool = False) -> Union[None, NoReturn]:
        """
        Add a new attribute to the Files object and store a Path value or update an existing path.
        Optionally, create the path at the same time as assigning the attribute.

        Args:
            attribute_name (str): name of the attribute to reference the path from the Files object
            attribute_path (str): string path to assign to the attribute

        Optional Args:
            is_dir (bool): set to True to create the path as a directory; defaults to False
            is_file (bool): set to True to create the path as a file; defaults to False

        Raises:
            TypeError: raised if both is_dir and is_file are True
        """

        converted_path = self._convert_path_type(attribute_path)                                   # normalize from str to Path
        if getattr(self, attribute_name, None) is not None:
            setattr(self, attribute_name, converted_path)                                          # create new Files attribute to provided attribute_path

        else:
            self.custom_path[attribute_name] = converted_path

        if is_dir and is_file:                                                                     # if both is_dir and is_file flags are True
            raise TypeError('Both is_dir and is_file are true. Only one option may be selected.')  # raise error

        elif is_dir:                                                                               # if only is_dir flag is True
            self.create_new_directory(converted_path)                                              # create the path directory

        elif is_file:                                                                              # if only the is_file flag is True
            self._get_file_extension(converted_path, verify_only=True)
            self.create_new_file(converted_path)                                                   # create the path as a file

    def write_file(self: 'FileMuncher', contents: Any, path_to_outfile: Union['Path', str]) -> None:
        """
        Update or create a new file with contents. Supports the following file types:

        * .csv
        * .cfg, .conf, .ini
        * .json
        * .nfo, .text, .txt
        * .yaml, .yml

        Args:
            contents (Any): contents to write to the file
            path_to_outfile (Path | str): path to file to write the contents
        """

        path_to_outfile = self._convert_path_type(path_to_outfile)                  # normalize from str to Path
        file_extension = str(self._get_file_extension(path_to_outfile))             # get the extension of the file

        {                                                                           # -- extension to function map --
            'csv': lambda: self._write_csv_file(contents, path_to_outfile),             # write csv contents
            'ini': lambda: self._write_ini_file(contents, path_to_outfile),             # write ini contents
            'json': lambda: self._write_json_file(contents, path_to_outfile),           # write json contents
            'txt': lambda: self._write_txt_file(contents, path_to_outfile),             # write txt contents
            'yaml': lambda: self._write_yaml_file(contents, path_to_outfile)            # write yaml contents
        }.get(file_extension)()                                                     # trigger the appropriate write method based on the file extension


# Functions to create and fetch the global objects


def create_global_files_object() -> 'FileMuncher':
    """
    Instantiate a global Files object.

    Returns:
        (Files): instantiated Files object
    """

    global FILES_OBJ           # declare the global
    FILES_OBJ = FileMuncher()  # assign the global

    return FILES_OBJ           # return


def get_global_files_object() -> 'FileMuncher':
    """
    Get the global Files object without instantiating a new instance.

    Returns:
        (Files): instantiated Files object

    Raises:
        NameError: raised if FILES_OBJ has not been created
    """

    if 'FILES_OBJ' not in globals():  # if the FILES_OBJ has not been created
        # raise error
        raise NameError("A global Files object has not yet been instantiated. Use 'create_global_files_object' to create one.")

    return FILES_OBJ                  # return the already instantiated FILES_OBJ
