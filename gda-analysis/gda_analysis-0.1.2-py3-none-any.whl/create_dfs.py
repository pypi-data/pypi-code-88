from src.gda_analysis import convert_vcf_to_df as vcf2df
import pandas as pd
from src.gda_analysis import convert_gs_to_df as gs2df


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


def create_gs_df(path: str) -> pd.DataFrame:
    data = gs2df.read_gs_file(path)
    sample_data = gs2df.extract_results_from_id(data, GS_SAMPLE_ID)

    return sample_data


def create_vcf_df(path: str) -> pd.DataFrame:
    data = vcf2df.read_vcf(path)
    data = vcf2df.split_info_col(data, 'INFO', NAME_LIST_INFO, ';')
    data = vcf2df.assign_split_col(data, VCF_SAMPLE_ID, NAME_LIST_FORMAT, ':')

    return data


def join_vcf_and_gs(vcf_data, gs_data):
    gs_data.rename(columns={'SNP Name': 'ID'}, inplace=True)
    merged_df = gs_data.merge(vcf_data, how='left', on='ID')

    return merged_df


if __name__ == '__main__':
    vcf_data = create_vcf_df(VCF_FILE_PATH)
    gs_data = create_gs_df(GS_FILE_PATH)
    merged_data = join_vcf_and_gs(vcf_data, gs_data)
    merged_data.to_excel(MERGED_DATA_PATH, encoding='utf-8')

