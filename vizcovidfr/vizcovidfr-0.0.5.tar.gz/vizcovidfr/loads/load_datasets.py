# ---------- requirements ----------
from download import download
import pandas as pd
import os


# Define global path target on which to join our files.
# Ends up in the data folder
path_target = os.path.join(
                os.path.dirname(
                    os.path.realpath(__file__)),
                "..", "data")

# ---------- chiffres-cles ----------
url_cc = "https://www.data.gouv.fr/fr/datasets/r/0b66ca39-1623-4d9c-83ad-5434b7f9e2a4"
path_target_cc = os.path.join(path_target, "chiffres-cles.csv")


class Load_chiffres_cles:
    """
    Download and save 'chiffres-cles.csv',
    a dataset containing general Covid-19 information
    """
    def __init__(self, url=url_cc, target_name=path_target_cc):
        download(url, target_name, replace=True)
        # above, set replace to True to always get the updated version

    @staticmethod
    def save_as_df():
        # convert last lines type to str to avoid DtypeWarning
        converters = {'source_nom': str, 'source_url': str,
                      'source_archive': str, 'source_type': str}
        df_covid = pd.read_csv(path_target_cc, converters=converters)
        return df_covid


# ---------- transfer ----------
url_tr = "https://www.data.gouv.fr/fr/datasets/r/70cf1fd0-60b3-4584-b261-63fb2281359e"
path_target_tr = os.path.join(path_target, "transfer.csv")


class Load_transfer:
    """
    Download and save 'transfer.csv',
    a dataset containing information about Covid-19 patient transfers
    """
    def __init__(self, url=url_tr, target_name=path_target_tr):
        download(url, target_name, replace=True)
        # above, set replace to True to always get the updated version

    @staticmethod
    def save_as_df():
        df_tr = pd.read_csv(path_target_tr)
        return df_tr


# ---------- stocks-es-national ----------
url_sen = "https://www.data.gouv.fr/fr/datasets/r/519e2699-27d2-47c0-840b-81dbb30d4318"
path_target_sen = os.path.join(path_target, "./stocks-es-national.csv")


class Load_Vaccine_storage:
    """
    Download and save 'stocks-es-national.csv',
    a dataset containing Covid-19 vaccination informations
    """
    def __init__(self, url=url_sen, target_name=path_target_sen):
        download(url, target_name, replace=True)

    @staticmethod
    def save_as_df():
        df = pd.read_csv(path_target_sen)
        return df


# ---------- covid-19-france-vaccinations-age-dep ----------
url_vac = 'https://public.opendatasoft.com/explore/dataset/covid-19-france-vaccinations-age-sexe-dep/download/?format=csv&disjunctive.variable_label=true&refine.variable=Par+tranche+d%E2%80%99%C3%A2ge&refine.date=2021&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B'
path_target_vac = os.path.join(
                    path_target, "./covid-19-france-vaccinations-age-dep.csv")


class Load_vaccination:
    """
    Download and save 'covid-19-france-vaccinations-age-dep.csv',
    a dataset containing Covid-19 vaccination information
    """
    def __init__(self, url=url_vac, target_name=path_target_vac):
        download(url, target_name, replace=True)

    @staticmethod
    def save_as_df():
        df = pd.read_csv(path_target_vac, sep=";")
        return df


# ---------- chiffres-fr ----------
url_cfr = "https://www.data.gouv.fr/fr/datasets/r/d3a98a30-893f-47f7-96c5-2f4bcaaa0d71"
path_target_cfr = os.path.join(path_target, "./chiffres-fr.csv")


class Load_chiffres_fr:
    """
    Download and save 'chiffres-fr.csv',
    a dataset containing global information for France as a whole
    """
    def __init__(self, url=url_cfr, target_name=path_target_cfr):
        download(url, target_name, replace=True)

    @staticmethod
    def save_as_df():
        df_covid = pd.read_csv(path_target_cfr)
        return df_covid


# ---------- posquotreg ----------
url_posreg = "https://www.data.gouv.fr/fr/datasets/r/001aca18-df6a-45c8-89e6-f82d689e6c01"
path_target_posreg = os.path.join(path_target, "./posquotreg.csv")


class Load_posquotreg:
    """
    Download and save 'posquotreg.csv',
    a dataset containing positivity information by region.
    """
    def __init__(self, url=url_posreg, target_name=path_target_posreg):
        download(url, target_name, replace=True)

    @staticmethod
    def save_as_df():
        df = pd.read_csv(path_target_posreg, sep=";")
        return df


# ---------- posquotdep ----------
url_posdep = "https://www.data.gouv.fr/fr/datasets/r/406c6a23-e283-4300-9484-54e78c8ae675"
path_target_posdep = os.path.join(path_target, "./posquotdep.csv")


class Load_posquotdep:
    """
    Download and save 'posquotdep.csv',
    a dataset containing positivity information by departments
    """
    def __init__(self, url=url_posdep, target_name=path_target_posdep):
        download(url, target_name, replace=True)

    @staticmethod
    def save_as_df():
        df = pd.read_csv(path_target_posdep, sep=";")
        return df


# ---------- posquotfr ----------
url_posfr = "https://www.data.gouv.fr/fr/datasets/r/dd0de5d9-b5a5-4503-930a-7b08dc0adc7c"
path_target_posfr = os.path.join(path_target, "./posquotfr.csv")


class Load_posquotfr:
    """
    Download and save 'posquotfr.csv',
    a dataset containing positivity information for France
    """
    def __init__(self, url=url_posfr, target_name=path_target_posfr):
        download(url, target_name, replace=True)

    @staticmethod
    def save_as_df():
        df = pd.read_csv(path_target_posfr, sep=";")
        return df


# ---------- poshebreg ----------
url_poshebreg = "https://www.data.gouv.fr/fr/datasets/r/1ff7af5f-88d6-44bd-b8b6-16308b046afc"
path_target_poshebreg = os.path.join(path_target, "./poshebreg.csv")


class Load_poshebreg:
    """
    Download and save 'poshebreg.csv',
    a dataset containing positivity informations by regions weekly
    """
    def __init__(self, url=url_poshebreg, target_name=path_target_poshebreg):
        download(url, target_name, replace=True)

    @staticmethod
    def save_as_df():
        df = pd.read_csv(path_target_poshebreg, sep=";")
        return df


# ---------- poshebfr ----------
url_poshebfr = "https://www.data.gouv.fr/fr/datasets/r/2f0f720d-fbd2-41a7-95b4-3a70ff5a9253"
path_target_poshebfr = os.path.join(path_target, "./poshebfr.csv")


class Load_poshebfr:
    """
    Download and save 'poshebfr.csv',
    a dataset containing positivity informations in France weekly
    """
    def __init__(self, url=url_poshebfr, target_name=path_target_poshebfr):
        download(url, target_name, replace=True)

    @staticmethod
    def save_as_df():
        df = pd.read_csv(path_target_poshebfr, sep=";")
        return df


# ---------- incquotreg ----------
url_increg = "https://www.data.gouv.fr/fr/datasets/r/ad09241e-52fa-4be8-8298-e5760b43cae2"
path_target_increg = os.path.join(path_target, "./incquotreg.csv")


class Load_incquotreg:
    """
    Download and save 'incquotreg.csv',
    a dataset containing incidence information by regions
    """
    def __init__(self, url=url_increg, target_name=path_target_increg):
        download(url, target_name, replace=True)

    @staticmethod
    def save_as_df():
        df = pd.read_csv(path_target_increg, sep=";")
        return df


# ---------- incfr ----------
url_incfr = "https://www.data.gouv.fr/fr/datasets/r/57d44bd6-c9fd-424f-9a72-7834454f9e3c"
path_target_incfr = os.path.join(path_target, "./incquotfr.csv")


class Load_incquotfr:
    """
    Download and save 'incquotfr.csv',
    a dataset containing incidence information for France
    """
    def __init__(self, url=url_incfr, target_name=path_target_incfr):
        download(url, target_name, replace=True)

    @staticmethod
    def save_as_df():
        df = pd.read_csv(path_target_incfr, sep=";")
        return df


# ---------- inchebreg ----------
url_incregheb = "https://www.data.gouv.fr/fr/datasets/r/66b09e9a-41b5-4ed6-b03c-9aef93a4b559"
path_target_incregheb = os.path.join(path_target, "./inchebreg.csv")


class Load_inchebreg:
    """
    Download and save 'inchebreg.csv',
    a dataset containing incidence information by regions weekly
    """
    def __init__(self, url=url_incregheb, target_name=path_target_incregheb):
        download(url, target_name, replace=True)

    @staticmethod
    def save_as_df():
        df = pd.read_csv(path_target_incregheb, sep=";")
        return df


# ---------- inchebfr ----------
url_incfrheb = "https://www.data.gouv.fr/fr/datasets/r/2360f82e-4fa4-475a-bc07-9caa206d9e32"
path_target_incfrheb = os.path.join(path_target, "./inchebfr.csv")


class Load_inchebfr:
    """
    Download and save 'inchebfr.csv',
    a dataset containing incidence information for France weekly
    """
    def __init__(self, url=url_incfrheb, target_name=path_target_incfrheb):
        download(url, target_name, replace=True)

    @staticmethod
    def save_as_df():
        df = pd.read_csv(path_target_incfrheb, sep=";")
        return df


# ---------- classe_age ----------
url_classe_age = "https://www.data.gouv.fr/fr/datasets/r/08c18e08-6780-452d-9b8c-ae244ad529b3"
path_target6 = os.path.join(
                os.path.dirname(
                    os.path.realpath(__file__)),
                "..", "data", "./classe_age.csv")


class Load_classe_age:
    def __init__(self, url=url_classe_age, target_name=path_target6):
        download(url, target_name, replace=True)

    @staticmethod
    def save_as_df():
        df = pd.read_csv(path_target6, sep=";")
        return df
