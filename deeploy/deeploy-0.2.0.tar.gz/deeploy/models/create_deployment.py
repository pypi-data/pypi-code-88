from typing import Optional, List, Any

from pydantic import BaseModel

from deeploy.enums import ModelType, ExplainerType


class CreateDeployment(BaseModel):
    """
    """
    repository_id: str
    name: str
    description: Optional[str]
    example_input: Optional[List[Any]]
    example_output: Optional[Any]
    model_type: ModelType
    model_serverless: Optional[bool] = False
    explainer_type: ExplainerType
    explainer_serverless: Optional[bool] = False
    branch_name: str
    commit: str

    def to_request_body(self):
        return {
            'repositoryId': self.repository_id,
            'name': self.name,
            'description': self.description,
            'exampleInput': self.example_input,
            'exampleOutput': self.example_output,
            'modelType': self.model_type.value,
            'modelServerless': self.model_serverless,
            'explainerType': self.explainer_type.value,
            'explainerServerless': self.explainer_serverless,
            'branchName': self.branch_name,
            'commit': self.commit,
        }
