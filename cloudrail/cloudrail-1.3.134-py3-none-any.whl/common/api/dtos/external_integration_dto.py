from dataclasses import dataclass
from enum import Enum
from typing import Optional, Union

from dataclasses_json import DataClassJsonMixin

# pylint:disable=invalid-name
from common.input_validator import InputValidator


class IntegrationTypeDTO(str, Enum):
    JIRA = 'jira'


@dataclass
class IntegrationSettingsDTO(DataClassJsonMixin):
    pass


@dataclass
class JiraSettingsDTO(IntegrationSettingsDTO):
    project_id: str
    issue_type: str
    default_reporter: str
    url: str

    def __post_init__(self):
        InputValidator.validate_not_empty(self.url)
        InputValidator.validate_allowed_chars(self.project_id)
        InputValidator.validate_not_empty(self.issue_type)
        InputValidator.validate_not_empty(self.default_reporter)


@dataclass
class ExternalIntegrationDTO(DataClassJsonMixin):
    id: str
    integration_type: IntegrationTypeDTO
    settings: Union[JiraSettingsDTO]
    created_at: str
    updated_at: str

    @classmethod
    # pylint:disable=arguments-differ
    def from_dict(cls, data, infer_missing=False):
        result = super().from_dict(data, infer_missing=infer_missing)
        integration_type = IntegrationTypeDTO(data['integration_type'])
        if integration_type == IntegrationTypeDTO.JIRA:
            settings = JiraSettingsDTO.from_dict(data['settings'])
        else:
            raise Exception(f'Unknown integration type {integration_type}')
        result.settings = settings
        return result


@dataclass
class AddUpdateExternalIntegrationDTO(DataClassJsonMixin):
    integration_type: Optional[IntegrationTypeDTO] = None
    settings: Optional[dict] = None
