# standard imports
import logging
import hashlib

# local imports
from .session import Session
from .error import TokenExpiredError

logg = logging.getLogger(__name__)



# ecuth provision, delete when ecuth is pruned
class SessionFetcher:
    """Base implementation of ACL retriever

    :param fetcher: Retrieves authentication info for authentication digest
    :type fetcher: function
    :param parser: Object capable of parsing authentication info returned from fetcher to return an ACL object
    :type parser: class
    """
    def __init__(self, fetcher, parser):
        self.fetcher = fetcher
        self.session = {}
        self.session_reverse = {}
        self.parser = parser


    def clear(self, identity):
        """Clear session from registry

        :param identity: Authorization digest of user
        :type identity: bytes
        """
        if self.session.get(identity) != None:
            del self.session[identity]


    def load(self, k):
        """Retrieves ACL, initializes session and stores session in registry.

        :param k: Token or identity key
        :type k: bytes
        :return: New session
        :rtype: ecuth.Session
        """
        session = None
        try:
            session = self.check(k) #session_reverse[k]
            logg.debug('session by auth token: {}'.format(k))
        except KeyError:
            data = self.fetcher(k)
            logg.debug('session load {} {}'.format(k, data))
            acl = self.parser(data)

            session = Session(k, acl)
            self.session[k] = session
            self.session_reverse[session.auth] = session
            logg.debug('added session {}'.format(session))

        if not session.valid():
            raise TokenExpiredError(k)

        return session


    def renew(self, address, refresh_token):
        """Renews an expired auth token.

        :param address: Ethereum address of user
        :type address: str, 0x-hex
        :raises ecuth.error.SessionExpiredError: Refresh token expired (must restart challenge)
        :return: New auth token
        :rtype: bytes
        """
        old_token = self.session[address].auth
        new_token = self.session[address].renew(refresh_token)
        self.session_reverse[new_token] = address
        if old_token != None:
            del self.session_reverse[old_token]
        return new_token 


    def check(self, address):
        return self.session_reverse[address]
