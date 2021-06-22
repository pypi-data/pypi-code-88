import logging
import torch
import torch.nn as nn
from yolo_ens_dist.utilz.torch_utils import do_detect


class Ensemble():
    """
    Ensemble of multiple trained models in one class.
    """
    def __init__(self, device: str='cuda'):
        logging.basicConfig(level=logging.INFO)
        self._log = logging.getLogger(name=self.__class__.__name__)
        self.members = []
        self.device = device


    def __len__(self):
        """
        Returns: Number of models in ensemble
        """
        return len(self.members)

    def add_member(self, new_member: nn.Module):
        """
        Adds a new model to the ensemble. Has to be a pytroch model with the same output
        dimensions as the other models already added if it is not the first one.
        Args:
            member (nn.Module): Model to add
        """
        self._log.info(f'Adding model {len(self.members)} to ensemble.')
        self.members.append(new_member)

    def predict(self, input: torch.Tensor, inference=False) -> torch.Tensor:
        """
        Predict output for each model of ensemble for given input.
        Args:
            input (torch.Tensor): Input for the ensemble to predict

        Returns:
            outputs (list(torch.Tensor)): List of outputs for each model in ensemble
        """
        outputs = []
        for model in self.members:
            model.eval()
            if inference:
                outputs.append(do_detect(model, input, 0.5, 0.5))
            else:
                outputs.append(model(input))
        return outputs

    def get_mean(self, input: torch.Tensor) -> torch.Tensor:
        """
        Get mean prediction for the ensemble.
        Args:
            input (torch.Tensor): Input for the ensemble to predict

        Returns:

        """
        NotImplementedError

    def get_std(self, input: torch.Tensor) -> torch.Tensor:
        """
        Get standard deviation of the predictions from the ensemble.
        Args:
            input (torch.Tensor): Input for the ensemble to predict

        Returns:

        """
        NotImplementedError







