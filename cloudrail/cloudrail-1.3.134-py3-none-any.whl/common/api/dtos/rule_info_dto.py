from dataclasses import dataclass
from enum import Enum
from typing import List, Optional

from cloudrail.knowledge.rules.rule_metadata import ResourceType
from dataclasses_json import DataClassJsonMixin

from common.api.dtos.associated_policy_dto import AssociatedPolicyDTO
from common.api.dtos.cloud_provider_dto import CloudProviderDTO
from common.api.dtos.rule_execlusion_dto import RuleExclusionDTO


class RuleSeverityDTO(str, Enum):
    LOW = 'low'
    MEDIUM = 'medium'
    MAJOR = 'major'

class RuleTypeDTO(str, Enum):
    NON_CONTEXT_AWARE = 'non_context_aware'
    CONTEXT_AWARE = 'context_aware'


class SecurityLayerDTO(str, Enum):
    IAM = 'iam'
    ENCRYPTION = 'encryption'
    NETWORKING = 'networking'
    LOGGING = 'logging'
    CODE = 'code'
    DISASTER_RECOVERY = 'disaster_recovery'
    STORAGE = 'storage'
    TAGGING = 'tagging'


ResourceTypeDTO = ResourceType


@dataclass
class RuleInfoDTO(DataClassJsonMixin):
    id: str
    name: str
    description: str
    severity: RuleSeverityDTO
    rule_type: RuleTypeDTO
    cloud_provider: CloudProviderDTO
    security_layer: SecurityLayerDTO
    resource_types: List[ResourceTypeDTO]
    logic: str
    iac_remediation_steps: str
    console_remediation_steps: str
    active: bool
    associated_policies: List[AssociatedPolicyDTO]
    rule_exclusion: RuleExclusionDTO
    source_control_link: Optional[str]


@dataclass
class RuleUpdateDTO(DataClassJsonMixin):
    active: Optional[bool] = None
    rule_exclusion: Optional[RuleExclusionDTO] = None


@dataclass
class RuleBulkUpdateDTO(DataClassJsonMixin):
    id: str
    active: Optional[bool]
