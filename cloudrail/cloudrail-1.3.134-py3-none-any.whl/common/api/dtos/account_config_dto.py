import json
from dataclasses import dataclass
from enum import Enum
from typing import Optional

from dataclasses_json import DataClassJsonMixin

from common.api.dtos.cloud_provider_dto import CloudProviderDTO
from common.input_validator import InputValidator


class AccountStatusDTO(str, Enum):
    CONNECTING = 'connecting'
    INITIAL_ENVIRONMENT_MAPPING = 'initial environment mapping'
    READY = 'ready'
    ERROR = 'error'

@dataclass
class CredentialsDTO(DataClassJsonMixin):
    pass


@dataclass
class AwsCredentialsDTO(CredentialsDTO):
    external_id: Optional[str] = None
    role_name: Optional[str] = None


@dataclass
class AzureCredentialsDTO(CredentialsDTO):
    tenant_id: Optional[str] = None
    client_id: Optional[str] = None
    client_secret: Optional[str] = None


@dataclass
class AccountConfigDTO(DataClassJsonMixin):
    name: str
    cloud_account_id: str
    interval_seconds: Optional[int] = None
    credentials: dict = None
    created_at: str = None
    status: AccountStatusDTO = AccountStatusDTO.CONNECTING
    id: str = None
    last_collected_at: str = None
    cloud_provider: CloudProviderDTO = None
    customer_id: str = None
    disable_collect: bool = False
    drift_detection_enabled: bool = True


@dataclass
class AccountConfigAddDTO(DataClassJsonMixin):
    name: str
    cloud_account_id: str
    cloud_provider: CloudProviderDTO = CloudProviderDTO.AMAZON_WEB_SERVICES
    interval_seconds: Optional[int] = None
    credentials: Optional[CredentialsDTO] = None
    disable_collect: bool = False
    drift_detection_enabled: bool = True

    def __post_init__(self):
        InputValidator.validate_allowed_chars(self.name)
        InputValidator.validate_cloud_account_id(self.cloud_account_id, self.cloud_provider)

    @staticmethod
    def convert_from_json(body):
        account_dict = json.loads(body)
        account_config = AccountConfigAddDTO.from_json(body)
        if credentials := account_dict.get('credentials'):
            if account_config.cloud_provider == CloudProviderDTO.AMAZON_WEB_SERVICES:
                account_config.credentials = AwsCredentialsDTO(credentials.get('external_id'),
                                                               credentials.get('role_name'))
            if account_config.cloud_provider == CloudProviderDTO.AZURE:
                account_config.credentials = AzureCredentialsDTO(credentials.get('tenant_id'),
                                                                 credentials.get('client_id'),
                                                                 credentials.get('client_secret'))
        return account_config


@dataclass
class AccountConfigUpdateDTO(DataClassJsonMixin):
    name: Optional[str] = None
    drift_detection_enabled: Optional[bool] = None

    def __post_init__(self):
        InputValidator.validate_allowed_chars(self.name, allow_none=True)
