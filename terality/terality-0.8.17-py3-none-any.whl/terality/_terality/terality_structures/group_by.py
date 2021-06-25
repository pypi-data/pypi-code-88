import pandas as pd

from . import ClassMethod, Struct


class ClassMethodGroupBy(ClassMethod):
    _class_name: str = "groupby"


class DataFrameGroupBy(Struct, metaclass=ClassMethodGroupBy):
    _class_name: str = "dataframe_groupby"
    # noinspection PyUnresolvedReferences
    _pandas_class_instance = pd.core.groupby.DataFrameGroupBy
    _additional_methods = Struct._additional_methods | {"sum", "mean"}
