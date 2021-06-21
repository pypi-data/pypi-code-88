from .BaseHelper import *
from .BlockPosHelper import *

class BlockDataHelper(BaseHelper, ):



    def __init__(b: BlockState, e: BlockEntity, bp: BlockPos, ):
        pass


    def getX(self, ) -> int:
        pass

    def getY(self, ) -> int:
        pass

    def getZ(self, ) -> int:
        pass

    def getId(self, ) -> str:
        pass

    def getName(self, ) -> str:
        pass

    def getNBT(self, ) -> list:
        pass

    def getBlockState(self, ) -> list:
        pass

    def getBlockPos(self, ) -> BlockPosHelper:
        pass

    def getRawBlock(self, ) -> Block:
        pass

    def getRawBlockState(self, ) -> BlockState:
        pass

    def getRawBlockEntity(self, ) -> BlockEntity:
        pass

    def toString(self, ) -> str:
        pass


    pass
