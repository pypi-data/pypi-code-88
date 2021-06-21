#!/usr/bin/python
# coding:utf-8
import pandas as pd
import numpy as np


def tsmom(start_date, direction=1, **kwargs):
    data = kwargs['data']
    liq_days = kwargs['liq_days']
    data['UCODE'] = data['EXCHANGE'].apply(lambda x: str(x)) + data['PCODE'].apply(lambda x: str(x))
    calendar = data['TDATE'].drop_duplicates().tolist()

    window_days = kwargs['window_days']

    if direction == 1:
        index_name = 'tsmom_d' + str(window_days)
    else:
        index_name = 'tsrev_d' + str(window_days)

    start_index = calendar.index(np.array(calendar)[np.array(calendar) >= start_date][0])

    positions = pd.DataFrame()
    for i in range(start_index, len(calendar) - 1):
        t_date = calendar[i]
        lookback_date = calendar[i - window_days]
        data_t = data[
            np.array(data['TDATE'] == t_date) & np.array(data['VOL'] > kwargs['min_volume'])
            ][['TDATE', 'EXCHANGE', 'PCODE', 'UCODE', 'CLOSE']]

        data_liq = data[
            data['TDATE'] == calendar[i - liq_days]
            ][['UCODE']]

        data_t = pd.merge(data_liq, data_t, on='UCODE', how='inner')

        data_lookback = data[data['TDATE'] == lookback_date][['TDATE', 'UCODE', 'CLOSE']]

        data_t = pd.merge(
            data_t[['EXCHANGE', 'PCODE', 'UCODE', 'CLOSE']],
            data_lookback[['UCODE', 'CLOSE']].rename(columns={'CLOSE': 'CLOSE0'}),
            on='UCODE', how='left'
        )

        data_t['FACTORVALUE'] = data_t['CLOSE'] / data_t['CLOSE0'] - 1
        data_t['POS'] = data_t['FACTORVALUE'] / data_t['FACTORVALUE'].abs() * direction
        data_t['POS'] = data_t['POS'].fillna(0)

        data_tomorrow = data[np.array(data['TDATE'] == calendar[i + 1])]

        data_t = pd.merge(
            data_t, data_tomorrow[['UCODE', 'CLOSE']].rename(columns={'CLOSE': 'CLOSE1'}),
            on='UCODE', how='left'
        )

        data_t['RETURN'] = (data_t['CLOSE1'] / data_t['CLOSE'] - 1)

        data_t['TDATE'] = calendar[i + 1]
        data_t['FACTOR'] = index_name
        if sum(data_t['POS'] != 0) > 0:
            data_t['WEIGHT'] = 1 / sum(data_t['POS'] != 0)
        else:
            data_t['WEIGHT'] = 0
        positions = pd.concat([positions, data_t])
        print(index_name + ', ' + t_date.strftime('%Y-%m-%d') + ', ' + str(sum(data_t['POS'] != 0)))
    if len(positions) == 0:
        return
    positions['WEIGHT'] = positions['WEIGHT'] * 100
    positions['RETURN'] = positions['RETURN'] * 100
    positions['FACTORVALUE'] = positions['FACTORVALUE'] * 100
    return positions.reset_index(drop=True)


def tsrev(start_date, **kwargs):
    return tsmom(start_date=start_date, direction=-1, **kwargs)


def tswr(start_date, price_field='CLOSE', lag=1, **kwargs):
    # 根据前一日仓单数据计算
    # 当日收盘价开平仓
    data = kwargs['data']
    data_wr = kwargs['data_wr']
    liq_days = kwargs['liq_days']
    data['UCODE'] = data['EXCHANGE'].apply(lambda x: str(x)) + data['PCODE'].apply(lambda x: str(x))
    data_wr['UCODE'] = data_wr['EXCHANGE'].apply(lambda x: str(int(x))) + data_wr['PCODE'].apply(lambda x: str(int(x)))

    calendar = data['TDATE'].drop_duplicates().tolist()

    window_days = kwargs['window_days']
    index_name = 'tswr_d' + str(window_days)

    start_index = calendar.index(np.array(calendar)[np.array(calendar) >= start_date][0])

    positions = pd.DataFrame()
    for i in range(start_index, len(calendar) - 1):
        t_date = calendar[i]
        data_wr_0 = data_wr[data_wr['TDATE'] == calendar[i - lag - window_days]][['UCODE', 'PNAME', 'WRQCURRENT']]
        data_wr_t = data_wr[data_wr['TDATE'] == calendar[i - lag]][['UCODE', 'WRQCURRENT']]

        data_wr_range = pd.merge(
            data_wr_0.rename(columns={'WRQCURRENT': 'WR0'}),
            data_wr_t.rename(columns={'WRQCURRENT': 'WR1'}),
            on='UCODE', how='left'
        )
        data_wr_range['FACTORVALUE'] = data_wr_range['WR1'] - data_wr_range['WR0']
        data_wr_range['POS'] = data_wr_range['FACTORVALUE'] / data_wr_range['FACTORVALUE'].abs() * -1
        data_wr_range['POS'] = data_wr_range['POS'].fillna(0)

        data_t = data[
            np.array(data['TDATE'] == t_date)
            & np.array(data['VOL'] > kwargs['min_volume'])
            ][['TDATE', 'EXCHANGE', 'PCODE', 'UCODE', price_field]]

        data_liq = data[
            data['TDATE'] == calendar[i - liq_days]
        ][['UCODE']]

        data_t = pd.merge(data_liq, data_t, on='UCODE', how='inner')

        data_tomorrow = data[
            np.array(data['TDATE'] == calendar[i + 1])
        ][['TDATE', 'EXCHANGE', 'PCODE', 'UCODE', price_field]]

        data_t = pd.merge(data_t[['UCODE', price_field]], data_wr_range, on='UCODE', how='inner')

        data_t = pd.merge(
            data_t.rename(columns={price_field: 'CLOSE'}),
            data_tomorrow.rename(columns={price_field: 'CLOSE1'}),
            on='UCODE', how='left'
        )

        data_t['RETURN'] = (data_t['CLOSE1'] / data_t['CLOSE'] - 1)

        data_t['TDATE'] = calendar[i + 1]
        data_t['FACTOR'] = index_name
        if sum(data_t['POS'] != 0) > 0:
            data_t['WEIGHT'] = 1 / sum(data_t['POS'] != 0)
        else:
            data_t['WEIGHT'] = 0
        positions = pd.concat([positions, data_t])
        print(index_name + ', ' + t_date.strftime('%Y-%m-%d') + ', ' + str(sum(data_t['POS'] != 0)))
    if len(positions) == 0:
        return
    positions['WEIGHT'] = positions['WEIGHT'] * 100
    positions['RETURN'] = positions['RETURN'] * 100
    positions = positions[
        ['TDATE', 'EXCHANGE', 'PCODE', 'UCODE', 'CLOSE', 'CLOSE1', 'POS', 'RETURN', 'FACTORVALUE', 'FACTOR', 'WEIGHT']
    ].reset_index(drop=True)
    return positions


def carry(start_date, **kwargs):
    data = kwargs['data']
    liq_days = kwargs['liq_days']
    data['UCODE'] = data['EXCHANGE'].apply(lambda x: str(x)) + data['PCODE'].apply(lambda x: str(x))
    calendar = data['TDATE'].drop_duplicates().tolist()

    window_days = kwargs['window_days']
    quantile = kwargs['quantile']
    index_name = 'carry_d' + str(window_days) + '_q' + str(quantile)

    start_index = calendar.index(np.array(calendar)[np.array(calendar) >= start_date][0])

    positions = pd.DataFrame()
    for i in range(start_index, len(calendar) - 1):
        t_date = calendar[i]
        lookback_date = calendar[i - window_days]
        data_ry = data[
            np.array(data['TDATE'] <= t_date)
            & np.array(data['TDATE'] > lookback_date)
            ].groupby('UCODE').mean().reset_index()[['UCODE', 'RY']]
        data_t = data[
            np.array(data['TDATE'] == t_date)
            & np.array(data['VOL'] > kwargs['min_volume'])
            ]

        data_liq = data[
            data['TDATE'] == calendar[i - liq_days]
            ][['UCODE']]

        data_t = pd.merge(data_liq, data_t, on='UCODE', how='inner')

        data_t = pd.merge(data_t.rename(columns={'RY': 'RY0'}), data_ry, on='UCODE')
        data_tomorrow = data[
            np.array(data['TDATE'] == calendar[i + 1])
        ]

        quantile_p = data_t['RY'].quantile(quantile / 100)
        quantile_n = data_t['RY'].quantile(1 - quantile / 100)

        data_t['POS'] = data_t['RY'].apply(lambda x: 1 if x > quantile_p else (-1 if x < quantile_n else 0))
        data_t = pd.merge(
            data_t, data_tomorrow[['UCODE', 'CLOSE']].rename(columns={'CLOSE': 'CLOSE1'}), on='UCODE', how='left'
        )
        data_t['RETURN'] = (data_t['CLOSE1'] / data_t['CLOSE'] - 1)
        pos_long = sum(data_t['POS'] == 1)
        pos_short = sum(data_t['POS'] == -1)
        data_t['WEIGHT'] = data_t['POS'].apply(
            lambda x: 0.5 / pos_long if x == 1 else (0.5 / pos_short if x == -1 else 0)
        )
        pos = data_t.rename(columns={'RY': 'FACTORVALUE'})

        pos['TDATE'] = calendar[i + 1]
        pos['FACTOR'] = index_name

        positions = pd.concat([positions, pos])
        print(index_name + ', ' + t_date.strftime('%Y-%m-%d') + ', ' + str(sum(data_t['POS'] != 0)))
    if len(positions) == 0:
        return

    positions['WEIGHT'] = positions['WEIGHT'] * 100
    positions['RETURN'] = positions['RETURN'] * 100
    positions['FACTORVALUE'] = positions['FACTORVALUE'] * 100
    return positions[
        ['TDATE', 'EXCHANGE', 'PCODE', 'UCODE', 'CLOSE', 'CLOSE1', 'POS', 'RETURN', 'FACTORVALUE', 'FACTOR', 'WEIGHT']
    ].reset_index(drop=True)


def xsmom(start_date, direction=1, **kwargs):
    data = kwargs['data']
    liq_days = kwargs['liq_days']
    data['UCODE'] = data['EXCHANGE'].apply(lambda x: str(x)) + data['PCODE'].apply(lambda x: str(x))
    calendar = data['TDATE'].drop_duplicates().tolist()

    window_days = kwargs['window_days']
    quantile = kwargs['quantile']

    if direction == 1:
        index_name = 'xsmom_d' + str(window_days) + '_q' + str(quantile)
    else:
        index_name = 'xsrev_d' + str(window_days) + '_q' + str(quantile)

    start_index = calendar.index(np.array(calendar)[np.array(calendar) >= start_date][0])

    positions = pd.DataFrame()

    for i in range(start_index, len(calendar) - 1):
        t_date = calendar[i]
        lookback_date = calendar[i - window_days]
        data_t = data[
            np.array(data['TDATE'] == t_date) & np.array(data['VOL'] > kwargs['min_volume'])
            ][['TDATE', 'EXCHANGE', 'PCODE', 'UCODE', 'CLOSE']]
        data_lookback = data[data['TDATE'] == lookback_date][['TDATE', 'UCODE', 'CLOSE']]
        data_tomorrow = data[
            np.array(data['TDATE'] == calendar[i + 1])
        ]

        data_liq = data[
            data['TDATE'] == calendar[i - liq_days]
            ][['UCODE']]

        data_t = pd.merge(data_liq, data_t, on='UCODE', how='inner')

        data_t = pd.merge(
            data_t[['EXCHANGE', 'PCODE', 'UCODE', 'CLOSE']],
            data_lookback[['UCODE', 'CLOSE']].rename(columns={'CLOSE': 'CLOSE0'}),
            on='UCODE', how='left'
        )
        data_t['FACTORVALUE'] = data_t['CLOSE'] / data_t['CLOSE0'] - 1

        quantile_p = data_t['FACTORVALUE'].quantile(quantile / 100)
        quantile_n = data_t['FACTORVALUE'].quantile(1 - quantile / 100)

        data_t['POS'] = data_t['FACTORVALUE'].apply(
            lambda x: direction if x > quantile_p else (-direction if x < quantile_n else 0)
        )
        data_t = pd.merge(
            data_t, data_tomorrow[['UCODE', 'CLOSE']].rename(columns={'CLOSE': 'CLOSE1'}), on='UCODE', how='left'
        )
        data_t['RETURN'] = (data_t['CLOSE1'] / data_t['CLOSE'] - 1)
        pos_long = sum(data_t['POS'] == 1)
        pos_short = sum(data_t['POS'] == -1)
        data_t['WEIGHT'] = data_t['POS'].apply(
            lambda x: 0.5 / pos_long if x == 1 else (0.5 / pos_short if x == -1 else 0)
        )
        pos = data_t

        pos['TDATE'] = calendar[i + 1]
        pos['FACTOR'] = index_name
        positions = pd.concat([positions, pos])
        print(index_name + ', ' + t_date.strftime('%Y-%m-%d') + ', ' + str(sum(data_t['POS'] != 0)))
    if len(positions) == 0:
        return
    positions['WEIGHT'] = positions['WEIGHT'] * 100
    positions['RETURN'] = positions['RETURN'] * 100
    positions['FACTORVALUE'] = positions['FACTORVALUE'] * 100
    return positions.reset_index(drop=True)


def xsrev(start_date, **kwargs):
    return xsmom(start_date=start_date, direction=-1, **kwargs)


def xswr(start_date, price_field='CLOSE', lag=1, **kwargs):
    # 根据前一日仓单数据计算
    # 当日收盘价开平仓
    data = kwargs['data']
    data_wr = kwargs['data_wr']
    liq_days = kwargs['liq_days']
    data['UCODE'] = data['EXCHANGE'].apply(lambda x: str(x)) + data['PCODE'].apply(lambda x: str(x))
    data_wr['UCODE'] = data_wr['EXCHANGE'].apply(lambda x: str(int(x))) + data_wr['PCODE'].apply(lambda x: str(int(x)))

    calendar = data['TDATE'].drop_duplicates().tolist()

    window_days = kwargs['window_days']
    quantile = kwargs['quantile']
    index_name = 'xswr_d' + str(window_days) + '_q' + str(quantile)

    start_index = calendar.index(np.array(calendar)[np.array(calendar) >= start_date][0])

    positions = pd.DataFrame()
    for i in range(start_index, len(calendar) - 1):
        t_date = calendar[i]
        data_wr_0 = data_wr[data_wr['TDATE'] == calendar[i - lag - window_days]][['UCODE', 'PNAME', 'WRQCURRENT']]
        data_wr_t = data_wr[data_wr['TDATE'] == calendar[i - lag]][['UCODE', 'WRQCURRENT']]

        data_wr_range = pd.merge(
            data_wr_0.rename(columns={'WRQCURRENT': 'WR0'}),
            data_wr_t.rename(columns={'WRQCURRENT': 'WR1'}),
            on='UCODE', how='left'
        )
        data_wr_range['FACTORVALUE'] = (
            data_wr_range[data_wr_range['WR0'] > 0]['WR1'] / data_wr_range[data_wr_range['WR0'] > 0]['WR0'] - 1
        )

        quantile_p = data_wr_range['FACTORVALUE'].quantile(quantile / 100)
        quantile_n = data_wr_range['FACTORVALUE'].quantile(1 - quantile / 100)
        data_wr_range['POS'] = data_wr_range['FACTORVALUE'].apply(
            lambda x: -1 if x > quantile_p else (1 if x < quantile_n else 0)
        )

        data_wr_range['POS'] = data_wr_range['POS'].fillna(0)

        data_t = data[
            np.array(data['TDATE'] == t_date) & np.array(data['VOL'] > kwargs['min_volume'])
            ][['TDATE', 'EXCHANGE', 'PCODE', 'UCODE', price_field]]

        data_liq = data[
            data['TDATE'] == calendar[i - liq_days]
            ][['UCODE']]

        data_t = pd.merge(data_liq, data_t, on='UCODE', how='inner')

        data_tomorrow = data[
            np.array(data['TDATE'] == calendar[i + 1])
        ][['TDATE', 'EXCHANGE', 'PCODE', 'UCODE', price_field]]

        data_t = pd.merge(data_t[['UCODE', price_field]], data_wr_range, on='UCODE', how='inner')

        data_t = pd.merge(
            data_t.rename(columns={price_field: 'CLOSE'}),
            data_tomorrow.rename(columns={price_field: 'CLOSE1'}),
            on='UCODE', how='left'
        )

        data_t['RETURN'] = (data_t['CLOSE1'] / data_t['CLOSE'] - 1)

        data_t['TDATE'] = calendar[i + 1]
        data_t['FACTOR'] = index_name
        if sum(data_t['POS'] != 0) > 0:
            data_t['WEIGHT'] = 1 / sum(data_t['POS'] != 0)
        else:
            data_t['WEIGHT'] = 0
        positions = pd.concat([positions, data_t])
        print(index_name + ', ' + t_date.strftime('%Y-%m-%d') + ', ' + str(sum(data_t['POS'] != 0)))
    if len(positions) == 0:
        return
    positions['WEIGHT'] = positions['WEIGHT'] * 100
    positions['RETURN'] = positions['RETURN'] * 100
    positions = positions[
        ['TDATE', 'EXCHANGE', 'PCODE', 'UCODE', 'CLOSE', 'CLOSE1', 'POS', 'RETURN', 'FACTORVALUE', 'FACTOR', 'WEIGHT']
    ].reset_index(drop=True)
    return positions


# n日净持仓
# 净头寸区间总和为正做多
def mr(start_date, price_field='CLOSE', lag=1, **kwargs):
    data = kwargs['data']
    data_mr = kwargs['data_mr']
    liq_days = kwargs['liq_days']
    data['UCODE'] = data['EXCHANGE'].apply(lambda x: str(x)) + data['PCODE'].apply(lambda x: str(x))
    data_mr['UCODE'] = data_mr['EXCHANGE'].apply(lambda x: str(x)) + data_mr['PCODE'].apply(lambda x: str(x))
    data_mr['SIDE'] = data_mr['SIDE'].apply(lambda x: 1 if x == 3 else (-1 if x == 4 else 0))

    data_mr['MR'] = data_mr['MR'] * data_mr['SIDE']

    calendar = data['TDATE'].drop_duplicates().tolist()

    window_days = kwargs['window_days']
    index_name = 'mr_d' + str(window_days)

    start_index = calendar.index(np.array(calendar)[np.array(calendar) >= start_date][0])

    positions = pd.DataFrame()
    for i in range(start_index, len(calendar) - 1):
        t_date = calendar[i]

        data_mr_t = data_mr[
            np.array(data_mr['TDATE'] >= calendar[i - lag - window_days])
            & np.array(data_mr['TDATE'] <= calendar[i - lag])
            ].groupby(by=['UCODE']).sum()[['MR']].reset_index()
        data_mr_range = data_mr_t

        data_mr_range['FACTORVALUE'] = data_mr_range['MR']
        data_mr_range['POS'] = data_mr_range['FACTORVALUE'] / data_mr_range['FACTORVALUE'].abs()
        data_mr_range['POS'] = data_mr_range['POS'].fillna(0)

        data_t = data[
            np.array(data['TDATE'] == t_date) & np.array(data['VOL'] > kwargs['min_volume'])
            ][['TDATE', 'EXCHANGE', 'PCODE', 'UCODE', price_field]]

        data_liq = data[
            data['TDATE'] == calendar[i - liq_days]
            ][['UCODE']]

        data_t = pd.merge(data_liq, data_t, on='UCODE', how='inner')

        data_tomorrow = data[
            np.array(data['TDATE'] == calendar[i + 1])
        ][['TDATE', 'EXCHANGE', 'PCODE', 'UCODE', price_field]]

        data_t = pd.merge(data_t[['UCODE', price_field]], data_mr_range, on='UCODE', how='inner')

        data_t = pd.merge(
            data_t.rename(columns={price_field: 'CLOSE'}),
            data_tomorrow.rename(columns={price_field: 'CLOSE1'}),
            on='UCODE', how='left'
        )

        data_t['RETURN'] = (data_t['CLOSE1'] / data_t['CLOSE'] - 1) #* data_t['POS']

        # index_all.append(index_all[-1] * (1 + data_t['RETURN'].mean()))
        data_t['TDATE'] = calendar[i + 1]
        data_t['FACTOR'] = index_name
        if sum(data_t['POS'] != 0) > 0:
            data_t['WEIGHT'] = 1 / sum(data_t['POS'] != 0)
        else:
            data_t['WEIGHT'] = 0
        positions = pd.concat([positions, data_t])
        print(index_name + ', ' + t_date.strftime('%Y-%m-%d') + ', ' + str(sum(data_t['POS'] != 0)))
    if len(positions) == 0:
        return
    positions['WEIGHT'] = positions['WEIGHT'] * 100
    positions['RETURN'] = positions['RETURN'] * 100
    # positions['FACTORVALUE'] = positions['FACTORVALUE'] * 100
    return positions[
        ['TDATE', 'EXCHANGE', 'PCODE', 'UCODE', 'CLOSE', 'CLOSE1', 'POS', 'RETURN', 'FACTORVALUE', 'FACTOR', 'WEIGHT']
    ].reset_index(drop=True)


# n日净持仓变化
# 净头寸时序增加做多
def tsmr(start_date, price_field='CLOSE', lag=1, **kwargs):
    data = kwargs['data']
    data_mr = kwargs['data_mr']
    liq_days = kwargs['liq_days']
    data['UCODE'] = data['EXCHANGE'].apply(lambda x: str(x)) + data['PCODE'].apply(lambda x: str(x))
    data_mr['UCODE'] = data_mr['EXCHANGE'].apply(lambda x: str(x)) + data_mr['PCODE'].apply(lambda x: str(x))
    data_mr['SIDE'] = data_mr['SIDE'].apply(lambda x: 1 if x == 3 else (-1 if x == 4 else 0))

    data_mr['MR'] = data_mr['MR'] * data_mr['SIDE']

    calendar = data['TDATE'].drop_duplicates().tolist()

    window_days = kwargs['window_days']
    index_name = 'tsmr_d' + str(window_days)

    start_index = calendar.index(np.array(calendar)[np.array(calendar) >= start_date][0])

    positions = pd.DataFrame()
    for i in range(start_index, len(calendar) - 1):
        t_date = calendar[i]
        data_mr_0 = data_mr[
            data_mr['TDATE'] == calendar[i - lag - window_days]
        ].groupby(by=['UCODE']).sum()[['MR']].reset_index()
        data_mr_t = data_mr[
            data_mr['TDATE'] == calendar[i - lag]
        ].groupby(by=['UCODE']).sum()[['MR']].reset_index()

        data_mr_range = pd.merge(
            data_mr_0.rename(columns={'MR': 'MR0'}),
            data_mr_t.rename(columns={'MR': 'MR1'}),
            on='UCODE', how='left'
        )
        data_mr_range['FACTORVALUE'] = data_mr_range['MR1'] - data_mr_range['MR0']
        data_mr_range['POS'] = data_mr_range['FACTORVALUE'] / data_mr_range['FACTORVALUE'].abs()
        data_mr_range['POS'] = data_mr_range['POS'].fillna(0)

        data_t = data[
            np.array(data['TDATE'] == t_date) & np.array(data['VOL'] > kwargs['min_volume'])
            ][['TDATE', 'EXCHANGE', 'PCODE', 'UCODE', price_field]]

        data_liq = data[
            data['TDATE'] == calendar[i - liq_days]
            ][['UCODE']]

        data_t = pd.merge(data_liq, data_t, on='UCODE', how='inner')

        data_tomorrow = data[
            np.array(data['TDATE'] == calendar[i + 1])
        ][['TDATE', 'EXCHANGE', 'PCODE', 'UCODE', price_field]]

        data_t = pd.merge(data_t[['UCODE', price_field]], data_mr_range, on='UCODE', how='inner')

        data_t = pd.merge(
            data_t.rename(columns={price_field: 'CLOSE'}),
            data_tomorrow.rename(columns={price_field: 'CLOSE1'}),
            on='UCODE', how='left'
        )

        data_t['RETURN'] = (data_t['CLOSE1'] / data_t['CLOSE'] - 1) #* data_t['POS']

        # index_all.append(index_all[-1] * (1 + data_t['RETURN'].mean()))
        data_t['TDATE'] = calendar[i + 1]
        data_t['FACTOR'] = index_name
        if sum(data_t['POS'] != 0) > 0:
            data_t['WEIGHT'] = 1 / sum(data_t['POS'] != 0)
        else:
            data_t['WEIGHT'] = 0
        positions = pd.concat([positions, data_t])
        print(index_name + ', ' + t_date.strftime('%Y-%m-%d') + ', ' + str(sum(data_t['POS'] != 0)))
    if len(positions) == 0:
        return
    positions['WEIGHT'] = positions['WEIGHT'] * 100
    positions['RETURN'] = positions['RETURN'] * 100
    # positions['FACTORVALUE'] = positions['FACTORVALUE'] * 100
    return positions[
        ['TDATE', 'EXCHANGE', 'PCODE', 'UCODE', 'CLOSE', 'CLOSE1', 'POS', 'RETURN', 'FACTORVALUE', 'FACTOR', 'WEIGHT']
    ].reset_index(drop=True)


# n日净增减
# 净变化为正做多
def mrchg(start_date, price_field='CLOSE', lag=1, **kwargs):
    data = kwargs['data']
    data_mr = kwargs['data_mr']
    liq_days = kwargs['liq_days']
    data['UCODE'] = data['EXCHANGE'].apply(lambda x: str(x)) + data['PCODE'].apply(lambda x: str(x))
    data_mr['UCODE'] = data_mr['EXCHANGE'].apply(lambda x: str(x)) + data_mr['PCODE'].apply(lambda x: str(x))
    data_mr['SIDE'] = data_mr['SIDE'].apply(lambda x: 1 if x == 3 else (-1 if x == 4 else 0))

    data_mr['MRCHG'] = data_mr['MRCHG'] * data_mr['SIDE']

    calendar = data['TDATE'].drop_duplicates().tolist()

    window_days = kwargs['window_days']
    index_name = 'mrchg_d' + str(window_days)

    start_index = calendar.index(np.array(calendar)[np.array(calendar) >= start_date][0])

    positions = pd.DataFrame()
    for i in range(start_index, len(calendar) - 1):
        t_date = calendar[i]
        data_mr_t = data_mr[
            np.array(data_mr['TDATE'] >= calendar[i - lag - window_days])
            & np.array(data_mr['TDATE'] <= calendar[i - lag])
            ].groupby(by=['UCODE']).sum()[['MRCHG']].reset_index()
        data_mr_range = data_mr_t

        data_mr_range['FACTORVALUE'] = data_mr_range['MRCHG']
        data_mr_range['POS'] = data_mr_range['FACTORVALUE'] / data_mr_range['FACTORVALUE'].abs()
        data_mr_range['POS'] = data_mr_range['POS'].fillna(0)

        data_t = data[
            np.array(data['TDATE'] == t_date) & np.array(data['VOL'] > kwargs['min_volume'])
            ][['TDATE', 'EXCHANGE', 'PCODE', 'UCODE', price_field]]

        data_liq = data[
            data['TDATE'] == calendar[i - liq_days]
            ][['UCODE']]

        data_t = pd.merge(data_liq, data_t, on='UCODE', how='inner')

        data_tomorrow = data[
            np.array(data['TDATE'] == calendar[i + 1])
        ][['TDATE', 'EXCHANGE', 'PCODE', 'UCODE', price_field]]

        data_t = pd.merge(data_t[['UCODE', price_field]], data_mr_range, on='UCODE', how='inner')

        data_t = pd.merge(
            data_t.rename(columns={price_field: 'CLOSE'}),
            data_tomorrow.rename(columns={price_field: 'CLOSE1'}),
            on='UCODE', how='left'
        )

        data_t['RETURN'] = (data_t['CLOSE1'] / data_t['CLOSE'] - 1) #* data_t['POS']

        # index_all.append(index_all[-1] * (1 + data_t['RETURN'].mean()))
        data_t['TDATE'] = calendar[i + 1]
        data_t['FACTOR'] = index_name
        if sum(data_t['POS'] != 0) > 0:
            data_t['WEIGHT'] = 1 / sum(data_t['POS'] != 0)
        else:
            data_t['WEIGHT'] = 0
        positions = pd.concat([positions, data_t])
        print(index_name + ', ' + t_date.strftime('%Y-%m-%d') + ', ' + str(sum(data_t['POS'] != 0)))
    if len(positions) == 0:
        return
    positions['WEIGHT'] = positions['WEIGHT'] * 100
    positions['RETURN'] = positions['RETURN'] * 100
    # positions['FACTORVALUE'] = positions['FACTORVALUE'] * 100
    return positions[
        ['TDATE', 'EXCHANGE', 'PCODE', 'UCODE', 'CLOSE', 'CLOSE1', 'POS', 'RETURN', 'FACTORVALUE', 'FACTOR', 'WEIGHT']
    ].reset_index(drop=True)

