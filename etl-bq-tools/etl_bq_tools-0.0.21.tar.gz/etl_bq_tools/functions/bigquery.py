from etl_bq_tools.utils import constants as cons
from etl_bq_tools.utils.time_execution import get_time_function_execution


@get_time_function_execution
def bq_create_dataset(project_id=None,
                      dataset_id=None,
                      logging=None,
                      key_path=None):
    """This method is for create a dataset

    :param project_id: String
    :param dataset_id: String
    :param key_path: file.json
    :param logging: object
    :return: True
    """

    from google.cloud import bigquery
    from google.api_core.exceptions import Conflict
    from color_tools import cprint

    if not project_id:
        raise Exception('require var project_id:{project_id} ')
    if not dataset_id:
        raise Exception('require var dataset_id:{dataset_id} ')

    client = bigquery.Client(project=project_id)
    if project_id and key_path:
        client = bigquery.Client.from_service_account_json(key_path)

    dataset_id = f"{project_id}.{dataset_id}"
    dataset = bigquery.Dataset(dataset_id)
    dataset.location = "US"

    try:
        dataset = client.create_dataset(dataset, exists_ok=True)
        if logging:
            logging.info(cons.txt_create_dt_success.forma(f"{project_id}.{dataset.dataset_id}"))
            cprint(cons.txt_create_dt_success.forma(f"{project_id}.{dataset.dataset_id}"), "yellow")
        else:
            cprint(cons.txt_create_dt_success.forma(f"{project_id}.{dataset.dataset_id}"), "yellow")
        return True
    except Conflict:
        if logging:
            logging.info(cons.txt_create_dt_error.forma(f"{project_id}.{dataset.dataset_id}"))
            cprint(cons.txt_create_dt_error.format(f"{project_id}.{dataset.dataset_id}"), "yellow")
        else:
            cprint(cons.txt_create_dt_error.format(f"{project_id}.{dataset.dataset_id}"), "yellow")
        return None


@get_time_function_execution
def bq_delete_dataset(project_id=None,
                      dataset_id=None,
                      logging=None,
                      key_path=None):
    """This method is for delete a dataset

    :param project_id: String
    :param dataset_id: String
    :param logging: object
    :param key_path: file.json
    :return: True
    """

    from google.cloud import bigquery
    from google.cloud.exceptions import Conflict
    from color_tools import cprint

    if not project_id:
        raise Exception('require var project_id:{project_id} ')
    if not dataset_id:
        raise Exception('require var dataset_id:{dataset_id} ')

    client = bigquery.Client(project=project_id)
    if project_id and key_path:
        client = bigquery.Client.from_service_account_json(key_path)

    dataset_id = f"{project_id}.{dataset_id}"

    try:
        client.delete_dataset(dataset_id, delete_contents=True, not_found_ok=True)
        if logging:
            logging.info(cons.txt_delete_dt_success.format(dataset_id))
            cprint(cons.txt_delete_dt_success.format(dataset_id), "yellow")
        else:
            cprint(cons.txt_delete_dt_success.format(dataset_id), "yellow")
        return True
    except Conflict:
        if logging:
            logging.info(cons.txt_delete_dt_error.format(f"{project_id}.{dataset_id}"))
            cprint(cons.txt_delete_dt_error.format(f"{project_id}.{dataset_id}"), "yellow")
        else:
            cprint(cons.txt_delete_dt_error.format(f"{project_id}.{dataset_id}"), "yellow")
        return None


@get_time_function_execution
def bq_list_dataset(project_id=None,
                    logging=None,
                    key_path=None):
    """This method is for list a dataset

    :param project_id: String
    :param logging: object
    :param key_path: file.json
    :return: list dataset
    """

    from google.cloud import bigquery

    client = bigquery.Client(project=project_id)
    if project_id and key_path:
        client = bigquery.Client.from_service_account_json(key_path)

    datasets = list(client.list_datasets())

    data_list = list()
    if datasets:
        logging.info(f"Datasets in project {project_id}:")
        for dataset in datasets:
            data_dict = dict()
            data_dict["project_id"] = dataset.project
            data_dict["dataset_id"] = dataset.dataset_id
            data_list.append(data_dict)
            print(f"\t {dataset.project}.{dataset.dataset_id}")
    else:
        logging.info(f"{project_id} project does not contain any datasets.")

    return data_list


@get_time_function_execution
def bq_create_table(project_id=None,
                    dataset_id=None,
                    table_id=None,
                    schema=None,
                    logging=None,
                    key_path=None):
    """This method is for create table

    :param project_id: String
    :param dataset_id: String
    :param table_id: String
    :param schema: dict
    :param logging: object
    :param key_path: file.json
    :return: True
    """

    from google.cloud import bigquery
    from google.api_core.exceptions import Conflict
    from color_tools import cprint

    if not project_id:
        raise Exception('require var project_id: {project_id} ')
    if not dataset_id:
        raise Exception('require var dataset_id: {dataset_id} ')
    if not table_id:
        raise Exception('require var table_id: {table_id} ')
    if not schema:
        raise Exception('require var schema ')

    client = bigquery.Client(project=project_id)
    if project_id and key_path:
        client = bigquery.Client.from_service_account_json(key_path)

    table_id = f"{project_id}.{dataset_id}.{table_id}"
    table = bigquery.Table(table_id, schema=schema)

    try:
        table = client.create_table(table)
        if logging:
            logging.info(cons.txt_create_tb_success.format(f"{table.project}.{table.dataset_id}.{table.table_id}"))
            cprint(cons.txt_create_tb_success.format(f"{table.project}.{table.dataset_id}.{table.table_id}"), "yellow")
        else:
            cprint(cons.txt_create_tb_success.format(f"{table.project}.{table.dataset_id}.{table.table_id}"), "yellow")
        return True
    except Conflict:
        if logging:
            logging.info(cons.txt_create_tb_error.format(f"{table.project}.{table.dataset_id}.{table.table_id}"))
            cprint(cons.txt_create_tb_error.format(f"{table.project}.{table.dataset_id}.{table.table_id}"), "yellow")
        else:
            cprint(cons.txt_create_tb_error.format(f"{table.project}.{table.dataset_id}.{table.table_id}"), "yellow")
        return None


@get_time_function_execution
def bq_delete_table(project_id=None,
                    table_full_id=None,
                    logging=None,
                    key_path=None):
    """This method is for delete table

    :param project_id: String
    :param table_full_id: String -> 'project.dataset.table'
    :param logging: object
    :param key_path: file.json
    :return: True
    """

    from google.cloud import bigquery
    from google.api_core.exceptions import Conflict
    from color_tools import cprint

    client = bigquery.Client(project=project_id)
    if project_id and key_path:
        client = bigquery.Client.from_service_account_json(key_path)

    table_id = f"{table_full_id}"
    try:
        client.delete_table(table_id, not_found_ok=True)
        if logging:
            logging.info(cons.txt_delete_tb_success.format(f"{table_id}"))
            cprint(cons.txt_delete_tb_success.format(f"{table_id}"), "yellow")
        else:
            cprint(cons.txt_delete_tb_success.format(f"{table_id}"), "yellow")
        return True
    except Conflict:
        if logging:
            logging.info(cons.txt_delete_tb_error.format(f"{table_id}"))
            cprint(cons.txt_delete_tb_error.format(f"{table_id}"), "yellow")
        else:
            cprint(cons.txt_delete_tb_error.format(f"{table_id}"), "yellow")
        return None


@get_time_function_execution
def bq_query_to_df(
        project_id=None, sql=None, file=None, use_legacy_sql=False,
        logging=None, key_path=None):
    """This method is for transform query to dataframe

    :param project_id: String
    :param sql: String
    :param file: String file_path.sql
    :param use_legacy_sql: Boolean
    :param logging: object
    :param key_path: file.json
    :return: Dataframe
    """

    from google.cloud import bigquery
    from color_tools import cprint

    if not project_id:
        raise Exception('require var project_id: {project_id} ')
    if not sql and not file:
        raise Exception('Required var sql or file')
    if sql and file:
        raise Exception('Only one variable is required {sql} or {file}')
    if file:
        if not str(file).endswith(".sql"):
            raise Exception('the file only support extension {file_path}.sql')

    client = bigquery.Client(project=project_id)
    if key_path:
        client = bigquery.Client.from_service_account_json(key_path)

    sql_text = ""
    if sql and file is None:
        sql_text = sql

    if file and sql is None:
        sql_text = open(file).read()

    try:
        query_config = bigquery.QueryJobConfig(use_legacy_sql=use_legacy_sql)
        query_job = client.query(sql_text, job_config=query_config)
        df = query_job.to_dataframe()
        if logging:
            logging.info(cons.txt_query_to_df_success)
            cprint(cons.txt_query_to_df_success, 'yellow')
        else:
            cprint(cons.txt_query_to_df_success, 'yellow')
        return df
    except Exception as e:
        if logging:
            logging.info(cons.txt_query_to_df_errors)
            cprint(cons.txt_query_to_df_errors, 'yellow')
        else:
            cprint(cons.txt_query_to_df_errors, 'yellow')
        return None


@get_time_function_execution
def bq_query_to_rows(
        project_id=None, sql=None, file=None, use_legacy_sql=False,
        logging=None, key_path=None):
    """This method is for transform query to rows

    :param project_id: String
    :param sql: String
    :param file: String file_path.sql
    :param use_legacy_sql: Boolean
    :param logging: object
    :param key_path: file.json
    :return: list rows
    """

    from google.cloud import bigquery
    from color_tools import cprint

    if not project_id:
        raise Exception('require var project_id: {project_id} ')
    if not sql and not file:
        raise Exception('Required var sql or file')
    if sql and file:
        raise Exception('Only one variable is required {sql} or {file}')
    if file:
        if not str(file).endswith(".sql"):
            raise Exception('the file only support extension {file_path}.sql')

    client = bigquery.Client(project=project_id)
    if key_path:
        client = bigquery.Client.from_service_account_json(key_path)

    sql_text = ""
    if sql and file is None:
        sql_text = sql

    if file and sql is None:
        sql_text = open(file).read()

    try:
        query_config = bigquery.QueryJobConfig(use_legacy_sql=use_legacy_sql)
        query_job = client.query(sql_text, job_config=query_config)
        rows = query_job.result()
        if logging:
            logging.info(cons.txt_query_to_rows_success)
            cprint(cons.txt_query_to_rows_success, 'yellow')
        else:
            cprint(cons.txt_query_to_rows_success, 'yellow')
        return rows
    except Exception as e:
        if logging:
            logging.info(cons.txt_query_to_rows_errors)
            cprint(cons.txt_query_to_rows_errors, 'yellow')
        else:
            cprint(cons.txt_query_to_rows_errors, 'yellow')
        return None


@get_time_function_execution
def bq_query_truncate(
        project_id=None, table_full_id="",
        logging=None, key_path=None):
    """This method is for truncate table

    :param project_id: String
    :param table_full_id: String -> 'project.dataset.table'
    :param logging: object
    :param key_path: file.json
    :return: job result
    """

    from google.cloud import bigquery
    from color_tools import cprint

    if not project_id:
        raise Exception('require var project_id: {project_id} ')
    if not table_full_id:
        raise Exception('require var table_full_id: {table_full_id} ')

    client = bigquery.Client(project=project_id)
    if key_path:
        client = bigquery.Client.from_service_account_json(key_path)

    sql_text = f"""TRUNCATE TABLE `{table_full_id}` """
    try:
        query_config = bigquery.QueryJobConfig(use_legacy_sql=False)
        query_job = client.query(sql_text, job_config=query_config)
        rows = query_job.result()
        if logging:
            logging.info(cons.txt_truncate_success)
            cprint(cons.txt_truncate_success, 'yellow')
        else:
            cprint(cons.txt_truncate_success, 'yellow')
        return rows
    except Exception as e:
        if logging:
            logging.info(cons.txt_truncate_errors)
            cprint(cons.txt_truncate_errors, 'yellow')
        else:
            cprint(cons.txt_truncate_errors, 'yellow')
        return None


@get_time_function_execution
def bq_query_delete_partition(
        project_id=None, table_full_id="",
        partition_column="_PARTITIONTIME",
        date_initial=None, date_final=None,
        logging=None, key_path=None):
    """This method is for delete partition table

    :param project_id: String
    :param table_full_id: String -> 'project.dataset.table'
    :param partition_column: String
    :param date_initial: String -> YYYY-MM-DD
    :param date_final: String -> YYYY-MM-DD
    :param logging: object
    :param key_path: file.json
    :return: job result
    """

    from google.cloud import bigquery
    from color_tools import cprint

    if not project_id:
        raise Exception('require var project_id: {project_id} ')
    if not table_full_id:
        raise Exception('require var table_full_id: {table_full_id} ')
    if not partition_column:
        raise Exception('require var partition_column: {partition_column} ')
    if not date_initial:
        raise Exception('require var date_initial: {date_initial} ')
    if not date_final:
        raise Exception('require var date_final: {date_final} ')

    client = bigquery.Client(project=project_id)
    if key_path:
        client = bigquery.Client.from_service_account_json(key_path)

    sql_text = f"""DELETE FROM `{table_full_id}` 
                   WHERE DATE({partition_column}) between '{date_initial}' and '{date_final}' """

    try:
        query_config = bigquery.QueryJobConfig(use_legacy_sql=False)
        query_job = client.query(sql_text, job_config=query_config)
        rows = query_job.result()
        if logging:
            logging.info(cons.txt_delete_partition_success.format(f"{date_initial}", f"{date_final}"))
            cprint(cons.txt_delete_partition_success.format(f"{date_initial}", f"{date_final}"), 'yellow')
        else:
            cprint(cons.txt_delete_partition_success.format(f"{date_initial}", f"{date_final}"), 'yellow')
        return rows
    except Exception as e:
        if logging:
            logging.info(cons.txt_delete_partition_errors.format(f"{date_initial}", f"{date_final}"))
            cprint(cons.txt_delete_partition_errors.format(f"{date_initial}", f"{date_final}"), 'yellow')
        else:
            cprint(cons.txt_delete_partition_errors.format(f"{date_initial}", f"{date_final}"), 'yellow')
        return None


@get_time_function_execution
def bq_query_restore_table(
        project_id=None, table_full_id="", interval=1,
        logging=None, key_path=None):
    """This method is for restore table

    :param project_id: String
    :param table_full_id: String -> 'project.dataset.table'
    :param interval: String
    :param logging: object
    :param key_path: file.json
    :return: job result
    """

    from google.cloud import bigquery
    from color_tools import cprint

    if not project_id:
        raise Exception('require var project_id: {project_id} ')
    if not table_full_id:
        raise Exception('require var table_full_id: {table_full_id} ')

    client = bigquery.Client(project=project_id)
    if key_path:
        client = bigquery.Client.from_service_account_json(key_path)

    sql_text = f""" CREATE OR REPLACE TABLE `{table_full_id}_RESTORE` AS 
                    SELECT * FROM `{table_full_id}` FOR SYSTEM_TIME AS OF TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL {interval} HOUR)
                """

    try:
        query_config = bigquery.QueryJobConfig(use_legacy_sql=False)
        query_job = client.query(sql_text, job_config=query_config)
        rows = query_job.result()
        if logging:
            logging.info(cons.txt_restore_table_success.format(f"{table_full_id}"))
            cprint(cons.txt_restore_table_success.format(f"{table_full_id}"), 'yellow')
        else:
            cprint(cons.txt_restore_table_success.format(f"{table_full_id}"), 'yellow')
        return rows
    except Exception as e:
        if logging:
            logging.info(cons.txt_restore_table_errors.format(f"{table_full_id}"))
            cprint(cons.txt_restore_table_errors.format(f"{table_full_id}"), 'yellow')
        else:
            cprint(cons.txt_restore_table_errors.format(f"{table_full_id}"), 'yellow')
        return None
