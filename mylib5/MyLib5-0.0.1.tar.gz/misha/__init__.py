def sql(table):
    import difflib as df
    import csv
    import pandas as pd
    import numpy as np
    import re
    import openpyxl
    import time
    import pyodbc
    import json
    from pandas.io.json import json_normalize
    from collections import namedtuple
    import ast
    start_time = time.time()

    #table = 'auto.mldev19_ml1_test_service'
    new_table_name = 'mldev19_ml1_test_service_json' # добавить auto. если создаем постоянную таблицу
    json_table = 'json_temp_table'
    #старое lvl_0 = 'service_reply' # название столбца
    lvl_1 = 'predictions' # json 1 ключ
    lvl_2 = 'name' # название нового столбца
    lvl_22 = 'value' # значение нового столбца
    bykva = 't.' # с точкой
    bykva_2 = 'h.' # с точкой
    zapros = '' # для генерации SQL запроса
    columns_no_changes = '' # для генерации SQL запроса
    
    SQL_Query = pd.read_excel(r'U:\Работа RGS\json\Attachments_Mikhail_Yurkevich@rgs.ru_2021-06-18_11-28-07\test 100.xlsx')
    json = SQL_Query.head(1).to_dict()

    columns = SQL_Query.columns

    for i in columns:
        if type(SQL_Query[i][0]) == str:
            try:
                B_json = ast.literal_eval(SQL_Query[i][0]) # преобразование строки в json 
                json_column = i
            except:
                columns_no_changes = columns_no_changes + bykva_2 + i + ', '
        else:
            columns_no_changes = columns_no_changes + bykva_2 + i + ', '
    #старое
    #A_json = json[lvl_0][0]
    #B_json = ast.literal_eval(A_json) # преобразование строки в json 

    C_json = B_json[lvl_1][0]

    list_json = list(C_json.keys())


    for i in list_json:
        try: 
            type(C_json[i][0]) == dict
            for j in range(len(C_json[i])):
                x = C_json[i][j]
                stroka = bykva + json_column + ' #> ' + "'{" + lvl_1 + "}'" + ' ->0 ' + ' #> ' + "'{" + i + "}'" + ' ->' + str(j) + ' #> ' + "'{" + lvl_22 + "}'" + ' as ' +  x[lvl_2] + ','
                #print(stroka)
                zapros = zapros + stroka + '\n'
        except:
            stroka = bykva + json_column + ' #> ' + "'{" + lvl_1 + "}'" + ' ->0 ' + ' #>> ' + "'{" + i + "}'" + ' as ' +  i + ','
            #print(stroka)
            zapros = zapros + stroka + '\n'
    zapros = zapros[0:-2]
    #print(zapros)


    N = '\n' 
    s1 = 'Drop table if exists '+ json_table + ';' + N
    s2 = 'create temp table ' + json_table + ' as (' + N
    s3 = 'select ' + columns_no_changes + ' ' + 'replace(' + bykva_2 + json_column + ',chr(39),chr(34))::json as ' + json_column + N
    s4 = 'from ' + table + ' ' + bykva_2.replace('.','')  + ' );' + N

    columns_no_changes = columns_no_changes.replace(bykva_2,bykva)

    s5 = 'Drop table if exists '+ new_table_name + ';' + N
    s6 = 'create temp table ' + new_table_name + ' as (' + N
    s7 = 'select ' + columns_no_changes + N 
    s8 =  zapros + N
    s9 = 'from ' + json_table + ' ' + bykva.replace('.','') + ' )'


    polniy_zapros = s1 + s2 + s3 + s4 + N + s5 + s6 + s7 + s8 + s9

    return(print(polniy_zapros + '\n'),print("--- {} min ---".format((time.time() - start_time)/60)))
    #print("--- {} min ---".format((time.time() - start_time)/60))


def typoi(name):
    return(print('{} тупица'.format(name)))
