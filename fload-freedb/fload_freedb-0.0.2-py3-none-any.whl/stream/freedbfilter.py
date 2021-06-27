from fload_freedb.stream.base import FreedbDocOperatePipeline
import os

from fload import Pipeline

from fload_freedb.freedb import FreedbClient, FreedbCollection, DocumentDotExist

class FreedbDocNotExistFilter(FreedbDocOperatePipeline):
    def process(self, item):
        id = item.get('id')
        if id is None:
            return item

        try:
            doc = self.col.doc(id)
            return None
        except DocumentDotExist:
            return item
