import logging
from typing import Dict, List

import numpy as np
from sklearn import metrics as sk_metrics

from ..utils.histogram import _remove_nans_and_infs, fast_histogram, get_bins
from .fairness import Fairness

logger = logging.getLogger(__name__)

"""
Example Fai config for regression metrics:

CONFIG_FAI = {
    'SEX': {
        'group_a': [1],
        'group_a_name': "Female",
        'group_b': [2],
        'group_b_name': "Male",
    }
}
"""

GROUP_A = "group_a"
GROUP_B = "group_b"
ALL_GROUP = "ALL"


class RegressionFairness(Fairness):
    def analyze_fairness(self):
        fairness_metrics: Dict[str, Dict] = {}
        for attr, attr_vals in self.fconfig.items():
            if attr not in self.features:
                logger.warning(f"Key '{attr}' in fairness config does not exist in test features")
            else:
                fairness_metrics[attr] = self._get_fairness(
                    attr,
                    [GROUP_B, GROUP_A],
                    attr_vals,
                )
        fairness_metrics[ALL_GROUP] = self._calculate_fairness_metrics(
            self.labels, self.predictions
        )
        return fairness_metrics

    def _get_fairness(
        self,
        protected_attribute: str,
        attribute_groups: List[str],
        attribute_values: Dict[str, List[int]],
    ) -> Dict:
        metrics = {}
        # To make sure, same bins are used for calculating histogram of different groups,
        # concatenating errors of all groups together and calculate bins
        combined_errors = np.asarray([])
        combined_inferences = np.asarray([])
        predictions_by_group = {}
        errors_by_group = {}

        for group in attribute_groups:
            labels = self.labels[self.features[protected_attribute].isin(attribute_values[group])]
            predictions = self.predictions[
                self.features[protected_attribute].isin(attribute_values[group])
            ]
            metrics[group] = self._calculate_fairness_metrics(
                labels=labels, predictions=predictions
            )

            # Find the error
            error = predictions - labels

            combined_errors = np.concatenate((combined_errors, error))
            combined_inferences = np.concatenate((combined_inferences, predictions))

            predictions_by_group[group] = predictions
            errors_by_group[group] = error

        # Now calculate bins using errors from all groups
        error_bins = get_bins(_remove_nans_and_infs(combined_errors))
        inference_bins = get_bins(_remove_nans_and_infs(combined_inferences))

        for group in attribute_groups:
            metrics[group]["error"] = list(
                fast_histogram(val=errors_by_group[group], bins=error_bins).items()
            )
            metrics[group]["inference"] = list(
                fast_histogram(val=predictions_by_group[group], bins=inference_bins).items()
            )

        return metrics

    @staticmethod
    def _calculate_fairness_metrics(labels, predictions):
        metrics = dict()
        metrics["MAE"] = sk_metrics.mean_absolute_error(labels, predictions)
        metrics["MSE"] = sk_metrics.mean_squared_error(labels, predictions)
        metrics["RMSE"] = np.sqrt(metrics["MSE"])
        metrics["RSQUARED"] = sk_metrics.r2_score(labels, predictions)
        return metrics
