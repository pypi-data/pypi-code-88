# coding: utf-8

"""
    XRELY

    API Documentation for XRELY platform  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: contact@xrely.com
    
"""


import pprint
import re  # noqa: F401

import six


class SearchRequest(object):
    """
    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'ak': 'str',
        'q': 'str',
        'size': 'str',
        'agg_field': 'list[AggrigationField]',
        'filter_field': 'list[FilterField]'
    }

    attribute_map = {
        'ak': 'ak',
        'q': 'q',
        'size': 'size',
        'agg_field': 'aggField',
        'filter_field': 'filterField'
    }

    def __init__(self, ak=None, q=None, size=None, agg_field=None, filter_field=None):  # noqa: E501
        """SearchRequest - a model defined """  # noqa: E501

        self._ak = None
        self._q = None
        self._size = None
        self._agg_field = None
        self._filter_field = None
        self.discriminator = None

        if ak is not None:
            self.ak = ak
        if q is not None:
            self.q = q
        if size is not None:
            self.size = size
        if agg_field is not None:
            self.agg_field = agg_field
        if filter_field is not None:
            self.filter_field = filter_field

    @property
    def ak(self):
        """Gets the ak of this SearchRequest.  # noqa: E501

        Account Key  # noqa: E501

        :return: The ak of this SearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._ak

    @ak.setter
    def ak(self, ak):
        """Sets the ak of this SearchRequest.

        Account Key  # noqa: E501

        :param ak: The ak of this SearchRequest.  # noqa: E501
        :type: str
        """

        self._ak = ak

    @property
    def q(self):
        """Gets the q of this SearchRequest.  # noqa: E501

        Query Term  # noqa: E501

        :return: The q of this SearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._q

    @q.setter
    def q(self, q):
        """Sets the q of this SearchRequest.

        Query Term  # noqa: E501

        :param q: The q of this SearchRequest.  # noqa: E501
        :type: str
        """

        self._q = q

    @property
    def size(self):
        """Gets the size of this SearchRequest.  # noqa: E501

        Number of results  # noqa: E501

        :return: The size of this SearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this SearchRequest.

        Number of results  # noqa: E501

        :param size: The size of this SearchRequest.  # noqa: E501
        :type: str
        """

        self._size = size

    @property
    def agg_field(self):
        """Gets the agg_field of this SearchRequest.  # noqa: E501


        :return: The agg_field of this SearchRequest.  # noqa: E501
        :rtype: list[AggrigationField]
        """
        return self._agg_field

    @agg_field.setter
    def agg_field(self, agg_field):
        """Sets the agg_field of this SearchRequest.


        :param agg_field: The agg_field of this SearchRequest.  # noqa: E501
        :type: list[AggrigationField]
        """

        self._agg_field = agg_field

    @property
    def filter_field(self):
        """Gets the filter_field of this SearchRequest.  # noqa: E501


        :return: The filter_field of this SearchRequest.  # noqa: E501
        :rtype: list[FilterField]
        """
        return self._filter_field

    @filter_field.setter
    def filter_field(self, filter_field):
        """Sets the filter_field of this SearchRequest.


        :param filter_field: The filter_field of this SearchRequest.  # noqa: E501
        :type: list[FilterField]
        """

        self._filter_field = filter_field

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SearchRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SearchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
