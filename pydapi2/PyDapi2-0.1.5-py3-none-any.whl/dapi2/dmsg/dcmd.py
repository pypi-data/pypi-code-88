'''
Created on 22 févr. 2021

@author: fv
'''
from .message import CommandMessage


class Null(CommandMessage):
    """Null commande message
        """
    def __init__(self):
        super().__init__("0x00", [])
        

class Reboot(CommandMessage):
    """Reboot message
    """
    def __init__(self):
        super().__init__("0x01", [])


class Connect(CommandMessage):
    """Connect message
    
    :param accessLevel: access level 0 to 6
    """
    def __init__(self, accessLevel, password):
        high, low = divmod(password, 0x100)
        super().__init__(0x05, [accessLevel, high, low], 3)


class Disconnect(CommandMessage):
    """Connect message
    
    :param accessLevel: access level 0 to 6
    """
    def __init__(self):
        super().__init__("0x06", [])
        

