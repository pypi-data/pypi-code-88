from yuncheng_util_pkg.util import get_for_request
from yuncheng_util_pkg.util_file import down_pic
from yuncheng_util_pkg.yuncheng_al_class import ask_for_yuncheng_al

def get_pipeline_error_info(id,savePath,url="http://192.168.1.222:12010/get-wrong-info",checkUrl = 'http://192.168.1.222:8001/lh/lhRawdataAnalysis'):
    ur = url+str(id)
    res = get_for_request(ur)
    down_pipeline_info(res,savePath)
    return ask_for_yuncheng(res,checkUrl)
def down_pipeline_info(res:object,savepath:str):
    for i in res['result']:
        url = i['url']
        picpath = down_pic(url,savepath)
        i['path'] = picpath

def ask_for_yuncheng(res:object,al_url):
    pics = [i['path'] for i in res['result']]
    result = ask_for_yuncheng_al(al_url,pics)
    for i in result:
        for k in res['result']:
            if i['id'] == k['path']:
                i['pipeinfo'] = k
                continue
    return result

