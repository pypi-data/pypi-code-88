import peewee
import inspect

from ..conf import settings


class WithSignal:
    callback = None
    @classmethod
    def add(cls, callback):
        cls.callback = callback

    def _execute(self, *args, **kwargs):
        if self.__class__.callback is not None:
            self.__class__.callback(self, inspect.stack())

        return super()._execute(*args, **kwargs)


class ModelUpdate(WithSignal, peewee.ModelUpdate):
    def _execute(self, *args, **kwargs):
        model_instance_or_none = None

        for field in self.table._meta.combined.values():
            if "pre_update" in dir(field):
                response = field.pre_update(self.dict_to_model())
                if response is not None:
                    model_instance_or_none = response

        if model_instance_or_none is not None:
            self._update = model_instance_or_none._normalize_data(None, model_instance_or_none.__data__.copy())

        super()._execute(*args, **kwargs)

    def dict_to_model(self):
        kwargs = {field.name: value for field, value in self._update.items()}
        return self.table(**kwargs)


class ModelSelect(WithSignal, peewee.ModelSelect):
    pass



def make_table_name(model):
    model_name = model.__name__
    pos = [i for i, e in enumerate(model_name + 'A') if e.isupper()]
    parts = [model_name[pos[j]:pos[j + 1]].lower() for j in range(len(pos) - 1)]
    table_name = "_".join(parts)
    return table_name


class Model(peewee.Model):
    class Meta:
        database = settings.DATABASE["peewee_engine"]
        table_function = make_table_name

    @classmethod
    def get_models(cls):
        return cls.__subclasses__()

    @classmethod
    def import_sql(cls):
        try:
            con = cls._meta.database.connect()
        except peewee.OperationalError:
            con = cls._meta.database.connection()

        sql = "\n".join(line for line in con.iterdump())

        return sql

    @classmethod
    def is_modified(cls):
        response = 0 < len(cls.__subclasses__())
        return response

    @classmethod
    def update(cls, __data=None, **update):
        return ModelUpdate(cls, cls._normalize_data(__data, update))

    @classmethod
    def select(cls, *fields):
        is_default = not fields
        if not fields:
            fields = cls._meta.sorted_fields
        return ModelSelect(cls, fields, is_default=is_default)
