"""
This library contains tools useful for using heedy in a notebook environment.

The intended usage is as follows::

    from heedy.nbtools import *

"""
import duckdb
from patsy import dmatrix, dmatrices


def sql(stmt):
    """
    Allows direct usage of sql statements on pandas dataframes. Allows easy joining and filtering of
    multiple data sources
    """
    return duckdb.query(stmt).to_df()


def dm(formula, data={}):
    """
    Generate design matrices
    """

    def stripIntercept(f, X):
        if not "+1" in f.replace(" ", "") and "Intercept" in X:
            X = X.drop(columns="Intercept")
        return X

    if "~" in formula:
        y, X = dmatrices(formula, data, return_type="dataframe", eval_env=1)
        return y, stripIntercept(formula.split("~")[1], X)
    return stripIntercept(
        formula, dmatrix(formula, data, return_type="dataframe", eval_env=1)
    )
