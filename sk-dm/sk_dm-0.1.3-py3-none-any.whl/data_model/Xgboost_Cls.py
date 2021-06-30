import xgboost as xgb


def xgboost_cls(xtrain, ytrain, xtest, ytest, n, param_grid):
    """
    xgboost分类模型

    :param xtrain: {array-like of shape (n_samples, n_features)} 输入训练数据集
    :param ytrain: {array-like of shape (n_samples, n_output) \
                   or (n_samples,), default=None} 输入测试数据集
    :param xtest: {array-like of shape (n_samples, n_features)} 输入测试数据集
    :param ytest: {array-like of shape (n_samples, n_output)} 输入测试标签
    :param n: {int} boosting迭代次数
    :param param_grid: {dict} 参数字典
    :return: 模型准确率
    """
    plst = param_grid.items()
    dtrain = xgb.DMatrix(xtrain, ytrain)
    model = xgb.train(plst, dtrain, num_boost_round=n)
    dtest = xgb.DMatrix(xtest)
    ans = model.predict(dtest)
    cnt1 = 0
    cnt2 = 0
    for i in range(len(ytest)):
        if ans[i] == ytest[i]:
            cnt1 += 1
        else:
            cnt2 += 1
    acc = 100 * cnt1 / (cnt1 + cnt2)
    print("Accuracy: %.2f %%" % acc)
    return acc
