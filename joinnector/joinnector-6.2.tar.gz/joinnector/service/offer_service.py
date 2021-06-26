# pylint: disable=useless-super-delegation

from joinnector.service.base_sdk_service import BaseSDKService


class OfferService(BaseSDKService):
    def __init__(self, name):
        super().__init__(name)

    def redeem(self, payload):
        return super().create(payload, "redeem")

    def get_by_sku(self, sku):
        return super().get_by("sku", sku)


offer_service = OfferService("offer")
