from functools import wraps
import contextlib

import numpy as np
import pandas as pd
import pandas.io.formats.format as pf

from IPython.display import display

from .outlier import ZscoreOutlierHandler


def describe_df(df, cardinality_ubound=10):
    @contextlib.contextmanager
    def float_and_int_formatting():
        orig_float_format = pd.options.display.float_format
        orig_int_format = pf.IntArrayFormatter

        pd.options.display.float_format = "{:0,.2f}".format

        class IntArrayFormatter(pf.GenericArrayFormatter):
            def _format_strings(self):
                formatter = self.formatter or "{:,d}".format
                fmt_values = [formatter(x) for x in self.values]
                return fmt_values

        pf.IntArrayFormatter = IntArrayFormatter
        yield
        pd.options.display.float_format = orig_float_format
        pf.IntArrayFormatter = orig_int_format

    # with pd.option_context('display.float_format', '{:,.2f}'.format).:
    with float_and_int_formatting():
        description_df = df.describe(include="all").T
        display(description_df.fillna(""))
    cat_description_df = df.select_dtypes(exclude="number")
    if (
        cat_description_df.shape[1] > 0
        and (description_df["unique"] <= cardinality_ubound).sum() > 0
    ):
        print("Categorical features distribution:")
        for c in cat_description_df:
            if df[c].nunique() <= cardinality_ubound:
                print(
                    c,
                    [
                        (k, v)
                        for k, v in df[c]
                        .value_counts(normalize=True, dropna=False)
                        .round(2)
                        .to_dict()
                        .items()
                    ],
                    sep=" ",
                )
    return


def summarize(df, count_missing=True, count_outliers=True, zscore_upperbound=3):
    display(df.head())
    display(df.shape)
    summary_df = pd.DataFrame(
        index=df.columns,
        data=np.nan,
        columns=["missing_count", "missing_perc", "outlier_count", "outlier_perc"],
    )
    summary_df["dtype"] = df.dtypes.apply(str)
    if count_missing:
        summary_df = summary_df.assign(
            missing_count=df.isnull().sum(axis=0),
            missing_perc=lambda s_df: (s_df["missing_count"] / df.shape[0]),
        )

    if count_outliers and df.select_dtypes(include="number").shape[1] > 0:
        scaled = ZscoreOutlierHandler.convert_zscore(df.select_dtypes(include="number"))
        summary_df = summary_df.assign(
            outlier_count=scaled.where(np.abs(scaled) > zscore_upperbound).count(
                axis=0
            ),
            outlier_perc=lambda df: (
                df["outlier_count"] / scaled.notnull().sum(axis=0)
            ),
        )

        summary_df = summary_df.assign(
            zero_count=(df.select_dtypes(include="number") == 0).sum(axis=0),
            zero_perc=lambda _df: (
                _df["zero_count"] / df.select_dtypes(include="number").shape[0]
            ),
            negative_count=(df.select_dtypes(include="number") < 0).sum(axis=0),
            negative_perc=lambda _df: (
                _df["negative_count"] / df.select_dtypes(include="number").shape[0]
            ),
        )
    print("\nSummary:")
    display(
        summary_df.replace(np.nan, 0)
        .loc[lambda df: ~((df["missing_count"] == 0) & (df["outlier_count"] == 0))]
        .sort_values(by=["missing_perc", "outlier_perc"], ascending=[False, False])
        .style.format(
            formatter=dict(
                zip(
                    [col for col in summary_df.columns if col.endswith("_perc")],
                    [
                        r"{:.2%}".format
                        for x in range(sum(summary_df.columns.str.endswith("_perc")))
                    ],
                )
            )
        )
        .format(
            formatter=dict(
                zip(
                    [col for col in summary_df.columns if col.endswith("_count")],
                    [
                        r"{:,.0f}".format
                        for x in range(sum(summary_df.columns.str.endswith("_count")))
                    ],
                )
            )
        )
        .background_gradient(axis=0)
    )

    if df.select_dtypes(include="number").shape[1] > 0:
        tmp = df.describe(include="number").T
        tmp.index.name = "Numeric features"
        print()
        display(tmp.style.format(r"{:,.1f}").background_gradient(axis=0))

    if df.select_dtypes(exclude="number").shape[1] > 0:
        tmp = df.describe(exclude="number").T
        tmp.index.name = "Categorical features"
        print()
        display(
            tmp.style.format(
                r"{:,.0f}", subset=[col for col in tmp.columns if col not in ["top"]]
            ).background_gradient(
                axis=0, subset=[col for col in tmp.columns if col not in ["top"]]
            )
        )
        for c in df.select_dtypes(exclude="number"):
            if df[c].nunique() <= 10:
                print(f"Categorical feature {c} distribution:")
                print(
                    c,
                    [
                        (k, v)
                        for k, v in df[c]
                        .value_counts(normalize=True, dropna=False)
                        .round(2)
                        .to_dict()
                        .items()
                    ],
                    sep=" ",
                )


def summarize_df(count_missing=True, count_outliers=True, zscore_upperbound=3):
    def _summarize_df(method):
        @wraps(method)
        def _summarize(*args, **kw):
            df = method(*args, **kw)
            if (
                kw.__contains__("activate_summarize_df_deco")
                and not kw["activate_summarize_df_deco"]
            ):
                return df
            summarize(
                df,
                count_missing=count_missing,
                count_outliers=count_outliers,
                zscore_upperbound=zscore_upperbound,
            )
            return df

        return summarize

    return _summarize_df
