import enum


class HeaderType(enum.IntEnum):
    PRG_RELOC = 1
    SEQ_DATA = 2
    PRG = 3
    SEQ = 4
    EOT = 5

    def __str__(self):
        parts = super().__str__().split('.', 1)
        return parts[1]
