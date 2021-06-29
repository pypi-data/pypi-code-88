# -*- coding: utf-8 -*-
"""
计算各种距离
"""

import numpy as np
from sklearn.preprocessing import normalize
import Levenshtein
from scipy.spatial.distance import cdist


def get_distance_sim_matrix(matrix1, matrix2, metric='cosine'):
    """
    返回2个矩阵的各种距离和相似度

    :param matrix1: 句子向量1
    :param matrix2: 句子向量2
    :param metric: 'braycurtis', 'canberra', 'chebyshev', 'cityblock', 'correlation',
    'cosine', 'dice', 'euclidean', 'hamming', 'jaccard', 'jensenshannon',
    'kulsinski', 'mahalanobis', 'matching', 'minkowski', 'rogerstanimoto',
    'russellrao', 'seuclidean', 'sokalmichener', 'sokalsneath', 'sqeuclidean',
    'wminkowski', 'yule'
    :return:
    """
    dist = cdist(matrix1, matrix2, metric=metric)
    sim = 1. - normalize(dist, axis=1, norm='max')
    return dist, sim


def get_edit_distance(query_sen_list, candidate_sen_list):
    """
    计算编辑距离

    :param query_sen_list: 如['我爱中国', '美国总统特朗普']
    :param candidate_sen_list: 如['我爱地球', '美国总统拜登']
    :return:
    """

    distance_matrix = []
    for query_sen in query_sen_list:
        distance_list = []
        for candidate_sen in candidate_sen_list:
            dis = Levenshtein.distance(query_sen, candidate_sen)
            dis = float(dis) / max(len(query_sen), len(candidate_sen))
            distance_list.append(dis)
        distance_matrix.append(distance_list)
    distance_matrix = np.array(distance_matrix)
    return distance_matrix


def get_jaccard_sim(sen_list1, sen_list2, norm=False):
    """
    获得杰卡德相似度

    :param sen_list1: [['我', '爱','中国'], ['美国', '总统', '特朗普']]
    :param sen_list2: [['我', '爱','地球'], ['美国', '总统', '拜登']]
    :param norm:是否对结果进行归一化
    :return:
    """
    sim_matrix = []
    for sen1 in sen_list1:
        sim_list = []
        for sen2 in sen_list2:
            intersection = list(set(sen1).intersection(set(sen2)))
            union = list(set(sen1).union(set(sen2)))
            sim_list.append(float(len(intersection)) / len(union))
        if norm:
            max_v = max(sim_list)
            min_v = min(sim_list)
            if max_v == min_v:
                sim_matrix.append(
                    np.array([1. / len(sim_list) for _ in range(len(sim_list))]))
            else:
                sim_list = (np.array(sim_list) - min_v) / (max_v - min_v)
                sim_matrix.append(sim_list)
        else:
            sim_matrix.append(sim_list)
    return np.array(sim_matrix)


def get_edit_similarity(distance_matrix, norm=True):
    """
    先反转编辑距离矩阵，得到编辑相似度矩阵，然后可以选择归一化

    :param distance_matrix: 距离矩阵
    :param norm: True/False
    :return:
    """
    # 编辑相似度计算的另一种方式：sim_matrix = 1/(distance_matrix+1.)
    sim_matrix = 1 - distance_matrix
    if norm:
        sim_matrix = normalization(sim_matrix, reversed=False)
    return sim_matrix


def normalization(matrix, reversed=True):
    """
    归一化矩阵，按照最后一个维度

    :param matrix:
    :param reversed:
    :return:
    """
    maxs = matrix.max(axis=1)
    mins = matrix.min(axis=1)
    mins = np.repeat(mins, matrix.shape[-1]).reshape(matrix.shape)
    maxs = np.repeat(maxs, matrix.shape[-1]).reshape(matrix.shape)
    if reversed:
        return 1. - (matrix - mins) / (maxs - mins)
    else:
        return (matrix - mins) / (maxs - mins)


def match_topk(sim_matrix, topk=1, order=0):
    """
    返回相似度矩阵前topk/或者后topk

    :param sim_matrix:
    :param topk:
    :param order:
    :return:
    """
    if order == 0:
        return np.argsort(sim_matrix, axis=-1)[:, :topk]
    else:
        return np.argsort(sim_matrix, axis=-1)[:, -topk:]


if __name__ == '__main__':
    """
    测试模块是否正常运行
    """
    j_distance_matrix = get_jaccard_sim([['我', '爱', '中国'], ['美国', '总统', '特朗普']], [
                                        ['我', '爱', '地球'], ['美国', '总统', '拜登']], norm=False)
    print("杰卡德距离是: ", j_distance_matrix)
    e_distance_matrix = get_edit_distance(
        ['我爱中国', '美国总统特朗普'], ['我爱地球', '美国总统拜登'])
    print("编辑距离是: ", e_distance_matrix)
    e_similarity_matrix = get_edit_similarity(e_distance_matrix, norm=False)
    print("编辑相似度是: ", e_similarity_matrix)
    res_topk = match_topk(e_similarity_matrix, order=1)
    print(res_topk)
    print("测试函数 get_distance_sim_matrix ")
    res_dis, res_sim = get_distance_sim_matrix(np.random.random((5, 10)), np.random.random((5, 10)))
    print(res_sim.shape)