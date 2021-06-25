from argparse import ArgumentParser
from fload_freedb.stream.base import FreedbDocOperateMixin
import json
import os

from fload import Source
from fload_freedb.freedb import FreedbClient, FreedbCollection


class FreedbSource(FreedbDocOperateMixin, Source):
    query: str = None
    skip: int = None

    def start(self):
        params = {}
        if self.query:
            params['query'] = json.loads(self.query)

        if self.skip:
            params['skip'] = self.skip

        for item in self.col.iter(**params):
            yield item

    def add_arguments(self, parser:ArgumentParser):
        super().add_arguments(parser)
        parser.add_argument('--query')
        parser.add_argument('--skip', type=int)
    
    def init(self, ops):
        super().init(ops)
        self.query = ops.query
        self.skip = ops.skip
    