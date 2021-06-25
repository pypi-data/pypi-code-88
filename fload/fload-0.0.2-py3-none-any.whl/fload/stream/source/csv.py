from fload.stream import Source
import csv

class CSVSource(Source):
    csv_file = None

    def add_arguments(self, parser):
        parser.add_argument('csvfile')

    def init(self, ops):
        self.csv_file = ops.csvfile

    def start(self):
        input_file = csv.DictReader(open(self.csv_file))
        for row in input_file:
            yield row
