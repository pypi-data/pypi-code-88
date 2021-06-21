"""提供一些辅助工具

1. 根据django settings初始化apscheduler配置
2. 提供register_job装饰器
"""
from django.conf import settings
from apscheduler.schedulers.blocking import BlockingScheduler, BaseScheduler
from apscheduler.schedulers.background import BackgroundScheduler
# from pytz import utc
from tzlocal import get_localzone
import logging

# logging.basicConfig()
# logging.getLogger('apscheduler').setLevel(logging.DEBUG)

def load_django_settings():
    """参考flask_apscheduler加载配置的方式从settings中获取配置内容
    """
    options = dict()

    job_stores = getattr(settings, 'SCHEDULER_JOBSTORES', None)
    if job_stores:
        options['jobstores'] = job_stores

    executors = getattr(settings, 'SCHEDULER_EXECUTORS', None)
    if executors:
        options['executors'] = executors

    job_defaults = getattr(settings, 'SCHEDULER_JOB_DEFAULTS', None)
    if job_defaults:
        options['job_defaults'] = job_defaults

    timezone = getattr(settings, 'SCHEDULER_TIMEZONE', get_localzone())
    options['timezone'] = timezone
    return options

def load_jobs(_scheduler: BaseScheduler):
    jobs = getattr(settings, 'SCHEDULER_JOBS', None)
    for job in jobs:
            _scheduler.add_job(**job)

scheduler = { '__inited__': False, '__instance__': None }

def create_scheduler(block: bool = False) -> BaseScheduler:
    if scheduler['__instance__']:
        return scheduler['__instance__']

    logging.debug("init apscheduler ...")
    options = load_django_settings()
    _instance = (BackgroundScheduler if not block else BlockingScheduler)()

    _instance.configure(**options)
    if not block:
        _instance.start(paused=True)

    load_jobs(_instance)

    scheduler['__instance__'] = _instance
    return scheduler['__instance__']

