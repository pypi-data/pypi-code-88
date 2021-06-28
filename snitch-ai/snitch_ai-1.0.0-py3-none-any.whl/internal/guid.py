from uuid import UUID


class GUID(UUID):
    """
    Basic implementation of a Microsoft GUID class over Python's base UUID class. This allows for using string
    representations of GUIDs generated in .NET in Python and be able to implicitly convert them to their binary
    representations without causing massive errors.
    """

    def __init__(self, str_guid: str):
        super().__init__(bytes_le=bytes(bytearray.fromhex(str_guid.replace("-", ""))))

    def __str__(self):
        hexes = self.bytes_le.hex()

        return f"{hexes[0:8]}-{hexes[8:12]}-{hexes[12:16]}-{hexes[16:20]}-{hexes[20:32]}"