import json
from .wom_logger import WOMLogger
from .rest_client import RestClient

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey
from cryptography.hazmat.primitives.serialization import load_pem_public_key

class RegistryProxy(object):

    def __init__(self, domain):
        self.client = RestClient(domain)
        self.__logger = WOMLogger("Registry")

        public_key_payload = bytes(self.client.registry_pkey_retrieve(), "utf8")
        self.PublicKey = self.__load_public_key(public_key_payload, "WOM Registry key")

    @staticmethod
    def __load_public_key(public_key_bytes, tag):
        public_key = load_pem_public_key(public_key_bytes, default_backend())
        if not isinstance(public_key, RSAPublicKey):
            raise TypeError("{0} is not a public RSA key" % tag)

        return public_key

    def voucher_create(self, source_id, nonce, payload):
        request_payload = json.dumps({'sourceId': source_id,
                                      'nonce': nonce,
                                      'payload': payload})
        self.__logger.debug(request_payload)

        return self.client.voucher_create(request_payload)

    def voucher_verify(self, payload):
        request_payload = json.dumps({'payload': payload})
        self.__logger.debug(request_payload)

        return self.client.voucher_verify(request_payload)

    def payment_register(self, source_id, nonce, payload):
        request_payload = json.dumps({'posId': source_id,
                                      'nonce': nonce,
                                      'payload': payload})
        self.__logger.debug(request_payload)

        return self.client.payment_register(request_payload)

    def payment_verify(self, payload):
        request_payload = json.dumps({'payload': payload})
        self.__logger.debug(request_payload)

        return self.client.payment_verify(request_payload)
