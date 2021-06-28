from etl_bq_tools import bq_query_to_df
from etl_bq_tools.utils import constants as cons
from etl_bq_tools.utils.prettytable import format_for_print
from etl_bq_tools.utils.time_execution import get_time_function_execution


@get_time_function_execution
def show_describe_dataset(project_id=None, dataset_full_id="",
                          logging=None, key_path=None, show_table=False):
    """
     :param project_id: String
     :param dataset_full_id: String {project}.{dateset}
     :param logging: object
     :param key_path: file.json
     :param show_table: False
    """
    from color_tools import cprint
    from sizebytes_tools import convert_bytes

    query_text = """
        SELECT
          project_id                                                             AS project_id
        , dataset_id                                                             AS dataset_id
        , table_id                                                               AS table_id
        , size_bytes                                                             AS size_bytes
        , TIMESTAMP_MILLIS(creation_time)                                        AS creation_time
        , TIMESTAMP_MILLIS(last_modified_time)                                   AS last_modified_time
        , CAST(DATETIME(TIMESTAMP_MILLIS(last_modified_time), "America/Lima") AS DATETIME) AS  last_modified_datetime_local
        , CAST(DATETIME(TIMESTAMP_MILLIS(last_modified_time), "America/Lima") AS DATE)     AS  last_modified_date_local
        , EXTRACT(HOUR FROM CAST(DATETIME(TIMESTAMP_MILLIS(last_modified_time), "America/Lima") AS DATETIME)) AS last_modified_hour_local
        , row_count
        , CASE
            WHEN type = 1
              THEN 'TABLE'
            WHEN type = 2
              THEN 'VIEW'
            ELSE NULL
          END                                                                     AS table_type
        FROM
          `{0}`.__TABLES__
    ;
    """

    try:
        _sql = query_text.format(dataset_full_id)
        df = bq_query_to_df(
            project_id=project_id,
            sql=_sql,
            file=None,
            use_legacy_sql=False,
            key_path=key_path
        )
        df["creation_time"] = df["creation_time"].astype(str).str[:19]
        df["last_modified_time"] = df["last_modified_time"].astype(str).str[:19]
        df["last_modified_datetime_local"] = df["last_modified_datetime_local"].astype(str).str[:19]
        df["size_bytes_format"] = df.apply(lambda x: convert_bytes(x["size_bytes"]), axis=1)

        if show_table:
            print(format_for_print(df))

        if logging:
            logging.info(cons.txt_show_describe_table_success.format(f"{dataset_full_id}"))
            cprint(cons.txt_show_describe_table_success.format(f"{dataset_full_id}"), "yellow")
        else:
            cprint(cons.txt_show_describe_table_success.format(f"{dataset_full_id}"), "yellow")
        return df
    except:
        if logging:
            logging.info(cons.txt_show_describe_table_errors.format(f"{dataset_full_id}"))
            cprint(cons.txt_show_describe_table_errors.format(f"{dataset_full_id}"), "yellow")
        else:
            cprint(cons.txt_show_describe_table_errors.format(f"{dataset_full_id}"), "yellow")
