import os
import sys
import copy
import json
import psutil
import platform
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.gen as gen
from loguru import logger
from script_client import run_script
from script_client.const import config, fm
from script_client.common.common_method import save_script,\
    upload_script,get_tree,import_and_regist,reload_script,regist_app



class ListenerHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Content-Type', 'application/json')

    # @print_run_time
    @gen.coroutine
    def post(self):
        try:
            data = json.loads(self.request.body)
            if not all((data['app_code'], data['moniter_path'], data['http_body'])):
                logger.error(f"有参数为空 data={data}")
                self.write({'code': 0, 'msg': f"有参数为空"})
                return
            fun_map = fm.get_map()
            t_l = []
            if data['app_code'] in fun_map:
                if data['moniter_path'] in fun_map[data['app_code']]:
                    for fun_name in data['fun_name']:
                        for f in fun_map[data['app_code']][data['moniter_path']]:
                            for k, v in f.items():
                                if k.__name__ == fun_name:
                                    data['func_obj'] = [k, v]
                                    t_l.append(copy.deepcopy(data))
                    if t_l:
                        if run_script.q.qsize() + len(t_l) > config.max_task:
                            logger.warning(f"{config.local_ip}:{config.local_port}的队列已满")
                            self.write({'code': 0, 'msg': f"{config.local_ip}:{config.local_port}的队列已满"})
                            return
                        for t_data in t_l:
                            run_script.q.put(t_data)
                            # logger.debug(f"q队列长度 = {run_script.q.qsize()}")
                        self.write({'code': 1, 'msg': 'success'})
                        return
            logger.info(f"没有命中函数，现在注册的函数有 {fun_map}")
            self.write({'code': 0, 'msg': '没有命中函数'})
        except Exception as e:
            self.write({'code': 0, 'msg': f'{e}'})

class ScriptManageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('file_manage.html', f_tree=get_tree())

class SysManageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('sys_manage.html')

class GetScriptHandler(tornado.web.RequestHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
            f_name = data['file_name'] + '.py'
            f_path = os.sep.join([config.work_path, 'test_script',f_name])
            if os.path.exists(f_path):
                with open(f_path,'r',encoding='utf-8') as f:
                    self.write(f.read())
        except Exception as e:
            logger.error(str(e))

class SaveScriptHandler(tornado.web.RequestHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
            f_name = data['file_name'] + '.py'
            f_text = data['text']
            f_path = os.sep.join([config.work_path, 'test_script', f_name])
            ret = save_script(f_text=f_text,f_path=f_path)
            if ret != True:
                self.write({'code':0,'msg':ret})
                return
            # print(f"reload 前{fm.get_map()}")
            reload_script()
            # print(f"reload 后{fm.get_map()}")
            self.write({'code':1,'msg':'保存成功'})
        except Exception as e:
            logger.error(str(e))
            self.write({'code': 0, 'msg': e})

class UploadScriptHandler(tornado.web.RequestHandler):
    def post(self):
        try:
            script_file = self.request.files.get('file', None)
            if script_file != None:
                f_path = os.sep.join([config.work_path, 'test_script', script_file[0].filename])
                ret = upload_script(f_path=f_path,files=script_file)
                if ret != True:
                    self.write({'code':0,'msg':ret})
                    return
                import_and_regist()
                self.write({'code':1,'msg':'上传成功'})
        except Exception as e:
            logger.error(str(e))
            self.write({'code': 0, 'msg': e})

class DelScriptHandler(tornado.web.RequestHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
        except Exception as e:
            logger.error(str(e))
            self.write({'code': 0, 'msg': e})

def run_web_server():
    logger.info(f"启动webserver...")
    handlers = [
        (r"/", ScriptManageHandler),
        (r"/sys", SysManageHandler),
        (r"/receive_data", ListenerHandler),
        (r"/get_script_text", GetScriptHandler),
        (r"/save_script_text", SaveScriptHandler),
        (r"/upload_script_text", UploadScriptHandler),
    ]
    setting = dict(
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
    )
    app = tornado.web.Application(handlers, **setting)
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.bind(int(config.local_port))
    if (platform.system() != "Windows"):
        httpServer.start(1)
    else:  # 目前情况一个实例绝对够了
        httpServer.start(1)
    tornado.ioloop.IOLoop.current().start()


def _kill_terminate(p):
    # p.terminate()
    p.kill()


def stop_web_server():
    if os.path.exists('pid.log') == False:
        logger.info('没有pid.log')
        sys.exit(0)
    with open("pid.log", 'r') as fp:
        pid = int(fp.read())
    try:
        pidc = psutil.Process(pid)
        # ppid = pid.parent()
        # _kill_terminate(ppid)
        _kill_terminate(pidc)
    except Exception as e:
        logger.error(f"{e}")


if __name__ == "__main__":
    run_web_server()
