import pandas as pd
import json
import os
from happyreport import excel_format
from happyreport import send_mail


class Setting(object):
    """
    替代settings.py的配置类
    """
    def __init__(self, job_url, jobs_from, data_url, save_path, host, port, **kwargs):
        """
        初始化属性
        """
        self.job_url = job_url
        self.jobs_from = jobs_from
        self.data_url = data_url
        self.save_path = save_path
        self.host = host
        self.port = port
        for key, value in kwargs.items():
            setattr(self, key, value)


class Setting2(object):
    """
    替代settings.py的配置类
    """
    def __init__(self, **kwargs):
        """
        初始化属性
        """
        for key, value in kwargs.items():
            setattr(self, key, value)


class MailJob(object):
    """
    报表获取，报表发送类
    执行逻辑：
        1、数仓构建源主题表数据：包含ds字段控制日期版本
        2、配置报表任务属性至数据库报表任务配置表：表包含字段：['job_id', 'job_name', 'table_fields', 'sender_email', 'password', 'receiver_email', 'acc_email', 'content']
            各字段释义：
                job_id              - int       : 报表任务ID
                job_name            - string    : 任务中文名即邮件主题名
                table_fields        - string    : JSON格式字符串，报表详细信息格式如下：
                        eg: [ {"workbook": [
                                    {"sheet": {
                                        "from": "主题表表名1",
                                        "select": ["字段1" , "字段2"],
                                        "as": ["别名1", "别名2"]},
                                     "sheet_name": "sheet页名称1"},
                                    {"sheet": {
                                        "from": "主题表表名2",
                                        "select": ["字段1" , "字段2"],
                                        "as": ["别名1", "别名2"]},
                                     "sheet_name": "sheet页名称2"}],
                               "attach_name": "附件名称.xlsx"},
                               {"workbook": [
                                    {"sheet": {
                                        "from": "主题表表名1",
                                        "select": ["字段1" , "字段2"],
                                        "as": ["别名1", "别名2"]},
                                     "sheet_name": "sheet页名称1"},
                                    {"sheet": {
                                        "from": "主题表表名2",
                                        "select": ["字段1" , "字段2"],
                                        "as": ["别名1", "别名2"]},
                                     "sheet_name": "sheet页名称2"}],
                               "attach_name": "附件名称.xlsx"}
                               ]
                sender_email        - string    : 发件人邮箱账号
                password            - string    : 发件人邮箱密码
                receiver_email      - string    : 收件人邮箱，多个收件人用“,“分隔
                acc_email           - string    : 抄送人邮箱，多个抄送人用“,“分隔
                content             - string    : 正文内容
        3、完成配置表实例化报表数据获取与邮箱发送类MailJob,结束任务
    """
    def __init__(self, job_id, settings, date):
        """
        初始化传入job_id与环境配置settings以及ds字段
        """
        self.date = date
        self.settings = settings
        self.jobs_from = settings.jobs_from
        self.jobs_url = settings.job_url
        self.data_url = settings.data_url
        self.job_id = job_id
        self.job = pd.read_sql(f"select * from {self.jobs_from} where job_id = '{job_id}'",
                               settings.job_url).to_dict(orient='series')
        self.job = dict(zip(self.job.keys(), map(lambda x: x.values[0], self.job.values())))
        self.attaches = json.loads(self.job['table_fields'])
        self.save_path = settings.save_path

    def _get_data(self):
        """
        获取报表数据，根据附件-子sheet，打包成list
        """
        res = []
        for at in self.attaches:
            sub = {"attach_name": at["attach_name"],
                   "data": [],
                   "sheet_names": []}
            for st in at['workbook']:
                sql = f"select {','.join(st['sheet']['select'])} from {st['sheet']['from']} where ds = '{self.date}'"
                print(sql)
                df = pd.read_sql(sql, self.data_url)
                df.columns = st['sheet']["as"]
                sub['data'].append(df)
                sub['sheet_names'].append(st['sheet_name'])
            res.append(sub)
        return res

    def _save(self, data_res):
        """
        保存附件至本地
        """
        for wb in data_res:
            excel_format(wb['data'], os.path.join(self.save_path, wb["attach_name"]),  sheetname_tuple=wb['sheet_names'])

    def _send_email(self):
        """
        根据任务配置项发送邮件
        """
        send_mail(host=self.settings.host,
                  port=self.settings.port,
                  user=self.job['sender_email'],
                  password=self.job['password'],
                  receivers=self.job['receiver_email'].split(","),
                  subject=self.job['job_name'] + self.date,
                  carbon_copy=self.job['acc_email'].split(","),
                  carbon_copy_mask=self.job['acc_email'].split(","),
                  content=self.job['content'],
                  attaches=[os.path.join(self.save_path, a['attach_name']) for a in self.attaches])

    def run(self):
        """
        启动任务
        """
        data_res = self._get_data()
        self._save(data_res)
        self._send_email()
