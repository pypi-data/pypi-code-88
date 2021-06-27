import os
from fload_freedb.freedb import FreedbClient, FreedbCollection
from fload import Pipeline


class FreedbDocOperateMixin:
    col:FreedbCollection = None
    
    def init(self, ops):
        if ops.freedb_url:
            freedb_url = ops.freedb_url
        else:
            freedb_url = os.environ.get('FREEDB_URL', 'http://localhost:8000')

        if ops.token:
            token = ops.token
        else:
            token = os.environ.get('FREEDB_TOKEN', '')
        collection = ops.collection

        client = FreedbClient(freedb_url, token=token)
        db = client.database(ops.db)
        self.col = db.collection(collection)

    def add_arguments(self, parser):
        parser.add_argument('--freedb-url')
        parser.add_argument('--token')
        parser.add_argument('--db')
        parser.add_argument('--collection')


class FreedbDocOperatePipeline(FreedbDocOperateMixin, Pipeline):
    pass
