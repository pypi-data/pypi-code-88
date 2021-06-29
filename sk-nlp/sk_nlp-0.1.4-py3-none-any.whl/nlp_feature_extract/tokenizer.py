# -*- coding:utf-8 -*-
"""
词语粒度的操作模块：分词，去停用词，同义词林转换
"""

from sk_nlp.util import tool, file_conf
import jieba
import os
from sk_common.file import file_reader

class StopWord(object):
    """
    停用词操作类：
    停用词汇表路径存放在 sk-nlp/data/stopword
    """

    def __init__(self, source='', define_stop_word=[]):
        """

        :param source: 可选的停用词库：wiki,cn,hit,baidu,scu，默认为不使用
        :param define_stop_word: 用户自定义的停用词列表

        Example
        -------
        >>> sw = StopWord('scu', define_stop_word=['我'])
        >>> print(sw.stop_word_list)
        ['简而言之', '极了', '唉', '从新', '啦',...]
        """
        self.source = source
        self.stop_word_list = self.merge_stop_word(define_stop_word)


    def load_stop_word(self):
        """
        根据不同的self.source加载不同的停用词表

        :return: stop_word_list 停用词列表

        """

        if self.source == 'wiki':
            return file_reader.read_txt_to_list(os.path.join(file_conf.stop_word_dir, "wiki_stop_word.txt"))
        elif self.source == 'cn':
            return file_reader.read_txt_to_list(os.path.join(file_conf.stop_word_dir, "cn_stopwords.txt"))
        elif self.source == 'hit':
            return file_reader.read_txt_to_list(os.path.join(file_conf.stop_word_dir, "hit_stopwords.txt"))
        elif self.source == 'baidu':
            return file_reader.read_txt_to_list(os.path.join(file_conf.stop_word_dir, "baidu_stopwords.txt"))
        elif self.source == 'scu':
            return file_reader.read_txt_to_list(os.path.join(file_conf.stop_word_dir, "scu_stopwords.txt"))
        else:
            return []

    def merge_stop_word(self, define_stop_word):
        """
        将用户自定义的停用词和用户指定的通用词库合并成一个list

        :param define_stop_word: 用户给的自定义停用词列表 list
        :return: stop_word_list 停用词列表
        """
        default_stop_word = self.load_stop_word()
        default_stop_word = [ele[0] for ele in default_stop_word]
        return list(set(default_stop_word).union(set(define_stop_word)))


class SentenceCut(object):
    """
    句子分词操作类
    目前集成了jieba分词
    """

    def __init__(self, is_lower=True, stopword_list=[], use_chinese_synonyms=False):
        """

        :param is_lower: 英文是否统一小写
        :param stopword_list: 输入需要去除的停用词列表
        :param use_chinese_synonyms: 是否需要将语义相同的词归一化
        """

        self.is_lower = is_lower
        self.stopword_list = stopword_list
        self.use_chinese_synonyms = use_chinese_synonyms
        if self.use_chinese_synonyms:
            self.union_find, self.synonyms_word_list = self.load_chinese_synonyms()


    def cut_word(self, sentence_list):
        """
        对传进来的句子进行分词

        :param sentence_list:['我爱中国', '我是中国人']
        :return:seg_lists [['我', '爱', '中国'], ['我', '是', '中国', '人']]  token_count {'我': 2, '爱': 1, '中国': 2, '是': 1, '人': 1}

        Example
        -------
        >>> sen_cut = SentenceCut(use_chinese_synonyms=True)
        >>> seg_lists, token_count = sen_cut.cut_word(['我爱baidu', '我是中国人'])
        >>> print(seg_lists, token_count)
        [['我', '爱', '百度'], ['我', '是', '中国', '人']]
        {'我': 2, '爱': 1, '百度': 1, '是': 1, '中国': 1, '人': 1}
        """

        seg_lists = []
        token_count = {}
        for sentence in sentence_list:
            word_list = jieba.cut(sentence, cut_all=False)
            filter_word_list = []
            for word in word_list:
                word = word.strip()
                if len(word) < 1:
                    continue
                if self.is_lower:
                    word = word.lower()
                if word not in self.stopword_list:
                    if self.use_chinese_synonyms and word in self.synonyms_word_list:
                        word = self.union_find.findFather(word)
                    filter_word_list.append(word)
                    if word not in token_count:
                        token_count[word] = 1
                    else:
                        token_count[word] += 1
            seg_lists.append(filter_word_list)
        return seg_lists, token_count

    def load_chinese_synonyms(self):
        """
        加载同义词林

        :return: union_find （并查集实例），word_list（同义词林所有的单词集合）
        """
        chinese_synonyms_list = file_reader.read_txt_to_list(file_conf.chinese_synonyms_dir)
        word_set = set()
        for element in chinese_synonyms_list:
            ele1, ele2 = element[0], element[1]
            word_set.add(ele1.strip())
            word_set.add(ele2.strip())
        word_list = list(word_set)
        union_find = tool.UnionFindSet(word_list)
        for element in chinese_synonyms_list:
            ele1, ele2 = element[0], element[1]
            union_find.union(ele1.strip(), ele2.strip())
        return union_find, word_list


if __name__ == '__main__':
    """
    测试模块是否正常运行
    """

    sw = StopWord('cn', define_stop_word=['我'])
    print(sw.stop_word_list)
    sen_cut = SentenceCut(use_chinese_synonyms=True)
    seg_lists, token_count = sen_cut.cut_word(['我爱baidu', '我是中国人'])
    print(seg_lists, token_count)