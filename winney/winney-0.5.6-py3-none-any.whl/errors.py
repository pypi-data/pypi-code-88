
class WinneyRequestError(Exception):

    def __init__(self, message="failed to request data"):
        Exception.__init__(self, message)


class WinneyParamError(Exception):

    def __init__(self, message="invalid param"):
        Exception.__init__(self, message)


class NoServerAvalible(Exception):
    def __init__(self, message="cannot find an avalible server"):
        Exception.__init__(self, message)
