from sklearn.metrics import roc_curve, auc, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
import pandas as pd


def model_ensemble(X_data, Y_data, model, **kwargs):
    x_train, x_val, y_train, y_val = train_test_split(X_data, Y_data, random_state=57, train_size=0.8)
    forest = model(**kwargs)
    forest.fit(x_train, y_train)
    y_pred = forest.predict(x_val)
    fpr, tpr, thresholds = roc_curve(y_val, y_pred, pos_label=None)
    print(f'Roc-curve: {auc(fpr, tpr)}')
    print(f'Report: \n {classification_report(y_val, y_pred)}')
    print(f'Confusion matrix: {confusion_matrix(y_val, y_pred)}')
    return forest

def model_ensemble_dict_params(X_data, Y_data, model, params):
    x_train, x_val, y_train, y_val = train_test_split(X_data, Y_data, random_state=57, train_size=0.8)
    forest = model(**params)
    forest.fit(x_train, y_train)
    y_pred = forest.predict(x_val)
    fpr, tpr, thresholds = roc_curve(y_val, y_pred, pos_label=None)
    print(f'Roc-curve: {auc(fpr, tpr)}')
    print(f'Report: \n {classification_report(y_val, y_pred)}')
    print(f'Confusion matrix: {confusion_matrix(y_val, y_pred)}')
    return forest


def choice_best(X_data, Y_data, model, **kwargs):
    sel = SelectFromModel(model(**kwargs))
    sel.fit(X_data, Y_data)
    X_data_drop = sel.transform(X_data)
    model = model_ensemble(X_data_drop, Y_data, model, **kwargs)
    return model


# Выбор "важных" фич
def features_selection(X_train, Y_train):
    print('RandomForestClassifier')
    choice_best(X_train, Y_train, RandomForestClassifier, n_jobs=-1, verbose=1)
    print('GradientBoostingClassifier')
    choice_best(X_train, Y_train, GradientBoostingClassifier, verbose=0)


# Извлечение фич с помощью полинома n-ой степени
def feature_extraction(X_train, Y_train):
    from sklearn.preprocessing import PolynomialFeatures
    poly = PolynomialFeatures()
    X_poly = pd.DataFrame(poly.fit_transform(X_train))
    print('RandomForestClassifier')
    model_ensemble(X_poly, Y_train, RandomForestClassifier, n_jobs=-1, verbose=1)
    print('GradientBoostingClassifier')
    model_ensemble(X_poly, Y_train, GradientBoostingClassifier, verbose=0)


# Выбор нормализатора
def choice_scaler(X_train, Y_train):
    from sklearn.preprocessing import MinMaxScaler, StandardScaler
    min_max_scaler = MinMaxScaler()
    std_scaler = StandardScaler()
    x_train_min_max = pd.DataFrame(min_max_scaler.fit_transform(X_train))
    x_train_std = pd.DataFrame(std_scaler.fit_transform(X_train))
    print('MinMax scaler')
    print('RandomForestClassifier')
    model_ensemble(x_train_min_max, Y_train, RandomForestClassifier, n_jobs=-1, verbose=1)
    print('GradientBoostingClassifier')
    model_ensemble(x_train_min_max, Y_train, GradientBoostingClassifier, verbose=0)
    print('Standard scaler')
    print('RandomForestClassifier')
    model_ensemble(x_train_std, Y_train, RandomForestClassifier, n_jobs=-1, verbose=1)
    print('GradientBoostingClassifier')
    model_ensemble(x_train_std, Y_train, GradientBoostingClassifier, verbose=0)
