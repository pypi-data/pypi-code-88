#!/usr/bin/env python3
from collections import Counter
from fuzzywuzzy import fuzz
import numpy as np
import pandas as pd
import re
import string

# TODO(danj): word stemming?


def identify_stop_words(series, n):
    series = normalize(series)
    top = Counter(series.explode()).most_common(n)
    for (i, (token, count)) in enumerate(top):
        print(f'{i:3d}: [{count:6d}] {token}')
    vals = input('Enter stop word indices [i.e. 1, 4, 26]: ')
    idxs = [int(idx) for idx in re.split(r'[\s,]+', vals.strip())]
    return set(np.array([token for token, _ in top])[idxs])


def normalize(series):
    def f(v):
        remove_punctuation = str.maketrans('', '', string.punctuation)
        try:
            x = v.upper().translate(remove_punctuation).split()
        except Exception:
            return []
        return x

    return series.apply(f)


def harmonize(series, threshold, stop_words):
    series = series.sort_values()
    name = series.name
    cleaned = remove_stop_words(
        normalize(series), stop_words).apply(lambda tokens: ' '.join(tokens))
    cleaned_name = name + '_harmonizer_cleaned'
    df = pd.DataFrame({
        name: series,
        cleaned_name: cleaned
    },
                      index=series.index)
    scores = [0]
    ids = [0]
    prev = None
    for idx, curr in df.iterrows():
        if prev is None:
            prev = curr
            continue
        tsr = fuzz.token_sort_ratio(prev[cleaned_name], curr[cleaned_name])
        pr = fuzz.partial_ratio(str(prev[name]), str(curr[name]))
        score = 2 * tsr * pr / (tsr + pr + 1e-10)
        scores.append(score)
        if score > threshold * 100:
            ids.append(ids[-1])
        else:
            ids.append(ids[-1] + 1)
        prev = curr
    id_col = name + '_harmonizer_id'
    df[name + '_harmonizer_score'] = scores
    df[id_col] = ids
    standardized_names = {}
    for _, group in df.groupby(id_col):
        harmonizer_id = None
        longest_name = None
        max_len = 0
        for _, row in group.iterrows():
            harmonizer_id = row[id_col]
            this_len = len(str(row[cleaned_name]))
            if this_len > max_len:
                max_len = this_len
                longest_name = row[name]
        standardized_names[harmonizer_id] = longest_name
    df[name + '_harmonizer_standardized'] = df[id_col].map(standardized_names)
    return df


def remove_stop_words(series, stop_words):
    def f(v):
        return [x for x in v if x not in stop_words]

    return series.apply(f)
