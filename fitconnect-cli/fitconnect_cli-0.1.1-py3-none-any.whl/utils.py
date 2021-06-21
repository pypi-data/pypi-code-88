from datetime import datetime
from typing import Dict

import jwt


# taken from https://github.com/Humanitec/django-oauth-toolkit-jwt
def generate_payload(issuer: str, expiration: datetime, **extra_data) -> Dict[str, str]:
    """
    :param expiration:
    :type: datetime
    :param issuer: identifies the principal that issued the token.
    :type issuer: str
    :param extra_data: extra data to be added to the payload.
    :type extra_data: dict
    :rtype: dict
    """
    now = datetime.utcnow()
    issued_at = now
    payload = {
        "iss": issuer,
        "exp": int(datetime.timestamp(expiration)),
        "iat": int(datetime.timestamp(issued_at)),
    }
    payload.update(**extra_data)

    return payload


def encode_jwt(payload: Dict[str, str], algorithm: str, private_key: str, headers=None):
    """
    :param algorithm: the algorithm should be used for signing
    :param private_key: the private key that should be used for signing
    :param payload: the payload that should be signed
    :param headers: additional headers
    :rtype: str
    """

    encoded = jwt.encode(payload, private_key, algorithm=algorithm, headers=headers)
    return encoded


def decode_jwt_claims_without_verification(token: str):
    decoded_claims = jwt.decode(token, options={"verify_signature": False})
    return decoded_claims


def decode_jwt_header_without_verification(token: str):
    decoded_header = jwt.get_unverified_header(token)
    return decoded_header
