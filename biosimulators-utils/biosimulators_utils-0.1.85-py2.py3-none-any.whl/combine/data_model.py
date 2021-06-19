""" Data model for COMBINE/OMEX archives

:Author: Jonathan Karr <karr@mssm.edu>
:Date: 2020-12-06
:Copyright: 2020, Center for Reproducible Biomedical Modeling
:License: MIT
"""

from ..utils.core import are_lists_equal, none_sorted
from ..data_model import Person  # noqa: F401
import abc
import datetime  # noqa: F401
import enum

__all__ = [
    'CombineArchiveBase',
    'CombineArchive',
    'CombineArchiveContent',
    'CombineArchiveContentFormat',
    'CombineArchiveContentFormatPattern',
]


class CombineArchiveBase(abc.ABC):
    """ A COMBINE/OMEX archive

    Attributes:
        description (:obj:`str`): description
        authors (:obj:`list` of :obj:`Person`): authors
        created (:obj:`datetime.datetime`): created date
        updated (:obj:`datetime.datetime`): updated date
    """
    pass


class CombineArchive(CombineArchiveBase):
    """ A COMBINE/OMEX archive

    Attributes:
        contents (:obj:`list` of :obj:`CombineArchiveContent`): contents of the archive
        description (:obj:`str`): description
        authors (:obj:`list` of :obj:`Person`): authors
        created (:obj:`datetime.datetime`): created date
        updated (:obj:`datetime.datetime`): updated date
    """

    def __init__(self, contents=None, description=None, authors=None, created=None, updated=None):
        """
        Args:
            contents (:obj:`list` of :obj:`CombineArchiveContent`, optional): contents of the archive
            description (:obj:`str`, optional): description
            authors (:obj:`list` of :obj:`Person`, optional): authors
            created (:obj:`datetime.datetime`, optional): created date
            updated (:obj:`datetime.datetime`, optional): updated date
        """
        self.contents = contents or []
        self.description = description
        self.authors = authors or []
        self.created = created
        self.updated = updated

    def get_master_content(self):
        """ Get the master content of an archive

        Returns:
            :obj:`list` of :obj:`CombineArchiveContent`: master content
        """
        master_content = []
        for content in self.contents:
            if content.master:
                master_content.append(content)
        return master_content

    def to_tuple(self):
        """ Tuple representation of a COMBINE/OMEX archive

        Returns:
            :obj:`tuple` of :obj:`str`: tuple representation of a COMBINE/OMEX archive
        """
        contents = tuple(none_sorted(content.to_tuple() for content in self.contents))
        authors = tuple(none_sorted(author.to_tuple() for author in self.authors))
        return (contents, self.description, authors, self.created, self.updated)

    def is_equal(self, other):
        """ Determine if two content items are equal

        Args:
            other (:obj:`CombineArchiveContent`): another content item

        Returns:
            :obj:`bool`: :obj:`True`, if two archives are equal
        """
        return self.__class__ == other.__class__ \
            and are_lists_equal(self.contents, other.contents) \
            and self.description == other.description \
            and are_lists_equal(self.authors, other.authors) \
            and self.created == other.created \
            and self.updated == other.updated


class CombineArchiveContent(CombineArchiveBase):
    """ A content item (e.g., file) in a COMBINE/OMEX archive

    Attributes:
        location (:obj:`str`): path to the content
        format (:obj:`str`): URL for the specification of the format of the content
        master (:obj:`bool`): :obj:`True`, if the content is the "primary" content of the parent archive
        description (:obj:`str`): description
        authors (:obj:`list` of :obj:`Person`): authors
        created (:obj:`datetime.datetime`): created date
        updated (:obj:`datetime.datetime`): updated date
    """

    def __init__(self, location=None, format=None, master=False, description=None, authors=None, created=None, updated=None):
        """
        Args:
            location (:obj:`str`, optional): path to the content
            format (:obj:`str`, optional): URL for the specification of the format of the content
            master (:obj:`bool`, optional): :obj:`True`, if the content is the "primary" content of the parent archive
            description (:obj:`str`, optional): description
            authors (:obj:`list` of :obj:`Person`, optional): authors
            created (:obj:`datetime.datetime`, optional): created date
            updated (:obj:`datetime.datetime`, optional): updated date
        """
        self.location = location
        self.format = format
        self.master = master
        self.description = description
        self.authors = authors or []
        self.created = created
        self.updated = updated

    def to_tuple(self):
        """ Tuple representation of a content item of a COMBINE/OMEX archive

        Returns:
            :obj:`tuple` of :obj:`str`: tuple representation of a content item of a COMBINE/OMEX archive
        """
        authors = tuple(none_sorted(author.to_tuple() for author in self.authors))
        return (self.location, self.format, self.master, self.description, authors, self.created, self.updated)

    def is_equal(self, other):
        """ Determine if two content items are equal

        Args:
            other (:obj:`CombineArchiveContent`): another content item

        Returns:
            :obj:`bool`: :obj:`True`, if two content items are equal
        """
        return self.__class__ == other.__class__ \
            and self.location == other.location \
            and self.format == other.format \
            and self.master == other.master \
            and self.description == other.description \
            and are_lists_equal(self.authors, other.authors) \
            and self.created == other.created \
            and self.updated == other.updated


class CombineArchiveContentFormat(str, enum.Enum):
    """ Format for the content of COMBINE/OMEX archives """
    BNGL = 'http://purl.org/NET/mediatypes/text/bngl+plain'
    BioPAX = 'http://identifiers.org/combine.specifications/biopax'
    CellML = 'http://identifiers.org/combine.specifications/cellml'
    CopasiML = 'http://purl.org/NET/mediatypes/application/x-copasi'
    HOC = 'http://purl.org/NET/mediatypes/text/x-hoc'
    Kappa = 'http://purl.org/NET/mediatypes/text/x-kappa'
    LEMS = 'http://purl.org/NET/mediatypes/application/lems+xml'
    MorpheusML = 'http://purl.org/NET/mediatypes/application/morpheusml+xml'
    NeuroML = 'http://identifiers.org/combine.specifications/neuroml'
    OMEX = 'http://identifiers.org/combine.specifications/omex'
    OMEX_MANIFEST = 'http://identifiers.org/combine.specifications/omex-manifest'
    OMEX_METADATA = 'http://identifiers.org/combine.specifications/omex-metadata'
    pharmML = 'http://purl.org/NET/mediatypes/application/pharmml+xml'
    SBGN = 'http://identifiers.org/combine.specifications/sbgn'
    SBML = 'http://identifiers.org/combine.specifications/sbml'
    SBOL = 'http://identifiers.org/combine.specifications/sbol'
    SBOL_VISUAL = 'http://identifiers.org/combine.specifications/sbol-visual'
    SED_ML = 'http://identifiers.org/combine.specifications/sed-ml'
    Smoldyn = 'http://purl.org/NET/mediatypes/text/smoldyn+plain'
    VCML = 'http://purl.org/NET/mediatypes/application/vcml+xml'
    TEXT = 'http://purl.org/NET/mediatypes/text/plain'
    OTHER = 'http://purl.org/NET/mediatypes/application/octet-stream'


class CombineArchiveContentFormatPattern(str, enum.Enum):
    """ Format for the content of COMBINE/OMEX archives """
    BNGL = r'^https?://purl\.org/NET/mediatypes/text/bngl\+plain($|\.)'
    BioPAX = r'^https?://identifiers\.org/combine\.specifications/biopax($|\.)'
    CellML = r'^https?://identifiers\.org/combine\.specifications/cellml($|\.)'
    CopasiML = r'^https?://purl\.org/NET/mediatypes/application/x-copasi$'
    HOC = r'^https?://purl\.org/NET/mediatypes/text/x-hoc$'
    Kappa = r'^https?://purl\.org/NET/mediatypes/text/x-kappa$'
    LEMS = r'https?://purl\.org/NET/mediatypes/application/lems\+xml$'
    MorpheusML = r'https?://purl\.org/NET/mediatypes/application/morpheusml\+xml$'
    NeuroML = r'^https?://identifiers\.org/combine\.specifications/neuroml($|\.)'
    OMEX = r'https?://identifiers\.org/combine\.specifications/omex($|\.)'
    OMEX_MANIFEST = r'https?://identifiers\.org/combine\.specifications/omex-manifest($|\.)'
    OMEX_METADATA = r'https?://identifiers\.org/combine\.specifications/omex-metadata($|\.)'
    pharmML = r'^https?://purl\.org/NET/mediatypes/application/pharmml\+xml$'
    SBGN = r'^https?://identifiers\.org/combine\.specifications/sbgn($|\.)'
    SBML = r'^https?://identifiers\.org/combine\.specifications/sbml($|\.)'
    SBOL = r'^https?://identifiers\.org/combine\.specifications/sbol($|\.)'
    SBOL_VISUAL = r'^https?://identifiers\.org/combine\.specifications/sbol-visual($|\.)'
    SED_ML = r'^https?://identifiers\.org/combine\.specifications/sed\-?ml($|\.)'
    Smoldyn = r'https?://purl\.org/NET/mediatypes/text/smoldyn\+plain$'
    VCML = r'^https?://purl\.org/NET/mediatypes/application/vcml\+xml$'
    TEXT = r'^https?://purl\.org/NET/mediatypes/text/plain$'
    OTHER = r'^https?://purl\.org/NET/mediatypes/application/octet-stream$'
