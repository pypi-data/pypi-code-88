from dataclasses import dataclass, field
from typing import Dict


@dataclass(frozen=True)
class Config:
    email: str
    users_key: str
    delimiter: str
    testing: bool
    debug: bool
    f_it_mode: bool
    profile_info: bool
    buy_one_sell_one_mode: bool
    window_length: int
    window_secs: int
    random_investors: int
    error_sleep_time_sec: int
    storage_bucket: str
    max_order_wait_attempts: int = 50
    dirs: Dict[str, str] = field(default_factory=dict)
    urls: Dict[str, str] = field(default_factory=dict)
