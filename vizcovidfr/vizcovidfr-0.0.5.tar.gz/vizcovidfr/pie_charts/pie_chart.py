# ---------- requirements ----------
import plotly.express as px
import time

# local reqs
from vizcovidfr.loads import load_datasets
from vizcovidfr.preprocesses import preprocess_chiffres_cles


def piechart(criterion='reanimation', date='2021-04-20',
             template='plotly_dark', num_dose='1'):
    '''
    Make a pie chart of France covid-19 data, per region.

    Parameters
    ----------
    :param criterion: the criterion we want information about.
        Either 'deces', 'hospitalises', 'reanimation' or 'vaccination':

            - 'deces':
                give the cumulated number of deaths
                and the death rate, per region,
                from the beginning of covid-19
                to the chosen date, due to covid-19.
            - 'hospitalises':
                give the number of persons in hospitalization
                and the hospitalization rate, per region,
                on the chosen date, due to covid-19.
            - 'reanimation':
                give the number of persons in intensive care
                and the intensive care rate, per region,
                on the chosen date, due to covid-19.
            - 'vaccination':
                give the cumulated number of first or second
                vaccination doses according to the chosen
                num_dose argument and its vaccination rate,
                per region.
                The rate per region represents the number of
                doses (first or second) out of the total number
                of French people vaccinated (first or second).

    :type criterion: str, optional, default='reanimation'
    :param date: only needed if criterion argument is 'hospitalises'
        or 'reanimation'.
        Set the date which we want to have information on.
        The date format must be the following one: 'YY-mm-dd'.
        The chosen date must be between '2020-04-04' and
        today's date.
    :type date: str, optional, default='2021-04-20'
    :param template: the visual style we want the graph to be
        based on.
        For reference, see https://plotly.com/python/templates/.
    :type template: str, optional, default='plotly_dark'
    :param num_dose: only if criterion argument is 'vaccination'.
        The dose number of the vaccine.
        Should be either '1' or '2':

            - '1':
                display only the number of first doses
            - '2':
                display only the number of second doses.

    :type num_dose: str, optional, default='1'

    Returns
    -------
    :return: An interactive pie chart
    :rtype: plotly.graph_objects.Figure

    :Examples:

    **Pie chart of first dose vaccination rate until today per region**

    >>> piechart(criterion='vaccination', num_dose='1')

    **Pie chart of hospitalization rate per region on the 2021-04-20**

    >>> piechart(criterion='hospitalises', date='2021-04-20')


    :Notes:

    **Manipulation tips:**

    - click on a region icon on the right to remove it from the pie chart till further notice: the rate per region
    will get adjusted.

    - Double click on a region icon to remove all the others from the pie chart.

    - click on the camera icon on the very top right of the chart to save the image as a png.

    - pass mouse on the pie chart slices to get thorough information.
    '''
    start = time.time()
    df_covid = load_datasets.Load_chiffres_cles().save_as_df()
    # preprocess
    df_covid = preprocess_chiffres_cles.drop_some_columns(df_covid)
    df_covid = preprocess_chiffres_cles.reg_depts(df_covid)
    df_region = df_covid.loc[df_covid['granularite'] == 'region']
    # columns renamed for visualization
    df_region.rename(
            columns={'deces': 'Number of deaths',
                     'maille_nom': 'Region name',
                     'reanimation': 'Number of people in intensive care',
                     'hospitalises': 'Number of people in hospitalization'},
            inplace=True)
    if (criterion == 'deces'):
        df = df_region.groupby(
                ['Region name'])['Number of deaths'].agg('max').reset_index()
        a = 'Death'
        fig = px.pie(df, values='Number of deaths', names='Region name',
                     color_discrete_sequence=px.colors.sequential.thermal,
                     title=f'{a} rate per region until today', template=template)
        # cool color palettes: solar, plasma, Turbo, Inferno, thermal
    elif (criterion == 'reanimation'):
        # before 2020-04-04, incorrect or missing reanimation data
        df_region = df_region[df_region['date'] >= '2020-04-04']
        df = df_region.loc[df_region['date'] == date]
        a = 'Intensive care'
        fig = px.pie(df, values='Number of people in intensive care',
                     names='Region name',
                     color_discrete_sequence=px.colors.sequential.thermal,
                     title=f'{a} rate per region on the {date}',
                     template=template)
    elif (criterion == 'hospitalises'):
        # before 2020-04-04, incorrect or missing hospitalisation data
        df_region = df_region[df_region['date'] >= '2020-04-04']
        df = df_region.loc[df_region['date'] == date]
        a = 'Hospitalisation'
        fig = px.pie(df, values='Number of people in hospitalization',
                     names='Region name',
                     color_discrete_sequence=px.colors.sequential.thermal,
                     title=f'{a} rate per region on the {date}',
                     template=template)
    elif (criterion == 'vaccination'):
        df_Vac = load_datasets.Load_vaccination().save_as_df()
        df_Vac = df_Vac.groupby(['Valeur de la variable'])
        all_ages = df_Vac.get_group(0).reset_index(drop=True)
        # sum per date and region
        df_reg2 = all_ages.groupby(
                    ['Date',
                     'Nom Officiel Région'])['Nombre cumulé de doses n°1',
                                             'Nombre cumulé de vaccinations complètes (doses n°2)'].agg('sum').reset_index()
        df = df_reg2.groupby(['Nom Officiel Région']).agg('max').reset_index()
        # Saint-Barthélemy and Saint-Martin are departments and not regions
        df.drop([17, 18], 0, inplace=True)
        df.reset_index(drop=True)
        if (num_dose == '1'):
            a = 'First dose vaccination'
            fig = px.pie(
                    df, values='Nombre cumulé de doses n°1',
                    names='Nom Officiel Région',
                    color_discrete_sequence=px.colors.sequential.thermal,
                    labels={'Nom Officiel Région': 'Region name',
                            'Nombre cumulé de doses n°1': 'First vaccine doses administered till today',
                            'Nombre cumulé de vaccinations complètes (doses n°2)': 'Second vaccine doses administered till today'},
                    title=f'{a} rate per region until today',
                    template=template)
        else:
            a = 'Second dose vaccination'
            fig = px.pie(
                    df, values='Nombre cumulé de vaccinations complètes (doses n°2)',
                    names='Nom Officiel Région',
                    color_discrete_sequence=px.colors.sequential.thermal,
                    labels={'Nom Officiel Région': 'Region name',
                            'Nombre cumulé de doses n°1': 'First vaccine doses administered till today',
                            'Nombre cumulé de vaccinations complètes (doses n°2)': 'Second vaccine doses administered till today'},
                    title=f'{a} rate per region until today',
                    template=template)
    fig.update_traces(textposition='inside',
                      textinfo='percent+label',
                      rotation=180)
    end = time.time()
    print("Time to execute: {0:.5f} s.".format(end - start))
    fig.show()
