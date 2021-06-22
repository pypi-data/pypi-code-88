from enum import Enum, unique


@unique
class AccessMode(Enum):
    SINGLE = "single"
    RECURRENT = "recurrent"


@unique
class TaxReturnType(Enum):
    YEARLY = "yearly"
    MONTHLY = "monthly"
