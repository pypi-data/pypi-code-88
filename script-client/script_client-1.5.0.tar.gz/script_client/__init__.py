import os
import sys
import configparser
from loguru import logger
from script_client import jobs
from script_client import web_server
from script_client import run_script
from script_client.const import config as conf,fm
from script_client.common.restart import restart_program
from script_client.common.common_method import regist_app,find_script,import_and_regist


__version__ = "1.5.0"

logger.add(os.sep.join([os.getcwd(), 'logs', 'script_client_{time}.log']),
               rotation="1 days", retention="2 days")

print_str = '''
                               __              __                      __  __                        __     
                              /  |            /  |                    /  |/  |                      /  |    
  _______   _______   ______  $$/   ______   _$$ |_           _______ $$ |$$/   ______   _______   _$$ |_   
 /       | /       | /      \ /  | /      \ / $$   |         /       |$$ |/  | /      \ /       \ / $$   |  
/$$$$$$$/ /$$$$$$$/ /$$$$$$  |$$ |/$$$$$$  |$$$$$$/         /$$$$$$$/ $$ |$$ |/$$$$$$  |$$$$$$$  |$$$$$$/   
$$      \ $$ |      $$ |  $$/ $$ |$$ |  $$ |  $$ | __       $$ |      $$ |$$ |$$    $$ |$$ |  $$ |  $$ | __ 
 $$$$$$  |$$ \_____ $$ |      $$ |$$ |__$$ |  $$ |/  |      $$ \_____ $$ |$$ |$$$$$$$$/ $$ |  $$ |  $$ |/  |
/     $$/ $$       |$$ |      $$ |$$    $$/   $$  $$/       $$       |$$ |$$ |$$       |$$ |  $$ |  $$  $$/ 
$$$$$$$/   $$$$$$$/ $$/       $$/ $$$$$$$/     $$$$/         $$$$$$$/ $$/ $$/  $$$$$$$/ $$/   $$/    $$$$/  
                                  $$ |                                                                      
                                  $$ |                                                                      
                                  $$/                                                                          
'''



def _get_config(config_path):
    if config_path == '':
        config_path = 'config.ini'
    if not os.path.exists(config_path):
        logger.error(f"config.ini 不存在")
        return False
    try:
        config = configparser.ConfigParser()
        config.read(config_path, encoding="utf-8")
        conf.local_ip = config.get('conf', 'local_ip')
        conf.local_port = config.getint('conf', 'local_port')
        conf.client_name = config.get('conf', 'client_name')
        conf.regist_server_url = config.get('conf', 'regist_server_url')
        conf.heart_beat_url = config.get('conf', 'heart_beat_url')
        conf.result_url = config.get('conf', 'result_url')
        conf.http_request_timeout = config.getint('conf', 'http_request_timeout')
        conf.max_thread = config.getint('conf', 'max_thread')
        conf.max_task = config.getint('conf', 'max_task')
        #conf.robot_url = config.get('conf', 'robot_url')
        conf.work_path = os.getcwd()
        return True
    except Exception as e:
        logger.error(f"读取配置信息失败 {e}")
        return False



def _run_threadpool():
    run_script.init_thread_pool()


def _run_job():
    jobs.init_jobs()


def _run_webserver():
    web_server.run_web_server()


def stop():
    logger.info(f"stop script client ... ")
    web_server.stop_web_server()


def run(config_path=''):
    '''
    启动服务
    :param config_path: config路径，默认当前路径
    :return:
    '''
    logger.info(print_str)
    if _get_config(config_path) and import_and_regist():
        with open(r'pid.log', 'wb') as f:
            pid = os.getpid()
            f.write(str(pid).encode())
        _run_threadpool()
        _run_job()
        _run_webserver()







if __name__ == "__main__":
    run()



