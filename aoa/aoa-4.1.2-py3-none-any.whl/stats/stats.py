import json
import numpy as np
import os
import math

from typing import List, Dict
from teradataml.analytics.valib import *
from teradataml import configure
from teradataml.dataframe.dataframe import DataFrame
from decimal import Decimal

configure.val_install_location = os.environ.get("AOA_VAL_DB", "VAL")


class _NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating) or isinstance(obj, Decimal):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(_NpEncoder, self).default(obj)


def _get_reference_edges(variables, statistics, dtypes, bins=10):
    edges = []
    if os.path.isfile("artifacts/input/data_stats.json"):
        with open("artifacts/input/data_stats.json") as f:
            data_stats = json.load(f)

            training_stats = dict(data_stats["features"])
            training_stats.update(data_stats["predictors"])

            for v in variables:
                edges.append(training_stats[v]["statistics"]["histogram"]["edges"])

    else:
        # should return what is in the feature catalog.. for now calculate linspace boundaries based on min/max
        ranges = statistics.drop(statistics.columns.difference(["xcol", "xmin", "xmax"]), 1)
        ranges = ranges.set_index("xcol")
        ranges = ranges.to_dict(orient='index')

        for var in variables:
            x_min, x_max = ranges[var]["xmin"], ranges[var]["xmax"]

            # if integer type and range is less than the number of bins, only use 'range' bins
            if x_max - x_min < bins and dtypes[var].startswith("int"):
                edges.append(np.linspace(x_min, x_max, int(x_max) - int(x_min) + 1).tolist())
            # if decimal fix to two decimal places for now.. we really need to know the decimal precision to do this
            # correctly.
            elif dtypes[var].startswith("decimal") or dtypes[var].startswith("float"):
                # for bins other than 1st and last, round to two decimal places
                # (min / max must be rounded up / down accordingly so easier to just use the vals from stats)
                vals = np.linspace(x_min, x_max, bins + 1).tolist()

                for i in range(1, bins):
                    vals[i] = Decimal("{:.2f}".format(vals[i]))

                edges.append(vals)
            else:
                edges.append(np.linspace(x_min, x_max, bins + 1).tolist())

    return edges


def _convert_all_edges_to_val_str(all_edges):
    # boundaries for multiple columns follows the following format..
    # ["{10, 0, 200000}", "{5, 0, 100}"]
    boundaries = []
    for edges in all_edges:
        edges_str = ",".join(str(edge) for edge in edges)
        boundaries.append("{{ {} }}".format(edges_str))

    return boundaries


def _fill_missing_bins(bin_edges, bin_values, var_ref_edges):
    epsilon = 1e-08
    for i, edge in enumerate(var_ref_edges):
        is_present = False
        for curr_edge in bin_edges:
            if abs(float(curr_edge) - float(edge)) < epsilon:
                is_present = True

        if not is_present:
            bin_values.insert(i, 0.0)


def _strip_key_x(d: Dict):
    return {k[1:]: v for k, v in d.items()}


def _process_categorical_var(frequencies, group_label, var, importance, category_labels, is_ordinal):
    data_struct = {
        "type": "categorical",
        "group": group_label,
        "category_labels": category_labels,
        "ordinal": is_ordinal,
        "statistics": {}
    }

    var_freq = frequencies[frequencies.xcol == var]

    # if first row is nan then it is the null values in the dataset. remove from histogram
    if var_freq["xval"].isnull().values.any():
        n = var_freq[var_freq["xval"].isnull()]
        data_struct["statistics"]["nulls"] = n.xcnt.tolist()[0]

        var_freq = var_freq[var_freq["xval"].notnull()]

    data_struct["statistics"]["frequency"] = var_freq[["xval", "xcnt"]].set_index("xval").T.to_dict(orient='records')[0]

    if var in importance:
        data_struct["importance"] = importance[var]

    return data_struct


def _process_continuous_var(hist, stats, var_ref_edges, group_label, var, importance):
    data_struct = {
        "type": "continuous",
        "group": group_label,
        "statistics": {},
    }

    var_hist = hist[hist.xcol == var].sort_values(by=['xbin'])

    # if first row is nan then it is the null values in the dataset. remove from histogram
    if var_hist["xbin"].isnull().values.any():
        n = var_hist[var_hist["xbin"].isnull()]
        data_struct["statistics"]["nulls"] = n.xcnt.tolist()[0]

        var_hist = var_hist[var_hist["xbin"].notnull()]

    bin_edges = [var_hist.xbeg.tolist()[0]] + var_hist.xend.tolist()
    bin_values = var_hist.xcnt.tolist()

    # (issue #123) VAL docs originally stated that:
    # VAL histograms will values lower than the first bin to the first bin, but values greater than the
    # largest bin are added to a new bin.. Therefore we did the same on both sides. However, it turns out this doc is
    # incorrect.

    is_right_outlier_bin = math.isnan(bin_edges[-1])
    is_left_outlier_bin = math.isnan(bin_edges[0])
    if is_right_outlier_bin:
        bin_edges = bin_edges[:-1]
    if is_left_outlier_bin:
        bin_edges = bin_edges[1:]

    # Add missing bin_values based on the bin_edges vs reference_edges.
    # VAL doesn't return empty bins
    if len(bin_edges) < len(var_ref_edges):
        _fill_missing_bins(bin_edges, bin_values, var_ref_edges)

    if is_right_outlier_bin:
        bin_values[-2] += bin_values[-1]
        bin_values = bin_values[:-1]
    if is_left_outlier_bin:
        bin_values[1] += bin_values[0]
        bin_values = bin_values[1:]

    stats_values = stats[stats.xcol == var].drop(["xdb", "xtbl", "xcol"], axis=1).to_dict(orient='records')[0]
    data_struct["statistics"].update(_strip_key_x(stats_values))

    data_struct["statistics"]["histogram"] = {
        "edges": var_ref_edges,
        "values": bin_values
    }

    if var in importance:
        data_struct["importance"] = importance[var]

    return data_struct


def record_stats(df: DataFrame,
                 features: List,
                 predictors: List,
                 categorical: List,
                 category_labels: Dict,
                 category_ordinals: Dict = {},
                 importance: Dict = {},
                 feature_group="default",
                 predictor_group="default"):
    """

    example usage:
        pima = DataFrame("PIMA_TRAIN")

        record_stats(pima,
                   features=["TwoHourSerIns", "Age"],
                   predictors=["HasDiabetes"],
                   categorical=["HasDiabetes"],
                   importance={"Age": 0.9, "TwoHourSerIns": 0.1},
                   category_labels={"HasDiabetes": {0: "false", 1: "true"}})

    :param df:
    :param features:
    :param predictors:
    :param categorical:
    :param category_labels:
    :param category_ordinals:
    :param importance:
    :param feature_group:
    :param predictor_group:
    :return:
    """
    if not isinstance(df, DataFrame):
        raise ValueError("We only support teradataml DataFrame currently")

    if not all(k in category_labels for k in categorical):
        raise ValueError("You must specify a category_label for each categorical variable")

    total_rows = df.shape[0]
    dtypes = {r[0]: r[1] for r in df.dtypes._column_names_and_types}

    continuous_vars = list((set(features) | set(predictors)) - set(categorical))

    reference_edges = []

    if len(continuous_vars) > 0:
        stats = valib.Statistics(data=df, columns=','.join(continuous_vars), stats_options="all")
        stats = stats.result.to_pandas().reset_index()

        reference_edges = _get_reference_edges(continuous_vars, stats, dtypes)

        hist = valib.Histogram(data=df, columns=','.join(continuous_vars),
                               boundaries=_convert_all_edges_to_val_str(reference_edges))
        hist = hist.result.to_pandas().reset_index()

    if len(categorical) > 0:
        frequencies = valib.Frequency(data=df, columns=','.join(categorical))
        frequencies = frequencies.result.to_pandas().reset_index()

    data_struct = {
        "num_rows": total_rows,
        "features": {},
        "predictors": {}
    }

    def add_var_metadata(var, group_label):

        if var in continuous_vars:
            var_ref_edges = reference_edges[continuous_vars.index(var)]

            data_struct["features"][var] = _process_continuous_var(
                hist,
                stats,
                var_ref_edges,
                group_label,
                var,
                importance)

        else:
            data_struct["predictors"][var] = _process_categorical_var(
                frequencies,
                group_label,
                var,
                importance,
                category_labels[var],
                category_ordinals.get(var, False))

    for var in features:
        add_var_metadata(var, feature_group)

    for var in predictors:
        add_var_metadata(var, predictor_group)

    with open("artifacts/output/data_stats.json", 'w+') as f:
        json.dump(data_struct, f, indent=2, cls=_NpEncoder)
