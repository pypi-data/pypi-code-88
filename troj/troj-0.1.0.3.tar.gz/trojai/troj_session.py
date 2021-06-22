import numpy as np
import json
import torch

"""

"""


class TrojSession:
    def __init__(self):
        super().__init__()
        # thing that makes requests to the troj api
        self.client = None
        # dataframe with the user's testing data

    def create_project(self, project_name: str):
        return self.client.create_project(project_name)

    def create_dataset(self, project_name: str, dataset_name: str):
        return self.client.create_dataset(project_name, dataset_name)

    def upload_dataframe(
        self, dataframe, project_name: str, dataset_name: str, drop_na=True
    ):
        if drop_na == True:
            dataframe = dataframe.dropna()
        # self.dataset.dataframe = self.dataset.dataframe[self.dataset.dataframe["stage"] == "train"]
        jsonified_df = json.loads(dataframe.to_json(orient="index"))

        return self.client.upload_df_results(project_name, dataset_name, jsonified_df)


def CreateClassifierInstance(
    model, input_shape, num_classes, loss_func=None, framework="pt", preprocessing=None, channels_first=True
):
    '''
    :param model:
    :param input_shape:
    :param num_classes:
    :param loss_func:
    :param framework:
    :return:
    '''
    if framework == "pt":
        if loss_func is not None:
            from art.estimators.classification import PyTorchClassifier
            class TrojClassifier(PyTorchClassifier):

                def ComputeLoss(self,x, y, return_preds = True, reduction='none'):
                    old_reduction =  self._loss.reduction
                    self._loss.reduction=reduction
                    preds = torch.tensor(self.predict(x))
                    y = torch.tensor(y)
                    loss_val = self._loss(preds, y)
                    self._loss.reduction = old_reduction
                    if return_preds:
                        return loss_val.numpy(), preds.numpy()
                    else:
                        return loss_val.numpy()
            # ensure model is in eval mode, not sure how to check that rn
            classifier = TrojClassifier(model, loss_func, input_shape, num_classes)
            # classifier = PyTorchClassifier(model, loss_func, input_shape, num_classes, preprocessing=preprocessing, channels_first=channels_first)
        else:
            print("Pass in loss function with pytorch classifier!")

    elif framework == "tf":
        # ensure model is compiled tensorflow
        from art.estimators.classification import KerasClassifier
        import tf.keras.losses
        class TrojClassifier(KerasClassifier):
            def ComputeLoss(self, x, y, return_preds=True, reduction = tf.keras.losses.Reduction.NONE):
                old_reduction = self._loss.reduction
                self._loss.reduction = reduction
                preds = self.predict(x)
                loss_val = self._loss(preds, y)
                self._loss.reduction = old_reduction
                if return_preds:
                    return loss_val.numpy(), preds
                else:
                    return loss_val.numpy()

        if True:
            classifier = TrojClassifier(model)
    return classifier
