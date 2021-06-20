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


class ReplaceStringRegexRequest(object):
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
        'text_content': 'str',
        'regular_expression_string': 'str',
        'replace_with_string': 'str'
    }

    attribute_map = {
        'text_content': 'TextContent',
        'regular_expression_string': 'RegularExpressionString',
        'replace_with_string': 'ReplaceWithString'
    }

    def __init__(self, text_content=None, regular_expression_string=None, replace_with_string=None):  # noqa: E501
        """ReplaceStringRegexRequest - a model defined in Swagger"""  # noqa: E501

        self._text_content = None
        self._regular_expression_string = None
        self._replace_with_string = None
        self.discriminator = None

        if text_content is not None:
            self.text_content = text_content
        if regular_expression_string is not None:
            self.regular_expression_string = regular_expression_string
        if replace_with_string is not None:
            self.replace_with_string = replace_with_string

    @property
    def text_content(self):
        """Gets the text_content of this ReplaceStringRegexRequest.  # noqa: E501

        Input text content  # noqa: E501

        :return: The text_content of this ReplaceStringRegexRequest.  # noqa: E501
        :rtype: str
        """
        return self._text_content

    @text_content.setter
    def text_content(self, text_content):
        """Sets the text_content of this ReplaceStringRegexRequest.

        Input text content  # noqa: E501

        :param text_content: The text_content of this ReplaceStringRegexRequest.  # noqa: E501
        :type: str
        """

        self._text_content = text_content

    @property
    def regular_expression_string(self):
        """Gets the regular_expression_string of this ReplaceStringRegexRequest.  # noqa: E501

        Target input regular expression (regex) string to match and be replaced; supports all regular expression values  # noqa: E501

        :return: The regular_expression_string of this ReplaceStringRegexRequest.  # noqa: E501
        :rtype: str
        """
        return self._regular_expression_string

    @regular_expression_string.setter
    def regular_expression_string(self, regular_expression_string):
        """Sets the regular_expression_string of this ReplaceStringRegexRequest.

        Target input regular expression (regex) string to match and be replaced; supports all regular expression values  # noqa: E501

        :param regular_expression_string: The regular_expression_string of this ReplaceStringRegexRequest.  # noqa: E501
        :type: str
        """

        self._regular_expression_string = regular_expression_string

    @property
    def replace_with_string(self):
        """Gets the replace_with_string of this ReplaceStringRegexRequest.  # noqa: E501

        Replacement for target string; supports referencing indexed regex matched values from RegularExpressionString, such as $1, $2, and so on  # noqa: E501

        :return: The replace_with_string of this ReplaceStringRegexRequest.  # noqa: E501
        :rtype: str
        """
        return self._replace_with_string

    @replace_with_string.setter
    def replace_with_string(self, replace_with_string):
        """Sets the replace_with_string of this ReplaceStringRegexRequest.

        Replacement for target string; supports referencing indexed regex matched values from RegularExpressionString, such as $1, $2, and so on  # noqa: E501

        :param replace_with_string: The replace_with_string of this ReplaceStringRegexRequest.  # noqa: E501
        :type: str
        """

        self._replace_with_string = replace_with_string

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
        if issubclass(ReplaceStringRegexRequest, dict):
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
        if not isinstance(other, ReplaceStringRegexRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
