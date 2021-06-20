"""Generating synthetic data for JRC to test Quality Check Software
July, 2020
"""
import numpy as np
import pandas as pd
from synthesis.synthesizers.marginal import MarginalSynthesizer

data_path = r"c:/data/1_iknl/processed/jrc/CancerCases_NL_nov2016_fixcolumns.csv"
df = pd.read_csv(data_path, delimiter=';').astype(str)
print(df.head())

ms = MarginalSynthesizer(epsilon=0.01)
ms.fit(df)
df_synth_10k = ms.transform(df, n_records=10000)
print(df_synth_10k.head())

# get random id col
df_synth_10k['2_Patient_ID'] = np.arange(10000, 20000)
df_synth_10k = df_synth_10k.replace('nan', np.nan)

df_synth_10k.to_csv(r"c:/data/1_iknl/synthetic/jrc/synth_cancercases_jrc_10k.csv", sep=';', index=False)

