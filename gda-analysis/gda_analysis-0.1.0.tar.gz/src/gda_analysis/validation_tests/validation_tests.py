from src.gda_analysis import create_dfs as vdf
from typing import List
import pandas as pd
import numpy as np


def extract_indels(merged_df):
    indels_df = merged_df[(merged_df['ref'] == 'I') | (merged_df['ref'] == 'D')
                          | (merged_df['alt'] == 'I') | (merged_df['alt'] == 'D')]

    return indels_df


def preprocess_df(merged_df: pd.DataFrame, cols_list: List[str]) -> pd.DataFrame:
    merged_df.columns = [x.lower() for x in merged_df.columns]
    merged_df = merged_df[cols_list]
    indels_df = extract_indels(merged_df)
    merged_df = merged_df[(merged_df['ref'] != 'I') & (merged_df['ref'] != 'D')
                          & (merged_df['alt'] != 'I') & (merged_df['alt'] != 'D')]
    merged_df[['alt1', 'alt2']] = merged_df['alt'].str.split(',', expand=True)
    merged_df['alt2'] = merged_df['alt2'].fillna(value="")
    merged_df['valid'] = ""

    return indels_df, merged_df


def validate_wildtype(merged_df):
    merged_df['valid'] = np.where((merged_df['gt'] == '0/0') & (merged_df['ref'] == merged_df['allele1 - plus']) &
                                  (merged_df['allele1 - plus'] == merged_df['allele2 - plus']) &
                                  (merged_df['alt2'] == ""), "matched", merged_df['valid'])

    return merged_df


def validate_homo_to_alt(merged_df):
    merged_df['valid'] = np.where((merged_df['gt'] == '1/1') & (merged_df['alt'] == merged_df['allele1 - plus']) &
                                  (merged_df['allele1 - plus'] == merged_df['allele2 - plus']) &
                                  (merged_df['alt2'] == ""), "matched", merged_df['valid'])
    merged_df['valid'] = np.where((merged_df['gt'] == '1/1') & (merged_df['alt1'] == merged_df['allele1 - plus']) &
                                  (merged_df['allele1 - plus'] == merged_df['allele2 - plus']), "matched",
                                  merged_df['valid'])

    return merged_df


def validate_hetro(merged_df):
    merged_df['valid'] = np.where((merged_df['gt'] == '0/1') & ((merged_df['alt1'] == merged_df['allele1 - plus']) |
                                  (merged_df['alt2'] == merged_df['allele1 - plus']) |
                                  (merged_df['alt1'] == merged_df['allele2 - plus']) |
                                  (merged_df['alt2'] == merged_df['allele2 - plus'])) &
                                  ((merged_df['ref'] == merged_df['allele1 - plus']) |
                                   (merged_df['ref'] == merged_df['allele2 - plus'])), "matched",
                                  merged_df['valid'])

    return merged_df


def validate_multi(merged_df):
    merged_df['valid'] = np.where((merged_df['gt'] == '2/2') & (merged_df['alt2'] == merged_df['allele1 - plus']) &
                                  (merged_df['allele1 - plus'] == merged_df['allele2 - plus']), "matched",
                                  merged_df['valid'])
    merged_df['valid'] = np.where((merged_df['gt'] == '1/2') & ((merged_df['alt1'] == merged_df['allele1 - plus']) |
                                                                (merged_df['alt1'] == merged_df['allele2 - plus'])) &
                                  (merged_df['allele1 - plus'] != merged_df['allele2 - plus']) &
                                  ((merged_df['alt2'] == merged_df['allele1 - plus']) |
                                   (merged_df['alt2'] == merged_df['allele2 - plus'])), "matched", merged_df['valid'])

    return merged_df


def validate_missing_info(merged_df):
    merged_df['valid'] = np.where((merged_df['allele1 - plus'] == '-'), "missing strand direction",
                                  merged_df['valid'])

    merged_df['valid'] = np.where(merged_df['chrom'].isnull(), "missing vcf result", merged_df['valid'])

    return merged_df


def validate_nocalls(merged_df):
    merged_df['valid'] = np.where((merged_df['gt'] == './.') & ((merged_df['alt1'] == merged_df['allele1 - plus']) |
                                  (merged_df['alt2'] == merged_df['allele1 - plus']) |
                                  (merged_df['alt1'] == merged_df['allele2 - plus']) |
                                  (merged_df['alt2'] == merged_df['allele2 - plus'])) &
                                  ((merged_df['ref'] == merged_df['allele1 - plus']) |
                                   (merged_df['ref'] == merged_df['allele2 - plus'])), "NOCALL- might be 0/1",
                                  merged_df['valid'])

    merged_df['valid'] = np.where((merged_df['gt'] == './.') & (merged_df['ref'] == merged_df['allele1 - plus']) &
                                  (merged_df['allele1 - plus'] == merged_df['allele2 - plus']) &
                                  (merged_df['alt2'] == ""), "NOCALL- might be 0/0", merged_df['valid'])

    merged_df['valid'] = np.where((merged_df['gt'] == './.') & (merged_df['alt'] == merged_df['allele1 - plus']) &
                                  (merged_df['allele1 - plus'] == merged_df['allele2 - plus']) &
                                  (merged_df['alt2'] == ""), "NOCALL- might be 1/1", merged_df['valid'])

    merged_df['valid'] = np.where((merged_df['gt'] == './.') & ((merged_df['alt1'] == merged_df['allele1 - plus']) |
                                                                (merged_df['alt2'] == merged_df['allele1 - plus'])) &
                                  (merged_df['alt2'] != "") & (merged_df['allele1 - plus'] ==
                                                               merged_df['allele2 - plus']), "NOCALL- might be 2/2",
                                  merged_df['valid'])

    return merged_df


def validate_exceptions(merged_df):
    merged_df['valid'] = np.where(merged_df['valid'] == "", "unmatched", merged_df['valid'])

    return merged_df













