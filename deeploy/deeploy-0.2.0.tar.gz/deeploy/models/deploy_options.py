from typing import Optional, List, Any

from pydantic import BaseModel


class DeployOptions(BaseModel):
    """Class that contains the options for deploying a model

    Attributes:
        name (str): name of the deployment
        model_serverless (bool, optional): whether to deploy the model in 
            a serverless fashion. Defaults to False
        explainer_serverless (bool, optional): whether to deploy the model in 
            a serverless fashion. Defaults to False
        description (str, optional): the description of the deployment
        example_input (List, optional): list of example input parameters for the model
        example_output (List, optional): list of example output for the model
        feature_labels (List, optional): list of feature labels for the explanations
        pytorch_model_file_path (str, optional): absolute or relative path to the .py file 
            containing the pytorch model class definition
        pytorch_torchserve_handler_name (str, optional): TorchServe handler name. One of 
            ['image_classifier', 'image_classifier', 'object_detector', 'text_classifier']. 
            See the (TorchServe documentation)[https://github.com/pytorch/serve/blob/master/docs/default_handlers.md#torchserve-default-inference-handlers]
            for more info.
    """ # noqa
    name: str
    model_serverless = False
    explainer_serverless = False
    description: Optional[str]
    example_input: Optional[List[Any]]
    example_output: Optional[List[Any]]
    feature_labels: Optional[List[str]]
    pytorch_model_file_path: Optional[str]
    pytorch_torchserve_handler_name: Optional[str]
