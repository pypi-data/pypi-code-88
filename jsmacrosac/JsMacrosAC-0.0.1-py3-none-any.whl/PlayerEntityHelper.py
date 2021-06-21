from .ItemStackHelper import *
from .PlayerAbilitiesHelper import *
from .LivingEntityHelper import *

class PlayerEntityHelper(LivingEntityHelper, ):



    def __init__(e: T, ):
        pass


    def getAbilities(self, ) -> PlayerAbilitiesHelper:
        pass

    def getMainHand(self, ) -> ItemStackHelper:
        pass

    def getOffHand(self, ) -> ItemStackHelper:
        pass

    def getHeadArmor(self, ) -> ItemStackHelper:
        pass

    def getChestArmor(self, ) -> ItemStackHelper:
        pass

    def getLegArmor(self, ) -> ItemStackHelper:
        pass

    def getFootArmor(self, ) -> ItemStackHelper:
        pass

    def getXP(self, ) -> int:
        pass

    def isSleeping(self, ) -> bool:
        pass

    def isSleepingLongEnough(self, ) -> bool:
        pass

    def toString(self, ) -> str:
        pass


    pass
