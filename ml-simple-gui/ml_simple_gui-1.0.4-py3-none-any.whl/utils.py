import pandas as pd
from io import StringIO


def calculate_sensitivity(y_test, y_pred):
    sick_test_cnt = len(y_test[y_test == 1])
    sick_pred_cnt = len(y_pred[y_pred == 1])
    return sick_pred_cnt / (sick_pred_cnt + abs(sick_test_cnt - sick_pred_cnt))


def calculate_specificity(y_test, y_pred):
    healthy_test_cnt = len(y_test[y_test == 0])
    healthy_pred_cnt = len(y_pred[y_pred == 0])
    return healthy_pred_cnt / (healthy_pred_cnt + abs(healthy_test_cnt - healthy_pred_cnt))


def check_model(model):
    fit_method = getattr(model, 'fit', None)
    if not callable(fit_method):
        return False

    predict_method = getattr(model, 'predict', None)
    if not callable(predict_method):
        return False

    return True


def get_data_from_csv(file_path, delimiter):
    try:
        with open(file_path, "r") as f:
            data = pd.read_csv(StringIO(f.read()), delimiter=delimiter)
            f.close()
            return data
    except Exception as error:
        print(error)
        return pd.DataFrame
