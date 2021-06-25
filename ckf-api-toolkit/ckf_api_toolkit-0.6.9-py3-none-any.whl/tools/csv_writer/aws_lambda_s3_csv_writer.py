from typing import List, Optional, BinaryIO
from ckf_api_toolkit.tools.csv_writer import CsvWriter
import boto3

LAMBDA_WRITE_DIR = "/tmp/"
s3 = boto3.client('s3')


class AwsLambdaS3CsvWriter(CsvWriter):
    """Factory class for generating CSV files in AWS Lambda and exporting to S3. Inherits CsvWriter."""
    __bucket_name: str
    __key_prefix: str

    def __init__(self, file_name: str, headers: List[str], bucket_name: str, *, suffix: Optional[str] = None,
                 prefix: Optional[str] = None, append_date_stamp: Optional[bool] = False, key_prefix: Optional[str]):
        """Inits AwsLambdaS3CsvWriter

        Args:
            file_name (str): The core of the csv file name (without affixes)
            headers (List[str]): List of CSV column headers
            bucket_name (str): S3 bucket name

        Keyword Args:
            prefix (Optional[str]): A prefix to prepend to the filename
            suffix (Optional[str]): A suffix to append to the filename
            append_date_stamp (Optional[bool]): append a date stamp to the filename (default is False)
            key_prefix (Optional[str]): S3 key prefix (prepends to filename)
        """
        super(AwsLambdaS3CsvWriter, self).__init__(file_name, headers, LAMBDA_WRITE_DIR, suffix=suffix,
                                                   prefix=prefix, append_date_stamp=append_date_stamp)
        self.__bucket_name = bucket_name
        self.__key_prefix = key_prefix

    def __s3_export_function(self, data: BinaryIO) -> str:
        keyed_file_name = f"{self.__key_prefix}{self._file_name}" if self.__key_prefix else self._file_name
        s3.upload_fileobj(data, self.__bucket_name, keyed_file_name)
        return keyed_file_name

    def export_csv_to_s3(self) -> str:
        """Export the generated CSV to a file on AWS S3

        Returns:
            (str) the S3 key of the exported file
        """
        return self.export_csv(self.__s3_export_function)
