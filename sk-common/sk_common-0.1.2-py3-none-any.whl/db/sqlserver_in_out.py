# -*- coding:utf-8 -*-
"""
对sql server数据库bcp导入和导出批量数据
"""
import subprocess
import os


def bcp_out(server, user, pwd, file_path, content_out, port='0', kind='table'):
    """
    bcp导出数据库表或查询结果到txt文件

    :param kind: str，'table'或者'query', 若为'table'导出整个表数据，若为'query'导出查询结果，默认'table'
    :param server:  str, 服务器ip
    :param user: str, 账号
    :param pwd: str, 密码
    :param file_path: str, 导出的txt文件地址
    :param content_out: str，表名或者sql 查询语句，例如：'[MTNOH_APP_SameCoverage].[dbo].[TB_同覆盖基础能力_数据_同覆盖小区_test] '
    :param port: str，端口号，默认'0'
    """
    if port != '0':
        server = server + ',' + port
    if kind == 'table':
        command_out = 'bcp  ' + content_out + '  out  ' + file_path + \
            ' -S' + server + '  -U' + user + ' -P' + pwd + '  -c -t'

    if kind == 'query':
        command_out = 'bcp  \" ' + content_out + ' \"  queryout  ' + \
            file_path + ' -S' + server + '  -U' + user + ' -P' + pwd + '  -c '

    result_code = subprocess.call(command_out, shell=True)
    print(result_code)


def bcp_in(server, user, pwd, file_path, table_name, port='0'):
    """
    bcp导入txt文件到sql server数据库表，表需要提前创建好

    :param server: str, 服务器ip
    :param user: str, 账号
    :param pwd: str, 密码
    :param file_path: str, 导入的txt文件地址
    :param table_name: str，导入到数据库的表名
    :param port: str，端口号，默认'0'
    """
    if port != '0':
        server = server + ',' + port
    if os.path.exists(file_path):
        command_in = 'bcp   ' + table_name + ' in  ' \
            + file_path + ' -S' + server + '  -U' + user + ' -P' + pwd + '  -c'
        result_code = subprocess.call(command_in, shell=True)
        print(result_code)
    else:
        print("文件不存在")
