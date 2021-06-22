import pandas as pd
import io
from sqlalchemy import create_engine
from typing import List, Dict


def read_vcf(path: str) -> pd.DataFrame:
    """
    read vcf (tab separated) file
    :param path: str: path of vcf file
    :return: df: pd.DataFrame of vcf file content
    """
    with open(path, 'r') as f:
        lines = [l for l in f if not l.startswith('##')]

    df = pd.read_csv(io.StringIO(''.join(lines)), dtype={'#CHROM': str, 'POS': int, 'ID': str, 'REF': str, 'ALT': str,
                                                         'QUAL': str, 'FILTER': str, 'INFO': str}, sep='\t').rename(
        columns={'#CHROM': 'CHROM'})

    return df


def assign_split_col(df: pd.DataFrame, col: str, name_list, delimiter: str) -> pd.DataFrame:
    """
    read vcf (tab separated) file
    :param: df src vcf dataframe
    :param: col name of column we need to split
    :param: name_list list of names of columns we split to
    :param: character we split by
    :return: df: pd.DataFrame of splitted vcf file
    """
    df = df.copy()
    split_col = df[col].str.split(delimiter, expand=True)
    df = df.assign(**dict(zip(name_list, [split_col.iloc[:, x] for x in range(split_col.shape[1])])))

    return df


def extract_numbers(df: pd.DataFrame, col):
    """
    extract numbers from
    :param: df src vcf dataframe
    :param: col name of column we need to split
    :param: name_list list of names of columns we split to
    :param: character we split by
    :return: df: pd.DataFrame of splitted vcf file
    """
    df[col] = df[col].str[(len(col)+1):]

    return df


def split_info_col(data, col_name, name_list, sep):
    df = assign_split_col(data, col_name, name_list, sep)
    for col in name_list:
        df = extract_numbers(df, col)

    return df



