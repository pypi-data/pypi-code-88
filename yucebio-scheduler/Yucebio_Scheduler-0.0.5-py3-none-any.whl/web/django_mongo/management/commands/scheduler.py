"""
适用于django + mongo框架的自定义命令


Refer:  https://docs.djangoproject.com/zh-hans/3.2/howto/custom-management-commands/
"""
import os
import psutil
from typing import Any, Optional
from django.core.management.base import CommandParser
from django.core.management.base import BaseCommand
from yucebio_scheduler.web.django_mongo.utils import create_scheduler
import logging


class Command(BaseCommand):
    help = "启动apscheduler服务管理自定义作业"
    pidfile = '.yucebio_scheduler.web.django_mongo.pid.log'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('--restart', action='store_true', help="重启APScheduler，防止同时启动多个进程")

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        scheduler = create_scheduler(block=True)
        restart = options.get('restart', False)
        # 需要让scheduler始终运行下去 或者 让scheduler跟着web服务一起启动
        pid = self.check_run_instance(restart)
        if pid:
            logging.warn(f"apscheduler is running in another process[PID: {pid}]!!! please do not run again!!!")
            return
        pid = os.getpid()
        with open(self.pidfile, 'w') as w:
            w.write(str(pid))
        logging.info(f"apscheduler has start [PID:{pid}]")
        scheduler.start()

    def check_run_instance(self, auto_restart = False):
        """检测当前命令是否存在正在运行的实例
        """
        if not os.path.exists(self.pidfile):
            return False

        pid = open(self.pidfile).read().strip()
        if not pid:
            return False
        pid = int(pid)
        if not psutil.pid_exists(pid):
            return False

        if auto_restart:
            process = psutil.Process(pid)
            process.kill()
            return False

        return pid
