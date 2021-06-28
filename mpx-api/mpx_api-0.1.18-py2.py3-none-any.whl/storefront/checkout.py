from mpxapi.api_base import ApiBase


class Checkout(ApiBase):
    def __init__(self, api):
        ApiBase.__init__(self, api)

        self.schema = "1.4"
        self.service = "Storefront Service"
        self.path = "/web/Checkout"
