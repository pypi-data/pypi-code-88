from leveropen.protocol import Protocol


class Client(Protocol):
    """
    Extends :func:`leveropen.protocol.Protocol`

    .. seealso:: `Lever Open Topics <https://www.leveropen.com/topics>`_

    """

    def get_datasets_by_page(self, page: int = 1, verbose: bool = False) -> dict:
        """
        Gets all datasets available from the Lever Open API

        :param page: Lever Open API page number, default ``0``
        :type page: int
        :param verbose: if ``True`` then print statements
        :type verbose: bool
        :return: json from API response
        :rtype: dict
        """
        resp = self.get(url_ext="datasets", params={"page": page}, verbose=verbose)
        return resp.json()

    def get_datasets_by_topic(
        self, topic: str, page: int, verbose: bool = False
    ) -> dict:
        """
        Gets all datasets available from the Lever Open API

        :param topic: Lever Open topic name
        :type topic: str
        :param page: Lever Open API page
        :type page: str
        :param verbose: if ``True`` then print statements
        :type verbose: bool
        :return: json from API response
        :rtype: dict

        """
        resp = self.get(
            url_ext="datasets", params={"query": topic, "page": page}, verbose=verbose
        )
        return resp.json()

    def get_datasets_by_collection(
        self, collection: str, page: int, verbose: bool = False
    ) -> dict:
        """
        Gets all datasets available from the Lever Open API

        :param collection: Lever Open collection name
        :type collection: str
        :param page: Lever Open API page
        :type page: str
        :param verbose: if ``True`` then print statements
        :type verbose: bool
        :return: json from API response
        :rtype: dict
        """
        resp = self.get(
            url_ext="datasets",
            params={"query": collection, "page": page},
            verbose=verbose,
        )
        return resp.json()

    def get_datasets_by_name(self, name: str, page: int, verbose: bool = False) -> dict:
        """
        Gets all datasets available from the Lever Open API

        :param name: Lever Open dataset name
        :type name: str
        :param page: Lever Open API page
        :type page: str
        :param verbose: if ``True`` then print statements
        :type verbose: bool
        :return: json from API response
        :rtype: dict
        """
        resp = self.get(
            url_ext="datasets", params={"query": name, "page": page}, verbose=verbose
        )
        return resp.json()
