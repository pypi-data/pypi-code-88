# -*- encoding:utf-8 -*-
import logging
import os
from logging import handlers
import json
import datetime
import socket

LOG_PATH = os.environ.get('LOG_PATH') if os.environ.get('LOG_PATH') else '/tmp'
REMOVE_ATTR = ["filename", "module", "exc_text", "stack_info", "created", "msecs", "relativeCreated", "exc_info", "msg",
               "args"]


class HostIp:
    host_name = None
    host_ip = None

    @classmethod
    def get_host_ip(cls):
        if not cls.host_name or not HostIp.host_ip:
            try:
                cls.host_name = socket.gethostname()
                cls.host_ip = socket.gethostbyname(cls.host_name)
            except:
                cls.host_name = "unknown hostname"
                cls.host_ip = "unknown ip"
        return cls.host_name, cls.host_ip


class JSONFormatter(logging.Formatter):
    host_name, host_ip = HostIp.get_host_ip()

    def format(self, record):
        extra = self.build_record(record)
        self.set_format_time(extra)  # set time
        self.set_host_ip(extra)  # set host name and host ip
        if isinstance(record.msg, dict):
            extra['data'] = record.msg  # set message
        else:
            if record.args:
                extra['msg'] = "'" + record.msg + "'," + str(record.args).strip('()')
            else:
                extra['msg'] = record.msg
        if record.exc_info:
            extra['exc_info'] = self.formatException(record.exc_info)
        if self._fmt == 'pretty':
            return json.dumps(extra, indent=1, ensure_ascii=False)
        else:
            return json.dumps(extra, ensure_ascii=False)

    @classmethod
    def build_record(cls, record):
        return {
            attr_name: record.__dict__[attr_name]
            for attr_name in record.__dict__
            if attr_name not in REMOVE_ATTR
        }

    @classmethod
    def set_format_time(cls, extra):
        now = datetime.datetime.utcnow()
        format_time = now.strftime("%Y-%m-%dT%H:%M:%S" + ".%03d" % (now.microsecond / 1000) + "Z")
        extra['@timestamp'] = format_time
        return format_time

    @classmethod
    def set_host_ip(cls, extra):
        extra['host_name'] = JSONFormatter.host_name
        extra['host_ip'] = JSONFormatter.host_ip


class Logger(object):
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }  # 日志级别关系映射

    def __init__(self, name=None, level='info', when='D', backup_count=7,
                 fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(name)
        format_str = logging.Formatter(fmt)  # 设置日志格式
        self.logger.setLevel(self.level_relations.get(level))  # 设置日志级别
        sh = logging.StreamHandler()  # 往屏幕上输出
        sh.setFormatter(format_str)  # 设置屏幕上显示的格式
        self.logger.addHandler(sh)  # 把对象加到logger里
        if name:
            th = handlers.TimedRotatingFileHandler(filename=os.path.join(LOG_PATH, f'{name}.log'),
                                                   when=when,
                                                   backupCount=backup_count,
                                                   encoding='utf-8')  # 往文件里写入#指定间隔时间自动生成文件的处理器
            # 实例化TimedRotatingFileHandler
            # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
            # S 秒
            # M 分
            # H 小时、
            # D 天、
            # W 每星期（interval==0时代表星期一）
            # midnight 每天凌晨
            th.setFormatter(JSONFormatter())  # 设置文件里写入的格式
            self.logger.addHandler(th)
