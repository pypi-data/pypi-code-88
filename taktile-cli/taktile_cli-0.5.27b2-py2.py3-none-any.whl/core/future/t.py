from tktl.core import ExtendedEnum


class EndpointKinds(str, ExtendedEnum):
    BASIC = "basic"
    TYPED = "typed"
    ARROW = "arrow"
    PROFILED = "profiled"


class ProfileKinds(str, ExtendedEnum):
    BINARY = "binary"
    REGRESSION = "regression"
