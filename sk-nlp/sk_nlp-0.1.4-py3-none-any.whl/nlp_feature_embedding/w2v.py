# -*- coding:utf-8 -*-
"""
传统的w2v模型:包含skip-gram和cbow
目前有一个从wiki语料训练出来的100维度的skip-gram模型
"""
import gensim
from gensim.models import word2vec
import numpy as np
from sk_nlp.util.file import file_exist
from sk_nlp.util import log, file_conf


class WordEmbedding(object):

    def __init__(self, model_file_path=file_conf.wiki_sg_file_path,
                 embedding_dim=100):
        """
        加载已经训练好的wiki词向量sg
        :param model_file_path: 模型的路径，默认为 /model/w2v/skip_gram_wiki2Vec.h5
        """
        self.wv_model = None
        if model_file_path and file_exist(model_file_path):
            self.wv_model = gensim.models.Word2Vec.load(model_file_path)
        else:
            log.logger.warning("模型文件不存在")
        self.unknow = 'unk'
        self.embedding_dim = embedding_dim

    def fine_tune(self, new_seg_list, model_file_path):
        """
        基于已有的w2v模型，使用其他语料进行微调。然后保存模型路径。

        :param new_seg_list: 新句子（分词后）
        :param model_file_path: 模型的保存路径
        :return:

        Example
        -------
        >>> model = WordEmbedding()
        >>> model.get_embedding()
        >>> new_seg_list = [['我', '爱','中国'], ['美国', '总统', '特朗普']]
        >>> model.fine_tune(new_seg_list, file_conf.ft_wiki_sg_file_path)

        """
        if self.wv_model:
            self.wv_model.build_vocab(new_seg_list, update=True)
            self.wv_model.train(new_seg_list, total_examples=self.wv_model.corpus_count, epochs=5)
            self.wv_model.save(model_file_path)
        else:
            log.logger.warning("模型为None,请先加载/训练模型")

    def get_embedding(self):
        """
        获取词向量模型的信息

        :return: embedding_matrix:词向量矩阵；index_word：索引到单词的映射； word_index：单词到索引的映射
        """
        if not self.wv_model:
            log.logger.warning("模型为None,请先加载已有模型或使用train_vec()函数训练模型")
        index_word = {}
        word_index = {}
        word2embed = self.wv_model.wv
        unknow_index = len(index_word)
        index_word[unknow_index] = self.unknow
        word_index[self.unknow] = unknow_index
        for index in range(len(word2embed.index_to_key)):
            index_word[index + 1] = word2embed.index_to_key[index]
            word_index[word2embed.index_to_key[index]] = index + 1
        embedding_matrix = np.zeros((len(word_index), self.embedding_dim))
        for word, i in word_index.items():
            if word in word2embed:  # words not found in embedding index will be all-zeros.
                embedding_vector = word2embed[word]
                embedding_matrix[i] = embedding_vector
        return embedding_matrix, index_word, word_index

    def train_vec(self, sentence_list, model_file_path,
                  window=5, min_count=5, sg=0):
        """
        使用w2v训练词向量

        :param sentence_list: 句子列表，[['我', '爱','中国'], ['美国', '总统', '特朗普']]
        :param model_file_path: 模型保存路径
        :param window: 滑动窗口
        :param min_count: 最小词频
        :param sg: 0是使用cbow, 1是使用跳字模型
        :return:
        """
        model = word2vec.Word2Vec(sentence_list,
                                  vector_size=self.embedding_dim,
                                  window=window, min_count=min_count,
                                  sg=sg)
        self.wv_model = model
        model.save(model_file_path)

    def op2model(self):
        """
        由于w2v的接口太多，不太好封装
        这里给出了模型的一些常用操作范例

        :return:
        """
        if not self.wv_model:
            log.logger.warning("模型为None,请先加载已有模型或使用train_vec()函数训练模型")
        #返回给定上下文可能的中心词
        print(model.wv_model.predict_output_word(['我', '爱', '中国']))
        #返回词语的相似程度
        print(model.wv_model.wv.similarity(u"陕西省", u"山西省"))
        #返回给定词语的前n个相似内容
        print(model.wv_model.wv.most_similar(u"陕西省", topn=5))


if __name__ == '__main__':
    """
    测试模块是否正常运行
    """
    model = WordEmbedding(model_file_path=None)
    model.train_vec(['我 爱 中国'.split(), '中国 是 发展 中 国家'.split(), '新疆 是 中国 省份'.split()],
                    model_file_path=file_conf.test_vec_file_path,
                    min_count=1)
    embedding_matrix, index_word, word_index = model.get_embedding()
    new_seg_list = [['我', '爱','中国'], ['美国', '总统', '特朗普']]
    print(index_word)
    #使用领域内的语料微调
    print(model.wv_model.predict_output_word(['我', '爱', '中国']))
    model.fine_tune(new_seg_list, file_conf.ft_wiki_sg_file_path)
    print(model.wv_model.wv.most_similar('中国'))



