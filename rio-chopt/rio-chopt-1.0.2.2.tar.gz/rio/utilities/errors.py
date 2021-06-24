class Error(Exception):
    """
    Base error class
    """
    def __init__(self, message="An unknown error has occurred."):
        super().__init__(message)


class BadCredError(Error):
    """
    Handles passing through bad credentials to Docker
    """
    def __init__(self, message="Credentials failed to authenticate."):
        super().__init__(message)


class DockerNotRunningError(Error):
    """
    Handles trying to run RIO locally without Docker running
    """
    def __init__(self, message="Docker is not running!"):
        super().__init__(message)


class LocalError(Error):
    """
    Error for when local flag is not set

    ***SET TO BE DEPRECATED UPON RELEASING CLOUD SUPPORT THROUGH CLI***
    """
    def __init__(self, message="Please email contact@chainopt.com for remote deployment services."):
        super().__init__(message)
