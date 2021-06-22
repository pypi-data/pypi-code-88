from .graphql_api import GraphqlApi
from .decorator import Decorator
from .gen_params import GenParams
from functools import partial


class FieldValueNotExistError(Exception):
    pass


class GraphqlQueryListAPi(GraphqlApi):

    @Decorator.set_query()
    def query(self, offset=0, limit=10, **kwargs):
        self.api_op(offset=offset, limit=limit, **kwargs)

    @Decorator.set_full_query()
    def query_full(self, offset=0, limit=10, **kwargs):
        self.api_op(offset=offset, limit=limit, **kwargs)

    @Decorator.only_query_id()
    def query_ids(self, offset=0, limit=10, **kwargs):
        self.api_op(offset=offset, limit=limit, **kwargs)

    def search(self, field_name, field_value):
        try:
            print(self.result)
            data = self.result.data
        except AttributeError:
            raise Exception("result is not list: %s" % self.result)
        for o in data:
            if getattr(o, field_name) == field_value:
                return o
        raise FieldValueNotExistError("field %s not found value %s" % (field_name, field_value))

    def search_return_dict(self, field_name, field_value):
        return dict(self.search(field_name, field_value).__json_data__)

    def assert_search_fail(self, field_name, field_value):
        try:
            result = self.search(field_name, field_value)
            raise AssertionError("field %s should not found value %s,but it found" % (field_name, field_value))
        except FieldValueNotExistError:
            pass

    def normal_request(self):
        return self.query()


class GraphqlQueryAPi(GraphqlApi):

    @Decorator.set_query()
    def query(self, id_):
        self.api_op(id=id_)

    @Decorator.set_full_query()
    def query_full(self, id_):
        self.api_op(id=id_)


class GraphqlOperationAPi(GraphqlApi):

    def __init__(self, user):
        super(GraphqlOperationAPi, self).__init__(user)
        self._gen = partial(GenParams(self.api.schema).gen, self.api)
        self.variables = self.new_var()

    @Decorator.set_query()
    def manual_run(self, **kwargs):
        self.api_op(**kwargs)

    @Decorator.set_full_query()
    def manual_run_return_all(self, **kwargs):
        self.api_op(**kwargs)

    def new_var(self, optional=False):
        self.variables = self._gen(optional)
        return self.variables

    def run(self):
        self.manual_run(**self.variables)

    def run_return_all(self, **kwargs):
        self.manual_run_return_all(**self.variables)


class GraphqlUpdateAPi(GraphqlOperationAPi):

    def __init__(self, user, set_id=None):
        self.set_id = set_id
        super(GraphqlUpdateAPi, self).__init__(user)

    @property
    def id(self):
        return self.set_id

    @id.setter
    def id(self, value):
        self.set_id = value
        self.variables.input.id = self.set_id

    def new_var(self, optional=False):
        self.variables = self._gen(optional)
        self.variables.input.id = self.set_id
        return self.variables


class GraphqlApiExtension:
    GraphqlQueryListAPi = GraphqlQueryListAPi
    GraphqlQueryAPi = GraphqlQueryAPi
    GraphqlOperationAPi = GraphqlOperationAPi
    GraphqlUpdateAPi = GraphqlUpdateAPi
