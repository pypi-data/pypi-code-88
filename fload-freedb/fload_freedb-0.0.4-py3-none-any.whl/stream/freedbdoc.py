from fload_freedb.stream.base import FreedbDocOperatePipeline
from ..freedb import DocumentDotExist


class FreedbDocGet(FreedbDocOperatePipeline):
    def process(self, item):
        id = item.get('id')
        if id is None:
            return None

        try:
            doc = self.col.doc(id)
            return doc
        except DocumentDotExist:
            pass
