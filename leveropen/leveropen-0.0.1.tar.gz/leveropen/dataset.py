from typing import List
import datetime as dt

import pandas as pd
from tqdm import tqdm
from halo import Halo

import leveropen.client
from leveropen.l_series import LSeries
from leveropen.utils import parse_categories


class Dataset:
    """
    Represents a Lever Open dataset

    :param uuid: Unique ID of the dataset
    :type uuid: str
    :param name: Name of the dataset
    :type name: str
    :param released_on: Most recent released date of the data
    :type released_on: datetime.datetime
    :param processed_on: Most recent date that Lever Open processed the data
    :type processed_on: datetime.datetime
    :param collection: Collection to which the dataset belongs
    :type collection: str
    :param topic: Topic to which the dataset belongs
    :type topic: str
    :param link: URL
    :type link: str
    :param license: {'name': 'License name', 'url': 'link-to-license'}
    :type license: dict
    :param datetimes: e.g. ``[{'name': 'Month', 'range': ['January 1997', 'December 2020']}, ...]``
    :type datetimes: List[dict]
    :param locations: e.g. ``[{'type': 'Country', 'name', 'UK'}, ...]``
    :type locations: List[dict]
    :param categories: e.g. ``[{'type': 'Sector', 'name': 'Construction'}, ...]``
    :type categories: List[dict]
    :param series_url: URL link to series data
    :type series_url: str
    :param client: Lever Open API Client
    :type client: :func:`leveropen.client.Client`

    """

    def __init__(
        self,
        uuid: str,
        name: str,
        released_on: dt.datetime,
        processed_on: dt.datetime,
        collection: str,
        topic: str,
        link: str,
        license: dict,
        datetimes: List[dict],
        locations: List[dict],
        categories: List[dict],
        series_url: str,
        client: leveropen.client.Client,
    ):
        self.uuid = uuid
        self.name = name
        self.released_on = released_on
        self.processed_on = processed_on
        self.collection = collection
        self.topic = topic
        self.link = link
        self.license = license
        self.datetimes = datetimes
        self.locations = locations
        self.categories = categories
        self.series_url = series_url
        self.series = None
        self.series_objects = None
        self.client = client

    def __repr__(self):
        return f"""
            {self.__class__.__name__}(
                uuid={repr(self.uuid)},
                name={repr(self.name)},
                released_on={repr(self.released_on)},
                processed_on={repr(self.processed_on)},
                collection={repr(self.collection)},
                topic={repr(self.topic)},
                link={repr(self.link)},
                license={repr(self.license)},
                datetimes={repr(self.datetimes)},
                locations={repr(self.locations)},
                categories={repr(self.categories)},
                series_url={repr(self.series_url)}
            )"""

    def __eq__(self, other):
        criteria = (
            (isinstance(other, Dataset))
            and (self.uuid == other.uuid)
            and (self.name == other.name)
            and (self.released_on == other.released_on)
            and (self.processed_on == other.processed_on)
            and (self.collection == other.collection)
            and (self.topic == other.topic)
            and (self.link == other.link)
            and (self.license == other.license)
            and (self.datetimes == other.datetimes)
            and (self.locations == other.locations)
            and (self.categories == other.categories)
            and (self.series_url == other.series_url)
        )
        return criteria

    def get_metadata(self) -> pd.Series:
        """

        :return: Key information about the dataset
        :rtype: pandas.Series

        :example:

        .. code-block:: python

           >>> metadata = self.get_metadata()
           >>> metadata.head()
           name                                              Example Dataset
           topic                                                     Economy
           collection                           Gross Domestic Product (GDP)
           released_on                                   2021-02-12 00:00:00
           processed_on                                  2021-03-05 00:00:00
           Name: example-dataset-uuid, dtype: object

        """
        return pd.Series(
            data={
                "name": self.name,
                "topic": self.topic,
                "collection": self.collection,
                "released_on": self.released_on,
                "processed_on": self.processed_on,
                "link": self.link,
                "license_name": self.license["name"],
                "license_url": self.license["url"],
                "series_names_and_uuids": self.get_series_names_and_uuids(),
                "categories": self.get_categories(),
            },
            name=self.uuid,
        )

    def get_categories(self) -> pd.DataFrame:
        """

        :return: Type and Categories
        :rtype: pandas.DataFrame

        :example:

        .. code-block:: python

           >>> self.get_categories()
                    type                 name
           0      Sector         Construction
           1      Sector             Services
           2  Adjustment  Seasonally adjusted
           3      Sector           Production
           4       Total          Monthly GDP
           5      Sector          Agriculture

        """
        return parse_categories(categories=self.categories)

    def get_series(self, load: bool = True) -> List[LSeries]:
        """

        :param load: if ``'True'`` then self.series_objects is set
        :return: all series names on the dataset
        :rtype: List[LSeries]

        :example:

        .. code-block:: python

           >>> self.get_series()
           [
                LSeries(
                    uuid='uuid-of-series-one',
                    name='Series-Name-One',
                    units='Count',
                    magnitude=1,
                    ...
                ),
                LSeries(
                    uuid='uuid-of-series-two',
                    name='Series-Name-Two',
                    units='Count',
                    magnitude=1,
                    ...
                )
           ]

        """
        series = self.series or self._get_series_by_url()
        parsed_series = self._parse_series(series)
        if load:
            self.series_objects = parsed_series
        return parsed_series

    def get_series_names_and_uuids(self) -> pd.DataFrame:
        """

        :return: all series name and their uuid
        :rtype: pandas.DataFrame

        :example:

        .. code-block:: python

           >>> self.get_series_names_and_uuids()
                          name                uuid
           0   Series-Name-One  uuid-of-series-one
           1   Series-Name-Two  uuid-of-series-Two
           2               ...                 ...
           n     Series-Name-N    uuid-of-series-N

        """
        series = self.series_objects or self.get_series()
        return pd.DataFrame(
            data={
                "name": [s.name for s in series],
                "uuid": [s.uuid for s in series],
            }
        )

    def get_series_by_name(self, name: str) -> LSeries:
        """

        :param name: the name of the series :attr:`leveropen.l_series.LSeries.name`
        :return: LSeries

        :example:

        .. code-block:: python

           >>> self.get_series_by_name(name='Series-Name-One')
           LSeries(
               uuid='uuid-of-series-one',
               name='Series-Name-One',
               units='Count',
               magnitude=1,
               ...
           )

        """
        series = [s for s in self.get_series() if s.name == name]
        if not series:
            raise ValueError(
                f"The dataset '{self.name}' has no series matching the name '{name}'"
            )
        if len(series) == 1:
            return series[0]
        else:
            raise ValueError(
                f"More than one series has the name '{name}'. "
                f"Try using the method get_series_by_name_containing"
            )

    def get_series_by_uuid(self, uuid: str) -> LSeries:
        """

        :param uuid: the uuid of the series :attr:`leveropen.l_series.LSeries.uuid`
        :return: LSeries

        :example:

        .. code-block:: python

           >>> self.get_series_by_uuid(uuid='uuid-of-series-one')
           LSeries(
               uuid='uuid-of-series-one',
               name='Series-Name-One',
               units='Count',
               magnitude=1,
               ...
           )

        """
        series = [s for s in self.get_series() if s.uuid == uuid]
        if not series:
            raise ValueError(
                f"The dataset '{self.uuid}' has no series matching the name '{uuid}'"
            )
        if len(series) == 1:
            return series[0]
        else:
            raise ValueError(f"More than one series has the uuid '{uuid}'")

    def get_series_by_name_containing(
        self, name_containing_string: str
    ) -> List[LSeries]:
        """

        :param name_containing_string: substring for which to find in series names
        :type name_containing_string: str
        :return: list of Lever Open Series
        :rtype: List[LSeries]

        :example:

        .. code-block:: python

           >>> self.get_series_by_name_containing(
           ...     name_containing_string='Series-Name'
           ... )
           [
                LSeries(
                    uuid='uuid-of-series-one',
                    name='Series-Name-One',
                    units='Count',
                    magnitude=1,
                    ...
                ),
                LSeries(
                    uuid='uuid-of-series-two',
                    name='Series-Name-Two',
                    units='Count',
                    magnitude=1,
                    ...
                )
           ]

        """
        series = [
            s for s in self.get_series() if s.name.find(name_containing_string) != -1
        ]
        if not series:
            raise ValueError(
                f"The dataset {self.name} has no series names containing '{name_containing_string}'"
            )
        return series

    def _get_series_by_url(self, load=True):
        spinner = Halo(spinner="dots")
        spinner.start(f"Requesting series data")
        url = self.series_url
        url = url.replace(self.client.host_url, "")
        resp = self.client.get(url, verbose=False).json()["data"]["series"]
        spinner.succeed("Loading series data successful")
        if load:
            self.series = resp
        return resp

    def _parse_series(self, series: list):
        series_objects = []
        for s in tqdm(series, desc="Parsing series", unit="series"):
            series_objects.append(
                LSeries(
                    uuid=s.get("uuid"),
                    name=s.get("name"),
                    units=s.get("units"),
                    magnitude=s.get("magnitude"),
                    link=s.get("link"),
                    date_time=s.get("datetime"),
                    location=s.get("location"),
                    categories=s.get("categories"),
                    client=self.client,
                )
            )
        return series_objects
