from typing import *

SEP = ';'

def formatter_csv(elems):
    return SEP.join(arg.strip() for arg in elems)

def formatter_console(elems):
    return ' '.join(elems)

class CsvWriter:

    def __init__(self, filename):
        self.f = open(filename, "w")
        self.latest_row = ''

    def on_dataset_ready(self, header_items: List[str], data_items: List[str]):
        if self.f.tell() == 0:
            self.f.write(formatter_csv(header_items) + '\n')
        self.f.write(formatter_csv(data_items) + '\n')
        self.latest_row = formatter_console(data_items)