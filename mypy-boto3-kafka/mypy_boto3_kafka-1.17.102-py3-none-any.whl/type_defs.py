"""
Type annotations for kafka service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kafka/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kafka.type_defs import BatchAssociateScramSecretRequestTypeDef

    data: BatchAssociateScramSecretRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ClientBrokerType,
    ClusterStateType,
    ConfigurationStateType,
    EnhancedMonitoringType,
    KafkaVersionStatusType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BatchAssociateScramSecretRequestTypeDef",
    "BatchAssociateScramSecretResponseResponseTypeDef",
    "BatchDisassociateScramSecretRequestTypeDef",
    "BatchDisassociateScramSecretResponseResponseTypeDef",
    "BrokerEBSVolumeInfoTypeDef",
    "BrokerLogsTypeDef",
    "BrokerNodeGroupInfoTypeDef",
    "BrokerNodeInfoTypeDef",
    "BrokerSoftwareInfoTypeDef",
    "ClientAuthenticationTypeDef",
    "CloudWatchLogsTypeDef",
    "ClusterInfoTypeDef",
    "ClusterOperationInfoTypeDef",
    "ClusterOperationStepInfoTypeDef",
    "ClusterOperationStepTypeDef",
    "CompatibleKafkaVersionTypeDef",
    "ConfigurationInfoTypeDef",
    "ConfigurationRevisionTypeDef",
    "ConfigurationTypeDef",
    "CreateClusterRequestTypeDef",
    "CreateClusterResponseResponseTypeDef",
    "CreateConfigurationRequestTypeDef",
    "CreateConfigurationResponseResponseTypeDef",
    "DeleteClusterRequestTypeDef",
    "DeleteClusterResponseResponseTypeDef",
    "DeleteConfigurationRequestTypeDef",
    "DeleteConfigurationResponseResponseTypeDef",
    "DescribeClusterOperationRequestTypeDef",
    "DescribeClusterOperationResponseResponseTypeDef",
    "DescribeClusterRequestTypeDef",
    "DescribeClusterResponseResponseTypeDef",
    "DescribeConfigurationRequestTypeDef",
    "DescribeConfigurationResponseResponseTypeDef",
    "DescribeConfigurationRevisionRequestTypeDef",
    "DescribeConfigurationRevisionResponseResponseTypeDef",
    "EBSStorageInfoTypeDef",
    "EncryptionAtRestTypeDef",
    "EncryptionInTransitTypeDef",
    "EncryptionInfoTypeDef",
    "ErrorInfoTypeDef",
    "FirehoseTypeDef",
    "GetBootstrapBrokersRequestTypeDef",
    "GetBootstrapBrokersResponseResponseTypeDef",
    "GetCompatibleKafkaVersionsRequestTypeDef",
    "GetCompatibleKafkaVersionsResponseResponseTypeDef",
    "IamTypeDef",
    "JmxExporterInfoTypeDef",
    "JmxExporterTypeDef",
    "KafkaVersionTypeDef",
    "ListClusterOperationsRequestTypeDef",
    "ListClusterOperationsResponseResponseTypeDef",
    "ListClustersRequestTypeDef",
    "ListClustersResponseResponseTypeDef",
    "ListConfigurationRevisionsRequestTypeDef",
    "ListConfigurationRevisionsResponseResponseTypeDef",
    "ListConfigurationsRequestTypeDef",
    "ListConfigurationsResponseResponseTypeDef",
    "ListKafkaVersionsRequestTypeDef",
    "ListKafkaVersionsResponseResponseTypeDef",
    "ListNodesRequestTypeDef",
    "ListNodesResponseResponseTypeDef",
    "ListScramSecretsRequestTypeDef",
    "ListScramSecretsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "LoggingInfoTypeDef",
    "MutableClusterInfoTypeDef",
    "NodeExporterInfoTypeDef",
    "NodeExporterTypeDef",
    "NodeInfoTypeDef",
    "OpenMonitoringInfoTypeDef",
    "OpenMonitoringTypeDef",
    "PaginatorConfigTypeDef",
    "PrometheusInfoTypeDef",
    "PrometheusTypeDef",
    "RebootBrokerRequestTypeDef",
    "RebootBrokerResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "S3TypeDef",
    "SaslTypeDef",
    "ScramTypeDef",
    "StateInfoTypeDef",
    "StorageInfoTypeDef",
    "TagResourceRequestTypeDef",
    "TlsTypeDef",
    "UnprocessedScramSecretTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateBrokerCountRequestTypeDef",
    "UpdateBrokerCountResponseResponseTypeDef",
    "UpdateBrokerStorageRequestTypeDef",
    "UpdateBrokerStorageResponseResponseTypeDef",
    "UpdateBrokerTypeRequestTypeDef",
    "UpdateBrokerTypeResponseResponseTypeDef",
    "UpdateClusterConfigurationRequestTypeDef",
    "UpdateClusterConfigurationResponseResponseTypeDef",
    "UpdateClusterKafkaVersionRequestTypeDef",
    "UpdateClusterKafkaVersionResponseResponseTypeDef",
    "UpdateConfigurationRequestTypeDef",
    "UpdateConfigurationResponseResponseTypeDef",
    "UpdateMonitoringRequestTypeDef",
    "UpdateMonitoringResponseResponseTypeDef",
    "ZookeeperNodeInfoTypeDef",
)

BatchAssociateScramSecretRequestTypeDef = TypedDict(
    "BatchAssociateScramSecretRequestTypeDef",
    {
        "ClusterArn": str,
        "SecretArnList": List[str],
    },
)

BatchAssociateScramSecretResponseResponseTypeDef = TypedDict(
    "BatchAssociateScramSecretResponseResponseTypeDef",
    {
        "ClusterArn": str,
        "UnprocessedScramSecrets": List["UnprocessedScramSecretTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDisassociateScramSecretRequestTypeDef = TypedDict(
    "BatchDisassociateScramSecretRequestTypeDef",
    {
        "ClusterArn": str,
        "SecretArnList": List[str],
    },
)

BatchDisassociateScramSecretResponseResponseTypeDef = TypedDict(
    "BatchDisassociateScramSecretResponseResponseTypeDef",
    {
        "ClusterArn": str,
        "UnprocessedScramSecrets": List["UnprocessedScramSecretTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BrokerEBSVolumeInfoTypeDef = TypedDict(
    "BrokerEBSVolumeInfoTypeDef",
    {
        "KafkaBrokerNodeId": str,
        "VolumeSizeGB": int,
    },
)

BrokerLogsTypeDef = TypedDict(
    "BrokerLogsTypeDef",
    {
        "CloudWatchLogs": "CloudWatchLogsTypeDef",
        "Firehose": "FirehoseTypeDef",
        "S3": "S3TypeDef",
    },
    total=False,
)

_RequiredBrokerNodeGroupInfoTypeDef = TypedDict(
    "_RequiredBrokerNodeGroupInfoTypeDef",
    {
        "ClientSubnets": List[str],
        "InstanceType": str,
    },
)
_OptionalBrokerNodeGroupInfoTypeDef = TypedDict(
    "_OptionalBrokerNodeGroupInfoTypeDef",
    {
        "BrokerAZDistribution": Literal["DEFAULT"],
        "SecurityGroups": List[str],
        "StorageInfo": "StorageInfoTypeDef",
    },
    total=False,
)


class BrokerNodeGroupInfoTypeDef(
    _RequiredBrokerNodeGroupInfoTypeDef, _OptionalBrokerNodeGroupInfoTypeDef
):
    pass


BrokerNodeInfoTypeDef = TypedDict(
    "BrokerNodeInfoTypeDef",
    {
        "AttachedENIId": str,
        "BrokerId": float,
        "ClientSubnet": str,
        "ClientVpcIpAddress": str,
        "CurrentBrokerSoftwareInfo": "BrokerSoftwareInfoTypeDef",
        "Endpoints": List[str],
    },
    total=False,
)

BrokerSoftwareInfoTypeDef = TypedDict(
    "BrokerSoftwareInfoTypeDef",
    {
        "ConfigurationArn": str,
        "ConfigurationRevision": int,
        "KafkaVersion": str,
    },
    total=False,
)

ClientAuthenticationTypeDef = TypedDict(
    "ClientAuthenticationTypeDef",
    {
        "Sasl": "SaslTypeDef",
        "Tls": "TlsTypeDef",
    },
    total=False,
)

_RequiredCloudWatchLogsTypeDef = TypedDict(
    "_RequiredCloudWatchLogsTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalCloudWatchLogsTypeDef = TypedDict(
    "_OptionalCloudWatchLogsTypeDef",
    {
        "LogGroup": str,
    },
    total=False,
)


class CloudWatchLogsTypeDef(_RequiredCloudWatchLogsTypeDef, _OptionalCloudWatchLogsTypeDef):
    pass


ClusterInfoTypeDef = TypedDict(
    "ClusterInfoTypeDef",
    {
        "ActiveOperationArn": str,
        "BrokerNodeGroupInfo": "BrokerNodeGroupInfoTypeDef",
        "ClientAuthentication": "ClientAuthenticationTypeDef",
        "ClusterArn": str,
        "ClusterName": str,
        "CreationTime": datetime,
        "CurrentBrokerSoftwareInfo": "BrokerSoftwareInfoTypeDef",
        "CurrentVersion": str,
        "EncryptionInfo": "EncryptionInfoTypeDef",
        "EnhancedMonitoring": EnhancedMonitoringType,
        "OpenMonitoring": "OpenMonitoringTypeDef",
        "LoggingInfo": "LoggingInfoTypeDef",
        "NumberOfBrokerNodes": int,
        "State": ClusterStateType,
        "StateInfo": "StateInfoTypeDef",
        "Tags": Dict[str, str],
        "ZookeeperConnectString": str,
        "ZookeeperConnectStringTls": str,
    },
    total=False,
)

ClusterOperationInfoTypeDef = TypedDict(
    "ClusterOperationInfoTypeDef",
    {
        "ClientRequestId": str,
        "ClusterArn": str,
        "CreationTime": datetime,
        "EndTime": datetime,
        "ErrorInfo": "ErrorInfoTypeDef",
        "OperationArn": str,
        "OperationState": str,
        "OperationSteps": List["ClusterOperationStepTypeDef"],
        "OperationType": str,
        "SourceClusterInfo": "MutableClusterInfoTypeDef",
        "TargetClusterInfo": "MutableClusterInfoTypeDef",
    },
    total=False,
)

ClusterOperationStepInfoTypeDef = TypedDict(
    "ClusterOperationStepInfoTypeDef",
    {
        "StepStatus": str,
    },
    total=False,
)

ClusterOperationStepTypeDef = TypedDict(
    "ClusterOperationStepTypeDef",
    {
        "StepInfo": "ClusterOperationStepInfoTypeDef",
        "StepName": str,
    },
    total=False,
)

CompatibleKafkaVersionTypeDef = TypedDict(
    "CompatibleKafkaVersionTypeDef",
    {
        "SourceVersion": str,
        "TargetVersions": List[str],
    },
    total=False,
)

ConfigurationInfoTypeDef = TypedDict(
    "ConfigurationInfoTypeDef",
    {
        "Arn": str,
        "Revision": int,
    },
)

_RequiredConfigurationRevisionTypeDef = TypedDict(
    "_RequiredConfigurationRevisionTypeDef",
    {
        "CreationTime": datetime,
        "Revision": int,
    },
)
_OptionalConfigurationRevisionTypeDef = TypedDict(
    "_OptionalConfigurationRevisionTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class ConfigurationRevisionTypeDef(
    _RequiredConfigurationRevisionTypeDef, _OptionalConfigurationRevisionTypeDef
):
    pass


ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "Description": str,
        "KafkaVersions": List[str],
        "LatestRevision": "ConfigurationRevisionTypeDef",
        "Name": str,
        "State": ConfigurationStateType,
    },
)

_RequiredCreateClusterRequestTypeDef = TypedDict(
    "_RequiredCreateClusterRequestTypeDef",
    {
        "BrokerNodeGroupInfo": "BrokerNodeGroupInfoTypeDef",
        "ClusterName": str,
        "KafkaVersion": str,
        "NumberOfBrokerNodes": int,
    },
)
_OptionalCreateClusterRequestTypeDef = TypedDict(
    "_OptionalCreateClusterRequestTypeDef",
    {
        "ClientAuthentication": "ClientAuthenticationTypeDef",
        "ConfigurationInfo": "ConfigurationInfoTypeDef",
        "EncryptionInfo": "EncryptionInfoTypeDef",
        "EnhancedMonitoring": EnhancedMonitoringType,
        "OpenMonitoring": "OpenMonitoringInfoTypeDef",
        "LoggingInfo": "LoggingInfoTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateClusterRequestTypeDef(
    _RequiredCreateClusterRequestTypeDef, _OptionalCreateClusterRequestTypeDef
):
    pass


CreateClusterResponseResponseTypeDef = TypedDict(
    "CreateClusterResponseResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterName": str,
        "State": ClusterStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateConfigurationRequestTypeDef = TypedDict(
    "_RequiredCreateConfigurationRequestTypeDef",
    {
        "Name": str,
        "ServerProperties": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalCreateConfigurationRequestTypeDef = TypedDict(
    "_OptionalCreateConfigurationRequestTypeDef",
    {
        "Description": str,
        "KafkaVersions": List[str],
    },
    total=False,
)


class CreateConfigurationRequestTypeDef(
    _RequiredCreateConfigurationRequestTypeDef, _OptionalCreateConfigurationRequestTypeDef
):
    pass


CreateConfigurationResponseResponseTypeDef = TypedDict(
    "CreateConfigurationResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "LatestRevision": "ConfigurationRevisionTypeDef",
        "Name": str,
        "State": ConfigurationStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteClusterRequestTypeDef = TypedDict(
    "_RequiredDeleteClusterRequestTypeDef",
    {
        "ClusterArn": str,
    },
)
_OptionalDeleteClusterRequestTypeDef = TypedDict(
    "_OptionalDeleteClusterRequestTypeDef",
    {
        "CurrentVersion": str,
    },
    total=False,
)


class DeleteClusterRequestTypeDef(
    _RequiredDeleteClusterRequestTypeDef, _OptionalDeleteClusterRequestTypeDef
):
    pass


DeleteClusterResponseResponseTypeDef = TypedDict(
    "DeleteClusterResponseResponseTypeDef",
    {
        "ClusterArn": str,
        "State": ClusterStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteConfigurationRequestTypeDef = TypedDict(
    "DeleteConfigurationRequestTypeDef",
    {
        "Arn": str,
    },
)

DeleteConfigurationResponseResponseTypeDef = TypedDict(
    "DeleteConfigurationResponseResponseTypeDef",
    {
        "Arn": str,
        "State": ConfigurationStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClusterOperationRequestTypeDef = TypedDict(
    "DescribeClusterOperationRequestTypeDef",
    {
        "ClusterOperationArn": str,
    },
)

DescribeClusterOperationResponseResponseTypeDef = TypedDict(
    "DescribeClusterOperationResponseResponseTypeDef",
    {
        "ClusterOperationInfo": "ClusterOperationInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClusterRequestTypeDef = TypedDict(
    "DescribeClusterRequestTypeDef",
    {
        "ClusterArn": str,
    },
)

DescribeClusterResponseResponseTypeDef = TypedDict(
    "DescribeClusterResponseResponseTypeDef",
    {
        "ClusterInfo": "ClusterInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigurationRequestTypeDef = TypedDict(
    "DescribeConfigurationRequestTypeDef",
    {
        "Arn": str,
    },
)

DescribeConfigurationResponseResponseTypeDef = TypedDict(
    "DescribeConfigurationResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "Description": str,
        "KafkaVersions": List[str],
        "LatestRevision": "ConfigurationRevisionTypeDef",
        "Name": str,
        "State": ConfigurationStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigurationRevisionRequestTypeDef = TypedDict(
    "DescribeConfigurationRevisionRequestTypeDef",
    {
        "Arn": str,
        "Revision": int,
    },
)

DescribeConfigurationRevisionResponseResponseTypeDef = TypedDict(
    "DescribeConfigurationRevisionResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "Description": str,
        "Revision": int,
        "ServerProperties": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EBSStorageInfoTypeDef = TypedDict(
    "EBSStorageInfoTypeDef",
    {
        "VolumeSize": int,
    },
    total=False,
)

EncryptionAtRestTypeDef = TypedDict(
    "EncryptionAtRestTypeDef",
    {
        "DataVolumeKMSKeyId": str,
    },
)

EncryptionInTransitTypeDef = TypedDict(
    "EncryptionInTransitTypeDef",
    {
        "ClientBroker": ClientBrokerType,
        "InCluster": bool,
    },
    total=False,
)

EncryptionInfoTypeDef = TypedDict(
    "EncryptionInfoTypeDef",
    {
        "EncryptionAtRest": "EncryptionAtRestTypeDef",
        "EncryptionInTransit": "EncryptionInTransitTypeDef",
    },
    total=False,
)

ErrorInfoTypeDef = TypedDict(
    "ErrorInfoTypeDef",
    {
        "ErrorCode": str,
        "ErrorString": str,
    },
    total=False,
)

_RequiredFirehoseTypeDef = TypedDict(
    "_RequiredFirehoseTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalFirehoseTypeDef = TypedDict(
    "_OptionalFirehoseTypeDef",
    {
        "DeliveryStream": str,
    },
    total=False,
)


class FirehoseTypeDef(_RequiredFirehoseTypeDef, _OptionalFirehoseTypeDef):
    pass


GetBootstrapBrokersRequestTypeDef = TypedDict(
    "GetBootstrapBrokersRequestTypeDef",
    {
        "ClusterArn": str,
    },
)

GetBootstrapBrokersResponseResponseTypeDef = TypedDict(
    "GetBootstrapBrokersResponseResponseTypeDef",
    {
        "BootstrapBrokerString": str,
        "BootstrapBrokerStringTls": str,
        "BootstrapBrokerStringSaslScram": str,
        "BootstrapBrokerStringSaslIam": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCompatibleKafkaVersionsRequestTypeDef = TypedDict(
    "GetCompatibleKafkaVersionsRequestTypeDef",
    {
        "ClusterArn": str,
    },
    total=False,
)

GetCompatibleKafkaVersionsResponseResponseTypeDef = TypedDict(
    "GetCompatibleKafkaVersionsResponseResponseTypeDef",
    {
        "CompatibleKafkaVersions": List["CompatibleKafkaVersionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IamTypeDef = TypedDict(
    "IamTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

JmxExporterInfoTypeDef = TypedDict(
    "JmxExporterInfoTypeDef",
    {
        "EnabledInBroker": bool,
    },
)

JmxExporterTypeDef = TypedDict(
    "JmxExporterTypeDef",
    {
        "EnabledInBroker": bool,
    },
)

KafkaVersionTypeDef = TypedDict(
    "KafkaVersionTypeDef",
    {
        "Version": str,
        "Status": KafkaVersionStatusType,
    },
    total=False,
)

_RequiredListClusterOperationsRequestTypeDef = TypedDict(
    "_RequiredListClusterOperationsRequestTypeDef",
    {
        "ClusterArn": str,
    },
)
_OptionalListClusterOperationsRequestTypeDef = TypedDict(
    "_OptionalListClusterOperationsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListClusterOperationsRequestTypeDef(
    _RequiredListClusterOperationsRequestTypeDef, _OptionalListClusterOperationsRequestTypeDef
):
    pass


ListClusterOperationsResponseResponseTypeDef = TypedDict(
    "ListClusterOperationsResponseResponseTypeDef",
    {
        "ClusterOperationInfoList": List["ClusterOperationInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListClustersRequestTypeDef = TypedDict(
    "ListClustersRequestTypeDef",
    {
        "ClusterNameFilter": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListClustersResponseResponseTypeDef = TypedDict(
    "ListClustersResponseResponseTypeDef",
    {
        "ClusterInfoList": List["ClusterInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListConfigurationRevisionsRequestTypeDef = TypedDict(
    "_RequiredListConfigurationRevisionsRequestTypeDef",
    {
        "Arn": str,
    },
)
_OptionalListConfigurationRevisionsRequestTypeDef = TypedDict(
    "_OptionalListConfigurationRevisionsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListConfigurationRevisionsRequestTypeDef(
    _RequiredListConfigurationRevisionsRequestTypeDef,
    _OptionalListConfigurationRevisionsRequestTypeDef,
):
    pass


ListConfigurationRevisionsResponseResponseTypeDef = TypedDict(
    "ListConfigurationRevisionsResponseResponseTypeDef",
    {
        "NextToken": str,
        "Revisions": List["ConfigurationRevisionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListConfigurationsRequestTypeDef = TypedDict(
    "ListConfigurationsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListConfigurationsResponseResponseTypeDef = TypedDict(
    "ListConfigurationsResponseResponseTypeDef",
    {
        "Configurations": List["ConfigurationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListKafkaVersionsRequestTypeDef = TypedDict(
    "ListKafkaVersionsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListKafkaVersionsResponseResponseTypeDef = TypedDict(
    "ListKafkaVersionsResponseResponseTypeDef",
    {
        "KafkaVersions": List["KafkaVersionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListNodesRequestTypeDef = TypedDict(
    "_RequiredListNodesRequestTypeDef",
    {
        "ClusterArn": str,
    },
)
_OptionalListNodesRequestTypeDef = TypedDict(
    "_OptionalListNodesRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListNodesRequestTypeDef(_RequiredListNodesRequestTypeDef, _OptionalListNodesRequestTypeDef):
    pass


ListNodesResponseResponseTypeDef = TypedDict(
    "ListNodesResponseResponseTypeDef",
    {
        "NextToken": str,
        "NodeInfoList": List["NodeInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListScramSecretsRequestTypeDef = TypedDict(
    "_RequiredListScramSecretsRequestTypeDef",
    {
        "ClusterArn": str,
    },
)
_OptionalListScramSecretsRequestTypeDef = TypedDict(
    "_OptionalListScramSecretsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListScramSecretsRequestTypeDef(
    _RequiredListScramSecretsRequestTypeDef, _OptionalListScramSecretsRequestTypeDef
):
    pass


ListScramSecretsResponseResponseTypeDef = TypedDict(
    "ListScramSecretsResponseResponseTypeDef",
    {
        "NextToken": str,
        "SecretArnList": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingInfoTypeDef = TypedDict(
    "LoggingInfoTypeDef",
    {
        "BrokerLogs": "BrokerLogsTypeDef",
    },
)

MutableClusterInfoTypeDef = TypedDict(
    "MutableClusterInfoTypeDef",
    {
        "BrokerEBSVolumeInfo": List["BrokerEBSVolumeInfoTypeDef"],
        "ConfigurationInfo": "ConfigurationInfoTypeDef",
        "NumberOfBrokerNodes": int,
        "EnhancedMonitoring": EnhancedMonitoringType,
        "OpenMonitoring": "OpenMonitoringTypeDef",
        "KafkaVersion": str,
        "LoggingInfo": "LoggingInfoTypeDef",
        "InstanceType": str,
    },
    total=False,
)

NodeExporterInfoTypeDef = TypedDict(
    "NodeExporterInfoTypeDef",
    {
        "EnabledInBroker": bool,
    },
)

NodeExporterTypeDef = TypedDict(
    "NodeExporterTypeDef",
    {
        "EnabledInBroker": bool,
    },
)

NodeInfoTypeDef = TypedDict(
    "NodeInfoTypeDef",
    {
        "AddedToClusterTime": str,
        "BrokerNodeInfo": "BrokerNodeInfoTypeDef",
        "InstanceType": str,
        "NodeARN": str,
        "NodeType": Literal["BROKER"],
        "ZookeeperNodeInfo": "ZookeeperNodeInfoTypeDef",
    },
    total=False,
)

OpenMonitoringInfoTypeDef = TypedDict(
    "OpenMonitoringInfoTypeDef",
    {
        "Prometheus": "PrometheusInfoTypeDef",
    },
)

OpenMonitoringTypeDef = TypedDict(
    "OpenMonitoringTypeDef",
    {
        "Prometheus": "PrometheusTypeDef",
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PrometheusInfoTypeDef = TypedDict(
    "PrometheusInfoTypeDef",
    {
        "JmxExporter": "JmxExporterInfoTypeDef",
        "NodeExporter": "NodeExporterInfoTypeDef",
    },
    total=False,
)

PrometheusTypeDef = TypedDict(
    "PrometheusTypeDef",
    {
        "JmxExporter": "JmxExporterTypeDef",
        "NodeExporter": "NodeExporterTypeDef",
    },
    total=False,
)

RebootBrokerRequestTypeDef = TypedDict(
    "RebootBrokerRequestTypeDef",
    {
        "BrokerIds": List[str],
        "ClusterArn": str,
    },
)

RebootBrokerResponseResponseTypeDef = TypedDict(
    "RebootBrokerResponseResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

_RequiredS3TypeDef = TypedDict(
    "_RequiredS3TypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalS3TypeDef = TypedDict(
    "_OptionalS3TypeDef",
    {
        "Bucket": str,
        "Prefix": str,
    },
    total=False,
)


class S3TypeDef(_RequiredS3TypeDef, _OptionalS3TypeDef):
    pass


SaslTypeDef = TypedDict(
    "SaslTypeDef",
    {
        "Scram": "ScramTypeDef",
        "Iam": "IamTypeDef",
    },
    total=False,
)

ScramTypeDef = TypedDict(
    "ScramTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

StateInfoTypeDef = TypedDict(
    "StateInfoTypeDef",
    {
        "Code": str,
        "Message": str,
    },
    total=False,
)

StorageInfoTypeDef = TypedDict(
    "StorageInfoTypeDef",
    {
        "EbsStorageInfo": "EBSStorageInfoTypeDef",
    },
    total=False,
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

TlsTypeDef = TypedDict(
    "TlsTypeDef",
    {
        "CertificateAuthorityArnList": List[str],
    },
    total=False,
)

UnprocessedScramSecretTypeDef = TypedDict(
    "UnprocessedScramSecretTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
        "SecretArn": str,
    },
    total=False,
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

UpdateBrokerCountRequestTypeDef = TypedDict(
    "UpdateBrokerCountRequestTypeDef",
    {
        "ClusterArn": str,
        "CurrentVersion": str,
        "TargetNumberOfBrokerNodes": int,
    },
)

UpdateBrokerCountResponseResponseTypeDef = TypedDict(
    "UpdateBrokerCountResponseResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBrokerStorageRequestTypeDef = TypedDict(
    "UpdateBrokerStorageRequestTypeDef",
    {
        "ClusterArn": str,
        "CurrentVersion": str,
        "TargetBrokerEBSVolumeInfo": List["BrokerEBSVolumeInfoTypeDef"],
    },
)

UpdateBrokerStorageResponseResponseTypeDef = TypedDict(
    "UpdateBrokerStorageResponseResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBrokerTypeRequestTypeDef = TypedDict(
    "UpdateBrokerTypeRequestTypeDef",
    {
        "ClusterArn": str,
        "CurrentVersion": str,
        "TargetInstanceType": str,
    },
)

UpdateBrokerTypeResponseResponseTypeDef = TypedDict(
    "UpdateBrokerTypeResponseResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateClusterConfigurationRequestTypeDef = TypedDict(
    "UpdateClusterConfigurationRequestTypeDef",
    {
        "ClusterArn": str,
        "ConfigurationInfo": "ConfigurationInfoTypeDef",
        "CurrentVersion": str,
    },
)

UpdateClusterConfigurationResponseResponseTypeDef = TypedDict(
    "UpdateClusterConfigurationResponseResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateClusterKafkaVersionRequestTypeDef = TypedDict(
    "_RequiredUpdateClusterKafkaVersionRequestTypeDef",
    {
        "ClusterArn": str,
        "CurrentVersion": str,
        "TargetKafkaVersion": str,
    },
)
_OptionalUpdateClusterKafkaVersionRequestTypeDef = TypedDict(
    "_OptionalUpdateClusterKafkaVersionRequestTypeDef",
    {
        "ConfigurationInfo": "ConfigurationInfoTypeDef",
    },
    total=False,
)


class UpdateClusterKafkaVersionRequestTypeDef(
    _RequiredUpdateClusterKafkaVersionRequestTypeDef,
    _OptionalUpdateClusterKafkaVersionRequestTypeDef,
):
    pass


UpdateClusterKafkaVersionResponseResponseTypeDef = TypedDict(
    "UpdateClusterKafkaVersionResponseResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateConfigurationRequestTypeDef = TypedDict(
    "_RequiredUpdateConfigurationRequestTypeDef",
    {
        "Arn": str,
        "ServerProperties": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalUpdateConfigurationRequestTypeDef = TypedDict(
    "_OptionalUpdateConfigurationRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class UpdateConfigurationRequestTypeDef(
    _RequiredUpdateConfigurationRequestTypeDef, _OptionalUpdateConfigurationRequestTypeDef
):
    pass


UpdateConfigurationResponseResponseTypeDef = TypedDict(
    "UpdateConfigurationResponseResponseTypeDef",
    {
        "Arn": str,
        "LatestRevision": "ConfigurationRevisionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateMonitoringRequestTypeDef = TypedDict(
    "_RequiredUpdateMonitoringRequestTypeDef",
    {
        "ClusterArn": str,
        "CurrentVersion": str,
    },
)
_OptionalUpdateMonitoringRequestTypeDef = TypedDict(
    "_OptionalUpdateMonitoringRequestTypeDef",
    {
        "EnhancedMonitoring": EnhancedMonitoringType,
        "OpenMonitoring": "OpenMonitoringInfoTypeDef",
        "LoggingInfo": "LoggingInfoTypeDef",
    },
    total=False,
)


class UpdateMonitoringRequestTypeDef(
    _RequiredUpdateMonitoringRequestTypeDef, _OptionalUpdateMonitoringRequestTypeDef
):
    pass


UpdateMonitoringResponseResponseTypeDef = TypedDict(
    "UpdateMonitoringResponseResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ZookeeperNodeInfoTypeDef = TypedDict(
    "ZookeeperNodeInfoTypeDef",
    {
        "AttachedENIId": str,
        "ClientVpcIpAddress": str,
        "Endpoints": List[str],
        "ZookeeperId": float,
        "ZookeeperVersion": str,
    },
    total=False,
)
