"""Module to hold the main RocketToken class that the library exposes."""

from __future__ import annotations

import base64
from datetime import datetime, timedelta
import json
import logging
import os
import re
from typing import Tuple
from typing import Union

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa

from .exceptions import InvalidTokenException, NoPrivateKeyException

LOGGER = logging.Logger(__name__, logging.INFO)

HTTP_METHODS = [
    "GET",
    "HEAD",
    "POST",
    "PUT",
    "DELETE",
    "CONNECT",
    "OPTIONS",
    "TRACE",
    "PATCH",
]


class RocketToken:
    r"""
    Class to:

        * Generate private and public keyfiles using RSA algorithm.
        * Validate payload tokens.
        * Generate and encrypt payload tokens
        * Decrypt encrypted payload tokens

    A token is an encoded string representation of a dictionary, e.g.

        rocket.new_token(path="id_rsa.pub", exp=10, method="GET", customer_id=3)
        {'customer_id': 3, 'path': 'id_rsa.pub', 'exp': 10, 'method': 'GET'}
        b"{'customer_id': 3, 'path': 'id_rsa.pub', 'exp': 10, 'method': 'GET'}"
        b"&\x8d}\xb1c\xa5\xdf\x89~\xea\xa2\x1clm\x9b\xb3"

    Validation is performed prior to encryption to ensure that each key, value
    dictionary pair conforms to an expected standard.
    """

    def __init__(
        self, public_key: rsa.RSAPublicKey, private_key=Union[rsa.RSAPrivateKey, None]
    ) -> None:
        self.public_key = public_key
        self.private_key = private_key

    @classmethod
    def load_from_env(cls: RocketToken) -> RocketToken:
        """Loads a public key and private key from environmental variables.

        Expected names for the environmental variables are public_key and
        private_key respectively. The private_key is optional.

        Args:
            cls (RocketToken): Instance of RocketToken class

        Returns: RocketToken
        """
        public_key = bytes(os.environ["public_key"], encoding="utf-8")
        public_key = re.sub(b"\\\\n", b"\\n", public_key)
        public_key = serialization.load_pem_public_key(
            public_key, backend=default_backend()
        )

        private_key = os.environ.get("private_key", None)
        if private_key is not None:
            private_key = bytes(private_key, encoding="utf-8")
            private_key = re.sub(b"\\\\n", b"\\n", private_key)
            private_key = serialization.load_pem_private_key(
                private_key, password=None, backend=default_backend()
            )

        return cls(public_key, private_key)

    @classmethod
    def load_from_path(
        cls, public_path: str = None, private_path: Union[str, None] = None
    ) -> RocketToken:
        """
        Creates an instance of the RocketToken class from a
        public and private key stored on the disk. The private key
        is optional.

        Args:
            public_path (str): File path to the public key file.
            private_path (str): File path to the private key file.

        Returns (RocketToken): RocketToken

        """
        public_key, private_key = None, None

        with open(public_path, "rb") as public:
            public_key = serialization.load_pem_public_key(
                public.read(), backend=default_backend()
            )

        if private_path:
            with open(private_path, "rb") as keyfile:
                private_key = serialization.load_pem_private_key(
                    keyfile.read(), password=None, backend=default_backend()
                )

        return cls(public_key=public_key, private_key=private_key)

    def encrypt_dictionary(self, dict_to_encrypt: dict) -> str:
        r"""
        Returns an encrypted user token.

        Args:
            path: (str) Path to the requested resource.
            exp: (int) Expiry time of request in minutes.
            method: (str) Request method, one of:
                    ['GET', 'POST']
            **kwargs: Arbitrary number of <key>=<value> pairs.

        Returns: (str) token

        """

        encrypted_token: bytes = self.public_key.encrypt(
            bytes(json.dumps(dict_to_encrypt), encoding="utf-8"),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )

        encrypted_token = base64.b64encode(encrypted_token)

        return f'Bearer {encrypted_token.decode("utf-8")}'

    def new_token(
        self, path: str = None, exp: int = None, method: str = None, **kwargs
    ) -> str:
        r"""
        Returns an encrypted user token.

        Args:
            path: (str) Path to the requested resource.
            exp: (int) Expiry time of request in minutes.
            method: (str) Request method, one of:
                    ['GET', 'POST']
            **kwargs: Arbitrary number of <key>=<value> pairs.

        Returns: (str) token

        """
        self.validate_path_exp_method(path=path, exp=exp, method=method)

        token = {
            "path": path,
            "expiry": exp,
            "expiry_date": (datetime.utcnow() + timedelta(minutes=exp)).isoformat(),
            "method": method.upper(),
            **kwargs,
        }

        self.validate(token=token, path=path, exp=exp, method=method)

        encrypted_token: bytes = self.public_key.encrypt(
            bytes(json.dumps(token), encoding="utf-8"),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )

        encrypted_token = base64.b64encode(encrypted_token)

        return f'Bearer {encrypted_token.decode("utf-8")}'

    def decode_token(self, token: str) -> dict:
        """Decrypts an encrypted token.

        Args:
            token (str): Encrypted token to decrypt.

        Returns (dict): json.loads(plaintext.decode(encoding="utf-8"))

        """
        if self.private_key is None:
            raise NoPrivateKeyException("No private key loaded. Cannot decode token.")

        _, token = token.split(" ")
        token = base64.b64decode(token.encode("utf-8"))

        self.private_key: rsa.RSAPrivateKey
        plaintext = self.private_key.decrypt(
            token,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )

        return json.loads(plaintext.decode(encoding="utf-8"))

    def decode_public_key(self) -> str:
        """
        Returns the Public key in PEM format.

        Returns (str): Public key

        """
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        ).decode("utf-8")

    @staticmethod
    def generate_key_pair(
        path: str, key_size: int = 4096, public_exponent: int = 65537
    ) -> Tuple[rsa.RSAPrivateKey, rsa.RSAPublicKey]:
        """
        Generates and saves public and private key files in PEM format.

        Args:
            path (str): Directory Location to save public and private key pairs.
            key_size (int): How many bits long the key should be.
            public_exponent int: indicates what one mathematical property of the
                                 key generation will be. Unless you have a
                                 valid reason to do otherwise, always use 65537.

        Returns (tuple[rsa.RSAPrivateKey, rsa.RSAPublicKey]): private_key, public_key

        """
        if not os.path.isdir(path):
            os.mkdir(path)

        private_key = rsa.generate_private_key(
            public_exponent=public_exponent,
            key_size=key_size,
            backend=default_backend(),
        )

        public_key = private_key.public_key()

        pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )

        public = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )

        with open(f"{path}/id_rsa", "wb") as binaryfile:
            binaryfile.write(pem)

        with open(f"{path}/id_rsa.pub", "wb") as binaryfile:
            binaryfile.write(public)

        print(f"Public and Private key pair saved to: {path}")
        return private_key, public_key

    @staticmethod
    def validate_path_exp_method(path: str, exp: int, method: str) -> Union[None, bool]:
        """Validates path, exp, and method.

        Returns True if path, exp, and method conform to expected parameters,
        or raises an InvalidTokenException otherwise.

        Args:
            path: (str) Path to the requested resource.
            exp: (int) Expiry time of request in minutes.
            method: (str) Request method, one of ['GET', 'POST']

        Raises:
            InvalidTokenException

        Returns (Union[None, bool]): Union[None, True]

        """
        if not isinstance(exp, int) or isinstance(exp, bool) or exp <= 0:
            raise InvalidTokenException("exp must be an integer greater than 0.")

        if not isinstance(path, str) or not path:
            raise InvalidTokenException("path must be a non-empty string")
        if path[-1] == "/":
            raise InvalidTokenException("path cannot end with '/'")

        if not isinstance(method, str) or method.upper() not in HTTP_METHODS:
            raise InvalidTokenException(f"method not in: {HTTP_METHODS}")

        return True

    @staticmethod
    def validate_token(token) -> Union[None, bool]:
        """Verifies token is a valid dictionary.

        Args:
            token (dict):

        Raises:
            InvalidTokenException

        Returns Union[None, bool]: Union[None, True]

        """
        expected_keys = ["path", "expiry_date", "method"]
        if not set(expected_keys).issubset(token.keys()):
            raise InvalidTokenException(
                f"Incorrect token keys; token must contain at least: {expected_keys}"
            )

        for key in expected_keys:
            if not token[key] or token[key] == "":
                raise InvalidTokenException(f"token[{key}] is missing.")

        if not datetime.utcnow() < datetime.fromisoformat(token["expiry_date"]):
            LOGGER.info("Invalid Token: expired")
            raise InvalidTokenException(
                f"token exp: {token['expiry_date']} has expired. Please set a new token exp."
            )

        return True

    @staticmethod
    def validate_token_path_method(
        token: dict, path: str, method: str
    ) -> Union[None, bool]:
        """Verify token[path] and token[method] match request path and request method

        Args:
            token (dict):
            path (str): Path to resource.
            method (str): HTTP method.

        Returns:

        """
        if token["path"] != path:
            raise InvalidTokenException(
                f"token['path'] != URL request path: {token['path']} != {path}"
            )

        if token["method"] != method:
            raise InvalidTokenException(
                f"token['method'] != URL request path: {token['method']} != {method}"
            )

        return True

    def validate(
        self, token: dict, path: str, exp: int, method: str
    ) -> Union[None, bool]:
        """Validates path, exp, method, and token.

        Checks that:
            1. path, exp, and method conform to expected values.
            1. token dictionary contains ["path", "exp", "method"] keys.
            1. token method and path match corresponding values.

        Args:
            token (dict): The underlying dictionary for the token
            path (str): The requested resource path.
            exp (int): Expiry time in minutes.
            method (str): A valid http request method from ["GET", "POST"]

        Raises:
            InvalidTokenException

        Returns Union[None, bool]: Union[None, True]
        """
        self.validate_path_exp_method(path=path, exp=exp, method=method)

        self.validate_token(token)

        self.validate_token_path_method(token=token, path=path, method=method)

        return True

    def decode_and_validate(self, token: str, path: str, exp: int, method: str) -> bool:
        """
        A convenience function to bundle the logic of decoding the token and
        validating it into one function.

        Args:
            token (str): The token to decode and validate.
            path (str): The path of the requested resource.
            exp (int): Expiry time in minutes.
            method (str): The HTTP method used to access the requested resource.

        Returns:
            bool: Indicates if the token was valid or not.
            NoReturn: No return when an exception is raised.

        Raises:
            NoPrivateKeyException: Raised when the RocketToken class is
            initialised without a private key and you attempt to decrypt a token.
            InvalidTokenException: Raised when token, path, exp, or method fail
            during validation.

        """
        token_dict = self.decode_token(token=token)

        return self.validate(token=token_dict, path=path, exp=exp, method=method)
