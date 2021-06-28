import base64
import hashlib
from lxml import etree
from zeep import Plugin, ns
from zeep.wsse.signature import (
    BinarySignature,
    _make_sign_key,
    _signature_prepare,
    _make_verify_key,
    _verify_envelope_with_key,
    _read_file,
)
from zeep.wsse.utils import ensure_id

from epuapesp.exceptions import EPuapWrongSignatureException


class EPuapSignature(BinarySignature):
    """BinarySignature replacement for ePUAP communication.
    It changes the order of signature related XML enries for ePUAP compliance
    and uses separate certificates to verify communication channel and envelope
    integrity.
    """

    def __init__(self, *args, signing_cert_data=None, **kwargs):
        super().__init__(*args, **kwargs)
        if signing_cert_data:
            self.signing_cert_data = _read_file(signing_cert_data)
        else:
            self.signing_cert_data = self.cert_data

    def apply(self, envelope, headers):
        key = _make_sign_key(self.key_data, self.cert_data, self.password)
        self._sign_envelope_with_key_epuap(envelope, key)
        return envelope, headers

    def verify(self, envelope):
        key = _make_verify_key(self.signing_cert_data or self.cert_data)
        try:
            _verify_envelope_with_key(envelope, key)
        except:
            raise EPuapWrongSignatureException(envelope)
        return envelope

    def _sign_envelope_with_key_epuap(self, envelope, key):
        security, sec_token_ref, x509_data = _signature_prepare(
            envelope, key, self.signature_method, self.digest_method
        )
        ref = etree.SubElement(
            sec_token_ref,
            etree.QName(ns.WSSE, "Reference"),
            {
                "ValueType": "http://docs.oasis-open.org/wss/2004/01/"
                "oasis-200401-wss-x509-token-profile-1.0#X509v3"
            },
        )
        bintok = etree.Element(
            etree.QName(ns.WSSE, "BinarySecurityToken"),
            {
                "ValueType": "http://docs.oasis-open.org/wss/2004/01/"
                "oasis-200401-wss-x509-token-profile-1.0#X509v3",
                "EncodingType": "http://docs.oasis-open.org/wss/2004/01/"
                "oasis-200401-wss-soap-message-security-1.0#Base64Binary",
            },
        )
        ref.attrib["URI"] = "#" + ensure_id(bintok)
        print(bintok, x509_data)
        with open("x509_data.xml", "wb") as f:
            x509_data.getroottree().write(f, pretty_print=True)
        bintok.text = x509_data.find(etree.QName(ns.DS, "X509Certificate")).text
        security.insert(0, bintok)
        x509_data.getparent().remove(x509_data)


class EPuapParser:
    """Generic class for ePUAP documents parsing."""

    __xml_parser = etree.XMLParser(remove_blank_text=True)

    def __init__(self, root):
        self.root = root

    def _iter_element(self, element: etree._Element) -> dict:
        result = {
            etree.QName(child).localname: self._iter_element(child)
            for child in element.getchildren()
            if child.tag != "{http://www.w3.org/2000/09/xmldsig#}Signature"
        }
        result.update(element.attrib)
        if element.text:
            if result:
                result["_text"] = element.text
            else:
                result = element.text
        return result

    def _parse_xml_element(self, xml_element: str) -> dict:
        """Parse given XML and return simple dictionary of items:
        tag: text and attribute: value
        """

        return self._iter_element(etree.fromstring(xml_element, self.__xml_parser))

    def __getattr__(self, key: str) -> any:
        """Redirect to root"""
        return getattr(self.root, key)


class EPuapPullResponse(EPuapParser):
    """Parser for OdpowiedzPull interface"""

    @property
    def content(self):
        """Return result XML"""
        return self._parse_xml_element(self.dokument.zawartosc)

    @property
    def sha256(self):
        """Return result's hash"""
        return base64.b64encode(
            hashlib.sha256(self.dokument.zawartosc).digest()
        ).decode()
