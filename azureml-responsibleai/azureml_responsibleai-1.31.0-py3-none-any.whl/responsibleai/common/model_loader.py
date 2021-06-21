# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Model loader used to load AzureML models into memory."""
from abc import ABC, abstractmethod
import tempfile

from azureml._base_sdk_common._docstring_wrapper import experimental
from azureml.core import Model, Workspace


@experimental
class ModelLoader(ABC):
    """Model loader used to load AzureML models into memory."""

    @abstractmethod
    def load(self, dirpath):
        """
        Load the model from the specified directory.

        :param dirpath: Directory into which the AzureML model has been downloaded.
        :return: Python model with fit and predict methods.
        """
        raise NotImplementedError

    def load_by_model_id(self,
                         workspace: Workspace,
                         model_id: str) -> object:
        """
        Load the specified model.

        :param workspace: Workspace containing the model
        :param model_id: Identifies the model to load
        """
        model = Model(workspace=workspace, id=model_id)

        download_dir = tempfile.mkdtemp()
        model.download(target_dir=download_dir)
        return self.load(download_dir)
