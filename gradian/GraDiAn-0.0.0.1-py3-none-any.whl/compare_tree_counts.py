import argparse
import json
import os
from tqdm import tqdm
from scipy.stats import chisquare


def find_missing(d1, d2):
    missing = dict()
    for tree, stats in tqdm(d1.items()):
        if tree not in d2.keys():
            missing[tree] = stats
    return missing

def compare_distributions(d1, d2):
    results = dict()
    expected_frequencies = list()
    observed_frequencies = list()
    total_d1 = sum([t['count'] for t in d1.values()])
    total_d2 = sum([t['count'] for t in d2.values()])
    missing_count = 0
    for tree, stats in tqdm(d1.items()):
        expected_frequencies.append((stats['count']/total_d1)*total_d2)
        if tree not in d2.keys():
            portion_of_test = stats['count']/total_d1
            portion_of_train = 0
            missing_count += 1
            results[tree] = {'prop_diff': portion_of_test,
                             'test_portion': portion_of_test,
                             'train_portion': portion_of_train,
                             'example': stats['texts'][0]
                            }
            observed_frequencies.append(0)
        else:
            observed_frequencies.append(d2[tree]['count'])
            portion_of_test = stats['count']/total_d1
            portion_of_train = d2[tree]['count']/total_d2
            results[tree] = {'prop_diff': portion_of_test-portion_of_train,
                             'test_portion': portion_of_test,
                             'train_portion': portion_of_train,
                             'example': stats['texts'][0]
                            }
    sorted_results = dict(sorted(results.items(), key=lambda item:
                                 abs(item[1]['prop_diff']),
                                 reverse=True))
    total_share_difference = sum([abs(v['prop_diff']) for v in
                                  sorted_results.values()])

    #chisq, p = chisquare(observed_frequencies, expected_frequencies,
                         #ddof=len(expected_frequencies)-1)
    return {'results': {**sorted_results}, 
            'missing_proportion': missing_count/total_d1,
            'test_length':len(d1), 'training_length':len(d2), 
            'total_difference': total_share_difference}
            #'chisq': chisq, 'p': p}


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument('-d', '--data_sets', type=str, required=True, nargs=2)
    p.add_argument('-o', '--output_path', type=str, required=True)
    p.add_argument('-f', '--full-comparison', dest='full', action='store_true')
    options = p.parse_args()
    test_set_fp = options.data_sets[0]
    train_set_fp = options.data_sets[1]
    with open(test_set_fp, 'r') as f:
        d1 = json.load(f)
    with open(train_set_fp, 'r') as f:
        d2 = json.load(f)
    if options.full:
        res = compare_distributions(d1, d2)
        file_name = f"{test_set_fp.split('.')[0]}_{train_set_fp.split('.')[0]}_comparison.json"
        with open(os.path.join(options.output_path, file_name), 'w') as f:
            json.dump(res, f, indent=2) 
    else:
        missing = find_missing(d1, d2)
        with open(os.path.join(options.output_path, 'missing.json'), 'w') as f:
            json.dump(missing, f,indent=2) 
