"""例外クラスの基底クラス
例外の元になる基底クラス。
"""

from typing import Optional, Union
from typing import Callable
from typing import Sequence, Iterable, List
from typing import Dict
from typing import TypeVar, Generic, NewType

# 元の例外となる型 BaseExceptionを継承
E = TypeVar('E', bound=BaseException)

class AbstractException(Exception):
    """例外の元になる基底クラス
        例外はこのクラスを継承して作成できる。
        属性にnextexを持ちこれは例外の元になった例外である。
    Attributes:
        message (str): エラーメッセージ
        nextex (:obj:Exception, optional): エラーの元になった例外
    """

    def __init__(self, message: str, nextex: Optional[E]=None) -> None:
        """コンストラクタ
        Args: 
            message (str): エラーメッセージ
            nextex  (:obj:Exception, optional): 元になった例外
        """
        self.__message: str = message
        self.__nextex = nextex

    @property
    def nextex(self) -> Optional[E]:
        """ この例外の元になった例外を返す
        Returns:
            Exception: この例外の元になった例外オブジェクト
        """
        return self.__nextex
    @nextex.setter
    def nextex(self, nextex: Optional[E]) -> None:
        """元になった例外をセットする
        Args:
            nextex (Exception): 例外オブジェクト
        """
        self.__nextex = nextex
    
    @property
    def message(self) -> str:
        """エラーメッセージを返す
        Returns:
            str: エラーメッセージ
        """
        return self.__message
    @message.setter
    def message(self, message: str) -> None:
        """例外メッセージをセットする
        Args:
            message (str): エラーメッセージ
        """
        self.__message = message

    def __str__(self) -> str:
        """このオブジェクトの文字列表現を返す
        Returns:
            str: このオブジェクトの文字列表現
        """
        ret = self.message + '\n'
        ret += str(self.nextex)
        return ret

# *でインポートする関数とクラス名
__all__ = ['AbstractException']

