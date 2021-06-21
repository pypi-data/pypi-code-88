import mlflow
from livelossplot import PlotLosses

from .utils import flatten_dict


# TODO - add docs and make a base class

class MLFlowWriter(object):
    
    def __init__(self, run_name, params, log_epochs=5):
        self.run_name = run_name
        self.params = flatten_dict(params)
        self.log_epochs = log_epochs
    
    def log_metrics(self, logs, epoch):
        if epoch % self.log_epochs == 0:
            with mlflow.start_run(run_name=self.run_name):
                mlflow.log_param("epoch", epoch)
                mlflow.log_params(self.params)
                mlflow.log_metrics(logs)


class LiveLossWriter(object):
    
    def __init__(self):
        self.liveloss = PlotLosses()
        
    def log_metrics(self, logs, epoch):
        self.liveloss.update(logs)
        self.liveloss.send()


# class ModelWriter(object):
    
#     def __init__(self):
#         self.liveloss = PlotLosses()
        
#     def log_metrics(self, logs, epoch):
#         self.liveloss.update(logs)
#         self.liveloss.send()