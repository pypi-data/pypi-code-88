# pylint: disable=useless-super-delegation

from joinnector.service.base_sdk_service import BaseSDKService


class DealService(BaseSDKService):
    def __init__(self, name):
        super().__init__(name)

    def reward(self, payload):
        return super().create(payload, "reward")

    def get_by_sku(self, sku):
        return super().get_by("sku", sku)


deal_service = DealService("deal")
