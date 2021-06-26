"""Pythonのユーティリティモジュール
    Pythonの一般的な文字列などの便利な関数を集めたモジュール。
    いまのところ文字列やhashの操作の関数がある。

"""
from typing import Optional, Union, Any
from typing import Callable, NoReturn
from typing import Sequence, Iterable, List, Tuple
from typing import Dict
from typing import TypeVar, Generic, NewType, Type


import hashlib
from chardet import UniversalDetector
import requests

MAX_UNSIGNED_INT = 4294967295
""" int: 4バイト unsigned intの最大値を表す整数
hashint()関数で最大値を指定するとき使用する。
"""

MAX_UNSIGNED_LONG = 18446744073709551615
""" int: 8バイト unsigned longの最大値を表す整数
hashint()関数で最大値を指定するとき使用する。
"""

def hashint(byte_content: bytes, max_range: int=MAX_UNSIGNED_INT) -> int:
    """バイトコンテントから４バイトの整数のハッシュ値を生成して返す。
    ハッシュはSHA256を使用。
    引数でハッシュ値の範囲を指定できる。指定できない場合は４バイト(32ビット)。
    
    Args:
        byte_content (bytes): バイトデーター
        max_range (:obj:`int`, optional) 生成されるハッシュ値の最大値
                                         MAX_UNSIGNED_INT(32ビットの最大値)か
                                         MAX_UNSIGNED_LONG(64ビットの最大値)を指定できる。
    Returns:
        int: 整数のハッシュ値
             max_rangeで指定した最大値までの整数。
    """
    ret = 1
    sha = hashlib.sha256()
    sha.update(byte_content)
    hashval = sha.hexdigest()
    for ch in hashval:
        val = ord(ch)
        ret = ret + val
    ret = ret * 1234567
    return ret % max_range

def hashint64(byte_content: bytes) -> int:
    """バイトコンテントから8バイトの整数のハッシュ値を生成して返す。
    
    Args: 
        byte_content (bytes): バイトデーター
    Returns:
        int: 8バイトのハッシュの整数値
    """
    return hashint(byte_content, MAX_UNSIGNED_LONG)

def seq_split(seq: Sequence[Any], size: int) -> Iterable[Any]:
    """シーケンスを引数のsize分の大きさのリストで分割して返す。
    ジェネレーター関数である。
    Args: 
        seq (Sequence): シーケンス型
        size (int): 分割したいシーケンスの大きさ
    Returns:
        Sequence: シーケンスの中のサイズ分のシーケンス
    """
    maxidx = size
    length = len(seq)       # シーケンスのサイズ
    for minidx in range(0, length, size):
        maxidx = minidx + size
        yield seq[minidx:maxidx]

def bytes_enc(bytes_content: bytes) -> Optional[str]:
    """バイト文字列のエンコード名を返す。
    Args: 
        bytes_content (bytes): バイト文字列
    Returns:
        str: エンコーディング名
        None: エンコーディングが不明
    """
    detector = UniversalDetector()
    buflen = 1000   # detectorに渡すバッファの大きさ
    for buf in seq_split(bytes_content, buflen):
        detector.feed(buf)
        if detector.done:
            break

    # UnivarsalDetectorのresultアトリビュートで
    # エンコーディング名を取り出す前にclose()関数を呼ばないと
    # きちんとエンコーディングを取得できないので注意。
    detector.close()
    encdic = detector.result
    return encdic['encoding']

def dict_conv_str(dic: Optional[Dict[str, Any]], connect_str: str='=', delim: str='&') -> str:
    """辞書を指定したキーと値をつなげる文字と区切り文字に変換した文字列を返す。
    Args:
        dic (Dict[str, Any]): 辞書
        connect_str (str): キーと値をつなげる文字列
        delim (str): 区切り文字
    Returns:
        変換後の文字列
    Raises:
        ValueError: 引数の辞書にNoneが渡された
    """
    if dic is None:
        raise ValueError('dict_conv_str()にNoneが渡されました。辞書オブジェクトが必要です。')
    list_entry = [f'{str(key)}{connect_str}{str(val)}' for key, val in dic.items()]
    ret = delim.join(list_entry)
    return ret

# *importでimportするクラス・関数
__all__ = ['MAX_UNSIGNED_INT', 'MAX_UNSIGNED_LONG', 'hashint', 'hashint64', 'bytes_enc',
        'dict_conv_str']
