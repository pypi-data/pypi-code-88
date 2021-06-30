import pandas as pd
from prophet import Prophet


def prediction(pollutant, city, date):
    pollutant_choice = pollutant + " AQI"

    # read the csv file into a dataframe
    df = pd.read_csv('pollution_us_2000_2016.csv')

    # delete unnecessary data columns
    df = df.drop(columns=['Unnamed: 0', 'NO2 Units', 'O3 Units', 'SO2 Units', 'CO Units'])

    # delete duplicate data tuples
    df.drop_duplicates(inplace=True)

    # convert Date local to python date and time
    df['date'] = pd.to_datetime(df['Date Local'])
    df = df.drop(columns=['Date Local'])

    # compute mean AQI for each citiy for each date
    mean_aqi = df.groupby(['City', 'date'])[['NO2 AQI', 'O3 AQI', 'SO2 AQI', 'CO AQI']].mean()

    # reset index mean_aqi
    mean_aqi = mean_aqi.reset_index()

    # create subset of dataset to include only city and column selected for analysis
    new_df = mean_aqi.loc[mean_aqi['City'] == city, ['date', pollutant_choice]]

    new_df = new_df.rename(columns={"date": "ds",
                                    pollutant_choice: "y"})

    # use ffill (forward fill) to handle missing value filling the missing value from the previous day
    new_df = new_df.ffill()

    prophet_model = Prophet()
    prophet_model.fit(new_df)

    # the parameter 'periods' represents the number of days you want to predict after 2016-04-30
    future = prophet_model.make_future_dataframe(periods=2500)

    forecast = prophet_model.predict(future)

    # output = prophet_model.plot(forecast)
    # output.show()

    temp = forecast[forecast['ds'] == date]
    output = list(x for x in temp["yhat"])

    print(output[0])

    return output[0]





#if __name__ == "__main__":
    #pollutant_choice = "O3"
    #city_choice = "Washington"
   # prediction(pollutant_choice, city_choice)
