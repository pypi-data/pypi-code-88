import numpy as np
import pandas as pd


def shifted_hourly_load(df: pd.DataFrame,
                        t: int = 72,
                        cols: str = 'aggregated_per_mp',
                        sort: str = 'trafo') -> pd.DataFrame:
    '''
    Adds a feature to the dataframe containing the T-t previous data where T is current time. 
    Then return dataframe with shifted feature and substation_ID columns.
    For example t=1 adds data from 1 hour back. 

    # Parameters
    --------------
    df: dataframe
    t: Shifting hour
    cols: The column where shifting is based on
    sort: refers to column name that keeps substation IDs

    # Returns
    --------------
    Dataframe with shifted time feature

    '''
    feature_name = 'd_' + str(t)
    df[feature_name] = df.groupby(sort)[cols].shift(periods=t)
    df[feature_name] = df[feature_name].astype(np.float32)
    return df
