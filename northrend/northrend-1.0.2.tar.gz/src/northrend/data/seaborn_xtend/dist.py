from matplotlib import pyplot as plt
import seaborn as sns

import numpy as np


def plot_hist(df, sample=True, n_cols=3, **histplot_kwargs):
    sample_threshold = 100000
    if sample:
        sample_number = min(sample_threshold, df.shape[0])
    _df = df.sample(sample_number)

    _df = _df.select_dtypes(include="number")

    n_rows = _df.shape[1] / n_cols
    n_rows = np.ceil(n_rows)
    n_rows = int(n_rows)

    fig, axes = plt.subplots(nrows=n_rows, ncols=n_cols, figsize=(20, 15))

    for i, column in enumerate(_df.columns):
        sns.histplot(
            _df[column], bins=50, ax=axes[i // n_cols, i % n_cols], **histplot_kwargs
        )
    plt.tight_layout()
