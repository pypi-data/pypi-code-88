#!/usr/bin/env python3

#BoBoBo#

from datetime import date, datetime
import os
import sys
import json
import pin.kit.util as util
import pin.kit.common as common

from jinja2 import Environment, \
    FileSystemLoader, \
    FileSystemBytecodeCache, \
    select_autoescape, \
    Template


def get_tpl_conf_value(conf, conf_key):
    if not conf:
        conf = common.get_conf(None)
    path = conf('app', conf_key, None)
    return path


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


def response_json(result, headers=None):
    res = {}
    res['headers'] = []
    res['headers'].append(('Content-Type', 'application/json;charset=utf-8'))
    if headers:
        res['headers'] += list(map(lambda k: (k, headers[k]), headers))
    res['status'] = '200 OK'
    res['content'] = json.dumps(result, cls=ComplexEncoder)
    return res


def response_raw(result, headers=None):
    res = {}
    res['headers'] = []
    res['headers'].append(('Content-Type', 'application/json;charset=utf-8'))
    if headers:
        res['headers'] += list(map(lambda k: (k, headers[k]), headers))
    res['status'] = '200 OK'
    res['content'] = result
    return res


def response_tpl(tpl_file, tpl_param, headers=None):
    if tpl_param is None:
        tpl_param = {}

    res = {}
    res['headers'] = []
    res['headers'].append(('Content-Type', 'text/html;charset=utf-8'))
    res['status'] = '200 OK'
    res['content'] = render(tpl_file, tpl_param)
    return res


def response_404():
    res = {}
    res['headers'] = []
    res['headers'].append(('Content-Type', 'text/html;charset=utf-8'))
    res['status'] = '404 Not Found'
    res['content'] = ''
    return res


def view(conf):
    tpl_path = get_tpl_conf_value(conf, 'template_path')
    if not tpl_path:
        return None
    print('Use template path: ' + tpl_path)

    tpl_reload = get_tpl_conf_value(conf, 'template_reload')
    if not tpl_reload or 'false' == tpl_reload.lower():
        tpl_reload = False
    else:
        tpl_reload = True

    jinja2_env = Environment(
        loader=FileSystemLoader(tpl_path),
        bytecode_cache=FileSystemBytecodeCache(tpl_path),
        auto_reload=tpl_reload,
        optimized=True,
        autoescape=select_autoescape(['htm', 'html', 'xml', 'json']))

    def render(tpl_file, variable):
        engine = jinja2_env.get_template(tpl_file)
        result = engine.render(variable)
        return str(result)

    return render


render = view(common.get_conf(None))


def config_render(conf):
    global render
    render = view(conf)
