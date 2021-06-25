from service_interface_logic.market_service_logic import MarketServiceLogic
from service_interface_logic.order_service_logic import OrderServiceLogic
from service_interface_logic.wallet_service_logic import WalletServiceLogic
from service_interface_logic.user_service_logic import UserServiceLogic
from service_interface_logic.initialization_logic import InitializationLogic


class ServiceLogicContainer:

    def __init__(self):
        self.container = {}

    def register(self, serviceLogic):
        self.container[serviceLogic.Name] = serviceLogic


il = InitializationLogic()
ml = MarketServiceLogic()
ol = OrderServiceLogic()
wl = WalletServiceLogic()
ul = UserServiceLogic()

Logics = ServiceLogicContainer()
Logics.register(il)
Logics.register(ml)
Logics.register(ol)
Logics.register(wl)
Logics.register(ul)
