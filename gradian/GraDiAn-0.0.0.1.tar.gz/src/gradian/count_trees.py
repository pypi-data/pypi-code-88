import argparse
import json
import os
from typing import List

import spacy
from pandas import read_csv
from pandas.core.frame import DataFrame
from spacytextblob.spacytextblob import SpacyTextBlob
from tqdm import tqdm

from sent_tree import SentTree


def get_tree_count(df: DataFrame, attribute: str):
    trees = dict()

    for i, s in df.iterrows():
        s_tree = SentTree.from_spacy_token([sent for sent in
                                            nlp(s['sentence']).sents][0].root,
                                          True)
        if attribute == 'multi':
            tree = str(s_tree.multi_attr_tree(['pos', 'sentiment'], False))
        else:
            tree = str(s_tree.attr_tree(attribute, False))
        if tree in trees.keys():
            trees[tree] = trees[tree] + 1
        else:
            trees[tree] = 1

        if i % 10000 == 0:
            print(i)

    sorted_trees = dict(sorted(trees.items(), key=lambda item: item[1],
                               reverse=True))
    return sorted_trees


def get_tree_count_arr(texts: List, attribute: str):
    trees = dict()

    for t in tqdm(texts):
        for sent in nlp(t).sents:
            s_tree = SentTree.from_spacy_token(sent.root,
                                              use_spacy_text_blob)
            if attribute == 'multi':
                tree = str(s_tree.multi_attr_tree(['pos', 'sentiment'], False))
            else:
                tree = str(s_tree.attr_tree(attribute, False))
            if tree in trees.keys():
                trees[tree]['count'] += 1
                trees[tree]['texts'].append(sent.text)
            else:
                trees[tree] = dict()
                trees[tree]['count'] = 1
                trees[tree]['texts'] = [sent.text]

    sorted_trees = dict(sorted(trees.items(), key=lambda item: item[1]['count'],
                               reverse=True))
    return sorted_trees
 

def get_tree_count_single(text: str, attribute: str):
    trees = dict()

    for sent in nlp(text).sents:
        s_tree = SentTree.from_spacy_token(sent.root,
                                          True)
        if attribute == 'multi':
            tree = str(s_tree.multi_attr_tree(['pos', 'sentiment'], False))
        else:
            tree = str(s_tree.attr_tree(attribute, False))
        if tree in trees.keys():
            trees[tree]['count'] += 1
            trees[tree]['texts'].append(sent.text)
        else:
            trees[tree] = dict()
            trees[tree]['count'] = 1
            trees[tree]['texts'] = [sent.text]
    return trees


def main(args):
    testset_path = args.data_sets[0]
    trainset_path = args.data_sets[1]
    df_test = read_csv(testset_path, sep='\t')
    df_train = read_csv(trainset_path, sep='\t')
    attribute = args.attribute

    test_trees = get_tree_count(df_test, attribute)
    if args.output_path is not None:
        with open(os.path.join(args.output_path, f'test_count_{attribute}.json'), 'w') as f:
            json.dump(test_trees, f, indent=2)

    train_trees = get_tree_count(df_train, attribute)
    if args.output_path is not None:
        with open(os.path.join(args.output_path, f'train_count_{attribute}.json'), 'w') as f:
            json.dump(train_trees, f, indent=2)

    return


if __name__ == "__main__":
    nlp = spacy.load("en_core_web_trf",
                     exclude=['ner', 'attribute_ruler', 'lemmatizer',
                              'token2vec'])  # Globally instantiated 

    p = argparse.ArgumentParser()
    p.add_argument('-d', '--data_sets', type=str, nargs=2,
                   default=['datasets/SST-2/test.tsv',
                            'datasets/SST-2/train.tsv'])
    p.add_argument('-o', '--output_path', type=str, default=None)
    p.add_argument('-a', '--attribute', type=str, default='pos')
    p.add_argument('-t', '--text-blob', type=bool, default=False)
    args = p.parse_args()

    if args.text_blob:
        nlp.add_pipe('spacytextblob')

    main(args)
