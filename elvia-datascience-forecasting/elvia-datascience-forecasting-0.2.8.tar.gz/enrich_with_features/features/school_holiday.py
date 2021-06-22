import json
import pandas as pd
from datetime import datetime

def school_holiday(df: pd.DataFrame,
                   region: str = 'Hedmark',
                   path_holiday: str = '',
                   substation_list: list = []) -> pd.DataFrame:
    '''
    Loads Norwegian school holidays and adds true if the index is a holiday to the dateframe otherwise false.
    Note that Sunday is considered a holiday in this set.
    
    # Parameters
    --------------
    df: Dataframe
    region: Region of substation
    path_holiday: The path of the json file that contains dates of school holidays
    substation_list: List of substation IDs

    # Returns:
    --------------
    Dataframe with the school_holiday and substation ID variables
    '''
    # Read the json file with holidays
    with open(path_holiday, 'r') as fn:
        h_n = json.load(fn)

    # elevdag_list contains planingdays at school in different regions
    elevdag_list = [
        'Fri inneklemt dag 2018', 'Fri inneklemt dag 2019',
        'Fri inneklemt dag 2020', 'Fri inneklemt dag 2021'
    ]

    # Looping each trafo and create datetime index from dates of school holidays in the trafos.
    # Then create new feature consists of True/False if related date is in the datetime index of the school holidays or not
    for station_id in df['trafo'].unique():
        # for station_id in df_holiday['station_region'].unique():
        station_region = df.loc[df['trafo'] ==
                                station_id]['fylkesnavn'].values[0]
        # regional_holidays contains datetime index of the longer holidays i.e. Summer, Easter etc.
        regional_holidays = pd.to_datetime([])
        for i in h_n['data']['school_holiday']:
            if i['region'] == station_region:
                for region_ferie in i['holiday']:
                    if region_ferie['description'] not in elevdag_list:
                        vec = pd.date_range(
                            start=datetime.strptime(region_ferie['date_start'],
                                                    '%Y-%m-%d'),
                            end=datetime.strptime(region_ferie['date_stop'],
                                                  '%Y-%m-%d'),
                            freq='D',
                            tz='UTC',  # Europe/Oslo
                            closed='left')
                        if regional_holidays.empty:
                            regional_holidays = vec
                        else:
                            regional_holidays = regional_holidays.append(vec)

        # create a holiday dataframe
        school_holiday = regional_holidays.to_frame().copy()

        # Creates a column with dates in the main dataframe
        frame = pd.DataFrame()
        frame['date'] = df.loc[df['trafo'] == station_id].index.date

        # Checks if datetime is holiday and add True/False.
        df.loc[df['trafo'] == station_id,
               'school_holiday'] = frame['date'].isin(
                   school_holiday.index.date).values

    return df
