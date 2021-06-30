
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
import datetime


class Certs:

    def __init__(self, pem_csr, passphrase):
        self.pem_csr = pem_csr
        self.passphrase = passphrase

        self._csr = csr(self.pem_csr)
        self._key = private_key()
        self._ca_cert = ca_cert(self._key)
        self._hsm_cert = hsm_cert(self._ca_cert, self._csr, self._key)

        self.valid = validate_hsm_cert(self._hsm_cert, self._ca_cert)
        self.pem_private_key = pem_private_key(self._key, self.passphrase)
        self.pem_ca_cert = pem_ca_cert(self._ca_cert)
        self.pem_hsm_cert = pem_hsm_cert(self._hsm_cert)


def csr(pem_csr):
    if type(pem_csr) is bytes:
        bytes_csr = pem_csr
    else:
        bytes_csr = bytes(pem_csr, 'utf-8')

    return x509.load_pem_x509_csr(bytes_csr)


def private_key():
    return rsa.generate_private_key(public_exponent=65537, key_size=2048)


def private_key_from_pem(pem_private_key, string_passphrase):
    return serialization.load_pem_private_key(pem_private_key, bytes(string_passphrase, 'UTF-8'))


def pem_private_key(bytes_private_key, string_passphrase):
    pem_sk = bytes_private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.BestAvailableEncryption(
            bytes(string_passphrase, 'utf-8')))
    return pem_sk


def ca_cert(private_key):
    builder = x509.CertificateBuilder()
    name = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"."),
        x509.NameAttribute(NameOID.LOCALITY_NAME, u"."),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"."),
        x509.NameAttribute(NameOID.COMMON_NAME, u".")
    ])

    builder = builder.serial_number(1)
    builder = builder.issuer_name(name)
    builder = builder.subject_name(name)
    builder = builder.public_key(private_key.public_key())
    builder = builder.not_valid_before(
        datetime.datetime.utcnow() - datetime.timedelta(hours=1))
    builder = builder.not_valid_after(
        datetime.datetime.utcnow() + datetime.timedelta(days=3652))
    builder = builder.add_extension(x509.BasicConstraints(ca=True, path_length=None), True
                                    )
    return builder.sign(private_key, hashes.SHA256(), default_backend())


def pem_ca_cert(ca_cert):
    return ca_cert.public_bytes(serialization.Encoding.PEM)


def hsm_cert(ca_cert, csr, private_key):
    builder = x509.CertificateBuilder(
        issuer_name=ca_cert.issuer,
        subject_name=csr.subject,
        public_key=csr.public_key(),
        not_valid_before=datetime.datetime.utcnow() - datetime.timedelta(hours=1),
        not_valid_after=datetime.datetime.utcnow() + datetime.timedelta(days=3652),
        extensions=csr.extensions,
        serial_number=x509.random_serial_number()
    )
    return builder.sign(
        private_key=private_key, algorithm=hashes.SHA256(), backend=default_backend())


def pem_hsm_cert(hsm_cert):
    return hsm_cert.public_bytes(serialization.Encoding.PEM)


def validate_hsm_cert(hsm_cert, ca_cert):
    public_key = ca_cert.public_key()

    try:
        public_key.verify(
            hsm_cert.signature,
            hsm_cert.tbs_certificate_bytes,
            padding.PKCS1v15(),
            hsm_cert.signature_hash_algorithm
        )
        return True
    except:
        return False
