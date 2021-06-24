import numpy as np
import pandas as pd
import pdb

np.random.seed(0)
raw_data = pd.read_csv("all_2018_processed.txt",
                        delimiter = "\t", header = 0)
new_data = pd.read_csv("all_2018_processed_cleaned_data.txt",
                        delimiter = "\t", header = 0)
print(np.all(raw_data.columns == new_data.columns))

raw_data = raw_data.to_numpy()
new_data = new_data.to_numpy()
expected_equal_vals = np.sum(np.isnan(new_data) == False)
actual_equal_vals = np.sum(raw_data == new_data)
print(expected_equal_vals == actual_equal_vals)

counts = np.array([len(np.unique(col[np.isnan(col) == False]))
                   for col in raw_data.T])
raw_data = raw_data[:, counts >= 10]
new_data = new_data[:, counts >= 10]
lbs = np.nanmin(new_data, axis = 0)
ubs = np.nanmax(new_data, axis = 0)
is_inlier = np.logical_and(raw_data <= ubs, raw_data >= lbs)
raw_counts = np.sum(is_inlier, axis = 0)
new_counts = np.sum(np.isnan(new_data) == False, axis = 0)
error_message = "Not all outliers have been removed and/or "
error_message += "non-outlier points have been removed"
print(np.all(raw_counts == new_counts))

old_counts = np.sum(np.isnan(raw_data) == False, axis = 0)
percents = new_counts/old_counts
bootstraps = np.random.choice(percents, (len(percents), 1000000))
bs_means = np.mean(bootstraps, axis = 0)
CI = np.percentile(bs_means, [2.5, 97.5])
print(CI)
