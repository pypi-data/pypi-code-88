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


class V1ConnectionKind(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    HOST_PATH = "host_path"
    VOLUME_CLAIM = "volume_claim"
    GCS = "gcs"
    S3 = "s3"
    WASB = "wasb"
    REGISTRY = "registry"
    GIT = "git"
    AWS = "aws"
    GCP = "gcp"
    AZURE = "azure"
    MYSQL = "mysql"
    POSTGRES = "postgres"
    ORACLE = "oracle"
    VERTICA = "vertica"
    SQLITE = "sqlite"
    MSSQL = "mssql"
    REDIS = "redis"
    PRESTO = "presto"
    MONGO = "mongo"
    CASSANDRA = "cassandra"
    FTP = "ftp"
    GRPC = "grpc"
    HDFS = "hdfs"
    HTTP = "http"
    PIG_CLI = "pig_cli"
    HIVE_CLI = "hive_cli"
    HIVE_METASTORE = "hive_metastore"
    HIVE_SERVER2 = "hive_server2"
    JDBC = "jdbc"
    JENKINS = "jenkins"
    SAMBA = "samba"
    SNOWFLAKE = "snowflake"
    SSH = "ssh"
    CLOUDANT = "cloudant"
    DATABRICKS = "databricks"
    SEGMENT = "segment"
    SLACK = "slack"
    DISCORD = "discord"
    MATTERMOST = "mattermost"
    PAGERDUTY = "pagerduty"
    HIPCHAT = "hipchat"
    WEBHOOK = "webhook"
    CUSTOM = "custom"

    allowable_values = [HOST_PATH, VOLUME_CLAIM, GCS, S3, WASB, REGISTRY, GIT, AWS, GCP, AZURE, MYSQL, POSTGRES, ORACLE, VERTICA, SQLITE, MSSQL, REDIS, PRESTO, MONGO, CASSANDRA, FTP, GRPC, HDFS, HTTP, PIG_CLI, HIVE_CLI, HIVE_METASTORE, HIVE_SERVER2, JDBC, JENKINS, SAMBA, SNOWFLAKE, SSH, CLOUDANT, DATABRICKS, SEGMENT, SLACK, DISCORD, MATTERMOST, PAGERDUTY, HIPCHAT, WEBHOOK, CUSTOM]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """V1ConnectionKind - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

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
        if not isinstance(other, V1ConnectionKind):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ConnectionKind):
            return True

        return self.to_dict() != other.to_dict()
