from abc import ABC, abstractmethod


class BaseModel(ABC):
    """This is an abstract base class which has to be inherited by any custom class
    used to build **models**. 

    Attributes
    ----------
    plot_results: bool, default=True

    Methods
    -------
    fit:
    predict:
    batch_fit:
    metrics:
    """
    def __init__(self, plot_results=False):
        """This is the constructor of the **BaseModel**.

        Parameters
        ----------
        plot_results: bool, default=True
        """
        super(BaseModel, self).__init__()
        self.plot_results = plot_results

    @abstractmethod
    def fit(self):
        """This method is used to *build* a *single* model and should be implemented
        by the subclass.
        """
        pass

    @abstractmethod
    def batch_fit(self, dir_config):
        """This method is used to *build* a *set* of models and should be implemented
        by the subclass.
        
        Parameters
        ----------
        dir_config: string
                    The path to the *config* file where the model configurations should be specified.

        """
        pass

    @abstractmethod
    def predict(self):
        """This method is used to *predict* from the *built* model and should be implemented
        by the subclass.
        """
        pass

    @abstractmethod
    def metrics(self):
        """This method is used to provide various *metrics* for each fitted model and should be implemented
        by the subclass.
        """
        pass

