import os
import pandas as pd
import json
from json.decoder import JSONDecodeError

def check(settings):
    """
    环境与任务配置验证函数
    """
    columns = ['job_id', 'job_name', 'table_fields', 'sender_email', 'password', 'receiver_email', 'acc_email', 'content']
    df = pd.read_sql(settings.jobs_from, settings.job_url)
    missing_columns = []
    for c in df:
        if c not in columns:
            missing_columns.append(c)
    assert not missing_columns, f"配置表缺失标准字段{missing_columns}"

    for i in range(df.shape[0]):
        try:
            for wb in json.loads(df.iloc[i]['table_fields']):
                assert 'workbook' in wb.keys(), f"行号{i}table_fields缺少对象workbook"
                assert 'attach_name' in wb.keys(), f"行号{i}table_fields缺少对象attach_name"
                for st in wb['workbook']:
                    assert 'sheet' in wb.keys(), f"行号{i}workbook缺少对象sheet"
                    assert 'sheet_name' in st[k].keys(), f"行号{i}workbook缺少对象sheet_name"
                    for k, v in st.items():
                        assert 'from' in st[k].keys(), f"行号{i}sheet缺少对象from"
                        assert 'select' in st[k].keys(), f"行号{i}sheet缺少对象select"
                        assert 'as' in st[k].keys(), f"行号{i}sheet缺少对象as"
        except JSONDecodeError:
            raise JSONDecodeError(f"table_fields错误字段格式,行号：'{i}'")

    if not os.path(settings.save_path):
        print(f"创建报表保存路径{settings.save_path}")
        os.mkdir(os.path.join(os.path.split(settings.save_path)))
    print("验证通过")
