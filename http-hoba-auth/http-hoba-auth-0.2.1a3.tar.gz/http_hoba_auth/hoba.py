# standard imports
import logging
import base64
import time
import hashlib
from urllib.parse import urlparse

# local imports
from . import signature_algorithm_ids

logg = logging.getLogger()

def validate_origin(origin):
    parsed_origin = urlparse(origin)
    if parsed_origin.scheme not in ['http', 'https']:
        raise ValueError('invalid origin {}, not http(s)'.format(origin))
    if parsed_origin.port == None:
        raise ValueError('port missing from origin')
    return origin


class Hoba:
    """Helper class for generating data for signing, and parsing authorization string

   
    :param origin: HOBA origin value
    :type origin: str
    :param realm: HOBA realm value
    :type origin: str
    :param signature_algorithm: Signature algorithm used for generating the authorization string, default RSA-SHA256
    :type signature_algorithm: 
    :raises ValueError: If origin is an invalid url or missing explicit port
    """
    def __init__(self, origin, realm, alg='00'):
        self.alg = alg
        self.origin = validate_origin(origin)
        self.realm = realm
        self.nonce = None
        self.kid = None
        self.challenge = None
        self.signature = None

    
    def parse(self, s):
        """Parses a HOBA authorization string, and sets the respective properties of the instance to the parsed values.
    
        :param s: Authorization string
        :type s: str
        """
        fields = s.split('.')
        self.nonce = base64.b64decode(fields[0])
        self.kid = base64.b64decode(fields[1])
        self.challenge = base64.b64decode(fields[2])
        self.signature = base64.b64decode(fields[3])
        logg.debug('parsed hoba nonce {}'.format(self.nonce.hex()))
        logg.debug('parsed hoba kid {}'.format(self.kid.hex()))
        logg.debug('parsed hoba challenge {}'.format(self.challenge.hex()))
        logg.debug('parsed hoba signature {}'.format(self.signature.hex()))


    def to_be_signed(self):
        """Generates a "to-be-signed" HOBA byte string based on the values set in the instance.

        :return: "To-be-signed" string
        :rtype: bytes
        """
        nonce_bytes = base64.b64encode(self.nonce)
        nonce = nonce_bytes.decode('utf-8')
        kid_bytes = base64.b64encode(self.kid)
        kid = kid_bytes.decode('utf-8')
        challenge_bytes = base64.b64encode(self.challenge)
        challenge = challenge_bytes.decode('utf-8')

        s = ''
        for f in [nonce, self.alg, self.origin, self.realm, kid, challenge]:
            s += '{}:{}'.format(str(len(f)), f)

        return s


    def __str__(self):
        return '{}.{}.{}.{}'.format(
                base64.b64encode(self.nonce).decode('utf-8'),
                base64.b64encode(self.kid).decode('utf-8'),
                base64.b64encode(self.challenge).decode('utf-8'),
                base64.b64encode(self.signature).decode('utf-8'),
                )


def hoba_auth_request_string(nonce, expire, realm=''):
    nonce_b64 = base64.b64encode(nonce)
    expires_duration = expire - time.time()
    wwwauth_header_value  = 'charset="UTF-8",challenge="{}",max-age="{}"'.format(
        nonce_b64.decode('utf-8'),
        int(expires_duration),
    )
    if realm != None:
        wwwauth_header_value += ',realm="{}"'.format(realm)
    return 'HOBA {}'.format(wwwauth_header_value)
