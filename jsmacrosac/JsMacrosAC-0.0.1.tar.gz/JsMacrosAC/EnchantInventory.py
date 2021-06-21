from .TextHelper import *
from .Inventory import *

class EnchantInventory(Inventory, ):



    def getRequiredLevels(self, ) -> int:
        pass

    def getEnchantments(self, ) -> TextHelper:
        pass

    def getEnchantmentIds(self, ) -> str:
        pass

    def getEnchantmentLevels(self, ) -> int:
        pass

    def doEnchant(self, index: int, ) -> bool:
        pass


    pass
