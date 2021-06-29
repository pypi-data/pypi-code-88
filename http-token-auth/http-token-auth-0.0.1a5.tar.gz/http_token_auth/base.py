# standard imports
import logging
import hashlib

# local imports
from .session import (
        Session,
        DEFAULT_AUTH_EXPIRE,
        DEFAULT_REFRESH_EXPIRE,
        )
from .error import TokenExpiredError

logg = logging.getLogger(__name__)


class SessionStore:
    """Holds current sessions in memory and generates new auth tokens based on current settings

    :param auth_expire_delta: Overrides http_token_auth.session.DEFAULT_AUTH_EXPIRE
    :type auth_expire_delta: number
    :param refresh_expire_delta: Overrides http_token_auth.session.DEFAULT_REFRESH_EXPIRE
    :type refresh_expire_delta: number
    """
    def __init__(self, auth_expire_delta=DEFAULT_AUTH_EXPIRE, refresh_expire_delta=DEFAULT_REFRESH_EXPIRE):
        self.session = {}
        self.session_reverse = {}
        self.auth_expire_delta = auth_expire_delta
        self.refresh_expire_delta = refresh_expire_delta


    def new(self, k):
        session = Session(k, auth_expire_delta=self.auth_expire_delta, refresh_expire_delta=self.refresh_expire_delta)
        self.session[k] = session
        auth_token = session.renew(session.refresh)
        self.session_reverse[session.auth] = session
        logg.debug('added session {} auth token {}'.format(session, auth_token))
        return auth_token


    def get_refresh(self, identity):
        return self.session[identity].refresh


    def get_session(self, auth_token):
        return self.session_reverse[auth_token]


    def get(self, k):
        """Initializes session and stores session in registry.

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


    def renew(self, k, refresh_token):
        """Renews an expired auth token.

        :param address: Ethereum address of user
        :type address: str, 0x-hex
        :raises ecuth.error.SessionExpiredError: Refresh token expired (must restart challenge)
        :return: New auth token
        :rtype: bytes
        """
        old_token = self.session[k].auth
        new_token = self.session[k].renew(refresh_token)
        self.session_reverse[new_token] = self.session_reverse[old_token]
        if old_token != None:
            del self.session_reverse[old_token]
        return new_token 


    def check(self, v):
        return self.session_reverse[v]
