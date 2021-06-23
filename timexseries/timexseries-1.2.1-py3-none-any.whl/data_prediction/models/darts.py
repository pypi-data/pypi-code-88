# import logging
# import os
#
# from pandas import DataFrame
# from darts.models import Prophet
# from darts.models import TCNModel
# from darts import TimeSeries
#
# from timexseries.data_prediction import PredictionModel
#
#
# class DartsModel(PredictionModel):
#     """Darts prediction model."""
#
#     def __init__(self, params: dict, transformation: str = "none"):
#         super().__init__(params, name="Darts Prophet", transformation=transformation)
#
#         # Stuff needed to make Prophet shut up during training.
#         self.suppress_stdout_stderr = suppress_stdout_stderr
#         self.model = TCNModel(input_chunk_length=13,
# output_chunk_length=12,)
#
#     def train(self, input_data: DataFrame, extra_regressors: DataFrame = None):
#         """Overrides PredictionModel.train()"""
#         series = TimeSeries.from_dataframe(input_data)
#         self.len_train_set = len(input_data)
#         self.model.fit(series)
#
#
#     def predict(self, future_dataframe: DataFrame, extra_regressors: DataFrame = None) -> DataFrame:
#         """Overrides PredictionModel.predict()"""
#         requested_predictions = len(future_dataframe) - self.len_train_set
#         prediction = self.model.predict(requested_predictions)
#         future_dataframe.iloc[-requested_predictions:, 0] = prediction.values().flatten()
#
#         return future_dataframe
#
#
# class suppress_stdout_stderr(object):
#     """
#     A context manager for doing a "deep suppression" of stdout and stderr in
#     Python, i.e. will suppress all print, even if the print originates in a
#     compiled C/Fortran sub-function.
#        This will not suppress raised exceptions, since exceptions are printed
#     to stderr just before a script exits, and after the context manager has
#     exited (at least, I think that is why it lets exceptions through).
#
#     """
#
#     def __init__(self):
#         # Open a pair of null files
#         self.null_fds = [os.open(os.devnull, os.O_RDWR) for x in range(2)]
#         # Save the actual stdout (1) and stderr (2) file descriptors.
#         self.save_fds = [os.dup(1), os.dup(2)]
#
#     def __enter__(self):
#         # Assign the null pointers to stdout and stderr.
#         os.dup2(self.null_fds[0], 1)
#         os.dup2(self.null_fds[1], 2)
#
#     def __exit__(self, *_):
#         # Re-assign the real stdout/stderr back to (1) and (2)
#         os.dup2(self.save_fds[0], 1)
#         os.dup2(self.save_fds[1], 2)
#         # Close the null files
#         for fd in self.null_fds + self.save_fds:
#             os.close(fd)
