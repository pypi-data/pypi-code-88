from argparse import ArgumentParser
from fload_freedb.stream.base import FreedbDocOperatePipeline
import re
import os

from fload_freedb.freedb import FreedbClient, FreedbCollection


class ToFreedb(FreedbDocOperatePipeline):
    exist_policy: str = 'skip'

    def add_arguments(self, parser:ArgumentParser):
        super().add_arguments(parser)
        parser.add_argument('--exist', choices=['skip', 'overwrite', 'merge'], default='skip')


    def init(self, ops):
        super().init(ops)
        self.exist_policy = ops.exist

    def process(self, item):
        doc_id = item.get('id')
        if self.exist_policy == 'skip' or not doc_id:
            return self.col.post(item)
        elif self.exist_policy == 'replace':
            return self.col.put_doc(doc_id, item)
        elif self.exist_policy == 'merge':
            return self.col.merge_doc(doc_id, item)
