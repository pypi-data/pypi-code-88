from typing import Any, Tuple
import pandas as pd
from .preprocess import preprocess_function


# pandas data frame columns
cols = ['4046', '4225', '4770', 'Small Bags', 'Large Bags',
        'XLarge Bags', 'type', 'region', 'season']
# columns given by client
given_cols = ['sold_plu_4046', 'sold_plu_4225', 'sold_plu_4770',
              'small_bags', 'large_bags', 'xlarge_bags', 'organic', 'region', 'date']


def _preprocess_data(avocado: dict, col: str) -> Tuple[bool, Any]:
    given_col = given_cols[cols.index(col)]
    preprocess = preprocess_function[given_col]

    return preprocess(avocado[given_col])


def create_avocado_data_frame(avocado: dict) -> pd.DataFrame:
    if list(avocado.keys()) != given_cols:
        return None

    data = [_preprocess_data(avocado, col) for col in cols]
    validations = [x[0] for x in data]
    if not all(validations):
        return None

    data = [x[1] for x in data]

    return pd.DataFrame([data], columns=cols)
