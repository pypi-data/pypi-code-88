from heaobject import root
import enum
import locale


class DataAdapter(root.AbstractShareableHEAObject):
    def __init__(self):
        super().__init__()
        self.data_model_uri = None


class DatabaseAdapter(DataAdapter):
    def __init__(self):
        super().__init__()


class RelationalDatabaseAdapter(DatabaseAdapter):
    def __init__(self):
        super().__init__()


class FileAdapter(DataAdapter):
    def __init__(self):
        super().__init__()
        self.path = None         # Use a.out


class ExcelNotebookAdapter(FileAdapter):
    def __init__(self):
        super().__init__()


class FlatFileAdapter(FileAdapter):
    def __init__(self):
        super().__init__()
        self.header = False
        self.line_ending = None  # Use default
        self.quote_char = '"'
        self.quoting = Quoting.MINIMAL
        self.encoding = locale.getpreferredencoding()


Quoting = enum.Enum('Quoting', 'NONE MINIMAL NONNUMERIC ALL')


class DelimitedFileAdapter(FlatFileAdapter):
    def __init__(self):
        super().__init__()
        self.delimiter = '\t'


class FixedWidthFileAdapter(FlatFileAdapter):
    def __init__(self):
        super().__init__()
        self.col_specs = []  #list of tuples (start_index, length)
