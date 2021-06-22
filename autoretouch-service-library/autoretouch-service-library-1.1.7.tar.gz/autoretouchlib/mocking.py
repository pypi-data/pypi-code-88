import hashlib
import json
from typing import List, Callable

from opencensus.trace.span_data import SpanData

from requests_mock import Mocker


class AiProxyMock(Mocker):
    def __init__(self, trimap, ghosting, remove_background, **kwargs):
        super().__init__(real_http=True, **kwargs)
        with open(trimap) as t, open(ghosting) as g, open(remove_background) as rb:
            self.trimap = json.load(t)
            self.ghosting = json.load(g)
            self.remove_background = json.load(rb)

    def __enter__(self):
        super().__enter__()
        self.register_uri('POST', 'http://localhost:8283/predict/', json=self.trimap)
        self.register_uri('POST', 'http://localhost:8282/predict/', json=self.ghosting)
        self.register_uri('POST', 'http://localhost:8281/predict/', json=self.remove_background)

        return self


class StorageSidecarMock(Mocker):
    def put_to_storage(self, blob: bytes, organization_id: str, content_type: str):
        content_hash = self.__create_content_hash__(blob)
        self.storage[organization_id + "/origin/" + content_hash] = bytes(blob)
        return content_hash

    def get_from_storage(self, content_hash: str, organization_id: str):
        return bytes(self.storage[organization_id + "/origin/" + content_hash])

    def __init__(self, **kwargs):
        super().__init__(real_http=True, **kwargs)

    def __enter__(self):
        super().__enter__()
        self.storage = {}
        self.register_uri('GET', 'http://localhost:8180/image/', content=self.get_image_callback)
        self.register_uri('GET', 'http://localhost:8180/blob/', content=self.get_blob_callback)
        self.register_uri('POST', 'http://localhost:8180/image/', json=self.post_image_callback)
        self.register_uri('POST', 'http://localhost:8180/blob/', json=self.post_blob_callback)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.storage.clear()

    def post_blob_callback(self, request, context):
        content_type = request.qs['content_type'].pop()
        content_hash = self.put_to_storage(
            blob=request.body, organization_id=request.qs['organization_id'].pop(), content_type=content_type)
        context.status_code = 201
        return {'contentHash': content_hash}

    def post_image_callback(self, request, context):
        content_hash = self.put_to_storage(
            blob=request.body, organization_id=self.__organization_id_from_uri__(request), content_type="image/png")
        context.status_code = 201
        return {'contentHash': content_hash}

    def get_image_callback(self, request, context):
        organization_id = self.__organization_id_from_uri__(request)
        content_hash = request.qs['content_hash'].pop()
        content = self.storage.get(organization_id + "/origin/" + content_hash)
        if content is None:
            context.status_code = 404
            context.reason = "Blob not found"
            return None
        return bytes(content)

    def get_blob_callback(self, request, context):
        organization_id = request.qs['organization_id'].pop()
        content_hash = request.qs['content_hash'].pop()
        content = self.storage.get(organization_id + "/origin/" + content_hash)
        if content is None:
            context.status_code = 404
            context.reason = "Blob not found"
            return None
        return bytes(content)

    @staticmethod
    def __organization_id_from_uri__(request):
        return request.qs['organization_id'].pop() if 'organization_id' in request.qs else request.qs[
            'company_id'].pop()

    @staticmethod
    def __create_content_hash__(image: bytes) -> str:
        m = hashlib.sha256()
        m.update(image)
        return m.hexdigest().lower()


class MockTraceExporter:
    spans: List[SpanData] = []

    def emit(self, span_datas: List[SpanData]):
        pass

    def export(self, span_datas: List[SpanData]):
        self.spans.extend(span_datas)


with_tracing_mock: Callable[[Callable], Callable] = lambda func: func
