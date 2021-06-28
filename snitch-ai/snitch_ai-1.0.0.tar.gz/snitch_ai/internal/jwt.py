import jwt
import pkg_resources

from cryptography.hazmat.backends import default_backend
from cryptography.x509 import load_pem_x509_certificate


def decode_token(token):
    cert_file = pkg_resources.resource_filename("snitch_ai", "cert/snitch.accesstokens.crt")
    with open(cert_file, "rb") as file:
        contents = file.read()

    key = load_pem_x509_certificate(contents, backend=default_backend())
    public_key = key.public_key()

    return jwt.decode(token, public_key, algorithms=["RS512"])