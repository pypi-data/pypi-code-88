import pandas as pd

PATH_OF_MERGED = '/Users/tovahallas/projects/gda_data/result_files/validated_merge_r01.xlsx'


def extract_zeroes(manifest):
   zero_manifest = manifest[manifest['chr'] == 0]

   return zero_manifest


def validate_manifest(manifest):
   zeroes_df = extract_zeroes(manifest)
   without_strand_df = manifest[(manifest['refstrand'] != '-') & (manifest['refstrand'] != '+')]


def extract_nocalls_from_merged_data(validated_merge_r01):
   validated_merge_r01_nocalls = validated_merge_r01[validated_merge_r01['gt'] == './.']


def extract_missing_strands(validated_merge_r01):
   validated_merge_r01_without_strand = validated_merge_r01[validated_merge_r01['plus/minus strand'] == '?']


def cmp_missing_strands(validated_merge_r01_without_strand, manifest):
   merged = validated_merge_r01_without_strand.merge(manifest, how='left', on='id')

   return merged


def find_missing_vcf_ids_in_merged(validated_merge_r01, manifest):
   missing_vcf = validated_merge_r01[validated_merge_r01['chrom'].isnull()]
   merged_missing_vcf = missing_vcf.merge(manifest, how='left', on='id')

   return merged_missing_vcf


def find_mismatches_in_manifest(validated_merge_r01, validated_merge_r01_without_strand, manifest):
   merged_missing_strands = cmp_missing_strands(validated_merge_r01_without_strand, manifest)
   merged_missing_vcf = find_missing_vcf_ids_in_merged(validated_merge_r01, manifest)


def preprocess_manifest(manifest):
   manifest.columns = [col.lower() for col in manifest.columns]
   manifest.rename(columns={'name': 'id'}, inplace=True)


def preprocess_vcf(vcf):
   vcf.columns = [col.lower() for col in vcf.columns]
   vcf.rename(columns={'ID': 'id'}, inplace=True)



def read_data():
   manifest = pd.read_excel('/Users/tovahallas/projects/GDA_project/manifest/20050209_GDA_manifest.xlsx')
   vcf = pd.read_csv('/Users/tovahallas/projects/GDA_project/vcf_files/205364000001_R01C01.csv')
   validated_merge_r01 = pd.read_excel(PATH_OF_MERGED)


   # merged_vcf_gs = pd.read_excel('/Users/tovahallas/projects/gda_data/raw_data/merged_vcf_gs.xlsx')
   #
   # merged_on_vcf = validated_merge_r01_without_strand.merge(vcf, how='left', on='id')


if __name__ == '__main__':




