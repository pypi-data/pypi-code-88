from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from dataclasses_json import DataClassJsonMixin

from common.api.dtos.assessment_job_dto import RunStatusDTO
from common.api.dtos.datetime_field import datetime_field


@dataclass
class DriftDetectionJobDTO(DataClassJsonMixin):
    id: str
    account_config_id: str
    customer_id: str
    run_status: RunStatusDTO
    assessment_job_id: str
    collect_job_id: str
    created_at: datetime = datetime_field()
    ended_at: datetime = datetime_field()
    drift_count: Optional[int] = None
    iac_coverage: Optional[int] = None
    error_message: Optional[str] = None
    build_link: Optional[str] = None
