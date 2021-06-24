from functools import wraps


def get_num_diff_rows(remove_kind="rows"):
    def _calc_diff(method):
        @wraps(method)
        def _calc(*args, **kw):
            old_df = args[0]
            result_df = method(*args, **kw)
            delta_units = result_df.shape[0] - old_df.shape[0]
            delta_units_perc = delta_units / old_df.shape[0]
            print(
                f"{method.__name__} >> {delta_units:,} ({delta_units_perc:,.2%}) {remove_kind} removed"
            )
            return result_df

        return _calc

    return _calc_diff


def get_shape_diff():
    def _calc_diff(method):
        @wraps(method)
        def _calc(*args, **kw):
            old_df = args[0]
            result_df = method(*args, **kw)
            delta_rows = result_df.shape[0] - old_df.shape[0]
            delta_rows_perc = delta_rows / old_df.shape[0]
            delta_columns = result_df.shape[1] - old_df.shape[1]
            delta_columns_perc = delta_columns / old_df.shape[1]
            print(
                f"{method.__name__} >> Delta shape: ({delta_rows:,}, {delta_columns:,}) | ({delta_rows_perc:,.1%}, {delta_columns_perc:,.1%})"
            )
            return result_df

        return _calc

    return _calc_diff
