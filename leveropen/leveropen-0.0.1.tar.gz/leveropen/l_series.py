from typing import List
import pandas as pd

import leveropen.client
from leveropen.utils import parse_categories


class LSeries:
    """
    Represents a Lever Open data series

    :param uuid: unique id
    :type uuid: str
    :param name: series name
    :type name: str
    :param units: Unit type
    :type units: str
    :param magnitude:
    :type magnitude: str
    :param link: URL of series
    :type link: str
    :param date_time: e.g. ``{'name': 'Month', 'range': ['January 1997', 'December 2020']}``
    :type date_time: dict
    :param location: e.g. ``{'type': 'Country', 'name': 'UK'}``
    :type location: dict
    :param categories:
        e.g. ``[{'type': 'Adjustment', 'name': 'Seasonally adjusted'}, {'type': 'Total', 'name': 'Monthly GDP'}]``
    :type categories: List[dict]
    :param client: API Client
    :type client: leveropen.client.Client
    """

    def __init__(
        self,
        uuid: str,
        name: str,
        units: str,
        magnitude: str,
        link: str,
        date_time: dict,
        location: dict,
        categories: List[dict],
        client: leveropen.client.Client,
    ):
        self.uuid = uuid
        self.name = name
        self.units = units
        self.magnitude = magnitude
        self.link = link
        self.date_time = date_time
        self.location = location
        self.categories = categories
        self.client = client

    def __repr__(self):
        return f"""
            {self.__class__.__name__}(
                uuid={repr(self.uuid)},
                name={repr(self.name)},
                units={repr(self.units)},
                magnitude={repr(self.magnitude)},
                link={repr(self.link)},
                date_time={repr(self.date_time)},
                location={repr(self.location)},
                categories={repr(self.categories)}
            )"""

    def __eq__(self, other):
        criteria = (
            (isinstance(other, LSeries))
            and (self.uuid == other.uuid)
            and (self.name == other.name)
            and (self.units == other.units)
            and (self.magnitude == other.magnitude)
            and (self.link == other.link)
            and (self.date_time == other.date_time)
            and (self.location == other.location)
            and (self.categories == other.categories)
        )
        return criteria

    def get_categories(self) -> pd.DataFrame:
        """

        :return: Type and Categories
        :rtype: pandas.DataFrame

        :example:

        .. code-block:: python

           >>> self.get_categories()

                    type                 name
           0  Adjustment  Seasonally adjusted
           1       Total          Monthly GDP

        """
        return parse_categories(categories=self.categories)

    def get_data(self) -> pd.DataFrame:
        """

        :return:
          Values of the Series data
            Columns: ``['Value', 'DateTime', 'DateFrom', 'DateTo', 'SeriesName', 'Country']``

            Index: ``pd.DatetimeIndex``
        :rtype: pandas.DataFrame

        :example:

        .. code-block:: python

           >>> self.get_data()
                       Value    ... Country
           1997-01-01  6.7701   ...      UK
           1997-02-01  8.9410   ...      UK
           1997-03-01  1.9841   ...      UK
           1997-04-01  5.6258   ...      UK
           1997-05-01  10.2138  ...      UK

        """
        url = self.link.replace(self.client.host_url, "")
        resp = self.client.get(url_ext=url, verbose=False)
        data = resp.json()["data"]["series"]["data"]
        df_list = []
        for row in data:
            date_from_and_to = pd.to_datetime(
                row["timestamps"], unit="s"
            )  # List[date_from, date_to]
            df_list.append(
                pd.DataFrame(
                    data={
                        "Value": float(row["value"]),
                        "DateTime": row["datetime"],
                        "DateFrom": date_from_and_to[0],
                        "DateTo": date_from_and_to[1],
                        "SeriesName": self.name,
                        self.location["type"]: self.location["name"],
                    },
                    index=pd.DatetimeIndex([date_from_and_to[0]]),
                )
            )
        return pd.concat(df_list, axis=0).sort_index()
