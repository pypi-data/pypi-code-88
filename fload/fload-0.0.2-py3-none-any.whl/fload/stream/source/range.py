from fload.stream import Source
import csv

class RangeSource(Source):
    field = 'x'
    _start = 1
    stop = 1
    step = 1

    def add_arguments(self, parser):
        parser.add_argument('--field', default='x')
        parser.add_argument('--start', type=int, default=0)
        parser.add_argument('--stop', type=int, default=1)
        parser.add_argument('--step', type=int, default=1)

    def init(self, ops):
        self.field = ops.field
        self._start = ops.start
        self.stop = ops.stop
        self.step = ops.step

    def start(self):
        for i in range(self._start, self.stop, self.step):
            yield {self.field: i}
