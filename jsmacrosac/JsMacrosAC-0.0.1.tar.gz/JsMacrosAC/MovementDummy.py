from .PlayerInput import *

class MovementDummy(LivingEntity, ):

    coordsHistory: list = None


    def __init__(player: ClientPlayerEntity, ):
        pass


    def applyInput(self, input: PlayerInput, ) -> Vec3d:
        pass

    def method_26318(self, movementInput: Vec3d, f: float, ) -> Vec3d:
        pass

    def canMoveVoluntarily(self, ) -> bool:
        pass

    def getMainHandStack(self, ) -> ItemStack:
        pass

    def setSprinting(self, sprinting: bool, ) -> None:
        pass

    def getArmorItems(self, ) -> Iterable:
        pass

    def getEquippedStack(self, slot: EquipmentSlot, ) -> ItemStack:
        pass

    def equipStack(self, slot: EquipmentSlot, stack: ItemStack, ) -> None:
        pass

    def getMainArm(self, ) -> Arm:
        pass


    pass
