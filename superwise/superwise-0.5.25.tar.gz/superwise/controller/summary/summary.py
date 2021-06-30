import json

import pandas as pd

from .boolean_summary_generator import BooleanSummaryGenerator
from .categorical_summary_generator import CategoricalSummaryGenerator
from .numeric_summary_generator import NumericalSummaryGenerator
from .timestamp_summary_generator import TimestampSummaryGenerator
from .unknown_summary_generator import UnknownSummaryGenerator
from superwise import logger
from superwise.resources.supwewise_enums import FeatureType


class Summary:
    def __init__(self, entities_df, data):
        self.logger = logger
        self._entities_df = entities_df.copy()
        self._data = data.copy()

    def get_summary_generator(self, feature_type):
        return {
            FeatureType.boolean.value: BooleanSummaryGenerator,
            FeatureType.categorical.value: CategoricalSummaryGenerator,
            FeatureType.numeric.value: NumericalSummaryGenerator,
            FeatureType.time_stamp.value: TimestampSummaryGenerator,
            FeatureType.unknown.value: UnknownSummaryGenerator,
        }[feature_type]

    def generate(self):
        def summarize_row(row):
            try:
                # TODO TO DECIDE WHAT TO RETURN
                if row["id"]:
                    print("skip summarizing")
                    return ""
                summary_generator = self.get_summary_generator(row["type"])
                kwargs = dict(entity=self._data[row["name"]])
                return json.loads(
                    pd.Series(summary_generator(**kwargs).generate_summary(row["secondary_type"])).to_json()
                )
            except:
                self.logger.exception(
                    "Failed to generate summary for {}. " f"Setting to null and continuing".format(row["name"]),
                    exc_info=True,
                )
                raise Exception("Exception while summarizing entities row")

        if self._entities_df["summary"].isnull().any():
            logger.debug("Calculating summary based on data")
            self._entities_df["summary"] = self._entities_df.apply(summarize_row, axis=1)
            return self._entities_df
        else:
            self.logger.debug("Using user provided entity summary")
