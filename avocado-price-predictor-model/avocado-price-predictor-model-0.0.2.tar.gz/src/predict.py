from datetime import datetime
import pandas as pd
from . import model


cols = ['4046', '4225', '4770', 'Small Bags', 'Large Bags',
        'XLarge Bags', 'type', 'region', 'season']
given_cols = ['sold_plu_4046', 'sold_plu_4225', 'sold_plu_4770',
              'small_bags', 'large_bags', 'xlarge_bags', 'organic', 'region', 'date']


def _create_avocado_data_frame(avocado: dict) -> pd.DataFrame:
    if avocado.keys() != given_cols:
        return None

    invalid = False
    def get_data(col: str):
        given_col = given_cols[cols.index(col)]
        data = avocado[given_col]

        if given_col == 'organic':
            if type(data) != bool:
                invalid = True
            else:
                data = 'organic' if data else 'conventional'
        elif given_col == 'date':
            seasons = [3, 3, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3]
            try:
                month = datetime.strptime(data, '%Y-%m-%d').month
                data = seasons[month - 1]
            except ValueError as e:
                invalid = True
            
        return data

    data = list(map(get_data, cols))
    if invalid:
        return None
        
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
    if x:
        y = model.predict(x).item()

    return round(y, 5)
