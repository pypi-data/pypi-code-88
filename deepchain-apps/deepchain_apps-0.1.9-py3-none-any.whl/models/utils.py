"""
Basic tools to build and evaluate a model
"""
from typing import List, Union

import matplotlib.pyplot as plt
import numpy as np
import torch
from deepchain import log
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score
from torch.utils.data import DataLoader, TensorDataset


def classification_dataloader_from_numpy(
    x: np.ndarray, y: np.array, batch_size: int = 32
) -> DataLoader:
    """Build a dataloader from numpy for classification problem

    This dataloader is use only for classification. It detects automatically the class of
    the problem (binary or multiclass classification)
    Args:
        x (np.ndarray): [description]
        y (np.array): [description]
        batch_size (int, optional): [description]. Defaults to None.

    Returns:
        DataLoader: [description]
    """
    n_class: int = len(np.unique(y))
    if n_class > 2:
        log.info("This is a classification problem with %s classes", n_class)
    else:
        log.info("This is a binary classification problem")

    # y is float for binary classification, int for multiclass
    y_tensor = torch.tensor(y).long() if len(np.unique(y)) > 2 else torch.tensor(y).float()
    tensor_set = TensorDataset(torch.tensor(x).float(), y_tensor)
    loader = DataLoader(tensor_set, batch_size=batch_size)
    return loader


def model_evaluation_accuracy(y_true: np.array, y_hat: np.array):
    """Make prediction for test data
    Work only for bibary classification problem


    Args:
        dataloader: a torch dataloader containing dataset to be evaluated
        model : a callable trained model with a predict method
    """
    acc_score = accuracy_score(y_true, (y_hat > 0.5).astype(int))  # type: ignore
    auc = roc_auc_score(y_true, y_hat)
    print(f" Test :  accuracy score : {acc_score:0.2f} - AUC score : {auc:0.2f}  ")

    return


def confusion_matrix_plot(
    y_true: Union[list, np.array], y_pred: Union[list, np.array], class_: List
):
    """
    Plot a confusion matrix based on
    """
    conf_arr = confusion_matrix(y_true, y_pred)
    norm_conf = []
    for i in conf_arr:
        a = 0
        tmp_arr = []
        a = sum(i, 0)
        for j in i:
            tmp_arr.append(float(j) / float(a))
        norm_conf.append(tmp_arr)

    fig = plt.figure(figsize=(10, 7))
    plt.clf()
    ax = fig.add_subplot(111)
    ax.set_title("Confusion Matrix")

    res = ax.imshow(np.array(norm_conf), cmap=plt.cm.Blues, interpolation="nearest")

    width, height = conf_arr.shape

    for x in range(width):
        for y in range(height):
            ax.annotate(
                str(conf_arr[x][y]),
                xy=(y, x),
                horizontalalignment="center",
                verticalalignment="center",
                size=25,
            )
    _ = fig.colorbar(res)
    alphabet = class_

    plt.xticks(range(width), alphabet[:width])
    plt.yticks(range(height), alphabet[:height])
    plt.savefig("confusion_matrix.png", format="png")
    plt.show()
    return
