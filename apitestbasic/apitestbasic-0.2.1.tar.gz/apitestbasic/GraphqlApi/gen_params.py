import random
from .tools import fake, create_timestamp
import weakref


# 重名情况
def handle_(item):
    if item.endswith("_"):
        return item[:-1]
    return item


class EasyList(list):

    def __getattr__(self, item):
        return EasyList([i.get(handle_(item)) for i in self])

    def __setattr__(self, key, value: list):
        if not len(self) == len(value):
            raise AssertionError("想要设置的列表长度不一样")
        for num, i in enumerate(self):
            i[handle_(key)] = value[num]


class EasyDict(dict):

    def __getattr__(self, item):
        return self.get(handle_(item))

    def __setattr__(self, key, value):
        self[handle_(key)] = value

    def pop_many(self, *args):
        for arg in args:
            self.pop(arg)

    def stay(self, *args):
        for i in list(self.keys()):
            if i not in args:
                self.pop(i)


class ParamType:
    __slots__ = ("is_required", "is_list", "type_", "in_list_required")

    def __init__(self, type_str: str = None):
        self.is_required = False
        self.is_list = False
        self.type_ = None
        self.in_list_required = False
        if type_str:
            self.handle(type_str)

    def handle(self, type_str):
        if type_str.endswith("!"):
            self.is_required = True
            type_str = type_str[:-1]
        if type_str.startswith("["):
            self.is_list = True
            type_str = type_str[1:-1]
            if type_str.endswith("!"):
                self.in_list_required = True
                type_str = type_str[:-1]
        self.type_ = type_str


class Cached(type):

    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls.__cache = weakref.WeakValueDictionary()

    def __call__(cls, name, *args):
        if args in cls.__cache:
            return cls.__cache[args]
        else:
            obj = super().__call__(name, *args)
            cls.__cache[args] = obj
            return obj


class GenParams(metaclass=Cached):
    def __init__(self, schema):
        self.schema = schema

    def gen(self, api, optional=False):
        result = EasyDict()
        for param in api.args.values():
            result[param.name] = self.__gen(param, optional)
        return result

    def __gen(self, param, optional):
        def handle(param_):
            r = EasyDict()
            for n in param_.__field_names__:
                t = getattr(param_, n)
                if optional and not ParamType(str(self.__type__(t))).is_required:
                    continue
                try:
                    r[param_.graphql_name] = self.__gen(t, optional)
                except AttributeError as e:
                    r[t.graphql_name] = self.__gen(t, optional)

            return r

        type_ = self.__type__(param)
        param_type = ParamType(str(type_))
        if param_type.is_list:
            if hasattr(type_, "converter") and "String" in str(type_):
                return EasyList([self._string(param) for i in range(3)])
            return EasyList([self.__gen(getattr(self.schema, param_type.type_), optional) for i in range(3)])
        elif hasattr(type_, "__field_names__"):
            result = handle(type_)
            return result
        elif hasattr(param, "__field_names__"):
            result = handle(param)
        elif hasattr(type_, "__choices__"):
            return random.choice(type_.__choices__)
        else:
            return getattr(self, "_" + str(param_type.type_).lower())(param)

    def __type__(self, obj):
        try:
            return obj.type
        except AttributeError as e:
            # print(e)
            return obj

    def _int(self, param):
        return fake.random_int

    def _float(self, param):
        return fake.pyfloat

    def _string(self, param):
        return getattr(fake, param.name)

    def _boolean(self, param):
        return random.choice([True, False])

    def _id(self, param):
        return 1

    def _timestamp(self, param):
        return create_timestamp()

    def _jsonstring(self, param):
        return "[]"

    def _json(self, param):
        return {"json": "json"}
