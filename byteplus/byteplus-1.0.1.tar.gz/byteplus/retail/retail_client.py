import logging
from optparse import Option

from byteplus.core.constant import MAX_WRITE_ITEM_COUNT, MAX_IMPORT_ITEM_COUNT
from byteplus.core.context import Param, Context
from byteplus.core.exception import BizException
from byteplus.core.http_caller import HttpCaller
from byteplus.retail.protocol.byteplus_retail_pb2 import *
from byteplus.retail.retail_url import _RetailURL

log = logging.getLogger(__name__)

_TOO_MANY_WRITE_ITEMS_ERR_MSG = "Only can receive %d items in one write request".format(MAX_WRITE_ITEM_COUNT)
_TOO_MANY_IMPORT_ITEMS_ERR_MSG = "Only can receive %d items in one import request".format(MAX_IMPORT_ITEM_COUNT)


class RetailClient(object):

    def __init__(self, param: Param):
        context: Context = Context(param)
        self._retail_url: _RetailURL = _RetailURL(context)
        self._http_caller: HttpCaller = HttpCaller(context)

    def write_users(self, request: WriteUsersRequest, *opts: Option) -> WriteUsersResponse:
        if len(request.users) > MAX_WRITE_ITEM_COUNT:
            raise BizException(_TOO_MANY_WRITE_ITEMS_ERR_MSG)
        url: str = self._retail_url.write_users_url
        response: WriteUsersResponse = WriteUsersResponse()
        self._http_caller.do_request(url, request, response, *opts)
        log.debug("[ByteplusSDK][WriteUsers] rsp:\n %s", response)
        return response

    def import_users(self, request: ImportUsersRequest, *opts: Option) -> OperationResponse:
        if len(request.input_config.users_inline_source.users) > MAX_IMPORT_ITEM_COUNT:
            raise BizException(_TOO_MANY_IMPORT_ITEMS_ERR_MSG)
        url: str = self._retail_url.import_users_url
        response: OperationResponse = OperationResponse()
        self._http_caller.do_request(url, request, response, *opts)
        log.debug("[ByteplusSDK][ImportUsers] rsp:\n%s", response)
        return response

    def write_products(self, request: WriteProductsRequest, *opts: Option) -> WriteProductsResponse:
        if len(request.products) > MAX_WRITE_ITEM_COUNT:
            raise BizException(_TOO_MANY_WRITE_ITEMS_ERR_MSG)
        url: str = self._retail_url.write_products_url
        response: WriteProductsResponse = WriteProductsResponse()
        self._http_caller.do_request(url, request, response, *opts)
        log.debug("[ByteplusSDK][WriteProducts] rsp:\n %s", response)
        return response

    def import_products(self, request: ImportProductsRequest, *opts: Option) -> OperationResponse:
        if len(request.input_config.products_inline_source.products) > MAX_IMPORT_ITEM_COUNT:
            raise BizException(_TOO_MANY_IMPORT_ITEMS_ERR_MSG)
        url: str = self._retail_url.import_products_url
        response: OperationResponse = OperationResponse()
        self._http_caller.do_request(url, request, response, *opts)
        log.debug("[ByteplusSDK][ImportProducts] rsp:\n%s", response)
        return response

    def write_user_events(self, request: WriteUserEventsRequest, *opts: Option) -> WriteUserEventsResponse:
        if len(request.user_events) > MAX_WRITE_ITEM_COUNT:
            raise BizException(_TOO_MANY_WRITE_ITEMS_ERR_MSG)
        url: str = self._retail_url.write_user_events_url
        response: WriteUserEventsResponse = WriteUserEventsResponse()
        self._http_caller.do_request(url, request, response, *opts)
        log.debug("[ByteplusSDK][WriteUserEvents] rsp:\n %s", response)
        return response

    def import_user_events(self, request: ImportUserEventsRequest, *opts: Option) -> OperationResponse:
        if len(request.input_config.user_events_inline_source.user_events) > MAX_IMPORT_ITEM_COUNT:
            raise BizException(_TOO_MANY_IMPORT_ITEMS_ERR_MSG)
        url: str = self._retail_url.import_user_events_url
        response: OperationResponse = OperationResponse()
        self._http_caller.do_request(url, request, response, *opts)
        log.debug("[ByteplusSDK][ImportUserEvents] rsp:\n%s", response)
        return response

    def get_operation(self, request: GetOperationRequest, *opts: Option) -> OperationResponse:
        url: str = self._retail_url.get_operation_url
        response: OperationResponse = OperationResponse()
        self._http_caller.do_request(url, request, response, *opts)
        log.debug("[ByteplusSDK][GetOperations] rsp:\n%s", response)
        return response

    def list_operations(self, request: ListOperationsRequest, *opts: Option) -> ListOperationsResponse:
        url: str = self._retail_url.list_operations_url
        response: ListOperationsResponse = ListOperationsResponse()
        self._http_caller.do_request(url, request, response, *opts)
        log.debug("[ByteplusSDK][ListOperations] rsp:\n%s", response)
        return response

    def predict(self, request: PredictRequest, scene: str, *opts: Option) -> PredictResponse:
        url_format: str = self._retail_url.predict_url_format
        url: str = url_format.replace("#", scene)
        response: PredictResponse = PredictResponse()
        self._http_caller.do_request(url, request, response, *opts)
        log.debug("[ByteplusSDK][Predict] rsp:\n%s", response)
        return response

    def ack_server_impressions(self, request: AckServerImpressionsRequest,
                               *opts: Option) -> AckServerImpressionsResponse:
        url: str = self._retail_url.ack_impression_url
        response: AckServerImpressionsResponse = AckServerImpressionsResponse()
        self._http_caller.do_request(url, request, response, *opts)
        log.debug("[ByteplusSDK][AckImpressions] rsp:\n%s", response)
        return response
