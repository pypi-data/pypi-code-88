from typing import List
import pandas as pd

BASE_URL = "https://www.leveropen.com/api/"
VERSION = "v1"
DATE_FORMAT = "%Y-%m-%d"
DATASET_FILTER_TYPES = ["name", "collection", "topic"]


def parse_categories(categories: List[dict]):
    return pd.concat(
        [
            pd.DataFrame(data=category, index=[idx])
            for idx, category in enumerate(categories)
        ]
    )
