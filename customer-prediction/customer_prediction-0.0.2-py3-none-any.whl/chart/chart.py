import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc


# рисование гистограмм для все категориальных фич
def plot_hist_categorical_features(data):
    for feature in data.select_dtypes(include=['object']).columns:
        sns.countplot(feature, data=data)
        plt.title(f'Histogram of {feature}')
        plt.xticks(rotation=70)
        plt.xlabel('Bins')
        plt.ylabel('Count')
        plt.show()


# рисование гистограммы
def plot_histogram(df_column, title):
    sns.countplot(df_column)
    plt.title(title)
    plt.show()


def plot_countplot(df_column):
    sns.countplot(df_column)
    plt.xticks(rotation=70)
    plt.show()


def plot_violinplot(df, x, y):
    sns.catplot(x=x, y=y, data=df, size=6, kind='violin')
    plt.title('Violin plot')
    plt.show()


def plot_kdeplot(df, x_1, x_2, y, label_1, label_2, title, xlabel, bw="scott"):
    sns.kdeplot(df[x_1][y], label=label_1, shade=True)
    sns.kdeplot(df[x_2][y], label=label_2, shade=True, bw=bw)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.show()


def plot_roc_curve(y_test, y_pred):
    fpr, tpr, thresholds = roc_curve(y_test, y_pred, pos_label=None)
    plt.figure(figsize=(10, 10))
    plt.plot(fpr, tpr, label='ROC curve (area = %0.3f)' % auc(fpr, tpr))
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic')
    plt.legend(loc="upper left")
    plt.show()
