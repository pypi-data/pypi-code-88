import pandas as pd
import io


def read_gs_file(path: str) -> pd.DataFrame:
    with open(path, 'r') as f:
        lines = [l for l in f if f if not l.startswith('##')]
    df = pd.read_csv(
        io.StringIO(''.join(lines)),
        dtype={'SNP Name': str, 'Sample ID': str, 'Allele1 - Top': str, 'Allele2 - Top': str, 'GC Score': float,
               'Allele1 - Forward': str, 'Allele2 - Forward': str,	'Allele1 - Design':str, 'Allele2 - Design':str,
               'Allele1 - AB': str,	'Allele2 - AB': str, 'Allele1 - Plus': str, 'Allele2 - Plus': str,	'SNP': str,
               'Igentify Short Name': str,	'Plus/Minus Strand': str},
        sep='\t'
    )
    return df


def extract_results_from_id(df: pd.DataFrame, id: str) -> pd.DataFrame:
    df = df[(df['Sample ID'] == id) & (df['GC Score'] > 0)]

    return df


