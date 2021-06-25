import argparse
from fload import Pipeline


class LastFieldToFile(Pipeline):
    def init(self, ops):
        self.field = ops.field
        self.dest_file = ops.dest_file

    def add_arguments(self, parser:argparse.ArgumentParser):
        parser.add_argument('--field', required=True)
        parser.add_argument('--dest-file', required=True)

    def process(self, item):
        field_value = item[self.field]
        with open(self.dest_file, 'w') as f:
            f.write(field_value)
        
        return item
