from google.cloud import bigquery, bigquery_datatransfer
from google.oauth2 import service_account
import datetime


class BigqueryHandler:

    def __init__(
            self,
            logger,
            project_id: str,
            service_account_file_path: str = '/defaultserviceaccount.json',
            bigquery_datetime_format: str = '%Y-%m-%d %H:%M:%S UTC',
            bigquery_date_format: str = '%Y-%m-%d',
    ):
        self.project_id = project_id
        self.bigquery_datetime_format = bigquery_datetime_format
        self.bigquery_date_format = bigquery_date_format

        cred = service_account.Credentials.from_service_account_file(service_account_file_path)
        self.client = bigquery.Client(project=self.project_id, credentials=cred)
        self.transfer_client = bigquery_datatransfer.DataTransferServiceClient(credentials=cred)
        self.logger = logger

    def get_list_from_query(self, querystr, params=None, job_config=None):
        if params is None:
            params = {}
        if any(params):
            for param in params:
                if type(params[param]) == datetime.datetime:
                    params[param] = params[param].strftime(self.bigquery_datetime_format)
                elif type(params[param]) == datetime.date:
                    params[param] = params[param].strftime(self.bigquery_date_format)
                else:
                    params[param] = str(params[param])
            query = querystr.format(**params)
        else:
            query = querystr
        if job_config:
            query_job = self.client.query(query, job_config=job_config)
        else:
            query_job = self.client.query(query)
        return list(query_job.result())

    def get_table(self, table_name):
        return self.get_list_from_query(querystr=f'select * from {table_name}')

    def get_column_names(self, dataset_name, table_name):
        dataset_ref = bigquery.DatasetReference(self.project_id, dataset_name)
        table_ref = bigquery.TableReference(dataset_ref, table_name)
        table = self.client.get_table(table_ref)
        cols = [f.name for f in table.schema]
        return cols

    def write_from_query(self, querystr, dataset_name, table_name):
        dataset_ref = bigquery.DatasetReference(self.project_id, dataset_name)
        table_ref = bigquery.TableReference(dataset_ref, table_name)
        table = self.client.get_table(table_ref)
        current_schema_len = len(table.schema)
        self.logger.info(f"start query write to table {str(table)} that contains {str(current_schema_len)} columns")
        job_config = bigquery.QueryJobConfig(destination=table,
                                             schema_update_options=[bigquery.SchemaUpdateOption.ALLOW_FIELD_ADDITION],
                                             write_disposition=bigquery.WriteDisposition.WRITE_APPEND)
        query_job = self.client.query(querystr, job_config=job_config)
        res = query_job.result()
        table = self.client.get_table(table_ref)
        self.logger.info(
            f"added {str(len(table.schema) - current_schema_len)} columns to table {str(table)}.")

    def execute_query(self, querystr):
        query_job = self.client.query(querystr)
        res = query_job.result()

    def export_table_to_gcs(self, dataset_name, table_name, bucket_name, file_name):
        destination_uri = f"gs://{bucket_name}/{file_name}"
        dataset_ref = bigquery.DatasetReference(self.project_id, dataset_name)
        table_ref = bigquery.TableReference(dataset_ref, table_name)
        extract_job = self.client.extract_table(
            table_ref,
            destination_uri,
            location="EU",
        )
        extract_job.result()
        self.logger.info(f"exported table {dataset_name}.{table_name} to gcs {bucket_name}.{file_name}")

    def update_views_query(self, view_dataset, view_name, query):
        view_id = self.project_id + "." + view_dataset + "."+ view_name
        view = bigquery.Table(view_id)
        view.view_query = query
        view = self.client.update_table(view, ["view_query"])
        self.logger.info(f"updated {view.table_type}: {str(view.reference)}")

    def schedule_query(
            self, query, dataset_name, display_name, table_name_template, schedule , write_disposition="WRITE_APPEND",
            partitioning_field=""
    ):
        parent = self.transfer_client.common_project_path(self.project_id)
        transfer_config = bigquery_datatransfer.TransferConfig(
            destination_dataset_id=dataset_name,
            display_name=display_name,
            data_source_id="scheduled_query",
            params={
                "query":query,
                "destination_table_name_template":table_name_template,
                "write_disposition": write_disposition,
                "partitioning_field": partitioning_field
            },
            schedule=schedule
        )
        transfer_config = self.transfer_client.create_transfer_config(
            bigquery_datatransfer.CreateTransferConfigRequest(
                transfer_config=transfer_config, parent=parent,
            )
        )
        self.logger.info(f"Created scheduled query {transfer_config.name}")

    def insert_rows(self, row_list, dataset_name, table_name):
        dataset_ref = bigquery.DatasetReference(self.project_id, dataset_name)
        table_ref = bigquery.TableReference(dataset_ref, table_name)
        table = self.client.get_table(table_ref)
        self.insert_rows_from_table(row_list, table)

    def insert_rows_from_table(self, row_list, table, batch_size=50):
        i = 0
        all_errors = []
        while i < len(row_list):
            rows = row_list[i:i + batch_size]
            i += batch_size
            all_errors.append(self.client.insert_rows(table, rows))
            if any(all_errors):
                self.logger.info(
                    "errors while writing row {} into bigquery with errors {}".format(str(rows[0]), str(all_errors)))

    def create_view(self, view):
        view_creation_query = f"""
        CREATE OR REPLACE VIEW {view['project']}.{view['dataset_name']}.{view['display_name']}_source
        AS
        {view['view_query']} 
        """
        self.execute_query(view_creation_query)

    def schedule_view_query(self, view):
        view = view.copy()
        view['table_name_template'] = view['display_name']
        if view['write_disposition'] == 'WRITE_EMPTY':
            view['table_name_template'] += '_{run_date}'
        view['query'] = f"SELECT * FROM {view['project']}.{view['dataset_name']}.{view['display_name']}_source"
        # non necessary arguments
        view.pop('view_query', None)
        self.schedule_query(
            **view
        )

    def create_functions(self, function):
        function_creation_query = f"""
                CREATE OR REPLACE FUNCTION `{function['project']}.{function['dataset_name']}.{function['display_name']}`({function['args']})
                AS(
                {function['function_query'].strip()}
                ) 
                """
        self.execute_query(function_creation_query)
