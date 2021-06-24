# GoogleBigQuery Class
from google.cloud import bigquery
from googlewrapper.connect import Connection


class GoogleBigQuery:
    # GBQ connector class
    # Wrapper to the GBQ api
    # To initialize, pass in GBQ resource object
    # Normally authenticated through the Connection object
    def __init__(self, auth = Connection().gbq()):
        self._client = bigquery.Client(credentials=auth)
        self._project = auth.project_id
        self._dataset = None
        self._table = None

    def set_dataset(self, data_set_name: str) -> None:
        # Assigns the GBQ dataset
        self._dataset = data_set_name

    def set_table(self, table_name: str) -> None:
        # Assigns the GBQ table name
        self._table = table_name

    def full_table_name(self) -> str:
        # Combines self._dataset and self._table to
        # become the full table name in GBQ
        return f"{self._dataset}.{self._table}"

    def list_datasets(self) -> list:
        # returns all dataset ids/names in the authorized client
        return [x.dataset_id for x in list(self._client.list_datasets())]

    def send(self, df, chunk_size=10000, behavior="append", progress_bar=False):
        # sends a pd.Df into GBQ
        # Option to change chunk size, if you want to append or fail
        # if table already exists
        # and if you want to see a progresss bar
        try:
            df.to_gbq(
                destination_table=f"{self._dataset}.{self._table}",
                project_id=self._project,
                chunksize=chunk_size,
                if_exists=behavior,
                progress_bar=progress_bar,
            )
        except AttributeError as e:
            issue = e.args[0].split("'")[-2].replace("_", "")
            raise AttributeError(
                f"Please run self.set_{issue}"
                f"('your_{issue}_name_here') before running self.send()"
            )

    def read(self):
        # TODO read from a GBQ table
        pass

    def delete_day(self, date_to_delete,str_return = False):
        # deletes the passed in day from the
        # pre-determined table in GBQ
        query_string = f"""
        DELETE
        FROM `{self._project}.{self._dataset}.{self._table}`
        WHERE
        EXTRACT(Year FROM `Date`) = {date_to_delete.year}
        AND
        EXTRACT(Month FROM `Date`) = {date_to_delete.month}
        AND
        EXTRACT(Day FROM `Date`) = {date_to_delete.day}
        """

        if str_return:
            return query_string
            
        return self._client.query(query_string)
