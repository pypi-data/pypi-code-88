"""Domain and utility classes.

"""
__author__ = 'Paul Landes'

from typing import Set, Dict, List
from dataclasses import dataclass, field
import logging
import sys
from itertools import chain
from datetime import datetime
from io import TextIOBase
import re
import dateparser
from zensols.config import Writable
from zensols.introspect import ClassImporter, ClassInspector, Class

logger = logging.getLogger(__name__)


@dataclass
class RegexFileParser(object):
    """Finds all instances of the citation references in a file.

    """
    REF_REGEX = re.compile(r'\{([a-zA-Z0-9,]+?)\}')
    """The default regular expression used to find citation references in sty and
    tex files (i.e. ``\\cite`` commands).

    """

    MULTI_REF_REGEX = re.compile(r'\s*,\s*')
    """The regular expression used to find comma separated lists of citations
    commands (i.e. ``\\cite``).

    """

    pattern: re.Pattern = field(default=REF_REGEX)
    """The regular expression pattern used to find the references."""

    collector: Set[str] = field(default_factory=lambda: set())
    """The set to add found references."""

    def find(self, fileobj: TextIOBase):
        for line in fileobj.readlines():
            refs = self.pattern.findall(line)
            refs = chain.from_iterable(
                map(lambda r: re.split(self.MULTI_REF_REGEX, r), refs))
            self.collector.update(refs)


@dataclass
class Converter(object):
    """A base class to convert fields of a BibTex entry (which is of type ``dict``)
    to another field.

    Subclasses should override :meth:`_convert`.

    """
    name: str = field()
    """The name of the converter, which is populated from the section name."""

    destructive: bool = field(default=False)
    """If true, remove the original field if converting from one key to another in
    the Bibtex entry.

    """

    def convert(self, entry: Dict[str, str]) -> Dict[str, str]:
        """Convert and return a new entry.

        :param entry: the source data to transform

        :return: a new instance of a ``dict`` with the transformed data
        """
        entry = dict(entry)
        self._convert(entry)
        return entry

    def _convert(self, entry: Dict[str, str]):
        """The templated method subclasses should extend.  The default base class
        implementation is to return what's given as an identity mapping.

        """
        return entry

    def __str__(self) -> str:
        return f'converter: {self.name}'


@dataclass
class ConverterLibrary(Writable):
    converter_class_names: List[str] = field()
    """The list of converter class names currently available."""

    def write(self, depth: int = 0, writer: TextIOBase = sys.stdout,
              markdown_depth: int = 1):
        for cname in self.converter_class_names:
            cls = ClassImporter(cname).get_class()
            inspector = ClassInspector(cls)
            mcls: Class = inspector.get_class()
            header = '#' * markdown_depth
            self._write_line(f'{header} Converter {cls.NAME}', depth, writer)
            writer.write('\n')
            self._write_line(mcls.doc.text, depth, writer)
            writer.write('\n\n')


@dataclass
class DateToYearConverter(Converter):
    """Converts the year part of a date field to a year.  This is useful when using
    Zotero's Better Biblatex extension that produces BibLatex formats, but you
    need BibTex entries.

    """
    NAME = 'date_year'
    """The name of the converter."""

    def _convert(self, entry: Dict[str, str]):
        if 'date' in entry:
            dt: datetime = dateparser.parse(entry['date'])
            if logger.isEnabledFor(logging.DEBUG):
                logger.debug(f"{entry['date']} -> {dt} -> {dt.year}")
            entry['year'] = str(dt.year)
            if self.destructive:
                del entry['date']


@dataclass
class CopyOrMoveConverter(Converter):
    """Copy or move one or more fields in the entry.  This is useful when your
    bibliography style expects one key, but the output (i.e.BibLatex) outputs a
    different named field).

    When :obj:``destructive`` is set to ``True``, this copy operation becomes a
    move.

    """
    NAME = 'copy'
    """The name of the converter."""

    fields: Dict[str, str] = field(default_factory=dict)
    """The source to target list of fields specifying which keys to keys get copied
    or moved.

    """

    def _convert(self, entry: Dict[str, str]):
        for src, dst in self.fields.items():
            if src in entry:
                entry[dst] = entry[src]
                if self.destructive:
                    del entry[src]
