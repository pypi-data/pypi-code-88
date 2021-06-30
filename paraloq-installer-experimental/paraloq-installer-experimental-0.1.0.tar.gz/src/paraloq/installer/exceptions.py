"""Exceptions used by the paraloq alpha module."""


class SessionError(Exception):
    """Exception raised when there is no valid paraloq session established.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression: str = None, message: str = None):
        self.expression = expression
        self.message = message
