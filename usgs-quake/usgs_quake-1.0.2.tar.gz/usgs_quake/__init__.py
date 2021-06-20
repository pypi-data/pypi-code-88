import requests
import json
import pandas
import re
import datetime

BASE_URL = 'https://earthquake.usgs.gov/'
REALTIME_FEED = 'earthquakes/feed/v1.0/summary/{}_{}.geojson'
LEVELS = { 'significant', '4.5', '2.5', '1.0', 'all' }
PERIODS = { 'hour', 'day', 'week', 'month' }

FDSNWS_EVENT = 'fdsnws/event/1/query?format=geojson' + \
    '&starttime={}&endtime={}' + \
    '&minlatitude={}&maxlatitude={}' + \
    '&minlongitude={}&maxlongitude={}' + \
    '&minmagnitude={}'

class USGSEarthquake:
    """
    USGS Earthquake Data from Realtime Feed and Historical ANSS ComCat

    Attributes
    ----------
    min_lat: float
        minimum latitude boundary
    max_lat: float
        maximum latitude boundary
    min_lon: float
        minimum longitude boundary
    max_lon: float
        maximum longitude boundary
    min_mag: float
        minimum magnitude condition
    url: string
        realtime feed / historical query URL
    data: pandas.DataFrame
        earthquake dataframe
    """
    def __init__(self, min_lat, max_lat, min_lon, max_lon, min_mag):
        """
        Constructs the boundaries and conditions for USGS
        Realtime Feed or Historical Data Queries

        Parameters
        ----------
        min_lat: float
            minimum latitude boundary
        max_lat: float
            maximum latitude boundary
        min_lon: float
            minimum longitude boundary
        max_lon: float
            maximum longitude boundary
        min_mag: float
            minimum magnitude condition
        """
        self.min_lat = min_lat
        self.max_lat = max_lat
        self.min_lon = min_lon
        self.max_lon = max_lon
        self.min_mag = min_mag

    def _to_dataframe(self, features):
        """
        Convert the GeoJSON to Pandas Dataframe
        """
        df = pandas.DataFrame(features)

        properties = df.properties.apply(pandas.Series).copy()
        properties = properties.add_prefix('properties_')

        geometry = df.geometry.apply(pandas.Series).copy()
        coordinates = geometry.coordinates.apply(pandas.Series).copy()
        coordinates = coordinates.add_prefix('geometry_coordinates_')

        self.data = pandas.concat([properties, coordinates, df.id], axis = 1)

    def _filter_conditions(self):
        """
        Filter the dataframe by latitude, longitude, and minimum magnitude
        """
        conditions = (self.data.geometry_coordinates_0 > self.min_lon) & \
            (self.data.geometry_coordinates_1 < self.max_lon) & \
            (self.data.geometry_coordinates_2 > self.min_lat) & \
            (self.data.geometry_coordinates_2 < self.max_lat) & \
            (self.data.properties_mag > self.min_mag)

        self.data = self.data[conditions].copy()
        self.data.reset_index(inplace = True, drop = True)

    def _reformat_dataframe(self):
        """
        Reformat the dataframe
        """
        self.data.properties_mag = self.data.properties_mag.astype('float64')
        self.data.properties_time = self.data.properties_time.astype('datetime64[ms]')
        self.data.properties_updated = self.data.properties_updated.astype('datetime64[ms]')

        self.data.properties_cdi = self.data.properties_cdi.astype('float64')
        self.data.properties_mmi = self.data.properties_mmi.astype('float64')
        self.data.properties_dmin = self.data.properties_dmin.astype('float64')
        self.data.properties_rms = self.data.properties_rms.astype('float64')
        self.data.properties_gap = self.data.properties_gap.astype('float64')

        self.data.geometry_coordinates_0 = self.data.geometry_coordinates_0.astype('float64')
        self.data.geometry_coordinates_1 = self.data.geometry_coordinates_1.astype('float64')
        self.data.geometry_coordinates_2 = self.data.geometry_coordinates_2.astype('float64')

    def get_realtime_data(self, level = 'significant', period = 'hour'):
        """
        Get realtime earthquake data from the USGS GeoJSON Summary Feed

        Parameters
        ----------
        level: string
            magnitude level of earthquake: e.g. 'significant', '1.0', '2.5', '4.5'
        period: string
            period of events queried: e.g. 'hour', 'day', 'week', 'month'
        Returns
        -------
        None
        """
        self.url = BASE_URL + REALTIME_FEED.format(level, period)
        req = requests.get(self.url)
        assert(req.status_code == 200)

        summary = json.loads(req.text)
        count = summary['metadata']['count']

        if count > 0:
            self._to_dataframe(summary['features'])
            self._reformat_dataframe()
            self._filter_conditions()
            return(len(self.data))
        else:
            return count

    def get_historical_data(self, start, end):
        """
        Get historical earthquake data from USGS' ANSS ComCat

        Parameters
        ----------
        start: datetime.datetime or datetime.date
            start datetime
        end: datetime.datetime or datetime.date
            end datetime
        Returns
        -------
        None
        """
        self.url = BASE_URL + FDSNWS_EVENT.format(start.isoformat(),
            end.isoformat(), str(self.min_lat), str(self.max_lat), \
            str(self.min_lon), str(self.max_lon), str(self.min_mag))
        req = requests.get(self.url)
        assert(req.status_code == 200)

        summary = json.loads(req.text)
        count = summary['metadata']['count']

        if count > 0:
            self._to_dataframe(summary['features'])
            self._reformat_dataframe()
            self._filter_conditions()
            return(len(self.data))
        else:
            return count

    def get_simplified_dataframe(self):
        list_columns = ['id', 'properties_time', 'properties_place', \
            'geometry_coordinates_0', 'geometry_coordinates_1', \
            'geometry_coordinates_2', 'properties_mag', 'properties_url']
        df = self.data[list_columns].copy()
        df.columns = ['ID', 'Datetime', 'Place', 'Longitude', 'Latitude', \
            'Depth', 'Magnitude', 'URL']
        return df.copy()
