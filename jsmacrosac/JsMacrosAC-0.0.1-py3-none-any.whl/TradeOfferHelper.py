from .ItemStackHelper import *
from .VillagerInventory import *
from .BaseHelper import *

class TradeOfferHelper(BaseHelper, ):



    def __init__(base: TradeOffer, index: int, inv: VillagerInventory, ):
        pass


    def getInput(self, ) -> list:
        pass

    def getOutput(self, ) -> ItemStackHelper:
        pass

    def select(self, ) -> None:
        pass

    def isAvailable(self, ) -> bool:
        pass

    def getNBT(self, ) -> str:
        pass

    def getUses(self, ) -> int:
        pass

    def getMaxUses(self, ) -> int:
        pass

    def getExperience(self, ) -> int:
        pass

    def getCurrentPriceAdjustment(self, ) -> int:
        pass

    def toString(self, ) -> str:
        pass


    pass
