from argparse import ArgumentParser
import re
from fload import Pipeline


class FilterPipeline(Pipeline):
    field = None
    regex = None
    value = None
    expression = None

    def add_arguments(self, parser:ArgumentParser):
        parser.add_argument('--field', required=True)
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('--value')
        group.add_argument('--regex')
        group.add_argument('--expression', '--exp')

    def init(self, ops):
        self.field = ops.field
        self.regex = ops.regex
        self.value = ops.value
        self.expression = ops.expression

    def process(self, item):
        field_value = item.get(self.field)
        if field_value is None:
            return None

        if self.regex:
            field_value = str(field_value)
            if re.search(self.regex, field_value):
                return item
            else: 
                return None
        
        if self.value is not None:
            compare_value = convert_type(self.value, type(field_value))
            if compare_value == field_value:
                return item
            else:
                return None

        
def convert_type(value, t):
    return t(value)
