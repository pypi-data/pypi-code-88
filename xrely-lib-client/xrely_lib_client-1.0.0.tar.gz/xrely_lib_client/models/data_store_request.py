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


class DataStoreRequest(object):
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
        'secret_key': 'str',
        'docs': 'list[DocStoreItem]'
    }

    attribute_map = {
        'secret_key': 'secretKey',
        'docs': 'docs'
    }

    def __init__(self, secret_key=None, docs=None):  # noqa: E501
        """DataStoreRequest - a model defined """  # noqa: E501

        self._secret_key = None
        self._docs = None
        self.discriminator = None

        if secret_key is not None:
            self.secret_key = secret_key
        if docs is not None:
            self.docs = docs

    @property
    def secret_key(self):
        """Gets the secret_key of this DataStoreRequest.  # noqa: E501

        private key of the account  # noqa: E501

        :return: The secret_key of this DataStoreRequest.  # noqa: E501
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this DataStoreRequest.

        private key of the account  # noqa: E501

        :param secret_key: The secret_key of this DataStoreRequest.  # noqa: E501
        :type: str
        """

        self._secret_key = secret_key

    @property
    def docs(self):
        """Gets the docs of this DataStoreRequest.  # noqa: E501


        :return: The docs of this DataStoreRequest.  # noqa: E501
        :rtype: list[DocStoreItem]
        """
        return self._docs

    @docs.setter
    def docs(self, docs):
        """Sets the docs of this DataStoreRequest.


        :param docs: The docs of this DataStoreRequest.  # noqa: E501
        :type: list[DocStoreItem]
        """

        self._docs = docs

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
        if issubclass(DataStoreRequest, dict):
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
        if not isinstance(other, DataStoreRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
