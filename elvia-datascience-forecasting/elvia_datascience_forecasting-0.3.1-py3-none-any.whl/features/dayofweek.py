import numpy as np
import pandas as pd


def dayofweek(df: pd.DataFrame, substation_id: str = 'trafo') -> pd.DataFrame:
    """
    This function adds day of week as a feature to the dataframe  and 
    returns just the new feature and substation_id as dataframe

    # Parameters
    --------------
    df: Dataframe with datetime index
    substation_id: refers to column name that keeps substation IDs

    # Returns
    --------------
    Pandas dataframe
    
    """
    dict = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 0}

    # Create day of week as a new feature (for example: 0-sunday, 6-saturday)
    df["dayofweek"] = df.index.dayofweek
    df["dayofweek"] = df["dayofweek"].map(dict)
    df['dayofweek'] = df['dayofweek'].astype(np.float32)

    return df
