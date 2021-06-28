# Generated from Dynamod.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from antlr4.Token import CommonToken
import re
import importlib
# Allow languages to extend the lexer and parser, by loading the parser dynamically
module_path = __name__[:-5]
language_name = __name__.split('.')[-1]
language_name = language_name[:-5]  # Remove Lexer from name
LanguageParser = getattr(importlib.import_module('{}Parser'.format(module_path)), '{}Parser'.format(language_name))



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2=")
        buf.write("\u01f1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\3\3\3\3\3\4\3")
        buf.write("\4\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \3!\3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3%\3")
        buf.write("%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3")
        buf.write("+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3/\5/\u015c\n/\3")
        buf.write("/\3/\5/\u0160\n/\3/\5/\u0163\n/\5/\u0165\n/\3/\3/\3\60")
        buf.write("\3\60\7\60\u016b\n\60\f\60\16\60\u016e\13\60\3\61\3\61")
        buf.write("\7\61\u0172\n\61\f\61\16\61\u0175\13\61\3\61\3\61\3\61")
        buf.write("\7\61\u017a\n\61\f\61\16\61\u017d\13\61\3\61\5\61\u0180")
        buf.write("\n\61\3\62\3\62\5\62\u0184\n\62\3\63\3\63\7\63\u0188\n")
        buf.write("\63\f\63\16\63\u018b\13\63\3\63\6\63\u018e\n\63\r\63\16")
        buf.write("\63\u018f\5\63\u0192\n\63\3\64\3\64\5\64\u0196\n\64\3")
        buf.write("\65\3\65\3\66\3\66\3\67\3\67\38\38\38\39\39\39\3:\3:\3")
        buf.write(":\3;\3;\3;\3<\3<\3<\5<\u01ad\n<\3<\3<\3=\3=\3>\3>\3?\5")
        buf.write("?\u01b6\n?\3?\3?\3@\3@\5@\u01bc\n@\3@\3@\3A\6A\u01c1\n")
        buf.write("A\rA\16A\u01c2\3B\3B\6B\u01c7\nB\rB\16B\u01c8\3C\3C\5")
        buf.write("C\u01cd\nC\3C\6C\u01d0\nC\rC\16C\u01d1\3D\6D\u01d5\nD")
        buf.write("\rD\16D\u01d6\3E\3E\7E\u01db\nE\fE\16E\u01de\13E\3F\3")
        buf.write("F\5F\u01e2\nF\3F\5F\u01e5\nF\3F\3F\5F\u01e9\nF\3G\5G\u01ec")
        buf.write("\nG\3H\3H\5H\u01f0\nH\2\2I\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\66k\67m8o9q:s;u<w=y\2{\2}\2\177\2\u0081\2\u0083")
        buf.write("\2\u0085\2\u0087\2\u0089\2\u008b\2\u008d\2\u008f\2\3\2")
        buf.write("\f\6\2\f\f\16\17))^^\6\2\f\f\16\17$$^^\3\2\63;\3\2\62")
        buf.write(";\4\2GGgg\4\2--//\4\2\13\13\"\"\4\2\f\f\16\17\u0129\2")
        buf.write("C\\aac|\u00ac\u00ac\u00b7\u00b7\u00bc\u00bc\u00c2\u00d8")
        buf.write("\u00da\u00f8\u00fa\u0243\u0252\u02c3\u02c8\u02d3\u02e2")
        buf.write("\u02e6\u02f0\u02f0\u037c\u037c\u0388\u0388\u038a\u038c")
        buf.write("\u038e\u038e\u0390\u03a3\u03a5\u03d0\u03d2\u03f7\u03f9")
        buf.write("\u0483\u048c\u04d0\u04d2\u04fb\u0502\u0511\u0533\u0558")
        buf.write("\u055b\u055b\u0563\u0589\u05d2\u05ec\u05f2\u05f4\u0623")
        buf.write("\u063c\u0642\u064c\u0670\u0671\u0673\u06d5\u06d7\u06d7")
        buf.write("\u06e7\u06e8\u06f0\u06f1\u06fc\u06fe\u0701\u0701\u0712")
        buf.write("\u0712\u0714\u0731\u074f\u076f\u0782\u07a7\u07b3\u07b3")
        buf.write("\u0906\u093b\u093f\u093f\u0952\u0952\u095a\u0963\u097f")
        buf.write("\u097f\u0987\u098e\u0991\u0992\u0995\u09aa\u09ac\u09b2")
        buf.write("\u09b4\u09b4\u09b8\u09bb\u09bf\u09bf\u09d0\u09d0\u09de")
        buf.write("\u09df\u09e1\u09e3\u09f2\u09f3\u0a07\u0a0c\u0a11\u0a12")
        buf.write("\u0a15\u0a2a\u0a2c\u0a32\u0a34\u0a35\u0a37\u0a38\u0a3a")
        buf.write("\u0a3b\u0a5b\u0a5e\u0a60\u0a60\u0a74\u0a76\u0a87\u0a8f")
        buf.write("\u0a91\u0a93\u0a95\u0aaa\u0aac\u0ab2\u0ab4\u0ab5\u0ab7")
        buf.write("\u0abb\u0abf\u0abf\u0ad2\u0ad2\u0ae2\u0ae3\u0b07\u0b0e")
        buf.write("\u0b11\u0b12\u0b15\u0b2a\u0b2c\u0b32\u0b34\u0b35\u0b37")
        buf.write("\u0b3b\u0b3f\u0b3f\u0b5e\u0b5f\u0b61\u0b63\u0b73\u0b73")
        buf.write("\u0b85\u0b85\u0b87\u0b8c\u0b90\u0b92\u0b94\u0b97\u0b9b")
        buf.write("\u0b9c\u0b9e\u0b9e\u0ba0\u0ba1\u0ba5\u0ba6\u0baa\u0bac")
        buf.write("\u0bb0\u0bbb\u0c07\u0c0e\u0c10\u0c12\u0c14\u0c2a\u0c2c")
        buf.write("\u0c35\u0c37\u0c3b\u0c62\u0c63\u0c87\u0c8e\u0c90\u0c92")
        buf.write("\u0c94\u0caa\u0cac\u0cb5\u0cb7\u0cbb\u0cbf\u0cbf\u0ce0")
        buf.write("\u0ce0\u0ce2\u0ce3\u0d07\u0d0e\u0d10\u0d12\u0d14\u0d2a")
        buf.write("\u0d2c\u0d3b\u0d62\u0d63\u0d87\u0d98\u0d9c\u0db3\u0db5")
        buf.write("\u0dbd\u0dbf\u0dbf\u0dc2\u0dc8\u0e03\u0e32\u0e34\u0e35")
        buf.write("\u0e42\u0e48\u0e83\u0e84\u0e86\u0e86\u0e89\u0e8a\u0e8c")
        buf.write("\u0e8c\u0e8f\u0e8f\u0e96\u0e99\u0e9b\u0ea1\u0ea3\u0ea5")
        buf.write("\u0ea7\u0ea7\u0ea9\u0ea9\u0eac\u0ead\u0eaf\u0eb2\u0eb4")
        buf.write("\u0eb5\u0ebf\u0ebf\u0ec2\u0ec6\u0ec8\u0ec8\u0ede\u0edf")
        buf.write("\u0f02\u0f02\u0f42\u0f49\u0f4b\u0f6c\u0f8a\u0f8d\u1002")
        buf.write("\u1023\u1025\u1029\u102b\u102c\u1052\u1057\u10a2\u10c7")
        buf.write("\u10d2\u10fc\u10fe\u10fe\u1102\u115b\u1161\u11a4\u11aa")
        buf.write("\u11fb\u1202\u124a\u124c\u124f\u1252\u1258\u125a\u125a")
        buf.write("\u125c\u125f\u1262\u128a\u128c\u128f\u1292\u12b2\u12b4")
        buf.write("\u12b7\u12ba\u12c0\u12c2\u12c2\u12c4\u12c7\u12ca\u12d8")
        buf.write("\u12da\u1312\u1314\u1317\u131a\u135c\u1382\u1391\u13a2")
        buf.write("\u13f6\u1403\u166e\u1671\u1678\u1683\u169c\u16a2\u16ec")
        buf.write("\u16f0\u16f2\u1702\u170e\u1710\u1713\u1722\u1733\u1742")
        buf.write("\u1753\u1762\u176e\u1770\u1772\u1782\u17b5\u17d9\u17d9")
        buf.write("\u17de\u17de\u1822\u1879\u1882\u18aa\u1902\u191e\u1952")
        buf.write("\u196f\u1972\u1976\u1982\u19ab\u19c3\u19c9\u1a02\u1a18")
        buf.write("\u1d02\u1dc1\u1e02\u1e9d\u1ea2\u1efb\u1f02\u1f17\u1f1a")
        buf.write("\u1f1f\u1f22\u1f47\u1f4a\u1f4f\u1f52\u1f59\u1f5b\u1f5b")
        buf.write("\u1f5d\u1f5d\u1f5f\u1f5f\u1f61\u1f7f\u1f82\u1fb6\u1fb8")
        buf.write("\u1fbe\u1fc0\u1fc0\u1fc4\u1fc6\u1fc8\u1fce\u1fd2\u1fd5")
        buf.write("\u1fd8\u1fdd\u1fe2\u1fee\u1ff4\u1ff6\u1ff8\u1ffe\u2073")
        buf.write("\u2073\u2081\u2081\u2092\u2096\u2104\u2104\u2109\u2109")
        buf.write("\u210c\u2115\u2117\u2117\u211a\u211f\u2126\u2126\u2128")
        buf.write("\u2128\u212a\u212a\u212c\u2133\u2135\u213b\u213e\u2141")
        buf.write("\u2147\u214b\u2162\u2185\u2c02\u2c30\u2c32\u2c60\u2c82")
        buf.write("\u2ce6\u2d02\u2d27\u2d32\u2d67\u2d71\u2d71\u2d82\u2d98")
        buf.write("\u2da2\u2da8\u2daa\u2db0\u2db2\u2db8\u2dba\u2dc0\u2dc2")
        buf.write("\u2dc8\u2dca\u2dd0\u2dd2\u2dd8\u2dda\u2de0\u3007\u3009")
        buf.write("\u3023\u302b\u3033\u3037\u303a\u303e\u3043\u3098\u309d")
        buf.write("\u30a1\u30a3\u30fc\u30fe\u3101\u3107\u312e\u3133\u3190")
        buf.write("\u31a2\u31b9\u31f2\u3201\u3402\u4db7\u4e02\u9fbd\ua002")
        buf.write("\ua48e\ua802\ua803\ua805\ua807\ua809\ua80c\ua80e\ua824")
        buf.write("\uac02\ud7a5\uf902\ufa2f\ufa32\ufa6c\ufa72\ufadb\ufb02")
        buf.write("\ufb08\ufb15\ufb19\ufb1f\ufb1f\ufb21\ufb2a\ufb2c\ufb38")
        buf.write("\ufb3a\ufb3e\ufb40\ufb40\ufb42\ufb43\ufb45\ufb46\ufb48")
        buf.write("\ufbb3\ufbd5\ufd3f\ufd52\ufd91\ufd94\ufdc9\ufdf2\ufdfd")
        buf.write("\ufe72\ufe76\ufe78\ufefe\uff23\uff3c\uff43\uff5c\uff68")
        buf.write("\uffc0\uffc4\uffc9\uffcc\uffd1\uffd4\uffd9\uffdc\uffde")
        buf.write("\u0096\2\62;\u0302\u0371\u0485\u0488\u0593\u05bb\u05bd")
        buf.write("\u05bf\u05c1\u05c1\u05c3\u05c4\u05c6\u05c7\u05c9\u05c9")
        buf.write("\u0612\u0617\u064d\u0660\u0662\u066b\u0672\u0672\u06d8")
        buf.write("\u06de\u06e1\u06e6\u06e9\u06ea\u06ec\u06ef\u06f2\u06fb")
        buf.write("\u0713\u0713\u0732\u074c\u07a8\u07b2\u0903\u0905\u093e")
        buf.write("\u093e\u0940\u094f\u0953\u0956\u0964\u0965\u0968\u0971")
        buf.write("\u0983\u0985\u09be\u09be\u09c0\u09c6\u09c9\u09ca\u09cd")
        buf.write("\u09cf\u09d9\u09d9\u09e4\u09e5\u09e8\u09f1\u0a03\u0a05")
        buf.write("\u0a3e\u0a3e\u0a40\u0a44\u0a49\u0a4a\u0a4d\u0a4f\u0a68")
        buf.write("\u0a73\u0a83\u0a85\u0abe\u0abe\u0ac0\u0ac7\u0ac9\u0acb")
        buf.write("\u0acd\u0acf\u0ae4\u0ae5\u0ae8\u0af1\u0b03\u0b05\u0b3e")
        buf.write("\u0b3e\u0b40\u0b45\u0b49\u0b4a\u0b4d\u0b4f\u0b58\u0b59")
        buf.write("\u0b68\u0b71\u0b84\u0b84\u0bc0\u0bc4\u0bc8\u0bca\u0bcc")
        buf.write("\u0bcf\u0bd9\u0bd9\u0be8\u0bf1\u0c03\u0c05\u0c40\u0c46")
        buf.write("\u0c48\u0c4a\u0c4c\u0c4f\u0c57\u0c58\u0c68\u0c71\u0c84")
        buf.write("\u0c85\u0cbe\u0cbe\u0cc0\u0cc6\u0cc8\u0cca\u0ccc\u0ccf")
        buf.write("\u0cd7\u0cd8\u0ce8\u0cf1\u0d04\u0d05\u0d40\u0d45\u0d48")
        buf.write("\u0d4a\u0d4c\u0d4f\u0d59\u0d59\u0d68\u0d71\u0d84\u0d85")
        buf.write("\u0dcc\u0dcc\u0dd1\u0dd6\u0dd8\u0dd8\u0dda\u0de1\u0df4")
        buf.write("\u0df5\u0e33\u0e33\u0e36\u0e3c\u0e49\u0e50\u0e52\u0e5b")
        buf.write("\u0eb3\u0eb3\u0eb6\u0ebb\u0ebd\u0ebe\u0eca\u0ecf\u0ed2")
        buf.write("\u0edb\u0f1a\u0f1b\u0f22\u0f2b\u0f37\u0f37\u0f39\u0f39")
        buf.write("\u0f3b\u0f3b\u0f40\u0f41\u0f73\u0f86\u0f88\u0f89\u0f92")
        buf.write("\u0f99\u0f9b\u0fbe\u0fc8\u0fc8\u102e\u1034\u1038\u103b")
        buf.write("\u1042\u104b\u1058\u105b\u1361\u1361\u136b\u1373\u1714")
        buf.write("\u1716\u1734\u1736\u1754\u1755\u1774\u1775\u17b8\u17d5")
        buf.write("\u17df\u17df\u17e2\u17eb\u180d\u180f\u1812\u181b\u18ab")
        buf.write("\u18ab\u1922\u192d\u1932\u193d\u1948\u1951\u19b2\u19c2")
        buf.write("\u19ca\u19cb\u19d2\u19db\u1a19\u1a1d\u1dc2\u1dc5\u2041")
        buf.write("\u2042\u2056\u2056\u20d2\u20de\u20e3\u20e3\u20e7\u20ed")
        buf.write("\u302c\u3031\u309b\u309c\ua804\ua804\ua808\ua808\ua80d")
        buf.write("\ua80d\ua825\ua829\ufb20\ufb20\ufe02\ufe11\ufe22\ufe25")
        buf.write("\ufe35\ufe36\ufe4f\ufe51\uff12\uff1b\uff41\uff41\2\u01ff")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\3\u0091\3\2")
        buf.write("\2\2\5\u0093\3\2\2\2\7\u0095\3\2\2\2\t\u0097\3\2\2\2\13")
        buf.write("\u0099\3\2\2\2\r\u009c\3\2\2\2\17\u009e\3\2\2\2\21\u00a0")
        buf.write("\3\2\2\2\23\u00a3\3\2\2\2\25\u00a5\3\2\2\2\27\u00a7\3")
        buf.write("\2\2\2\31\u00af\3\2\2\2\33\u00ba\3\2\2\2\35\u00c5\3\2")
        buf.write("\2\2\37\u00d2\3\2\2\2!\u00db\3\2\2\2#\u00e3\3\2\2\2%\u00eb")
        buf.write("\3\2\2\2\'\u00f2\3\2\2\2)\u00f9\3\2\2\2+\u00fc\3\2\2\2")
        buf.write("-\u0100\3\2\2\2/\u0103\3\2\2\2\61\u010d\3\2\2\2\63\u0111")
        buf.write("\3\2\2\2\65\u0115\3\2\2\2\67\u0118\3\2\2\29\u011b\3\2")
        buf.write("\2\2;\u0121\3\2\2\2=\u0126\3\2\2\2?\u0129\3\2\2\2A\u012e")
        buf.write("\3\2\2\2C\u0132\3\2\2\2E\u0135\3\2\2\2G\u0139\3\2\2\2")
        buf.write("I\u013b\3\2\2\2K\u013e\3\2\2\2M\u0140\3\2\2\2O\u0143\3")
        buf.write("\2\2\2Q\u0146\3\2\2\2S\u0149\3\2\2\2U\u014c\3\2\2\2W\u014f")
        buf.write("\3\2\2\2Y\u0152\3\2\2\2[\u0155\3\2\2\2]\u0164\3\2\2\2")
        buf.write("_\u0168\3\2\2\2a\u017f\3\2\2\2c\u0183\3\2\2\2e\u0191\3")
        buf.write("\2\2\2g\u0195\3\2\2\2i\u0197\3\2\2\2k\u0199\3\2\2\2m\u019b")
        buf.write("\3\2\2\2o\u019d\3\2\2\2q\u01a0\3\2\2\2s\u01a3\3\2\2\2")
        buf.write("u\u01a6\3\2\2\2w\u01ac\3\2\2\2y\u01b0\3\2\2\2{\u01b2\3")
        buf.write("\2\2\2}\u01b5\3\2\2\2\177\u01bb\3\2\2\2\u0081\u01c0\3")
        buf.write("\2\2\2\u0083\u01c4\3\2\2\2\u0085\u01ca\3\2\2\2\u0087\u01d4")
        buf.write("\3\2\2\2\u0089\u01d8\3\2\2\2\u008b\u01df\3\2\2\2\u008d")
        buf.write("\u01eb\3\2\2\2\u008f\u01ef\3\2\2\2\u0091\u0092\7?\2\2")
        buf.write("\u0092\4\3\2\2\2\u0093\u0094\7.\2\2\u0094\6\3\2\2\2\u0095")
        buf.write("\u0096\7-\2\2\u0096\b\3\2\2\2\u0097\u0098\7/\2\2\u0098")
        buf.write("\n\3\2\2\2\u0099\u009a\7,\2\2\u009a\u009b\7,\2\2\u009b")
        buf.write("\f\3\2\2\2\u009c\u009d\7\61\2\2\u009d\16\3\2\2\2\u009e")
        buf.write("\u009f\7\'\2\2\u009f\20\3\2\2\2\u00a0\u00a1\7\'\2\2\u00a1")
        buf.write("\u00a2\7\'\2\2\u00a2\22\3\2\2\2\u00a3\u00a4\7&\2\2\u00a4")
        buf.write("\24\3\2\2\2\u00a5\u00a6\7~\2\2\u00a6\26\3\2\2\2\u00a7")
        buf.write("\u00a8\7g\2\2\u00a8\u00a9\7z\2\2\u00a9\u00aa\7v\2\2\u00aa")
        buf.write("\u00ab\7g\2\2\u00ab\u00ac\7p\2\2\u00ac\u00ad\7f\2\2\u00ad")
        buf.write("\u00ae\7u\2\2\u00ae\30\3\2\2\2\u00af\u00b0\7r\2\2\u00b0")
        buf.write("\u00b1\7c\2\2\u00b1\u00b2\7t\2\2\u00b2\u00b3\7c\2\2\u00b3")
        buf.write("\u00b4\7o\2\2\u00b4\u00b5\7g\2\2\u00b5\u00b6\7v\2\2\u00b6")
        buf.write("\u00b7\7g\2\2\u00b7\u00b8\7t\2\2\u00b8\u00b9\7u\2\2\u00b9")
        buf.write("\32\3\2\2\2\u00ba\u00bb\7c\2\2\u00bb\u00bc\7v\2\2\u00bc")
        buf.write("\u00bd\7v\2\2\u00bd\u00be\7t\2\2\u00be\u00bf\7k\2\2\u00bf")
        buf.write("\u00c0\7d\2\2\u00c0\u00c1\7w\2\2\u00c1\u00c2\7v\2\2\u00c2")
        buf.write("\u00c3\7g\2\2\u00c3\u00c4\7u\2\2\u00c4\34\3\2\2\2\u00c5")
        buf.write("\u00c6\7r\2\2\u00c6\u00c7\7t\2\2\u00c7\u00c8\7q\2\2\u00c8")
        buf.write("\u00c9\7i\2\2\u00c9\u00ca\7t\2\2\u00ca\u00cb\7g\2\2\u00cb")
        buf.write("\u00cc\7u\2\2\u00cc\u00cd\7u\2\2\u00cd\u00ce\7k\2\2\u00ce")
        buf.write("\u00cf\7q\2\2\u00cf\u00d0\7p\2\2\u00d0\u00d1\7u\2\2\u00d1")
        buf.write("\36\3\2\2\2\u00d2\u00d3\7h\2\2\u00d3\u00d4\7q\2\2\u00d4")
        buf.write("\u00d5\7t\2\2\u00d5\u00d6\7o\2\2\u00d6\u00d7\7w\2\2\u00d7")
        buf.write("\u00d8\7n\2\2\u00d8\u00d9\7c\2\2\u00d9\u00da\7u\2\2\u00da")
        buf.write(" \3\2\2\2\u00db\u00dc\7t\2\2\u00dc\u00dd\7g\2\2\u00dd")
        buf.write("\u00de\7u\2\2\u00de\u00df\7w\2\2\u00df\u00e0\7n\2\2\u00e0")
        buf.write("\u00e1\7v\2\2\u00e1\u00e2\7u\2\2\u00e2\"\3\2\2\2\u00e3")
        buf.write("\u00e4\7e\2\2\u00e4\u00e5\7j\2\2\u00e5\u00e6\7c\2\2\u00e6")
        buf.write("\u00e7\7p\2\2\u00e7\u00e8\7i\2\2\u00e8\u00e9\7g\2\2\u00e9")
        buf.write("\u00ea\7u\2\2\u00ea$\3\2\2\2\u00eb\u00ec\7x\2\2\u00ec")
        buf.write("\u00ed\7c\2\2\u00ed\u00ee\7n\2\2\u00ee\u00ef\7w\2\2\u00ef")
        buf.write("\u00f0\7g\2\2\u00f0\u00f1\7u\2\2\u00f1&\3\2\2\2\u00f2")
        buf.write("\u00f3\7u\2\2\u00f3\u00f4\7j\2\2\u00f4\u00f5\7c\2\2\u00f5")
        buf.write("\u00f6\7t\2\2\u00f6\u00f7\7g\2\2\u00f7\u00f8\7u\2\2\u00f8")
        buf.write("(\3\2\2\2\u00f9\u00fa\7c\2\2\u00fa\u00fb\7v\2\2\u00fb")
        buf.write("*\3\2\2\2\u00fc\u00fd\7h\2\2\u00fd\u00fe\7q\2\2\u00fe")
        buf.write("\u00ff\7t\2\2\u00ff,\3\2\2\2\u0100\u0101\7k\2\2\u0101")
        buf.write("\u0102\7p\2\2\u0102.\3\2\2\2\u0103\u0104\7q\2\2\u0104")
        buf.write("\u0105\7v\2\2\u0105\u0106\7j\2\2\u0106\u0107\7g\2\2\u0107")
        buf.write("\u0108\7t\2\2\u0108\u0109\7y\2\2\u0109\u010a\7k\2\2\u010a")
        buf.write("\u010b\7u\2\2\u010b\u010c\7g\2\2\u010c\60\3\2\2\2\u010d")
        buf.write("\u010e\7x\2\2\u010e\u010f\7c\2\2\u010f\u0110\7t\2\2\u0110")
        buf.write("\62\3\2\2\2\u0111\u0112\7u\2\2\u0112\u0113\7g\2\2\u0113")
        buf.write("\u0114\7v\2\2\u0114\64\3\2\2\2\u0115\u0116\7c\2\2\u0116")
        buf.write("\u0117\7u\2\2\u0117\66\3\2\2\2\u0118\u0119\7d\2\2\u0119")
        buf.write("\u011a\7{\2\2\u011a8\3\2\2\2\u011b\u011c\7c\2\2\u011c")
        buf.write("\u011d\7h\2\2\u011d\u011e\7v\2\2\u011e\u011f\7g\2\2\u011f")
        buf.write("\u0120\7t\2\2\u0120:\3\2\2\2\u0121\u0122\7y\2\2\u0122")
        buf.write("\u0123\7k\2\2\u0123\u0124\7v\2\2\u0124\u0125\7j\2\2\u0125")
        buf.write("<\3\2\2\2\u0126\u0127\7k\2\2\u0127\u0128\7h\2\2\u0128")
        buf.write(">\3\2\2\2\u0129\u012a\7g\2\2\u012a\u012b\7n\2\2\u012b")
        buf.write("\u012c\7u\2\2\u012c\u012d\7g\2\2\u012d@\3\2\2\2\u012e")
        buf.write("\u012f\7c\2\2\u012f\u0130\7p\2\2\u0130\u0131\7f\2\2\u0131")
        buf.write("B\3\2\2\2\u0132\u0133\7q\2\2\u0133\u0134\7t\2\2\u0134")
        buf.write("D\3\2\2\2\u0135\u0136\7p\2\2\u0136\u0137\7q\2\2\u0137")
        buf.write("\u0138\7v\2\2\u0138F\3\2\2\2\u0139\u013a\7>\2\2\u013a")
        buf.write("H\3\2\2\2\u013b\u013c\7>\2\2\u013c\u013d\7?\2\2\u013d")
        buf.write("J\3\2\2\2\u013e\u013f\7@\2\2\u013fL\3\2\2\2\u0140\u0141")
        buf.write("\7@\2\2\u0141\u0142\7?\2\2\u0142N\3\2\2\2\u0143\u0144")
        buf.write("\7#\2\2\u0144\u0145\7?\2\2\u0145P\3\2\2\2\u0146\u0147")
        buf.write("\7?\2\2\u0147\u0148\7?\2\2\u0148R\3\2\2\2\u0149\u014a")
        buf.write("\7\60\2\2\u014a\u014b\7\60\2\2\u014bT\3\2\2\2\u014c\u014d")
        buf.write("\7-\2\2\u014d\u014e\7?\2\2\u014eV\3\2\2\2\u014f\u0150")
        buf.write("\7/\2\2\u0150\u0151\7?\2\2\u0151X\3\2\2\2\u0152\u0153")
        buf.write("\7,\2\2\u0153\u0154\7?\2\2\u0154Z\3\2\2\2\u0155\u0156")
        buf.write("\7\61\2\2\u0156\u0157\7?\2\2\u0157\\\3\2\2\2\u0158\u0159")
        buf.write("\6/\2\2\u0159\u0165\5\u0087D\2\u015a\u015c\7\17\2\2\u015b")
        buf.write("\u015a\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015d\3\2\2\2")
        buf.write("\u015d\u0160\7\f\2\2\u015e\u0160\4\16\17\2\u015f\u015b")
        buf.write("\3\2\2\2\u015f\u015e\3\2\2\2\u0160\u0162\3\2\2\2\u0161")
        buf.write("\u0163\5\u0087D\2\u0162\u0161\3\2\2\2\u0162\u0163\3\2")
        buf.write("\2\2\u0163\u0165\3\2\2\2\u0164\u0158\3\2\2\2\u0164\u015f")
        buf.write("\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0167\b/\2\2\u0167")
        buf.write("^\3\2\2\2\u0168\u016c\5\u008dG\2\u0169\u016b\5\u008fH")
        buf.write("\2\u016a\u0169\3\2\2\2\u016b\u016e\3\2\2\2\u016c\u016a")
        buf.write("\3\2\2\2\u016c\u016d\3\2\2\2\u016d`\3\2\2\2\u016e\u016c")
        buf.write("\3\2\2\2\u016f\u0173\7)\2\2\u0170\u0172\n\2\2\2\u0171")
        buf.write("\u0170\3\2\2\2\u0172\u0175\3\2\2\2\u0173\u0171\3\2\2\2")
        buf.write("\u0173\u0174\3\2\2\2\u0174\u0176\3\2\2\2\u0175\u0173\3")
        buf.write("\2\2\2\u0176\u0180\7)\2\2\u0177\u017b\7$\2\2\u0178\u017a")
        buf.write("\n\3\2\2\u0179\u0178\3\2\2\2\u017a\u017d\3\2\2\2\u017b")
        buf.write("\u0179\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017e\3\2\2\2")
        buf.write("\u017d\u017b\3\2\2\2\u017e\u0180\7$\2\2\u017f\u016f\3")
        buf.write("\2\2\2\u017f\u0177\3\2\2\2\u0180b\3\2\2\2\u0181\u0184")
        buf.write("\5e\63\2\u0182\u0184\5g\64\2\u0183\u0181\3\2\2\2\u0183")
        buf.write("\u0182\3\2\2\2\u0184d\3\2\2\2\u0185\u0189\5y=\2\u0186")
        buf.write("\u0188\5{>\2\u0187\u0186\3\2\2\2\u0188\u018b\3\2\2\2\u0189")
        buf.write("\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u0192\3\2\2\2")
        buf.write("\u018b\u0189\3\2\2\2\u018c\u018e\7\62\2\2\u018d\u018c")
        buf.write("\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u018d\3\2\2\2\u018f")
        buf.write("\u0190\3\2\2\2\u0190\u0192\3\2\2\2\u0191\u0185\3\2\2\2")
        buf.write("\u0191\u018d\3\2\2\2\u0192f\3\2\2\2\u0193\u0196\5}?\2")
        buf.write("\u0194\u0196\5\177@\2\u0195\u0193\3\2\2\2\u0195\u0194")
        buf.write("\3\2\2\2\u0196h\3\2\2\2\u0197\u0198\7\60\2\2\u0198j\3")
        buf.write("\2\2\2\u0199\u019a\7,\2\2\u019al\3\2\2\2\u019b\u019c\7")
        buf.write("<\2\2\u019cn\3\2\2\2\u019d\u019e\7*\2\2\u019e\u019f\b")
        buf.write("8\3\2\u019fp\3\2\2\2\u01a0\u01a1\7+\2\2\u01a1\u01a2\b")
        buf.write("9\4\2\u01a2r\3\2\2\2\u01a3\u01a4\7]\2\2\u01a4\u01a5\b")
        buf.write(":\5\2\u01a5t\3\2\2\2\u01a6\u01a7\7_\2\2\u01a7\u01a8\b")
        buf.write(";\6\2\u01a8v\3\2\2\2\u01a9\u01ad\5\u0087D\2\u01aa\u01ad")
        buf.write("\5\u0089E\2\u01ab\u01ad\5\u008bF\2\u01ac\u01a9\3\2\2\2")
        buf.write("\u01ac\u01aa\3\2\2\2\u01ac\u01ab\3\2\2\2\u01ad\u01ae\3")
        buf.write("\2\2\2\u01ae\u01af\b<\7\2\u01afx\3\2\2\2\u01b0\u01b1\t")
        buf.write("\4\2\2\u01b1z\3\2\2\2\u01b2\u01b3\t\5\2\2\u01b3|\3\2\2")
        buf.write("\2\u01b4\u01b6\5\u0081A\2\u01b5\u01b4\3\2\2\2\u01b5\u01b6")
        buf.write("\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01b8\5\u0083B\2\u01b8")
        buf.write("~\3\2\2\2\u01b9\u01bc\5\u0081A\2\u01ba\u01bc\5}?\2\u01bb")
        buf.write("\u01b9\3\2\2\2\u01bb\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2")
        buf.write("\u01bd\u01be\5\u0085C\2\u01be\u0080\3\2\2\2\u01bf\u01c1")
        buf.write("\5{>\2\u01c0\u01bf\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01c0")
        buf.write("\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3\u0082\3\2\2\2\u01c4")
        buf.write("\u01c6\7\60\2\2\u01c5\u01c7\5{>\2\u01c6\u01c5\3\2\2\2")
        buf.write("\u01c7\u01c8\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c8\u01c9\3")
        buf.write("\2\2\2\u01c9\u0084\3\2\2\2\u01ca\u01cc\t\6\2\2\u01cb\u01cd")
        buf.write("\t\7\2\2\u01cc\u01cb\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd")
        buf.write("\u01cf\3\2\2\2\u01ce\u01d0\5{>\2\u01cf\u01ce\3\2\2\2\u01d0")
        buf.write("\u01d1\3\2\2\2\u01d1\u01cf\3\2\2\2\u01d1\u01d2\3\2\2\2")
        buf.write("\u01d2\u0086\3\2\2\2\u01d3\u01d5\t\b\2\2\u01d4\u01d3\3")
        buf.write("\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6\u01d7")
        buf.write("\3\2\2\2\u01d7\u0088\3\2\2\2\u01d8\u01dc\7%\2\2\u01d9")
        buf.write("\u01db\n\t\2\2\u01da\u01d9\3\2\2\2\u01db\u01de\3\2\2\2")
        buf.write("\u01dc\u01da\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u008a\3")
        buf.write("\2\2\2\u01de\u01dc\3\2\2\2\u01df\u01e1\7^\2\2\u01e0\u01e2")
        buf.write("\5\u0087D\2\u01e1\u01e0\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2")
        buf.write("\u01e8\3\2\2\2\u01e3\u01e5\7\17\2\2\u01e4\u01e3\3\2\2")
        buf.write("\2\u01e4\u01e5\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01e9")
        buf.write("\7\f\2\2\u01e7\u01e9\4\16\17\2\u01e8\u01e4\3\2\2\2\u01e8")
        buf.write("\u01e7\3\2\2\2\u01e9\u008c\3\2\2\2\u01ea\u01ec\t\n\2\2")
        buf.write("\u01eb\u01ea\3\2\2\2\u01ec\u008e\3\2\2\2\u01ed\u01f0\5")
        buf.write("\u008dG\2\u01ee\u01f0\t\13\2\2\u01ef\u01ed\3\2\2\2\u01ef")
        buf.write("\u01ee\3\2\2\2\u01f0\u0090\3\2\2\2\36\2\u015b\u015f\u0162")
        buf.write("\u0164\u016c\u0173\u017b\u017f\u0183\u0189\u018f\u0191")
        buf.write("\u0195\u01ac\u01b5\u01bb\u01c2\u01c8\u01cc\u01d1\u01d6")
        buf.write("\u01dc\u01e1\u01e4\u01e8\u01eb\u01ef\b\3/\2\38\3\39\4")
        buf.write("\3:\5\3;\6\b\2\2")
        return buf.getvalue()


class DynamodLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    EXTENDS = 11
    PARAMETERS = 12
    ATTRIBUTES = 13
    PROGRESSION = 14
    FORMULAS = 15
    RESULTS = 16
    CHANGES = 17
    VALUES = 18
    SHARES = 19
    AT = 20
    FOR = 21
    IN = 22
    OTHERWISE = 23
    VAR = 24
    SET = 25
    AS = 26
    BY = 27
    AFTER = 28
    WITH = 29
    IF = 30
    ELSE = 31
    AND = 32
    OR = 33
    NOT = 34
    LT = 35
    LE = 36
    GT = 37
    GE = 38
    NE = 39
    EQ = 40
    DOTDOT = 41
    PLUSASS = 42
    MINUSASS = 43
    MULTASS = 44
    DIVASS = 45
    NEWLINE = 46
    NAME = 47
    STRING = 48
    NUMBER = 49
    INTEGER = 50
    FLOAT_NUMBER = 51
    DOT = 52
    STAR = 53
    COLON = 54
    OPEN_PAREN = 55
    CLOSE_PAREN = 56
    OPEN_BRACK = 57
    CLOSE_BRACK = 58
    SKIP_ = 59

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "','", "'+'", "'-'", "'**'", "'/'", "'%'", "'%%'", "'$'", 
            "'|'", "'extends'", "'parameters'", "'attributes'", "'progressions'", 
            "'formulas'", "'results'", "'changes'", "'values'", "'shares'", 
            "'at'", "'for'", "'in'", "'otherwise'", "'var'", "'set'", "'as'", 
            "'by'", "'after'", "'with'", "'if'", "'else'", "'and'", "'or'", 
            "'not'", "'<'", "'<='", "'>'", "'>='", "'!='", "'=='", "'..'", 
            "'+='", "'-='", "'*='", "'/='", "'.'", "'*'", "':'", "'('", 
            "')'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "EXTENDS", "PARAMETERS", "ATTRIBUTES", "PROGRESSION", "FORMULAS", 
            "RESULTS", "CHANGES", "VALUES", "SHARES", "AT", "FOR", "IN", 
            "OTHERWISE", "VAR", "SET", "AS", "BY", "AFTER", "WITH", "IF", 
            "ELSE", "AND", "OR", "NOT", "LT", "LE", "GT", "GE", "NE", "EQ", 
            "DOTDOT", "PLUSASS", "MINUSASS", "MULTASS", "DIVASS", "NEWLINE", 
            "NAME", "STRING", "NUMBER", "INTEGER", "FLOAT_NUMBER", "DOT", 
            "STAR", "COLON", "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACK", 
            "CLOSE_BRACK", "SKIP_" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "EXTENDS", "PARAMETERS", "ATTRIBUTES", 
                  "PROGRESSION", "FORMULAS", "RESULTS", "CHANGES", "VALUES", 
                  "SHARES", "AT", "FOR", "IN", "OTHERWISE", "VAR", "SET", 
                  "AS", "BY", "AFTER", "WITH", "IF", "ELSE", "AND", "OR", 
                  "NOT", "LT", "LE", "GT", "GE", "NE", "EQ", "DOTDOT", "PLUSASS", 
                  "MINUSASS", "MULTASS", "DIVASS", "NEWLINE", "NAME", "STRING", 
                  "NUMBER", "INTEGER", "FLOAT_NUMBER", "DOT", "STAR", "COLON", 
                  "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACK", "CLOSE_BRACK", 
                  "SKIP_", "NON_ZERO_DIGIT", "DIGIT", "POINT_FLOAT", "EXPONENT_FLOAT", 
                  "INT_PART", "FRACTION", "EXPONENT", "SPACES", "COMMENT", 
                  "LINE_JOINING", "ID_START", "ID_CONTINUE" ]

    grammarFileName = "Dynamod.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    @property
    def tokens(self):
        try:
            return self._tokens
        except AttributeError:
            self._tokens = []
            return self._tokens
    @property
    def indents(self):
        try:
            return self._indents
        except AttributeError:
            self._indents = []
            return self._indents
    @property
    def opened(self):
        try:
            return self._opened
        except AttributeError:
            self._opened = 0
            return self._opened
    @opened.setter
    def opened(self, value):
        self._opened = value
    @property
    def lastToken(self):
        try:
            return self._lastToken
        except AttributeError:
            self._lastToken = None
            return self._lastToken
    @lastToken.setter
    def lastToken(self, value):
        self._lastToken = value
    def reset(self):
        super().reset()
        self.tokens = []
        self.indents = []
        self.opened = 0
        self.lastToken = None
    def emitToken(self, t):
        super().emitToken(t)
        self.tokens.append(t)
    def nextToken(self):
        if self._input.LA(1) == Token.EOF and self.indents:
            for i in range(len(self.tokens)-1,-1,-1):
                if self.tokens[i].type == Token.EOF:
                    self.tokens.pop(i)
            self.emitToken(self.commonToken(LanguageParser.NEWLINE, '\n'))
            while self.indents:
                self.emitToken(self.createDedent())
                self.indents.pop()
            self.emitToken(self.commonToken(LanguageParser.EOF, "<EOF>"))
        next = super().nextToken()
        if next.channel == Token.DEFAULT_CHANNEL:
            self.lastToken = next
        return next if not self.tokens else self.tokens.pop(0)
    def createDedent(self):
        dedent = self.commonToken(LanguageParser.DEDENT, "")
        dedent.line = self.lastToken.line
        return dedent
    def commonToken(self, type, text, indent=0):
        stop = self.getCharIndex()-1-indent
        start = (stop - len(text) + 1) if text else stop
        return CommonToken(self._tokenFactorySourcePair, type, super().DEFAULT_TOKEN_CHANNEL, start, stop)
    @staticmethod
    def getIndentationCount(spaces):
        count = 0
        for ch in spaces:
            if ch == '\t':
                count += 8 - (count % 8)
            else:
                count += 1
        return count
    def atStartOfInput(self):
        return Lexer.column.fget(self) == 0 and Lexer.line.fget(self) == 1


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[45] = self.NEWLINE_action 
            actions[54] = self.OPEN_PAREN_action 
            actions[55] = self.CLOSE_PAREN_action 
            actions[56] = self.OPEN_BRACK_action 
            actions[57] = self.CLOSE_BRACK_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            tempt = Lexer.text.fget(self)
            newLine = re.sub("[^\r\n\f]+", "", tempt)
            spaces = re.sub("[\r\n\f]+", "", tempt)
            la_char = ""
            try:
                la = self._input.LA(1)
                la_char = chr(la)       # Python does not compare char to ints directly
            except ValueError:          # End of file
                pass
            # Strip newlines inside open clauses except if we are near EOF. We keep NEWLINEs near EOF to
            # satisfy the final newline needed by the single_put rule used by the REPL.
            try:
                nextnext_la = self._input.LA(2)
                nextnext_la_char = chr(nextnext_la)
            except ValueError:
                nextnext_eof = True
            else:
                nextnext_eof = False
            if self.opened > 0 or nextnext_eof is False and (la_char == '\r' or la_char == '\n' or la_char == '\f' or la_char == '#'):
                self.skip()
            else:
                indent = self.getIndentationCount(spaces)
                previous = self.indents[-1] if self.indents else 0
                self.emitToken(self.commonToken(self.NEWLINE, newLine, indent=indent))      # NEWLINE is actually the '\n' char
                if indent == previous:
                    self.skip()
                elif indent > previous:
                    self.indents.append(indent)
                    self.emitToken(self.commonToken(LanguageParser.INDENT, spaces))
                else:
                    while self.indents and self.indents[-1] > indent:
                        self.emitToken(self.createDedent())
                        self.indents.pop()
                
     

    def OPEN_PAREN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.opened += 1
     

    def CLOSE_PAREN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.opened -= 1
     

    def OPEN_BRACK_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.opened += 1
     

    def CLOSE_BRACK_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.opened -= 1
     

    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates is None:
            preds = dict()
            preds[45] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.atStartOfInput()
         


