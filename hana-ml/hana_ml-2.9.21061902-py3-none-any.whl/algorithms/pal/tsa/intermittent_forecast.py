"""
This module contains Python wrappers for PAL exponential smoothing algorithms.

The following classes are available:

    * :func:`intermittent_forecast`

"""
import logging
import uuid

from hdbcli import dbapi
from hana_ml.algorithms.pal.pal_base import (
    ParameterTable,
    arg,
    try_drop,
    require_pal_usable,
    call_pal_auto
)

logger = logging.getLogger(__name__)#pylint:disable=invalid-name

def intermittent_forecast(data, key=None, endog=None, p=None, q=None,#pylint:disable=too-many-statements, too-many-arguments, too-many-locals, invalid-name
                          forecast_num=None, optimizer=None,
                          method=None, grid_size=None, optimize_step=None,
                          accuracy_measure=None, ignore_zero=None,
                          expost_flag=None, thread_ratio=None):
    r"""
    This function is a wrapper for PAL
    **Intermittent Time Series Forecast (ITSF)**, which is a new forecast
    strategy for products with intermittent demand.

    Difference to constant weight of the croston method:

        - ITSF provides a exponential weight to estimate, which means
          the closer the data, the greater the weight

        - ITSF does not need the initial value of non-zero demands and
          time interval between non-zero demands

    Parameters
    ----------
    data : DataFrame
        Data that contains the time-series analysis.

    key : str, optional
        Specifies the ID(representing time-order) column of ``data``.

        Required if a single ID column cannot be inferred from the index of ``data``.

        If there is a single column name in the index of ``data``,
        then ``key`` defaults to that column; otherwise ``key`` is mandatory.

    endog : str, optional
        Specifies name of the column for intermittent demand values.

        Defaults to the 1st non-key column of ``data``.

    p : int, optional
        The smoothing parameter for demand, where:

            - -1 : optimizing this parameter automatically
            - positive integers : the specified  value for smoothing, cannot exceed
              length of time-series for analysis.

        The specified value cannot exceed the length of time-series for analysis.

        Defaults to -1.

    q : int, optional
        The smoothing parameter for the time-intervals between intermittent demands, where:

            - -1 : optimizing this parameter automatically
            - non-negative integers : the specified value for smoothing, cannot exceed
              the value of ``p``.

        Defaults to -1.

    forecast_num : int, optional
        Number of values to be forecast.

        When it is set to 1, the algorithm only forecasts one value.

        Defaults to 1.

    optimizer : {'lbfgsb_default', 'lbfgsb_grid'}, optional
        Specifies the optimization algorithm for automatically identifying
        parameters ``p`` and ``q``.

            - 'lbfgsb_default' :  Bounded Limited-memory Broyden-Fletcher-Goldfarb-Shanno(LBFGSB)
              method with parameters ``p`` and ``q`` initialized by default scheme.

            - 'lbfgsb_grid' : LBFGSB method, with parameter ``p`` and ``q``
              initialized by grid search.

        Defaults to 'lbfgsb_default'.

    method : str, optional
        Specifies the method(or mode) for the output:

            - 'sporadic': Use the sporadic method.
            - 'constant': Use the constant method.

        Defaults to 'constant'.

    grid_size : int, optional
        Specifying the number of steps from the start point to the length of data for grid search.

        Only valid for when ``optimizer`` is set as 'lbfgsb_grid'.

        Defaults to 20.

    optimize_step : float, optional
        Specifying minimum step for each iteration of LBFGSB method.

        Defaults to 0.001.

    accuracy_measure : {'mse', 'rmse', 'mae', 'mape', 'smape', 'mase'}, optional
        The criterion used for the optimization.

        Defaults to 'mse'.

        .. Note::
            Specify a measure name if you want the corresponding measure value to be
            reflected in the output statistics.

    ignore_zero : bool, optional

        - False: Uses zero values in the input dataset when calculating 'mape'.
        - True: Ignores zero values in the input dataset when calculating 'mape'.

        Only valid when ``accuracy_measure`` is 'mape'.

        Defaults to False.

    expost_flag : bool, optional

       - False: Does not output the expost forecast, and just outputs the forecast values.
       - True: Outputs the expost forecast and the forecast values.

       Defaults to True.

    thread_ratio : float, optional
        Specify the ratio of available threads for performing ITSF.

            - 0 : single thread
            - 0~1 : percentage

        Defaults to 0.

    Returns
    -------
    DataFrames

       A tuple of two DataFrames, where:

           - the 1st DateFrame stores forecast values.
           - the 2nd DataFrame stores related statistics.

    Examples
    --------

    Time-series data for intermittent forecast:

    >>> data.collect()
        ID  RAWDATA
    0    0      0.0
    1    1      1.0
    2    2      4.0
    3    3      0.0
    4    4      0.0
    5    5      0.0
    6    6      5.0
    7    7      3.0
    8    8      0.0
    9    9      0.0
    10  10      0.0

    Apply intermittent forecast to the given time-series data:

    >>> forecasts, stats = intermittent_forecast(data=data, p=3, forecast_num=3,
    ...                                          optimizer='lbfgsb_grid', grid_size=20,
    ...                                          optimize_step = 0.011, expost_flag=False,
    ...                                          accuracy_measure='mse', ignore_zero=False,
    ...                                          thread_ratio=0.5)

    Check the ouput DataFrames:

    >>> forecasts.collect()
       ID   RAWDATA
    0  12  2.831169
    1  13  2.831169
    2  14  2.831169
    >>> output[1].collect()
           STAT_NAME  STAT_VALUE
    0            MSE   10.650383
    1    LAST_DEMAND    3.892857
    2  LAST_INTERVAL    0.000000
    3          OPT_P    3.000000
    4          OPT_Q    0.000000
    5      OPT_STATE    0.000000
"""
    conn = data.connection_context
    require_pal_usable(conn)
    method_map = {'constant':0, 'sporadic':1}
    optimizer_map = {'lbfgsb_default': 0, 'lbfgsb_grid': 1}
    measures = ['mse', 'rmse', 'mae', 'mape', 'smape', 'mase']
    cols = data.columns
    if len(cols) < 2:
        msg = ("Input data should contain at least 2 columns: " +
               "one for ID, another for raw data.")
        logger.error(msg)
        raise ValueError(msg)
    index = data.index
    key = arg('key', key, str, not isinstance(index, str))
    if key is not None:
        if key not in cols:
            msg = ('Please select key from name of columns!')
            logger.error(msg)
            raise ValueError(msg)
    if isinstance(index, str):
        if key is not None and index != key:
            msg = "Discrepancy between the designated key column '{}' ".format(key) +\
            "and the designated index column '{}'.".format(index)
            logger.warning(msg)
    key = index if key is None else key
    cols.remove(key)
    endog = arg('endog', endog, str)
    if endog not in cols + [None]:
        msg = ('Please select endog from name of columns!')
        logger.error(msg)
        raise ValueError(msg)
    endog = cols[0] if endog is None else endog
    p = arg('p', p, int)
    if p is not None and p > data.count():
        msg = 'The value of p exceeds the length of time-series.'
        raise ValueError(msg)
    q = arg('q', q, int)
    if all(x is not None for x in [p, q]):
        if p != -1 and q > p:
            msg = 'The value of q is greater than p.'
            raise ValueError(msg)
    forecast_num = arg('forecast_num', forecast_num, int)
    optimizer = arg('optimizer', optimizer, optimizer_map)
    method = arg('method', method, method_map)
    grid_size = arg('grid_size', grid_size, int)
    optimize_step = arg('optimize_step', optimize_step, float)
    accuracy_measure = arg('accuracy_measure', accuracy_measure,
                           {ms:ms.upper() for ms in measures})
    ignore_zero = arg('ignore_zero', ignore_zero, bool)
    expost_flag = arg('expost_flag', expost_flag, bool)
    thread_ratio = arg('thread_ratio', thread_ratio, float)
    data_ = data[[key] + [endog]]
    unique_id = str(uuid.uuid1()).replace('-', '_').upper()
    outputs = ['FORECAST', 'STATS']
    outputs = ['#PAL_ITSF_{}_TBL_{}'.format(name, unique_id) for name in outputs]
    forecast_tbl, stats_tbl = outputs

    param_rows = [('P', p, None, None),
                  ('Q', q, None, None),
                  ('FORECAST_NUM', forecast_num, None, None),
                  ('METHOD', optimizer, None, None),
                  ('ALGORITHM_TYPE', method, None, None),
                  ('BRUTE_STEP', grid_size, None, None),
                  ('OPTIMIZE_STEP', None, optimize_step, None),
                  ('MEASURE_NAME', None, None, accuracy_measure),
                  ('IGNORE_ZERO', ignore_zero, None, None),
                  ('EXPOST_FLAG', expost_flag, None, None),
                  ('THREAD_RATIO', None, thread_ratio, None)]
    try:
        call_pal_auto(conn,
                      'PAL_ITSF',
                      data_,
                      ParameterTable().with_data(param_rows),
                      *outputs)
    except dbapi.Error as db_err:
        logger.exception(str(db_err))
        try_drop(conn, stats_tbl)
        try_drop(conn, forecast_tbl)
        raise

    return conn.table(forecast_tbl), conn.table(stats_tbl)
