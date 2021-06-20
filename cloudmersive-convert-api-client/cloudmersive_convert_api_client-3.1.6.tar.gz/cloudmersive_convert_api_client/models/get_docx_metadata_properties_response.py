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


class GetDocxMetadataPropertiesResponse(object):
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
        'company': 'str',
        'manager': 'str',
        'application_version': 'str',
        'word_count': 'int',
        'line_count': 'int',
        'paragraph_count': 'int',
        'page_count': 'int',
        'custom_properties': 'list[DocxMetadataCustomProperty]',
        'successful': 'bool'
    }

    attribute_map = {
        'company': 'Company',
        'manager': 'Manager',
        'application_version': 'ApplicationVersion',
        'word_count': 'WordCount',
        'line_count': 'LineCount',
        'paragraph_count': 'ParagraphCount',
        'page_count': 'PageCount',
        'custom_properties': 'CustomProperties',
        'successful': 'Successful'
    }

    def __init__(self, company=None, manager=None, application_version=None, word_count=None, line_count=None, paragraph_count=None, page_count=None, custom_properties=None, successful=None):  # noqa: E501
        """GetDocxMetadataPropertiesResponse - a model defined in Swagger"""  # noqa: E501

        self._company = None
        self._manager = None
        self._application_version = None
        self._word_count = None
        self._line_count = None
        self._paragraph_count = None
        self._page_count = None
        self._custom_properties = None
        self._successful = None
        self.discriminator = None

        if company is not None:
            self.company = company
        if manager is not None:
            self.manager = manager
        if application_version is not None:
            self.application_version = application_version
        if word_count is not None:
            self.word_count = word_count
        if line_count is not None:
            self.line_count = line_count
        if paragraph_count is not None:
            self.paragraph_count = paragraph_count
        if page_count is not None:
            self.page_count = page_count
        if custom_properties is not None:
            self.custom_properties = custom_properties
        if successful is not None:
            self.successful = successful

    @property
    def company(self):
        """Gets the company of this GetDocxMetadataPropertiesResponse.  # noqa: E501

        Name of the Company that authored the document, if available  # noqa: E501

        :return: The company of this GetDocxMetadataPropertiesResponse.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this GetDocxMetadataPropertiesResponse.

        Name of the Company that authored the document, if available  # noqa: E501

        :param company: The company of this GetDocxMetadataPropertiesResponse.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def manager(self):
        """Gets the manager of this GetDocxMetadataPropertiesResponse.  # noqa: E501

        Name of the Manager that authored the document, if available  # noqa: E501

        :return: The manager of this GetDocxMetadataPropertiesResponse.  # noqa: E501
        :rtype: str
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        """Sets the manager of this GetDocxMetadataPropertiesResponse.

        Name of the Manager that authored the document, if available  # noqa: E501

        :param manager: The manager of this GetDocxMetadataPropertiesResponse.  # noqa: E501
        :type: str
        """

        self._manager = manager

    @property
    def application_version(self):
        """Gets the application_version of this GetDocxMetadataPropertiesResponse.  # noqa: E501

        Application version that authored the document, if available  # noqa: E501

        :return: The application_version of this GetDocxMetadataPropertiesResponse.  # noqa: E501
        :rtype: str
        """
        return self._application_version

    @application_version.setter
    def application_version(self, application_version):
        """Sets the application_version of this GetDocxMetadataPropertiesResponse.

        Application version that authored the document, if available  # noqa: E501

        :param application_version: The application_version of this GetDocxMetadataPropertiesResponse.  # noqa: E501
        :type: str
        """

        self._application_version = application_version

    @property
    def word_count(self):
        """Gets the word_count of this GetDocxMetadataPropertiesResponse.  # noqa: E501

        Word count of the document  # noqa: E501

        :return: The word_count of this GetDocxMetadataPropertiesResponse.  # noqa: E501
        :rtype: int
        """
        return self._word_count

    @word_count.setter
    def word_count(self, word_count):
        """Sets the word_count of this GetDocxMetadataPropertiesResponse.

        Word count of the document  # noqa: E501

        :param word_count: The word_count of this GetDocxMetadataPropertiesResponse.  # noqa: E501
        :type: int
        """

        self._word_count = word_count

    @property
    def line_count(self):
        """Gets the line_count of this GetDocxMetadataPropertiesResponse.  # noqa: E501

        Line count of the document  # noqa: E501

        :return: The line_count of this GetDocxMetadataPropertiesResponse.  # noqa: E501
        :rtype: int
        """
        return self._line_count

    @line_count.setter
    def line_count(self, line_count):
        """Sets the line_count of this GetDocxMetadataPropertiesResponse.

        Line count of the document  # noqa: E501

        :param line_count: The line_count of this GetDocxMetadataPropertiesResponse.  # noqa: E501
        :type: int
        """

        self._line_count = line_count

    @property
    def paragraph_count(self):
        """Gets the paragraph_count of this GetDocxMetadataPropertiesResponse.  # noqa: E501

        Paragraph count of the document  # noqa: E501

        :return: The paragraph_count of this GetDocxMetadataPropertiesResponse.  # noqa: E501
        :rtype: int
        """
        return self._paragraph_count

    @paragraph_count.setter
    def paragraph_count(self, paragraph_count):
        """Sets the paragraph_count of this GetDocxMetadataPropertiesResponse.

        Paragraph count of the document  # noqa: E501

        :param paragraph_count: The paragraph_count of this GetDocxMetadataPropertiesResponse.  # noqa: E501
        :type: int
        """

        self._paragraph_count = paragraph_count

    @property
    def page_count(self):
        """Gets the page_count of this GetDocxMetadataPropertiesResponse.  # noqa: E501

        Page count of the document  # noqa: E501

        :return: The page_count of this GetDocxMetadataPropertiesResponse.  # noqa: E501
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """Sets the page_count of this GetDocxMetadataPropertiesResponse.

        Page count of the document  # noqa: E501

        :param page_count: The page_count of this GetDocxMetadataPropertiesResponse.  # noqa: E501
        :type: int
        """

        self._page_count = page_count

    @property
    def custom_properties(self):
        """Gets the custom_properties of this GetDocxMetadataPropertiesResponse.  # noqa: E501

        Custom properties applied to the document  # noqa: E501

        :return: The custom_properties of this GetDocxMetadataPropertiesResponse.  # noqa: E501
        :rtype: list[DocxMetadataCustomProperty]
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """Sets the custom_properties of this GetDocxMetadataPropertiesResponse.

        Custom properties applied to the document  # noqa: E501

        :param custom_properties: The custom_properties of this GetDocxMetadataPropertiesResponse.  # noqa: E501
        :type: list[DocxMetadataCustomProperty]
        """

        self._custom_properties = custom_properties

    @property
    def successful(self):
        """Gets the successful of this GetDocxMetadataPropertiesResponse.  # noqa: E501

        True if successful, false otherwise  # noqa: E501

        :return: The successful of this GetDocxMetadataPropertiesResponse.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this GetDocxMetadataPropertiesResponse.

        True if successful, false otherwise  # noqa: E501

        :param successful: The successful of this GetDocxMetadataPropertiesResponse.  # noqa: E501
        :type: bool
        """

        self._successful = successful

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
        if issubclass(GetDocxMetadataPropertiesResponse, dict):
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
        if not isinstance(other, GetDocxMetadataPropertiesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
