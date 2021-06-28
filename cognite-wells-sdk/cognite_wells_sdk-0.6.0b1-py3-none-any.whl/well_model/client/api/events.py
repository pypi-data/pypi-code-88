import logging
from typing import List, Optional

from requests import Response

from cognite.well_model.client._api_client import APIClient
from cognite.well_model.client.api.api_base import BaseAPI
from cognite.well_model.client.models.resource_list import NPTList
from cognite.well_model.client.utils.multi_request import cursor_multi_request
from cognite.well_model.models import NPT, DoubleRange, LengthRange, NPTFilter, NPTItems

logger = logging.getLogger("WellsAPI")


class EventsAPI(BaseAPI):
    def __init__(self, wells_client: APIClient):
        super().__init__(wells_client)

    def list_npt_events(
        self,
        md: Optional[LengthRange] = None,
        duration: Optional[DoubleRange] = None,
        npt_codes: Optional[List[str]] = None,
        npt_code_details: Optional[List[str]] = None,
        wellbore_ids: Optional[List[int]] = None,
        limit: Optional[int] = 100,
    ) -> NPTList:
        def request(cursor):
            npt_filter = NPTFilter(
                measured_depth=md,
                duration=duration,
                npt_codes=npt_codes,
                npt_code_details=npt_code_details,
                wellbore_ids=wellbore_ids,
            )

            path: str = self._get_path("/events/list")
            response: Response = self.wells_client.post(
                url_path=path, json=npt_filter.json(), params={"cursor": cursor}
            )
            well_items_data: NPTItems = NPTItems.parse_raw(response.text)
            return well_items_data

        items = cursor_multi_request(
            get_cursor=self._get_cursor, get_items=self._get_items, limit=limit, request=request
        )
        return NPTList(items)

    def list_nds_events(self):
        raise NotImplementedError

    def npt_codes(self) -> List[str]:
        """ List valid measurement type values """
        path: str = self._get_path("/events/nptcodes")
        response: Response = self.wells_client.get(url_path=path)
        data: List[str] = response.json()
        return data

    def npt_detail_codes(self) -> List[str]:
        """ List valid measurement type values """
        path: str = self._get_path("/events/nptdetailcodes")
        response: Response = self.wells_client.get(url_path=path)
        data: List[str] = response.json()
        return data

    @staticmethod
    def _get_items(npt_items: NPTItems) -> List[NPT]:
        items: List[NPT] = npt_items.items  # For mypy
        return items

    @staticmethod
    def _get_cursor(npt_items: NPTItems) -> Optional[str]:
        next_cursor: Optional[str] = npt_items.next_cursor  # For mypy
        return next_cursor
