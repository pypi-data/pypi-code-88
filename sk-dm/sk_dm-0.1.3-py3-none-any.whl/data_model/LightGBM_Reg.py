import lightgbm as lgb
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error


def lightgbm_reg(xtrain, ytrain, xtest, ytest, m, n, param_grid):
    """
    Lightbgm回归模型

    :param xtrain: {array-like of shape (n_samples, n_features)} 输入训练数据集
    :param ytrain: {array-like of shape (n_samples, n_output) \
                   or (n_samples,), default=None} 输入测试数据集
    :param xtest: {array-like of shape (n_samples, n_features)} 输入测试数据集
    :param ytest: {array-like of shape (n_samples, n_output)} 输入测试标签
    :param m: {int, optional (default=100)} boosting迭代数
    :param n: {int or None, optional (default=None)} 激活提前停止。 该模型将一直训练，直到验证分数停止提高
    :param param_grid: {dict} 参数字典
    :return: mae值
    """
    my_imputer = SimpleImputer()
    xtrain = my_imputer.fit_transform(xtrain)
    xtest = my_imputer.transform(xtest)
    train_data = lgb.Dataset(xtrain, ytrain)
    validation_data = lgb.Dataset(xtest, ytest, reference=train_data)
    gbm = lgb.train(param_grid, train_data, num_boost_round=m, valid_sets=validation_data, early_stopping_rounds=n)
    y_pred = gbm.predict(xtest, num_iteration=gbm.best_iteration)
    mae = mean_absolute_error(y_pred, ytest)
    print("Mean Absolute Error: " + str(mae))
    return mae
