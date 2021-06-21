
class MixinMinecraftClient(Object, ):

    currentScreen: Screen = None


    def __init__():
        pass


    def onJoinWorld(self, world: ClientWorld, info: CallbackInfo, ) -> None:
        pass

    def onOpenScreen(self, screen: Screen, info: CallbackInfo, ) -> None:
        pass

    def onDisconnect(self, info: CallbackInfo, ) -> None:
        pass


    pass
