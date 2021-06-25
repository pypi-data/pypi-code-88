""" Модуль html структур

"""

import re
import typing as _T

import rlogging
from rocshelf.template.areas import CloseNodeArea
from rocshelf.template import deconstruct
from rocshelf.template.literals import CommentLiteral, Literal, LiteralValue
from rocshelf.template.main import NodesList, ProcessingParams, registration
from rocshelf.template.nodes import CommentNode, Node, ProcessingOutputNode

logger = rlogging.get_logger('mainLogger')

CONTEXT_TYPE = 'file-html'


class HtmlTagLiteral(Literal):
    """ Открывающая и закрывающая html тег структура """

    def gen_patterns(self):
        self.patterns = (
            re.compile(r'<(?P<content>(?P<tag>([\!][^\-])?[\w\-\_]+)(?P<attributes>[\s\S]*?)(\\)?)>'),
            re.compile(r'<\/(?P<content>(?P<tag>([\!][^\-])?[\w\-\_]+))>')
        )


class HtmlTagNodeArea(CloseNodeArea):
    """ Область видимости - html tag """

    @classmethod
    def arealize(cls, litValues: list[_T.Union[LiteralValue, Node]], thisIndex: int) -> _T.Optional[range]:

        callLitValue = litValues[thisIndex]

        if callLitValue.patterIndex == 1:
            return None

        logger.debug(f'Поиск закрывающего литерала для литерала "{callLitValue}"')

        startIndex = thisIndex
        stopIndex = None

        closeOpenCount = 1

        for literalIndex in range(thisIndex + 1, len(litValues)):
            litValue = litValues[literalIndex]

            if isinstance(litValue, Node):
                continue

            if litValue.literal.node != callLitValue.literal.node:
                continue

            if callLitValue.contentMath.group('tag') != litValue.contentMath.group('tag'):
                continue

            if litValue.patterIndex == 0:
                closeOpenCount += 1

            elif litValue.patterIndex == 1:
                closeOpenCount -= 1

            if closeOpenCount == 0:
                stopIndex = literalIndex
                break

        if stopIndex is None:
            return ClosingHtmlTagNode.create(callLitValue)

        startIndex += 1

        nodesList = deconstruct.Juxtaposition.juxtaposition_core(litValues[startIndex:stopIndex])

        newNode = HtmlTagNode.create(
            callLitValue, nodesList
        )

        return (
            range(startIndex, stopIndex),
            newNode
        )


tag_attributes_regex = {
    'attr_val_2': re.compile(r'\s*(?P<key>\w+)\s*=\s*"(?P<value>[^"]*)"\s*'),
    'attr_val_1': re.compile(r"\s*(?P<key>\w+)\s*=\s*'(?P<value>[^']*)'\s*"),
    'attr': re.compile(r'\s*(?P<key>[^\s]+)\s*')
}


class BaseHtmlTag(Node):
    """ Базовый класс html тегов """

    area = HtmlTagNodeArea

    @classmethod
    def literal_rule(cls):
        return HtmlTagLiteral(
            CONTEXT_TYPE, cls
        )

    __slots__ = ('tag', 'attributes')
    tag: _T.Optional[str]
    attributes: dict[str, _T.Optional[list]]

    def _deconstruct(self, litValue: LiteralValue) -> None:
        self.tag = litValue.contentMath.group('tag')
        if self.tag in ('rocshelf-tag', '_'):
            self.tag = None

        self.deconstruct_attributes(litValue.contentMath.group('attributes'))

    def _processing(self, proccParams: ProcessingParams) -> ProcessingOutputNode:
        if self.tag is None:
            self.tag = 'rocshelf-tag'

        return ProcessingOutputNode.node(self, proccParams)

    def deconstruct_attributes(self, attributesString):
        """ Зазбор строки аттрибутов """

        attributes = {}

        stringLen = -1
        while stringLen != len(attributesString):
            stringLen = len(attributesString)

            for _, regexMatch in tag_attributes_regex.items():
                attributeMatch = regexMatch.match(attributesString)
                if attributeMatch is None:
                    continue

                attributesString = attributesString[attributeMatch.end():]

                attributeMatchDict = attributeMatch.groupdict()
                attributes[attributeMatchDict['key']] = attributeMatchDict.get('value', None)
                break

        for attributeName in attributes:
            if attributes[attributeName] is not None:
                attributes[attributeName] = attributes[attributeName].split()

        self.attributes = attributes

    def compile_header(self) -> str:
        """ Компиляция открывающего тега

        Returns:
            str: Открывающий тег

        """

        header = [self.tag]

        for attribute in self.attributes:
            if self.attributes[attribute] is None:
                header.append(attribute)
            else:
                header.append('{}="{}"'.format(
                    attribute,
                    ' '.join(self.attributes[attribute])
                ))

        return '<{}>'.format(
            ' '.join(header)
        )

    def compile_footer(self) -> str:
        """ Компиляция закрывающего тега

        Returns:
            str: Закрывающий тег

        """

        return '</{}>'.format(
            self.tag
        )


class HtmlTagNode(BaseHtmlTag):
    """ Html тег требующий закрытие.

    Html тег указан.

    """

    @classmethod
    def create(cls, litValue: LiteralValue, subNodes: NodesList):
        node = cls(litValue.content, litValue.fileSpan, NodesList(subNodes))
        node.deconstruct(litValue)
        return node

    def _compile(self, proccParams: ProcessingParams) -> str:

        resultString = self.compile_header()

        for subItem in self.subNodes:
            resultString += subItem.compile(proccParams)

        resultString += self.compile_footer()

        return resultString


class ClosingHtmlTagNode(BaseHtmlTag):
    """ Html тег не требующий закрытие.

    Html тег указан.

    """

    @classmethod
    def create(cls, litValue: LiteralValue):
        node = cls(litValue.content, litValue.fileSpan)
        node.deconstruct(litValue)
        return node

    def _compile(self, proccParams: ProcessingParams) -> str:
        return self.compile_header()


class HtmlCommentLiteral(CommentLiteral):
    """ Литерал закоментированного текста для html разметки """

    def gen_patterns(self):
        self.patterns = (
            re.compile(r'<!--(?P<content>[\s\S]*?)-->'),
        )


class HtmlCommentNode(CommentNode):
    """ Нода закоментированного текста для html разметки """

    @classmethod
    def literal_rule(cls):
        return HtmlCommentLiteral(
            CONTEXT_TYPE, cls
        )


for node in [BaseHtmlTag, HtmlCommentNode]:
    registration(node)
