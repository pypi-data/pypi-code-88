import logging
from typing import Any, List, Optional, cast

from requests import Response

from cognite.well_model.client._api_client import APIClient
from cognite.well_model.client.api.api_base import BaseAPI
from cognite.well_model.client.models.resource_list import WellboreList
from cognite.well_model.models import Wellbore, WellboreItems, WellboresByIds, WellsByIds

logger = logging.getLogger("WellboresAPI")


class WellboresAPI(BaseAPI):
    def __init__(self, client: APIClient):
        super().__init__(client)

    # guranteed to be non-empty list
    def _retrieve_multiple(self, external_ids: List[str]) -> List[Wellbore]:
        self._validate_external_ids(external_ids)
        wellboress_by_ids = WellboresByIds(items=external_ids)
        path: str = self._get_path("/wellbores/byids")
        response: Response = self.client.post(url_path=path, json=wellboress_by_ids.json())
        return WellboreItems.parse_raw(response.text).items

    # guranteed to be non-empty list
    def _retrieve_multiple_by_wells(self, well_external_ids: List[str]) -> List[Wellbore]:
        self._validate_external_ids(well_external_ids)
        wells_by_ids = WellsByIds(items=well_external_ids)
        path: str = self._get_path("/wellbores/bywellids")
        response: Response = self.client.post(url_path=path, json=wells_by_ids.json())
        return WellboreItems.parse_raw(response.text).items

    def retrieve(self, external_id: str) -> Wellbore:
        """
        Get wellbore by external id

        @param wellbore_id: wellbore external id
        @return: Wellbore object
        """
        return self._retrieve_multiple([external_id])[0]

    def retrieve_multiple(self, external_ids: List[str]) -> WellboreList:
        """
        Get wellbores by a list of external ids

        @param external_ids: list of wellbore external ids
        @return: list of Wellbore objects
        """
        return self._retrieve_multiple(external_ids)

    def retrieve_multiple_by_well(self, well_external_id: str) -> WellboreList:
        """
        Get wellbores by a well external id

        @param well_external_id: well external id
        @return: list of Wellbore objects
        """
        return self._retrieve_multiple_by_wells([well_external_id])

    def retrieve_multiple_by_wells(self, well_external_ids: List[str]) -> WellboreList:
        """
        Get wellbores by a list of well external ids

        @param well_external_ids: list of well external ids
        @return: list of Wellbore objects
        """
        return self._retrieve_multiple_by_wells(well_external_ids)
