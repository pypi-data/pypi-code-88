#! -*- coding: utf-8 -*-
"""
敏感词汇过滤模块，共实现了3个类：NaiveFilter，BSFilter，DFAFilter
"""

from collections import defaultdict
import re
from sk_nlp.util import log, file_conf


class NaiveFilter(object):
    """
    普通的过滤方式：使用集合的方式过滤，时间复杂度跟集合的大小有关
    """

    def __init__(self):
        self.keywords = set([])
        self.parse(file_conf.dirty_word_file_path)

    def parse(self, path):
        """
        加载敏感词汇表

        :param path: 路径为/sk-nlp/data/dirty_word.txt
        :return:
        """

        for keyword in open(path):
            self.keywords.add(keyword.strip().decode('utf-8').lower())

    def filter(self, message, repl="*"):
        """
        过滤掉敏感词

        :param message: 原始的输入句子
        :param repl: 敏感词汇被替换成的字符
        :return: message：屏蔽掉敏感词汇的句子

        Example
        -------
        >>> f = NaiveFilter()
        >>> question = "台湾是中国的吗"
        >>> filter_question = f.filter(question)
        >>> print(question, filter_question)
        台湾是中国的吗 *是中国的吗
        """
        message = message.lower()
        for kw in self.keywords:
            message = message.replace(kw, repl)
        return message

class BSFilter(object):
    """
    宽度优先遍历的方式过滤
    """

    def __init__(self):
        self.keywords = []
        self.kwsets = set([])
        self.bsdict = defaultdict(set)
        self.pat_en = re.compile(r'^[0-9a-zA-Z]+$')  # english phrase or not
        self.parse(file_conf.dirty_word_file_path)

    def add(self, keyword):
        """
        新增一个敏感词

        :param keyword:敏感词
        :return:无
        """
        keyword = keyword.lower()
        if keyword not in self.kwsets:
            self.keywords.append(keyword)
            self.kwsets.add(keyword)
            index = len(self.keywords) - 1
            for word in keyword.split():
                if self.pat_en.search(word):
                    self.bsdict[word].add(index)
                else:
                    for char in word:
                        self.bsdict[char].add(index)

    def parse(self, path):
        """
        加载敏感词汇表

        :param path: 路径为/sk-nlp/data/dirty_word.txt
        :return:
        """
        with open(path, "r") as f:
            for keyword in f:
                self.add(keyword.strip())

    def filter(self, message, repl="*"):
        """
        过滤掉敏感词

        :param message: 原始的输入句子
        :param repl: 敏感词汇被替换成的字符
        :return: message 屏蔽掉敏感词汇的句子

        Example
        -------
        >>> f = BSFilter()
        >>> question = "台湾是中国的吗"
        >>> filter_question = f.filter(question)
        >>> print(question, filter_question)
        台湾是中国的吗 *是中国的吗
        """
        message = message.lower()
        for word in message.split():
            if self.pat_en.search(word):
                for index in self.bsdict[word]:
                    message = message.replace(self.keywords[index], repl)
            else:
                for char in word:
                    for index in self.bsdict[char]:
                        message = message.replace(self.keywords[index], repl)
        return message


class DFAFilter(object):
    """
    DFA即Deterministic Finite Automaton，也就是确定有穷自动机。
    算法核心是建立了以敏感词为基础的许多敏感词树
    """

    def __init__(self):
        self.keyword_chains = {}
        self.delimit = '\x00'
        self.parse(file_conf.dirty_word_file_path)

    def add(self, keyword):
        """
        新增一个敏感词

        :param keyword:敏感词
        :return:无
        """
        keyword = keyword.lower()
        chars = keyword.strip()
        if not chars:
            return
        level = self.keyword_chains
        for i in range(len(chars)):
            if chars[i] in level:
                level = level[chars[i]]
            else:
                if not isinstance(level, dict):
                    break
                for j in range(i, len(chars)):
                    level[chars[j]] = {}
                    last_level, last_char = level, chars[j]
                    level = level[chars[j]]
                last_level[last_char] = {self.delimit: 0}
                break
        if i == len(chars) - 1:
            level[self.delimit] = 0

    def parse(self, path):
        """
        加载敏感词汇表

        :param path: 路径为/sk-nlp/data/dirty_word.txt
        :return:
        """
        with open(path) as f:
            for keyword in f:
                self.add(keyword.strip())

    def filter(self, message, repl="*"):
        """
        过滤掉敏感词

        :param message: 原始的输入句子
        :param repl: 敏感词汇被替换成的字符
        :return: message 屏蔽掉敏感词汇的句子

        Example
        -------
        >>> f = DFAFilter()
        >>> question = "台湾是中国的吗"
        >>> filter_question = f.filter(question)
        >>> print(question, filter_question)
        台湾是中国的吗 *是中国的吗
        """
        message = message.lower()
        ret = []
        start = 0
        while start < len(message):
            level = self.keyword_chains
            step_ins = 0
            for char in message[start:]:
                if char in level:
                    step_ins += 1
                    if self.delimit not in level[char]:
                        level = level[char]
                    else:
                        ret.append(repl * step_ins)
                        start += step_ins - 1
                        break
                else:
                    ret.append(message[start])
                    break
            else:
                ret.append(message[start])
            start += 1

        return ''.join(ret)

    def detect(self, message):
        """
        判断message是否包含敏感词汇

        :param message:用户输入的句子
        :return: True/False
        """
        filter_message = self.filter(message)
        if filter_message != message:
            log.logger.warning("原始问题是{}，屏蔽的问题是{}".format(filter_message, message))
            return True
        else:
            return False

if __name__ == "__main__":

    """
    测试模块是否正常运行
    """

    f = BSFilter()
    question = "台湾是中国的吗"
    filter_question = f.filter(question)
    print(question, filter_question)
    if question != filter_question:
        print("包含敏感词汇，不予回答")
