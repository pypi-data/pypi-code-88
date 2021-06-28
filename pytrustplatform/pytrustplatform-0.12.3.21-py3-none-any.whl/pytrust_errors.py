"""
pytrustplatform specific exceptions
"""

class PytrustError(Exception):
    """
    Base class for all pytrustplatform specific exceptions
    """

    def __init__(self, msg=None, code=0):
        super(PytrustError, self).__init__(msg)
        self.code = code

class PytrustCertificateError(PytrustError):
    """
    Signals a problem with a certificate
    """

    def __init__(self, msg=None, code=0):
        super(PytrustCertificateError, self).__init__(msg)
        self.code = code
