import numpy as np
import pandas as pd


def import_sample_dfs(transactions: int = 7):
    """

    Parameters
    ----------
    transactions: int
        number of transactions to generate.

    Returns
    -------

    """
    df1 = pd.DataFrame({"numbers": [1, 2, 3], "colors": ["red", "white", "blue"]})

    transactions = transactions

    df2 = pd.DataFrame(index=range(transactions))
    df2["amount"] = [np.random.randint(1000, 10000) for x in range(transactions)]
    df2["date"] = [
        (pd.to_datetime("now") - pd.Timedelta(value=x, unit="days")).strftime("%Y-%m-%d")
        for x in range(transactions)
    ]

    dfs = {"Metadata": df1, "Transactions": df2}

    return dfs
