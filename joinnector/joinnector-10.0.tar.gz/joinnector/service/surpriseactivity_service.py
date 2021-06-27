# pylint: disable=useless-super-delegation

from joinnector.service.base_sdk_service import BaseSDKService


class SurpriseActivityService(BaseSDKService):
    def __init__(self, name):
        super().__init__(name)


surpriseactivity_service = SurpriseActivityService("surpriseactivity")
