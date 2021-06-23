import base64
from typing import Dict, List

from requests import Response

from . import utils
from .cfdi import CFDI
from .cfdi.parsers import XML2CFDI, Metadata2CFDI
from .enums import RequestType
from .sat_connector import SATConnector
from .sat_parsers import DownloadParser


class Package:
    identifier: str
    request_type: RequestType

    binary: bytes
    cfdis: List[CFDI]

    request_status: int

    def __init__(self, package_id: str, request_type: RequestType):
        self.identifier = package_id
        self.request_type = request_type

    @classmethod
    def from_ids(cls, package_ids: List[str], request_type: RequestType) -> List["Package"]:
        packages = [cls(package_id, request_type) for package_id in package_ids]
        return packages

    def download(self, connector: SATConnector):
        data = self.soap_download()
        response = connector.download_package(data)
        self._process_download_response(response)

    def soap_download(self) -> Dict[str, str]:
        """Creates the SOAP body to the verify request"""
        data = {
            "package_id": self.identifier,
            "signature": "{signature}",
        }
        return data

    def _process_download_response(self, response: Response):
        self.request_status = response.status_code
        if self.request_status != 200:
            return
        response_clean = utils.remove_namespaces(response.content.decode("UTF-8"))
        parsed = DownloadParser.parse(response_clean)
        if not parsed["Content"]:
            raise ValueError(
                "No content downloaded, this can be caused by already dowload twice the same package"
            )
        self.binary = base64.b64decode(parsed["Content"])
        if self.request_type == RequestType.CFDI:
            self.cfdis = XML2CFDI.from_binary(self.binary)
        elif self.request_type == RequestType.METADATA:
            self.cfdis = Metadata2CFDI.from_binary(self.binary)
        else:
            raise ValueError("Unkown request type")
