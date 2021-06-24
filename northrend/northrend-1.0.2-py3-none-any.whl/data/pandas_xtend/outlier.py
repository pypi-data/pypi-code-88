import pandas as pd
import numpy as np

from sklearn import preprocessing as sklearn_preprocessing

from .commons import get_shape_diff


class ZscoreOutlierHandler:
    @staticmethod
    def convert_zscore(df: pd.DataFrame, cols: list = None):
        scaled = df.select_dtypes(include="number").astype(np.float64)
        if scaled.shape[1] == 0:
            print("No numeric columns to convert")
            return df
        ss = sklearn_preprocessing.StandardScaler()
        if cols is None:
            return pd.DataFrame(
                ss.fit_transform(scaled), columns=scaled.columns, index=scaled.index
            )
        else:
            scaled.loc[:, cols] = ss.fit_transform(scaled[cols])
            return pd.DataFrame(scaled, columns=scaled.columns, index=scaled.index)

    @staticmethod
    @get_shape_diff()
    def remove_outliers(
        df: pd.DataFrame,
        cols: list = None,
        upper_bound: int = 3,
        return_original_df: bool = False,
    ) -> pd.DataFrame:
        scaled = ZscoreOutlierHandler.convert_zscore(df.copy(), cols)
        if return_original_df:
            res = df.copy()
        else:
            res = scaled
        if cols is None:
            return res.loc[(np.abs(scaled) <= upper_bound).all(axis=1)]
        else:
            return res.loc[(np.abs(scaled[cols]) <= upper_bound).all(axis=1)]
