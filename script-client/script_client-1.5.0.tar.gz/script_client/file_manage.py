
import os
from script_client.const import config
from loguru import logger



def find_file(**k):
    app_code = k['app_code']
    moniter_path = k['moniter_path']
    if '/' in k['moniter_path']:
        moniter_path = moniter_path.replace('/','-')
        file_name = moniter_path+'.'+'py'
    else:
        moniter_path = k['moniter_path'].split('#')[0]
        file_name = k['moniter_path'].split('#')[1]+'.'+'py'
    path = os.sep.join([config.test_script_dir,app_code,moniter_path,file_name])
    if os.path.exists(path):
        return path
    else:
        return False



def save_file(post_date):
    try:
        root_folder = config.test_script_dir #root
        app_code_folder = post_date['app_code']# app_code
        moniter_path_folder = post_date['moniter_path']# moniter_path
        file_name = post_date['script_file'][0].filename # name.py
        if '/' in moniter_path_folder:# url
            moniter_path_folder = moniter_path_folder.replace('/','-')
            file_name = moniter_path_folder+'.'+post_date['script_file'][0].filename.split('.')[-1]
        path = os.sep.join([root_folder,app_code_folder,moniter_path_folder])
        if not os.path.exists(path):
            os.makedirs(path)
        # tornado save file
        for meta in post_date['script_file']:
            with open(os.sep.join([path,file_name]), 'wb+') as f:
                f.write(meta['body'])
        return True
    except Exception as e:
        msg = f"保存文件过程出错：{str(e)}"
        logger.error(msg)
        return msg




