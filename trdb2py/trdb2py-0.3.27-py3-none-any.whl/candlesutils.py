# -*- coding:utf-8 -*-
import trdb2py.trading2_pb2
import numpy as np


def calcCandlesSimilarity(candles0: trdb2py.trading2_pb2.Candles, candles1: trdb2py.trading2_pb2.Candles):
    if len(candles0.candles) != len(candles1.candles):
        raise ValueError

    arr0 = []
    arr1 = []

    for candle in candles0.candles:
        arr0.append(candle.close - candle.open)

    for candle in candles1.candles:
        arr1.append(candle.close - candle.open)

    arr = []
    for i in range(len(arr0)):
        if arr1[i] == arr0[i]:
            arr.append(1.0)
        elif arr0[i] > arr1[i] and arr1[i] >= 0:
            arr.append(arr1[i] / arr0[i])
        elif arr1[i] > arr0[i] and arr0[i] >= 0:
            arr.append(arr0[i] / arr1[i])
        elif arr0[i] > arr1[i] and arr0[i] <= 0:
            arr.append(arr0[i] / arr1[i])
        elif arr1[i] > arr0[i] and arr1[i] <= 0:
            arr.append(arr1[i] / arr0[i])            
        else:
            arr.append(-1.0)

    return np.mean(arr)


def calcCandlesSimilarity_ln(candles0: trdb2py.trading2_pb2.Candles, candles1: trdb2py.trading2_pb2.Candles):
    if len(candles0.candles) != len(candles1.candles):
        raise ValueError

    arr0 = []
    arr1 = []

    for candle in candles0.candles:
        arr0.append(candle.close - candle.open)

    for candle in candles1.candles:
        arr1.append(candle.close - candle.open)

    arr = []
    for i in range(len(arr0)):
        if arr1[i] == arr0[i]:
            arr.append(np.log(1.0+1.0))
        elif arr0[i] > arr1[i] and arr1[i] >= 0:
            arr.append(np.log(1.0+(arr1[i] / arr0[i])))
        elif arr1[i] > arr0[i] and arr0[i] >= 0:
            arr.append(np.log(1.0+(arr0[i] / arr1[i])))
        elif arr0[i] > arr1[i] and arr0[i] <= 0:
            arr.append(np.log(1.0+(arr0[i] / arr1[i])))
        elif arr1[i] > arr0[i] and arr1[i] <= 0:
            arr.append(np.log(1.0+(arr1[i] / arr0[i])))
        else:
            arr.append(0.0)

    return np.mean(arr)    


def calcCandlesSimilarity_LowLevel(candles0: trdb2py.trading2_pb2.Candles, candles1: trdb2py.trading2_pb2.Candles):
    if len(candles0.candles) != len(candles1.candles):
        raise ValueError

    arr0 = []
    arr1 = []

    for candle in candles0.candles:
        if candle.close > candle.open:
            arr0.append(1.0)
        elif candle.close < candle.open:
            arr0.append(-1.0)
        else:
            arr0.append(0.0)

    for candle in candles1.candles:
        if candle.close > candle.open:
            arr1.append(1.0)
        elif candle.close < candle.open:
            arr1.append(-1.0)
        else:
            arr1.append(0.0)

    nums = 0
    for i in range(len(arr0)):
        if (arr0[i] > 0 and arr1[i] >= 0) or (arr0[i] < 0 and arr1[i] <= 0) or (arr1[i] > 0 and arr0[i] >= 0) or (arr1[i] < 0 and arr0[i] <= 0):
            nums = nums + 1

    return nums / len(arr0)


def calcCandlesSimilarity_LowLevel2(candles0: trdb2py.trading2_pb2.Candles, candles1: trdb2py.trading2_pb2.Candles):
    if len(candles0.candles) != len(candles1.candles):
        raise ValueError

    arr0 = []
    arr1 = []
    arrv0 = []
    arrv1 = []

    for candle in candles0.candles:
        arrv0.append(candle.close - candle.open)

        if candle.close > candle.open:
            arr0.append(1.0)
        elif candle.close < candle.open:
            arr0.append(-1.0)
        else:
            arr0.append(0.0)

    for candle in candles1.candles:
        arrv1.append(candle.close - candle.open)        

        if candle.close > candle.open:
            arr1.append(1.0)
        elif candle.close < candle.open:
            arr1.append(-1.0)
        else:
            arr1.append(0.0)

    nums = 0
    cv = 0
    for i in range(len(arr0)):
        if (arr0[i] == 0 and arr1[i] == 0):
            nums += 1

            cv += 1.0
        elif (arr0[i] > 0 and arr1[i] >= 0) or (arr1[i] > 0 and arr0[i] >= 0) and (arr0[i] < 0 and arr1[i] <= 0) or (arr1[i] < 0 and arr0[i] <= 0):
            nums += 1

            if abs(arrv0[i]) < abs(arrv1[i]):
                cv += abs(arrv0[i]) / abs(arrv1[i])
            elif abs(arr0[i]) == 0:
                cv += 0.0
            else:
                cv += abs(arrv1[i]) / abs(arrv0[i])

    return (cv / nums)