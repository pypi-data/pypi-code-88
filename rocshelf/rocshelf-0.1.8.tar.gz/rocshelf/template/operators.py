""" Модуль структур. Узлы Стандартных операторов: insert, if, else, for

Предупреждение:
    Все нижеописанные структуры работают с переменными Python.
    Если при обработки ваш код выдаст исключение, то rocshelf остановит компиляцию всего приложения (кроме default insert).
    Ошибки по типу SyntaxError будут обнаружены почти сразу же,
    а ошибки вида TypeError, могут обнаружиться в самой последней структуре самого последнего файла и сломать все...

"""

import re
import typing as _T
from copy import deepcopy

import rlogging
from rcore.strpython import ReturnValue
from rocshelf import exception as ex
from rocshelf.template import areas
from rocshelf.template.literals import (InLineOptionalStructureLiteral,
                                        InTwoLineStructureLiteral,
                                        LiteralValue)
from rocshelf.template.main import NodesList, ProcessingParams, registration
from rocshelf.template.nodes import Node, ProcessingOutputNode, TextNode

logger = rlogging.get_logger('mainLogger')

allowExceptions = (NameError, )


def python_value(contextVars: dict[str, _T.Any], condition: str) -> _T.Any:
    """ Фомирование python объекта по строке и локальным переменным

    Args:
        contextVars (dict[str, _T.Any]): Доступные переменные
        condition (str): Строковое представление значения

    Raises:
        rException: Ошибка произошедшая при компиляции страницы. Обернутая в ex.ex.rException.

    Returns:
        _T.Any: Результат выполнения строки condition

    """

    logger.debug('Выполнение условия "{0}" с локальными переменными: {1}'.format(
        condition,
        contextVars
    ))

    try:
        pythonValue = ReturnValue(contextVars, condition)

    except Exception as exError:
        logger.error('Выполнение условия "{0}" выдало исключение: "{1}"'.format(
            condition,
            exError
        ))
        raise ex.ex.rException(exError)

    logger.debug('Результат выполнения условия "{0}": {1}'.format(
        condition,
        pythonValue
    ))

    return pythonValue


class BaseOperatorNode(Node):
    """ Основа всех нод - опереторов """

    area = areas.CloseNodeArea

    def _exception(self, stage: str, exError: ex.rExError) -> ex.rExError:
        if stage == 'processing':
            exError.append_traceback(
                self.fileSpan.generate_traceback()
            )
        return exError

    @classmethod
    def create(cls, litValue: LiteralValue, literals: NodesList):
        return cls(litValue.content, litValue.fileSpan, literals)

    def python_value(self, proccParams: ProcessingParams, condition: _T.Optional[str] = None) -> _T.Any:
        condition = self.callParameter if condition is None else condition
        return python_value(proccParams.localVars, condition)


class InsertNode(BaseOperatorNode):
    """ Структура вставки переменной """

    area = areas.ThisNodeArea

    @classmethod
    def literal_rule(cls):
        for point in ['i', 'insert']:
            yield InLineOptionalStructureLiteral(
                'operators', cls,
                (point, None)
            )

    __slots__ = ('defaultValue', )
    defaultValue: str

    def _deconstruct(self, defaultValue: _T.Optional[str] = None) -> None:
        self.defaultValue = defaultValue

        if self.callParameter is None:
            logger.warning('Переданный в структуру "{0}" аргумент - пустой. Структура заменится на пустую строку'.format(
                self.__class__.__name__
            ))
            self.callParameter = '""'

    @classmethod
    def create(cls, literal: LiteralValue):

        try:
            option = literal.contentMath.group('option')

        except IndexError:
            option = None

        node = cls(literal.content, literal.fileSpan)
        node.deconstruct(option)

        return node

    def _processing(self, proccParams: ProcessingParams) -> ProcessingOutputNode:
        try:
            callParameterValue = self.python_value(proccParams)
        
        except BaseException as exError:
            if self.defaultValue is None:
                raise exError

            callParameterValue = self.defaultValue

        textNode = TextNode(str(callParameterValue), self.fileSpan)
        textNode.deconstruct()

        self.subNodes = NodesList([textNode])

        return ProcessingOutputNode.from_node(self, proccParams)


class IfNode(BaseOperatorNode):
    """ Структура условия """

    @classmethod
    def literal_rule(cls):
        return InTwoLineStructureLiteral(
            'operators',
            cls,
            ('if', None),
            (None, 'if')
        )

    __slots__ = ('sections', )

    sections: dict[str, list]

    def _deconstruct(self) -> None:
        self.sections = {
            'true': [],
            'else': []
        }

        for subNode in self.subNodes:
            if isinstance(subNode, ElseNode):
                self.sections['else'].append(subNode)

            else:
                self.sections['true'].append(subNode)

    @classmethod
    def create(cls, litValue: LiteralValue, litValues: NodesList):
        node = cls(litValue.content, litValue.fileSpan, litValues)
        node.deconstruct()
        return node

    def _processing(self, proccParams: ProcessingParams) -> ProcessingOutputNode:
        callParameterValue = self.python_value(proccParams)

        if callParameterValue:
            subNodes = deepcopy(self.sections['true'])

        else:
            subNodes = deepcopy(self.sections['else'])

        self.subNodes = NodesList(subNodes)

        return ProcessingOutputNode.from_node(self, proccParams)


class ElseNode(IfNode):
    """ Структура условия else """

    @classmethod
    def literal_rule(cls):
        for point in ['else', 'elif']:
            yield InTwoLineStructureLiteral(
                'operators',
                cls,
                (point, None),
                (None, point)
            )

    def _processing(self, proccParams: ProcessingParams) -> ProcessingOutputNode:
        if self.callParameter is None:
            return ProcessingOutputNode.from_node(self, proccParams)

        return super()._processing(proccParams)


class ForNode(BaseOperatorNode):
    """ Структура цикла """

    __slots__ = ('iterableCondition', 'newVars')

    iterableCondition: str
    newVarsNames: tuple[str]

    @classmethod
    def literal_rule(cls):
        return InTwoLineStructureLiteral(
            'operators', cls,
            ('for', None),
            (None, 'for')
        )

    __slots__ = ('sections', )

    sections: dict[str, list]

    def parse_condition(self):
        """ Разбивка условия цикла на подобный python синтаксис """

        logger.debug('Выборка переменных и итерируемого значения для ноды "{0}" из строки "{1}"'.format(
            self.__class__.__name__,
            self.callParameter
        ))

        try:
            (newVarsNames, self.iterableCondition) = [i.strip() for i in self.callParameter.split('in')]
            self.newVarsNames = re.split(r',\s*', newVarsNames)

            for i in self.newVarsNames:
                if i.find(' ') != -1:
                    raise ValueError

        except ValueError as exError:
            logger.warning('Заголовок структуры "{0}" при обработки выдал исключение: "{1}"'.format(
                self.__class__.__name__,
                exError
            ))
            raise SyntaxError('For structure must follow python syntax')

        logger.debug('Результат выборки. Новые переменные {0} из итерируемой {1}'.format(
            self.newVarsNames,
            self.iterableCondition
        ))

    def _deconstruct(self) -> None:
        self.parse_condition()

        self.sections = {
            'true': [],
            'else': []
        }

        for subNode in self.subNodes:
            if isinstance(subNode, ElseNode):
                self.sections['else'].append(subNode)

            else:
                self.sections['true'].append(subNode)

    @classmethod
    def create(cls, litValue: LiteralValue, litValues: NodesList):
        node = cls(litValue.content, litValue.fileSpan, litValues)
        node.deconstruct()
        return node

    def __iterable(self, proccParams: ProcessingParams, iterVar: _T.Iterable):
        newNodesList = []

        for anyItems in iterVar:

            localVars = {}

            if len(self.newVarsNames) == 1:
                localVars[self.newVarsNames[0]] = anyItems

            else:
                for (VarName, val) in zip(self.newVarsNames, anyItems):
                    localVars[VarName] = val

            localProccParams = deepcopy(proccParams)
            localProccParams.localVars.update(localVars)

            node = Node(fileSpan=self.fileSpan)
            node.subNodes = deepcopy(self.sections['true'])
            node.proccParams = localProccParams
            newNodesList.append(node)

        self.subNodes = NodesList(newNodesList)

    def _processing(self, proccParams: ProcessingParams) -> ProcessingOutputNode:
        iterVar = self.python_value(proccParams, self.iterableCondition)

        if not iterVar:
            self.subNodes = NodesList(deepcopy(self.sections['else']))
            return ProcessingOutputNode.from_node(self, proccParams)

        if not isinstance(iterVar, _T.Iterable):
            raise ex.SyntaxTemplateError('Передаваемое в конструкцию цикла значение, должно быть итерируемым, или == False')

        self.__iterable(proccParams, iterVar)

        return ProcessingOutputNode.from_node(self, proccParams)


# Регистрация узлов, которые могут быть вызваны в шаблонах
for node in [InsertNode, IfNode, ElseNode, ForNode]:
    registration(node)
