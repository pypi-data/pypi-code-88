# coding: utf-8

"""
    convertapi

    Convert API lets you effortlessly convert file formats and types.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class HtmlSsrfThreatCheckResult(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'is_valid': 'bool',
        'is_threat': 'bool',
        'threat_links': 'list[HtmlThreatLink]'
    }

    attribute_map = {
        'is_valid': 'IsValid',
        'is_threat': 'IsThreat',
        'threat_links': 'ThreatLinks'
    }

    def __init__(self, is_valid=None, is_threat=None, threat_links=None):  # noqa: E501
        """HtmlSsrfThreatCheckResult - a model defined in Swagger"""  # noqa: E501

        self._is_valid = None
        self._is_threat = None
        self._threat_links = None
        self.discriminator = None

        if is_valid is not None:
            self.is_valid = is_valid
        if is_threat is not None:
            self.is_threat = is_threat
        if threat_links is not None:
            self.threat_links = threat_links

    @property
    def is_valid(self):
        """Gets the is_valid of this HtmlSsrfThreatCheckResult.  # noqa: E501

        True if the document is valid and has no errors, false otherwise  # noqa: E501

        :return: The is_valid of this HtmlSsrfThreatCheckResult.  # noqa: E501
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """Sets the is_valid of this HtmlSsrfThreatCheckResult.

        True if the document is valid and has no errors, false otherwise  # noqa: E501

        :param is_valid: The is_valid of this HtmlSsrfThreatCheckResult.  # noqa: E501
        :type: bool
        """

        self._is_valid = is_valid

    @property
    def is_threat(self):
        """Gets the is_threat of this HtmlSsrfThreatCheckResult.  # noqa: E501

        True if the document contains an SSRF threat, false otherwise  # noqa: E501

        :return: The is_threat of this HtmlSsrfThreatCheckResult.  # noqa: E501
        :rtype: bool
        """
        return self._is_threat

    @is_threat.setter
    def is_threat(self, is_threat):
        """Sets the is_threat of this HtmlSsrfThreatCheckResult.

        True if the document contains an SSRF threat, false otherwise  # noqa: E501

        :param is_threat: The is_threat of this HtmlSsrfThreatCheckResult.  # noqa: E501
        :type: bool
        """

        self._is_threat = is_threat

    @property
    def threat_links(self):
        """Gets the threat_links of this HtmlSsrfThreatCheckResult.  # noqa: E501

        Links found in the input HTML that contains threats  # noqa: E501

        :return: The threat_links of this HtmlSsrfThreatCheckResult.  # noqa: E501
        :rtype: list[HtmlThreatLink]
        """
        return self._threat_links

    @threat_links.setter
    def threat_links(self, threat_links):
        """Sets the threat_links of this HtmlSsrfThreatCheckResult.

        Links found in the input HTML that contains threats  # noqa: E501

        :param threat_links: The threat_links of this HtmlSsrfThreatCheckResult.  # noqa: E501
        :type: list[HtmlThreatLink]
        """

        self._threat_links = threat_links

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
        if issubclass(HtmlSsrfThreatCheckResult, dict):
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
        if not isinstance(other, HtmlSsrfThreatCheckResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
