# -*- coding: utf-8 -*-


class UnknownTokenError(Exception):
    """401 error when server cannot find the token"""

    def __init__(self, msg="Invalid token"):
        self.msg = msg
        super().__init__(self.msg)


class NoAuthorizationError(Exception):
    """403 error when server won't allow the upload"""

    def __init__(self, msg="No authorization"):
        self.msg = msg
        super().__init__(self.msg)


class FileConflictError(Exception):
    """409 error when file already on the server"""

    def __init__(self, msg="Conflict: file already on server"):
        self.msg = msg
        super().__init__(self.msg)
