from . import crawler_data_service_pb2_grpc as importStub

class DataServiceService(object):

    def __init__(self, router):
        self.connector = router.get_connection(DataServiceService, importStub.DataServiceStub)

    def crawlerConnect(self, request, timeout=None):
        return self.connector.create_request('crawlerConnect', request, timeout)

    def sendEvent(self, request, timeout=None):
        return self.connector.create_request('sendEvent', request, timeout)

    def sendMessage(self, request, timeout=None):
        return self.connector.create_request('sendMessage', request, timeout)