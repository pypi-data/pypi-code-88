#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. current_module:: file_tool.py
.. created_by:: Darren Xie
.. created_on:: 04/25/2021

Collect File action tools
"""
import os
import re
import stat
import sys
from codecs import open
from datetime import datetime
from pathlib import Path
from typing import List
from shutil import rmtree

TIME_FORMAT = '%m/%d/%Y %H:%M:%S'
PERCENT_RE = re.compile(r'%(.+?)%')
FILE_TYPE_RE = re.compile(r'.*(\..+)$')


class FileTool:
    """
    Contain all tools for file action.
    1. Load config text file for environment variables
    2. Unit to Dos format conversion
    3. Dos ot Unit format conversion.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load_env(self, full_path):
        """
        Load environment vars by reading a config text file
        :param full_path: Path to the config text file.
        """
        try:
            with open(full_path, 'r') as in_fh:
                for line in in_fh:
                    line = str(line)
                    # skip comment line and lines without mark '='
                    if "#" in line or '=' not in line:
                        continue
                    line = line.strip()
                    key, value = line.split('=', 1)
                    key, value = key.strip(), value.strip().replace('\\', '/')

                    # Keep the following comment for future
                    # if '%' in value:
                    #     try:
                    #         while '%' in value:
                    #             try_k = re.search(PERCENT_RE, value).group(1)
                    #             value = re.sub(PERCENT_RE, os.environ[try_k].replace('\\', '/'), value, 1)
                    #     except Exception:
                    #         raise Exception(f"{try_k} not defined")
                    os.environ[key] = value.replace('/', '\\')
        except IOError:
            raise IOError(f"Cannot open file {full_path}")
        except Exception:
            raise Exception(f"Cannot open file {full_path}")

    def on_rm_error(self, func, path, exc_info):
        """
        This function is for shutil.rmtree() onerror=self.on_rm_error
        :param func:
        :param path:
        :param exc_info:
        :return:
        """
        # path contains the path of the file that couldn't be removed
        # let's just assume that it's read-only and unlink it.
        os.chmod(path, stat.S_IWRITE)
        os.unlink(path)

    def dos2unix(self, filename):
        """
        Convert Dos format to Unix format for EOF (\r\n to \n)
        :param filename: Full path to the file to be converted.
        """
        try:
            with open(filename, 'rb') as in_fh:
                text = in_fh.read().replace(b'\r\n', b'\n')
        except IOError as e:
            raise IOError(str(e))
        except Exception as e:
            raise Exception(str(e))
        with open(filename, 'wb') as out_fh:
            out_fh.write(text)

    def unix2dos(self, filename):
        """
        Convert Unix format to Dos format (\n to \r\n)
        :param filename: Full path to the file to be converted.
        """
        self.dos2unix(filename)
        try:
            with open(filename, 'rb') as in_fh:
                text = in_fh.read().replace(b'\n', b'\r\n')
        except IOError as e:
            raise IOError(str(e))
        except Exception as e:
            raise Exception(str(e))
        with open(filename, 'wb') as out_fh:
            out_fh.write(text)

    def _print_log(self, msg=''):
        """print out the log message"""
        sys.stdout.write(f"[{datetime.now().strftime(TIME_FORMAT)}]: {msg}\n")

    def unit2dos_recurs(self, root_path, file_types: [List] = None):
        """
        Convert Unix to Dos format recursively
        :param root_path: Passing in path for recursive conversion
        :param file_types: Limit files with specific types to be converted
        """
        # walk through all directories and files
        count = 0
        for dir_name, subdir_list, file_list in os.walk(root_path):
            for fname in file_list:
                if file_types:
                    find_type = re.search(FILE_TYPE_RE, fname)
                    if find_type:
                        file_type = find_type.group(1)
                        if file_type in file_types:
                            path_file = Path(dir_name).joinpath(fname)
                            self.unix2dos(path_file)
                            self._print_log(f"Converted {path_file}")
                            count += 1
                else:
                    path_file = Path(dir_name).joinpath(fname)
                    self.unix2dos(path_file)
                    self._print_log(f"Converted {path_file}")
                    count += 1

        self._print_log(f"Converted {count} files.")

    def dos2unix_recurs(self, root_path, file_types: [List] = None):
        """
        Convert Dos to Unix format recursively
        :param root_path: Passing in path for recursive conversion
        :param file_types: Limit files with specific types to be converted
        """
        # walk through all directories and files
        count = 0
        for dir_name, subdir_list, file_list in os.walk(root_path):
            for fname in file_list:
                if file_types:
                    find_type = re.search(FILE_TYPE_RE, fname)
                    if find_type:
                        file_type = find_type.group(1)
                        if file_type in file_types:
                            path_file = Path(dir_name).joinpath(fname)
                            self.dos2unix(path_file)
                            self._print_log(f"Converted {path_file}")
                            count += 1
                else:
                    path_file = Path(dir_name).joinpath(fname)
                    self.dos2unix(path_file)
                    self._print_log(f"Converted {path_file}")
                    count += 1

        self._print_log(f"Converted {count} files.")

    def update_string_in_file(self, old_string, new_string, to_file):
        """
        Update a line in a file.
        :param old_string: the target string in to_file to be updated
        :param new_string: the new string
        :param to_file: the target file
        """
        try:
            with open(str(to_file), 'r') as in_fh, \
                    open(f"{str(to_file)}_r", 'w') as out_fh:
                content = in_fh.read()
                if old_string in content:
                    new_content = content.replace(old_string, new_string)
                    out_fh.write(new_content)
                else:
                    self._print_log(f"Could not fine {old_string}")

            os.unlink(to_file)
            os.rename(f"{str(to_file)}_r", to_file)
        except IOError as e:
            self._print_log(f"Could open file: {to_file}")
        except Exception as e:
            self._print_log(f"Error: {str(e)}")

    def remove_folder(self, f_path):
        """
        Remove folder
        :param f_path: passing in folder
        """
        if Path(f_path).exists():
            rmtree(f_path, onerror=self.on_rm_error)
