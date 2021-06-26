from enum import Enum
from typing import List, Dict


class DataField:
    """
    Class representing a single CSV attribute field w/value
    """
    def __init__(self, azure_field_name, variable_name, value):
        self.azure_field_name = azure_field_name
        self.variable_name = variable_name
        self.value = value


class CSV:
    """
    Class representing a work item
    """
    def __init__(self,
                 csv_fields: List[DataField]):
        """
        :param csv_fields: List of the data fields that the csv object should have
        """
        self._csv_fields = csv_fields
        self.csv_header = ",".join([x.azure_field_name for x in csv_fields])
        self._var_names = [x.variable_name for x in csv_fields]
        self.__dict__.update({x.variable_name: x.value for x in csv_fields})

    def __str__(self):
        return ','.join([self.__dict__[k] for k in self.__dict__ if k in self._var_names])


def to_csv(filename, comment_data: List[str], tag_work_item_type_dict: Dict[str, str]):
    """
    Translates comment data to csv
    :param filename: The name of the file
    :param comment_data: Data corresponding to a singular comment
    :param tag_work_item_type_dict: A dict mapping codetags to work_item_types
    :return:
    """
    firstline = comment_data[0]
    title = ''.join(['_ag_', firstline])
    _x = [filename, '_ag_']
    _x.extend(comment_data)
    description = ' '.join(_x)

    _t = firstline.strip()
    _t = firstline.split(' ')
    firstword = _t[0]

    try:
        work_item_type = tag_work_item_type_dict[firstword]
    except KeyError:
        raise RuntimeError('The codetag %s does not exist in the CODETAG_TO_WORK_ITEM type dict in the config'%firstword)
    title = title.replace(',', ';')
    description = description.replace(',', ';')
    return CSV([
        DataField('Work Item Type', 'work_item_type', work_item_type),
        DataField('Title', 'title', title),
        DataField('Description', 'description', description)
    ])


def write_csv(output_path: str, comment_data: Dict[str, List[List[str]]],
              tag_work_item_type_dict: Dict[str, str]) -> None:
    """
    Given a dictionary with filenames to comments, write a csv file
    :param comment_data: dictionary with filenames to comments
    :param output_path: Where to write csv file to
    :param tag_work_item_type_dict: A dict mapping codetags to work_item_types
    """
    csvs = []
    for key in comment_data:
        for comment_lists in comment_data[key]:
            csvs.extend([to_csv(key, comment_lists, tag_work_item_type_dict)])
    with open(output_path, 'w') as f:
        to_write = [csvs[0].csv_header]
        to_write.extend([str(x) for x in csvs])
        to_write = [''.join([x, '\n']) for x in to_write]
        f.writelines(to_write)

