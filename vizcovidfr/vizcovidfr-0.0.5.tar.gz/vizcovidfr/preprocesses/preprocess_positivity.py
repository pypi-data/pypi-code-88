import pandas as pd

# match between number and territory
DEPARTMENTS = {
    '01': 'Ain',
    '02': 'Aisne',
    '03': 'Allier',
    '04': 'Alpes-de-Haute-Provence',
    '05': 'Hautes-Alpes',
    '06': 'Alpes-Maritimes',
    '07': 'Ardèche',
    '08': 'Ardennes',
    '09': 'Ariège',
    '10': 'Aube',
    '11': 'Aude',
    '12': 'Aveyron',
    '13': 'Bouches-du-Rhône',
    '14': 'Calvados',
    '15': 'Cantal',
    '16': 'Charente',
    '17': 'Charente-Maritime',
    '18': 'Cher',
    '19': 'Corrèze',
    '2A': 'Corse-du-Sud',
    '2B': 'Haute-Corse',
    '21': 'Côte-d\'Or',
    '22': 'Côtes-d\'Armor',
    '23': 'Creuse',
    '24': 'Dordogne',
    '25': 'Doubs',
    '26': 'Drôme',
    '27': 'Eure',
    '28': 'Eure-et-Loir',
    '29': 'Finistère',
    '30': 'Gard',
    '31': 'Haute-Garonne',
    '32': 'Gers',
    '33': 'Gironde',
    '34': 'Hérault',
    '35': 'Ille-et-Vilaine',
    '36': 'Indre',
    '37': 'Indre-et-Loire',
    '38': 'Isère',
    '39': 'Jura',
    '40': 'Landes',
    '41': 'Loir-et-Cher',
    '42': 'Loire',
    '43': 'Haute-Loire',
    '44': 'Loire-Atlantique',
    '45': 'Loiret',
    '46': 'Lot',
    '47': 'Lot-et-Garonne',
    '48': 'Lozère',
    '49': 'Maine-et-Loire',
    '50': 'Manche',
    '51': 'Marne',
    '52': 'Haute-Marne',
    '53': 'Mayenne',
    '54': 'Meurthe-et-Moselle',
    '55': 'Meuse',
    '56': 'Morbihan',
    '57': 'Moselle',
    '58': 'Nièvre',
    '59': 'Nord',
    '60': 'Oise',
    '61': 'Orne',
    '62': 'Pas-de-Calais',
    '63': 'Puy-de-Dôme',
    '64': 'Pyrénées-Atlantiques',
    '65': 'Hautes-Pyrénées',
    '66': 'Pyrénées-Orientales',
    '67': 'Bas-Rhin',
    '68': 'Haut-Rhin',
    '69': 'Rhône',
    '70': 'Haute-Saône',
    '71': 'Saône-et-Loire',
    '72': 'Sarthe',
    '73': 'Savoie',
    '74': 'Haute-Savoie',
    '75': 'Paris',
    '76': 'Seine-Maritime',
    '77': 'Seine-et-Marne',
    '78': 'Yvelines',
    '79': 'Deux-Sèvres',
    '80': 'Somme',
    '81': 'Tarn',
    '82': 'Tarn-et-Garonne',
    '83': 'Var',
    '84': 'Vaucluse',
    '85': 'Vendée',
    '86': 'Vienne',
    '87': 'Haute-Vienne',
    '88': 'Vosges',
    '89': 'Yonne',
    '90': 'Territoire de Belfort',
    '91': 'Essonne',
    '92': 'Hauts-de-Seine',
    '93': 'Seine-Saint-Denis',
    '94': 'Val-de-Marne',
    '95': 'Val-d\'Oise',
    '971': 'Guadeloupe',
    '972': 'Martinique',
    '973': 'Guyane',
    '974': 'La Réunion',
    '976': 'Mayotte',
}

REGIONS = {
    'Auvergne-Rhône-Alpes': 84,
    'Bourgogne-Franche-Comté': 27,
    'Bretagne': 53,
    'Centre-Val de Loire': 24,
    'Corse': 94,
    'Grand Est': 44,
    'Guadeloupe': 1,
    'Guyane': 3,
    'Hauts-de-France': 32,
    'Île-de-France': 11,
    'La Réunion': 4,
    'Martinique': 2,
    'Normandie': 28,
    'Nouvelle-Aquitaine': 75,
    'Occitanie': 76,
    'Pays de la Loire': 52,
    'Provence-Alpes-Côte d\'Azur': 93, }

DEPARTMENTS = dict(zip(DEPARTMENTS.values(), DEPARTMENTS.keys()))
REGIONS = dict(REGIONS)


def ignoreage(df, weekday="jour"):
    """
    Extract the dataframe and ignore the age component by selecting
    the 0 age class.

    Parameters
    ----------
    :param df: A dataframe containing covid information by age
        Pandas dataframe
    :param weekday: whether it's a day "jour" or a "week"
    :type weekday: str, optional, default="jour"

    Returns
    -------
    :return: A dataframe of incidence ignoring age
    :rtype: 'pandas.dataframe'

    """
    df.index = df[weekday]
    del df[weekday]
    return df.loc[df['cl_age90'] == 0]


def granupositivity(df, nom, granularite=None):

    """

    Extract the dataframe for a specific region or department

    Parameters
    ----------
    :param df: A dataframe containing covid information by age
        Pandas dataframe
    :param nom: str or int for a specific region if it's a
        int granularity must be region
        if it's a string containing a int it must be departments
    :param granularite: a string to tell whether it's "reg" or "dep"
        if the name is not specific
    Returns
    -------
    :return: A dataframe of incidence for a region
    :rtype: 'pandas.dataframe'
    """
    if granularite is not None:
        return df.loc[df[granularite] == nom, :]
    if nom in REGIONS.keys():
        number = REGIONS[nom]
        df = df.loc[df["reg"] == number, :]
        return df
    if nom in DEPARTMENTS.keys():
        number = DEPARTMENTS[nom]
        df = df.loc[df["dep"] == number, :]
        return df
