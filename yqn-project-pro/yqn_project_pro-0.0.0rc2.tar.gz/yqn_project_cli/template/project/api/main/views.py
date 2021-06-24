# -*- coding: utf-8 -*-
# Author: ZKH
# Date：2021/3/8
import datetime
from yqn_project_cli.utils.restx import DANamespace
from yqn_project_cli.utils.core.as_flask import JSONResponse
from yqn_project_cli.utils.decorators import parse_request_with
from api.main.parser import MainIndexParser
from api.main.model import (
    RequestSchema,
    ResponseSchema
)


# one module, one namespace, more will be ignored
ns = DANamespace('main', description='', path='/')

req_name = "req-main"
res_name = "res-main"

req = RequestSchema(req_name)
res = ResponseSchema(res_name)
ns.add_model(req_name, req)
ns.add_model(res_name, res)


"""
import datetime
from yqn_project_cli.utils.core.as_flask import JSONResponse
from yqn_project_cli.utils.decorators import parse_request_with
from api.main.parser import MainIndexParser
from api.main.model import (
    RequestSchema,
    ResponseSchema
)

req_name = "req-tool"
res_name = "res-tool"

req = RequestSchema(req_name)
res = ResponseSchema(res_name)
ns.add_model(req_name, req)
ns.add_model(res_name, res)


class Swagger:

    @ns.doc(expect=[req])
    @ns.doc(responses={200: ("description", res)})
    @parse_request_with(MainIndexParser())
    def new_add(self, *args, **kwargs):
        return JSONResponse({'now': datetime.datetime.now()})
"""


class Swagger:

    @ns.doc(expect=[req])
    @ns.doc(responses={200: ("description", res)})
    @parse_request_with(MainIndexParser())
    def new_add(self, *args, **kwargs):
        return JSONResponse({'now': datetime.datetime.now()})