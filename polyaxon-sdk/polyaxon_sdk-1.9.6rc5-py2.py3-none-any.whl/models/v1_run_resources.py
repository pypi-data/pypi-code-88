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


class V1RunResources(object):
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
        'cpu': 'float',
        'memory': 'float',
        'gpu': 'float',
        'custom': 'float',
        'cost': 'float'
    }

    attribute_map = {
        'cpu': 'cpu',
        'memory': 'memory',
        'gpu': 'gpu',
        'custom': 'custom',
        'cost': 'cost'
    }

    def __init__(self, cpu=None, memory=None, gpu=None, custom=None, cost=None, local_vars_configuration=None):  # noqa: E501
        """V1RunResources - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cpu = None
        self._memory = None
        self._gpu = None
        self._custom = None
        self._cost = None
        self.discriminator = None

        if cpu is not None:
            self.cpu = cpu
        if memory is not None:
            self.memory = memory
        if gpu is not None:
            self.gpu = gpu
        if custom is not None:
            self.custom = custom
        if cost is not None:
            self.cost = cost

    @property
    def cpu(self):
        """Gets the cpu of this V1RunResources.  # noqa: E501


        :return: The cpu of this V1RunResources.  # noqa: E501
        :rtype: float
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this V1RunResources.


        :param cpu: The cpu of this V1RunResources.  # noqa: E501
        :type: float
        """

        self._cpu = cpu

    @property
    def memory(self):
        """Gets the memory of this V1RunResources.  # noqa: E501


        :return: The memory of this V1RunResources.  # noqa: E501
        :rtype: float
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this V1RunResources.


        :param memory: The memory of this V1RunResources.  # noqa: E501
        :type: float
        """

        self._memory = memory

    @property
    def gpu(self):
        """Gets the gpu of this V1RunResources.  # noqa: E501


        :return: The gpu of this V1RunResources.  # noqa: E501
        :rtype: float
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu):
        """Sets the gpu of this V1RunResources.


        :param gpu: The gpu of this V1RunResources.  # noqa: E501
        :type: float
        """

        self._gpu = gpu

    @property
    def custom(self):
        """Gets the custom of this V1RunResources.  # noqa: E501


        :return: The custom of this V1RunResources.  # noqa: E501
        :rtype: float
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """Sets the custom of this V1RunResources.


        :param custom: The custom of this V1RunResources.  # noqa: E501
        :type: float
        """

        self._custom = custom

    @property
    def cost(self):
        """Gets the cost of this V1RunResources.  # noqa: E501


        :return: The cost of this V1RunResources.  # noqa: E501
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this V1RunResources.


        :param cost: The cost of this V1RunResources.  # noqa: E501
        :type: float
        """

        self._cost = cost

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
        if not isinstance(other, V1RunResources):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1RunResources):
            return True

        return self.to_dict() != other.to_dict()
