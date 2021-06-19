#!/usr/bin/python
#
# Copyright 2018-2021 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    Polyaxon SDKs and REST API specification.

    Polyaxon SDKs and REST API specification.  # noqa: E501

    The version of the OpenAPI document: 1.9.6-rc5
    Contact: contact@polyaxon.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from polyaxon_sdk.configuration import Configuration


class V1ConnectionSchema(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'bucket_connection': 'V1BucketConnection',
        'host_path_connection': 'V1HostPathConnection',
        'claim_connection': 'V1ClaimConnection',
        'host_connection': 'V1HostConnection',
        'git_connection': 'V1GitConnection'
    }

    attribute_map = {
        'bucket_connection': 'bucketConnection',
        'host_path_connection': 'hostPathConnection',
        'claim_connection': 'claimConnection',
        'host_connection': 'hostConnection',
        'git_connection': 'gitConnection'
    }

    def __init__(self, bucket_connection=None, host_path_connection=None, claim_connection=None, host_connection=None, git_connection=None, local_vars_configuration=None):  # noqa: E501
        """V1ConnectionSchema - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bucket_connection = None
        self._host_path_connection = None
        self._claim_connection = None
        self._host_connection = None
        self._git_connection = None
        self.discriminator = None

        if bucket_connection is not None:
            self.bucket_connection = bucket_connection
        if host_path_connection is not None:
            self.host_path_connection = host_path_connection
        if claim_connection is not None:
            self.claim_connection = claim_connection
        if host_connection is not None:
            self.host_connection = host_connection
        if git_connection is not None:
            self.git_connection = git_connection

    @property
    def bucket_connection(self):
        """Gets the bucket_connection of this V1ConnectionSchema.  # noqa: E501


        :return: The bucket_connection of this V1ConnectionSchema.  # noqa: E501
        :rtype: V1BucketConnection
        """
        return self._bucket_connection

    @bucket_connection.setter
    def bucket_connection(self, bucket_connection):
        """Sets the bucket_connection of this V1ConnectionSchema.


        :param bucket_connection: The bucket_connection of this V1ConnectionSchema.  # noqa: E501
        :type: V1BucketConnection
        """

        self._bucket_connection = bucket_connection

    @property
    def host_path_connection(self):
        """Gets the host_path_connection of this V1ConnectionSchema.  # noqa: E501


        :return: The host_path_connection of this V1ConnectionSchema.  # noqa: E501
        :rtype: V1HostPathConnection
        """
        return self._host_path_connection

    @host_path_connection.setter
    def host_path_connection(self, host_path_connection):
        """Sets the host_path_connection of this V1ConnectionSchema.


        :param host_path_connection: The host_path_connection of this V1ConnectionSchema.  # noqa: E501
        :type: V1HostPathConnection
        """

        self._host_path_connection = host_path_connection

    @property
    def claim_connection(self):
        """Gets the claim_connection of this V1ConnectionSchema.  # noqa: E501


        :return: The claim_connection of this V1ConnectionSchema.  # noqa: E501
        :rtype: V1ClaimConnection
        """
        return self._claim_connection

    @claim_connection.setter
    def claim_connection(self, claim_connection):
        """Sets the claim_connection of this V1ConnectionSchema.


        :param claim_connection: The claim_connection of this V1ConnectionSchema.  # noqa: E501
        :type: V1ClaimConnection
        """

        self._claim_connection = claim_connection

    @property
    def host_connection(self):
        """Gets the host_connection of this V1ConnectionSchema.  # noqa: E501


        :return: The host_connection of this V1ConnectionSchema.  # noqa: E501
        :rtype: V1HostConnection
        """
        return self._host_connection

    @host_connection.setter
    def host_connection(self, host_connection):
        """Sets the host_connection of this V1ConnectionSchema.


        :param host_connection: The host_connection of this V1ConnectionSchema.  # noqa: E501
        :type: V1HostConnection
        """

        self._host_connection = host_connection

    @property
    def git_connection(self):
        """Gets the git_connection of this V1ConnectionSchema.  # noqa: E501


        :return: The git_connection of this V1ConnectionSchema.  # noqa: E501
        :rtype: V1GitConnection
        """
        return self._git_connection

    @git_connection.setter
    def git_connection(self, git_connection):
        """Sets the git_connection of this V1ConnectionSchema.


        :param git_connection: The git_connection of this V1ConnectionSchema.  # noqa: E501
        :type: V1GitConnection
        """

        self._git_connection = git_connection

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1ConnectionSchema):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ConnectionSchema):
            return True

        return self.to_dict() != other.to_dict()
