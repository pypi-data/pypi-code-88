""" Модуль описания литералов, на которые будут разбираться компилируемые строки

"""

from __future__ import annotations

import re
import typing as _T

import rlogging
from rocshelf import template

logger = rlogging.get_logger('mainLogger')

StructurePoint = tuple[_T.Union[str, None], _T.Union[str, None]]


CONTEXT_TYPES = (
    'text',
    'operators',

    'file',
    'file-html', 'shelves',
    'file-style', 'file-style-sass',
    'file-script',

    'page',
    'page-route', 'media', 'localization'
)

LITERALS: dict[str, list[Literal]] = {}

for contextType in CONTEXT_TYPES:
    LITERALS[contextType] = []


class LiteralValue(object):
    """ """

    __slots__ = ('literal', 'patterIndex', 'fileSpan', 'contentMath', 'content')

    literal: type[Literal]
    patterIndex: int
    fileSpan: template.main.FileSpan
    contentMath: re.Match
    content: str

    def __str__(self):
        return '<{0} ({1})>'.format(
            self.__class__.__name__,
            re.sub(r'\n+', ' ', self.content)
        )

    def __repr__(self) -> str:
        return '<{0} ({1}) with [{2}]>'.format(
            self.__class__.__name__,
            re.sub(r'\n+', ' ', self.content),
            repr(self.fileSpan),
        )

    def __init__(self, literal: type[Literal], patterIndex: int, fileSpan: template.main.FileSpan, contentMath: re.Match):
        self.literal = literal
        self.patterIndex = patterIndex
        self.fileSpan = fileSpan
        self.contentMath = contentMath
        self.content = self.contentMath.group('content')


class Literal(object):
    """ Правило для разбиения стороки """

    weight: int = 5

    contextType: str
    node: type[template.nodes.Node]
    patterns: tuple[re.Pattern, ...]

    def __init__(self, contextType: str, node: type[template.nodes.Node], *args, **kwargs):
        self.contextType = contextType
        self.node = node

        self.gen_patterns(*args, **kwargs)

    def gen_patterns(self, *args, **kwargs):
        """ Генерация патернов, по которым будет разбиваться строка """

        raise AttributeError('Литерал "{0}" не поддерживает генерацию патернов'.format(
            self.__class__.__name__
        ))


class TextLiteral(Literal):
    """ Правило для работы с обычным текстом """

    def gen_patterns(self):
        pass


class PatternLiteral(Literal):
    """ Правило для разбиения стороки для произвольных паттернов """

    def gen_patterns(self, pattern: re.Pattern):
        self.patterns = (
            pattern,
        )


class CommentLiteral(Literal):
    weight = 4


# # # # # # # # # #
# HTML STRUCTURES #
# # # # # # # # # #

class StructureLiteral(Literal):
    """ Правило для разбиения стороки для структур """

    def construct_re_pattern(self, structurePoint: StructurePoint) -> re.Pattern:
        """ Формирование патера для структур """

        openPoint = structurePoint[0] or ''
        closePoint = structurePoint[1] or ''

        openPointPattern = r'{{'
        if openPoint:
            openPointPattern = r'{\s*(?P<openPoint>' + openPoint + r')\s*{'

        contentPattern = r'\s*(?P<content>[\s\S]*?)\s*'

        closePointPattern = r'}}'
        if closePoint:
            closePointPattern = r'}\s*(?P<closePoint>' + closePoint + r')\s*}'

        pattern = ''.join([openPointPattern, contentPattern, closePointPattern])

        logger.debug(f'Формирование паттерна структуры для пойнтов: "{structurePoint}" -> "{pattern}"')

        return re.compile(pattern)

    def construct_optional_re_pattern(self, structurePoint: StructurePoint) -> re.Pattern:
        """ Формирование патера для структур с возможностью опционации """

        closePoint = r'(\s*{\s*(?P<option>[\S ]*?)\s*}\s*)?'

        return self.construct_re_pattern((
            structurePoint[0], closePoint
        ))


class InLineStructureLiteral(StructureLiteral):
    """ Правило для разбиения стороки для структур """

    def gen_patterns(self, structurePoint: StructurePoint):
        self.patterns = (
            self.construct_re_pattern(structurePoint),
        )


class InLineOptionalStructureLiteral(StructureLiteral):
    """ Одностроковая структура. Вторая часть которой является доп параметром """

    def gen_patterns(self, structurePoint: StructurePoint):
        if structurePoint[1] is not None:
            ValueError('Литерал {0} подразумевает пустой закрывающий пойнт'.format(
                self.__class__.__name__
            ))

        self.patterns = (
            self.construct_optional_re_pattern(structurePoint),
        )


class InTwoLineStructureLiteral(StructureLiteral):
    """ Правило для разбиения стороки для структур """

    openPoint: StructurePoint
    closePoint: StructurePoint

    def gen_patterns(self, openPoint: StructurePoint, closePoint: StructurePoint):
        self.patterns = (
            self.construct_re_pattern(openPoint),
            self.construct_re_pattern(closePoint)
        )


# # # # # # # # # # # # # #
# STATIC FILES STRUCTURES #
# # # # # # # # # # # # # #


class StaticStructureLiteral(StructureLiteral):
    """ Правило для разбиения стороки для структур """

    def construct_re_pattern(self, structurePoint: StructurePoint) -> re.Pattern:
        """ Формирование патера для структур """

        pattern = super().construct_re_pattern(structurePoint)
        stringPattern = pattern.pattern

        newPattern = r'\/\/\s*{}'.format(
            stringPattern
        )

        return re.compile(newPattern)


class InLineStaticStructureLiteral(InLineStructureLiteral, StaticStructureLiteral):
    """ Правило для разбиения стороки для структур """

    def gen_patterns(self, structurePoint: StructurePoint):
        self.patterns = (
            self.construct_re_pattern(structurePoint),
        )


class InLineOptionalStaticStructureLiteral(InLineOptionalStructureLiteral, StaticStructureLiteral):
    """ Одностроковая структура. Вторая часть которой является доп параметром """

    def gen_patterns(self, structurePoint: StructurePoint):
        if structurePoint[1] is not None:
            ValueError('Литерал {0} подразумевает пустой закрывающий пойнт'.format(
                self.__class__.__name__
            ))

        self.patterns = (
            self.construct_optional_re_pattern(structurePoint),
        )


class InTwoLineStaticStructureLiteral(InTwoLineStructureLiteral, StaticStructureLiteral):
    """ Правило для разбиения стороки для структур """

    openPoint: StructurePoint
    closePoint: StructurePoint

    def gen_patterns(self, openPoint: StructurePoint, closePoint: StructurePoint):
        self.patterns = (
            self.construct_re_pattern(openPoint),
            self.construct_re_pattern(closePoint)
        )
