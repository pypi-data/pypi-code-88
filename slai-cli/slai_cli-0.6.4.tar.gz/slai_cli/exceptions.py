class InvalidModelInputException(Exception):
    pass


class InvalidModelOutputException(Exception):
    pass


class ProjectExistsException(Exception):
    pass


class ModelExistsException(Exception):
    pass


class InvalidPathException(Exception):
    pass


class InvalidApiKey(Exception):
    pass


class InvalidHandlerSyntax(Exception):
    pass


class RetryException(Exception):
    pass
