from .ItemStackHelper import *

class Inventory(Object, ):



    def create(self, ) -> self:
        pass

    def click(self, slot: int, mousebutton: int, ) -> self:
        pass

    def dragClick(self, slots: int, mousebutton: int, ) -> self:
        pass

    def getSelectedHotbarSlotIndex(self, ) -> int:
        pass

    def setSelectedHotbarSlotIndex(self, index: int, ) -> None:
        pass

    def closeAndDrop(self, ) -> self:
        pass

    def close(self, ) -> None:
        pass

    def quick(self, slot: int, ) -> self:
        pass

    def getHeld(self, ) -> ItemStackHelper:
        pass

    def getSlot(self, slot: int, ) -> ItemStackHelper:
        pass

    def getTotalSlots(self, ) -> int:
        pass

    def split(self, slot1: int, slot2: int, ) -> self:
        pass

    def grabAll(self, slot: int, ) -> self:
        pass

    def swap(self, slot1: int, slot2: int, ) -> self:
        pass

    def openGui(self, ) -> None:
        pass

    def getSlotUnderMouse(self, ) -> int:
        pass

    def getType(self, ) -> str:
        pass

    def getMap(self, ) -> list:
        pass

    def getLocation(self, slotNum: int, ) -> str:
        pass

    def getCraftableRecipes(self, ) -> list:
        pass

    def getContainerTitle(self, ) -> str:
        pass

    def getRawContainer(self, ) -> T:
        pass

    def toString(self, ) -> str:
        pass


    pass
