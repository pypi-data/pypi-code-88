# -*- coding: utf-8 -*-

from mod.server.component.effectCompServer import EffectComponentServer
from mod.server.component.actorMotionCompServer import ActorMotionComponentServer
from mod.server.component.engineTypeCompServer import EngineTypeComponentServer
from mod.server.component.rideCompServer import RideCompServer
from mod.server.component.blockInfoCompServer import BlockInfoComponentServer
from mod.server.component.gameCompServer import GameComponentServer
from typing import Union
from mod.server.component.actorPushableCompServer import ActorPushableCompServer
from mod.server.component.bulletAttributesCompServer import BulletAttributesComponentServer
from mod.server.component.timeCompServer import TimeComponentServer
from mod.server.component.portalCompServer import PortalComponentServer
from mod.server.component.blockCompServer import BlockCompServer
from mod.server.component.projectileCompServer import ProjectileComponentServer
from mod.server.component.scaleCompServer import ScaleComponentServer
from mod.server.component.attrCompServer import AttrCompServer
from mod.server.component.gravityCompServer import GravityComponentServer
from mod.server.component.itemCompServer import ItemCompServer
from mod.server.component.featureCompServer import FeatureCompServer
from mod.server.component.itemBannedCompServer import ItemBannedCompServer
from mod.server.component.breathCompServer import BreathCompServer
from mod.server.component.controlAiCompServer import ControlAiCompServer
from mod.server.component.actorLootCompServer import ActorLootComponentServer
from mod.server.component.exDataCompServer import ExDataCompServer
from mod.server.component.playerCompServer import PlayerCompServer
from mod.server.component.msgCompServer import MsgComponentServer
from mod.server.component.posCompServer import PosComponentServer
from mod.server.component.petCompServer import PetComponentServer
from mod.server.component.expCompServer import ExpComponentServer
from mod.server.component.flyCompServer import FlyComponentServer
from mod.server.component.nameCompServer import NameComponentServer
from mod.server.component.commandCompServer import CommandCompServer
from mod.server.component.dimensionCompServer import DimensionCompServer
from mod.server.component.hurtCompServer import HurtCompServer
from mod.server.component.mobSpawnCompServer import MobSpawnComponentServer
from mod.server.component.moveToCompServer import MoveToComponentServer
from mod.server.component.recipeCompServer import RecipeCompServer
from mod.server.component.levelCompServer import LevelComponentServer
from mod.server.component.persistenceCompServer import PersistenceCompServer
from mod.server.component.weatherCompServer import WeatherComponentServer
from mod.server.component.auxValueCompServer import AuxValueComponentServer
from mod.server.component.chunkSourceComp import ChunkSourceCompServer
from mod.server.component.biomeCompServer import BiomeCompServer
from mod.server.component.chestContainerCompServer import ChestContainerCompServer
from mod.server.component.tameCompServer import TameComponentServer
from mod.server.component.entityEventCompServer import EntityEventComponentServer
from mod.server.component.blockEntityExDataCompServer import BlockEntityExDataCompServer
from mod.server.component.blockStateCompServer import BlockStateComponentServer
from mod.server.component.actorOwnerCompServer import ActorOwnerComponentServer
from mod.server.component.collisionBoxCompServer import CollisionBoxComponentServer
from mod.server.component.redStoneCompServer import RedStoneComponentServer
from mod.server.component.modAttrCompServer import ModAttrComponentServer
from mod.server.component.rotCompServer import RotComponentServer
from mod.server.component.modelCompServer import ModelComponentServer
from mod.server.component.blockUseEventWhiteListCompServer import BlockUseEventWhiteListComponentServer
from mod.server.component.explosionCompServer import ExplosionComponentServer
from mod.server.component.actionCompServer import ActionCompServer

class EngineCompFactoryServer(object):
    def CreateAction(self, entityId):
        # type: (Union[str,int]) -> ActionCompServer
        """
        创建action组件
        """

    def CreateActorLoot(self, entityId):
        # type: (Union[str,int]) -> ActorLootComponentServer
        """
        创建actorLoot组件
        """

    def CreateActorMotion(self, entityId):
        # type: (Union[str,int]) -> ActorMotionComponentServer
        """
        创建actorMotion组件
        """

    def CreateActorOwner(self, entityId):
        # type: (Union[str,int]) -> ActorOwnerComponentServer
        """
        创建actorOwner组件
        """

    def CreateActorPushable(self, entityId):
        # type: (Union[str,int]) -> ActorPushableCompServer
        """
        创建actorPushable组件
        """

    def CreateAttr(self, entityId):
        # type: (Union[str,int]) -> AttrCompServer
        """
        创建attr组件
        """

    def CreateAuxValue(self, entityId):
        # type: (Union[str,int]) -> AuxValueComponentServer
        """
        创建auxValue组件
        """

    def CreateBiome(self, entityId):
        # type: (Union[str,int]) -> BiomeCompServer
        """
        创建biome组件
        """

    def CreateBlock(self, entityId):
        # type: (Union[str,int]) -> BlockCompServer
        """
        创建block组件
        """

    def CreateBlockEntityData(self, entityId):
        # type: (Union[str,int]) -> BlockEntityExDataCompServer
        """
        创建blockEntityData组件
        """

    def CreateBlockInfo(self, entityId):
        # type: (Union[str,int]) -> BlockInfoComponentServer
        """
        创建blockInfo组件
        """

    def CreateBlockState(self, entityId):
        # type: (Union[str,int]) -> BlockStateComponentServer
        """
        创建blockState组件
        """

    def CreateBlockUseEventWhiteList(self, entityId):
        # type: (Union[str,int]) -> BlockUseEventWhiteListComponentServer
        """
        创建blockUseEventWhiteList组件
        """

    def CreateBreath(self, entityId):
        # type: (Union[str,int]) -> BreathCompServer
        """
        创建breath组件
        """

    def CreateBulletAttributes(self, entityId):
        # type: (Union[str,int]) -> BulletAttributesComponentServer
        """
        创建bulletAttributes组件
        """

    def CreateChestBlock(self, entityId):
        # type: (Union[str,int]) -> ChestContainerCompServer
        """
        创建chestBlock组件
        """

    def CreateChunkSource(self, entityId):
        # type: (Union[str,int]) -> ChunkSourceCompServer
        """
        创建chunkSource组件
        """

    def CreateCollisionBox(self, entityId):
        # type: (Union[str,int]) -> CollisionBoxComponentServer
        """
        创建collisionBox组件
        """

    def CreateCommand(self, entityId):
        # type: (Union[str,int]) -> CommandCompServer
        """
        创建command组件
        """

    def CreateControlAi(self, entityId):
        # type: (Union[str,int]) -> ControlAiCompServer
        """
        创建controlAi组件
        """

    def CreateDimension(self, entityId):
        # type: (Union[str,int]) -> DimensionCompServer
        """
        创建dimension组件
        """

    def CreateEffect(self, entityId):
        # type: (Union[str,int]) -> EffectComponentServer
        """
        创建effect组件
        """

    def CreateEngineType(self, entityId):
        # type: (Union[str,int]) -> EngineTypeComponentServer
        """
        创建engineType组件
        """

    def CreateEntityEvent(self, entityId):
        # type: (Union[str,int]) -> EntityEventComponentServer
        """
        创建entityEvent组件
        """

    def CreateExp(self, entityId):
        # type: (Union[str,int]) -> ExpComponentServer
        """
        创建exp组件
        """

    def CreateExplosion(self, entityId):
        # type: (Union[str,int]) -> ExplosionComponentServer
        """
        创建explosion组件
        """

    def CreateExtraData(self, entityId):
        # type: (Union[str,int]) -> ExDataCompServer
        """
        创建extraData组件
        """

    def CreateFeature(self, entityId):
        # type: (Union[str,int]) -> FeatureCompServer
        """
        创建feature组件
        """

    def CreateFly(self, entityId):
        # type: (Union[str,int]) -> FlyComponentServer
        """
        创建fly组件
        """

    def CreateGame(self, entityId):
        # type: (Union[str,int]) -> GameComponentServer
        """
        创建game组件
        """

    def CreateGravity(self, entityId):
        # type: (Union[str,int]) -> GravityComponentServer
        """
        创建gravity组件
        """

    def CreateHurt(self, entityId):
        # type: (Union[str,int]) -> HurtCompServer
        """
        创建hurt组件
        """

    def CreateItem(self, entityId):
        # type: (Union[str,int]) -> ItemCompServer
        """
        创建item组件
        """

    def CreateItemBanned(self, entityId):
        # type: (Union[str,int]) -> ItemBannedCompServer
        """
        创建itembanned组件
        """

    def CreateLv(self, entityId):
        # type: (Union[str,int]) -> LevelComponentServer
        """
        创建lv组件
        """

    def CreateMobSpawn(self, entityId):
        # type: (Union[str,int]) -> MobSpawnComponentServer
        """
        创建mobSpawn组件
        """

    def CreateModAttr(self, entityId):
        # type: (Union[str,int]) -> ModAttrComponentServer
        """
        创建modAttr组件
        """

    def CreateModel(self, entityId):
        # type: (Union[str,int]) -> ModelComponentServer
        """
        创建model组件
        """

    def CreateMoveTo(self, entityId):
        # type: (Union[str,int]) -> MoveToComponentServer
        """
        创建moveTo组件
        """

    def CreateMsg(self, entityId):
        # type: (Union[str,int]) -> MsgComponentServer
        """
        创建msg组件
        """

    def CreateName(self, entityId):
        # type: (Union[str,int]) -> NameComponentServer
        """
        创建name组件
        """

    def CreatePersistence(self, entityId):
        # type: (Union[str,int]) -> PersistenceCompServer
        """
        创建persistence组件
        """

    def CreatePet(self, entityId):
        # type: (Union[str,int]) -> PetComponentServer
        """
        创建pet组件
        """

    def CreatePlayer(self, entityId):
        # type: (Union[str,int]) -> PlayerCompServer
        """
        创建player组件
        """

    def CreatePortal(self, entityId):
        # type: (Union[str,int]) -> PortalComponentServer
        """
        创建portal组件
        """

    def CreatePos(self, entityId):
        # type: (Union[str,int]) -> PosComponentServer
        """
        创建pos组件
        """

    def CreateProjectile(self, entityId):
        # type: (Union[str,int]) -> ProjectileComponentServer
        """
        创建projectile组件
        """

    def CreateRecipe(self, entityId):
        # type: (Union[str,int]) -> RecipeCompServer
        """
        创建recipe组件
        """

    def CreateRedStone(self, entityId):
        # type: (Union[str,int]) -> RedStoneComponentServer
        """
        创建redStone组件
        """

    def CreateRide(self, entityId):
        # type: (Union[str,int]) -> RideCompServer
        """
        创建ride组件
        """

    def CreateRot(self, entityId):
        # type: (Union[str,int]) -> RotComponentServer
        """
        创建rot组件
        """

    def CreateScale(self, entityId):
        # type: (Union[str,int]) -> ScaleComponentServer
        """
        创建scale组件
        """

    def CreateTame(self, entityId):
        # type: (Union[str,int]) -> TameComponentServer
        """
        创建tame组件
        """

    def CreateTime(self, entityId):
        # type: (Union[str,int]) -> TimeComponentServer
        """
        创建time组件
        """

    def CreateWeather(self, entityId):
        # type: (Union[str,int]) -> WeatherComponentServer
        """
        创建weather组件
        """

