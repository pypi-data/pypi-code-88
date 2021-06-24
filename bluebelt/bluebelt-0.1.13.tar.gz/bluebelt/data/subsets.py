import pandas as pd
import numpy as np

import bluebelt.core.decorators

@bluebelt.core.decorators.class_methods
class Subset():
    """
    Create a subset based on the pandas.Dataframe column values        
    """
    def __init__(self, frame, inverse=False, **kwargs):

        self.frame = frame
        self.inverse = inverse
        self.kwargs = kwargs
        self.calculate(**kwargs)

    def calculate(self, **kwargs):

        # build filters
        filters={}
        for col in self.kwargs:
            if col in self.frame.columns:
                values = self.kwargs.get(col) if isinstance(self.kwargs.get(col), list) else [self.kwargs.get(col)]
                for value in values:
                    if value not in self.frame[col].values:
                        raise ValueError(f'{value} is not in {col}')
                filters[col]=values
            else:
                raise ValueError(f'{col} is not in frame')

        self.filters = filters

        # filter the frame
        if self.inverse:
            frame=self.frame[self.frame.isin(filters).sum(axis=1) != len(filters.keys())]
        else:
            frame=self.frame[self.frame.isin(filters).sum(axis=1) == len(filters.keys())]
            
        self.result = frame

    def __str__(self):
        return ""
    
    def __repr__(self):
        return (f'{self.__class__.__name__}(frame_length={self.frame.shape[0]:1.0f}, result_length={self.result.shape[0]:1.0f}, filter={self.filters})')
