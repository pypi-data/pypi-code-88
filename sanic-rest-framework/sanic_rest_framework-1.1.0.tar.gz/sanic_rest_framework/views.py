"""
@Author: WangYuXiang
@E-mile: Hill@3io.cc
@CreateTime: 2021/1/19 15:44
@DependencyLibrary:
@MainFunction：
@FileDoc:
    login.py
    基础视图文件
    BaseView    只实现路由分发的基础视图
    GeneralView 通用视图，可以基于其实现增删改查，提供权限套件
    ViewSetView 视图集视图，可以配合Mixin实现复杂的视图集，
                数据来源基于模型查询集,可以配合Route组件实现便捷的路由管理



"""
import inspect
from datetime import datetime

from sanic.log import logger
from sanic.response import json, HTTPResponse
from tortoise.exceptions import IntegrityError

from sanic_rest_framework import mixins
from sanic_rest_framework.constant import ALL_METHOD, DEFAULT_METHOD_MAP
from sanic_rest_framework.exceptions import APIException, ValidationException
from sanic_rest_framework.filters import SearchFilter, ORMAndFilter
from sanic_rest_framework.status import RuleStatus, HttpStatus
from simplejson import dumps, JSONEncoder
from tortoise.queryset import QuerySet

__all__ = ['BaseView', 'GeneralView', 'ViewSetView', 'ModelViewSet']


class BaseView:
    """只实现路由分发的基础视图
    在使用时应当开放全部路由 ALL_METHOD
    app.add_route('/test', BaseView.as_view(), 'test', ALL_METHOD)
    如需限制路由则在其他地方注明
    app.add_route('/test', BaseView.as_view(), 'test', ALL_METHOD)
    注意以上方法的报错是不可控的
    """

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    async def dispatch(self, request, *args, **kwargs):
        """分发路由"""
        request.user = None
        method = request.method
        if method.lower() not in self.method_map:
            return HTTPResponse('405请求方法错误', status=405)
        handler = getattr(self, method.lower(), None)
        response = handler(request, *args, **kwargs)
        if inspect.isawaitable(response):
            response = await response
        return response

    @classmethod
    def get_method_map(cls):
        methods = {}
        for method in ALL_METHOD:
            method = method.lower()
            if hasattr(cls, method):
                methods[method] = method
        return methods

    @classmethod
    def as_view(cls, method_map=DEFAULT_METHOD_MAP, *class_args, **class_kwargs):

        # 返回的响应方法闭包
        def view(request, *args, **kwargs):
            self = view.base_class(*class_args, **class_kwargs)
            view_method_map = {}
            for method, action in method_map.items():
                handler = getattr(self, action, None)
                if handler:
                    setattr(self, method, handler)
                    view_method_map[method] = action

            self.method_map = view_method_map
            self.methods = list(view_method_map.keys())
            self.request = request
            self.args = args
            self.kwargs = kwargs
            self.app = request.app
            return self.dispatch(request, *args, **kwargs)

        view.base_class = cls
        view.methods = list(method_map.keys())
        view.API_DOC_CONFIG = class_kwargs.get('API_DOC_CONFIG')  # 未来的API文档配置属性+
        view.__doc__ = cls.__doc__
        view.__module__ = cls.__module__
        view.__name__ = cls.__name__
        return view


class GeneralView(BaseView):
    """通用视图，可以基于其实现增删改查，提供权限套件"""
    authentication_classes = ()
    permission_classes = ()

    async def dispatch(self, request, *args, **kwargs):
        """分发路由"""
        request.user = None
        method = request.method
        if method.lower() not in self.methods:
            return self.json_response(msg='发生错误：未找到%s方法' % method, status=RuleStatus.STATUS_0_FAIL,
                                      http_status=HttpStatus.HTTP_405_METHOD_NOT_ALLOWED)
        handler = getattr(self, method.lower(), None)

        try:
            await self.initial(request, *args, **kwargs)
            response = handler(request, *args, **kwargs)
            if inspect.isawaitable(response):
                response = await response
        except APIException as exc:
            response = self.handle_exception(exc)
        except ValidationException as exc:
            response = self.error_json_response(exc.error_detail, '数据验证失败')
        except AssertionError as exc:
            raise exc
        except IntegrityError as exc:
            response = self.json_response(msg=str(exc), status=RuleStatus.STATUS_0_FAIL)
        except Exception as exc:
            logger.error('--捕获未知错误--', exc)
            msg = '发生致命的未知错误，请在服务器查看时间为{}的日志'.format(datetime.now().strftime('%F %T'))
            response = self.json_response(msg=msg, status=RuleStatus.STATUS_0_FAIL,
                                          http_status=HttpStatus.HTTP_500_INTERNAL_SERVER_ERROR)
        return response

    def handle_exception(self, exc: APIException):
        return self.json_response(**exc.response_data())

    def json_response(self, data=None, msg="OK", status=RuleStatus.STATUS_1_SUCCESS,
                      http_status=HttpStatus.HTTP_200_OK):
        """
        Json 相应体
        :param data: 返回的数据主题
        :param msg: 前台提示字符串
        :param status: 前台约定状态，供前台判断是否成功
        :param http_status: Http响应数据
        :return:
        """
        if data is None:
            data = {}
        response_body = {
            'data': data,
            'message': msg,
            'status': status
        }
        return json(body=response_body, status=http_status, dumps=dumps)

    def success_json_response(self, data=None, msg="Success", **kwargs):
        """
        快捷的成功的json响应体
        :param data: 返回的数据主题
        :param msg: 前台提示字符串
        :return: json
        """
        status = kwargs.pop('status', RuleStatus.STATUS_1_SUCCESS)
        http_status = kwargs.pop('http_status', HttpStatus.HTTP_200_OK)
        return self.json_response(data=data, msg=msg, status=status, http_status=http_status)

    def error_json_response(self, data=None, msg="Fail", **kwargs):
        """
        快捷的失败的json响应体
        :param data: 返回的数据主题
        :param msg: 前台提示字符串
        :return: json
        """
        status = kwargs.pop('status', RuleStatus.STATUS_0_FAIL)
        http_status = kwargs.pop('http_status', HttpStatus.HTTP_400_BAD_REQUEST)
        return self.json_response(data=data, msg=msg, status=status, http_status=http_status)

    def get_authenticators(self):
        """
        实例化并返回此视图可以使用的身份验证器列表
        """
        return [auth() for auth in self.authentication_classes]

    async def check_authentication(self, request):
        """
        检查权限 查看是否拥有权限，并在此处为Request.User 赋值
        :param request: 请求
        :return:
        """
        for authenticators in self.get_authenticators():
            await authenticators.authenticate(request)

    def get_permissions(self):
        """
        实例化并返回此视图所需的权限列表
        """
        return [permission() for permission in self.permission_classes]

    async def check_permissions(self, request):
        """
        检查是否应允许该请求，如果不允许该请求，
        则在 has_permission 中引发一个适当的异常。
        :param request: 当前请求
        :return:
        """
        for permission in self.get_permissions():
            await permission.has_permission(request, self)

    async def check_object_permissions(self, request, obj):
        """
        检查是否应允许给定对象的请求, 如果不允许该请求，
        则在 has_object_permission 中引发一个适当的异常。
            常用于 get_object() 方法
        :param request: 当前请求
        :param obj: 需要鉴权的模型对象
        :return:
        """
        for permission in self.get_permissions():
            await permission.has_object_permission(request, self, obj)

    async def check_throttles(self, request):
        """
        检查范围频率。
        则引发一个 APIException 异常。
        :param request:
        :return:
        """
        pass

    async def initial(self, request, *args, **kwargs):
        """
        在请求分发之前执行初始化操作，用于检查权限及检查基础内容
        """
        await self.check_authentication(request)
        await self.check_permissions(request)
        await self.check_throttles(request)


class ViewSetView(GeneralView):
    """
    视图集视图，可以配合Mixin实现复杂的视图集，
    数据来源基于模型查询集,可以配合Route组件实现便捷的路由管理
    """
    queryset = None
    lookup_field = 'pk'
    serializer_class = None
    pagination_class = None
    filter_class = ORMAndFilter
    search_fields = None

    async def get_object(self):
        """
        返回视图显示的对象。
        如果您需要提供非标准的内容，则可能要覆盖此设置
        queryset查找。
        """
        queryset = await self.filter_queryset(await self.get_queryset())

        lookup_field = self.lookup_field

        assert lookup_field in self.kwargs, (
                '%s 不存在于 %s 的 Url配置中的关键词内 ' %
                (lookup_field, self.__class__.__name__,)
        )

        filter_kwargs = {lookup_field: self.kwargs[lookup_field]}
        obj = await queryset.get_or_none(**filter_kwargs)
        if obj is None:
            raise APIException('不存在%s为%s的数据' % (lookup_field, self.kwargs[lookup_field]),
                               http_status=HttpStatus.HTTP_200_OK)

        # May raise a permission denied
        await self.check_object_permissions(self.request, obj)

        return obj

    async def get_queryset(self):
        assert self.queryset is not None, (
                "'%s'应该包含一个'queryset'属性，"
                "或重写`get_queryset()`方法。"
                % self.__class__.__name__
        )
        queryset = self.queryset
        filter_orm = await self.filter_orm()
        queryset = queryset.filter(filter_orm)
        return queryset

    async def filter_orm(self):
        """得到ORM过滤参数"""
        return self.filter_class(self.request, self).orm_filter

    def get_serializer(self, *args, **kwargs):
        """
        返回应该用于验证和验证的序列化程序实例
        对输入进行反序列化，并对输出进行序列化。
        """
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
        return serializer_class(*args, **kwargs)

    def get_serializer_class(self):
        """
        返回用于序列化器的类。
        默认使用`self.serializer_class`。

        如果您需要提供其他信息，则可能要覆盖此设置
        序列化取决于传入的请求。

        （例如，管理员获得完整的序列化，其他获得基本的序列化）
        """
        assert self.serializer_class is not None, (
                "'%s' should either include a `serializer_class` attribute, "
                "or override the `get_serializer_class()` method."
                % self.__class__.__name__
        )
        return self.serializer_class

    def get_serializer_context(self):
        """
        提供给序列化程序类的额外上下文。
        """
        return {
            'request': self.request,
            'view': self
        }

    @property
    def paginator(self) -> ORMPagination:
        """
        与视图关联的分页器实例，或“None”。
        """
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class(self.request, self)
        return self._paginator

    async def get_paginator_count(self, queryset):
        """
        获取记录总数
        :param queryset:
        :return:
        """
        return await queryset.count()

    async def paginate_queryset(self, queryset):
        """
        返回单页结果，如果禁用了分页，则返回“无”。
        """
        if self.paginator is None:
            return None
        offset = (self.paginator.query_page - 1) * self.paginator.query_page_size
        return queryset.limit(self.paginator.query_page_size).offset(offset)

    def get_paginated_response(self, data):
        """
        返回给定输出数据的分页样式`Response`对象。
        """
        return {
            'count': self.paginator.count,
            'next': self.paginator.next_link,
            'next_page_num': self.paginator.next_page,
            'previous': self.paginator.previous_link,
            'previous_num': self.paginator.previous_page,
            'results': data
        }


class ModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   ViewSetView):
    """
    `create()`, `retrieve()`, `update()`, `partial_update()`, `destroy()`, `list()` actions.
    """
    pass
