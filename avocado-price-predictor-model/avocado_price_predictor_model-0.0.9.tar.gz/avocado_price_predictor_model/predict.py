from . import model
from .load import create_avocado_data_frame


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

    x = create_avocado_data_frame(avocado)
    y = 0.0
    if x is not None:
        try:
            y = model.predict(x).item()
        except:
            pass

    return round(y, 5)
