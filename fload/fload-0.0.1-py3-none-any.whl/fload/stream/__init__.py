from ..base import Pipeline, Source
from .source.csv import CSVSource
from .source.range import RangeSource
from .source.imap_scan import ImapScaner
from .pipeline.last_field_to_file import LastFieldToFile
from .pipeline.filter import FilterPipeline


csv = CSVSource
last_field_to_field = LastFieldToFile
range = RangeSource
filter = FilterPipeline
imap = ImapScaner
