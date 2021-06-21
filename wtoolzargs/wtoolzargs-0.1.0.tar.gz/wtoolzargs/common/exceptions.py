class wtoolzargsError(Exception):
    pass


class ScanError(wtoolzargsError, RuntimeError):
    pass


class ParseError(wtoolzargsError, RuntimeError):
    pass


class InterpretError(wtoolzargsError, RuntimeError):
    pass
