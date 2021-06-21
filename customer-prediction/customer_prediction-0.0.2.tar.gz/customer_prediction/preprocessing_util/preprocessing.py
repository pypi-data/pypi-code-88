import pandas as pd
from sklearn.feature_selection import SelectFromModel


def preprocessing(data, id_column, target_column, label_columns):
    from sklearn.preprocessing import LabelEncoder
    if target_column in data.keys():
        Y_train = data[target_column]
        X_train = data.drop(labels=[id_column, target_column], axis=1)
    else:
        Y_train = None
        X_train = data.drop(labels=[id_column], axis=1)
    X_train = X_train.replace({0: 1})
    for col in label_columns:
        X_train[col] = LabelEncoder().fit_transform(X_train[col])
    return X_train, Y_train


# переводит колонку в представление бинами (создает новую колонку)
def convert_column_to_bin_without_borders(data, column, new_column, dividers):
    if len(dividers) == 0:
        raise ValueError('Size can not be zero')

    bins = []
    for i in range(len(data)):
        if data[column][i] <= dividers[0]:
            bins.append(0)
            continue
        for j in range(1, len(dividers)):
            if dividers[j - 1] < data[column][i] <= dividers[j]:
                bins.append(j)
                break
        else:
            if data[column][i] > dividers[len(dividers) - 1]:
                bins.append(len(dividers))
    data[new_column] = bins


# переводит колонку в представление бинами (создает новую колонку)
def convert_column_to_bin_with_right_border(data, column, new_column, dividers):
    if len(dividers) == 0:
        raise ValueError('Size can not be zero')

    bins = []
    for i in range(len(data)):
        if data[column][i] <= dividers[0]:
            bins.append(0)
            continue
        for j in range(1, len(dividers)):
            if dividers[j - 1] < data[column][i] <= dividers[j]:
                bins.append(j)
                break
    data[new_column] = bins


def polynomial_features(X_data):
    from sklearn.preprocessing import PolynomialFeatures
    poly = PolynomialFeatures()
    return pd.DataFrame(poly.fit_transform(X_data))


def min_max_scaler(X_data):
    from sklearn.preprocessing import MinMaxScaler
    min_max_scaler = MinMaxScaler()
    return pd.DataFrame(min_max_scaler.fit_transform(X_data)), min_max_scaler


def selection_features(X_data, Y_data, model):
    select = SelectFromModel(model(n_estimators=100, n_jobs=-1, criterion='entropy'))
    select.fit(X_data, Y_data)
    X_data = select.transform(X_data)
    return X_data, select
