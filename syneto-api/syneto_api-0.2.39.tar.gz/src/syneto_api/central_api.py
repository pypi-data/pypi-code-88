import os
from typing import Any, Optional, List, Dict
from .api_client import APIClientBase


class Central(APIClientBase):
    def __init__(self, url_base=None, **kwargs):
        super().__init__(url_base or os.environ.get("CENTRAL_SERVICE", ""), **kwargs)

    def activate_product(
        self, email: str, password: str, activation_key: Optional[str]
    ) -> Any:
        body: Dict = {
            "email": email,
            "password": password,
            "activation_key": activation_key,
        }
        return self.post_request("/licensing/activate", body=body)

    def sync(self) -> Any:
        return self.post_request("/sync")

    def is_monitoring_purchased(self) -> Any:
        return self.get_request("/monitoring/is-purchased")

    def is_monitoring_enabled(self) -> Any:
        return self.get_request("/monitoring/is-enabled")

    def enable_monitoring(self) -> Any:
        return self.post_request("/monitoring/enable")

    def disable_monitoring(self) -> Any:
        return self.post_request("/monitoring/disable")

    def configure_monitoring(self, exporters: List[Any]) -> Any:
        body: Dict = {
            "exporters": exporters,
        }
        return self.post_request("/monitoring/configure", body=body)

    def get_external_services(self) -> Any:
        return self.get_request("/external-services")

    def get_certificates(self) -> Any:
        return self.get_request("/certificates")