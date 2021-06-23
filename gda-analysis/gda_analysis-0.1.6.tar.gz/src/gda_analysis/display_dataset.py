import pandas as pd
from src.gda_analysis import validation_tests as vtests
import sys

PATH_OF_MERGED_DATA = '/Users/tovahallas/projects/gda_data/raw_data/merged_vcf_gs_r01.xlsx'
PATH_OF_VALIDATED = '/Users/tovahallas/projects/test2/validated_merge_r01.xlsx'

COLS_LIST = ['id', 'chrom', 'pos', 'ref', 'alt', 'gt', 'allele1 - top', 'allele2 - top', 'allele1 - forward',
             'allele2 - forward', 'allele1 - ab', 'allele2 - ab', 'allele1 - plus', 'allele2 - plus',
             'allele1 - design', 'allele2 - design', 'gc score', 'snp', 'igentify short name', 'plus/minus strand']


def display_analyzed_data(path_of_merged_data):
    merged_df = pd.read_excel(path_of_merged_data)
    indels_df, merged_df = vtests.preprocess_df(merged_df, COLS_LIST)
    merged_df = vtests.validate_wildtype(merged_df)
    merged_df = vtests.validate_homo_to_alt(merged_df)
    merged_df = vtests.validate_hetro(merged_df)
    merged_df = vtests.validate_multi(merged_df)
    merged_df = vtests.validate_missing_info(merged_df)
    merged_df = vtests.validate_nocalls(merged_df)
    merged_df = vtests.validate_exceptions(merged_df)

    return merged_df


def output_toexcel(merged_df, path_of_validated):
    merged_df.to_excel(path_of_validated, encoding='utf-8')


def main_validation():
    merged_df = display_analyzed_data(sys.argv[1])
    output_toexcel(merged_df, sys.argv[2])


if __name__ == '__main__':
    main_validation(sys.argv)
