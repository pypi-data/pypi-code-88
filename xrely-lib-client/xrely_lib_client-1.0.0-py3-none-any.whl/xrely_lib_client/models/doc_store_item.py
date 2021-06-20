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


class DocStoreItem(object):
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
        'keyword': 'str',
        'url': 'str',
        'data': 'MapObject'
    }

    attribute_map = {
        'keyword': 'keyword',
        'url': 'url',
        'data': 'data'
    }

    def __init__(self, keyword=None, url=None, data=None):  # noqa: E501
        """DocStoreItem - a model defined """  # noqa: E501

        self._keyword = None
        self._url = None
        self._data = None
        self.discriminator = None

        if keyword is not None:
            self.keyword = keyword
        if url is not None:
            self.url = url
        if data is not None:
            self.data = data

    @property
    def keyword(self):
        """Gets the keyword of this DocStoreItem.  # noqa: E501

        keyword or phrase  # noqa: E501

        :return: The keyword of this DocStoreItem.  # noqa: E501
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        """Sets the keyword of this DocStoreItem.

        keyword or phrase  # noqa: E501

        :param keyword: The keyword of this DocStoreItem.  # noqa: E501
        :type: str
        """

        self._keyword = keyword

    @property
    def url(self):
        """Gets the url of this DocStoreItem.  # noqa: E501

        Related url with the keyword  # noqa: E501

        :return: The url of this DocStoreItem.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this DocStoreItem.

        Related url with the keyword  # noqa: E501

        :param url: The url of this DocStoreItem.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def data(self):
        """Gets the data of this DocStoreItem.  # noqa: E501


        :return: The data of this DocStoreItem.  # noqa: E501
        :rtype: MapObject
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this DocStoreItem.


        :param data: The data of this DocStoreItem.  # noqa: E501
        :type: MapObject
        """

        self._data = data

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
        if issubclass(DocStoreItem, dict):
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
        if not isinstance(other, DocStoreItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
