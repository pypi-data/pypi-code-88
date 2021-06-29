
import os
import requests
import importlib
from loguru import logger
from script_client.const import config,fm
from script_client.common.my_requests import MyRequests
from script_client.common.common_method import robot_send_message
from apscheduler.schedulers.background import BackgroundScheduler



scheduler = BackgroundScheduler()


@scheduler.scheduled_job('interval',id='heart_beat', seconds=30)
def send_heart_beat():
    try:
        mr = MyRequests(timeout=config.http_request_timeout)
        url = config.heart_beat_url
        app_list = []
        for k in fm.get_map():
            app_list.append(str(k))
        data = {"type": 0, "app_code": app_list}
        # logger.info(data)
        rep = mr.run(url=url, method='post', json=data)
        if isinstance(rep, requests.models.Response):
            if rep.status_code != 200:
                msg = f"心跳发送失败 - app = {app_list} status_code = {rep.status_code}"
                logger.error(msg)
                robot_send_message(message=msg)
        else:
            logger.error(f"心跳发送失败 app = {app_list} ， {rep}")
            robot_send_message(message='心跳发送失败')
    except Exception as e:
        logger.error(e)


# @scheduler.scheduled_job('interval',id='import_func', seconds=5)
# def import_func():
#     if os.path.exists(os.sep.join([config.work_path,'test_script'])):
#         for root, dirs, files in os.walk(os.sep.join([config.work_path,'test_script'])):
#             for file in files:
#                 if os.path.splitext(file)[1] == '.py':
#                     importlib.import_module(f"test_script.{os.path.splitext(file)[0]}")
#     # logger.debug(fm.get_map())



def init_jobs():
    try:
        scheduler.start()
        logger.info(f"scheduler启动完成")
    except Exception as e:
        logger.error(f"job err =  {e}")