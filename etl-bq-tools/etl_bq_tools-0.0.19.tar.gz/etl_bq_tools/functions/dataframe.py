from etl_bq_tools.utils.time_execution import get_time_function_execution
from etl_bq_tools.utils import constants as cons


@get_time_function_execution
def upload_df_to_bq(
        project_id, table_full_id, key_path, partition_column=None,
        schema=None, df=None, if_exists="truncate", logging=None):
    """
     :param project_id: String
     :param table_full_id: String -> 'project.dataset.table'
     :param key_path: file.json
     :param partition_column: Date
     :param schema: dict
     :param df: Dataframe
     :param if_exists: String -> "append" or "truncate"
     :param logging: object
     :return:
    """
    from google.cloud import bigquery
    from google.api_core.exceptions import Conflict
    import pandas as pd
    from color_tools import cprint

    if not project_id:
        raise Exception('require var project_id: {project_id} ')
    if not table_full_id:
        raise Exception('require var table_full_id: {table_full_id} ')
    if not isinstance(df, pd.DataFrame):
        raise Exception('require var df: {df} ')
    if not if_exists:
        raise Exception('require var if_exists: {if_exists} ')

    client = bigquery.Client(project=project_id)
    if key_path:
        client = bigquery.Client.from_service_account_json(key_path)

    table_id = f"{table_full_id}"

    job_config = bigquery.LoadJobConfig()

    if partition_column:
        job_config.time_partitioning = bigquery.TimePartitioning(
            type_=bigquery.TimePartitioningType.DAY,
            field=partition_column,
            expiration_ms=None
        )

    if if_exists == "truncate":
        job_config.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE
    elif if_exists == "append":
        job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND

    if schema:
        job_config.schema = schema
    else:
        job_config.autodetect = True

    try:
        job = client.load_table_from_dataframe(
            df, table_id, job_config=job_config
        )
        job.result()

        if logging:
            logging.info(cons.txt_upload_df_to_bq_success.format(table_id))
            cprint(cons.txt_upload_df_to_bq_success.format(table_id), 'yellow')
        else:
            cprint(cons.txt_upload_df_to_bq_success.format(table_id), 'yellow')
    except Conflict:
        if logging:
            logging.info(cons.txt_upload_df_to_bq_errors.format(table_id))
            cprint(cons.txt_upload_df_to_bq_errors.format(table_id), 'yellow')
        else:
            cprint(cons.txt_upload_df_to_bq_errors.format(table_id), 'yellow')
