# standard imports
import logging
import hashlib

# local imports
from .session import Session
from .error import TokenExpiredError

logg = logging.getLogger(__name__)


class SessionStore:

    def __init__(self):
        self.session = {}
        self.session_reverse = {}


    def new(self, k):
        session = Session(k)
        self.session[k] = session
        auth_token = session.renew(session.refresh)
        self.session_reverse[session.auth] = session
        logg.debug('added session {} auth token {}'.format(session, auth_token))
        return auth_token


    def get(self, k):
        """Retrieves ACL, initializes session and stores session in registry.

        :param k: Token or identity key
        :type k: bytes
        :return: New session
        :rtype: ecuth.Session
        """
        session = None
        try:
            logg.debug('try session by auth token: {}'.format(k))
            session = self.check(k)
        except KeyError:
            logg.debug('try session by identity: {}'.format(k))
            session = self.session[k]
        except KeyError:
            logg.debug('session not found for: {}'.format(k))
            return None

        if not session.valid():
            raise TokenExpiredError(k)

        return session


#    def renew(self, address, refresh_token):
#        """Renews an expired auth token.
#
#        :param address: Ethereum address of user
#        :type address: str, 0x-hex
#        :raises ecuth.error.SessionExpiredError: Refresh token expired (must restart challenge)
#        :return: New auth token
#        :rtype: bytes
#        """
#        old_token = self.session[address].auth
#        new_token = self.session[address].renew(refresh_token)
#        self.session_reverse[new_token] = address
#        if old_token != None:
#            del self.session_reverse[old_token]
#        return new_token 


    def check(self, v):
        return self.session_reverse[v]


