# ---------- requirements ----------
import time
import pandas as pd

import geopandas as gpd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np
import folium
import os

import pydeck as pdk
import ipywidgets
import json

# local reqs
from vizcovidfr.loads import load_datasets
from vizcovidfr.preprocesses import preprocess_chiffres_cles
from vizcovidfr.preprocesses import preprocess_maps

# add python option to avoid "false positive" warning:
pd.options.mode.chained_assignment = None  # default='warn'


# ---------- format some default arguments ----------

# format yesterday's date
dt_today = datetime.now()
dt_yesterday = (dt_today - timedelta(1))
yesterday = dt_yesterday.strftime('%Y-%m-%d')


# ---------- define viz2Dmap ----------
def viz2Dmap(granularity='departement', date=yesterday,
             criterion='hospitalises', color_pal='YlGnBu',
             file_path='~/Desktop/vizcovidfr_files/', file_name='Covid2Dmap'):
    '''
    Make interactive choropleth map to visualize different aspects of the
    Covid-19 pandemic in France. The map is saved on an html file at a given
    path on a given name, see function parameters for details.

    Parameters
    ----------
    :param granularity: the granularity we want the map to be based on.
        Should be either 'region' or 'departement'.
    :type granularity: str, optional, default='departement'
    :param date: the date on which we want to get Covid-19 information.
        Should be of the form 'YYYY-MM-DD', and from 2020-01-24 to yesterday,
        (because the database is updated on the end of every day, so depending
        on the hour you want to use the function,
        today's data might not exist yet)
    :type date: str, optional, default=yesterday
    :param criterion: the Covid-19 indicator we want to see on the map.
        Should be either 'hospitalises', 'reanimation', or 'deces':

        - 'hospitalises':
            display the number of persons hospitalized
            on the given date due to Covid-19
        - 'reanimation':
            display the number of persons in intensive care
            on the given date due to Covid-19
        - 'deces':
            display the cumulated number of death due to
            the Covid-19 in France from the beginning of the pandemic, up to
            the given date

    :type criterion: str, optional, default='hospitalises'
    :param color_pal: the color palette we want for the map.

        For reference,
        see https://colorbrewer2.org/#type=sequential&scheme=YlGnBu&n=3,
        defaults to 'YlGnBu' (for color-blind people purpose)
    :type color_pal: str, optional, default='YlGnBu'
    :param file_path: the path on which to save the file, can be either Linux,
        MAC-OS, or Windows path.

            (*) **Warning:** the default parameter only works if the user's
            OS default language is english. Otherwise,
            path is **not optional**.
    :type file_path: str, optional*, default to a folder 'vizcovidfr_files'
        in the user's Desktop
    :param file_name: the name under which to save the file
    :type file_name: str, optional, default='Covid2Dmap'

    Returns
    -------
    :return: An interactive choropleth map saved on a html file openable on
        your favorite web browser
    :rtype: '.html' file

    :Examples:

    **easy example**

    >>> viz2Dmap()

    **example using Linux path**

    >>> import os
    >>> path_to_Documents = os.path.expanduser("~/Documents")
    >>> viz2Dmap(granularity='region', date='2020-12-25', criterion='deces',
    ...          color_pal='Greys', file_path=path_to_Documents,
    ...          file_name='creepymap')

    **example using Windows path**

    >>> W_path = 'c:\\Users\\username\\Documents'
    >>> viz2Dmap(granularity='department', date='2021-01-17',
    ...          criterion='reanimation', color_pal='Greys',
    ...          file_path=W_path, file_name='funkymap')

    :Notes:

    **Manipulation tips:**

    - pass mouse on map to get local information
    - use 'clic + mouse move' to move map
    '''
    # ---------- file imports ----------
    # load geojson file containing geographic information
    start = time.time()
    reg_path = os.path.join(
                    os.path.dirname(
                        os.path.realpath(__file__)),
                    "geodata", "regions.geojson")
    dep_path = os.path.join(
                    os.path.dirname(
                        os.path.realpath(__file__)),
                    "geodata", "departements.geojson")
    regions = gpd.read_file(reg_path)
    departments = gpd.read_file(dep_path)
    # load covid data
    df_covid = load_datasets.Load_chiffres_cles().save_as_df()
    # ---------- preprocesses ----------
    # use preprocess to clean df_covid
    df_covid = preprocess_chiffres_cles.drop_some_columns(df_covid)
    df_covid = preprocess_chiffres_cles.reg_depts(df_covid)
    df_covid = preprocess_chiffres_cles.reg_depts_code_format(df_covid)
    # keep only data corresponding to the given granularity
    df_local = df_covid.loc[df_covid['granularite'] == granularity]
    # choose the dataframe containing geographic
    # information according to the granularity
    # (plus english precision)
    if (granularity == 'departement'):
        df = departments.copy()
        gra = 'department'
    else:
        df = regions.copy()
        gra = 'region'
    # merge on the 'code' column
    df_merged = pd.merge(df_local, df, on="code")
    # keep only data corresponding to the given date
    at_date = df_merged.loc[df_merged['date'] == date]
    # convert to GeoPandas dataframe
    gpd_at_date = gpd.GeoDataFrame(at_date)
    # -------- format legend ----------
    # format date for legend purpose
    given_date = datetime.strptime(date, '%Y-%m-%d')
    given_date = given_date.strftime("%A %d. %B %Y")
    # format crierion for legend purpose
    if (criterion == 'hospitalises'):
        formulated_criterion = 'hospitalization'
    elif (criterion == 'reanimation'):
        formulated_criterion = 'resuscitation'
    else:
        formulated_criterion = 'death'
    # change legend and title according to criterion
    if (criterion == 'deces'):
        legend = f'Cumulated number of {formulated_criterion} per {gra}'
        title = f'Cumulated number of {formulated_criterion} per {gra} in\
                France from the beginning of the pandemic up to {given_date}'
    else:
        legend = f'Number of {formulated_criterion} per {gra}'
        title = f'Number of {formulated_criterion} per {gra}\
                in France on {given_date}'
    # ---------- make map! ----------
    # initialize view (centered on Paris!)
    map = folium.Map(location=[46.2322, 2.20967], zoom_start=6, tiles=None)
    folium.TileLayer('CartoDB positron',
                     name="Light Map",
                     control=False).add_to(map)
    # add choropleth
    map.choropleth(
            geo_data=gpd_at_date,
            name='Choropleth',
            data=gpd_at_date,
            columns=['code', criterion],
            key_on="feature.properties.code",
            fill_color=color_pal,
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name=legend,
            smooth_factor=0
    )
    # Pep8 doesn't seem to like lambda expressions...
    # but I do, so I let these like that
    style_function = lambda x: {'fillColor': '#ffffff',
                                'color': '#000000',
                                'fillOpacity': 0.1,
                                'weight': 0.1}
    highlight_function = lambda x: {'fillColor': '#000000',
                                    'color': '#000000',
                                    'fillOpacity': 0.50,
                                    'weight': 0.1}
    # make interactivity!
    geo_interact = folium.features.GeoJson(
                            gpd_at_date,
                            style_function=style_function,
                            control=False,
                            highlight_function=highlight_function,
                            tooltip=folium.features.GeoJsonTooltip(
                                fields=['nom', 'date', criterion],
                                style=("background-color: white;\
                                color: #333333; font-family: arial;\
                                font-size: 12px; padding: 10px;")
                                ))
    # add interactivity to the initial map
    map.add_child(geo_interact)
    # keep interactive layer on top of the map
    map.keep_in_front(geo_interact)
    folium.LayerControl().add_to(map)
    # add title
    title_html = '''
                 <h3 align="center" style="font-size:16px"><b>{}</b></h3>
                 '''.format(title)
    map.get_root().html.add_child(folium.Element(title_html))
    # save map
    file_path = preprocess_maps.map_save_path_routine(file_path)
    suffix = '.html'
    save_path = os.path.join(file_path, file_name + suffix)
    map.save(save_path)
    sms1 = f"\nThat's it! \n{file_name + suffix} has been successfully saved"
    sms2 = f" in {file_path}! \nYou can go ahead and open it with your"
    sms3 = " favorite web browser!"
    print(sms1 + sms2 + sms3)
    end = time.time()
    print("Time to execute: {0:.5f} s.".format(end - start))


# TODO:
# NOTE: it worked without importing df_covid...


# ---------- define viz3Dmap ----------
def viz3Dmap(granularity='departement', criterion='hospitalises',
             file_path='~/Desktop/vizcovidfr_files/', file_name='Covid3Dmap',
             color=[255, 165, 0, 80]):
    '''
    Make a 3D map out of France Covid-19 data.
    Layers elevation represent the amount of death for the given place at a
    given day, which can be view by passing the mouse on it.

    Parameters
    ----------
    :param granularity: the granularity we want the map to be based on.
        Should be either 'region' or 'departement'. On the latter case,
        columns layers will be raised from the centroid of each department,
        while on the former, these will be raides from each region's centroid.
    :type granularity: str, optional, default='departement'
    :param criterion: the Covid-19 indicator we want to see on the map.
        Should be either 'hospitalises', 'reanimation', or 'deces':

        - 'hospitalises':
            display the number of persons hospitalized
            on a given date due to Covid-19
        - 'reanimation':
            display the number of persons in intensive care
            on a given date due to Covid-19
        - 'deces':
            display the cumulated number of death due to
            the Covid-19 in France from the beginning of the pandemic, up to
            a given date

    :type criterion: str, optional, default='hospitalises'
    :param color: color for columns. Should be a list
        containing RGBA colors (red, green, blue, alpha).

        Need inspiration? see here https://rgbacolorpicker.com/
    :type color: list, optional, default=[255, 165, 0, 80] ~yellow
    :param file_path: the path on which to save the file, can be either Linux,
        MAC-OS, or Windows path.

            (*) **Warning:** the default parameter only works if the user's
            OS default language is english. Otherwise,
            path is **not optional**.
    :type file_path: str, optional*, default to a folder 'vizcovidfr_files'
        in the user's Desktop
    :param file_name: the name under which to save the file
    :type file_name: str, optional, default='Covid3Dmap'

    Returns
    -------
    :return: An interactive 3D map saved on a html file openable on
        your favorite web browser
    :rtype: '.html' file

    :Examples:

    **easy example**

    >>> viz3Dmap()

    **example using Linux path**

    >>> import os
    >>> path_to_Documents = os.path.expanduser("~/Documents")
    >>> viz3Dmap(file_path=path_to_Documents, file_name='rea_3D_map',
    ...          granularity='departement', criterion='reanimation',
    ...          color=[245, 92, 245, 80])

    **example using Windows path**

    >>> W_path = 'c:\\Users\\username\\Documents'
    >>> viz3Dmap(file_path=W_path, color=[230, 37, 37, 80],
    ...          criterion='deces')

    :Notes:

    The bottom of the map corresponds to the beginning of the Covid-19
    pandemic in France, specifically here, data start on 2020-01-24. The top
    of the columns corresponds to now.

    **Manipulation tips:**

    - pass mouse on columns to see time evolution
    - use 'ctrl + mouse move' to change view angle
    - use 'clic + mouse move' to move map
    '''
    # ---------- file imports ----------
    start = time.time()
    # geo files
    reg_path = os.path.join(
                    os.path.dirname(
                        os.path.realpath(__file__)),
                    "geodata", "regions.geojson")
    dep_path = os.path.join(
                    os.path.dirname(
                        os.path.realpath(__file__)),
                    "geodata", "departements.geojson")
    reg = gpd.read_file(reg_path)
    dep = gpd.read_file(dep_path)
    # covid files
    df_covid = load_datasets.Load_chiffres_cles().save_as_df()
    # ---------- preprocesses ----------
    df_covid = preprocess_chiffres_cles.drop_some_columns(df_covid)
    df_covid = preprocess_chiffres_cles.reg_depts(df_covid)
    df_covid = preprocess_chiffres_cles.reg_depts_code_format(df_covid)
    # choose dataframe according to granularity argument
    if (granularity == 'departement'):
        df = dep.copy()
        gra = 'department'
    else:
        df = reg.copy()
        gra = 'region'
    # format crierion for markers purpose
    if (criterion == 'hospitalises'):
        tooltip = {
            "html": "<b>Place:</b> {nom} <br /><b>Date:</b> {date}\
            <br /><b>Number of hospitalization:</b> {hospitalises}"}
    elif (criterion == 'reanimation'):
        tooltip = {
            "html": "<b>Place:</b> {nom} <br /><b>Date:</b> {date}\
            <br /><b>Number of persons in intensive care:</b> {reanimation}"}
    else:
        tooltip = {
            "html": "<b>Place:</b> {nom} <br /><b>Date:</b> {date}\
            <br /><b>Cumulated number of death:</b> {deces}"}
    # for covid data
    df_local = df_covid.loc[df_covid['granularite'] == granularity]
    # for geo data
    # grab department's centroids (lat and lon)
    df_points = df.copy()
    # set Europe Coordinate Reference System for geographic accuracy purpose
    df_points = df_points.set_crs(epsg=3035, allow_override=True)
    df_points['geometry'] = df_points['geometry'].centroid
    # merging on 'code'
    A = pd.merge(df_local, df_points, on='code')
    # separate latitude and longitude
    A['lon'] = A.geometry.apply(lambda p: p.x)
    A['lat'] = A.geometry.apply(lambda p: p.y)
    # ---------- make map! ----------
    # initialize view (centered on Paris!)
    view = pdk.ViewState(latitude=46.2322,
                         longitude=2.20967,
                         pitch=50,
                         zoom=5.5)
    # add pydeck layers
    covid_amount_layer = pdk.Layer('ColumnLayer',
                                   data=A,
                                   get_position=['lon', 'lat'],
                                   get_elevation=criterion,
                                   elevation_scale=100,
                                   radius=7000,
                                   get_fill_color=color,
                                   pickable=True,
                                   auto_highlight=True)
    # render map
    covid_amount_layer_map = pdk.Deck(layers=covid_amount_layer,
                                      initial_view_state=view,
                                      tooltip=tooltip)
    # save map
    file_path = preprocess_maps.map_save_path_routine(file_path)
    suffix = '.html'
    save_path = os.path.join(file_path, file_name + suffix)
    covid_amount_layer_map.to_html(save_path)
    # show map
    covid_amount_layer_map.show()
    sms1 = f"\nThat's it! \n{file_name + suffix} has been successfully saved"
    sms2 = f" in {file_path}! \nYou can go ahead and open it with your"
    sms3 = " favorite web browser!"
    print(sms1 + sms2 + sms3)
    end = time.time()
    print("Time to execute: {0:.5f} s.".format(end - start))


# ---------- define transfer_map ----------
def transfer_map(file_path='~/Desktop/vizcovidfr_files/',
                 file_name='Covid_transfer_map',
                 color_d=[243, 31, 44, 80], color_a=[230, 190, 37, 80]):
    """
    Make interactive 3D-arc-map to visualize the transfer of Covid-19
    patient in France from regions to others.

    Parameters
    ----------

    :param color_d: color for departure point on arcs. Should be a list
        containing RGBA colors (red, green, blue, alpha).

        Need inspiration? see here https://rgbacolorpicker.com/
    :type color_d: list, optional, default=[243, 31, 44, 80] ~red
    :param color_a: color for arrival point on arcs. Should be a list
        containing RGBA colors (red, green, blue, alpha).

        Need inspiration? see here https://rgbacolorpicker.com/
    :type color_a: list, optional, default=[230, 190, 37, 80] ~yellow
    :param file_path: the path on which to save the file, can be either Linux,
        MAC-OS, or Windows path.

            (*) **Warning:** the default parameter only works if the user's
            OS default language is english. Otherwise,
            path is **not optional**.
    :type file_path: str, optional*, default to a folder 'vizcovidfr_files'
        in the user's Desktop
    :param file_name: the name under which to save the file
    :type file_name: str, optional, default='Covid_transfer_map'

    Returns
    -------
    :return: An interactive 3D-arc-map saved on a html file openable on
        your favorite web browser
    :rtype: '.html' file

    :Examples:

    **easy example**

    >>> transfer_map()

    **example using Linux path**

    >>> import os
    >>> path_to_Documents = os.path.expanduser("~/Documents")
    >>> transfer_map(file_path=path_to_Documents, file_name='arc_map',
    ...          color_d=[255, 165, 0, 80], color_a=[128, 0, 128, 80])

    **example using Windows path**

    >>> W_path = 'c:\\Users\\username\\Documents'
    >>> transfer_map(file_path=W_path, file_name='counter_intuitive_arc_map',
    ...          color_d=[61, 230, 37, 80], color_a=[230, 37, 37, 80])

    :Notes:

    **Manipulation tips:**

    - pass mouse on arc to see tooltip
    - use 'ctrl + mouse move' to change view angle
    - use 'clic + mouse move' to move map
    """
    start = time.time()
    # ---------- covid file ----------
    transfer = load_datasets.Load_transfer().save_as_df()
    # Keep trace of transfer order
    # because rows get mixed up when merging.
    # number transfer from first to last
    transfer_order = np.arange(0, len(transfer), 1)
    # add transfer_order column
    transfer['order'] = transfer_order
    # ---------- geo files ----------
    # only need regions here
    reg_path = os.path.join(
                    os.path.dirname(
                        os.path.realpath(__file__)),
                    "geodata", "regions.geojson")
    regions = gpd.read_file(reg_path)
    # grab region's centroids (lat and lon)
    region_points = regions.copy()
    # set Europe Coordinate Reference System for geographic accuracy purpose
    region_points = region_points.set_crs(epsg=3035, allow_override=True)
    region_points['geometry'] = region_points['geometry'].centroid
    # extract departure information
    departure = transfer[['region_depart', 'order', 'debut_transfert']]
    departure['nom'] = departure['region_depart']
    # extract departure information
    arrival = transfer[['region_arrivee',
                        'nombre_patients_transferes',
                        'order']]
    arrival['nom'] = arrival['region_arrivee']
    # get departure and arrival geographic coordinates
    D = pd.merge(departure, region_points, on="nom")
    A = pd.merge(arrival, region_points, on="nom")
    # extract latitude and longitude
    # for departure
    D['lon_d'] = D.geometry.apply(lambda p: p.x)
    D['lat_d'] = D.geometry.apply(lambda p: p.y)
    # for arrival
    A['lon_a'] = A.geometry.apply(lambda p: p.x)
    A['lat_a'] = A.geometry.apply(lambda p: p.y)
    # delete not-useful-anymore columns for clarity purpose
    del D['nom']
    del D['geometry']
    del A['nom']
    del A['geometry']
    # merge these new dataframes together
    # (on order so that we have our chronology back!)
    DA = pd.merge(A, D, on='order')
    # save for sparse matrix purpose ?
    # DA.to_csv('departure_arrival.csv')
    # ---------- map time! ----------
    # initialize view (centered on Paris!)
    view = pdk.ViewState(latitude=46.2322, longitude=2.20967, pitch=50, zoom=5)
    # make arc layers from departure to arrival points
    arc_layer = pdk.Layer('ArcLayer',
                          data=DA,
                          get_source_position=['lon_d', 'lat_d'],
                          get_target_position=['lon_a', 'lat_a'],
                          get_width=5,
                          get_tilt=15,
                          get_source_color=color_d,
                          get_target_color=color_a,
                          # interactivity
                          pickable=True,
                          auto_highlight=True)
    # add tooltip
    tooltip = {
            "html": "<b>Date:\
            </b> {debut_transfert} <br />\
            <b>Number of transfered patient:\
            </b> {nombre_patients_transferes} <br />\
            <b>Departure region:</b> {region_depart} <br />\
            <b>Arrival region:</b> {region_arrivee}\
            "}
    # add view and layer to map
    arc_layer_map = pdk.Deck(layers=arc_layer,
                             initial_view_state=view,
                             tooltip=tooltip)
    # save map
    file_path = preprocess_maps.map_save_path_routine(file_path)
    suffix = '.html'
    save_path = os.path.join(file_path, file_name + suffix)
    arc_layer_map.to_html(save_path)
    sms1 = f"\nThat's it! \n{file_name + suffix} has been successfully saved"
    sms2 = f" in {file_path}! \nYou can go ahead and open it with your"
    sms3 = " favorite web browser!"
    print(sms1 + sms2 + sms3)
    end = time.time()
    print("Time to execute: {0:.5f} s.".format(end - start))


# TODO:
# remove # save for sparse matrix purpose ? if not needed


# ---------- define vacmap function ----------
def vacmap(granularity='region', age_range='all ages',
           file_path='~/Desktop/vizcovidfr_files/', file_name='vacmap',
           color_rgb=[255, 69, 0, 150]):
    '''
    Make an interactive map of France vaccine data.

    Parameters
    ----------
    :param granularity: the granularity we want the map to be based on.
        Either 'region' or 'department'. On the latter case,
        column layers will be raised from the centroid of each department,
        while on the former case, they will be raised from each region's
        centroid.
    :type granularity: str, optional, default='region'
    :param age_range: the age range we want to have information about
        vaccination.

        It can be '18-24', '25-29', '30-39', '40-49', '50-59', '60-64',
        '65-69', '70-74', '75-79', '80 and +', or 'all ages'.
        This last one represents the cumulation of all the age ranges.
    :type age_range: str, optional, default='all ages'
    :param file_path: the path on which to save the file, can be either Linux,
        MAC-OS, or Windows path.

            (*) **Warning:** the default parameter only works if the user's
            OS default language is english. Otherwise,
            path is **not optional**.
    :type file_path: str, optional*, default to a folder 'vizcovidfr_files'
        in the user's Desktop
    :param file_name: the name under which to save the file.
    :type file_name: str, optional, default='vacmap'

    Returns
    -------
    :return: an interactive map representing the actual amount of both first
        and second doses, per granularity and per age range, according to
        the chosen argument.
    :rtype: '.html' file

    :Examples:

    **easy example**

    >>> vacmap()

    **example using Linux path**

    >>> import os
    >>> path_to_Documents = os.path.expanduser("~/Documents")
    >>> vacmap(granularity='region', age_range='all ages',
    ...        file_path=path_to_Documents, file_name='vaccine_map',
    ...        color=[245, 92, 245, 80])

    **example using Windows path**

    >>> W_path = 'c:\\Users\\username\\Documents'
    >>> vacmap(granularity='department', age_range='18-24',
    ...        file_path=path_to_desktop, file_name='vaccine_map',
    ...        color = [207, 67, 80, 140])

    '''
    start = time.time()
    # load vaccin dataset
    df_Vac = load_datasets.Load_vaccination().save_as_df()
    df_Vac.sort_values(by=['Date', 'Valeur de la variable'], inplace=True)
    # load geographic datasets
    reg_path = os.path.join(
                    os.path.dirname(
                        os.path.realpath(__file__)),
                    "geodata", "regions.geojson")
    dep_path = os.path.join(
                    os.path.dirname(
                        os.path.realpath(__file__)),
                    "geodata", "departements.geojson")
    rgn = gpd.read_file(reg_path)
    dpt = gpd.read_file(dep_path)
    # make groups
    df_Vac = df_Vac.groupby(['Valeur de la variable'])
    till_24 = df_Vac.get_group(24).reset_index(drop=True)
    till_29 = df_Vac.get_group(29).reset_index(drop=True)
    till_39 = df_Vac.get_group(39).reset_index(drop=True)
    till_49 = df_Vac.get_group(49).reset_index(drop=True)
    till_59 = df_Vac.get_group(59).reset_index(drop=True)
    till_64 = df_Vac.get_group(64).reset_index(drop=True)
    till_69 = df_Vac.get_group(69).reset_index(drop=True)
    till_74 = df_Vac.get_group(74).reset_index(drop=True)
    till_79 = df_Vac.get_group(79).reset_index(drop=True)
    sup_80 = df_Vac.get_group(80).reset_index(drop=True)
    all_ages = df_Vac.get_group(0).reset_index(drop=True)
    # choose dataframe according to age_range argument
    if (age_range == '18-24'):
        df = till_24.copy()
        age = '18-24'
    elif (age_range == '25-29'):
        df = till_29.copy()
        age = '25-29'
    elif (age_range == '30-39'):
        df = till_39.copy()
        age = '30-39'
    elif (age_range == '40-49'):
        df = till_49.copy()
        age = '40-49'
    elif (age_range == '50-59'):
        df = till_59.copy()
        age = '50-59'
    elif (age_range == '60-24'):
        df = till_64.copy()
        age = '60-64'
    elif (age_range == '65-69'):
        df = till_69.copy()
        age = '65-69'
    elif (age_range == '70-74'):
        df = till_74.copy()
        age = '70-74'
    elif (age_range == '75-79'):
        df = till_79.copy()
        age = '65-79'
    elif (age_range == '80 and +'):
        df = sup_80.copy()
        age = '80 and +'
    elif (age_range == 'all ages'):
        df = all_ages.copy()
        age = 'all ages'
    # choose dataframe according to granularity argument
    if (granularity == 'department'):
        df2 = dpt.copy()
        gra = 'department'
        df['code'] = df['Code Officiel Département']
        df3 = df.groupby(['Date',
                          'code'])['Nombre cumulé de doses n°1',
                                   'Nombre cumulé de vaccinations complètes (doses n°2)'].agg('sum').reset_index()
        # pick the latest cumulation per granularity
        df3 = df3.groupby(['code']).agg('max')
        df3['code'] = df3.index
        df3.reset_index(drop=True, inplace=True)
        df3.drop([76, 97], 0, inplace=True)  # non-existent departments
        # no localisation data for these departments:
        df3.drop([98, 99, 100, 101, 102, 103, 104], 0, inplace=True)
    else:
        df2 = rgn.copy()
        gra = 'region'
        df['code'] = df['Code Officiel Région']
        df3 = df.groupby(['Date',
                          'code'])['Nombre cumulé de doses n°1',
                                   'Nombre cumulé de vaccinations complètes (doses n°2)'].agg('sum').reset_index()
        # pick the latest cumule per granularity
        df3 = df3.groupby(['code']).agg('max')
        df3['code'] = df3.index
        df3.reset_index(drop=True, inplace=True)
        df3['code'] = df3['code'].astype(int)
        df3['code'] = df3['code'].astype(str)
        df3['code'][0] = '01'
        df3['code'][1] = '02'
        df3['code'][2] = '03'
        df3['code'][3] = '04'
        df3['code'][4] = '06'
        df3.drop([18, 19], 0, inplace=True)
        # 977 and 978 are departments, not regions
    # grab department centroids (lat and lon)
    df_points = df2.copy()
    df_points = df_points.set_crs(epsg=3035, allow_override=True)
    df_points['geometry'] = df_points['geometry'].centroid
    # merge dataframes
    df_merged = pd.merge(df3, df_points, on='code')
    df_merged['lon'] = df_merged.geometry.apply(lambda p: p.x)
    df_merged['lat'] = df_merged.geometry.apply(lambda p: p.y)
    if (granularity == 'department'):
        df_merged.rename(
            columns={'Nombre cumulé de doses n°1': 'Nmb of first doses',
                     'code': 'department_code', 'nom': 'department_name',
                     'Nombre cumulé de vaccinations complètes (doses n°2)': 'Nmb of second doses'}, inplace=True)
    else:
        df_merged.rename(
            columns={'Nombre cumulé de doses n°1': 'Nmb of first doses',
                     'code': 'region_code', 'nom': 'region_name',
                     'Nombre cumulé de vaccinations complètes (doses n°2)': 'Nmb of second doses'}, inplace=True)
    # ---------- make map! ----------
    # initialize view (centered on Paris!)
    view = pdk.ViewState(latitude=46.2322,
                         longitude=2.20967,
                         pitch=50,
                         zoom=6)
    covid_amount_layer = pdk.Layer('ColumnLayer',
                                   data=df_merged,
                                   get_position=['lon', 'lat'],
                                   get_elevation=150,
                                   elevation_scale=50,
                                   radius=10000,
                                   get_fill_color=[255, 69, 0, 150],
                                   pickable=True,
                                   auto_highlight=True)
    if (granularity == 'department'):
        tooltip = {
            "html": "<b>{Nmb of first doses}</b> first doses and\
                     <b>{Nmb of second doses}</b> second doses,\
                     in <b>{department_name}</b>",
            "style": {"background": "grey",
                      "color": "white",
                      "font-family": '"Helvetica Neue", Arial',
                      "z-index": "10000"},
                   }
    else:
        tooltip = {
            "html": "<b>{Nmb of first doses}</b> first doses and\
                    <b>{Nmb of second doses}</b> second doses,\
                    in <b>{region_name}</b>",
            "style": {"background": "grey",
                      "color": "white",
                      "font-family": '"Helvetica Neue", Arial',
                      "z-index": "10000"},
                   }
    r = pdk.Deck(covid_amount_layer,
                 initial_view_state=view,
                 tooltip=tooltip)
    # save map
    file_path = preprocess_maps.map_save_path_routine(file_path)
    suffix = '.html'
    save_path = os.path.join(file_path, file_name + suffix)
    r.to_html(save_path)
    sms1 = f"\nThat's it! \n{file_name + suffix} has been successfully saved"
    sms2 = f" in {file_path}! \nYou can go ahead and open it with your"
    sms3 = " favorite web browser!"
    print(sms1 + sms2 + sms3)
    end = time.time()
    print("Time to execute: {0:.5f} s.".format(end - start))
