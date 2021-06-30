import pandas as pd
import numpy as np

def average_weekly_data(tab_data_set):
    """
    This function takes into Azure dataset of the average weekly data  and 
    returns a pandas dataframe

    tab_data_set: Azure tabular dataset
    """
    data = tab_data_set.to_pandas_dataframe()
    data['houroftheweek_average'] = data['houroftheweek_average'].astype(np.float32)
    
    return data
