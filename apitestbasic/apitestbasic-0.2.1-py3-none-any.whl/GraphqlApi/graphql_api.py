from python_utils.formatters import camel_to_underscore
from sgqlc.operation import Operation
from .decorator import Decorator


class Register(type):
    __register_api__ = {}

    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if getattr(cls, "api"):
            cls.__register_api__[args[0]] = cls

    def __call__(cls, *args, **kwargs):
        instance = super(Register, cls).__call__(*args, **kwargs)
        setattr(instance, "register_api", cls.register_api)
        return instance

    @property
    def register_api(cls):
        return cls.__register_api__


class GraphqlApi(metaclass=Register):
    api = None

    def __init__(self, user):
        self.user = user
        self.flag = False
        self.api_name = self.api.graphql_name
        self.camel_name = camel_to_underscore(self.api.name)
        self.sgqlc_schema = self.api.container
        self.op = self.new_operation()
        self.data = None
        self.result = None
        self.old_result = None

    # create operation
    def new_operation(self):
        op = Operation(self.sgqlc_schema)
        return op

    @property
    def op(self):
        return self._op

    @op.setter
    def op(self, value):
        self._op = value
        self.api_op = getattr(self._op, self.camel_name)

    # send requests
    def f(self, op):
        self.flag = True
        self.old_result = self.result
        self.data = self.user.f(self.api_name, op)
        self.result = EasyResult(getattr(op + self.data, self.camel_name))
        return self

    # get result
    def __getattr__(self, item):
        if item.startswith("old_"):
            return getattr(self.old_result, item[4:])
        return getattr(self.result, item)

    @Decorator.set_query()
    def run(self, *args, **kwargs):
        self.api_op(*args, **kwargs)


class EasyResult(object):
    __slots__ = ["obj"]

    def __init__(self, obj):
        self.obj = obj

    def __len__(self):
        return len(self.obj)

    def __getattr__(self, item):
        if isinstance(self.obj, list):
            return EasyResult([getattr(i, item) for i in self.obj])
        else:
            result = EasyResult(getattr(self.obj, item))
            if isinstance(result.obj, str) or isinstance(result.obj, int) or isinstance(result.obj, float):
                return result.obj
            else:
                return result

    def __getitem__(self, item):
        return EasyResult(self.obj[item])

    def __eq__(self, other):
        if isinstance(other, list):
            flag = True
            for i in other:
                if i not in self.obj:
                    flag = False
                    break
            if flag:
                for i in self.obj:
                    if i not in other:
                        flag = False
                        break
            return flag
        elif isinstance(other, int):
            return str(self.obj) == str(other)

        return self.obj == other

    def __str__(self):
        return str(self.obj)

    def __repr__(self):
        return self.__str__()

    @property
    def value(self):
        return self.obj
