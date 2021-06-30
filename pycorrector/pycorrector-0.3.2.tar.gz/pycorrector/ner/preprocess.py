# -*- coding: utf-8 -*-
# Author: XuMing(xuming624@qq.com)
# Brief:
import os
import re
import sys
from xml.dom import minidom

sys.path.append('../..')
from pycorrector.utils.tokenizer import segment


def parse_cged_xml_file(path, use_segment, segment_type, delete_w=False):
    print('Parse data from %s' % path)
    res = []
    dom_tree = minidom.parse(path)
    docs = dom_tree.documentElement.getElementsByTagName('DOC')

    for doc in docs:
        # Input the text
        text = doc.getElementsByTagName('TEXT')[0]. \
            childNodes[0].data.strip()
        # Segment
        word_seq = segment(text.strip(), cut_type=segment_type) if use_segment else list(text.strip())
        label_seq = []
        errors = doc.getElementsByTagName('ERROR')
        # Locate the error position and error type
        locate_dict = {}
        is_W = False
        for error in errors:
            start_off = error.getAttribute('start_off')
            end_off = error.getAttribute('end_off')
            error_type = error.getAttribute('type')
            if error_type in ['W'] and delete_w:
                is_W = True
                break
            for i in range(int(start_off) - 1, int(end_off)):
                if i == int(start_off) - 1:
                    error_type_change = 'B-' + error_type
                else:
                    error_type_change = 'I-' + error_type
                locate_dict[i] = error_type_change
        if is_W and delete_w:
            print("pass W error type")
            continue

        label_seq = []
        for i in range(len(word_seq)):
            if i in locate_dict:
                # Fill with error type
                label_seq.append(locate_dict[i])
            else:
                # Fill with 'O'
                label_seq.append('O')
        if len(word_seq) != len(label_seq):
            print("error, size not match, word_seq:", len(word_seq), ' label_seq:', len(label_seq))
            continue
        res.append(' '.join(word_seq) + '\t' + ' '.join(label_seq))
    return res


def parse_sighan_tsv_file(path, use_segment, segment_type):
    data_list = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) != 2:
                continue
            target = ' '.join(segment(parts[1].strip(), cut_type=segment_type)) if use_segment else parts[1].strip()
            data_list.append(target)
    return data_list


def save_corpus_data(data_list, data_path):
    dirname = os.path.dirname(data_path)
    os.makedirs(dirname, exist_ok=True)
    with open(data_path, 'w', encoding='utf-8') as f:
        count = 0
        for line in data_list:
            f.write(line + '\n')
            count += 1
        print("save line size:%d to %s" % (count, data_path))


class CharTokenizer(object):
    """Given Full tokenization."""

    def __init__(self, lower=True):
        self.lower = lower

    def tokenize(self, text):
        """Tokenizes a piece of text."""
        res = []
        if len(text) == 0:
            return res

        if self.lower:
            text = text.lower()
        # for the multilingual and Chinese
        res = list(text)
        return res


def get_bio_from_augment(aug_sent, details, B='B-R', I='I-R'):
    label_sent = ['O' for i in aug_sent]
    for i in range(len(aug_sent)):
        for detail in details:
            if i == detail[2]:
                label_sent[i] = B
    return ' '.join(aug_sent) + '\t' + ' '.join(label_sent)


def data_augmentation(sentence_list):
    """
    文本数据增强，通过正常造些纠错样本
    限制：一句话最多一个错误类型，一句话最多一个字出错
    错误类型：insert, delete, replace, disorder
    :param sentence_list:
    :return:
    """
    res = []
    from textgen.augment import TextAugment
    m = TextAugment(sentence_list, tokenizer=CharTokenizer())
    for sentence in sentence_list:
        insert_sent, insert_details = m.augment(sentence, aug_ops='insert-0.02')
        delete_sent, delete_details = m.augment(sentence, aug_ops='delete-0.02')
        replace_sent, replace_details = m.augment(sentence, aug_ops='random-0.02')
        if insert_details:
            print(insert_sent, insert_details)
            res.append(get_bio_from_augment(insert_sent, insert_details, 'B-R', 'I-R'))

        if delete_details:
            print(delete_sent, delete_details)
            res.append(get_bio_from_augment(delete_sent, delete_details, 'B-M', 'I-M'))

        if replace_details:
            print(replace_sent, replace_details)
            res.append(get_bio_from_augment(replace_sent, replace_details, 'B-S', 'I-S'))

        label_sent = ['O' for i in sentence]
        res.append(' '.join(sentence) + '\t' + ' '.join(label_sent))
    return res


def remove_noisy(content):
    """
    移除括号内的信息，去除噪声
    :param content:
    :return:
    """
    p1 = re.compile(r'（[^）]*）')
    p2 = re.compile(r'\([^\)]*\)')
    return p2.sub('', p1.sub('', content))


def remove_feed_noisy(line):
    line = line.strip()
    r = re.sub(r'%[0-9a-zA-Z]{2}', '', line)
    r = r.replace('#', '')
    r = re.sub(r'\{[^\)]*\}', '', r)
    return r


def build_bio_sample(src_sent, trg_sent):
    # 少字：我 不 大 想 学 习 英 语 。	我 不 大 想 习 英 语 。
    # 多字：我 不 大 想 学 习 英 语 。	我 不 大 想 学 学 习 英 语 。
    # 错字：我 不 大 想 学 习 英 语 。	我 不 大 想 学 细 英 语 。
    # 多错字：我 不 大 想 学 习 英 语 。	我 不 大 想 学 习 细 英 语 。
    """
    print(lcs("我大想学习英语。", "我不大想习英语。"))
    print(lcs("我1不大想学习英语。", "我不大想习英语。"))
    print(lcs("我1不大想学习英语。52", "我11不大想习英语。1"))
    print(lcs("我1不大想学习英语。12", "我11不大想习英语。1"))
    print(lcs("我1不大想学习英语。123", "我11不大想习英语。1"))
    """
    diffs = lcs(src_sent, trg_sent)
    src_len = len(src_sent)
    trg_len = len(trg_sent)
    p = []
    j = 0
    for i in range(len(src_sent)):
        for j in range(len(diffs)):
            m,n = diffs[j]
            # 若src有，trg无，则是多字
            if len(diffs) > 1:
                j_ = j+1
                m,n = diffs[j_]
                if n > m:
                    p.append({n:'R'})
                elif n == m:
                    print('error, n==m')
                elif n<m:
                    p.append({n:'M'})
            elif trg_len > src_len:
                p.append({n:'R'})
            elif trg_len <= src_len:
                print('error, trg_len <=src_len')
            # 若src无，trg有，则是少字

            # 若src跟trg不同，则是错字
            if src_sent[m] == trg_sent[n]:
                continue
            else:
                p.append(i)
                j += 1
        j += 1


def levenshtein_distance(str1, str2):
    """
    计算字符串 str1 和 str2 的编辑距离
    :param str1
    :param str2
    :return:
    """
    matrix = [[i + j for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                d = 0
            else:
                d = 1

            matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + d)
    return matrix[len(str1)][len(str2)]


def lcs(list_n, list_m):
    print(list_n, list_m)
    # 计算LCS的长度
    n = len(list_n)
    m = len(list_m)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if list_n[i - 1] == list_m[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    # 输出LCS
    if dp[-1][-1] == 0:
        return -1
    list_LCS = []
    i, j = n, m
    diff = []
    while i > 0 and j > 0:
        if list_n[i - 1] == list_m[j - 1]:

            list_LCS.append(list_n[i - 1])
            i -= 1
            j -= 1
            continue
        else:
            if dp[i][j - 1] >= dp[i - 1][j]:
                j -= 1
            else:
                i -= 1
            diff.append((i,j))
    # print(diff)
    # return ''.join(list(reversed(list_LCS)))
    return list(reversed(diff))


if __name__ == '__main__':
    # train data
    # data_list = []
    # if config.dataset == 'sighan':
    #     data = parse_sighan_tsv_file(config.sighan_train_path, config.use_segment, config.segment_type)
    #     data_list.extend(data)
    # else:
    #     for path in config.cged_train_paths:
    #         data_list.extend(parse_cged_xml_file(path, config.use_segment, config.segment_type, delete_w=True))
    # # save data
    # save_corpus_data(data_list, config.train_path)
    print(levenshtein_distance("我 不 大 想 学 习 英 语 。", "我 不 大 想 习 英 语 。"))
    print(lcs("我大想学习英语。", "我不大想习英语。"))
    print(lcs("我1不大想学习英语。", "我不大想习英语。"))
    print(lcs("我1不大想学习英语。52", "我11不大想习英语。1"))
    print(lcs("我1不大想学习英语。12", "我11不大想习英语。1"))
    print(lcs("我1不大想学习英语。123", "我11不大想习英语。1"))
    sentence_list = []
    with open('output/sample.txt', 'r', encoding='utf-8') as f:
        for line in f:
            sentence_list.append(line.strip())
    # res = data_augmentation(sentence_list)
    # save_corpus_data(res, 'output/sample_aug.txt')
