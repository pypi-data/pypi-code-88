"""Module for custom exceptions"""


class DeepChainAppException(Exception):
    pass


class AppNotFoundError(DeepChainAppException):
    def __init__(self, app):
        super(AppNotFoundError, self).__init__(
            f"App {app} not found, you must create it "
            f"before deployement or specify correct name."
        )


class ConfigNotFoundError(DeepChainAppException):
    def __init__(self):
        super(ConfigNotFoundError, self).__init__(
            (
                "Config File not found. You must login and register you PAT with :"
                " >> deepchain login"
            )
        )


class AppsNotFoundError(DeepChainAppException):
    def __init__(self):
        super(AppsNotFoundError, self).__init__(
            (
                "Apps files registry not found. You must create an app before deploy:"
                " >> deepchain create my_app"
            )
        )


class CheckpointNotFoundError(DeepChainAppException):
    def __init__(self):
        super(CheckpointNotFoundError, self).__init__(
            "Don't find any checkpoint file in checkpoint folder"
        )


class InvalidAppName(DeepChainAppException):
    def __init__(self, invalid_char):
        super(InvalidAppName, self).__init__(
            f"Your app' name must not contain the invalid character {invalid_char}"
        )
