# ---------- requirements ----------
import time
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# local reqs
from vizcovidfr.loads import load_datasets
from vizcovidfr.loads.load_datasets import Load_posquotreg
from vizcovidfr.loads.load_datasets import Load_chiffres_fr
from vizcovidfr.preprocesses import preprocess_chiffres_cles
from vizcovidfr.preprocesses import preprocess_positivity
from vizcovidfr.preprocesses.preprocess_positivity import REGIONS, DEPARTMENTS

# add python option to avoid "false positive" warning:
pd.options.mode.chained_assignment = None  # default='warn'


def vactypedoses(vaccine_type='All vaccines', color_pal='darkblue',
                 color_pal2='orangered', color_pal3='green',
                 font_size=16, font_family="Franklin Gothic Medium",
                 font_color='white', bgcolor='darkslategrey',
                 template='plotly_dark'):
    '''
    Make an interactive line chart of France vaccine storage,
    according to the vaccine type.

    Parameters
    ----------
    :param vaccine_type: the vaccine type we want to display.
        Either 'Pfizer', 'Moderna', 'AstraZeneca' or 'All vaccines'.
        In this latter case, the three vaccine types are represented.
        It is possible to hover one's mouse over the curves to get thorough
        information.
    :type vaccine_type: str, optional, default='All vaccines'
    :param color_pal: the color of the chosen vaccine type curve.
        If 'All vaccines' vaccine_type is chosen, set the color of the
        'Pfizer' curve.

        For reference, see http://www.python-simple.com/img/img45.png.
    :type color_pal: str, optional, default='darkblue'
    :param color_pal2: Only if 'All vaccines' vaccine_type is chosen.
        Set the color of 'Moderna' curve.

        For reference, see http://www.python-simple.com/img/img45.png.
    :type color_pal2: str, optional, default='orangered'
    :param color_pal3: Only if 'All vaccines' vaccine_type is chosen.
        Set the color of 'AstraZeneca' curve.

        For reference, see http://www.python-simple.com/img/img45.png.
    :type color_pal3: str, optional, default='green'
    :param font_size: the size of characters in hover labels
    :type font_size: int, optional, default=16
    :param font_family: the font family of the characters in hover labels.

        For reference, see
        http://jonathansoma.com/site/lede/data-studio/matplotlib/list-all-fonts-available-in-matplotlib-plus-samples/
    :type font_family: str, optional, default='Franklin Gothic Medium'
    :param font_color: the color of characters in hover labels,
        For reference, see http://www.python-simple.com/img/img45.png.
    :type font_color: str, optional, default='white'
    :param bgcolor: the background color of all hover labels on graph.
        For reference, see http://www.python-simple.com/img/img45.png.
    :type bgcolor: str, optional, default='darkslategrey'
    :param template: the visual style we want the graph to be
        based on.

        For reference, see https://plotly.com/python/templates/.
    :type template: str, optional, default='plotly_dark'

    Returns
    -------
    :return: animated line chart representing the actual
        dose number of the chosen vaccine type (in storage).
    :rtype: plotly.graph_objects.Figure

    :Notes:

    **Manipulation tips:**

    - click on a vaccine type label on the top right of the graph to remove it from the chart.
    - click on the camera icon on the very top right of the chart to save the image as a png.
    - click on the 'zoom in' icon to zoom in, or on the icon 'zoom out' to zoom out, on the chart.
    - click on the 'autoscale' icon to let plotly autoscale the chart.

    **For colorbind safe colors**

    See https://colorbrewer2.org/#type=qualitative&scheme=Dark2&n=3.
    Default colors in that function are colorbind safe.
    '''
    start = time.time()
    df_Vac_type = load_datasets.Load_Vaccine_storage().save_as_df()
    df_Vac_type2 = df_Vac_type.groupby(['type_de_vaccin'])
    pfizer = df_Vac_type2.get_group('Pfizer').reset_index(drop=True)
    mdn = df_Vac_type2.get_group('Moderna').reset_index(drop=True)
    astra = df_Vac_type2.get_group('AstraZeneca').reset_index(drop=True)
    # choose dataframe according to vaccine_type argument
    if (vaccine_type == 'Pfizer'):
        df = pfizer.copy()
        vac_type = 'Pfizer'
        df.rename(columns={'nb_doses': 'Number of doses', 'date': 'Date'}, inplace=True)
        fig = px.line(df,
                      x='Date',
                      y='Number of doses',
                      color='type_de_vaccin',
                      labels={'type_de_vaccin': 'Vaccine type'},
                      color_discrete_map={'Pfizer': color_pal},
                      title='Evolution of Pfizer vaccine storage in France',
                      template=template)
    elif (vaccine_type == 'Moderna'):
        df = mdn.copy()
        vac_type = 'Moderna'
        df.rename(columns={'nb_doses': 'Number of doses', 'date': 'Date'}, inplace=True)
        fig = px.line(df,
                      x='Date',
                      y='Number of doses',
                      color='type_de_vaccin',
                      labels={'type_de_vaccin': 'Vaccine type'},
                      color_discrete_map={'Moderna': color_pal},
                      title='Evolution of Moderna vaccine storage in France',
                      template=template)
    elif (vaccine_type == 'AstraZeneca'):
        df = astra.copy()
        vac_type = 'AstraZeneca'
        df.rename(columns={'nb_doses': 'Number of doses', 'date': 'Date'}, inplace=True)
        fig = px.line(df,
                      x='Date',
                      y='Number of doses',
                      color='type_de_vaccin',
                      labels={'type_de_vaccin': 'Vaccine type'},
                      color_discrete_map={'AstraZeneca': color_pal},
                      title='Evolution of AstraZeneca vaccine storage in France',
                      template=template)
    elif (vaccine_type == 'All vaccines'):
        df = df_Vac_type.copy()
        vac_type = 'ALL'
        df.rename(columns={'nb_doses': 'Number of doses', 'date': 'Date'}, inplace=True)
        fig = px.line(df,
                      x='Date',
                      y='Number of doses',
                      color='type_de_vaccin',
                      labels={'type_de_vaccin': 'Vaccine type'},
                      color_discrete_map={'Pfizer': color_pal,
                                          'Moderna': color_pal2,
                                          'AstraZeneca': color_pal3},
                      title='Evolution of vaccine storage in France',
                      template=template)
    fig.update_traces(mode="markers + lines", hovertemplate=None)
    fig.update_layout(hovermode="x unified")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor='lightslategrey',
            font_color='white',
            font_size=16,
            font_family="Franklin Gothic Medium"
            )
        )
    end = time.time()
    print("Time to execute: {0:.5f} s.".format(end - start))
    # display line chart according to vaccine_type argument
    fig.show()


def vacdoses(unit='doses', font_size=16,
             font_family="Franklin Gothic Medium",
             font_color='white', bgcolor='darkslategrey',
             template='plotly_dark'):
    '''
    Make an interactive line chart of France vaccine storage.

    Parameters
    ----------
    :param unit: the type of dose units we want to display.
        Either 'doses' or 'cdu' (shorts for 'common dispensing units'),

        - 'doses':
            display the evolution of total vaccine doses in storage,
            from January 2021 until now. (checkouts are not made everyday).
        - 'cdu':
            display the evolution of total vaccine bottles in storage,
            from January 2021 until now. (checkouts are not made everyday).

        For 'Pfizer' vaccine, the cdu conversion rate per dose
        is multiplied by 6.
        For Moderna and AstraZeneca vaccines, the cdu conversion rate per dose
        is multiplied by 10.
    :type unit: str, optional, default='doses'
    :param font_size: the size of characters in hover labels.
    :type font_size: int, optional, default=16
    :param font_family: the font family of the characters in hover labels.
        For reference, see
        http://jonathansoma.com/site/lede/data-studio/matplotlib/list-all-fonts-available-in-matplotlib-plus-samples/.
    :type font_family: str, optional, default='Franklin Gothic Medium'
    :param font_color: the color of characters in hover labels.
        For reference, see http://www.python-simple.com/img/img45.png.
    :type font_color: str, optional, default='white'
    :param bgcolor: the background color of all hover labels on graph.

        For reference, see http://www.python-simple.com/img/img45.png.
    :type bgcolor: str, optional, default='darkslategrey'
    :param template: the visual style we want the graph to be
        based on.

        For reference, see https://plotly.com/python/templates/.
    :type template: str, optional, default='plotly_dark'

    Returns
    -------
    :return: An interactive line chart representing the actual
        amount in storage of vaccine doses, according to the chosen unit.
    :rtype: plotly.graph_objects.Figure

    :Notes:

    **Manipulation tips:**

    - click on the camera icon on the very top right of the chart to save the image as a png.

    - click on the 'zoom in' icon to zoom in, or on the icon 'zoom out' to zoom out, on the chart.

    - click on the 'autoscale' icon to let plotly autoscale the chart.

    '''
    start = time.time()
    df_Vac_type = load_datasets.Load_Vaccine_storage().save_as_df()
    df = df_Vac_type.groupby(['date'])['nb_doses',
                                       'nb_ucd'].agg('sum').reset_index()
    doses = df.groupby(['date'])['nb_doses'].size().reset_index()
    ucd = df.groupby(['date'])['nb_ucd'].size().reset_index()
    doses['nb_doses'] = df['nb_doses']
    doses.rename(columns={'nb_doses': 'Number of doses with basic unit',
                          'date': 'Date'}, inplace=True)
    ucd['nb_ucd'] = df['nb_ucd']
    ucd.rename(columns={'nb_ucd': 'Number of doses with ucd unit',
                        'date': 'Date'}, inplace=True)
    if (unit == 'doses'):
        df = doses.copy()
        nbr = 'Number of doses with basic unit'
        a = 'dose'
    else:
        df = ucd.copy()
        nbr = 'Number of doses with ucd unit'
        a = 'cdu'
    fig = px.line(
                df,
                x='Date',
                y=nbr,
                title=f"Evolution of vaccine {a} number in storage in France",
                template=template)
    fig.update_traces(mode="markers + lines", hovertemplate=None)
    fig.update_layout(hovermode="x unified")
    fig.update_layout(
        hoverlabel=dict(
            bgcolor=bgcolor,
            font_color=font_color,
            font_size=font_size,
            font_family=font_family
            ))
    end = time.time()
    print("Time to execute: {0:.5f} s.".format(end - start))
    # display line chart according to unit argument
    fig.show()


def keytimeseries(place='France', criterion='hospitalisation',
                  evo=True, average=True):
    """
    Make a time series about information concerning
    the evolution of the COVID-19 in France or a sub-part of France.

    Parameters
    ----------
    :param place: 'France' for the whole territory or the (french)
        name of a region,
        for reference,
        see https://www.regions-et-departements.fr/regions-francaises
    :type place: str, optional, default='France'
    :param criterion: The figure of interest in French suc as "deces" , "cas"

        - 'cas_confirmes':
            number of confirmed cases
        - 'deces':
            cumulated number of deaths
        - 'reanimation':
            number of people in intensive care
        - 'hospitalisation':
            number of hospitalized people
        - 'gueris':
            number of cured people

    :type criterion: str, optional, default='hospitalisation'

    :param evo:
        if True: new per day
        if False: cumulative
    :type evo: bool, optional, default=True
    :param average:
        if True: evolution on a 7 day moving average
    :type evo: bool, optional, default=True

    Returns
    -------
    :return: A time series until today since the beginning of the records of
        the figure of interest
    :rtype: plotly.graph_objects.Figure

    :Examples:
    >>> keytimeseries(place='Occitanie', criterion='gueris',
    ...               evo=False, average=True)

    >>> keytimeseries(place='France', criterion='cas_confirmes',
    ...               evo=True, average=False)

    """
    start = time.time()
    fr = (place == "France")
    if fr:
        df_covid = preprocess_chiffres_cles.gooddates(
                                        Load_chiffres_fr().save_as_df())
    if criterion in ["cas", "nombre_de_cas", "cas_confirmes"]:
        criterion = "cas_confirmes"
        key_legend = 'confirmed cases'
        if fr:
            criterion = "total_cas_confirmes"
    elif criterion in ["hospitalisation", "hôpital", "hospitalises"]:
        criterion = "hospitalises"
        key_legend = 'hospitalizations'
        if fr:
            criterion = "patients_hospitalises"
    elif criterion in ["deces_ehpad"]:
        key_legend = 'deaths in EHPAD'
        if fr:
            criterion = "total_deces_ehpad"
    elif criterion in ["morts", "deces", "deces_à_l'hôpital"]:
        criterion = "deces"
        key_legend = 'deaths'
        if fr:
            criterion = "total_deces_hopital"
    elif criterion in ["reanimation"]:
        key_legend = 'patients in intensive care'
        if fr:
            criterion = "patients_reanimation"

    elif criterion in ["cas_confirmes_ehpad"]:
        key_legend = 'confirmed cases in EHPAD'
        if fr:
            criterion = "total_cas_confirmes_ehpad"
    elif criterion in ["gueris"]:
        key_legend = 'cured patients'
        if fr:
            criterion = "total_patients_gueris"  # options with
            # different expressions for a same argument
    if fr:
        if evo:
            if average:
                axis = 'Average number'
                title = f'Evolution of the number of {key_legend} in France on a 7 day moving average'
                fig = px.line(
                        df_covid[criterion].diff().rolling(window=7).mean(),
                        title=title)
                fig = fig.update_yaxes(title_text=axis)
                fig.show()
                end = time.time()
                print("Time to execute: {0:.5f} s.".format(end - start))
                return
            axis = 'Number'
            title = f'Evolution of the number of {key_legend} in France'
            fig = px.line(df_covid[criterion].diff(), title=title)
            fig = fig.update_yaxes(title_text=axis)
            fig.show()
            end = time.time()
            print("Time to execute: {0:.5f} s.".format(end - start))
            return
        else:
            if average:
                axis = 'Cumulated average number'
                title = f'Evolution of the cumulated number of {key_legend} in France on a 7 day moving average'
                fig = px.line(df_covid[criterion].rolling(window=7).mean(),
                              title=title)
                fig = fig.update_yaxes(title_text=axis)
                fig.show()
                end = time.time()
                print("Time to execute: {0:.5f} s.".format(end - start))
                return
            axis = 'Cumulated number'
            title = f'Evolution of the cumulated number of {key_legend} in France'
            fig = px.line(df_covid[criterion], title=title)
            fig = fig.update_yaxes(title_text=axis)
            fig.show()
            end = time.time()
            print("Time to execute: {0:.5f} s.".format(end - start))
            return
    elif criterion in ["cas_confirmes"]:  # need specific datasets
        if place in REGIONS.keys():
            df = preprocess_positivity.ignoreage(
                            preprocess_positivity.granupositivity(
                                        Load_posquotreg().save_as_df(), place)).cumsum()
            series = df['P']
        elif place in DEPARTMENTS.keys():
            df = preprocess_positivity.ignoreage(
                            preprocess_positivity.granupositivity(
                                        Load_posquotreg().save_as_df(), place))
            series = df['P']
    else:
        series = preprocess_chiffres_cles.gooddates(
                    preprocess_chiffres_cles.keysubtablename(
                                                    place))[criterion].dropna()
    if evo:
        if average:
            axis = 'Average number'
            title = f'Evolution of the number of {key_legend} in {place} on a 7 day moving average'
            fig = px.line(series.diff().rolling(window=7).mean(),
                          title=title)
            fig = fig.update_yaxes(title_text=axis)
            fig.show()
            end = time.time()
            print("Time to execute: {0:.5f} s.".format(end - start))
            return
        axis = 'Number'
        title = f'Evolution of the number of {key_legend} in {place}'
        fig = px.line(series.diff(), title=title)
        fig = fig.update_yaxes(title_text=axis)
        fig.show()
        end = time.time()
        print("Time to execute: {0:.5f} s.".format(end - start))
        return
    else:
        if average:
            axis = 'Cumulated average number'
            title = f'Evolution of the cumulated number of {key_legend} in {place} on a 7 day moving average'
            fig = px.line(series.rolling(window=7).mean(), title=title)
            fig = fig.update_yaxes(title_text=axis)
            fig.show()
            end = time.time()
            print("Time to execute: {0:.5f} s.".format(end - start))
            return
        axis = 'Cumulated number'
        title = f'Evolution of the cumulated number of {key_legend} in {place}'
        fig = px.line(series, title=title)
        fig = fig.update_yaxes(title_text=axis)
        fig.show()
        end = time.time()
        print("Time to execute: {0:.5f} s.".format(end - start))
        return
