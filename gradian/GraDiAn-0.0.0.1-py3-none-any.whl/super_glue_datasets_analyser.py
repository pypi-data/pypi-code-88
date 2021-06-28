import argparse
import json
import os

import datasets
from compare_tree_counts import compare_distributions
from count_trees import get_tree_count_arr
from tqdm import tqdm


def super_glue_tasks():
    tasks = {
        'cb': {'splits': ['train', 'test', 'validation'],
                  'atts': ['premise', 'hypothesis'],
                   'atts_to_drop': ['label']},
        #'axb': {'splits': ['test'],
                #'atts': ['sentence1', 'sentence2']},
        #'axg': {'splits': ['test'],
                #'atts': ['premise', 'hypothesis']},
        'copa': {'splits': ['train', 'test', 'validation'],
                 'atts': ['premise', 'choice1', 'choice2'],
                 'atts_to_drop': ['question', 'label']},
        'wsc': {'splits': ['train', 'test', 'validation'],
                'atts': ['text'],
                'atts_to_drop': ['span1_index', 'span2_index', 'span1_text',
                                 'span2_text', 'label']},
        'rte': {'splits': ['train', 'test', 'validation'],
                'atts': ['premise', 'hypothesis'],
                'atts_to_drop': ['label']},
        'wic': {'splits': ['train', 'test', 'validation'],
                'atts': ['word', 'sentence1', 'sentence2'],
                'atts_to_drop':['label', 'start1', 'start2', 'end1', 'end2']},
        'boolq': {'splits': ['train', 'test', 'validation'],
                  'atts': ['question', 'passage'],
                   'atts_to_drop': ['label']},
        'multirc': {'splits': ['train', 'test', 'validation'],
                    'atts': ['paragraph', 'question', 'answer'],
                    'atts_to_drop': ['label']},
        'record': {'splits': ['train', 'test', 'validation'],
                   'atts': ['passage', 'query'],
                    'atts_to_drop': ['entities', 'answers']}
    }
    return tasks


def analyse_tasks(tasks, percent_to_load, output_path=os.getcwd(), dump_results=False):
    comparisons= list()
    all_tree_counts = list()
    for k, v in tasks.items():
        tree_counts = list()
        for split in ['test', 'train']:
            print(k, split)
            ri = datasets.ReadInstruction(split, to=percent_to_load, unit='%')
            dataset = datasets.load_dataset('super_glue', k, split=ri)
            sentences_combined = list()

            # Extract sentences for analysis (ignoring dropped attributes e.g.
            # label)
            for attribute in v['atts']:
                sentences = [i[attribute] for i in tqdm(dataset)]
                sentences_combined += sentences

            tree_count = get_tree_count_arr(sentences_combined, attribute='pos')
            tree_counts.append(tree_count)
            all_tree_counts.append(tree_count)

            if dump_results == True:
                fp = os.path.join(output_path,f'{k}_{split}_pos_tree_count.json') 
                with open(fp, 'w') as f:
                    json.dump(tree_count, f, indent=2)

        comparison = compare_distributions(tree_counts[0], tree_counts[1])
        comparisons.append(comparison)
        if dump_results == True:
            fp = os.path.join(output_path, f"temp/{k}_test_train_comparison.json")
            with open(fp, 'w') as f:
                json.dump(comparison, f, indent=2) 
    
    return comparisons, all_tree_counts


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument('-o', '--output-path', type=str, required=True)
    p.add_argument('-p', '--percent-to-load', dest='percent_to_load',
                   type=int, default=100)
    options = p.parse_args()
    tasks = super_glue_tasks()
    analyse_tasks(tasks, options.percent_to_load, options.output_path,
                  dump_results=True)
