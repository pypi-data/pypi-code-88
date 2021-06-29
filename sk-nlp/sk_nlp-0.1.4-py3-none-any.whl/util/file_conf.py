# -*- coding: utf-8 -*-

import os

current_dir = os.path.dirname(__file__)
project_path = os.path.dirname(current_dir)

log_dir = os.path.join(project_path, 'log')
log_file_path = os.path.join(log_dir, 'ml.txt')

data_dir = os.path.join(project_path, 'data')
stop_word_dir = os.path.join(data_dir, 'stopword')

chinese_synonyms_dir = os.path.join(data_dir, "chinese_synonyms.txt")
dirty_word_file_path = os.path.join(data_dir, "dirty_word.txt")

model_dir = os.path.join(project_path, 'model')
tf_idf_file_path = os.path.join(model_dir, 'tf_idf.h5')
wv_dir = os.path.join(model_dir, "w2v")
wiki_sg_file_path = os.path.join(wv_dir, "skip_gram_wiki2Vec.h5")
test_wv_dir = os.path.join(wv_dir, "test")
ft_wiki_sg_file_path = os.path.join(test_wv_dir, "ft_test_vec.h5")
test_vec_file_path = os.path.join(test_wv_dir, "test_vec.h5")

bert_dir = os.path.join(model_dir, "bert")
chinese_L12_H_768_A_12bert_dir = os.path.join(bert_dir, 'chinese_L-12_H-768_A-12')
bert_vocab_file_path = os.path.join(chinese_L12_H_768_A_12bert_dir, 'vocab.txt')
bert_config_file_path = os.path.join(chinese_L12_H_768_A_12bert_dir, 'bert_config.json')
bert_checkpoint_path = os.path.join(chinese_L12_H_768_A_12bert_dir, 'bert_model.ckpt')