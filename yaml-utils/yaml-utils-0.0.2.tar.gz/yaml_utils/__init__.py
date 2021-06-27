__version__ = '0.0.2'

import os
import yaml


def __obtain_data(d, target_key, parent_key=None):
    """
    Method to get parent key and value of target for passed target key
    :param d: dict or list[dict]
    :param target_key: str
    :param parent_key: None -> in run time value will be assigned recursively
    """
    if parent_key is None and isinstance(d, list):
        for data in d:
            for k, v in data.items():
                if k == target_key:
                    yield [parent_key, v]
                if isinstance(v, dict):
                    for res in __obtain_data(v, target_key, k):
                        yield res
    elif not isinstance(d, list):
        for k, v in d.items():
            if k == target_key:
                yield [parent_key, v]
            if isinstance(v, dict):
                for res in __obtain_data(v, target_key, k):
                    yield res


def get_parent_key_and_value(obj, target_key):
    """
    Method to get parent key and value of target for passed target key
    :param obj: dict or list[dict]
    :param target_key: str
    :return: list[str]
    """
    output_list = __obtain_data(obj, target_key).__next__()
    return output_list


def yaml_reader(file_path_list):
    """
    Method to read yaml files from passed file path list and return a list of file path
    :param file_path_list: list[str]
    :return: list[dict]
    """
    yaml_list = []
    if type(file_path_list) == "str":
        with open(r"{}".format(file_path_list)) as file:
            yml = yaml.load(file, Loader=yaml.FullLoader)
            yaml_list.append(yml)
            return yaml_list
    for filePath in file_path_list:
        with open(r"{}".format(filePath)) as file:
            yml = yaml.load(file, Loader=yaml.FullLoader)
            yaml_list.append(yml)
    return yaml_list


def get_file_list(dir_name):
    """
    Method to get list of files from directories and sub-directories
    :param dir_name: str
    :return: list[str]
    """
    # create a list of file and sub directories
    # names in the given directory
    list_of_file = os.listdir(dir_name)
    all_files = list()
    # Iterate over all the entries
    for entry in list_of_file:
        # Create full path
        full_path = os.path.join(dir_name, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(full_path):
            all_files = all_files + get_file_list(full_path)
        else:
            all_files.append(full_path)

    return all_files
