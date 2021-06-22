from src.gda_analysis import create_dfs as cdf
import pandas as pd
from sqlalchemy import create_engine


GS_CSV_FILE_PATH = '/Users/tovahallas/projects/GDA_project/genome_studio_file/csv_files_test/r02_gs_table.csv'
GS_SAMPLE_NAME_IN_SQL = "r02_gs_table"

VCF_CSV_FILE_PATH = '/Users/tovahallas/projects/GDA_project/vcf_files/csv_files_test/205364000001_R02C01.csv'
VCF_SAMPLE_NAME_IN_SQL = 'r02c01_205364000001'
VCF_FILE_PATH = '/Users/tovahallas/projects/GDA_project/vcf_files/205364000001_R03C01.vcf'


def save_as_csv(data: pd.DataFrame, path: str):
    data.to_csv(path)


def import_table_to_postgres(data, sample_name_in_sql):
    data.columns = [c.lower() for c in data.columns] #postgres doesn't like capitals or spaces
    engine = create_engine('postgresql://postgres:postgres@localhost:54320/test')

    data.to_sql(sample_name_in_sql, engine)


if __name__ == '__main__':
    vcf_data = cdf.create_vcf_df(VCF_FILE_PATH)
    # gs_data = cdf.create_gs_df()
    import_table_to_postgres(vcf_data, VCF_SAMPLE_NAME_IN_SQL)
    # import_table_to_postgres(gs_data, GS_SAMPLE_NAME_IN_SQL)
    # save_as_csv(vcf_data, VCF_CSV_FILE_PATH)
    # save_as_csv(gs_data, GS_CSV_FILE_PATH)
