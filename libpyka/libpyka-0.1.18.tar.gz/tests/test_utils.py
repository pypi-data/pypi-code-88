"""libpykaライブラリのutilsモジュールのテスト
"""

from typing import Optional, Union, Any
from typing import Callable, NoReturn
from typing import Sequence, Iterable, List, Tuple
from typing import Dict
from typing import TypeVar, Generic, NewType, Type

import unittest
from pathlib import Path
import subprocess
from subprocess import Popen
import re
from libpyka.utils import bytes_enc, dict_conv_str
from libpyka.utils import hashint, hashint64
from libpyka.utils import MAX_UNSIGNED_INT, MAX_UNSIGNED_LONG

class BytesEncTest(unittest.TestCase):
    """libpykaライブラリのbytes_enc()関数のテスト
    バイトの文字列から文字コードを認識できるかテストする。
    """
    
    def test_bytes_enc_utf8(self) -> None:
        """このファイルを元にUTF-8を認識できるかテストする
        Raises:
            AssertionError:  このファイルをUTF-8と認識できない
        """
        fname = Path(__file__)
        byte_content = fname.read_bytes()
        enc = bytes_enc(byte_content)
        self.assertEqual('utf-8', enc)

    def test_bytes_enc_shift_jis(self) -> None:
        """Shift_JIS文字コードのファイルで認識できるかテストする
        Raises:
            AssertionError:  ファイルをShift_JISと認識できない
        """
        fname = 'data/test_utils.py.shift_jis'
        path = Path('tests') / fname
        byte_content = path.read_bytes()
        enc = bytes_enc(byte_content)
        self.assertEqual('shift_jis', enc.lower() if enc is not None else enc)

    def test_bytes_enc_none(self) -> None:
        """文字コードを認識できない場合はNoneを返すかテストする
        Raises:
            AssertionError:  文字コードを認識できない場合Noneを返さない
        """
        fname = 'data/logo.png'
        path = Path('tests') / fname
        byte_content = path.read_bytes()
        enc = bytes_enc(byte_content)
        self.assertIsNone(enc)

class HashIntTest(unittest.TestCase):
    """libpykaライブラリのhashint**()関数のテスト
    ハッシュがちゃんと生成できるかテストする。
    """

    def read_bytes(self, fname: Path) -> bytes:
        """ファイルの内容のバイト列を返す
        Args:
            path (str): ファイル名
        Returns:
            bytes: ファイルの内容
        Raises:
            FileNotFoundError: ファイルが存在しない
        """
        if not fname.exists():
            raise FileNotFoundError(f'ファイル: {str(fname)}は存在しません。')
        return fname.read_bytes();

    def test_hash_int_equal(self) -> None:
        """hashint()関数が同じファイルで同じハッシュ関数を生成するかテスト
        Raises:
            AssertionError: 同じ内容でハッシュが同じものでない
        """
        fname = 'data/logo.png'
        path = Path('tests') / fname
        byte_content = path.read_bytes()
        hash1 = hashint(byte_content)
        hash2 = hashint(byte_content)
        self.assertEqual(hash1, hash2)

    def hash_to_int(self, hashval: str, max_range: int=MAX_UNSIGNED_INT) -> int:
        """ハッシュ値の文字列から整数値を組み立てて返す。
        ハッシュ値は文字列を指定する。
        ハッシュ値の文字列の一個一個の文字からUnicode Pointを求めて、
        その合計でハッシュの整数値を求めている。
        Args:
            hashval (str): ハッシュ値
            max_range (int): 整数値の範囲
        Returns:
            int: 文字列のハッシュ値から生成した整数値
        """
        ret = 1
        for ch in hashval:
            val = ord(ch)
            ret = ret + val
        ret = ret * 1234567
        return ret % max_range

    def test_hash_int_sha256sum_equal(self) -> None:
        """libpykaライブラリのhashint()関数の生成するハッシュと
        シェルのsha256sum関数が生成するハッシュで同じ
        整数値が生成できるかテストする。
        """
        fname = 'data/logo.png'
        path = Path('tests') / fname
        cmd = f'sha256sum {path}'
        proc = Popen(cmd, shell=True, stdout=subprocess.PIPE)
        result = proc.stdout.read().decode('utf-8') # type: ignore
        shhash = re.sub(r'[ \t]+.*$', '', result, flags=re.DOTALL)
        hash1 = self.hash_to_int(shhash)
        proc.wait()
        proc.stdout.close() # type: ignore
        byte_content = self.read_bytes(path)
        hash2 = hashint(byte_content)
        self.assertEqual(hash1, hash2)

        
class DicConvStrTest(unittest.TestCase):
    def test_dict_conv_str_params(self) -> None:
        """入力パラメーターを複数変えテストする
        """
        params = [
                { 
                    'param': {
                        'dic': {'name': 'kamail', 'value': 'テスト'},
                    },
                    'result': 'name=kamail&value=テスト'
                },
                { 
                    'param': {
                        'dic': {'name': 'kamail', 'value': 'テスト', 'python': 'dict'},
                        'connect_str': '#',
                        'delim': ','
                    },
                    'result': 'name#kamail,value#テスト,python#dict'
                },
                { 
                    'param': {
                        'dic': {},
                        'connect_str': '#',
                        'delim': ','
                    },
                    'result': ''
                },
        ]
        for entry in params:
            param = entry['param']
            test_result = entry['result']
            with self.subTest(**param): # type: ignore
                result = dict_conv_str(**param) # type: ignore
                self.assertEqual(result, test_result)
        
    def test_dict_conv_str_ex(self) -> None:
        """辞書がNoneの場合ValueErrorが送出されるかテストする。
        """
        with self.assertRaises(ValueError):
            dict_conv_str(None)

