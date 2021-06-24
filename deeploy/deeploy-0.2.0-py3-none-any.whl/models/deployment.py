from typing import Optional, List, Any

from pydantic import BaseModel

from deeploy.common.functions import to_lower_camel


class Deployment(BaseModel):
    name: str
    versions: Optional[List[Any]]
    workspace_id: str
    description: Optional[str]
    example_input: Optional[List[Any]]
    example_output: Optional[List[Any]]
    status: int
    owner_id: str
    kf_serving_id: Optional[str]
    public_url: Optional[str]
    id: str
    created_at: str
    updated_at: str

    class Config:
        alias_generator = to_lower_camel


class DeployOptions(BaseModel):
    """
    Class that contains the options for deploying a model

    Attributes:
      name: name of the deployment
      model_serverless: boolean indicating whether to deploy the model in
        a serverless fashion. Defaults to False
      explainer_serverless: boolean indicating whether to deploy the model in
        a serverless fashion. Defaults to False
      description: string with the description of the deployment
      example_input: list of example input parameters for the model
      example_output: list of example output for the model
    """
    name: str
    model_serverless = False
    explainer_serverless = False
    description: Optional[str]
    example_input: Optional[List[Any]]
    example_output: Optional[List[Any]]
