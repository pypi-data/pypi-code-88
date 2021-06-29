"""
This script implements the "custom" Azure provisioning method, using
self-generated root and signer certificates.
It is intended to be invoked from iotprovison, but can also be run stand-alone.
"""

from logging import getLogger
from cryptography import x509
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from pykitcommander.firmwareinterface import KitSerialConnection
from pytrustplatform.device_cert_builder import build_device_cert

class AzureCustomProvisioner:
    """Provides "custom" provisioning for Azure"""
    def __init__(self, signer_ca_key_file, signer_ca_cert_file, device_csr_file, device_cert_file,
                 force_new_device_certificate=False):
        """
        :param signer_ca_key_file: Path to file containing signer Certificate Authority private key
        :type signer_ca_key_file: str (path)
        :param signer_ca_cert_file: Path to file containing signer Certificate Authority certificate file
        :type signer_ca_cert_file: str (path)
        :param device_csr_file: Path to the file to write the generated Certificate Signer Request to
        :type device_csr_file: str (path)
        :param device_cert_file: Path to the file to write the generated device certificate to
        :type device_cert_file: str (path)
        :param force_new_device_certificate: Force creation of new device certificate even if it exists already
        :type force_new_device_certificate: Boolean, optional
        """
        self.signer_ca_key_file = signer_ca_key_file
        self.signer_ca_cert_file = signer_ca_cert_file
        self.device_csr_file = device_csr_file
        self.device_cert_file = device_cert_file
        self.force_new_device_certificate = force_new_device_certificate

        self.logger = getLogger(__name__)
        self.crypto_be = default_backend()


    def provision(self, protocol, port):
        """
        Do the actual provisioning.

        This will generate a device certificate, and save it along with the CA signer certificate in WINC flash
        Returns the Device ID (Subject Key Identifier) if successful.
        Generated certificates and Device ID are saved to files as well.
        :param protocol: Firmware protocol driver
        :type protocol: :class:`pykitcommander.firmwareinterface.ApplicationFirmwareInterface` or one of it's
            sub-classes
        :param port: Name of serial port
        :type port: str
        :return: Device ID (Subject Key Identifier) if successful, else None
        :rtype: str
        """
        with KitSerialConnection(protocol, port):
            self.logger.info("Loading signer CA certificate")
            with open(self.signer_ca_cert_file, 'rb') as certfile:
                self.logger.info("    Loading from %s", certfile.name)
                signer_ca_cert = x509.load_pem_x509_certificate(certfile.read(), self.crypto_be)

            self.logger.info("Erase WINC TLS certificate sector")
            protocol.erase_tls_certificate_sector()

            self.logger.info("Generating device certificate")
            device_cert = build_device_cert(self.signer_ca_cert_file,
                                            self.signer_ca_key_file,
                                            protocol,
                                            self.device_csr_file,
                                            self.device_cert_file,
                                            force=self.force_new_device_certificate)

            # Set the Device ID to the subject common name (will be "sn<ECC serial>")
            device_id = device_cert.subject.get_attributes_for_oid(x509.oid.NameOID.COMMON_NAME)[0].value

            self.logger.info("Provisioning device with Azure credentials")
            self.logger.info("Send Signer Certificate")
            protocol.write_signer_certificate(signer_ca_cert.public_bytes(encoding=serialization.Encoding.DER).hex())

            self.logger.info("Send Device Certificate")
            protocol.write_device_certificate(device_cert.public_bytes(encoding=serialization.Encoding.DER).hex())

            self.logger.info("Transfer certificates to WINC")
            protocol.transfer_certificates("2")

            # TODO Store Device ID, connection URL etc

        return device_id
