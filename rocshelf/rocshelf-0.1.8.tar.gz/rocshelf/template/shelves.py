""" Модуль структур: Шелфы - идейный структуры rocshelf """

from __future__ import annotations

import typing as _T
from copy import copy

import rlogging
from rocshelf import exception as ex
from rocshelf.components.shelves import GetShelf, ShelfItem
from rocshelf.template import areas
from rocshelf.template import deconstruct
from rocshelf.template.file import _FileNode
from rocshelf.template.html import BaseHtmlTag, HtmlTagNode
from rocshelf.template.literals import (InLineStructureLiteral,
                                        InTwoLineStructureLiteral,
                                        LiteralValue)
from rocshelf.template.main import NodesList, ProcessingParams, registration
from rocshelf.template.nodes import (DevNode, Node, ProcessingOutputNode,
                                     StringNode, TextNode)

logger = rlogging.get_logger('mainLogger')


class ShelfNode(_FileNode):
    """ Основной класс шелф нод """

    __slots__ = ('shelfItem', 'shelfFileNodes')

    shelfItem: ShelfItem
    shelfFileNodes: NodesList

    def _deconstruct(self, shelfType: str, shelfName: str) -> None:
        self.shelfItem = GetShelf.name(shelfType, shelfName)
        self.callParameter = str(self.shelfItem)

        logger.debug('Инициализация ноды шелфа: {}'.format(
            self.shelfItem
        ))

        shelfHtmlPath = self.shelfItem.get_paths()['html']

        try:
            super()._deconstruct(shelfHtmlPath)

        except FileNotFoundError:
            self.decFile = None

    def _processing(self) -> ProcessingOutputNode:
        """ Инициализация нод шелф-файла """

        logger.debug('Обработка ноды "{0}" разобранного файла "{1}"'.format(
            self.__class__.__name__,
            self.decFile
        ))

        self.shelfFileNodes = self.get_file_nodes()

# # # # # # # #
# Shelf Page  #
# # # # # # # #


class ShelfPageNode(ShelfNode):
    """ Нода шелфа-страницы """

    def __init__(self, shelfPageName: str):
        super().__init__(None, None, None)
        self.deconstruct('page', shelfPageName)

    
    def _processing(self, proccParams: ProcessingParams) -> ProcessingOutputNode:
        super()._processing()

        self.subNodes = self.shelfFileNodes

        return ProcessingOutputNode.from_node(self, proccParams, {
            'shelves': [str(self.shelfItem)]
        })


# # # # # # # # #
# Shelf Wrapper #
# # # # # # # # #

class ShelfWrapperNode(ShelfNode):
    """ Нода шелфа-обертки """

    area = areas.AllNodeArea

    @classmethod
    def literal_rule(cls):
        for point in ['wp', 'wrapper']:
            yield InLineStructureLiteral(
                'shelves', cls,
                (point, None)
            )

    __slots__ = ('sections', )

    sections: dict[str, list]

    def _deconstruct(self, litValues: list[_T.Union[LiteralValue, Node]]) -> None:
        super()._deconstruct('wrapper', self.callParameter)

        self.sections = {
            'main': []
        }

        litValues = deconstruct.Juxtaposition.juxtaposition_core(litValues)

        for litValue in litValues:
            if isinstance(litValue, ShelfWrapperSectionNode):
                if litValue.callParameter not in self.sections:
                    self.sections[litValue.callParameter] = []

                self.sections[litValue.callParameter].append(litValue)

            else:
                self.sections['main'].append(litValue)

    @classmethod
    def create(cls, litValue: LiteralValue, litValues: NodesList):
        logger.debug('Создание "{0}" со значением имен: "{1}"'.format(
            cls.__name__,
            litValue.content
        ))

        shelfNames = litValue.content.split()

        if not shelfNames:
            raise ex.SyntaxTemplateError('Wrapper Shelf должен принимать минимум 1 параметр [имя шелфа]')

        shelfNode = cls(shelfNames[-1], litValue.fileSpan)
        shelfNode.deconstruct(litValues)

        if len(shelfNames) == 1:
            return shelfNode

        for shelfName in shelfNames[::-1][1:]:
            node = cls(shelfName, litValue.fileSpan)
            node.deconstruct(NodesList([
                shelfNode
            ]))

            shelfNode = node

        newNode = Node(litValue.content, litValue.fileSpan)
        newNode.subNodes = NodesList([
            shelfNode
        ])

        return newNode

    def __processing(self, shelfSubNodes):
        newShelfSubNodes = []

        for litValue in shelfSubNodes:
            if isinstance(litValue, ShelfWrapperPlaceNode) and litValue.callParameter in self.sections:
                newShelfSubNodes += self.sections.get(litValue.callParameter)
                continue

            elif litValue.subNodes is not None:
                litValue.subNodes = self.__processing(litValue.subNodes)

            newShelfSubNodes.append(litValue)

        return NodesList(newShelfSubNodes)

    
    def _processing(self, proccParams: ProcessingParams) -> ProcessingOutputNode:
        super()._processing()

        self.subNodes = self.shelfFileNodes
        middleProcessingNode = ProcessingOutputNode.from_node(self, proccParams)

        self.subNodes = self.__processing(middleProcessingNode.subNodes)

        processingNode = ProcessingOutputNode.from_node(self, proccParams, {
            'shelves': [str(self.shelfItem)]
        })

        processingNode.add(middleProcessingNode, False)

        return processingNode


class ShelfWrapperPlaceNode(Node):
    """ Нода места для вставки секций шелфа-обертки """

    area = areas.ThisNodeArea

    @classmethod
    def literal_rule(cls):
        for wpPoint in ['wp', 'wrapper']:
            for placePoint in ['p', 'place']:
                yield InLineStructureLiteral(
                    'shelves', cls,
                    (wpPoint, placePoint),
                )

    @classmethod
    def create(cls, litValue: LiteralValue):
        sectionName = litValue.content if litValue.content else 'main'
        return cls(sectionName, litValue.fileSpan)

    
    def _processing(self, proccParams: ProcessingParams) -> ProcessingOutputNode:
        return ProcessingOutputNode.node(self, proccParams)


class ShelfWrapperSectionNode(Node):
    """ Нода секции для шелфа-обертки """

    area = areas.CloseNodeArea

    @classmethod
    def literal_rule(cls):
        for wpPoint in ['wp', 'wrapper']:
            for sectionPoint in ['s', 'sect', 'section']:
                yield InTwoLineStructureLiteral(
                    'shelves', cls,
                    (wpPoint, sectionPoint),
                    (sectionPoint, wpPoint)
                )

    @classmethod
    def create(cls, litValue: LiteralValue, litValues: NodesList):
        sectionName = litValue.content if litValue.content else 'main'
        return cls(sectionName, litValue.fileSpan, NodesList(litValues))


# # # # # # #
# Shelf Tag #
# # # # # # #


class MergedHtmlTags(object):
    """ Класс-группировка функций для слияния двух тегов """

    __merge_attrs = ['class']

    fromTag_subTags: dict[str, ShelfSubTagNode]

    def merge(self, inTag: BaseHtmlTag, fromTag: BaseHtmlTag, fromTag_subTags: dict[str, ShelfSubTagNode]) -> BaseHtmlTag:
        """ Слияние двух html tag нод

        Args:
            inTag (BaseHtmlTag): Тег, в который будет добавлен другой тег
            fromTag (BaseHtmlTag): 'другой тег'
            fromTag_subTags (dict[str, ShelfSubTagNode]): Список под тегов из 'from' ShelfTagNode

        Returns:
            BaseHtmlTag: Новый тег

        """

        if type(inTag) != type(fromTag):
            raise ex.SyntaxTemplateError('Нельзя соединить теги разных типов ({} и {})'.format(
                str(inTag), str(fromTag)
            ))

        newTag = type(fromTag)()

        newTag.tag = self.merge_tag(inTag.tag, fromTag.tag)
        newTag.attributes = self.merge_attrs(inTag.attributes, fromTag.attributes)

        if isinstance(newTag, HtmlTagNode):
            self.fromTag_subTags = fromTag_subTags
            newTag.subNodes = self.merge_content(inTag.subNodes, fromTag.subNodes)

        return newTag

    def merge_tag(self, inTag: _T.Optional[str], fromTag: _T.Optional[str]):
        """ Слияние тегов """

        if fromTag is not None:
            return fromTag
        return inTag

    def merge_attrs(self, inAttributes: dict[str, _T.Optional[list]], fromAttributes: dict[str, _T.Optional[list]]) -> dict[str, _T.Optional[list]]:
        """ Слияние атрибутов """

        newAttributes = copy(inAttributes)

        for attributeName, attributeValue in fromAttributes.items():
            if attributeName in self.__merge_attrs:
                newAttributes[attributeName] += attributeValue
            else:
                newAttributes[attributeName] = attributeValue

        return newAttributes

    def merge_content_recursion(self, inSubNodes: NodesList, fromSubNodes: NodesList) -> NodesList:
        newNodes = []

        for node in inSubNodes:
            if isinstance(node, ShelfTagPlaceNode):
                wrapperNode = Node()
                wrapperNode.subNodes = fromSubNodes
                newNodes.append(wrapperNode)
                continue

            elif isinstance(node, ShelfSubTagNode):
                newTag = MergedHtmlTags().merge(
                    node.htmlTagNode,
                    self.fromTag_subTags[node.callParameter].htmlTagNode,
                    {}
                )
                newNodes.append(newTag)
                continue

            elif isinstance(node, ShelfTagNode):
                pass

            elif node.subNodes is not None:
                node.subNodes = self.merge_content_recursion(node.subNodes, fromSubNodes)

            newNodes.append(node)

        return NodesList(newNodes)

    def merge_content(self, inSubNodes: NodesList, fromSubNodes: NodesList) -> NodesList:
        """ Слияние наполнения тегов """

        return self.merge_content_recursion(inSubNodes, fromSubNodes)


class ShelfTagNode(ShelfNode):
    """ Нода шелфа-тега """

    area = areas.NextNodeArea

    @classmethod
    def literal_rule(cls):
        return InLineStructureLiteral(
            'shelves', cls,
            ('tag', None),
        )

    __slots__ = ('htmlTagNode', 'subTags')
    htmlTagNode: _T.Union[BaseHtmlTag, ShelfTagNode]
    subTags: dict[str, ShelfSubTagNode]

    def _deconstruct(self, nextNode: Node) -> None:
        super()._deconstruct('tag', self.callParameter)

        self.deconstruct_tag(nextNode)

        self.subTags = {}
        if isinstance(self.htmlTagNode, HtmlTagNode):
            self.htmlTagNode.subNodes = self.deconstruct_sub_tags(self.htmlTagNode.subNodes)

    def deconstruct_tag(self, nextNode: Node) -> None:
        if isinstance(nextNode, BaseHtmlTag):
            self.htmlTagNode = nextNode

        elif isinstance(nextNode, ShelfTagNode):
            htmlTagNode = DevNode('<_></_>', ['file-html']).subNodes.nodes[0]
            htmlTagNode.subNodes = NodesList([nextNode])
            self.htmlTagNode = htmlTagNode

        elif isinstance(nextNode, TextNode):
            htmlTagNode = DevNode('<_></_>', ['file-html']).subNodes.nodes[0]
            htmlTagNode.subNodes = NodesList([nextNode])
            self.htmlTagNode = htmlTagNode

        else:
            raise ex.ex.errors.DeveloperIsShitError(str(nextNode))

    def deconstruct_sub_tags(self, subNodes: NodesList):
        """ Поиск дочерних тегов """

        newNodes = []

        for node in subNodes:
            if isinstance(node, ShelfSubTagNode):
                self.subTags[node.callParameter] = node
                continue

            elif isinstance(node, ShelfTagNode):
                pass

            elif node.subNodes is not None:
                node.subNodes = self.deconstruct_sub_tags(node.subNodes)

            newNodes.append(node)

        return NodesList(newNodes)

    @classmethod
    def create(cls, litValue: LiteralValue, nextNode: Node):
        logger.debug('Создание "{0}" со значением имен: "{1}"'.format(
            cls.__name__,
            litValue.content
        ))

        shelfNames = litValue.content.split()

        if not shelfNames:
            raise ex.SyntaxTemplateError('Tag Shelf должен принимать минимум 1 параметр [имя шелфа]')

        shelfNode = cls(shelfNames[-1], litValue.fileSpan)
        shelfNode.deconstruct(nextNode)

        if len(shelfNames) == 1:
            return shelfNode

        for shelfName in shelfNames[::-1][1:]:
            subNode = cls(shelfName, litValue.fileSpan)
            subNode.deconstruct(shelfNode)

            shelfNode = subNode

        newNode = Node(litValue.content, litValue.fileSpan)
        newNode.subNodes = NodesList([
            shelfNode
        ])

        return newNode

    
    def _processing(self, proccParams: ProcessingParams) -> ProcessingOutputNode:
        super()._processing()

        targetHtmltagNode = None

        for subNode in self.shelfFileNodes:
            if isinstance(subNode, BaseHtmlTag):
                targetHtmltagNode = subNode
                break

            else:
                # Добавить провеку на коментарий или нет.
                # Если нет, то ошибка
                ...

        if targetHtmltagNode is None:
            raise ex.SyntaxTemplateError('Tag-Shelf должен содержать любой html тег')

        newHtmltagNode = self.__merge_tags(targetHtmltagNode, self)

        self.htmlTagNode = newHtmltagNode
        self.subNodes = NodesList([newHtmltagNode])

        return ProcessingOutputNode.from_node(self, proccParams, {
            'shelves': [str(self.shelfItem)]
        })

    def __merge_tags(self, inHtmlTag: BaseHtmlTag, fromTag: _T.Union[BaseHtmlTag, ShelfTagNode]) -> BaseHtmlTag:
        """ Поиск и передача тегов в класс слияния тегов

        Args:
            inHtmlTag (BaseHtmlTag): [description]
            fromTag (_T.Union[BaseHtmlTag, ShelfTagNode]): [description]

        Returns:
            BaseHtmlTag: Новый тег

        """

        if isinstance(fromTag, BaseHtmlTag):
            return MergedHtmlTags().merge(inHtmlTag, fromTag, self.subTags)

        elif isinstance(fromTag, ShelfTagNode):
            return MergedHtmlTags().merge(inHtmlTag, fromTag.htmlTagNode, fromTag.subTags)

        raise ex.ex.errors.DeveloperIsShitError(str(fromTag))


class ShelfSubTagNode(ShelfTagNode):
    """ Нода шелфа-тега """

    @classmethod
    def literal_rule(cls):
        return InLineStructureLiteral(
            'shelves', cls,
            ('t', None),
        )

    def _deconstruct(self, nextLitValue: Node) -> None:
        self.deconstruct_tag(nextLitValue)
        self.subNodes = NodesList([
            self.htmlTagNode
        ])

    
    def _processing(self, proccParams: ProcessingParams) -> ProcessingOutputNode:
        return ProcessingOutputNode.from_node(self, proccParams)


class ShelfTagPlaceNode(Node):
    """ Нода места для вставки секций шелфа-обертки """

    area = areas.ThisNodeArea

    @classmethod
    def literal_rule(cls):
        for tagPoint in ['t', 'tag']:
            for placePoint in ['p', 'place']:
                yield InLineStructureLiteral(
                    'shelves', cls,
                    (tagPoint, placePoint),
                )

    @classmethod
    def create(cls, litValue: LiteralValue):
        return cls(None, litValue.fileSpan)

    
    def _processing(self, proccParams: ProcessingParams) -> ProcessingOutputNode:
        return ProcessingOutputNode.node(self, proccParams)

    
    def _compile(self, proccParams: ProcessingParams) -> str:
        return 'ShelfTagPlaceNode'


# # # # # # # #
# Shelf Block #
# # # # # # # #


class ShelfBlockNode(ShelfNode):
    """ Нода шелфа-блока """

    area = areas.ThisNodeArea

    @classmethod
    def literal_rule(cls):
        for point in ['bl', 'block']:
            yield InLineStructureLiteral(
                'shelves', cls,
                (point, None)
            )

    def _deconstruct(self) -> None:
        super()._deconstruct('block', self.callParameter)

    @classmethod
    def create(cls, litValue: LiteralValue):
        logger.debug('Создание "{0}" со значением имен: "{1}"'.format(
            cls.__name__,
            litValue.content
        ))

        shelfNames = litValue.content.split()

        if not shelfNames:
            raise ex.SyntaxTemplateError('Tag Shelf должен принимать минимум 1 параметр [имя шелфа]')

        elif len(shelfNames) == 1:
            shelfNode = cls(shelfNames[0], litValue.fileSpan)
            shelfNode.deconstruct()
            return shelfNode

        subNodes = []

        for shelfName in shelfNames:
            node = cls(shelfName, litValue.fileSpan)
            node.deconstruct()
            subNodes.append(node)

        shelfNode = Node(litValue.content, litValue.fileSpan)
        shelfNode.subNodes = NodesList(subNodes)

        return shelfNode

    
    def _processing(self, proccParams: ProcessingParams) -> ProcessingOutputNode:
        super()._processing()

        self.subNodes = self.shelfFileNodes

        return ProcessingOutputNode.from_node(self, proccParams, {
            'shelves': [str(self.shelfItem)]
        })


for node in [ShelfWrapperNode, ShelfWrapperPlaceNode, ShelfWrapperSectionNode, ShelfTagNode, ShelfSubTagNode, ShelfTagPlaceNode, ShelfBlockNode]:
    registration(node)
