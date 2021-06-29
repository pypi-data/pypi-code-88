"""Extract BibTex references from a Tex file and add them from a master BibTex
file.

"""
__author__ = 'plandes'

from typing import List, Dict, Tuple
from dataclasses import dataclass, field
import sys
import logging
import re
from pathlib import Path
from io import TextIOWrapper
import bibtexparser
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bparser import BibTexParser
from zensols.persist import persisted
from zensols.config import ConfigFactory
from . import RegexFileParser, Converter

logger = logging.getLogger(__name__)


@dataclass
class Extractor(object):
    """Extracts references, parses the BibTex master source file, and extracts
    matching references from the LaTex file.

    """
    TEX_FILE_REGEX = re.compile(r'.+\.(?:tex|sty|cls)$')

    config_factory: ConfigFactory = field()
    """The configuration factory used to create the converters."""

    master_bib: Path = field()
    """The path to the master BibTex file."""

    texpath: Path = field(default=None)
    """Either a file or directory to recursively scan for files with LaTex citation
    references.

    """

    converter_names: List[str] = field(default=None)
    """A list of converter names used to convert to BibTex entries."""

    def __post_init__(self):
        self.converter_names = list(filter(
            lambda x: x != 'identity', self.converter_names))

    @property
    @persisted('_converters')
    def converters(self) -> Tuple[Converter]:
        fac = self.config_factory
        return tuple(map(lambda n: fac.new_instance(f'{n}_converter'),
                         self.converter_names))

    @property
    @persisted('_database')
    def database(self) -> BibDatabase:
        """Return the BibTex Python object representation of master file.

        """
        logger.info(f'parsing master bibtex file: {self.master_bib}')
        parser = BibTexParser()
        parser.ignore_nonstandard_types = False
        with open(self.master_bib) as f:
            return bibtexparser.load(f, parser)

    @property
    def bibtex_ids(self) -> iter:
        """Return all BibTex string IDs.  These could be BetterBibtex citation
        references.

        """
        return map(lambda e: e['ID'], self.database.entries)

    def _is_tex_file(self, path: Path) -> bool:
        """Return whether or not path is a file that might contain citation references.

        """
        return path.is_file() and \
            self.TEX_FILE_REGEX.match(path.name) is not None

    @property
    def tex_refs(self) -> set:
        """Return the set of parsed citation references.

        """
        parser = RegexFileParser()
        path = self.texpath
        logger.info(f'parsing references from Tex file: {path}')
        if path.is_file():
            paths = (path,)
        elif path.is_dir():
            paths = tuple(filter(self._is_tex_file, path.rglob('*')))
        logger.debug(f'parsing references from Tex files: {paths}')
        for path in paths:
            with open(path) as f:
                parser.find(f)
        return parser.collector

    @property
    def extract_ids(self) -> set:
        """Return the set of BibTex references to be extracted.

        """
        bib = set(self.bibtex_ids)
        trefs = self.tex_refs
        return bib & trefs

    def print_bibtex_ids(self):
        logging.getLogger('bibtexparser').setLevel(logging.ERROR)
        for id in self.bibtex_ids:
            print(id)

    def print_texfile_refs(self):
        for ref in self.tex_refs:
            print(ref)

    def print_extracted_ids(self):
        for id in self.extract_ids:
            print(id)

    @property
    @persisted('_entries')
    def entries(self) -> Dict[str, Dict[str, str]]:
        """The BibTex entries parsed from the master bib file."""
        db = self.database.get_entry_dict()
        entries = {}
        for did in sorted(self.extract_ids):
            entry = db[did]
            for conv in self.converters:
                if logger.isEnabledFor(logging.DEBUG):
                    logger.debug(f'applying {conv}')
                entry = conv.convert(entry)
            entries[did] = entry
        return entries

    def extract(self, writer: TextIOWrapper = sys.stdout):
        """Extract the master source BibTex matching citation references from the LaTex
        file(s) and write them to ``writer``.

        :param writer: the BibTex entry data sink

        """
        bwriter = BibTexWriter()
        for bid, entry in self.entries.items():
            logger.info(f'writing entry {bid}')
            writer.write(bwriter._entry_to_bibtex(entry))
            logger.debug(f'extracting: {bid}: <{entry}>')
        writer.flush()
