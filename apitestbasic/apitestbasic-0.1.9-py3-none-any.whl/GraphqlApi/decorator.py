import functools
from python_utils.formatters import camel_to_underscore
import time


class NotFoundId(Exception):
    pass


class CreateFailureError(Exception):
    pass


class GraphqlQuery:

    @staticmethod
    def set_query(*args_, **kwargs_):
        def out_wrapper(func):
            @functools.wraps(func)
            def inner_wrapper(instance, *args, **kwargs):
                # get sgqlc field name
                graphql_name = instance.camel_name
                # create operation
                if instance.flag:
                    instance.op = instance.new_operation()
                    instance.flag = False
                op = instance.op
                # change query
                result = func(instance, *args, **kwargs)
                if args_:
                    name = args_[0]
                    attrs = ".".join([graphql_name, name]).split(".")
                    f = op
                    for attr in attrs:
                        f = getattr(f, camel_to_underscore(attr))

                    f(*[camel_to_underscore(i) for i in args_[1:]], **kwargs_)
                # send requests
                return instance.f(op)

            return inner_wrapper

        return out_wrapper

    @staticmethod
    def get_id(api, method, *args_, **kwargs_):
        def out_wrapper(func):
            @functools.wraps(func)
            def inner_wrapper(instance, *args, **kwargs):
                a = api(instance.user)

                def g():
                    getattr(a, method)(*args_, **kwargs_)
                    try:
                        return a.data_id
                    except Exception as e:
                        print(e)
                        raise NotFoundId("%s not found id" % a.result)

                f_list = g()
                result = func(instance, *args, **kwargs)
                b_list = g()

                for i in b_list:
                    if i not in f_list:
                        setattr(instance, "id", i)
                        return result
                raise CreateFailureError("maybe create failure or some  problems about sort")

            return inner_wrapper

        return out_wrapper


class Decorator(object):

    # 记录函数执行时间
    @staticmethod
    def time_this(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print("%s cost %s s" % (func.__name__, end - start))
            return result

        return wrapper

    set_query = GraphqlQuery.set_query
    set_full_query = functools.partial(set_query, "__fields__")
    only_query_id = functools.partial(set_query, "data.__fields__", "id")
    set_fields = functools.partial(set_query, "data.__fields__")

    get_id = GraphqlQuery.get_id
