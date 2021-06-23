from src.gda_analysis.convert_vcf_to_df import convert_vcf_to_df as vcf2df
import pandas as pd
from src.gda_analysis.convert_gs_to_df import convert_gs_to_df as gs2df
import sys


GS_FILE_PATH = '/Users/tovahallas/projects/GDA_project/genome_studio_file/GDACS_dudi_FinalReport_tova.txt'
GS_SAMPLE_ID = 'GRC005690'

VCF_FILE_PATH = '/Users/tovahallas/projects/GDA_project/vcf_files/205364000001_R01C01.vcf'
VCF_SAMPLE_ID = '205364000001_R01C01'

MERGED_DATA_PATH = '/Users/tovahallas/projects/tests/merged_vcf_gs_r01.xlsx'

NAME_LIST_INFO = ['GC', 'ALLELE_A', 'ALLELE_B', 'FRAC_A', 'FRAC_C', 'FRAC_G', 'FRAC_T', 'NORM_ID', 'ASSAY_TYPE',
                 'GenTrain_Score', 'Orig_Score', 'Cluster_Sep', 'N_AA', 'N_AB', 'N_BB', 'devR_AA', 'devR_AB', 'devR_BB',
                 'devTHETA_AA','devTHETA_AB', 'devTHETA_BB', 'meanR_AA', 'meanR_AB', 'meanR_BB', 'meanTHETA_AA',
                 'meanTHETA_AB', 'meanTHETA_BB', 'Intensity_Threshold']
NAME_LIST_FORMAT = ['GT', 'GQ', 'IGC', 'BAF', 'LRR', 'NORMX', 'NORMY', 'R', 'THETA', 'X', 'Y']


def create_gs_df(path: str, gs_sample_id: str) -> pd.DataFrame:
    data = gs2df.read_gs_file(path)
    sample_data = gs2df.extract_results_from_id(data, gs_sample_id)

    return sample_data


def create_vcf_df(path: str, vcf_sample_id: str) -> pd.DataFrame:
    data = vcf2df.read_vcf(path)
    data = vcf2df.split_info_col(data, 'INFO', NAME_LIST_INFO, ';')
    data = vcf2df.assign_split_col(data, vcf_sample_id, NAME_LIST_FORMAT, ':')

    return data


def join_vcf_and_gs(vcf_data, gs_data):
    gs_data.rename(columns={'SNP Name': 'ID'}, inplace=True)
    merged_df = gs_data.merge(vcf_data, how='left', on='ID')

    return merged_df


def main_merge():
    #print("/nplease enter genome studio file path and gs sample id: ")
    gs_data = create_gs_df(sys.argv[1], sys.argv[2])
    print(gs_data)
    # print("please enter vcf file path and vcf sample id: ")
    vcf_data = create_vcf_df(sys.argv[3], sys.argv[4])
    # print("/nplease enter path of merged data excel output: ")
    merged_data = join_vcf_and_gs(vcf_data, gs_data)
    merged_data.to_excel(sys.argv[5], encoding='utf-8')


if __name__ == '__main__':
    main_merge(sys.argv)

