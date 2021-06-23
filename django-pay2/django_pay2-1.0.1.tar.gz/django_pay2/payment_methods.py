from dataclasses import dataclass
from typing import Dict


@dataclass
class PaymentRedirect:
    method = "redirect"
    url: str


@dataclass
class PaymentForm:
    method = "form"
    action: str
    fields: Dict[str, str]
