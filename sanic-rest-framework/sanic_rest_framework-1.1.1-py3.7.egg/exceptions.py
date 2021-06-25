"""
@Author: WangYuXiang
@E-mile: Hill@3io.cc
@CreateTime: 2021/1/20 20:03
@DependencyLibrary: 无
@MainFunction：无
@FileDoc:
    exceptions.py
    序列化器文件
"""

from sanic_rest_framework.status import HttpStatus, RuleStatus


class ValidatorAssertError(Exception):
    pass


class APIException(Exception):
    def __init__(self, message, status=RuleStatus.STATUS_0_FAIL, http_status=HttpStatus.HTTP_500_INTERNAL_SERVER_ERROR,
                 *args, **kwargs):
        self.message = message
        self.status = status
        self.http_status = http_status

    def response_data(self):
        return {
            'msg': self.message,
            'status': self.status,
            'http_status': self.http_status
        }


class ValidationException(Exception):
    """验证错误类"""
    default_detail = '无效的输入'
    default_code = 'invalid'

    def __init__(self, error_detail=None, code=None):
        if error_detail is None:
            error_detail = self.default_detail
        if code is None:
            code = self.default_code

        # For validation failures, we may collect many errors together,
        # so the details should always be coerced to a list if not already.
        if not isinstance(error_detail, dict) and not isinstance(error_detail, list):
            error_detail = [error_detail]

        self.code = code
        self.error_detail = error_detail
