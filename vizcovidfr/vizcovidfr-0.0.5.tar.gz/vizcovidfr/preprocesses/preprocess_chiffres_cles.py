# ---------- requirements ----------
import pandas as pd
from vizcovidfr.loads import load_datasets
from datetime import date


# ---------- preprocess functions ----------

def drop_some_columns(df):
    '''
    Delete unused columns in the 'chiffres-cles' dataset.

    :param df: 'chiffres-cles' as Pandas dataframe.
        Should only be used with this dataset.
    :return: 'chiffres-cles' without some of its original columns
    :rtype: Pandas dataframe
    '''
    del df["cas_ehpad"]
    del df["cas_confirmes_ehpad"]
    del df["cas_possibles_ehpad"]
    del df["deces_ehpad"]
    del df["source_url"]
    del df["source_nom"]
    del df["source_archive"]
    del df["source_type"]
    del df["depistes"]
    return df


def reg_depts(df):
    '''
    Select only 'region' and 'department' rows in the 'chiffres-cles' dataset.

    :param df: 'chiffres-cles' as Pandas dataframe.
        Should only be used with this dataset.
    :return: 'chiffres-cles' with only 'region' and 'department' rows
    :rtype: Pandas dataframe
    '''
    df_local = df.loc[
        (df['granularite'] == 'departement') | (df['granularite'] == 'region')]
    return df_local


def reg_depts_code_format(df):
    '''
    Format strings in the 'maille_code' column in the 'chiffres-cles' dataset.
    Regions and departements are left with their official code number. In a
    new column called 'code'.
    For exemple, 'Herault' has now a '34' code instead of a 'DEP-34' code.

    :param df: 'chiffres-cles' as Pandas dataframe.
        Should only be used with this dataset.
    :return: 'chiffres-cles' with well formated 'region' and 'department' codes
    :rtype: Pandas dataframe
    '''
    for i in range(len(df['maille_code'])):
        df['maille_code'].iloc[i] = df['maille_code'].iloc[i][4:]
    df['code'] = df['maille_code']
    del df['maille_code']
    return df


def keysubtablename(name):
    '''
    Extract the data frame that contains the information for
    a certain granularity or territory

    :param name: A territory or a granularity
    :return: 'chiffres-cles' for only a region or a specific granularity
    :rtype: Pandas dataframe
    '''
    df_covid = load_datasets.Load_chiffres_cles().save_as_df()
    if name in ["departements", "pays", "region"]:
        dfsub = df_covid.loc[df_covid['granularite'] == name]
    else:
        dfsub = df_covid.loc[df_covid['maille_nom'] == name]
    dfsub = dfsub[~dfsub.index.duplicated(keep='first')]  # have an
    # information once
    return dfsub


def gooddates(df_covid):
    '''
    Remove the fake first lines with wrong dates

    :param df_covid: 'chiffres-cles' as Pandas dataframe.
        Should only be used with this dataset.
    :return: 'chiffres-cles' for only a region or a specific granularity
    :rtype: Pandas dataframe
    '''
    dat = df_covid['date']
    a = list((dat[:]))
    b = list(map(lambda x: x[:4] + "-" + x[5:7] + "-" + x[8:], a))
    b = pd.DatetimeIndex(b)  # put a correct way to view date
    df_covid.loc[:, 'date'] = b
    df_covid = df_covid.set_index('date')
    return df_covid["2020-01-18":]

# to be used as follow:
# A = drop_some_columns(df_covid)
# B = reg_depts(A)
# C = reg_depts_code_format(B)
# print(C.head())
