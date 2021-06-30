import numpy as np
import pandas as pd
import json
import requests
endpoint_fcst = 'https://elvia.azure-api.net/weather-ingest/api/Forecasts'

def temperature_hourly(df,
                       weather_variable: str,
                       start_date: str,
                       end_date: str,
                       time_zone: bool = False,
                       weather_token_id: str = '') -> pd.DataFrame:
    """
    This function loads the weather data for a specific substation for a given start_date & end_date and latitude & longitude. 

    # Parameters
    --------------
    df              : Pandas dataframe
    weather_variable: Refers to which weather variable we use. Here it is 'temperature'.
    start_date      : The day the temperature readings are started to be taken
    end_date        : The day the temperature readings are ended to be taken
    time_zone       : Weather data comes with timezone UTC. It can be set to Oslo-timezone by writing 'time_zone = True'
    weather_token_id: Token ID for accesing Weather API

    # Returns:
    --------------
    A dataframe with temperature and related substation ID variables with the index of datetime.
    """
    token = weather_token_id

    dataframe_list = []
    # Looping in substaions and getting temperature values from the Weather API. Then save it as a dataframe to dataframe_list
    for station in df['trafo'].unique():
        # latitude and longitude of each trafo
        longitude = df.loc[df['trafo'] == station]['long'][0]
        latitude = df.loc[df['trafo'] == station]['lat'][0]

        # Loads data for the respective weather variable
        input_data = {
            "startTime": start_date,
            "endTime": end_date,
            "coordinates": [{
                "latitude": latitude,
                "longitude": longitude
            }],
            "variables": [weather_variable]
        }

        # Access token and the media type of body sent to the API
        headers = {
            'Content-Type': 'application/json-patch+json',
            'Ocp-Apim-Subscription-Key': token
        }
        # Requesting data based on the input_data from the weather API
        r = requests.post(endpoint_fcst, json=input_data, headers=headers)
        while r.status_code != 200:
            print(r.status_code)
            r = requests.post(endpoint_fcst, json=input_data, headers=headers)

        weather_data_json = r.json()
        weather_data_temp = weather_data_json['coordinates'][0]['variables'][
            0]['data']
        weather_data_df = pd.DataFrame.from_records(
            weather_data_temp)  # converting structured data to dataframe

        # CHECK  TIME_ZONE IS
        weather_data_df['time'] = pd.to_datetime(weather_data_df['time'])
        weather_data_df = weather_data_df.set_index('time')
        weather_data_df.rename(columns={'value': weather_variable},
                               inplace=True)
        weather_data_df['trafo'] = station
        dataframe_list.append(weather_data_df)

    all_weather_data_df = pd.concat(
        dataframe_list)  # concatenating all dataframes

    if time_zone == True:
        # Convert to 'Europe/Oslo' time zone
        all_weather_data_df.index = all_weather_data_df.index.tz_convert(
            tz='Europe/Oslo')

    all_weather_data_df.reset_index(inplace=True)
    all_weather_data_df['temperature'] = all_weather_data_df['temperature'].astype(np.float32)

    return all_weather_data_df
