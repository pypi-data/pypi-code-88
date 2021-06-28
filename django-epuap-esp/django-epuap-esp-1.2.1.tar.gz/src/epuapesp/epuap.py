import datetime
import logging
import sys
import xmlsec
from django.conf import settings
from zeep import Client
from zeep.xsd import valueobjects

from epuapesp.envelope import EPuapSignature, EPuapPullResponse
from epuapesp.exceptions import EPuapException

logger = logging.getLogger()

class EPuapGeneric:
    """Generic ePUAP service wrapper"""

    wsdl = None

    def __init__(self):
        wsse = EPuapSignature(
            settings.EPUAP_ESP_SYSTEM_KEY,
            settings.EPUAP_ESP_SYSTEM_CERT,
            signing_cert_data=settings.EPUAP_ESP_WS_CERT,
            digest_method=xmlsec.constants.TransformSha256,
            signature_method=xmlsec.constants.TransformRsaSha256,
        )
        self.client = Client(self.wsdl, wsse=wsse)

    def _wrap_service(self, name: str, *args, **kwargs) -> valueobjects.CompoundValue:
        service = getattr(self.client.service, name)
        try:
            res = service(*args, **kwargs)
        except AttributeError as ex:
            raise IOError(f"Failed to get {name}.") from ex
        else:
            status = res.__values__.pop("status", {})
        if status.kod != 1:
            raise EPuapException(status.komunikat, status.kod)
        return res


class EPuapPull(EPuapGeneric):
    """ePUAP Pull interface wrapper"""
    wsdl = "https://ws-int.epuap.gov.pl/pk_external_ws/services/pull?wsdl"

    def count_awaiting_documents(self, subject, box_name, box_address):
        """Get a number of awaiting documents"""

        result = self._wrap_service(
            "oczekujaceDokumenty",
            podmiot=subject,
            nazwaSkrytki=box_name,
            adresSkrytki=box_address,
        )
        return result.oczekujace

    def get_next_document(self, subject, box_name, box_address):
        """Get a next awaiting document"""
        result = self._wrap_service(
            "pobierzNastepny",
            podmiot=subject,
            nazwaSkrytki=box_name,
            adresSkrytki=box_address,
        )
        return EPuapPullResponse(result)

    def acknowledge_receipt(self, subject, box_name, box_address, skrot):
        """Confirm completion of a document processing"""
        result = self._wrap_service(
            "potwierdzOdebranie",
            podmiot=subject,
            nazwaSkrytki=box_name,
            adresSkrytki=box_address,
            skrot=skrot,
        )
        return result


class EPuapDeliver(EPuapGeneric):
    """ePUAP document delivery interface wrapper"""
    wsdl = "https://ws-int.epuap.gov.pl/pk_external_ws/services/doreczyciel?wsdl"

    def deliver(
            self,
            subject,
            box_address,
            response_address,
            document_id,
            case_id,
            xml_document,
    ):
        """Deliver a document to another box"""
        result = self._wrap_service(
            "dorecz",
            adresSkrytki=box_address,
            adresOdpowiedzi=response_address,
            terminDoreczenia=datetime.datetime.now().isoformat(),
            czyProbne=1,
            identyfikatorDokumentu=document_id,
            identyfikatorSprawy=case_id,
            dokument=xml_document,
        )
        return result


class EPuap:
    """Standard entry methods"""

    @classmethod
    def pull(cls):
        service = EPuapPull()
        awaiting_documents = service.count_awaiting_documents(
            settings.EPUAP_ESP_SUBJECT,
            settings.EPUAP_ESP_BOX,
            settings.EPUAP_ESP_ADDRESS,
        )
        if not awaiting_documents:
            return None
        return service.get_next_document(
            settings.EPUAP_ESP_SUBJECT,
            settings.EPUAP_ESP_BOX,
            settings.EPUAP_ESP_ADDRESS,
        )

    @classmethod
    def acknowledge(cls, sha256):
        service = EPuapPull()
        return service.acknowledge_receipt(
            settings.EPUAP_ESP_SUBJECT,
            settings.EPUAP_ESP_BOX,
            settings.EPUAP_ESP_ADDRESS,
            skrot=sha256,
        )

    @classmethod
    def deliver(cls, address, document_xml):
        service = EPuapDeliver()
        return service.deliver(
            settings.EPUAP_ESP_SUBJECT,
            settings.EPUAP_ESP_ADDRESS,
            settings.EPUAP_ESP_ADDRESS,
            0,
            0,
            document_xml,
        )


if __name__ == "__main__":
    response = EPuap.pull()
    print(response.sha256, response.content)
