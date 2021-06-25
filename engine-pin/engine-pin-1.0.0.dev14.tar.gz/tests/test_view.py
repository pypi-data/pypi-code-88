#!/usr/bin/env python3

#BoBoBo#

from pin.view import *


def test_tpl_conf():
    path = get_tpl_conf_value(None, 'template_path')
    assert not None is path
    reload = get_tpl_conf_value(None, 'template_reload')
    assert not None is reload


def test_render():
    res = response_tpl('hello.html', {})
    assert res['content'].endswith('</html>')
