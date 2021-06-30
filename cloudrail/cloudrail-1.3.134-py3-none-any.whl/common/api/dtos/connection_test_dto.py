from dataclasses import dataclass
from typing import Optional

from dataclasses_json import DataClassJsonMixin

from common.api.dtos.cloud_provider_dto import CloudProviderDTO


@dataclass
class ConnectionTestDTO(DataClassJsonMixin):
    connection_test_passed: bool
    account_id: Optional[str] = None


@dataclass
class ConnectivityTestRequestDTO(DataClassJsonMixin):
    cloud_provider: CloudProviderDTO
    cloud_account_id: Optional[str] = None
    tenant_id: Optional[str] = None
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
