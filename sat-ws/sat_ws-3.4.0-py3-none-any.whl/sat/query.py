import logging
import time
from datetime import datetime, timedelta
from typing import Dict, List

from requests import Response

from . import exceptions, utils
from .enums import DownloadType, RequestType
from .package import Package
from .sat_connector import SATConnector
from .sat_parsers import QueryParser, VerifyParser

_logger = logging.getLogger(__name__)
DEFAULT_TIME_WINDOW = timedelta(days=30)


class Query:
    download_type: DownloadType
    request_type: RequestType
    start: datetime
    end: datetime

    identifier: str
    status: int

    request_status: int

    query_status: int
    message: str
    status_code: int
    cfdi_qty: int
    packages: List[Package]

    def __init__(
        self,
        download_type: DownloadType,
        request_type: RequestType,
        start: datetime = None,
        end: datetime = None,
    ):
        self.download_type = download_type
        self.request_type = request_type
        self.start = start or datetime.utcnow()
        self.end = end or self.start + DEFAULT_TIME_WINDOW

    def send(self, connector: SATConnector):
        data = self.soap_send()
        response = connector.send_query(data)
        self._process_send_response(response)

    def soap_send(self) -> Dict[str, str]:
        """Creates the SOAP body to the send request"""
        start = self.start.isoformat()
        end = self.end.isoformat()
        data = {
            "start": start,
            "end": end,
            "download_type": self.download_type.value,
            "request_type": self.request_type.value,
            "signature": "{signature}",
        }
        return data

    def _process_send_response(self, response: Response):
        self.request_status = response.status_code
        if self.request_status != 200:
            return
        response_clean = utils.remove_namespaces(response.content.decode("UTF-8"))
        parsed = QueryParser.parse(response_clean)
        self.status = int(parsed["CodEstatus"])

        self.identifier = parsed["IdSolicitud"]

    def verify(self, connector: SATConnector):
        data = self.soap_verify()
        response = connector.verify_query(data)
        self._process_verify_response(response)

    def soap_verify(self) -> Dict[str, str]:
        """Creates the SOAP body to the verify request"""
        data = {
            "identifier": self.identifier,
            "signature": "{signature}",
        }
        return data

    def _process_verify_response(self, response: Response):
        self.request_status = response.status_code
        if self.request_status != 200:
            return
        response_clean = utils.remove_namespaces(response.content.decode("UTF-8"))
        try:
            parsed = VerifyParser.parse(response_clean)
        except KeyError as e:
            _logger.error("Missing key %s in query ID %s", e, self.identifier)
            raise
        self.status = int(parsed["CodEstatus"])

        self.query_status = int(parsed["EstadoSolicitud"])
        self.message = parsed["Mensaje"]
        self.status_code = int(parsed["CodigoEstadoSolicitud"])
        self.cfdi_qty = int(parsed["NumeroCFDIs"])
        self.packages = Package.from_ids(parsed["IdsPaquetes"], self.request_type)

    def download(self, connector: SATConnector):
        for package in self.packages:
            package.download(connector)

    def get_packages(self, connector: SATConnector, retries: int = 10, wait_seconds: int = 2):
        for _ in range(retries):
            self.verify(connector)
            if self.query_status > 3:
                raise exceptions.QueryException(f"EstadoSolicitud({self.status_code})")
            if self.query_status == 3:
                return self.packages
            time.sleep(wait_seconds)
        raise TimeoutError("The query is not yet resolved")
