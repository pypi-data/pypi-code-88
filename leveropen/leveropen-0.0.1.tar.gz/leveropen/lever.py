import os
from typing import List, Union
import datetime as dt

from tqdm import tqdm
from halo import Halo

from leveropen.client import Client
from leveropen.dataset import Dataset
from leveropen.utils import BASE_URL, VERSION, DATE_FORMAT, DATASET_FILTER_TYPES

ACCESS_TOKEN = os.environ.get("TOKEN")


class Lever:
    """

    :param access_token: Personal Access Token for Lever Open
    :type access_token: str
    :param base_url: host url for Lever Open API e.g. ``'https://www.leveropen.com/api/'``
    :type base_url: str
    :param version: Lever Open API version e.g. ``'v1'``
    :type version: str

    :ivar client: (:func:`leveropen.client.Client`) Lever Open API Client

    :example:

    .. code-block:: python

       from leveropen import Lever

       access_token = 'your-unique-personal-access-token'
       lever = Lever(access_token)

    """

    def __init__(
        self,
        access_token: str = ACCESS_TOKEN,
        base_url: str = BASE_URL,
        version: str = VERSION,
    ):
        self.client = Client(
            access_token=access_token, base_url=base_url, version=version
        )

    def get_all_datasets(self) -> List[Dataset]:
        """
        All Lever Open datasets

        .. note::
            This method **takes a long time to complete**, therefore it
            is recommended to use one of the specific methods to get a
            specific dataset (or datasets specific to a Topic/Collection):

            - :func:`leveropen.lever.Lever.get_datasets_by_topic`
            - :func:`leveropen.lever.Lever.get_datasets_by_collection`
            - :func:`leveropen.lever.Lever.get_datasets_by_name`

        :return: list of all Lever Open datasets
        :rtype: List[Dataset]

        :example:

        .. code-block:: python

           >>> self.get_all_datasets()
           [
               Dataset(
                   uuid='example-uuid-1',
                   name='Example dataset 1',
                   released_on=datetime.datetime(2021, 2, 11, 0, 0),
                   processed_on=datetime.datetime(2021, 3, 3, 0, 0),
                   collection='Example Collection',
                   ...
               ),
               Dataset(
                   uuid='example-uuid-2',
                   name='Example dataset 2',
                   released_on=datetime.datetime(2021, 2, 11, 0, 0),
                   processed_on=datetime.datetime(2021, 3, 3, 0, 0),
                   collection='Example Collection',
                   ...
               ),
               ...
           ]

        """
        next_page = True
        page = 1
        datasets_list = []
        spinner = Halo(spinner="dots")
        while next_page:
            spinner.start(f"Requesting datasets: page={page}")
            content = self.client.get_datasets_by_page(page=page)
            next_link = content["links"]["next"]
            datasets = content.get("data").get("datasets")
            datasets_parsed = self._parse_datasets(datasets=datasets)
            datasets_list = datasets_list + datasets_parsed
            if not next_link:
                next_page = False
            page += 1
        if not datasets_list:
            spinner.fail("Loading datasets failed")
            raise ValueError(f"Dataset not found with page '{page}'")
        else:
            spinner.succeed("Loading datasets successful")
            return datasets_list

    def get_datasets_by_collection(self, collection: str) -> List[Dataset]:
        """

        :return: list of datasets
        :rtype: List[Dataset]

        :example:

        .. code-block:: python

           >>> self.get_datasets_by_collection(collection='Example Collection')
           [Dataset(
               uuid='example-uuid',
               name='Example dataset',
               released_on=datetime.datetime(2021, 2, 11, 0, 0),
               processed_on=datetime.datetime(2021, 3, 3, 0, 0),
               collection='Example Collection',
               ...
           )]

        """
        return self._get_datasets_by(by="collection", query=collection)

    def get_datasets_by_topic(self, topic: str) -> List[Dataset]:
        """

        :return: list of datasets
        :rtype: List[Dataset]

        :example:

        .. code-block:: python

           >>> self.get_datasets_by_topic(topic='Example Topic')
           [Dataset(
               uuid='example-uuid',
               name='Example dataset',
               released_on=datetime.datetime(2021, 2, 11, 0, 0),
               processed_on=datetime.datetime(2021, 3, 3, 0, 0),
               collection='Example Collection',
               topic='Example Topic',
               ...
           )]

        """
        return self._get_datasets_by(by="topic", query=topic)

    def get_datasets_by_name(self, name: str) -> List[Dataset]:
        """

        :return: list of datasets
        :rtype: List[Dataset]

        :example:

        .. code-block:: python

           >>> self.get_datasets_by_name(name='Example dataset')
           [Dataset(
               uuid='example-uuid',
               name='Example dataset',
               released_on=datetime.datetime(2021, 2, 11, 0, 0),
               processed_on=datetime.datetime(2021, 3, 3, 0, 0),
               collection='Example Collection',
               ...
           )]

        """
        return self._get_datasets_by(by="name", query=name)

    def _get_datasets_by(self, by: str, query: Union[str, int]) -> List[Dataset]:
        """

        :param by: how to search the dataset, either ``'name'``, ``'collection'``, ``'topic'``
        :type by: str
        :param query: String to search, e.g. dataset name
        :type query: str or int
        :return: Lever Open dataset
        :rtype: List[Dataset]

        :example:

        .. code-block:: python

           >>> self._get_datasets_by(by='name', query='Example dataset')
           [Dataset(
               uuid='example-uuid',
               name='Example dataset',
               released_on=datetime.datetime(2021, 2, 11, 0, 0),
               processed_on=datetime.datetime(2021, 3, 3, 0, 0),
               collection='Example Collection',
               ...
           )]

        """
        by = by.lower()
        assert (
            by in DATASET_FILTER_TYPES
        ), f"'by' input must be one of {DATASET_FILTER_TYPES}"
        next_page = True
        datasets = []
        page = 1
        spinner = Halo(spinner="dots")
        while next_page:
            spinner.start(f"Requesting datasets: query='{query}' and page={page}")
            if by == "name":
                content = self.client.get_datasets_by_name(name=query, page=page)
            elif by == "collection":
                content = self.client.get_datasets_by_collection(
                    collection=query, page=page
                )
            elif by == "topic":
                content = self.client.get_datasets_by_topic(topic=query, page=page)
            else:
                raise ValueError(f"'by' input must be one of {DATASET_FILTER_TYPES}")
            next_link = content["links"]["next"]
            datasets_resp = content.get("data").get("datasets")
            datasets = datasets + self._parse_datasets(datasets=datasets_resp)
            if not next_link:
                next_page = False
            else:
                page += 1
                print(f"Processing next page: {page}")
        if not datasets:
            spinner.fail("Loading datasets failed")
            raise ValueError(f"Dataset not found with query '{query}'")
        else:
            spinner.succeed("Loading datasets successful")
            return datasets

    def _parse_datasets(self, datasets: list) -> List[Dataset]:
        dataset_objects = []
        for ds in tqdm(datasets, desc="Parsing datasets", unit="datasets"):
            dataset_objects.append(
                Dataset(
                    uuid=ds.get("uuid"),
                    name=ds.get("name"),
                    released_on=dt.datetime.strptime(
                        ds.get("released_on"), DATE_FORMAT
                    ),
                    processed_on=dt.datetime.strptime(
                        ds.get("processed_on"), DATE_FORMAT
                    ),
                    collection=ds.get("collection"),
                    topic=ds.get("topic"),
                    link=ds.get("link"),
                    license=ds.get("license"),
                    datetimes=ds.get("datetimes"),
                    locations=ds.get("locations"),
                    categories=ds.get("categories"),
                    series_url=ds.get("series"),
                    client=self.client,
                )
            )
        return dataset_objects
