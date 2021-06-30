import xgboost as xgb
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error


def xgboost_reg(xtrain, ytrain, xtest, ytest):
    """
    xgboost回归模型

    :param xtrain: {array-like of shape (n_samples, n_features)} 输入训练数据集
    :param ytrain: {array-like of shape (n_samples, n_output) \
                   or (n_samples,), default=None} 输入测试数据集
    :param xtest: {array-like of shape (n_samples, n_features)} 输入测试数据集
    :param ytest: {array-like of shape (n_samples, n_output)} 输入测试标签
    :return: mae值
    """
    my_imputer = SimpleImputer()
    xtrain = my_imputer.fit_transform(xtrain)
    xtest = my_imputer.transform(xtest)
    my_model = xgb.XGBRegressor(objective='reg:squarederror', verbosity=2)
    my_model.fit(xtrain, ytrain, verbose=False)
    predictions = my_model.predict(xtest)
    mae = mean_absolute_error(predictions, ytest)
    print("Mean Absolute Error: " + str(mae))
    return mae
