import csv
from _csv import writer
from datetime import datetime
from typing import List, TextIO, Callable, Any, BinaryIO, Optional

CsvWriteFunction = Callable[[BinaryIO], Any]


class CsvWriter:
    """Factory class for generating and exporting CSV files"""
    _headers: List[str]
    _file: TextIO
    _report_writer: writer
    _file_name: str
    _path: str

    def __init__(self, file_name: str, headers: List[str], write_dir: str, *, suffix: Optional[str] = None,
                 prefix: Optional[str] = None, append_date_stamp: Optional[bool] = False):
        """Inits CsvWriter

        Args:
            file_name (str): The core of the csv file name (without affixes)
            headers (List[str]): List of CSV column headers
            write_dir (str): path to directory where files will be written

        Keyword Args:
            prefix (Optional[str]): A prefix to prepend to the filename
            suffix (Optional[str]): A suffix to append to the filename
            append_date_stamp (Optional[bool]): append a date stamp to the filename (default is False)
        """
        self._headers = headers
        now_datetime = datetime.now()

        filename_prefix = f"{prefix}-" if prefix else ""

        filename_suffix = f"-{suffix}" if suffix else ""

        date_stamp = (
            f"-{now_datetime.year}_{now_datetime.month}_{now_datetime.day}_{now_datetime.hour}_{now_datetime.minute}"
            f"_{now_datetime.second}"
        ) if append_date_stamp else ""

        self._file_name = f"{filename_prefix}{file_name}{filename_suffix}{date_stamp}.csv"
        write_dir_path = write_dir if write_dir[-1] == "/" else f"{write_dir}/"
        self._path = f"{write_dir_path}{self._file_name}"
        self._file = open(self._path, mode='w')

        self._report_writer = csv.writer(self._file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        self._report_writer.writerow(self._headers)

    def add_row(self, row_list: List[Any]):
        """Add a row of data to the CSV file

        Args:
            row_list (List[Any]): The data to be written, ordered according to the CSV file headers
        """
        self._report_writer.writerow(row_list)

    def close(self):
        """Close the CSV file. Prevents additional updates."""
        self._file.close()

    def export_csv(self, write_func: CsvWriteFunction) -> Any:
        """Export the CSV file to a data store

        Args:
            write_func (Callable[[BinaryIO], Any]): The function to export the CSV
        """
        self.close()
        with open(self._path, 'rb') as data:
            return write_func(data)
