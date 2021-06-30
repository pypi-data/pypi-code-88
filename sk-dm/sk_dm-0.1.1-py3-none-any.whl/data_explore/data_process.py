# -*- coding: UTF-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Binarizer
from imblearn.over_sampling import SMOTE
import seaborn as sns
from scipy import stats
"""
用于数据处理，探索数据的隐含内容

"""
myfont = FontProperties(fname=r'C:\Windows\Fonts\simhei.ttf', size=14)
sns.set(font=myfont.get_name())


def scaler_process(df):
    """
    数据归一化处理

    :param df: array-like of shape (n_samples, n_features)
            用于计算每个特征的最小最大值的数据
            用于稍后沿特征轴缩放.输入数据
    :return: 返回处理后的结果
    """
    scaler = MinMaxScaler()
    result = scaler.fit_transform(df)
    return result


def standardization_process(df):
    """
    数据标准化处理

    :param df: {array-like, sparse matrix} of shape (n_samples, n_features)
            用于计算均值和标准差的数据
            用于稍后沿特征轴缩放.
    :return: 返回处理后的结果
    """
    scaler = StandardScaler()
    result = scaler.fit_transform(df)
    return result


def binarizer_process(df, n):
    """
    数据二值化处理

    :param df: {array-like, sparse matrix} of shape (n_samples, n_features)
            输入数据
    :param n: 阈值，大于n的值设为1，小于n的值设为0
    :return: 返回处理后的结果
    """
    scaler = Binarizer(threshold=n)
    result = scaler.fit_transform(df)
    return result


def under_sample(df, label, m, n):
    """
    数据欠采样处理
    需要有数据标签列label，可以调整采样参数frac的值来控制数据平衡

    :param df: {array-like, sparse matrix} of shape (n_samples, n_features) 输入数据
    :param m: {float} 通过设置m值来调整某个标签数据量
    :param n: {float} 通过设置n值来调整某个标签数据量
    :param label: {str} 标签名
    :return: 返回欠采样后的数据
    """
    X_pos = df[df[label] == 0].sample(frac=m, random_state=50)
    Y_neg = df[df[label] == 1].sample(frac=n, random_state=100)
    df_test = pd.concat([X_pos, Y_neg], axis=0, ignore_index=True)
    return df_test


def over_sample(xtrain, ytrain):
    """
    数据过采样处理

    :param xtrain: {array-like, dataframe, sparse matrix} of shape \
                    (n_samples, n_features)
                    输入训练集样本
    :param ytrain: array-like of shape (n_samples,) 输入标签训练样本
    :return: 返回过采样后的数据
    """
    model_smote = SMOTE(sampling_strategy='minority', random_state=45)
    x_smote_resampled, y_smote_resampled = model_smote.fit_resample(
        xtrain, ytrain)
    x_smote_resampled = pd.DataFrame(x_smote_resampled)
    y_smote_resampled = pd.DataFrame(y_smote_resampled)
    df = pd.concat([x_smote_resampled, y_smote_resampled], axis=1)
    return df


def box_pic(df, n, w, h):
    """
    箱型图

    :param df: {array-like, sparse matrix} of shape (n_samples, n_features) 输入数据
    :param n: {int} 输出n个特征的箱型图
    :param w: {int} 设置画布宽
    :param h: {int} 设置画布高
    """
    column = df.columns.tolist()[:n]
    plt.figure(figsize=(w, h), dpi=75)
    for i in range(n):
        plt.subplot(10, n // 10, i + 1)
        sns.boxplot(df[column[i]], orient='v', width=0.5)
        plt.ylabel(column[i], fontsize=36)
    plt.show()


def data_correlation(df, label, n):
    """
    特征、标签之间热力图

    :param df: {array-like, sparse matrix} of shape (n_samples, n_features) 输入数据
    :param label: {str} 预测标签
    :param n: {float} 设置阈值
    """
    threshold = n
    corrmat = df.corr()
    top_corr_features = corrmat.index[abs(corrmat[label]) > threshold]
    plt.figure(figsize=(20, 10))
    sns.heatmap(df[top_corr_features].corr(), annot=True, cmap='RdYlGn')
    plt.show()


def train_test_distribute(train_path, test_path, m, n):
    """
    显示训练集和测试集样本分布是否一样

    :param train_path: {str} 训练集路径
    :param test_path: {str} 测试集路径
    :param m: {float} 设置显示列数
    :param n: {float} 设置显示画布行列比例
    """
    train_data_file = train_path
    test_data_file = test_path
    train_data = pd.read_csv(train_data_file, encoding="utf-8")
    test_data = pd.read_csv(test_data_file, encoding="utf-8")

    dist_cols = m
    dist_rows = len(test_data.columns)
    plt.figure(figsize=(n * dist_cols, n * dist_rows))
    i = 1
    for col in train_data.columns:
        plt.subplot(dist_rows, dist_cols, i)
        sns.kdeplot(train_data[col], color="Red", shade=True)
        ax = sns.kdeplot(test_data[col], color="Blue", shade=True)
        ax.set_xlabel(col)
        ax.set_ylabel("Frequency")
        ax.legend(["train", "test"])
        i += 1
    plt.show()


def pearson_corr(df, label):
    """
    特征、标签之间相关性

    :param df: {array-like, sparse matrix} of shape (n_samples, n_features) 输入数据
    :param label: {str} 预测标签
    """
    feature_corr = {}
    for f in df:
        df_tmp = df[df[f].notnull()]
        col = df_tmp[f].corr(df_tmp[label], method='pearson')
        feature_corr[f] = col
    print(sorted(feature_corr.items(), key=lambda kv: (-kv[1], kv[0])))


def normal_distribution(filepath, feature):
    """
    用于查看某数据字段是否符合正态分布
    W检验用于从值上查看，输出为(统计数,p值) 与KS检验基本相同，也认为 p值大于0.05时，为正态分布,小于则为非正态性。这里为正态分布
    
    :param filepath: {str} 输入数据路径
    :param feature: {str}要查看的数据字段名称
    """
    data = pd.read_csv(filepath, encoding='utf-8')
    # 画出拥有拟合曲线正态分布直方图
    sns.set_palette("hls")
    sns.distplot(data[feature], bins=130, kde=True, color='blue')
    plt.xlabel(feature)
    plt.ylabel('frequency')
    plt.title(r'Histogram of normal distribution of [feature]')
    plt.show()
    # 使用W检验
    stats.shapiro(data[feature])
