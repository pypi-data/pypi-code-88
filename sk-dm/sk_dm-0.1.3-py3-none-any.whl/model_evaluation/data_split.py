from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import train_test_split
from sklearn import metrics


def kfold_cross_validation(m, n, x, y, model):
    """
    交叉验证法模型

    :param x: {array-like of shape (n_samples, n_features)} 输入数据
    :param y: {str}输入标签
    :param m: {int} 重新洗牌和拆分迭代次数
    :param n: {float, int} 如果是float，应该在0.0到1.0之间，代表比例要包含在测试分组中的组（四舍五入）。
                           如果是整数，表示测试组的所有数量。 如果没有，则值为设置为训练组大小。。
    :param model: {estimator object implementing 'fit' and 'predict'
        The object to use to fit the data} 输入训练模型
    :return: 预测准确率
    """
    cv = ShuffleSplit(n_splits=m, test_size=n, random_state=0)
    predict = cross_val_predict(model, x, y, cv=cv)
    print(metrics.accuracy_score(y, predict))
    return predict


def loo(x, y, n):
    """
    留出法模型

    :param x: {array-like of shape (n_samples)} 输入数据
    :param y: {array-like of shape (n_features)} 输入标签
    :param n: {float or int} 测试集占比
    :return: 分好的训练集测试集
    """
    Xtrain, Xtest, Ytrain, Ytest = train_test_split(x, y, test_size=n, random_state=0)
    return Xtrain, Xtest, Ytrain, Ytest


def bootstrapping(df, n):
    """
    自助法划分数据

    :param df: {array-like of shape (n_samples, n_features)} 输入数据
    :param n: {int or float} 采样的比例
    :return: 划分好的训练集和测试集
    """
    Xtrain = df.sample(frac=n, replace=True)  # 有放回随机采样
    Xtest = df.loc[df.index.difference(Xtrain.index)].copy()
    print(Xtrain)
    print(Xtest)
    return Xtrain, Xtest


