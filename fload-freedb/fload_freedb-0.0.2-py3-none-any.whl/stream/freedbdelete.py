from argparse import ArgumentParser
from fload_freedb.stream.base import FreedbDocOperatePipeline
import re
import os

from fload import Pipeline, base
from fload_freedb.freedb import DocumentDotExist, FreedbClient, FreedbCollection


class FreedbDeleteDoc(FreedbDocOperatePipeline):
    exist_policy: str = 'skip'
    ignore_all = False
    ignore_doc_not_exist = False

    def add_arguments(self, parser:ArgumentParser):
        super().add_arguments(parser)
        parser.add_argument('--exist', choices=['skip', 'overwrite', 'merge'], default='skip')
        parser.add_argument('--ignore-all', '-g', action='store_true', default=False, 
                            help='ignore all exception')
        parser.add_argument('--ignore-doc-not-exist', action='store_true', default=False, 
                            help='ignore doc not exist exception.')


    def init(self, ops):
        super().init(ops)
        self.exist_policy = ops.exist
        self.ignore_all = ops.ignore_all
        self.ignore_doc_not_exist = ops.ignore_doc_not_exist

    def process(self, item):
        doc_id = item.get('id')
        try:
            self.col.delete_doc(doc_id)
        except DocumentDotExist:
            if self.ignore_doc_not_exist or self.ignore_all:
                return
            raise
        except Exception:
            if self.ignore_all:
                return
            raise
