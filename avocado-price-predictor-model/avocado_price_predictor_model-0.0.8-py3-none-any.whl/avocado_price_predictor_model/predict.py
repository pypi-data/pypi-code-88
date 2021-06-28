from datetime import datetime
from typing import Any, Tuple
import pandas as pd
from . import model


cols = ['4046', '4225', '4770', 'Small Bags', 'Large Bags',
        'XLarge Bags', 'type', 'region', 'season']
given_cols = ['sold_plu_4046', 'sold_plu_4225', 'sold_plu_4770',
              'small_bags', 'large_bags', 'xlarge_bags', 'organic', 'region', 'date']


def _get_data(avocado: dict, col: str) -> Tuple[bool, Any]:
    valid = True
    given_col = given_cols[cols.index(col)]
    value = avocado[given_col]

    if given_col == 'organic':
        if type(value) != bool:
            valid = False
        else:
            value = 'organic' if value else 'conventional'
    elif given_col == 'date':
        seasons = [3, 3, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3]
        try:
            month = datetime.strptime(value, '%Y-%m-%d').month
            value = seasons[month - 1]
        except ValueError as e:
            valid = False
        
    return valid, value


def _create_avocado_data_frame(avocado: dict) -> pd.DataFrame:
    if list(avocado.keys()) != given_cols:
        return None

    data = [_get_data(avocado, col) for col in cols]
    validations = [x[0] for x in data]
    if not all(validations):
        return None

    data = [x[1] for x in data]
        
    return pd.DataFrame([data], columns=cols)


def predict(avocado: dict) -> float:
    """
    Parameters
    ----------
    avocado : dict
        avocado instance data
    
    Returns
    -------
    float
        if avocado is valid, its predicted price is returned.
        otherwise , 0 is returned.

    Example
    -------
    avocado = {
        'sold_plu_4046': 5,
        'sold_plu_4225': 6,
        'sold_plu_4770': 8,
        'small_bags': 4,
        'large_bags': 0,
        'xlarge_bags': 0,
        'organic': True,
        'region': 'Albany',
        'date': '2020-12-27'
    }
    price = predict(avocado)
    """

    x = _create_avocado_data_frame(avocado)
    y = 0.0
    if x is not None:
        try:
            y = model.predict(x).item()
        except:
            pass

    return round(y, 5)
