from . import GetErrorMessageFromCode, GetMifareErrorMessageFromCode
from .MPStatus import CTS3ErrorCode, MifareErrorCode


class CTS3Exception(Exception):
    """CTS3 exception"""

    def __init__(self, err_code: CTS3ErrorCode):
        """Contructor

        Parameters
        ----------
        err_code: CTS3ErrorCode
            Error code
        """
        Exception.__init__(self, GetErrorMessageFromCode(err_code.value))
        self.ErrorCode = err_code


class CTS3MifareException(Exception):
    """CTS3 MIFARE exception"""

    def __init__(self, err_code: MifareErrorCode):
        """Contructor

        Parameters
        ----------
        err_code: MifareErrorCode
            Error code
        """
        Exception.__init__(self, GetMifareErrorMessageFromCode(err_code.value))
        self.ErrorCode = err_code
