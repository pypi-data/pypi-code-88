# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Named entity recognition metrics class."""
import logging
import numpy as np
import scipy
from typing import Dict, List, Tuple

from seqeval.metrics import accuracy_score, f1_score, precision_score, recall_score
from torch import nn
from transformers import EvalPrediction

logger = logging.getLogger(__name__)


class TokenClassificationMetrics:
    """Compute metrics for token classification task"""

    def __init__(self, label_list: List[str]):
        """
        Token classification metrics constructor func.

        :param label_list: unique labels list
        """
        self.label_list = label_list
        self.label_map = {i: label for i, label in enumerate(label_list)}

    def align_predictions(self, predictions: np.ndarray, label_ids: np.ndarray) -> Tuple[List[int], List[int]]:
        """Align the predictions.

        :predictions: array of predictions
        :label_ids: array of label ids
        """
        preds = np.argmax(predictions, axis=2)

        batch_size, seq_len = preds.shape

        out_label_list = [[] for _ in range(batch_size)]
        preds_list = [[] for _ in range(batch_size)]

        for i in range(batch_size):
            for j in range(seq_len):
                if label_ids[i, j] != nn.CrossEntropyLoss().ignore_index:
                    out_label_list[i].append(self.label_map[label_ids[i][j]])
                    preds_list[i].append(self.label_map[preds[i][j]])

        return preds_list, out_label_list

    def align_predictions_with_proba(
            self,
            predictions: np.ndarray,
            label_ids: np.ndarray
    ) -> Tuple[List[int], List[int], List[int]]:
        """Align the predictions.

        :predictions: array of predictions
        :label_ids: array of label ids
        """
        preds = np.argmax(predictions, axis=2)
        probas = scipy.special.softmax(predictions, axis=2)
        pred_probas = np.amax(probas, axis=2)
        batch_size, seq_len = preds.shape

        out_label_list = [[] for _ in range(batch_size)]
        preds_list = [[] for _ in range(batch_size)]
        preds_proba_list = [[] for _ in range(batch_size)]

        for i in range(batch_size):
            for j in range(seq_len):
                if label_ids[i, j] != nn.CrossEntropyLoss().ignore_index:
                    out_label_list[i].append(self.label_map[label_ids[i][j]])
                    preds_list[i].append(self.label_map[preds[i][j]])
                    preds_proba_list[i].append(pred_probas[i][j])

        return preds_list, out_label_list, preds_proba_list

    def compute_metrics(self, p: EvalPrediction) -> Dict:
        """Compute the metrics.

        :p: EvalPrediction that contains the predictions and the label ids
        """
        preds_list, out_label_list = self.align_predictions(p.predictions, p.label_ids)
        return {
            "accuracy": accuracy_score(out_label_list, preds_list),
            "precision": precision_score(out_label_list, preds_list),
            "recall": recall_score(out_label_list, preds_list),
            "f1": f1_score(out_label_list, preds_list),
        }
