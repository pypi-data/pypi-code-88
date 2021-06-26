from typing import Any

from us_libraries.client.base_client import BaseClient
from us_libraries.graphite import client_timing

service_name = "usf-account-service"


class DriverClient(BaseClient):
    def __init__(self) -> None:
        super().__init__(service_name)

    @client_timing
    def add_driver(self,
                   first_name: str = None,
                   last_name: str = None,
                   id_type: str = None,
                   id_number: str = None,
                   gender: str = None,
                   email: str = None,
                   phone: str = None,
                   date_of_birth: str = None,
                   license_number: str = None
                   ) -> Any:
        return self.post('driver',
                         first_name=first_name,
                         last_name=last_name,
                         id_type=id_type,
                         id_number=id_number,
                         gender=gender,
                         email=email,
                         phone=phone,
                         date_of_birth=date_of_birth,
                         license_number=license_number)

    @client_timing
    def get_driver(self, driver_id: int) -> Any:
        return self.get(f'driver/{driver_id}')
