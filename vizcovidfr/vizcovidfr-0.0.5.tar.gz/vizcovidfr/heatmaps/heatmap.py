# ---------- requirements ----------
import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# local reqs
from vizcovidfr.loads import load_datasets
from vizcovidfr.preprocesses import preprocess_heatmaps
from vizcovidfr.preprocesses.preprocess_positivity import granupositivity
from vizcovidfr.preprocesses import preprocess_classe_age as pca


def heatmap_age(start, end=None, granularity='France', num_reg=1,
                frequency='daily'):
    """
    Make a heatmap by age class and the given frequency for incidence rate.

    Parameters
    ----------
    :param start:
        if frequency='daily':
            if end=None, must be a year and a month on the format 'YYYY-MM'
            else, must be a day on the format 'YYYY-MM-DD'
        if frequency='weekly':
            must be the week of a year on the format 'YYYY-SWW',
            and end is **not** optional and must be of the same format
    :type start: str
    :param end: date when the heatmap stops.
        Only if start is on format 'YYYY-MM-DD' or 'YYYY-SWW'.
        Must be on format 'YYYY-MM-DD' or 'YYYY-SWW', same than start.
        Must be a date later than start.
    :type end: NoneType or str, optional only if frequency='daily' and if
        start is of the format 'YYYY-MM'
    :param granularity: the granularity we want the heatmap to be based on.
        Should be either 'region' or 'France'.
    :type granularity: str, optional, default='France'
    :param num_reg: code of the region you want to display.
        Codes are the official INSAA code region and are given in the
        dictionary below.
    :type num_reg: int, optional (useful only if granularity='region'),
        default=Guadeloupe


    Region dictionary :

        1 : Guadeloupe

        2 : Martinique

        3 : Guyane

        4 : La Reunion

        6 : Mayotte

        11 : Île-de-France

        24 : Centre-Val de Loire

        27 : Bourgogne-Franche-Comte

        28 : Normandie

        32 : Hauts-de-France

        44 : Grand Est

        52 : Pays de la Loire

        53 : Bretagne

        75 : Nouvelle-Aquitaine

        76 : Occitanie

        84 : Auvergne-Rhône-Alpes

        93 : Provence-Alpes Côte d'Azur

        94 : Corse


    :param frequency: the time frequency to show on the heatmap
        should be 'weekly' or 'daily'
    :type frequency: str, optional, default='daily'

    Returns
    -------
    :return: A heatmap with two axis: one for age and one for day
    :rtype: seaborn heatmap

    :Example:

    **Heatmap for the month of March 2021 in France**

    >>> heatmap_age(start='2021-03')

    **Heatmap between 2021-03-12 and 2021-04-10 in France**

    >>> heatmap_age(start='2021-03-12', end='2021-04-10')

    **Heatmap between week 3 and week 10 of the year 2021 in France**

    >>> heatmap_age(start='2021-S03', end='2021-S10', frequency='weekly')

    **Heatmap for the month of March 2021 in Martinique**

    >>> heatmap_age(start='2021-03', granularity='region', num_reg=2)

    """
    starting = time.time()
    if ((granularity == 'France') & (frequency == 'weekly')):
        df = load_datasets.Load_poshebfr().save_as_df()
        freq = 'week'
    if ((granularity == 'France') & (frequency == 'daily')):
        df = load_datasets.Load_posquotfr().save_as_df()
        freq = 'jour'
    if ((granularity == 'region') & (frequency == 'daily')):
        df = granupositivity(load_datasets.Load_posquotreg().save_as_df(),
                             num_reg, "reg")
        freq = 'jour'
    if ((granularity == 'region') & (frequency == 'weekly')):
        df = granupositivity(load_datasets.Load_poshebreg().save_as_df(),
                             num_reg, "reg")
        freq = 'week'

    df["incid"] = df["P"]/df['pop']*100000
    if (freq == "jour"):
        df[freq] = pd.to_datetime(df[freq])
        df = df.set_index(freq)
        if end is None:
            df = df[start][['incid', 'cl_age90']].reset_index()
        else:
            df = df[start:end][['incid', 'cl_age90']].reset_index()
        df[freq] = pd.to_datetime(df['jour']).dt.date
    elif (freq == "week"):
        a = [preprocess_heatmaps.W2020_2021(i) for i in range(preprocess_heatmaps.S2020_2021(start), preprocess_heatmaps.S2020_2021(end)+1)]
        df = df[df[freq].isin(a)]

    df.drop(df.loc[df["cl_age90"] == 0].index, inplace=True)
    dico_reg = pca.dico_reg()
    end = time.time()
    print("Time to execute: {0:.5f} s.".format(end - starting))
    if (granularity == 'region'):
        sns.heatmap(df.pivot(freq, "cl_age90", "incid"))
        plt.figure(1, figsize=(14, 11))
        plt.title(f'Incidence rate in ' + dico_reg[num_reg] + f' on a {frequency} time basis')
        plt.xlabel('Age')
        plt.ylabel('Time')
        plt.show()
    else:
        sns.heatmap(df.pivot(freq, "cl_age90", "incid"))
        plt.figure(1, figsize=(14, 11))
        plt.title(f'Incidence rate in France on a {frequency} time basis')
        plt.xlabel('Age')
        plt.ylabel('Time')
        plt.show()


def heatmap_reg_age(date):
    """
    Make the heatmap for one given date between regions and age ranges
    for incidence rate.

    Parameters
    ----------
    :param date:
        a day on the format 'YYYY-MM-DD' or a week on the format 'YYYY-SWW'
    :type date: str

    Returns
    -------
    :return: A heatmap with two axis: one for age range and one for region
    :rtype: seaborn heatmap

    :Example:
    >>> heatmap_reg_age("2020-S35")

    """
    starting = time.time()
    if (len(date) > 8):
        df = load_datasets.Load_posquotreg().save_as_df()
    if (len(date) <= 8):
        df = load_datasets.Load_poshebreg().save_as_df()
    if len(date) > 8:
        df = df.loc[df["jour"] == date]
    else:
        df = df.loc[df["week"] == date]
    df["incid"] = df["P"]/df['pop']*100000
    df.drop(df.loc[df["cl_age90"] == 0].index, inplace=True)
    end = time.time()
    print("Time to execute: {0:.5f} s.".format(end - starting))
    plt.figure(1, figsize=(11, 8))
    sns.heatmap(df.pivot("reg", "cl_age90", "incid"))
    plt.title(f'Incidence rate per region and age range on {date}')
    plt.xlabel('Age')
    plt.ylabel('Region number')
    plt.show()


def heatmap_reg_day(age, start, end=None, frequency='daily'):
    """
    Make the heatmap for one given age range between regions and date interval
    for incidence rate.

    Parameters
    ----------
    :param start:
        if frequency='daily':
            if end=None, must be a year and a month on the format 'YYYY-MM'
            else, must be a day on the format 'YYYY-MM-DD'
        if frequency='weekly':
            must be the week of a year on the format 'YYYY-SWW',
            and end is **not** optional and must be of the same format
    :type start: str
    :param end: date when the heatmap stops.
        Only if start is on format 'YYYY-MM-DD' or 'YYYY-SWW'.
        Must be on format 'YYYY-MM-DD' or 'YYYY-SWW', same than start.
        Must be a date later than start.
    :type end: NoneType or str, optional only if frequency='daily' and if
        start is of the format 'YYYY-MM'

    :param age: integer in the following list:

        0: all ages

        9: from 0 to 9 years old

        19: from 10 to 19 years old

        29: from 20 to 29 years old

        39: from 30 to 39 years old

        49: from 40 to 49 years old

        59: from 50 to 59 years old

        69: from 60 to 69 years old

        79: from 70 to 79 years old

        89: 80 or older

    :type age: int

    :param frequency: the time frequency to show on the heatmap
        should be 'weekly' or 'daily'
    :type frequency: str, optional, default='daily'

    Returns
    -------

    :return: A heatmap with two axis: one for time and one for regions
    :rtype: seaborn heatmap

    :Examples:

    **Heatmap for incidence rate between march 2021 and today for 80 years old or older people**

    >>> heatmap_reg_day(89, start='2021-03')

    **Heatmap between week 36 and week 52 of the year 2020 for all ages**

    >>> heatmap_reg_day(0, '2020-S36', '2020-S52', 'weekly')

    """
    starting = time.time()
    if (frequency == "daily"):
        freq = "jour"
        df = load_datasets.Load_posquotreg().save_as_df()
    if (frequency == "weekly"):
        freq = "week"
        df = load_datasets.Load_poshebreg().save_as_df()
    df = df.loc[df["cl_age90"] == age]
    df['incid'] = df['P']/df['pop']*100000
    if frequency == "daily":
        df[freq] = pd.to_datetime(df[freq])
        df = df.set_index(freq)
        if end is None:
            df = df[start][['incid', 'reg', 'cl_age90']].reset_index()
        else:
            df = df[start:end][['incid', 'reg', 'cl_age90']].reset_index()
        df[freq] = pd.to_datetime(df['jour']).dt.date
    elif frequency == "weekly":
        a = [preprocess_heatmaps.W2020_2021(i) for i in range(preprocess_heatmaps.S2020_2021(start),
             preprocess_heatmaps.S2020_2021(end)+1)]
        df = df[df['week'].isin(a)]
    end = time.time()
    print("Time to execute: {0:.5f} s.".format(end - starting))
    plt.figure(1, figsize=(11, 8))
    sns.heatmap(df.pivot(freq, "reg", "incid"))
    plt.title(
        f'Incidence rate per region and per date for age range number {age}')
    plt.xlabel('Region number')
    plt.ylabel('Date')
    plt.show()
