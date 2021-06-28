"""
Certificate builder for ATECC608 certificates

This module supports building certificates from templates and data fetched from ECC compressed certificates
"""
import os.path
from logging import getLogger
import binascii
import asn1crypto.x509
import asn1crypto.pem
from asn1crypto.core import GeneralizedTime, UTCTime, OctetString
from asn1crypto.algos import DSASignature
from asn1crypto.keys import ECPointBitString
from asn1crypto.x509 import Name, GeneralName, GeneralNames, Extension, AuthorityKeyIdentifier
import cryptography.x509
from cryptography.hazmat.backends import default_backend

from .compressed_cert_decoder import CompressedCertificateData
from .compressed_cert_decoder import DeviceCertificateRepresentation
from .compressed_cert_decoder import SignerCertificateRepresentation
from .pytrust_errors import PytrustError

MAH1H_DEVICE_CERT_TEMPLATE_FILE = "certs/ATECC608A-MAH1H/device.crt"
MAH1H_SIGNER_CERT_TEMPLATE_FILE = "certs/ATECC608A-MAH1H/signer_218B.crt"
MAH4I_DEVICE_CERT_TEMPLATE_FILE = "certs/ATECC608A-MAH4I/device_template.crt"
MAH4I_SIGNER_CERT_TEMPLATE_FILE = "certs/ATECC608A-MAH4I/signer_2C10.crt"
TNGTLS_DEVICE_CERT_TEMPLATE_FILE = "certs/ATECC608B-TNGTLS/device_template.crt"

INSTALLDIR = os.path.abspath(os.path.dirname(__file__))

# Serial number suffix for custom ECC608 devices
ECC608_CUSTOM_SERIAL_SUFFIX = b"fe"
# Serial number suffix for Trust&Go and Trust&Flex based ECC608 devices
ECC608_TFLX_TNG_SERIAL_SUFFIX = b"01"


def build_certs_from_ecc(protocol,
                         signer_cert_filename,
                         device_cert_filename,
                         device_cert_template=None,
                         signer_cert_template=None,
                         force=False):
    """Build device and signer certificates from compressed certificates read out from the ECC device

    :param protocol: Firmware protocol driver.  The protocol object is assumed to be "ready to use", i.e. any port
        opening etc. should be done upfront
    :type protocol: :class:`pykitcommander.firmwareinterface.ApplicationFirmwareInterface` or one of it's sub-classes
    :param signer_cert_filename: Name of file to write the generated signer certificate to.
    :type signer_cert_filename: str
    :param device_cert_filename: Name of file to write the generated device certificate to.
    :type device_cert_filename: str
    :param device_cert_template: File with device certificate template.  Optional.  If set to None a built in
        template will be used
    :type device_cert_template: str (path)
    :param signer_cert_template: File with signer certificate template.  Optional.  If set to None a built in
        template will be used
    :type signer_cert_template: str (path)
    :param force: Force creating new certificates overwriting pre-existing output file
    :type force: bool
    :return: device_certificate, signer_certificate
    :rtype: :class:`cryptography.x509.Certificate` objects
    """
    logger = getLogger(__name__)

    dev_cert_cryptography_x509 = None
    sign_cert_cryptography_x509 = None

    if not force:
        try:
            # If the device cert file already exists, read it instead of re-creating it
            with open(device_cert_filename, "rb") as certfile:
                logger.info("Certificate already exists and will not be regenerated (force=False)")
                logger.info("Reading existing device certificate from '%s'", device_cert_filename)
                dev_cert_cryptography_x509 = cryptography.x509.load_pem_x509_certificate(data=certfile.read(),
                                                                                         backend=default_backend())
        except FileNotFoundError:
            pass
        try:
            # If the signer cert file already exists, read it instead of re-creating it
            with open(signer_cert_filename, "rb") as certfile:
                logger.info("Certificate already exists and will not be regenerated (force=False)")
                logger.info("Reading existing signer certificate from '%s'", signer_cert_filename)
                sign_cert_cryptography_x509 = cryptography.x509.load_pem_x509_certificate(data=certfile.read(),
                                                                                          backend=default_backend())
        except FileNotFoundError:
            pass

        if dev_cert_cryptography_x509 and sign_cert_cryptography_x509:
            # Both certificates already exists, nothing more to do
            logger.info("Certificates already exist and will not be regenerated (force=False)")
            return dev_cert_cryptography_x509, sign_cert_cryptography_x509

    compressed_data = CompressedCertificateData()
    compressed_data.read_from_kit(protocol)
    # Only read slot 5 if the ECC is not in [MAH1H, MAH4I]
    if not _is_ecc608_mah1h(compressed_data.ecc_serial_number) and not _is_ecc608_mah4i(compressed_data.ecc_serial_number):
        compressed_data.read_from_kit_slot5(protocol)

    if not dev_cert_cryptography_x509:
        logger.info("Decoding compressed device certificate")
        device_cert = DeviceCertificateRepresentation(compressed_data)

        # Find out what template to use, if none is provided
        if device_cert_template is None:
            device_cert_template = _get_ecc608_certificate_template_file(compressed_data.ecc_serial_number, "device")

        logger.info("Building device certificate using template: %s", device_cert_template)
        dev_builder = _get_ecc608_certificate_builder(compressed_data.ecc_serial_number, "device", device_cert_template)

        # Build from template
        dev_builder.build(device_cert)

        with open(device_cert_filename, "wb") as out:
            logger.info("Writing device certificate to file: %s", device_cert_filename)
            out.write(asn1crypto.pem.armor("CERTIFICATE", dev_builder.certificate.dump()))

        # Convert certificate object to cryptography.x509.Certificate
        dev_cert_cryptography_x509 = cryptography.x509.load_pem_x509_certificate(
            data=asn1crypto.pem.armor("CERTIFICATE", dev_builder.certificate.dump()), backend=default_backend())


    if not sign_cert_cryptography_x509:
        logger.info("Decoding compressed signer certificate")
        signer_cert = SignerCertificateRepresentation(compressed_data)

        # Find out what template to use, if none is provided
        if signer_cert_template is None:
            signer_cert_template = _get_ecc608_certificate_template_file(compressed_data.ecc_serial_number, "signer")

        logger.info("Building signer certificate using template: %s", signer_cert_template)
        sign_builder = _get_ecc608_certificate_builder(compressed_data.ecc_serial_number,
                                                       "signer", signer_cert_template)

        # Build from template
        sign_builder.build(signer_cert)

        with open(signer_cert_filename, "wb") as out:
            logger.info("Writing signer certificate to file: %s", signer_cert_filename)
            out.write(asn1crypto.pem.armor("CERTIFICATE", sign_builder.certificate.dump()))

        # Convert certificate object to cryptography.x509.Certificate
        sign_cert_cryptography_x509 = cryptography.x509.load_pem_x509_certificate(
            data=asn1crypto.pem.armor("CERTIFICATE", sign_builder.certificate.dump()), backend=default_backend())

    return dev_cert_cryptography_x509, sign_cert_cryptography_x509

def _get_ecc608_certificate_template_file(ecc_serial_number, cert_type):
    """
    Retrieves a template (/example) ECC608 certificate based

    :param ecc_serial_number: Serial number of ECC
    :type ecc_serial_number: binary
    :param cert_type: Type of certificate ('device' or 'signer')
    :type cert_type: str
    :return: template Certificate file (full path)
    :rtype: str (path)
    :raises:
        PytrustError: If a matching template file could not be identified
    """
    logger = getLogger(__name__)
    logger.info("Checking ECC variant")
    logger.info("ECC serial number {}".format(ecc_serial_number.hex()))
    # ECC608 as used in IOT kits:
    if _is_ecc608_mah1h(ecc_serial_number):
        logger.info("ECC variant 'MAH1H' found")
        if cert_type == "device":
            logger.info("Device certificate template: %s", MAH1H_DEVICE_CERT_TEMPLATE_FILE)
            cert_template_file = MAH1H_DEVICE_CERT_TEMPLATE_FILE
        elif cert_type == "signer":
            logger.info("Signer certificate template: %s", MAH1H_SIGNER_CERT_TEMPLATE_FILE)
            cert_template_file = MAH1H_SIGNER_CERT_TEMPLATE_FILE
        else:
            raise PytrustError("Unknown certificate type: {}!".format(cert_type))
    elif _is_ecc608_mah4i(ecc_serial_number):
        logger.info("ECC variant 'MAH4I' found")
        if cert_type == "device":
            logger.info("Device certificate template: %s", MAH4I_DEVICE_CERT_TEMPLATE_FILE)
            cert_template_file = MAH4I_DEVICE_CERT_TEMPLATE_FILE
        elif cert_type == "signer":
            logger.info("Signer certificate template: %s", MAH4I_SIGNER_CERT_TEMPLATE_FILE)
            cert_template_file = MAH4I_SIGNER_CERT_TEMPLATE_FILE
        else:
            raise PytrustError("Unknown certificate type: {}!".format(cert_type))
    else:
        raise PytrustError("Unknown ECC variant")

    return os.path.normpath(os.path.join(INSTALLDIR, cert_template_file))

def _get_ecc608_certificate_builder(ecc_serial_number, cert_type, cert_template_file):
    """
    Instantiates the correct certificate builder based on the given parameters

    :param ecc_serial_number: Serial number of ECC
    :type ecc_serial_number: binary
    :param cert_type: Type of certificate ('device' or 'signer')
    :type cert_type: str
    :param cert_template_file: File name (full path) to file with a certificate tempate/example to use for the
        certificate builder
    :type cert_template_file: str (path)
    :return: certificate builder object
    :rtype: instance of :class:EccCertificateBuilder or one of its subclasses
    :raises:
        PytrustError: If a matching certificate builder could not be identified
    """
    logger = getLogger(__name__)
    logger.info("Checking ECC variant")
    # ECC608 as used in IOT kits:
    cert_builder = None
    if _is_ecc608_mah1h(ecc_serial_number):
        with open(cert_template_file, "rb") as myfile:
            cert_template = myfile.read()
        if cert_type == "device":
            cert_builder = Mah1hDeviceCertificateBuilder(cert_template)
        elif cert_type == "signer":
            cert_builder = Mah1hSignerCertificateBuilder(cert_template)
        else:
            raise PytrustError("Unknown certificate type: {}!".format(cert_type))
    elif _is_ecc608_mah4i(ecc_serial_number):
        with open(cert_template_file, "rb") as myfile:
            cert_template = myfile.read()
        if cert_type == "device":
            cert_builder = Mah4iDeviceCertificateBuilder(cert_template)
        elif cert_type == "signer":
            cert_builder = Mah4iSignerCertificateBuilder(cert_template)
        else:
            raise PytrustError("Unknown certificate type: {}!".format(cert_type))
    else:
        raise PytrustError("Unknown ECC variant")

    return cert_builder


def _is_ecc608_mah1h(ecc_serial_number):
    """
    Check if ECC is variant MAH1H

    :param ecc_serial_number: Serial number from ECC device
    :type ecc_serial_number: binary
    :return: True if the ECC serial number corresponds to an ECC variant MAH1H
    """
    if binascii.b2a_hex(ecc_serial_number)[0-len(ECC608_CUSTOM_SERIAL_SUFFIX):] == ECC608_CUSTOM_SERIAL_SUFFIX:
        return True
    return False

def _is_ecc608_mah4i(ecc_serial_number):
    """
    Check if ECC is variant MAH4I

    :param ecc_serial_number: Serial number from ECC device
    :type ecc_serial_number: binary
    :return: True if the ECC serial number corresponds to an ECC variant MAH1H
    """
    if binascii.b2a_hex(ecc_serial_number)[0-len(ECC608_TFLX_TNG_SERIAL_SUFFIX):] == ECC608_TFLX_TNG_SERIAL_SUFFIX:
        return True
    return False

class EccCertificateBuilder():
    """ Certificate builder for ATECC608 certificates.
    """
    def __init__(self, cert_pem):
        """ Init with template certificate.

        Args:
           cert_pem (str): Certificate in PEM format.
        """
        _, _, cert_der = asn1crypto.pem.unarmor(cert_pem)
        certificate = asn1crypto.x509.Certificate.load(cert_der)
        self.certificate = certificate

    def add_signature(self, signature):
        sig = DSASignature().from_p1363(signature)
        self.certificate['signature_value'] = sig.dump()

    def set_validity_dates(self, validity_not_before, validity_not_after):
        """ Set validity dates in certificate.

        :param datetime validity_not_before: Date and time where certificate should note be valid before
        :param datetime validity_not_after: Date and time where certificate should note be valid after
        """
        utc_time = UTCTime()
        utc_time.set(validity_not_before)
        self.certificate['tbs_certificate']['validity']['not_before'] = utc_time

        gen_time = GeneralizedTime()
        gen_time.set(validity_not_after)
        self.certificate['tbs_certificate']['validity']['not_after'] = gen_time

    def set_pubkey(self, pubkey):
        """
        TBD the from_coords does not result in the expected outcome so we create the raw DER encoding
        that we load into the ECPointString class.

        ecpoint = ECPointBitString().from_coords(int.from_bytes(pubkey[0:33], byteorder='big', signed=False),
                 int.from_bytes(pubkey[33:], byteorder='big', signed=False))
        """
        ecpoint = ECPointBitString().load(b"\x03\x42\x00\x04" + pubkey)
        self.certificate['tbs_certificate']['subject_public_key_info']['public_key'] = ecpoint

    def set_serial_number(self, serial):
        self.certificate['tbs_certificate']['serial_number'].set(serial)


class Mah1hDeviceCertificateBuilder(EccCertificateBuilder):
    """ Build device certificate for ATECC608A-MAH1H
    """
    def set_authority_key_identifier(self, akid):
        akk = AuthorityKeyIdentifier()
        akk[0] = OctetString(akid)
        self.certificate['tbs_certificate']['extensions'][0]['extn_value'] = akk

    def set_issuer(self, signer_id):
        test = Name().build({"organization_name": "Microchip Technology Inc",
                             "common_name": "ATECC 1H Signer {:X}".format(signer_id)})
        self.certificate['tbs_certificate']['issuer'] = test

    def build(self, data):
        self.set_validity_dates(data.validity_not_before, data.validity_not_after)
        self.add_signature(data.signature)
        self.set_pubkey(data.device_pkey)
        self.set_serial_number(data.sn_number)
        self.set_issuer(data.signer_id)
        self.set_authority_key_identifier(data.akid)

class Mah1hSignerCertificateBuilder(EccCertificateBuilder):
    """ Build signer certificate for ATECC608A-MAH1H
    """
    def set_validity_dates(self, validity_not_before, validity_not_after):
        not_before = UTCTime()
        not_before.set(validity_not_before)
        self.certificate['tbs_certificate']['validity']['not_before'] = not_before

        not_after = UTCTime()
        not_after.set(validity_not_after)
        self.certificate['tbs_certificate']['validity']['not_after'] = not_after

    def set_subject(self, signer_id):
        subject = Name().build({"organization_name": "Microchip Technology Inc",
                                "common_name": "ATECC 1H Signer {:X}".format(signer_id)})
        self.certificate['tbs_certificate']['subject'] = subject

    def set_subject_key_identifier(self, skid):
        string = OctetString(skid)
        self.certificate['tbs_certificate']['extensions'][2]['extn_value'] = string

    def build(self, data):
        self.set_validity_dates(data.validity_not_before, data.validity_not_after)
        self.set_subject(data.signer_id)
        self.set_subject_key_identifier(data.skid)
        self.add_signature(data.signature)
        self.set_pubkey(data.signer_pkey)
        self.set_serial_number(data.sn_number)

class TngDeviceCertificateBuilder(EccCertificateBuilder):
    def set_issuer(self, signer_id):
        issuer = Name().build({"organization_name": "Microchip Technology Inc",
                               "common_name": "Crypto Authentication Signer {:X}".format(signer_id)})
        self.certificate['tbs_certificate']['issuer'] = issuer

    def set_subject(self, serial_number):
        serial_number = serial_number.hex()
        serial_number = serial_number.upper()
        subject = Name().build({"organization_name": "Microchip Technology Inc",
                                "common_name": "sn{}".format(serial_number)})
        self.certificate['tbs_certificate']['subject'] = subject

    def set_mac_address(self, eui48="FFFFFFFFFFFFFFFF"):
        name = Name().build({"serial_number": "eui48_{}".format(eui48)})
        gname = GeneralName("directory_name", name)
        gnames = GeneralNames()
        gnames[0] = gname
        ext = Extension({'extn_id': 'subject_alt_name', 'extn_value': gnames})
        self.certificate['tbs_certificate']['extensions'][0] = ext

    def set_subject_key_identifier(self, skid, extension_index=3):
        string = OctetString(skid)
        self.certificate['tbs_certificate']['extensions'][extension_index]['extn_value'] = string
        # Alternative update of the skid by creating the whole extension
        # ext = Extension({'extn_id': 'key_identifier', 'extn_value': string})
        # self.certificate['tbs_certificate']['extensions'][extension_index] = ext

    def set_authority_key_identifier(self, akid, extension_index=4):
        akk = AuthorityKeyIdentifier()
        akk[0] = OctetString(akid)
        self.certificate['tbs_certificate']['extensions'][extension_index]['extn_value'] = akk

    def build(self, data):
        self.set_validity_dates(data.validity_not_before, data.validity_not_after)
        self.add_signature(data.signature)
        self.set_pubkey(data.device_pkey)
        self.set_serial_number(data.sn_number)
        self.set_subject(data.ecc_serial_number)
        self.set_issuer(data.signer_id)
        self.set_subject_key_identifier(data.skid)
        self.set_authority_key_identifier(data.akid)
        self.set_mac_address(data.eui48)

class TngSignerCertificateBuilder(EccCertificateBuilder):

    def set_subject(self, signer_id):
        subject = Name().build({"organization_name": "Microchip Technology Inc",
                                "common_name": "Crypto Authentication Signer {:X}".format(signer_id)})
        self.certificate['tbs_certificate']['subject'] = subject

    def set_subject_key_identifier(self, skid):
        string = OctetString(skid)
        self.certificate['tbs_certificate']['extensions'][2]['extn_value'] = string

    def build(self, data):
        self.set_validity_dates(data.validity_not_before, data.validity_not_after)
        self.add_signature(data.signature)
        self.set_pubkey(data.signer_pkey)
        self.set_serial_number(data.sn_number)
        self.set_subject(data.signer_id)
        self.set_subject_key_identifier(data.skid)
        #self.set_authority_key_identifier(data.device.akid)

class Mah4iDeviceCertificateBuilder(TngDeviceCertificateBuilder):
    def build(self, data):
        self.set_validity_dates(data.validity_not_before, data.validity_not_after)
        self.add_signature(data.signature)
        self.set_pubkey(data.device_pkey)
        self.set_serial_number(data.sn_number)
        self.set_subject(data.ecc_serial_number)
        self.set_issuer(data.signer_id)
        self.set_subject_key_identifier(data.skid, extension_index=2)
        self.set_authority_key_identifier(data.akid, extension_index=3)

class Mah4iSignerCertificateBuilder(TngSignerCertificateBuilder):
    pass
