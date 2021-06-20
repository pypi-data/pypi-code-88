"""A reversible pipeline with processing steps for synthetic data generation"""
from sklearn.pipeline import Pipeline


class ReversiblePipeline(Pipeline):

    def __init__(self, steps, *, memory=None, verbose=False):
        super().__init__(steps=steps, memory=memory, verbose=verbose)

    def fit(self, X, y=None, **fit_params):
        super().fit(X=X, y=y, **fit_params)


    def reverse_pipeline(self):
        for i in steps

