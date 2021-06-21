import pandas
import requests
import json
import datetime

BASE_URL = 'https://webcritech.jrc.ec.europa.eu/TAD_server/'
GROUPS_API = 'api/Groups/GetGEOJSON?group={}&maxLatency={}'
DATA_API = 'api/Data/Get/{}?tMin={}%20{}&tMax={}%20{}&nRec={}&mode=json'

class IDSLGauge:
    """
    Python Wrapper for IDSL Tide Gauges API from JRC WebCritech

    Attributes
    ----------
    group: string
        group name (e.g. Indonesia or IDSL)
    max_latency: int
        maximum latency in seconds
    metadata: pandas.DataFrame
        metadata from available stations
    stations: list
        list of station_id
    data: pandas.DataFrame
        tide gauges data
    """
    def __init__(self, group, max_latency):
        """
        IDSL Tide Gauges Data from JRC Webcritech

        Attributes
        ----------
        group: group
        """
        self.group = group
        self.max_latency = max_latency

    def get_metadata(self):
        """
        Get metadata from active tide gauge stations
        """
        # Get stations metadata from GeoJSON API
        url = BASE_URL + GROUPS_API.format(self.group, self.max_latency)
        req = requests.get(url)
        assert(req.status_code == 200)

        # Create stations DataFrame
        summary = json.loads(req.text)
        df = pandas.DataFrame(summary[0]['features'])
        df.set_index('id', inplace = True, drop = True)

        # Obtain Latitude and Longitude
        geometry = df.geometry.apply(pandas.Series).copy()
        coordinates = geometry.coordinates.apply(pandas.Series).copy()
        coordinates.columns = ['Longitude', 'Latitude']

        # Obtain metadata
        properties = df.properties.apply(pandas.Series).copy()
        latency = properties.Latency.apply(pandas.Series).copy()

        # Dropping unused columns
        properties_drop = ['LastData', 'Latency', 'GroupColor']
        properties.drop(properties_drop, axis = 1, inplace = True)
        latency_drop = ['Literal', 'Color']
        latency.drop(latency_drop, axis = 1, inplace = True)
        latency.columns = ['Latency_Seconds']

        # Add attributes stations and list
        self.metadata = pandas.concat([coordinates, properties, \
            latency], axis = 1)
        self.stations = self.metadata.index.to_list()

    def get_gauges_data(self, station_id, start, end, max_records = 5000):
        """
        Get data from station_id from start to end

        Parameters
        ----------
        station_id: string
            ID of the IDSL tide gauge station
        start: datetime.datetime
            start datetime
        end: datetime.datetime
            end datetime
        max_records: int
            maximum number of records
        Returns
        -------
        data: pandas.DataFrame
            station_id data queried from JSON API converted to DataFrame
        """
        # Get data from JSON data API
        url = BASE_URL + DATA_API.format(station_id, \
            start.date().isoformat(), start.time().isoformat()[:8], \
            end.date().isoformat(), end.time().isoformat()[:8], \
            max_records)
        req = requests.get(url)
        assert(req.status_code == 200)

        summary = json.loads(req.text)
        if len(summary) > 0:
            self.data = pandas.DataFrame(summary)
            self._reformat_dataframe()
            return self.data.copy()
        else:
            return None

    def _reformat_dataframe(self):
        """
        Reformat and rename the DataFrame columns
        """
        self.data.Timestamp = self.data.Timestamp.astype('datetime64[ms]')
        self.data.set_index('Timestamp', inplace = True, drop = True)

        df = self.data.Values.apply(pandas.Series).copy()
        df.columns = ['WaterLevelRadar', 'SolarPanel', 'RmsLimit', \
            'CPUTemperature', 'AmbientTemperature', 'Alert', \
            'AlertSignal', 'Battery', 'Forecast30', 'Forecast300']
        self.data = df.copy()
