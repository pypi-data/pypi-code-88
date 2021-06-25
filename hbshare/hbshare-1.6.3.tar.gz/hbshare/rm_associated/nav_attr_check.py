"""
线上和本地的净值归因结果的校验程序
"""
import pandas as pd
import hbshare as hbs
from nav_attribution import StyleAttribution


def get_attr_res_from_sql(fund_id, date, at_type):
    sql_script = "SELECT * FROM st_fund.r_st_nav_attr_df where jjdm = '{}'".format(fund_id)
    # sql_script = "SELECT * FROM st_fund.r_st_nav_attr_df where jjdm = '{}'".format(fund_id)
    # sql_script = "SELECT * FROM st_fund.r_st_nav_style_allo_bar where jjdm = '{}'".format(fund_id)
    # results = hbs.db_data_query('funduser', sql_script, page_size=5000)
    results = hbs.db_data_query('funduser', sql_script, page_size=5000)
    data = pd.DataFrame(results['data'])
    data = data[['jjdm', 'tjrq', 'attr_type', 'data_type', 'style_factor', 'data_value']].rename(
        columns={"jjdm": "fund_id", "tjrq": "date", "data_type": "value_type", "data_value": "value"})
    data = data[data['date'] == date]
    data = data[data['attr_type'] == at_type]
    data = data[data['value_type'] == 'exposure']
    print(data)


if __name__ == '__main__':
    attr_type = 'style_allo'
    dt = '20201231'
    get_attr_res_from_sql(fund_id='110011', date=dt, at_type=attr_type)
    res = StyleAttribution(fund_id='110011', fund_type='mutual', start_date='20191220', end_date='20210120',
                           factor_type=attr_type, benchmark_id='000985', nav_frequency='day').get_all()
    print(res)