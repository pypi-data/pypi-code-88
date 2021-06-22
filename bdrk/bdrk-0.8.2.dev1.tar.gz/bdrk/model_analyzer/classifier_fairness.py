import logging
from typing import Dict, List

import numpy as np
import pandas as pd
from aif360.datasets import BinaryLabelDataset
from aif360.metrics.classification_metric import ClassificationMetric

from .fairness import Fairness

logger = logging.getLogger(__name__)


class ClassifierFairness(Fairness):
    def analyze_fairness(self):
        fairness_metrics: Dict[str, Dict] = {}
        labels_cls = set(self.labels.ravel())
        for attr, attr_vals in self.fconfig.items():
            if attr not in self.features:
                logger.warning(f"Key '{attr}' in fairness config does not exist in test features")
            else:
                fairness_metrics[attr] = {}
                for cl in labels_cls:
                    fairness_metrics[attr][f"class {cl}"] = self._get_fairness(
                        Fairness.binarize(self.predictions, cl),
                        Fairness.binarize(self.labels, cl),
                        attr,
                        attr_vals["group_b"],
                        attr_vals["group_a"],
                    )
        return fairness_metrics

    def _prepare_dataset(
        self,
        labels: np.array,
        protected_attribute: str,
        favorable_label=1.0,
        unfavorable_label=0.0,
    ) -> BinaryLabelDataset:
        """Prepare dataset for computing fairness metrics."""
        df = self.features[[protected_attribute]].copy()
        df["outcome"] = labels

        return BinaryLabelDataset(
            df=df,
            label_names=["outcome"],
            scores_names=[],
            protected_attribute_names=[protected_attribute],
            favorable_label=favorable_label,
            unfavorable_label=unfavorable_label,
        )

    def _get_fairness(
        self,
        predictions: np.array,
        labels: np.array,
        protected_attribute: str,
        privileged_attribute_values: List[int],
        unprivileged_attribute_values: List[int],
        favorable_label=1.0,
        unfavorable_label=0.0,
        threshold=0.2,
    ) -> Dict:
        """Fairness wrapper function."""
        available_attributes = set(self.features[protected_attribute].tolist())
        config_attributes = set(privileged_attribute_values + unprivileged_attribute_values)
        invalid_attributes = config_attributes.difference(available_attributes)
        if invalid_attributes:
            raise ValueError(
                f"Attributes {invalid_attributes} do not exist in feature {protected_attribute}"
            )

        predicted = self._prepare_dataset(
            predictions,
            protected_attribute,
            favorable_label=favorable_label,
            unfavorable_label=unfavorable_label,
        )
        grdtruth = self._prepare_dataset(
            labels,
            protected_attribute,
            favorable_label=favorable_label,
            unfavorable_label=unfavorable_label,
        )
        clf_metric = ClassificationMetric(
            grdtruth,
            predicted,
            unprivileged_groups=[{protected_attribute: v} for v in unprivileged_attribute_values],
            privileged_groups=[{protected_attribute: v} for v in privileged_attribute_values],
        )
        fmeasures = self._compute_fairness_metrics(clf_metric)
        fmeasures["fair?"] = fmeasures["ratio"].apply(
            lambda x: "Yes" if np.abs(x - 1) < threshold else "No"
        )

        confusion_matrix = {
            "all": clf_metric.binary_confusion_matrix(privileged=None),
            "privileged": clf_metric.binary_confusion_matrix(privileged=True),
            "unprivileged": clf_metric.binary_confusion_matrix(privileged=False),
        }

        metrics = fmeasures.to_dict()
        metrics["confusion_matrix"] = confusion_matrix
        metrics["confusion_matrix_by_attributes"] = {}
        for v in available_attributes:
            clf_metric = ClassificationMetric(
                grdtruth,
                predicted,
                privileged_groups=[{protected_attribute: v}],
                unprivileged_groups=[],
            )
            metrics["confusion_matrix_by_attributes"][v] = clf_metric.binary_confusion_matrix(
                privileged=True
            )
        return metrics

    @staticmethod
    def _compute_fairness_metrics(aif_metric: ClassificationMetric) -> pd.DataFrame:
        """Compute and report fairness metrics."""
        fmeasures = []

        # Equal opportunity: equal FNR
        fmeasures.append(
            [
                "Equal opportunity (equal FNR)",
                "Separation",
                aif_metric.false_negative_rate(),
                aif_metric.false_negative_rate(False),
                aif_metric.false_negative_rate(True),
                aif_metric.false_negative_rate_ratio(),
            ]
        )

        # Predictive parity: equal PPV
        fmeasures.append(
            [
                "Predictive parity (equal PPV)",
                "Sufficiency",
                aif_metric.positive_predictive_value(),
                aif_metric.positive_predictive_value(False),
                aif_metric.positive_predictive_value(True),
                aif_metric.positive_predictive_value(False)
                / aif_metric.positive_predictive_value(True),
            ]
        )

        # Statistical parity
        fmeasures.append(
            [
                "Statistical parity",
                "Independence",
                aif_metric.selection_rate(),
                aif_metric.selection_rate(False),
                aif_metric.selection_rate(True),
                aif_metric.disparate_impact(),
            ]
        )

        # Predictive equality: equal FPR
        fmeasures.append(
            [
                "Predictive equality (equal FPR)",
                "Separation",
                aif_metric.false_positive_rate(),
                aif_metric.false_positive_rate(False),
                aif_metric.false_positive_rate(True),
                aif_metric.false_positive_rate_ratio(),
            ]
        )

        # Equal TPR
        fmeasures.append(
            [
                "Equal TPR",
                "Separation",
                aif_metric.true_positive_rate(),
                aif_metric.true_positive_rate(False),
                aif_metric.true_positive_rate(True),
                aif_metric.true_positive_rate(False) / aif_metric.true_positive_rate(True),
            ]
        )

        # Equal NPV
        fmeasures.append(
            [
                "Equal NPV",
                "Sufficiency",
                aif_metric.negative_predictive_value(),
                aif_metric.negative_predictive_value(False),
                aif_metric.negative_predictive_value(True),
                aif_metric.negative_predictive_value(False)
                / aif_metric.negative_predictive_value(True),
            ]
        )

        return pd.DataFrame(
            fmeasures,
            columns=["metric", "criterion", "all", "unprivileged", "privileged", "ratio"],
        )
