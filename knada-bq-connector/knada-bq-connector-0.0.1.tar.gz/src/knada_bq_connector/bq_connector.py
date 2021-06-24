import logging
from typing import Sequence

from google.cloud import bigquery
from google.oauth2 import service_account


class BigQueryConnector:
    """
    A wrapper for google BigQuery packages. Run BigQuery queries and get the results with metadata.

    """

    def __init__(self, credentials: any = None):
        """
        Init method for BigQueryConnector class

        :param credentials: The OAuth2 Credentials to use for this client. If not passed,
        falls back to the default inferred from the environment.
        """
        self._client = self._create_client(credentials=credentials)
        self._logger = self._create_logger()

    def execute_bq_query(self, sql: str) -> bigquery.job.QueryJob:
        """
        Executes any BigQuery query and returns data if any.

        :param sql: Either query string or path to query file.
        :return:  Return a QueryJob object.
        """
        query = self._load_sql(sql=sql)
        result = self._client.query(query)

        self._query_report(result=result)

        return result

    def insert_rows_bq(self, table_id: str, rows: list) -> Sequence[dict]:
        self._logger.info(f"Writing {len(rows)} rows to {table_id}")
        errors = self._client.insert_rows_json(table=table_id, json_rows=rows)

        if len(errors) == 0:
            self._logger.info(f"Successfully wrote {len(rows)} rows to {table_id}")

        return errors

    @staticmethod
    def format_data_as_records(data: bigquery.table.RowIterator) -> list:
        """
        Formats data in a RowIterator to a list of records.

        :param data: A BigQuery RowIterator
        :return:
        """
        return [{column_name: value for column_name, value in row.items()} for row in data]

    @staticmethod
    def _load_sql(sql: str) -> str:
        """
        Private method that loads a sql query from file or from a string.

        :param sql: A sql query string or path to file containing sql query.
        :return: The sql query
        """
        try:
            with open(file=sql, mode="r") as file:
                query = file.read()
        except FileNotFoundError:
            query = sql

        return query

    def _query_report(self, result: bigquery.job.QueryJob) -> None:

        """
        Private method that logs the result of BigQuery query job.

        :param result: A BigQuery QueryJob object, that contains the results of the query job.
        :return:
        """
        start = result.started

        project = result.project
        errors = result.errors

        if errors is None:
            number_errors = 0
        else:
            number_errors = len(errors)

        self._logger.info(f"BigQuery job started at {start} in {project} project. Number of errors {number_errors}.")

    @staticmethod
    def _create_client(credentials: any) -> bigquery.Client:
        """
        Private method that creates a BigQuery Client, from credentials.

        :param credentials: Either dict, str or None. If not passed,
        falls back to the default inferred from the environment.

        :return: A BiqQuery Client object.
        """
        if isinstance(credentials, str):
            return bigquery.Client.from_service_account_json(json_credentials_path=credentials)
        elif isinstance(credentials, dict):
            creds = service_account.Credentials.from_service_account_info(credentials)
            return bigquery.Client(credentials=creds, project=creds.project_id)
        else:
            return bigquery.Client()

    def _create_logger(self) -> logging.Logger:
        """
        Private method that creates a logger.
        :return: A logger.
        """
        logger = logging.getLogger(self.__class__.__name__)
        logger.setLevel(logging.INFO)

        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)

        logger.addHandler(handler)

        return logger
