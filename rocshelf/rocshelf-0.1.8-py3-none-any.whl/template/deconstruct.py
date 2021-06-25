""" Модуль для предварительной обработки текста """

from __future__ import annotations

import re
import typing as _T
from pprint import pprint

import rlogging
from rcore.utils import short_text, split_list_by_indexes
from rocshelf import exception as ex
from rocshelf import template

logger = rlogging.get_logger('mainLogger')

textNodeLiteral: _T.Optional[template.literals.TextLiteral] = None


class LiteralMask(object):
    """ Маска некого совпадения с литералами """

    isEmpty: bool

    literal: template.literals.Literal
    patternIndex: int
    position: tuple[int, int]

    def __init__(self):
        self.isEmpty = True

    def check(self, literal: template.literals.Literal, patternIndex: int, math: re.Match):
        """ Сравнение совпадения сохраненного в маске с новым

        Args:
            literal (template.literals.Literal): Литерал, по которому нашлось совпадение
            patternIndex (int): Индекс паттерна из литреала
            math (re.Match): Результат совпадения

        Raises:
            ex.ex.errors.DeveloperIsShitError: Я где то накосячил

        """

        position = math.span()

        def update():
            self.literal = literal
            self.patternIndex = patternIndex
            self.position = position
            self.math = math

        if self.isEmpty:
            self.isEmpty = False
            update()
            return

        if self.position[0] > position[0]:
            update()

        elif self.position[0] == position[0] and self.position[1] > position[1]:
            update()

        elif self.position[0] == position[0] and self.position[1] == position[1] and self.literal.weight < literal.weight:
            update()

        elif self.position[0] == position[0] and self.position[1] == position[1] and self.literal.weight == literal.weight:
            pprint([
                (self.literal, self.math),
                (literal, math)
            ])
            raise ex.ex.errors.DeveloperIsShitError('print')

    def literal_value(self, onFileId: _T.Union[int, None]) -> template.literals.LiteralValue:
        """ Формированеи Значения литерала сохраненного в маске

        Args:
            onFileId (_T.Union[int, None]): Идентификатор файла в котором найдено совпадение

        Returns:
            template.literals.LiteralValue: Объект значения литерала

        """

        return template.literals.LiteralValue(
            self.literal,
            self.patternIndex,
            template.main.FileSpan(onFileId, self.position),
            self.math
        )

    @staticmethod
    def text_literal(string: str, onFileId: _T.Union[int, None], position: tuple[int, int]):
        """ Формирование литерала """

        global textNodeLiteral
        if textNodeLiteral is None:
            textNodeLiteral = template.nodes.TextNode.literal_rule()

        # 50/50
        string = re.sub(r'^\s+|\s+$', ' ', string)
        if string == ' ':
            string = ''

        return template.literals.LiteralValue(
            textNodeLiteral,
            0,
            template.main.FileSpan(onFileId, position),
            re.search(r'(?P<content>[\s\S]*)', string)
        )


class Explore(object):
    """ Класс разбиения строки на составляющие литералы """

    string: str
    onFileId: _T.Optional[int]
    contextsList: list[str]

    def __init__(self, string: str, onFileId: _T.Optional[int] = None, contextsList: list[str] = None):
        logger.debug('Инициализация класса разбиения строки на литералы')

        self.string = string
        self.onFileId = onFileId
        self.contextsList = contextsList

    def explore_core(self, string: str, onFileId: _T.Union[int, None] = None, contextsList: list[str] = []) -> list[template.nodes.Node]:
        """ Разбор строки на составляющие литералы """

        literalsList = []

        textPointer = 0
        textLength = len(string)

        while string:

            match = LiteralMask()

            for contextType in contextsList:
                for literal in template.literals.LITERALS[contextType]:

                    # Вставить разделение на файлы
                    for patternIndex in range(len(literal.patterns)):
                        pattern = literal.patterns[patternIndex]

                        newMatch = pattern.search(string)

                        if newMatch:
                            match.check(literal, patternIndex, newMatch)

            if match.isEmpty:
                literalsList.append(
                    LiteralMask.text_literal(
                        string, onFileId, (textPointer, textLength)
                    )
                )
                string = None

            else:
                if match.position[0] != 0:
                    preString = string[:match.position[0]]
                    literalsList.append(
                        LiteralMask.text_literal(
                            preString, onFileId, (textPointer, match.position[0])
                        )
                    )

                literalsList.append(
                    match.literal_value(onFileId)
                )
                string = string[(match.position[1]):]

        # В конец всех обработаных сток/файлов добавляется нода текста,
        # Чтобы адаптироваться случайные обработки (исключить возможность появления других нод в конце списка)
        literalsList.append(
            LiteralMask.text_literal('', None, (-1, -1))
        )

        return literalsList

    def explore(self) -> template.main.NodesList:
        logger.debug('Разбиение строки: "{0}" файла с идентификатором {1} и списком контекста: "{2}"'.format(
            short_text(self.string),
            self.onFileId,
            self.contextsList
        ))

        if self.contextsList is None:
            raise ValueError('Deconstruct need contexts list')

        nodesList = template.main.NodesList(
            self.explore_core(self.string, self.onFileId, self.contextsList)
        )

        logger.debug('Результат состоит из {0} литералов: {1}'.format(
            len(nodesList),
            nodesList
        ))

        return nodesList


class Juxtaposition(object):
    """ Класс анализа литералов и создание нод на их основе """

    litValues: template.main.NodesList

    def __init__(self, litValues: template.main.NodesList):
        logger.debug('Инициализация класса анализа литералов')

        self.litValues = litValues

    @staticmethod
    def juxtaposition_core(litValues: list[_T.Union[template.literals.LiteralValue, template.nodes.Node]]):

        newLiterals = []

        literalsLength = len(litValues)

        for litValueIndex in range(literalsLength):
            litValue = litValues[litValueIndex]

            logger.debug('Сопоставление литерала "{0}"'.format(
                litValue
            ))

            if isinstance(litValue, template.nodes.Node):
                newLiterals.append(litValue)
                continue

            node = litValue.literal.node

            arealizeResult = node.area.arealize(litValues, litValueIndex)

            if arealizeResult is None:
                continue

            elif isinstance(arealizeResult, tuple):
                if isinstance(arealizeResult[0], range) and isinstance(arealizeResult[1], template.nodes.Node):
                    _, _, postLitValue = split_list_by_indexes(litValues, [arealizeResult[0].start, arealizeResult[0].stop])

                    newLiterals.append(arealizeResult[1])
                    newLiterals += postLitValue

                    return Juxtaposition.juxtaposition_core(newLiterals)

                else:
                    print(arealizeResult, type(arealizeResult))
                    raise ex.ex.errors.DeveloperIsShitError()

            elif isinstance(arealizeResult, template.nodes.Node):
                newLiterals.append(arealizeResult)

            elif isinstance(arealizeResult, int) and litValueIndex == arealizeResult:
                newLiterals.append(
                    node.create(litValue)
                )

            elif isinstance(arealizeResult, int) and arealizeResult == -1:
                return [
                    node.create(litValue, newLiterals + litValues[litValueIndex + 1:])
                ]

            elif isinstance(arealizeResult, range):

                _, nowLitValue, postLitValue = split_list_by_indexes(litValues, [arealizeResult.start, arealizeResult.stop])

                nowLitValue = Juxtaposition.juxtaposition_core(nowLitValue)

                newLiterals.append(
                    node.create(
                        litValue,
                        nowLitValue
                    )
                )
                newLiterals += postLitValue

                return Juxtaposition.juxtaposition_core(newLiterals)

            elif isinstance(arealizeResult, template.main.NodesList):
                return Juxtaposition.juxtaposition_core(arealizeResult.nodes)

            else:
                print(arealizeResult, type(arealizeResult))
                raise ex.ex.errors.DeveloperIsShitError('qwerty')

        return newLiterals

    def juxtaposition(self) -> template.main.NodesList:
        logger.debug('Анализ литералов: {0}'.format(
            self.litValues
        ))

        newLiterals = Juxtaposition.juxtaposition_core(
            self.litValues.nodes
        )

        return template.main.NodesList(newLiterals)


def explore(string: str, onFileId: _T.Optional[int], contextsList: list[str]):
    return Explore(string, onFileId, contextsList).explore()


def juxtaposition(string: str, onFileId: _T.Optional[int], contextsList: list[str]):
    return Juxtaposition(string, onFileId, contextsList).juxtaposition()


def deconstruct(string: str, onFileId: _T.Optional[int], contextsList: list[str]):
    litValuesList = Explore(string, onFileId, contextsList).explore()
    return Juxtaposition(litValuesList).juxtaposition()
