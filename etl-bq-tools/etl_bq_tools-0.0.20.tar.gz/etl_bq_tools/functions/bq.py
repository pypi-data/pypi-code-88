from etl_bq_tools.utils.time_execution import get_time_function_execution
from etl_bq_tools.utils import constants as cons


def bq_set_project(project_id=None, logging=None):
    """
     :param project_id: String
     :param logging: Object
     :return:
    """
    import os
    from color_tools import cprint

    if not project_id:
        raise Exception('require var project_id: {project_id} ')

    try:
        os.system(f"gcloud config set project {project_id}")

        if logging:
            logging.info(cons.txt_set_project_success.format(project_id))
            cprint(cons.txt_set_project_success.format(project_id), 'yellow')
        else:
            cprint(cons.txt_set_project_success.format(project_id), 'yellow')
    except:
        if logging:
            logging.info(cons.txt_set_project_errors.format(project_id))
            cprint(cons.txt_set_project_errors.format(project_id), 'yellow')
        else:
            cprint(cons.txt_set_project_errors.format(project_id), 'yellow')


@get_time_function_execution
def bq_execute_sql(sql=None, parameter=None, logging=None):
    """
     :param sql: file.sql
     :param parameter: list dict params [{"variable": "", "type": "", "value":""}]
     :param logging: object
     :return:
    """

    import os
    from color_tools import cprint

    if not sql:
        raise Exception('require var sql: {file.sql} ')

    file_sql = os.path.basename(sql)

    try:
        _parameter2 = ""
        if parameter:
            parameter = {"parameter": parameter}
            list_params = [params_values for _, params_values in parameter.items()][0]
            for value in list_params:
                _var = value["variable"]
                _type = value["type"]
                _val = value["value"]
                _parameter = f"--parameter={_var}:{_type}:{_val} "
                _parameter2 += f"{_parameter}"
            sentence_bq = f"bq query --quiet  --use_legacy_sql=false {_parameter2} --flagfile={sql} "
        else:
            sentence_bq = f"bq query --quiet  --use_legacy_sql=false --flagfile={sql} "

        os.system(sentence_bq)

        if logging:
            logging.info(cons.txt_execute_sql_success.format(file_sql))
            cprint(cons.txt_execute_sql_success.format(file_sql), 'yellow')
        else:
            cprint(cons.txt_execute_sql_success.format(file_sql), 'yellow')

    except Exception as e:
        if logging:
            logging.info(cons.txt_execute_sql_errors.format(file_sql))
            cprint(cons.txt_execute_sql_errors.format(file_sql), 'yellow')
        else:
            cprint(cons.txt_execute_sql_errors.format(file_sql), 'yellow')
