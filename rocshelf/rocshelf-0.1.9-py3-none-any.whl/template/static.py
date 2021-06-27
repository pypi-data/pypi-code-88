""" Модуль для описания структур, которые предназначины для файлов статики (styles, scripts) """


import re

import rlogging
from rocshelf.template import areas
from rocshelf.template.literals import (CommentLiteral,
                                        InLineStaticStructureLiteral,
                                        InTwoLineStaticStructureLiteral,
                                        LiteralValue)
from rocshelf.template.main import NodesList, ProcessingParams, registration
from rocshelf.template.nodes import (CommentNode, Node, ProcessingOutputNode,
                                     TextNode)

logger = rlogging.get_logger('mainLogger')

contextTypes = {
    'style': 'file-style',
    'sass': 'file-style-sass',
    'script': 'file-script',
}


class ImportSassFileNode(Node):
    """ Нода указать на то, что обрабатываемому файлу нужен другой файл для выполнения скриптов.

    Заменяется на относительную ссылку до того файла.

    Так же целевой файл должен быть в папе, в которой происходит компиляция статики.

    """

    area = areas.ThisNodeArea

    @classmethod
    def literal_rule(cls):
        return InLineStaticStructureLiteral(
            contextTypes['sass'], cls,
            ('import', 'sass')
        )

    def _deconstruct(self) -> None:
        targetFile = self.fileSpan.path().merge(
            self.callParameter
        )

        importNode = TextNode('@import url(\'{0}\');'.format(
            targetFile
        ))
        self.subNodes = NodesList([importNode])

    @classmethod
    def create(cls, litValue: LiteralValue):
        node = cls(litValue.content, litValue.fileSpan)
        node.deconstruct()
        return node

    
    def _processing(self, proccParams: ProcessingParams) -> ProcessingOutputNode:
        return ProcessingOutputNode.from_node(self, proccParams)


class SectionNode(Node):
    """ Нода - разделение на секции  """

    area = areas.CloseNodeArea

    @classmethod
    def literal_rule(cls):
        for context in ['style', 'script']:
            yield InTwoLineStaticStructureLiteral(
                contextTypes[context], cls,
                (cls.loadTime, None),
                (None, cls.loadTime)
            )

    __slots__ = ('loadTime', )

    loadTime: str

    @classmethod
    def create(cls, litValue: LiteralValue, litValues: NodesList):
        return cls(litValue.content, litValue.fileSpan, litValues)

    def _processing(self, proccParams: ProcessingParams) -> ProcessingOutputNode:

        if proccParams.localVars['__meta__'].loadTime != self.loadTime:
            self.subNodes = None

        return ProcessingOutputNode.from_node(self, proccParams)


class PrependSectionNode(SectionNode):
    """ Нода секции кода, которая должна загружаться в начале страницы """

    loadTime = 'prep'


class FinalSectionNode(SectionNode):
    """ Нода секции кода, которая должна загружаться в начале страницы """

    loadTime = 'final'


class StaticInLineCommentLiteral(CommentLiteral):
    """ Литерал для обозначения блока однострочного комментария в css/js разметке """

    def gen_patterns(self):
        self.patterns = (
            re.compile(r'\/\/\s*(?P<content>[^\n]*?)\n'),
            re.compile(r'\/\/\s*(?P<content>[^\n]*?)$'),
        )


class StaticMoreLineCommentLiteral(CommentLiteral):
    """ Литерал для обозначения блока многострочного комментария в css/js разметке """

    def gen_patterns(self):
        self.patterns = (
            re.compile(r'\/\*\s*(?P<content>[\s\S]*?)\s*\*\/'),
        )


class StaticCommentNode(CommentNode):
    """ Нода закоментированного текста для html разметки """

    @classmethod
    def literal_rule(cls):
        for context in ['file-style-sass', 'file-script']:
            yield StaticInLineCommentLiteral(
                context, cls
            )

        for context in ['file-style', 'file-script']:
            yield StaticMoreLineCommentLiteral(
                context, cls
            )


# Регистрация узлов, которые могут быть вызваны в шаблонах
for node in [ImportSassFileNode, PrependSectionNode, FinalSectionNode, StaticCommentNode]:
    registration(node)
