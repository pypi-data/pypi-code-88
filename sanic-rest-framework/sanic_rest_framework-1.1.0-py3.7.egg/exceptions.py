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
from typing import Mapping

from sanic.response import json

from sanic_rest_framework.status import HttpStatus, RuleStatus

#
# class ValidationError(Exception):
#     """验证器通用错误类 发生错误即抛出此类"""
#
#     def __init__(self, message, code=None, params=None):
#         super().__init__(message, code, params)
#         if isinstance(message, ValidationError):
#             if hasattr(message, 'error_dict'):
#                 message = message.error_dict
#             elif not hasattr(message, 'message'):
#                 message = message.error_list
#             else:
#                 message, code, params = message.message, message.code, message.params
#         if isinstance(message, dict):
#             self.error_dict = {}
#             for field, msg in message.items():
#                 if not isinstance(msg, ValidationError):
#                     msg = ValidationError(msg)
#                 if hasattr(msg, 'error_dict'):
#                     self.error_dict[field] = [msg.error_dict]
#                 else:
#                     self.error_dict[field] = msg.error_list
#         elif isinstance(message, list):
#             self.error_list = []
#             for message in message:
#                 if not isinstance(message, ValidationError):
#                     message = ValidationError(message)
#                 if hasattr(message, 'error_dict'):
#                     self.error_list.extend(sum(message.error_dict.values(), []))
#                 else:
#                     self.error_list.extend(message.error_list)
#         else:
#             self.message = message
#             self.code = code
#             self.params = params
#             self.error_list = [self]
#
#     @property
#     def message_dict(self):
#         getattr(self, 'error_dict')
#         return dict(self)
#
#     @property
#     def messages(self):
#         if hasattr(self, 'error_dict'):
#             return sum(dict(self).values(), [])
#         return list(self)
#
#     def update_error_dict(self, error_dict):
#         if hasattr(self, 'error_dict'):
#             for field, error_list in self.error_dict.items():
#                 error_dict.setdefault(field, []).extend(error_list)
#         else:
#             error_dict.setdefault('__all__', []).extend(self.error_list)
#         return error_dict
#
#     def __iter__(self):
#         if hasattr(self, 'error_dict'):
#             for field, errors in self.error_dict.items():
#                 yield field, list(ValidationError(errors))
#         else:
#             for error in self.error_list:
#                 message = error.message
#                 if error.params:
#                     message %= error.params
#                 yield str(message)
#
#     def __str__(self):
#         if hasattr(self, 'error_dict'):
#             return repr(dict(self))
#         return repr(list(self))
#
#     def __repr__(self):
#         return 'ValidationError(%s)' % self
#
#     def __eq__(self, other):
#         if not isinstance(other, ValidationError):
#             return NotImplemented
#         return hash(self) == hash(other)


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
