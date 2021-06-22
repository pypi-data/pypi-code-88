import numpy as np
import pandas as pd


def sin_cos_transformation(df: pd.DataFrame, col: str,
                           max_val: int) -> pd.DataFrame:
    """
    This function takes in dataframe with cyclical features and apply sine and cosine transformations to the features

    # Parameters
    --------------
    df      : Pandas dataframe
    col     : The column name that will be transformed
    max_val : Maximum value in the col feature 

    # Returns
    --------------
    A pandas dataframe with the transformed features
    """
    df[col + '_sin'] = np.sin(2 * np.pi * df[col] /
                              max_val)  # sine transformation
    df[col + '_sin'] = df[col + '_sin'].astype(np.float32)

    df[col + '_cos'] = np.cos(2 * np.pi * df[col] /
                              max_val)  # cosine transformation
    df[col + '_cos'] = df[col + '_cos'].astype(np.float32)

    return df
