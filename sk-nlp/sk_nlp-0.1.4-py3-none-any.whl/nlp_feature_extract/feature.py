# -*- coding:utf-8 -*-
"""
0 使用ac自动机统计给定的词语的词频
1 获取tf-idf特征
"""
from sk_nlp.util import io, tool, file_conf
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd


class CountByAC(object):
    """
    基于ac自动机来统计模式串

    :param pattern_list: 匹配的模式串列表
    """

    def __init__(self, pattern_list=[]):
        """

        :param pattern_list: 匹配的模式串列表
        """
        self.ac = tool.AC()
        self.build_tree(pattern_list)

    def build_tree(self, pattern_list):
        """
        构建模式串前缀树

        :param pattern_list: 模式串列表
        """
        for p in pattern_list:
            self.ac.add(p)
        self.ac.make_fail()

    def count(self, sentence):
        """
        统计sentence中关于给定的模式串的频率

        :param sentence: 句子
        :return: word_count 每个关键词对应的频率
        Example
        -------
        >>> ac = CountByAC(['杰伦的七', '周杰伦的', '七里香'])
        >>> result = ac.count('周杰伦的七里香七里香')
        >>> print(result)
        {'周杰伦的': 1, '杰伦的七': 1, '七里香': 2}
        """

        result = self.ac.search(sentence)
        word_count = {}
        for word in result:
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1
        return word_count


class KeyWordExtract(object):
    """
    关键词抽取算法，基于tf-idf

    """

    def train_tf_idf(self, sentence_list, model_file, ngram_range=(1, 1)):
        """
        训练tf-idf模型，保存模型，返回模型和特征

        :param sentence_list: 句子列表（分词后）
        :param model_file: tf-idf模型保存文件
        :return: tf_idf_model, tfidf_feature
        """

        tf_idf_model = TfidfVectorizer(ngram_range=ngram_range)
        tfidf_feature = tf_idf_model.fit_transform(sentence_list)
        io.save_model(tf_idf_model, model_file, mode='wb')
        return tf_idf_model, tfidf_feature

    def get_tf_idf(self, sentence_list, model_file):
        """
        加载tf-idf模型，返回sentence_list对应的特征和模型

        :param sentence_list: 句子列表（分词后）
        :param model_file: tf-idf模型文件
        :return: tf_idf_model(模型实例), tfidf_feature(sentence_list对应的tf-idf特征)

        Example
        -------
        >>> tf_idf_model, tfidf_feature = kwe.get_tf_idf(['杰伦 是 台湾 歌手', '七里香 是 杰伦 创作'], file_conf.tf_idf_file_path)
        >>> print(tfidf_feature)
          (0, 4)	0.6316672017376245
          (0, 3)	0.4494364165239821
          (0, 2)	0.6316672017376245
          (1, 3)	0.4494364165239821
          (1, 1)	0.6316672017376245
          (1, 0)	0.6316672017376245
        """

        tf_idf_model = io.load_model(model_file, mode='rb')
        tfidf_feature = tf_idf_model.transform(sentence_list)
        return tf_idf_model, tfidf_feature

    def get_topk_keywords(self, data_list, topk=200):
        """
        得到topk个关键词

        :param data_list: 句子列表（分词后）
        :param topk: tf-idf重要度排序后前topk
        :return: keywords

        Example
        -------
        >>> keywords = kwe.get_topk_keywords(['杰伦 是 台湾 歌手', '七里香 是 杰伦 创作'], topk=1)
        >>> print(keywords)
        [['歌手']['创作']]

        """
        vectorizer = TfidfVectorizer()
        tf_idf = vectorizer.fit_transform(data_list)
        sort_tf_idf = np.argsort(tf_idf.toarray(), axis=1)[:, -topk:]
        names = vectorizer.get_feature_names()
        keywords = pd.Index(names)[sort_tf_idf].values
        return keywords


if __name__ == '__main__':
    """
    测试模块是否正常运行
    """
    ac = CountByAC(['杰伦的七', '周杰伦的', '七里香'])
    result = ac.count('周杰伦的七里香七里香')
    print(result)

    kwe = KeyWordExtract()
    tf_idf_model, tfidf_feature = kwe.train_tf_idf(
        ['杰伦 是 台湾 歌手', '七里香 是 杰伦 创作'], file_conf.tf_idf_file_path)
    # 有n个词语，矩阵的维度就为n*n,而且是一个下（上）三角对称矩阵
    tf_idf_model, tfidf_feature = kwe.get_tf_idf(
        ['杰伦 是 台湾 歌手', '七里香 是 杰伦 创作'], file_conf.tf_idf_file_path)
    print(tfidf_feature)

    keywords = kwe.get_topk_keywords(['杰伦 是 台湾 歌手', '七里香 是 杰伦 创作'], topk=1)
    print(keywords)
