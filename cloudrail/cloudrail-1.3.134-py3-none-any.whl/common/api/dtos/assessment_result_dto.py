from dataclasses import dataclass
from enum import Enum
from typing import List

from dataclasses_json import DataClassJsonMixin

from common.api.dtos.associated_account_data_dto import AssociatedAccountDataDTO
from common.api.dtos.associated_policy_dto import AssociatedPolicyDTO
from common.api.dtos.assessment_job_dto import RunOriginDTO
from common.api.dtos.cloud_provider_dto import CloudProviderDTO


class AssessmentResultTypeDTO(str, Enum):
    PASSED = 'passed'
    PASSED_WITH_WARNINGS = 'passed_with_warnings'
    FAILED_DUE_TO_VIOLATIONS = 'failed_due_to_violations'


@dataclass
class ResultsSummaryDTO(DataClassJsonMixin):
    assessment_result_type: AssessmentResultTypeDTO = AssessmentResultTypeDTO.PASSED
    evaluated_rules: int = 0
    passed_rules: int = 0
    failed_rules: int = 0
    skipped_rules: int = 0
    ignored_rules: int = 0


@dataclass
class AssessmentResultDTO(DataClassJsonMixin):
    id: str
    account: AssociatedAccountDataDTO
    created_at: str
    origin: RunOriginDTO
    build_link: str
    execution_source_identifier: str
    results_summary: ResultsSummaryDTO
    associated_policies: List[AssociatedPolicyDTO]
    cloud_provider: CloudProviderDTO
    assessment_name: str
