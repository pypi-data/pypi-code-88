import numpy as np
import pandas as pd


def monthyear(df: pd.DataFrame, substation_id: str = 'trafo') -> pd.DataFrame:
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
    # Create months of of a year as a new feature (for example: 1-Januar, 12-December)
    df['monthyear'] = df.index.month
    df['monthyear'] = df['monthyear'].astype(np.float32)

    return df
