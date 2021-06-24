# standard imports
import time
import uuid

# local imports
from .error import SessionExpiredError
from .error import SessionError
from .error import TokenExpiredError

DEFAULT_AUTH_EXPIRE = 60
DEFAULT_REFRESH_EXPIRE = 60 * 60 * 24 * 30


class Session:
    """State of authentication session and ACL data.

    :param identity: Authorization digest of user
    :type identity: str, 0x-hex
    :param acl: ACL entries for user
    :type acl: ecuth.acl.Acl
    """
    def __init__(self, identity): #, acl=None):
        self.identity = identity
        uu = uuid.uuid4()
        self.refresh = uu.bytes
        self.refresh_expire = time.time() + DEFAULT_REFRESH_EXPIRE
        self.auth = None
        self.auth_expire = 0.0
#        self.acl = acl
        self.renew(self.refresh)


    def renew(self, refresh):
        """Renew auth token.

        :param refresh: Refresh token
        :type refresh: bytes
        :raises ecuth.error.SessionError: Refresh token unknown
        :raises ecuth.error.SessionExpiredError: Refresh token expired (must restart challenge)
        :return: New auth token
        :rtype: bytes
        """
        if self.refresh != refresh:
            raise SessionError('invalid refresh token for {}'.format(self.identity))
        if self.refresh_expire < time.time():
            raise SessionExpiredError(self.identity)
        uu = uuid.uuid4()
        self.auth = uu.bytes
        self.auth_expire = time.time() + DEFAULT_AUTH_EXPIRE
        return self.auth


    def valid(self):
        """Check if auth token is currently valid.

        :returns: Valid or not
        :rtype: boolean
        """
        return self.auth_expire > time.time()

#
#    def read(self, item):
#        if not self.valid():
#            raise TokenExpiredError()
#        return self.acl.read(item)
#
#    def write(self, item):
#        if not self.valid():
#            raise TokenExpiredError()
#        return self.acl.write(item)
#
#    def val(self, item):
#        if not self.valid():
#            raise TokenExpiredError()
#        return self.acl.val(item)
#


    def __str__(self):
        f = """identity: {}
token: {}
expires: {}
acl:
{} 
"""
        d = f.format(
            self.identity.hex(),
            self.auth.hex(),
            self.auth_expire,
            #self.acl,
            None,
        )

        return d
