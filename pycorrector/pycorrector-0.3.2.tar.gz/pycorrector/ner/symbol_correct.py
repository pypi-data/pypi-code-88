# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 标点符号纠正
1. 训练模型
基于BIO的NER识别模型标注标点符号，然后按句子预测该一句话的文本的标点符号位置及标点类型，再跟原始文本比对标点是否一致。
训练单句的文本时，事先去掉标点符号，保留标点位置和类型；预测单句文本时也要去掉标点符号，通过预测的BIO判定标点位置和类型。
1.1 造训练样本
仅限于中文标点符号，包括，句子的界定：？。！短句的界定：、，：
标注BIO，由于所有标点符号只有一个字符长度，故没I标记，标记为：B-? B-。 B-！ B-、 B-，B-：
1.2 训练
由于不需要判断BI之间的相互依赖关系，故不需要CRF层。模型选型：Bert_softmax, ERNIE_fc, ERNIE_2.0_fc

2. 预测模型
预测BIO，然后转为标点即可。

3. 评估
准召率和F1
"""

import re
import os
symbols = ['？', '。', '！', '、', '，', '：', '?', '!', ',', ':']
en_ch_symbol_map = {
    '?': '？',
    '!': '！',
    ',': '，',
    ':': '：',
}


def get_bio_from_augment(aug_sent, details, B='B-R'):
    label_sent = ['O' for i in aug_sent]
    for i in range(len(aug_sent)):
        for detail in details:
            if i == detail[2]:
                label_sent[i] = B
    return ' '.join(aug_sent) + '\t' + ' '.join(label_sent)


def build_sample(sentence):
    """
    通过正常样本造些纠错样本
    :param sentence:
    :return:
    """
    if not sentence:
        return
    sentence_split = [i for i in sentence if i]
    label_split = ['O' for _ in sentence_split]
    for i in range(len(label_split)):
        for s in symbols:
            if sentence_split[i] == s:
                sentence_split[i] = ''
                label_split[i] = ''
                label_split[i - 1] = 'B-' + en_ch_symbol_map.get(s, s)
    sentence_split = [i for i in sentence_split if i]
    label_split = [i for i in label_split if i]
    if len(sentence_split) != len(label_split):
        print('error, size not match')
        return
    res = ' '.join(sentence_split) + '\t' + ' '.join(label_split)
    return res


def load_file(file_path):
    sentence_list = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            r = re.sub(r'%[0-9a-zA-Z]{2}', '', line)
            r = r.replace('#', '')
            r = re.sub(r'\{[^\)]*\}', '', r)
            sentence_list.append(r)
    return sentence_list


def save_corpus_data(data_list, data_path):
    dirname = os.path.dirname(data_path)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
    with open(data_path, 'w', encoding='utf-8') as f:
        count = 0
        for line in data_list:
            f.write(line + '\n')
            count += 1
        print("save line size:%d to %s" % (count, data_path))


if __name__ == '__main__':
    sents = load_file('output/sample.txt')
    outs = []
    for i in sents:
        r = build_sample(i)
        print(r)
        if r:
            outs.append(r)
    save_corpus_data(outs, 'output/sample_symbol.txt')
