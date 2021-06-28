
import logging
import io
import functools
import joblib
from google.cloud import storage
import google.cloud.bigquery
import google.cloud.storage.blob
import pandas as pd
import tensorflow as tf
from tensorflow.python.lib.io import file_io
from mesh.connectors.base import GoogleConnector
from mesh.google.connectors import bigquery


log = logging.getLogger(__name__)


class GcsConnector(GoogleConnector):
    """
    a wee wrapper of the googl client
    """
    def __init__(self, project, **kwargs):
        """
        :param service_key_filename - if not provided, the assumption is already provided
        :param context: (optional) provide a mesh context for
        """
        super().__init__(project)
        self.client_gcsfs=None
        try:
            log.debug('connecting to gcs')
            self.service_key_file = kwargs['service_key_filename']
            self.client = storage.Client.from_service_account_json(self.service_key_file)
        except KeyError as e:
            self.client = storage.Client.create_anonymous_client()
            log.info('Please provide a service key file and project if you require a non-anonymous connection')
            log.info('anonymous key created')

    @property
    def client_gcsfs(self):  #todo is this still relevant
        self._client_gcsfs = gcsfs.GCSFileSystem(
            project=self.project,
            token=self.service_key_file
        )

    @client_gcsfs.setter
    def client_gcsfs(self, value):
        self._client_gcsfs = value


    def read_blob(self, bucket_name: str, blob_path: str) -> io.BytesIO:
        """
        Trivial wrapper to read a blob at a path from cloud storage
        This binary is kept in memory and a BytesIO buffer is returned
        :param bucket_name: a gcs bucket name
        :param path: path within the bucket for gcs
        :return: a blob object buffer
        """
        log.info(f'read from gs:\\{bucket_name}/{str}')
        bucket = self.client.get_bucket('{}'.format(bucket_name))
        gcs_object = bucket.blob(blob_path)
        buffer = io.BytesIO()
        gcs_object.download_to_file(buffer)
        # now that the buffer is populated, get cursor back to start
        buffer.seek(0)
        return buffer


    def read_joblib(self, bucket_name: str, blob_path: str):
        """
        Trivial wrapper to read an object serialised with joblib
        and located at <bucket_name>/<path> from cloud storage.
        :param bucket_name: a gcs bucket name
        :param path: path within the bucket for gcs
        :return: a blob object
        """
        log.debug(f'read from gs://{bucket_name}/{blob_path}')
        buffer = self.read_blob(bucket_name, blob_path)
        # now, deserialise it using joblib
        obj = joblib.load(buffer)
        return obj


    def _read_pandas_dataframe(self, bucket_name,
                               blob_path,
                               delimiter=',',
                               parse_dates=None) -> pd.DataFrame:
        """
        Read a csv file into a pandas dataframe
        :param filename: the filename (may include full path) of the csv file
        :param delimiter: a character delimiter for the csv file
        :param parse_dates: pass through to the pandas api
        :return: a pandas dataframe
        """
        with file_io.FileIO(f'gs://{bucket_name}/{blob_path}', 'r') as f:
            if parse_dates is not None:
                df = pd.read_csv(f, delimiter=delimiter, parse_dates=parse_dates)
            else:
                df = pd.read_csv(f, delimiter=delimiter)
            return df

    # this is broken now? later person not sure why - what a past person nincompoop
    # todo todo todo
    def read_pandas_dataframe(self, bucket_name, blob_path_pattern, delimiter=',', parse_dates=None):
        """
        Concatenate sharded csv files from a provided filename pattern
        :param filename_pattern: a filename pattern including a gcs location and ending in a '_*'
        :param delimiter: a csv delimiter, eg '|'
        :return: a pandas data frame
        """
        raise NotImplementedError('here be dragons - this stuff does not work')
        # # there is an issue with anonymous keys and listing in public buckets
        # filenames = tf.io.gfile.glob(blob_path_pattern)
        # dataframes = [_pandas_dataframe(filename, delimiter, parse_dates) for filename in filenames]
        # return pd.concat(dataframes)


    def read_string(self, bucket_name: str, blob_path: str):
        """
        read a string encoded as utf-8 in a bucket
        :param bucket_name: the name of the bucket in gcs
        :param blob_path: the full path of the blob in gcs (including filename)
        """
        bucket = self.client.bucket(bucket_name)
        return bucket.blob(blob_path).download_as_string().decode('utf-8')


    def write_string(self, bucket_name: str, blob_path: str, a_string: str):
        """
        write a string to gcs
        :param bucket_name: the name of a bucket in gcs
        :param blob_path: the path to (and including) the blob in gcs
        :param a_string: a string
        """
        bucket = self.client.bucket(bucket_name)
        string_buffer = io.StringIO(a_string)
        bucket.blob(blob_path).upload_from_string(string_buffer.read(), content_type="text/plain")
        string_buffer.close()

    def write_blob(self, bucket_name: str, blob_path: str,  obj: object):
        """
        :param obj:
        :param bucket_name:
        :param path:
        :return:
        """
        log.info(f'persisting to gs:\\{bucket_name}/{blob_path}')
        buffer = io.BytesIO()
        joblib.dump(obj, buffer)
        # rewind to the start of the bugger
        buffer.seek(0)

        # get bucket via the client
        bucket = self.client.bucket(bucket_name)
        blob = bucket.blob(blob_path)
        blob.upload_from_file(buffer)


    def write_local_file(self, bucket_name: str, blob_path: str, file: str):
        """
        Uploads a local file to the provided bucket
        :param bucket_name: a gcs bucket
        :param file: the location of the file in the local directory (including name)
        :param path: the desired location of the file in the provided gcs bucket
        """
        log.info(f'persisting to gs:\\{bucket_name}/{blob_path}')
        bucket = self.client.bucket(bucket_name)
        blob = bucket.blob(blob_path)
        blob.upload_from_filename(file)


    def write_pandas_dataframe(self, bucket_name: str,
                               blob_path: str,
                               data: pd.DataFrame,
                               delimiter=',',
                               file_type: str = 'csv'):
        """
        :param bucket_name: the bucket name in cloud storage
        :param blob_path: the blob path within storage
        :param data: the data frame that will be written
        :param delimiter: the element separator if csv file
        :param file_type: the file_type (at the moment we only support csv, alternatives are parquet)
        """

        log.info(f'Writing to gs://{bucket_name}/{blob_path}')
        bucket = self.client.get_bucket('{}'.format(bucket_name))
        if file_type == 'csv':
            bucket.blob(blob_path).upload_from_string(data.to_csv(index=False, sep=delimiter), file_type)
        else:
            raise NotImplementedException()



    def write_joblib(self, bucket_name: str, blob_path: str, obj: object, chunk_size_mb=None):
        """
        :param obj: an object in memory to write with joblib serialisation to a bucket
        :param bucket_name: a gcs bucket
        :param blob_path: the desired location of the file in the provided gcs bucket
        """
        log.info(f'persisting to gcs: {bucket_name}/{blob_path}')
        bucket = self.client.bucket(bucket_name)
        blob = bucket.blob(blob_path)
        if chunk_size_mb:
            blob.chunk_size = chunk_size_mb * 1024 * 1024 # 5 MB is good for local; default is 100MB

        buffer = io.BytesIO()
        joblib.dump(obj, buffer)
        buffer.seek(0)

        blob.upload_from_file(buffer)

    # this is a static method because it depends only on the bq connector,
    # and not on the gcs one - bit of an oddball this function
    @staticmethod
    def write_bq(bucket_name: str,
                    blob_path: str,
                    project: str,
                    dataset_name: str,
                    table_name: str,
                    connector: bigquery.BqConnector,
                    columns: list,
                    destination_format=google.cloud.bigquery.DestinationFormat.CSV,
                    destination_delimiter=','):
        """
        Creates a job to export a bigquery table to a gcs bucket
        :param bucket_name: The name of the bucket to export the table to
        :param blob_path: The name of the file in the specified bucket
        :param project: The project in which the biq query table is
        :param dataset_name: The dataset from which to export the table
        :param table_name: The table to be exported
        :param connector: a big query connection (these credentials are used)
        :param columns: The columns to export

        Presently, the credentials of the Big Query connection are used to access
        the big query and to write to Google Cloud Storage. This read and write
        (BQ --> GCS) happens within the same project.
        """
        columns = [columns] if isinstance(columns, str) else columns
        bq_name = '{project}.{dataset}.{table}'.format(project=project,
                                                       dataset=dataset_name,
                                                       table=table_name)
        log.info('loading data (bq: {}) into gcp storage bucket: {}'.format(
            bq_name,
            bucket_name)
        )

        # create query
        query = connector.client.query(r"""SELECT {columns} FROM `{name}`""".format(
            name=bq_name,
            columns=', '.join(columns)))
        log.info('bq query job_id: {}'.format(query.job_id))
        query.result()

        # create job config object
        job_config = google.cloud.bigquery.job.ExtractJobConfig()
        job_config.destination_format = (destination_format)
        job_config.field_delimiter = destination_delimiter

        destination_uri = "gs://{}/{}".format(bucket_name, blob_path)
        log.info('writing to: {}'.format(destination_uri))

        # dataset_ref = self.client.dataset(dataset_name, project=self.project)
        # table_ref = dataset_ref.table(table_name)

        extract_job = connector.client.extract_table(
            query.destination,
            destination_uri,
            location="EU",
            job_config=job_config
        )
        log.info('extract job_id: {}'.format(query.job_id))
        extract_job.result()
        log.info("Exported {}.{}.{} to {}".format(project, dataset_name, table_name, destination_uri))


class GcsConnect(GcsConnector):

    """
    fix a connection to a specific bucket_name and blob_name pair, whilst specifying
    how you would like it read into memory too. So, connect it specifically.
    """
    def __init__(self,
                project,
                service_key_filename,
                bucket_name,
                blob_name,
                data_type,
                path_conventions=None):
        super().__init__(project=project,
                         service_key_filename=service_key_filename)
        self.bucket_name = bucket_name
        self.__blob_name = blob_name
        self.data_type = data_type
        self.path_conventions = path_conventions


    @property
    def read(self):
        """
        read the data from the connection
        """
        return self._accessor()

    @property
    def write(self):
        """
        write data to the connection
        """
        return self._accessor(write=True)


    @property
    def blob_name(self):
        if self.path_conventions:
            return f'{self.path_conventions.storage_path()}/{self.__blob_name}'
        return self.__blob_name


    @blob_name.setter
    def blob_name(self, blob_name):
        self.__blob_name = blob_name


    def _accessor(self, write=False, **kwargs):
        """
        get a callable to the functions in this object that are linked to the
        data_type you would like to read and write to (e.g. gcs -> pandas and pandas -> gcs)
        :param kwargs: there to ignore all that is irrelevant
        """
        if self.data_type == 'pandas':
            func = self.write_pandas_dataframe if write else self._read_pandas_dataframe
        elif self.data_type == 'joblib':
            func = self.write_joblib if write else self.read_joblib
        elif self.data_type == 'string':
            func = self.write_string if write else self.read_string
        else:
            raise ValueError(f'no such datatype: "{self.data_type}"')
        return functools.partial(func, self.bucket_name, self.blob_name)

    
