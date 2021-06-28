"""
Type annotations for dms service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/type_defs.html)

Usage::

    ```python
    from mypy_boto3_dms.type_defs import AccountQuotaTypeDef

    data: AccountQuotaTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    AuthMechanismValueType,
    AuthTypeValueType,
    CharLengthSemanticsType,
    CompressionTypeValueType,
    DataFormatValueType,
    DatePartitionDelimiterValueType,
    DatePartitionSequenceValueType,
    DmsSslModeValueType,
    EncodingTypeValueType,
    EncryptionModeValueType,
    EndpointSettingTypeValueType,
    KafkaSecurityProtocolType,
    MessageFormatValueType,
    MigrationTypeValueType,
    NestingLevelValueType,
    ParquetVersionValueType,
    RefreshSchemasStatusTypeValueType,
    ReloadOptionValueType,
    ReplicationEndpointTypeValueType,
    SafeguardPolicyType,
    StartReplicationTaskTypeValueType,
    TargetDbTypeType,
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
    "AccountQuotaTypeDef",
    "AddTagsToResourceMessageTypeDef",
    "ApplyPendingMaintenanceActionMessageTypeDef",
    "ApplyPendingMaintenanceActionResponseResponseTypeDef",
    "AvailabilityZoneTypeDef",
    "CancelReplicationTaskAssessmentRunMessageTypeDef",
    "CancelReplicationTaskAssessmentRunResponseResponseTypeDef",
    "CertificateTypeDef",
    "ConnectionTypeDef",
    "CreateEndpointMessageTypeDef",
    "CreateEndpointResponseResponseTypeDef",
    "CreateEventSubscriptionMessageTypeDef",
    "CreateEventSubscriptionResponseResponseTypeDef",
    "CreateReplicationInstanceMessageTypeDef",
    "CreateReplicationInstanceResponseResponseTypeDef",
    "CreateReplicationSubnetGroupMessageTypeDef",
    "CreateReplicationSubnetGroupResponseResponseTypeDef",
    "CreateReplicationTaskMessageTypeDef",
    "CreateReplicationTaskResponseResponseTypeDef",
    "DeleteCertificateMessageTypeDef",
    "DeleteCertificateResponseResponseTypeDef",
    "DeleteConnectionMessageTypeDef",
    "DeleteConnectionResponseResponseTypeDef",
    "DeleteEndpointMessageTypeDef",
    "DeleteEndpointResponseResponseTypeDef",
    "DeleteEventSubscriptionMessageTypeDef",
    "DeleteEventSubscriptionResponseResponseTypeDef",
    "DeleteReplicationInstanceMessageTypeDef",
    "DeleteReplicationInstanceResponseResponseTypeDef",
    "DeleteReplicationSubnetGroupMessageTypeDef",
    "DeleteReplicationTaskAssessmentRunMessageTypeDef",
    "DeleteReplicationTaskAssessmentRunResponseResponseTypeDef",
    "DeleteReplicationTaskMessageTypeDef",
    "DeleteReplicationTaskResponseResponseTypeDef",
    "DescribeAccountAttributesResponseResponseTypeDef",
    "DescribeApplicableIndividualAssessmentsMessageTypeDef",
    "DescribeApplicableIndividualAssessmentsResponseResponseTypeDef",
    "DescribeCertificatesMessageTypeDef",
    "DescribeCertificatesResponseResponseTypeDef",
    "DescribeConnectionsMessageTypeDef",
    "DescribeConnectionsResponseResponseTypeDef",
    "DescribeEndpointSettingsMessageTypeDef",
    "DescribeEndpointSettingsResponseResponseTypeDef",
    "DescribeEndpointTypesMessageTypeDef",
    "DescribeEndpointTypesResponseResponseTypeDef",
    "DescribeEndpointsMessageTypeDef",
    "DescribeEndpointsResponseResponseTypeDef",
    "DescribeEventCategoriesMessageTypeDef",
    "DescribeEventCategoriesResponseResponseTypeDef",
    "DescribeEventSubscriptionsMessageTypeDef",
    "DescribeEventSubscriptionsResponseResponseTypeDef",
    "DescribeEventsMessageTypeDef",
    "DescribeEventsResponseResponseTypeDef",
    "DescribeOrderableReplicationInstancesMessageTypeDef",
    "DescribeOrderableReplicationInstancesResponseResponseTypeDef",
    "DescribePendingMaintenanceActionsMessageTypeDef",
    "DescribePendingMaintenanceActionsResponseResponseTypeDef",
    "DescribeRefreshSchemasStatusMessageTypeDef",
    "DescribeRefreshSchemasStatusResponseResponseTypeDef",
    "DescribeReplicationInstanceTaskLogsMessageTypeDef",
    "DescribeReplicationInstanceTaskLogsResponseResponseTypeDef",
    "DescribeReplicationInstancesMessageTypeDef",
    "DescribeReplicationInstancesResponseResponseTypeDef",
    "DescribeReplicationSubnetGroupsMessageTypeDef",
    "DescribeReplicationSubnetGroupsResponseResponseTypeDef",
    "DescribeReplicationTaskAssessmentResultsMessageTypeDef",
    "DescribeReplicationTaskAssessmentResultsResponseResponseTypeDef",
    "DescribeReplicationTaskAssessmentRunsMessageTypeDef",
    "DescribeReplicationTaskAssessmentRunsResponseResponseTypeDef",
    "DescribeReplicationTaskIndividualAssessmentsMessageTypeDef",
    "DescribeReplicationTaskIndividualAssessmentsResponseResponseTypeDef",
    "DescribeReplicationTasksMessageTypeDef",
    "DescribeReplicationTasksResponseResponseTypeDef",
    "DescribeSchemasMessageTypeDef",
    "DescribeSchemasResponseResponseTypeDef",
    "DescribeTableStatisticsMessageTypeDef",
    "DescribeTableStatisticsResponseResponseTypeDef",
    "DmsTransferSettingsTypeDef",
    "DocDbSettingsTypeDef",
    "DynamoDbSettingsTypeDef",
    "ElasticsearchSettingsTypeDef",
    "EndpointSettingTypeDef",
    "EndpointTypeDef",
    "EventCategoryGroupTypeDef",
    "EventSubscriptionTypeDef",
    "EventTypeDef",
    "FilterTypeDef",
    "IBMDb2SettingsTypeDef",
    "ImportCertificateMessageTypeDef",
    "ImportCertificateResponseResponseTypeDef",
    "KafkaSettingsTypeDef",
    "KinesisSettingsTypeDef",
    "ListTagsForResourceMessageTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "MicrosoftSQLServerSettingsTypeDef",
    "ModifyEndpointMessageTypeDef",
    "ModifyEndpointResponseResponseTypeDef",
    "ModifyEventSubscriptionMessageTypeDef",
    "ModifyEventSubscriptionResponseResponseTypeDef",
    "ModifyReplicationInstanceMessageTypeDef",
    "ModifyReplicationInstanceResponseResponseTypeDef",
    "ModifyReplicationSubnetGroupMessageTypeDef",
    "ModifyReplicationSubnetGroupResponseResponseTypeDef",
    "ModifyReplicationTaskMessageTypeDef",
    "ModifyReplicationTaskResponseResponseTypeDef",
    "MongoDbSettingsTypeDef",
    "MoveReplicationTaskMessageTypeDef",
    "MoveReplicationTaskResponseResponseTypeDef",
    "MySQLSettingsTypeDef",
    "NeptuneSettingsTypeDef",
    "OracleSettingsTypeDef",
    "OrderableReplicationInstanceTypeDef",
    "PaginatorConfigTypeDef",
    "PendingMaintenanceActionTypeDef",
    "PostgreSQLSettingsTypeDef",
    "RebootReplicationInstanceMessageTypeDef",
    "RebootReplicationInstanceResponseResponseTypeDef",
    "RedshiftSettingsTypeDef",
    "RefreshSchemasMessageTypeDef",
    "RefreshSchemasResponseResponseTypeDef",
    "RefreshSchemasStatusTypeDef",
    "ReloadTablesMessageTypeDef",
    "ReloadTablesResponseResponseTypeDef",
    "RemoveTagsFromResourceMessageTypeDef",
    "ReplicationInstanceTaskLogTypeDef",
    "ReplicationInstanceTypeDef",
    "ReplicationPendingModifiedValuesTypeDef",
    "ReplicationSubnetGroupTypeDef",
    "ReplicationTaskAssessmentResultTypeDef",
    "ReplicationTaskAssessmentRunProgressTypeDef",
    "ReplicationTaskAssessmentRunTypeDef",
    "ReplicationTaskIndividualAssessmentTypeDef",
    "ReplicationTaskStatsTypeDef",
    "ReplicationTaskTypeDef",
    "ResourcePendingMaintenanceActionsTypeDef",
    "ResponseMetadataTypeDef",
    "S3SettingsTypeDef",
    "StartReplicationTaskAssessmentMessageTypeDef",
    "StartReplicationTaskAssessmentResponseResponseTypeDef",
    "StartReplicationTaskAssessmentRunMessageTypeDef",
    "StartReplicationTaskAssessmentRunResponseResponseTypeDef",
    "StartReplicationTaskMessageTypeDef",
    "StartReplicationTaskResponseResponseTypeDef",
    "StopReplicationTaskMessageTypeDef",
    "StopReplicationTaskResponseResponseTypeDef",
    "SubnetTypeDef",
    "SupportedEndpointTypeTypeDef",
    "SybaseSettingsTypeDef",
    "TableStatisticsTypeDef",
    "TableToReloadTypeDef",
    "TagTypeDef",
    "TestConnectionMessageTypeDef",
    "TestConnectionResponseResponseTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "WaiterConfigTypeDef",
)

AccountQuotaTypeDef = TypedDict(
    "AccountQuotaTypeDef",
    {
        "AccountQuotaName": str,
        "Used": int,
        "Max": int,
    },
    total=False,
)

AddTagsToResourceMessageTypeDef = TypedDict(
    "AddTagsToResourceMessageTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

ApplyPendingMaintenanceActionMessageTypeDef = TypedDict(
    "ApplyPendingMaintenanceActionMessageTypeDef",
    {
        "ReplicationInstanceArn": str,
        "ApplyAction": str,
        "OptInType": str,
    },
)

ApplyPendingMaintenanceActionResponseResponseTypeDef = TypedDict(
    "ApplyPendingMaintenanceActionResponseResponseTypeDef",
    {
        "ResourcePendingMaintenanceActions": "ResourcePendingMaintenanceActionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "Name": str,
    },
    total=False,
)

CancelReplicationTaskAssessmentRunMessageTypeDef = TypedDict(
    "CancelReplicationTaskAssessmentRunMessageTypeDef",
    {
        "ReplicationTaskAssessmentRunArn": str,
    },
)

CancelReplicationTaskAssessmentRunResponseResponseTypeDef = TypedDict(
    "CancelReplicationTaskAssessmentRunResponseResponseTypeDef",
    {
        "ReplicationTaskAssessmentRun": "ReplicationTaskAssessmentRunTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "CertificateIdentifier": str,
        "CertificateCreationDate": datetime,
        "CertificatePem": str,
        "CertificateWallet": bytes,
        "CertificateArn": str,
        "CertificateOwner": str,
        "ValidFromDate": datetime,
        "ValidToDate": datetime,
        "SigningAlgorithm": str,
        "KeyLength": int,
    },
    total=False,
)

ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "ReplicationInstanceArn": str,
        "EndpointArn": str,
        "Status": str,
        "LastFailureMessage": str,
        "EndpointIdentifier": str,
        "ReplicationInstanceIdentifier": str,
    },
    total=False,
)

_RequiredCreateEndpointMessageTypeDef = TypedDict(
    "_RequiredCreateEndpointMessageTypeDef",
    {
        "EndpointIdentifier": str,
        "EndpointType": ReplicationEndpointTypeValueType,
        "EngineName": str,
    },
)
_OptionalCreateEndpointMessageTypeDef = TypedDict(
    "_OptionalCreateEndpointMessageTypeDef",
    {
        "Username": str,
        "Password": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "ExtraConnectionAttributes": str,
        "KmsKeyId": str,
        "Tags": List["TagTypeDef"],
        "CertificateArn": str,
        "SslMode": DmsSslModeValueType,
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "DynamoDbSettings": "DynamoDbSettingsTypeDef",
        "S3Settings": "S3SettingsTypeDef",
        "DmsTransferSettings": "DmsTransferSettingsTypeDef",
        "MongoDbSettings": "MongoDbSettingsTypeDef",
        "KinesisSettings": "KinesisSettingsTypeDef",
        "KafkaSettings": "KafkaSettingsTypeDef",
        "ElasticsearchSettings": "ElasticsearchSettingsTypeDef",
        "NeptuneSettings": "NeptuneSettingsTypeDef",
        "RedshiftSettings": "RedshiftSettingsTypeDef",
        "PostgreSQLSettings": "PostgreSQLSettingsTypeDef",
        "MySQLSettings": "MySQLSettingsTypeDef",
        "OracleSettings": "OracleSettingsTypeDef",
        "SybaseSettings": "SybaseSettingsTypeDef",
        "MicrosoftSQLServerSettings": "MicrosoftSQLServerSettingsTypeDef",
        "IBMDb2Settings": "IBMDb2SettingsTypeDef",
        "ResourceIdentifier": str,
        "DocDbSettings": "DocDbSettingsTypeDef",
    },
    total=False,
)


class CreateEndpointMessageTypeDef(
    _RequiredCreateEndpointMessageTypeDef, _OptionalCreateEndpointMessageTypeDef
):
    pass


CreateEndpointResponseResponseTypeDef = TypedDict(
    "CreateEndpointResponseResponseTypeDef",
    {
        "Endpoint": "EndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEventSubscriptionMessageTypeDef = TypedDict(
    "_RequiredCreateEventSubscriptionMessageTypeDef",
    {
        "SubscriptionName": str,
        "SnsTopicArn": str,
    },
)
_OptionalCreateEventSubscriptionMessageTypeDef = TypedDict(
    "_OptionalCreateEventSubscriptionMessageTypeDef",
    {
        "SourceType": str,
        "EventCategories": List[str],
        "SourceIds": List[str],
        "Enabled": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateEventSubscriptionMessageTypeDef(
    _RequiredCreateEventSubscriptionMessageTypeDef, _OptionalCreateEventSubscriptionMessageTypeDef
):
    pass


CreateEventSubscriptionResponseResponseTypeDef = TypedDict(
    "CreateEventSubscriptionResponseResponseTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateReplicationInstanceMessageTypeDef = TypedDict(
    "_RequiredCreateReplicationInstanceMessageTypeDef",
    {
        "ReplicationInstanceIdentifier": str,
        "ReplicationInstanceClass": str,
    },
)
_OptionalCreateReplicationInstanceMessageTypeDef = TypedDict(
    "_OptionalCreateReplicationInstanceMessageTypeDef",
    {
        "AllocatedStorage": int,
        "VpcSecurityGroupIds": List[str],
        "AvailabilityZone": str,
        "ReplicationSubnetGroupIdentifier": str,
        "PreferredMaintenanceWindow": str,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "Tags": List["TagTypeDef"],
        "KmsKeyId": str,
        "PubliclyAccessible": bool,
        "DnsNameServers": str,
        "ResourceIdentifier": str,
    },
    total=False,
)


class CreateReplicationInstanceMessageTypeDef(
    _RequiredCreateReplicationInstanceMessageTypeDef,
    _OptionalCreateReplicationInstanceMessageTypeDef,
):
    pass


CreateReplicationInstanceResponseResponseTypeDef = TypedDict(
    "CreateReplicationInstanceResponseResponseTypeDef",
    {
        "ReplicationInstance": "ReplicationInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateReplicationSubnetGroupMessageTypeDef = TypedDict(
    "_RequiredCreateReplicationSubnetGroupMessageTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "SubnetIds": List[str],
    },
)
_OptionalCreateReplicationSubnetGroupMessageTypeDef = TypedDict(
    "_OptionalCreateReplicationSubnetGroupMessageTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateReplicationSubnetGroupMessageTypeDef(
    _RequiredCreateReplicationSubnetGroupMessageTypeDef,
    _OptionalCreateReplicationSubnetGroupMessageTypeDef,
):
    pass


CreateReplicationSubnetGroupResponseResponseTypeDef = TypedDict(
    "CreateReplicationSubnetGroupResponseResponseTypeDef",
    {
        "ReplicationSubnetGroup": "ReplicationSubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateReplicationTaskMessageTypeDef = TypedDict(
    "_RequiredCreateReplicationTaskMessageTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "SourceEndpointArn": str,
        "TargetEndpointArn": str,
        "ReplicationInstanceArn": str,
        "MigrationType": MigrationTypeValueType,
        "TableMappings": str,
    },
)
_OptionalCreateReplicationTaskMessageTypeDef = TypedDict(
    "_OptionalCreateReplicationTaskMessageTypeDef",
    {
        "ReplicationTaskSettings": str,
        "CdcStartTime": Union[datetime, str],
        "CdcStartPosition": str,
        "CdcStopPosition": str,
        "Tags": List["TagTypeDef"],
        "TaskData": str,
        "ResourceIdentifier": str,
    },
    total=False,
)


class CreateReplicationTaskMessageTypeDef(
    _RequiredCreateReplicationTaskMessageTypeDef, _OptionalCreateReplicationTaskMessageTypeDef
):
    pass


CreateReplicationTaskResponseResponseTypeDef = TypedDict(
    "CreateReplicationTaskResponseResponseTypeDef",
    {
        "ReplicationTask": "ReplicationTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCertificateMessageTypeDef = TypedDict(
    "DeleteCertificateMessageTypeDef",
    {
        "CertificateArn": str,
    },
)

DeleteCertificateResponseResponseTypeDef = TypedDict(
    "DeleteCertificateResponseResponseTypeDef",
    {
        "Certificate": "CertificateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteConnectionMessageTypeDef = TypedDict(
    "DeleteConnectionMessageTypeDef",
    {
        "EndpointArn": str,
        "ReplicationInstanceArn": str,
    },
)

DeleteConnectionResponseResponseTypeDef = TypedDict(
    "DeleteConnectionResponseResponseTypeDef",
    {
        "Connection": "ConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEndpointMessageTypeDef = TypedDict(
    "DeleteEndpointMessageTypeDef",
    {
        "EndpointArn": str,
    },
)

DeleteEndpointResponseResponseTypeDef = TypedDict(
    "DeleteEndpointResponseResponseTypeDef",
    {
        "Endpoint": "EndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEventSubscriptionMessageTypeDef = TypedDict(
    "DeleteEventSubscriptionMessageTypeDef",
    {
        "SubscriptionName": str,
    },
)

DeleteEventSubscriptionResponseResponseTypeDef = TypedDict(
    "DeleteEventSubscriptionResponseResponseTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteReplicationInstanceMessageTypeDef = TypedDict(
    "DeleteReplicationInstanceMessageTypeDef",
    {
        "ReplicationInstanceArn": str,
    },
)

DeleteReplicationInstanceResponseResponseTypeDef = TypedDict(
    "DeleteReplicationInstanceResponseResponseTypeDef",
    {
        "ReplicationInstance": "ReplicationInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteReplicationSubnetGroupMessageTypeDef = TypedDict(
    "DeleteReplicationSubnetGroupMessageTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
    },
)

DeleteReplicationTaskAssessmentRunMessageTypeDef = TypedDict(
    "DeleteReplicationTaskAssessmentRunMessageTypeDef",
    {
        "ReplicationTaskAssessmentRunArn": str,
    },
)

DeleteReplicationTaskAssessmentRunResponseResponseTypeDef = TypedDict(
    "DeleteReplicationTaskAssessmentRunResponseResponseTypeDef",
    {
        "ReplicationTaskAssessmentRun": "ReplicationTaskAssessmentRunTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteReplicationTaskMessageTypeDef = TypedDict(
    "DeleteReplicationTaskMessageTypeDef",
    {
        "ReplicationTaskArn": str,
    },
)

DeleteReplicationTaskResponseResponseTypeDef = TypedDict(
    "DeleteReplicationTaskResponseResponseTypeDef",
    {
        "ReplicationTask": "ReplicationTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccountAttributesResponseResponseTypeDef = TypedDict(
    "DescribeAccountAttributesResponseResponseTypeDef",
    {
        "AccountQuotas": List["AccountQuotaTypeDef"],
        "UniqueAccountIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeApplicableIndividualAssessmentsMessageTypeDef = TypedDict(
    "DescribeApplicableIndividualAssessmentsMessageTypeDef",
    {
        "ReplicationTaskArn": str,
        "ReplicationInstanceArn": str,
        "SourceEngineName": str,
        "TargetEngineName": str,
        "MigrationType": MigrationTypeValueType,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeApplicableIndividualAssessmentsResponseResponseTypeDef = TypedDict(
    "DescribeApplicableIndividualAssessmentsResponseResponseTypeDef",
    {
        "IndividualAssessmentNames": List[str],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCertificatesMessageTypeDef = TypedDict(
    "DescribeCertificatesMessageTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeCertificatesResponseResponseTypeDef = TypedDict(
    "DescribeCertificatesResponseResponseTypeDef",
    {
        "Marker": str,
        "Certificates": List["CertificateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConnectionsMessageTypeDef = TypedDict(
    "DescribeConnectionsMessageTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeConnectionsResponseResponseTypeDef = TypedDict(
    "DescribeConnectionsResponseResponseTypeDef",
    {
        "Marker": str,
        "Connections": List["ConnectionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeEndpointSettingsMessageTypeDef = TypedDict(
    "_RequiredDescribeEndpointSettingsMessageTypeDef",
    {
        "EngineName": str,
    },
)
_OptionalDescribeEndpointSettingsMessageTypeDef = TypedDict(
    "_OptionalDescribeEndpointSettingsMessageTypeDef",
    {
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)


class DescribeEndpointSettingsMessageTypeDef(
    _RequiredDescribeEndpointSettingsMessageTypeDef, _OptionalDescribeEndpointSettingsMessageTypeDef
):
    pass


DescribeEndpointSettingsResponseResponseTypeDef = TypedDict(
    "DescribeEndpointSettingsResponseResponseTypeDef",
    {
        "Marker": str,
        "EndpointSettings": List["EndpointSettingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndpointTypesMessageTypeDef = TypedDict(
    "DescribeEndpointTypesMessageTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeEndpointTypesResponseResponseTypeDef = TypedDict(
    "DescribeEndpointTypesResponseResponseTypeDef",
    {
        "Marker": str,
        "SupportedEndpointTypes": List["SupportedEndpointTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndpointsMessageTypeDef = TypedDict(
    "DescribeEndpointsMessageTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeEndpointsResponseResponseTypeDef = TypedDict(
    "DescribeEndpointsResponseResponseTypeDef",
    {
        "Marker": str,
        "Endpoints": List["EndpointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventCategoriesMessageTypeDef = TypedDict(
    "DescribeEventCategoriesMessageTypeDef",
    {
        "SourceType": str,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

DescribeEventCategoriesResponseResponseTypeDef = TypedDict(
    "DescribeEventCategoriesResponseResponseTypeDef",
    {
        "EventCategoryGroupList": List["EventCategoryGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventSubscriptionsMessageTypeDef = TypedDict(
    "DescribeEventSubscriptionsMessageTypeDef",
    {
        "SubscriptionName": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeEventSubscriptionsResponseResponseTypeDef = TypedDict(
    "DescribeEventSubscriptionsResponseResponseTypeDef",
    {
        "Marker": str,
        "EventSubscriptionsList": List["EventSubscriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventsMessageTypeDef = TypedDict(
    "DescribeEventsMessageTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": Literal["replication-instance"],
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Duration": int,
        "EventCategories": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeEventsResponseResponseTypeDef = TypedDict(
    "DescribeEventsResponseResponseTypeDef",
    {
        "Marker": str,
        "Events": List["EventTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrderableReplicationInstancesMessageTypeDef = TypedDict(
    "DescribeOrderableReplicationInstancesMessageTypeDef",
    {
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeOrderableReplicationInstancesResponseResponseTypeDef = TypedDict(
    "DescribeOrderableReplicationInstancesResponseResponseTypeDef",
    {
        "OrderableReplicationInstances": List["OrderableReplicationInstanceTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePendingMaintenanceActionsMessageTypeDef = TypedDict(
    "DescribePendingMaintenanceActionsMessageTypeDef",
    {
        "ReplicationInstanceArn": str,
        "Filters": List["FilterTypeDef"],
        "Marker": str,
        "MaxRecords": int,
    },
    total=False,
)

DescribePendingMaintenanceActionsResponseResponseTypeDef = TypedDict(
    "DescribePendingMaintenanceActionsResponseResponseTypeDef",
    {
        "PendingMaintenanceActions": List["ResourcePendingMaintenanceActionsTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRefreshSchemasStatusMessageTypeDef = TypedDict(
    "DescribeRefreshSchemasStatusMessageTypeDef",
    {
        "EndpointArn": str,
    },
)

DescribeRefreshSchemasStatusResponseResponseTypeDef = TypedDict(
    "DescribeRefreshSchemasStatusResponseResponseTypeDef",
    {
        "RefreshSchemasStatus": "RefreshSchemasStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeReplicationInstanceTaskLogsMessageTypeDef = TypedDict(
    "_RequiredDescribeReplicationInstanceTaskLogsMessageTypeDef",
    {
        "ReplicationInstanceArn": str,
    },
)
_OptionalDescribeReplicationInstanceTaskLogsMessageTypeDef = TypedDict(
    "_OptionalDescribeReplicationInstanceTaskLogsMessageTypeDef",
    {
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)


class DescribeReplicationInstanceTaskLogsMessageTypeDef(
    _RequiredDescribeReplicationInstanceTaskLogsMessageTypeDef,
    _OptionalDescribeReplicationInstanceTaskLogsMessageTypeDef,
):
    pass


DescribeReplicationInstanceTaskLogsResponseResponseTypeDef = TypedDict(
    "DescribeReplicationInstanceTaskLogsResponseResponseTypeDef",
    {
        "ReplicationInstanceArn": str,
        "ReplicationInstanceTaskLogs": List["ReplicationInstanceTaskLogTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplicationInstancesMessageTypeDef = TypedDict(
    "DescribeReplicationInstancesMessageTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeReplicationInstancesResponseResponseTypeDef = TypedDict(
    "DescribeReplicationInstancesResponseResponseTypeDef",
    {
        "Marker": str,
        "ReplicationInstances": List["ReplicationInstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplicationSubnetGroupsMessageTypeDef = TypedDict(
    "DescribeReplicationSubnetGroupsMessageTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeReplicationSubnetGroupsResponseResponseTypeDef = TypedDict(
    "DescribeReplicationSubnetGroupsResponseResponseTypeDef",
    {
        "Marker": str,
        "ReplicationSubnetGroups": List["ReplicationSubnetGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplicationTaskAssessmentResultsMessageTypeDef = TypedDict(
    "DescribeReplicationTaskAssessmentResultsMessageTypeDef",
    {
        "ReplicationTaskArn": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeReplicationTaskAssessmentResultsResponseResponseTypeDef = TypedDict(
    "DescribeReplicationTaskAssessmentResultsResponseResponseTypeDef",
    {
        "Marker": str,
        "BucketName": str,
        "ReplicationTaskAssessmentResults": List["ReplicationTaskAssessmentResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplicationTaskAssessmentRunsMessageTypeDef = TypedDict(
    "DescribeReplicationTaskAssessmentRunsMessageTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeReplicationTaskAssessmentRunsResponseResponseTypeDef = TypedDict(
    "DescribeReplicationTaskAssessmentRunsResponseResponseTypeDef",
    {
        "Marker": str,
        "ReplicationTaskAssessmentRuns": List["ReplicationTaskAssessmentRunTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplicationTaskIndividualAssessmentsMessageTypeDef = TypedDict(
    "DescribeReplicationTaskIndividualAssessmentsMessageTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeReplicationTaskIndividualAssessmentsResponseResponseTypeDef = TypedDict(
    "DescribeReplicationTaskIndividualAssessmentsResponseResponseTypeDef",
    {
        "Marker": str,
        "ReplicationTaskIndividualAssessments": List["ReplicationTaskIndividualAssessmentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplicationTasksMessageTypeDef = TypedDict(
    "DescribeReplicationTasksMessageTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
        "WithoutSettings": bool,
    },
    total=False,
)

DescribeReplicationTasksResponseResponseTypeDef = TypedDict(
    "DescribeReplicationTasksResponseResponseTypeDef",
    {
        "Marker": str,
        "ReplicationTasks": List["ReplicationTaskTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeSchemasMessageTypeDef = TypedDict(
    "_RequiredDescribeSchemasMessageTypeDef",
    {
        "EndpointArn": str,
    },
)
_OptionalDescribeSchemasMessageTypeDef = TypedDict(
    "_OptionalDescribeSchemasMessageTypeDef",
    {
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)


class DescribeSchemasMessageTypeDef(
    _RequiredDescribeSchemasMessageTypeDef, _OptionalDescribeSchemasMessageTypeDef
):
    pass


DescribeSchemasResponseResponseTypeDef = TypedDict(
    "DescribeSchemasResponseResponseTypeDef",
    {
        "Marker": str,
        "Schemas": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeTableStatisticsMessageTypeDef = TypedDict(
    "_RequiredDescribeTableStatisticsMessageTypeDef",
    {
        "ReplicationTaskArn": str,
    },
)
_OptionalDescribeTableStatisticsMessageTypeDef = TypedDict(
    "_OptionalDescribeTableStatisticsMessageTypeDef",
    {
        "MaxRecords": int,
        "Marker": str,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)


class DescribeTableStatisticsMessageTypeDef(
    _RequiredDescribeTableStatisticsMessageTypeDef, _OptionalDescribeTableStatisticsMessageTypeDef
):
    pass


DescribeTableStatisticsResponseResponseTypeDef = TypedDict(
    "DescribeTableStatisticsResponseResponseTypeDef",
    {
        "ReplicationTaskArn": str,
        "TableStatistics": List["TableStatisticsTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DmsTransferSettingsTypeDef = TypedDict(
    "DmsTransferSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "BucketName": str,
    },
    total=False,
)

DocDbSettingsTypeDef = TypedDict(
    "DocDbSettingsTypeDef",
    {
        "Username": str,
        "Password": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "NestingLevel": NestingLevelValueType,
        "ExtractDocId": bool,
        "DocsToInvestigate": int,
        "KmsKeyId": str,
        "SecretsManagerAccessRoleArn": str,
        "SecretsManagerSecretId": str,
    },
    total=False,
)

DynamoDbSettingsTypeDef = TypedDict(
    "DynamoDbSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
    },
)

_RequiredElasticsearchSettingsTypeDef = TypedDict(
    "_RequiredElasticsearchSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "EndpointUri": str,
    },
)
_OptionalElasticsearchSettingsTypeDef = TypedDict(
    "_OptionalElasticsearchSettingsTypeDef",
    {
        "FullLoadErrorPercentage": int,
        "ErrorRetryDuration": int,
    },
    total=False,
)


class ElasticsearchSettingsTypeDef(
    _RequiredElasticsearchSettingsTypeDef, _OptionalElasticsearchSettingsTypeDef
):
    pass


EndpointSettingTypeDef = TypedDict(
    "EndpointSettingTypeDef",
    {
        "Name": str,
        "Type": EndpointSettingTypeValueType,
        "EnumValues": List[str],
        "Sensitive": bool,
        "Units": str,
        "Applicability": str,
        "IntValueMin": int,
        "IntValueMax": int,
    },
    total=False,
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "EndpointIdentifier": str,
        "EndpointType": ReplicationEndpointTypeValueType,
        "EngineName": str,
        "EngineDisplayName": str,
        "Username": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "ExtraConnectionAttributes": str,
        "Status": str,
        "KmsKeyId": str,
        "EndpointArn": str,
        "CertificateArn": str,
        "SslMode": DmsSslModeValueType,
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "ExternalId": str,
        "DynamoDbSettings": "DynamoDbSettingsTypeDef",
        "S3Settings": "S3SettingsTypeDef",
        "DmsTransferSettings": "DmsTransferSettingsTypeDef",
        "MongoDbSettings": "MongoDbSettingsTypeDef",
        "KinesisSettings": "KinesisSettingsTypeDef",
        "KafkaSettings": "KafkaSettingsTypeDef",
        "ElasticsearchSettings": "ElasticsearchSettingsTypeDef",
        "NeptuneSettings": "NeptuneSettingsTypeDef",
        "RedshiftSettings": "RedshiftSettingsTypeDef",
        "PostgreSQLSettings": "PostgreSQLSettingsTypeDef",
        "MySQLSettings": "MySQLSettingsTypeDef",
        "OracleSettings": "OracleSettingsTypeDef",
        "SybaseSettings": "SybaseSettingsTypeDef",
        "MicrosoftSQLServerSettings": "MicrosoftSQLServerSettingsTypeDef",
        "IBMDb2Settings": "IBMDb2SettingsTypeDef",
        "DocDbSettings": "DocDbSettingsTypeDef",
    },
    total=False,
)

EventCategoryGroupTypeDef = TypedDict(
    "EventCategoryGroupTypeDef",
    {
        "SourceType": str,
        "EventCategories": List[str],
    },
    total=False,
)

EventSubscriptionTypeDef = TypedDict(
    "EventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
    },
    total=False,
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": Literal["replication-instance"],
        "Message": str,
        "EventCategories": List[str],
        "Date": datetime,
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "Values": List[str],
    },
)

IBMDb2SettingsTypeDef = TypedDict(
    "IBMDb2SettingsTypeDef",
    {
        "DatabaseName": str,
        "Password": str,
        "Port": int,
        "ServerName": str,
        "SetDataCaptureChanges": bool,
        "CurrentLsn": str,
        "MaxKBytesPerRead": int,
        "Username": str,
        "SecretsManagerAccessRoleArn": str,
        "SecretsManagerSecretId": str,
    },
    total=False,
)

_RequiredImportCertificateMessageTypeDef = TypedDict(
    "_RequiredImportCertificateMessageTypeDef",
    {
        "CertificateIdentifier": str,
    },
)
_OptionalImportCertificateMessageTypeDef = TypedDict(
    "_OptionalImportCertificateMessageTypeDef",
    {
        "CertificatePem": str,
        "CertificateWallet": Union[bytes, IO[bytes], StreamingBody],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class ImportCertificateMessageTypeDef(
    _RequiredImportCertificateMessageTypeDef, _OptionalImportCertificateMessageTypeDef
):
    pass


ImportCertificateResponseResponseTypeDef = TypedDict(
    "ImportCertificateResponseResponseTypeDef",
    {
        "Certificate": "CertificateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

KafkaSettingsTypeDef = TypedDict(
    "KafkaSettingsTypeDef",
    {
        "Broker": str,
        "Topic": str,
        "MessageFormat": MessageFormatValueType,
        "IncludeTransactionDetails": bool,
        "IncludePartitionValue": bool,
        "PartitionIncludeSchemaTable": bool,
        "IncludeTableAlterOperations": bool,
        "IncludeControlDetails": bool,
        "MessageMaxBytes": int,
        "IncludeNullAndEmpty": bool,
        "SecurityProtocol": KafkaSecurityProtocolType,
        "SslClientCertificateArn": str,
        "SslClientKeyArn": str,
        "SslClientKeyPassword": str,
        "SslCaCertificateArn": str,
        "SaslUsername": str,
        "SaslPassword": str,
    },
    total=False,
)

KinesisSettingsTypeDef = TypedDict(
    "KinesisSettingsTypeDef",
    {
        "StreamArn": str,
        "MessageFormat": MessageFormatValueType,
        "ServiceAccessRoleArn": str,
        "IncludeTransactionDetails": bool,
        "IncludePartitionValue": bool,
        "PartitionIncludeSchemaTable": bool,
        "IncludeTableAlterOperations": bool,
        "IncludeControlDetails": bool,
        "IncludeNullAndEmpty": bool,
    },
    total=False,
)

ListTagsForResourceMessageTypeDef = TypedDict(
    "ListTagsForResourceMessageTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "TagList": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MicrosoftSQLServerSettingsTypeDef = TypedDict(
    "MicrosoftSQLServerSettingsTypeDef",
    {
        "Port": int,
        "BcpPacketSize": int,
        "DatabaseName": str,
        "ControlTablesFileGroup": str,
        "Password": str,
        "QuerySingleAlwaysOnNode": bool,
        "ReadBackupOnly": bool,
        "SafeguardPolicy": SafeguardPolicyType,
        "ServerName": str,
        "Username": str,
        "UseBcpFullLoad": bool,
        "UseThirdPartyBackupDevice": bool,
        "SecretsManagerAccessRoleArn": str,
        "SecretsManagerSecretId": str,
    },
    total=False,
)

_RequiredModifyEndpointMessageTypeDef = TypedDict(
    "_RequiredModifyEndpointMessageTypeDef",
    {
        "EndpointArn": str,
    },
)
_OptionalModifyEndpointMessageTypeDef = TypedDict(
    "_OptionalModifyEndpointMessageTypeDef",
    {
        "EndpointIdentifier": str,
        "EndpointType": ReplicationEndpointTypeValueType,
        "EngineName": str,
        "Username": str,
        "Password": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "ExtraConnectionAttributes": str,
        "CertificateArn": str,
        "SslMode": DmsSslModeValueType,
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "DynamoDbSettings": "DynamoDbSettingsTypeDef",
        "S3Settings": "S3SettingsTypeDef",
        "DmsTransferSettings": "DmsTransferSettingsTypeDef",
        "MongoDbSettings": "MongoDbSettingsTypeDef",
        "KinesisSettings": "KinesisSettingsTypeDef",
        "KafkaSettings": "KafkaSettingsTypeDef",
        "ElasticsearchSettings": "ElasticsearchSettingsTypeDef",
        "NeptuneSettings": "NeptuneSettingsTypeDef",
        "RedshiftSettings": "RedshiftSettingsTypeDef",
        "PostgreSQLSettings": "PostgreSQLSettingsTypeDef",
        "MySQLSettings": "MySQLSettingsTypeDef",
        "OracleSettings": "OracleSettingsTypeDef",
        "SybaseSettings": "SybaseSettingsTypeDef",
        "MicrosoftSQLServerSettings": "MicrosoftSQLServerSettingsTypeDef",
        "IBMDb2Settings": "IBMDb2SettingsTypeDef",
        "DocDbSettings": "DocDbSettingsTypeDef",
    },
    total=False,
)


class ModifyEndpointMessageTypeDef(
    _RequiredModifyEndpointMessageTypeDef, _OptionalModifyEndpointMessageTypeDef
):
    pass


ModifyEndpointResponseResponseTypeDef = TypedDict(
    "ModifyEndpointResponseResponseTypeDef",
    {
        "Endpoint": "EndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyEventSubscriptionMessageTypeDef = TypedDict(
    "_RequiredModifyEventSubscriptionMessageTypeDef",
    {
        "SubscriptionName": str,
    },
)
_OptionalModifyEventSubscriptionMessageTypeDef = TypedDict(
    "_OptionalModifyEventSubscriptionMessageTypeDef",
    {
        "SnsTopicArn": str,
        "SourceType": str,
        "EventCategories": List[str],
        "Enabled": bool,
    },
    total=False,
)


class ModifyEventSubscriptionMessageTypeDef(
    _RequiredModifyEventSubscriptionMessageTypeDef, _OptionalModifyEventSubscriptionMessageTypeDef
):
    pass


ModifyEventSubscriptionResponseResponseTypeDef = TypedDict(
    "ModifyEventSubscriptionResponseResponseTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyReplicationInstanceMessageTypeDef = TypedDict(
    "_RequiredModifyReplicationInstanceMessageTypeDef",
    {
        "ReplicationInstanceArn": str,
    },
)
_OptionalModifyReplicationInstanceMessageTypeDef = TypedDict(
    "_OptionalModifyReplicationInstanceMessageTypeDef",
    {
        "AllocatedStorage": int,
        "ApplyImmediately": bool,
        "ReplicationInstanceClass": str,
        "VpcSecurityGroupIds": List[str],
        "PreferredMaintenanceWindow": str,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AllowMajorVersionUpgrade": bool,
        "AutoMinorVersionUpgrade": bool,
        "ReplicationInstanceIdentifier": str,
    },
    total=False,
)


class ModifyReplicationInstanceMessageTypeDef(
    _RequiredModifyReplicationInstanceMessageTypeDef,
    _OptionalModifyReplicationInstanceMessageTypeDef,
):
    pass


ModifyReplicationInstanceResponseResponseTypeDef = TypedDict(
    "ModifyReplicationInstanceResponseResponseTypeDef",
    {
        "ReplicationInstance": "ReplicationInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyReplicationSubnetGroupMessageTypeDef = TypedDict(
    "_RequiredModifyReplicationSubnetGroupMessageTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "SubnetIds": List[str],
    },
)
_OptionalModifyReplicationSubnetGroupMessageTypeDef = TypedDict(
    "_OptionalModifyReplicationSubnetGroupMessageTypeDef",
    {
        "ReplicationSubnetGroupDescription": str,
    },
    total=False,
)


class ModifyReplicationSubnetGroupMessageTypeDef(
    _RequiredModifyReplicationSubnetGroupMessageTypeDef,
    _OptionalModifyReplicationSubnetGroupMessageTypeDef,
):
    pass


ModifyReplicationSubnetGroupResponseResponseTypeDef = TypedDict(
    "ModifyReplicationSubnetGroupResponseResponseTypeDef",
    {
        "ReplicationSubnetGroup": "ReplicationSubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyReplicationTaskMessageTypeDef = TypedDict(
    "_RequiredModifyReplicationTaskMessageTypeDef",
    {
        "ReplicationTaskArn": str,
    },
)
_OptionalModifyReplicationTaskMessageTypeDef = TypedDict(
    "_OptionalModifyReplicationTaskMessageTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "MigrationType": MigrationTypeValueType,
        "TableMappings": str,
        "ReplicationTaskSettings": str,
        "CdcStartTime": Union[datetime, str],
        "CdcStartPosition": str,
        "CdcStopPosition": str,
        "TaskData": str,
    },
    total=False,
)


class ModifyReplicationTaskMessageTypeDef(
    _RequiredModifyReplicationTaskMessageTypeDef, _OptionalModifyReplicationTaskMessageTypeDef
):
    pass


ModifyReplicationTaskResponseResponseTypeDef = TypedDict(
    "ModifyReplicationTaskResponseResponseTypeDef",
    {
        "ReplicationTask": "ReplicationTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MongoDbSettingsTypeDef = TypedDict(
    "MongoDbSettingsTypeDef",
    {
        "Username": str,
        "Password": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "AuthType": AuthTypeValueType,
        "AuthMechanism": AuthMechanismValueType,
        "NestingLevel": NestingLevelValueType,
        "ExtractDocId": str,
        "DocsToInvestigate": str,
        "AuthSource": str,
        "KmsKeyId": str,
        "SecretsManagerAccessRoleArn": str,
        "SecretsManagerSecretId": str,
    },
    total=False,
)

MoveReplicationTaskMessageTypeDef = TypedDict(
    "MoveReplicationTaskMessageTypeDef",
    {
        "ReplicationTaskArn": str,
        "TargetReplicationInstanceArn": str,
    },
)

MoveReplicationTaskResponseResponseTypeDef = TypedDict(
    "MoveReplicationTaskResponseResponseTypeDef",
    {
        "ReplicationTask": "ReplicationTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MySQLSettingsTypeDef = TypedDict(
    "MySQLSettingsTypeDef",
    {
        "AfterConnectScript": str,
        "CleanSourceMetadataOnMismatch": bool,
        "DatabaseName": str,
        "EventsPollInterval": int,
        "TargetDbType": TargetDbTypeType,
        "MaxFileSize": int,
        "ParallelLoadThreads": int,
        "Password": str,
        "Port": int,
        "ServerName": str,
        "ServerTimezone": str,
        "Username": str,
        "SecretsManagerAccessRoleArn": str,
        "SecretsManagerSecretId": str,
    },
    total=False,
)

_RequiredNeptuneSettingsTypeDef = TypedDict(
    "_RequiredNeptuneSettingsTypeDef",
    {
        "S3BucketName": str,
        "S3BucketFolder": str,
    },
)
_OptionalNeptuneSettingsTypeDef = TypedDict(
    "_OptionalNeptuneSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "ErrorRetryDuration": int,
        "MaxFileSize": int,
        "MaxRetryCount": int,
        "IamAuthEnabled": bool,
    },
    total=False,
)


class NeptuneSettingsTypeDef(_RequiredNeptuneSettingsTypeDef, _OptionalNeptuneSettingsTypeDef):
    pass


OracleSettingsTypeDef = TypedDict(
    "OracleSettingsTypeDef",
    {
        "AddSupplementalLogging": bool,
        "ArchivedLogDestId": int,
        "AdditionalArchivedLogDestId": int,
        "AllowSelectNestedTables": bool,
        "ParallelAsmReadThreads": int,
        "ReadAheadBlocks": int,
        "AccessAlternateDirectly": bool,
        "UseAlternateFolderForOnline": bool,
        "OraclePathPrefix": str,
        "UsePathPrefix": str,
        "ReplacePathPrefix": bool,
        "EnableHomogenousTablespace": bool,
        "DirectPathNoLog": bool,
        "ArchivedLogsOnly": bool,
        "AsmPassword": str,
        "AsmServer": str,
        "AsmUser": str,
        "CharLengthSemantics": CharLengthSemanticsType,
        "DatabaseName": str,
        "DirectPathParallelLoad": bool,
        "FailTasksOnLobTruncation": bool,
        "NumberDatatypeScale": int,
        "Password": str,
        "Port": int,
        "ReadTableSpaceName": bool,
        "RetryInterval": int,
        "SecurityDbEncryption": str,
        "SecurityDbEncryptionName": str,
        "ServerName": str,
        "SpatialDataOptionToGeoJsonFunctionName": str,
        "Username": str,
        "SecretsManagerAccessRoleArn": str,
        "SecretsManagerSecretId": str,
        "SecretsManagerOracleAsmAccessRoleArn": str,
        "SecretsManagerOracleAsmSecretId": str,
    },
    total=False,
)

OrderableReplicationInstanceTypeDef = TypedDict(
    "OrderableReplicationInstanceTypeDef",
    {
        "EngineVersion": str,
        "ReplicationInstanceClass": str,
        "StorageType": str,
        "MinAllocatedStorage": int,
        "MaxAllocatedStorage": int,
        "DefaultAllocatedStorage": int,
        "IncludedAllocatedStorage": int,
        "AvailabilityZones": List[str],
        "ReleaseStatus": Literal["beta"],
    },
    total=False,
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

PendingMaintenanceActionTypeDef = TypedDict(
    "PendingMaintenanceActionTypeDef",
    {
        "Action": str,
        "AutoAppliedAfterDate": datetime,
        "ForcedApplyDate": datetime,
        "OptInStatus": str,
        "CurrentApplyDate": datetime,
        "Description": str,
    },
    total=False,
)

PostgreSQLSettingsTypeDef = TypedDict(
    "PostgreSQLSettingsTypeDef",
    {
        "AfterConnectScript": str,
        "CaptureDdls": bool,
        "MaxFileSize": int,
        "DatabaseName": str,
        "DdlArtifactsSchema": str,
        "ExecuteTimeout": int,
        "FailTasksOnLobTruncation": bool,
        "Password": str,
        "Port": int,
        "ServerName": str,
        "Username": str,
        "SlotName": str,
        "SecretsManagerAccessRoleArn": str,
        "SecretsManagerSecretId": str,
    },
    total=False,
)

_RequiredRebootReplicationInstanceMessageTypeDef = TypedDict(
    "_RequiredRebootReplicationInstanceMessageTypeDef",
    {
        "ReplicationInstanceArn": str,
    },
)
_OptionalRebootReplicationInstanceMessageTypeDef = TypedDict(
    "_OptionalRebootReplicationInstanceMessageTypeDef",
    {
        "ForceFailover": bool,
    },
    total=False,
)


class RebootReplicationInstanceMessageTypeDef(
    _RequiredRebootReplicationInstanceMessageTypeDef,
    _OptionalRebootReplicationInstanceMessageTypeDef,
):
    pass


RebootReplicationInstanceResponseResponseTypeDef = TypedDict(
    "RebootReplicationInstanceResponseResponseTypeDef",
    {
        "ReplicationInstance": "ReplicationInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RedshiftSettingsTypeDef = TypedDict(
    "RedshiftSettingsTypeDef",
    {
        "AcceptAnyDate": bool,
        "AfterConnectScript": str,
        "BucketFolder": str,
        "BucketName": str,
        "CaseSensitiveNames": bool,
        "CompUpdate": bool,
        "ConnectionTimeout": int,
        "DatabaseName": str,
        "DateFormat": str,
        "EmptyAsNull": bool,
        "EncryptionMode": EncryptionModeValueType,
        "ExplicitIds": bool,
        "FileTransferUploadStreams": int,
        "LoadTimeout": int,
        "MaxFileSize": int,
        "Password": str,
        "Port": int,
        "RemoveQuotes": bool,
        "ReplaceInvalidChars": str,
        "ReplaceChars": str,
        "ServerName": str,
        "ServiceAccessRoleArn": str,
        "ServerSideEncryptionKmsKeyId": str,
        "TimeFormat": str,
        "TrimBlanks": bool,
        "TruncateColumns": bool,
        "Username": str,
        "WriteBufferSize": int,
        "SecretsManagerAccessRoleArn": str,
        "SecretsManagerSecretId": str,
    },
    total=False,
)

RefreshSchemasMessageTypeDef = TypedDict(
    "RefreshSchemasMessageTypeDef",
    {
        "EndpointArn": str,
        "ReplicationInstanceArn": str,
    },
)

RefreshSchemasResponseResponseTypeDef = TypedDict(
    "RefreshSchemasResponseResponseTypeDef",
    {
        "RefreshSchemasStatus": "RefreshSchemasStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RefreshSchemasStatusTypeDef = TypedDict(
    "RefreshSchemasStatusTypeDef",
    {
        "EndpointArn": str,
        "ReplicationInstanceArn": str,
        "Status": RefreshSchemasStatusTypeValueType,
        "LastRefreshDate": datetime,
        "LastFailureMessage": str,
    },
    total=False,
)

_RequiredReloadTablesMessageTypeDef = TypedDict(
    "_RequiredReloadTablesMessageTypeDef",
    {
        "ReplicationTaskArn": str,
        "TablesToReload": List["TableToReloadTypeDef"],
    },
)
_OptionalReloadTablesMessageTypeDef = TypedDict(
    "_OptionalReloadTablesMessageTypeDef",
    {
        "ReloadOption": ReloadOptionValueType,
    },
    total=False,
)


class ReloadTablesMessageTypeDef(
    _RequiredReloadTablesMessageTypeDef, _OptionalReloadTablesMessageTypeDef
):
    pass


ReloadTablesResponseResponseTypeDef = TypedDict(
    "ReloadTablesResponseResponseTypeDef",
    {
        "ReplicationTaskArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveTagsFromResourceMessageTypeDef = TypedDict(
    "RemoveTagsFromResourceMessageTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

ReplicationInstanceTaskLogTypeDef = TypedDict(
    "ReplicationInstanceTaskLogTypeDef",
    {
        "ReplicationTaskName": str,
        "ReplicationTaskArn": str,
        "ReplicationInstanceTaskLogSize": int,
    },
    total=False,
)

ReplicationInstanceTypeDef = TypedDict(
    "ReplicationInstanceTypeDef",
    {
        "ReplicationInstanceIdentifier": str,
        "ReplicationInstanceClass": str,
        "ReplicationInstanceStatus": str,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "VpcSecurityGroups": List["VpcSecurityGroupMembershipTypeDef"],
        "AvailabilityZone": str,
        "ReplicationSubnetGroup": "ReplicationSubnetGroupTypeDef",
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": "ReplicationPendingModifiedValuesTypeDef",
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "KmsKeyId": str,
        "ReplicationInstanceArn": str,
        "ReplicationInstancePublicIpAddress": str,
        "ReplicationInstancePrivateIpAddress": str,
        "ReplicationInstancePublicIpAddresses": List[str],
        "ReplicationInstancePrivateIpAddresses": List[str],
        "PubliclyAccessible": bool,
        "SecondaryAvailabilityZone": str,
        "FreeUntil": datetime,
        "DnsNameServers": str,
    },
    total=False,
)

ReplicationPendingModifiedValuesTypeDef = TypedDict(
    "ReplicationPendingModifiedValuesTypeDef",
    {
        "ReplicationInstanceClass": str,
        "AllocatedStorage": int,
        "MultiAZ": bool,
        "EngineVersion": str,
    },
    total=False,
)

ReplicationSubnetGroupTypeDef = TypedDict(
    "ReplicationSubnetGroupTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List["SubnetTypeDef"],
    },
    total=False,
)

ReplicationTaskAssessmentResultTypeDef = TypedDict(
    "ReplicationTaskAssessmentResultTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "ReplicationTaskArn": str,
        "ReplicationTaskLastAssessmentDate": datetime,
        "AssessmentStatus": str,
        "AssessmentResultsFile": str,
        "AssessmentResults": str,
        "S3ObjectUrl": str,
    },
    total=False,
)

ReplicationTaskAssessmentRunProgressTypeDef = TypedDict(
    "ReplicationTaskAssessmentRunProgressTypeDef",
    {
        "IndividualAssessmentCount": int,
        "IndividualAssessmentCompletedCount": int,
    },
    total=False,
)

ReplicationTaskAssessmentRunTypeDef = TypedDict(
    "ReplicationTaskAssessmentRunTypeDef",
    {
        "ReplicationTaskAssessmentRunArn": str,
        "ReplicationTaskArn": str,
        "Status": str,
        "ReplicationTaskAssessmentRunCreationDate": datetime,
        "AssessmentProgress": "ReplicationTaskAssessmentRunProgressTypeDef",
        "LastFailureMessage": str,
        "ServiceAccessRoleArn": str,
        "ResultLocationBucket": str,
        "ResultLocationFolder": str,
        "ResultEncryptionMode": str,
        "ResultKmsKeyArn": str,
        "AssessmentRunName": str,
    },
    total=False,
)

ReplicationTaskIndividualAssessmentTypeDef = TypedDict(
    "ReplicationTaskIndividualAssessmentTypeDef",
    {
        "ReplicationTaskIndividualAssessmentArn": str,
        "ReplicationTaskAssessmentRunArn": str,
        "IndividualAssessmentName": str,
        "Status": str,
        "ReplicationTaskIndividualAssessmentStartDate": datetime,
    },
    total=False,
)

ReplicationTaskStatsTypeDef = TypedDict(
    "ReplicationTaskStatsTypeDef",
    {
        "FullLoadProgressPercent": int,
        "ElapsedTimeMillis": int,
        "TablesLoaded": int,
        "TablesLoading": int,
        "TablesQueued": int,
        "TablesErrored": int,
        "FreshStartDate": datetime,
        "StartDate": datetime,
        "StopDate": datetime,
        "FullLoadStartDate": datetime,
        "FullLoadFinishDate": datetime,
    },
    total=False,
)

ReplicationTaskTypeDef = TypedDict(
    "ReplicationTaskTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "SourceEndpointArn": str,
        "TargetEndpointArn": str,
        "ReplicationInstanceArn": str,
        "MigrationType": MigrationTypeValueType,
        "TableMappings": str,
        "ReplicationTaskSettings": str,
        "Status": str,
        "LastFailureMessage": str,
        "StopReason": str,
        "ReplicationTaskCreationDate": datetime,
        "ReplicationTaskStartDate": datetime,
        "CdcStartPosition": str,
        "CdcStopPosition": str,
        "RecoveryCheckpoint": str,
        "ReplicationTaskArn": str,
        "ReplicationTaskStats": "ReplicationTaskStatsTypeDef",
        "TaskData": str,
        "TargetReplicationInstanceArn": str,
    },
    total=False,
)

ResourcePendingMaintenanceActionsTypeDef = TypedDict(
    "ResourcePendingMaintenanceActionsTypeDef",
    {
        "ResourceIdentifier": str,
        "PendingMaintenanceActionDetails": List["PendingMaintenanceActionTypeDef"],
    },
    total=False,
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

S3SettingsTypeDef = TypedDict(
    "S3SettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "CsvRowDelimiter": str,
        "CsvDelimiter": str,
        "BucketFolder": str,
        "BucketName": str,
        "CompressionType": CompressionTypeValueType,
        "EncryptionMode": EncryptionModeValueType,
        "ServerSideEncryptionKmsKeyId": str,
        "DataFormat": DataFormatValueType,
        "EncodingType": EncodingTypeValueType,
        "DictPageSizeLimit": int,
        "RowGroupLength": int,
        "DataPageSize": int,
        "ParquetVersion": ParquetVersionValueType,
        "EnableStatistics": bool,
        "IncludeOpForFullLoad": bool,
        "CdcInsertsOnly": bool,
        "TimestampColumnName": str,
        "ParquetTimestampInMillisecond": bool,
        "CdcInsertsAndUpdates": bool,
        "DatePartitionEnabled": bool,
        "DatePartitionSequence": DatePartitionSequenceValueType,
        "DatePartitionDelimiter": DatePartitionDelimiterValueType,
        "UseCsvNoSupValue": bool,
        "CsvNoSupValue": str,
        "PreserveTransactions": bool,
        "CdcPath": str,
    },
    total=False,
)

StartReplicationTaskAssessmentMessageTypeDef = TypedDict(
    "StartReplicationTaskAssessmentMessageTypeDef",
    {
        "ReplicationTaskArn": str,
    },
)

StartReplicationTaskAssessmentResponseResponseTypeDef = TypedDict(
    "StartReplicationTaskAssessmentResponseResponseTypeDef",
    {
        "ReplicationTask": "ReplicationTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartReplicationTaskAssessmentRunMessageTypeDef = TypedDict(
    "_RequiredStartReplicationTaskAssessmentRunMessageTypeDef",
    {
        "ReplicationTaskArn": str,
        "ServiceAccessRoleArn": str,
        "ResultLocationBucket": str,
        "AssessmentRunName": str,
    },
)
_OptionalStartReplicationTaskAssessmentRunMessageTypeDef = TypedDict(
    "_OptionalStartReplicationTaskAssessmentRunMessageTypeDef",
    {
        "ResultLocationFolder": str,
        "ResultEncryptionMode": str,
        "ResultKmsKeyArn": str,
        "IncludeOnly": List[str],
        "Exclude": List[str],
    },
    total=False,
)


class StartReplicationTaskAssessmentRunMessageTypeDef(
    _RequiredStartReplicationTaskAssessmentRunMessageTypeDef,
    _OptionalStartReplicationTaskAssessmentRunMessageTypeDef,
):
    pass


StartReplicationTaskAssessmentRunResponseResponseTypeDef = TypedDict(
    "StartReplicationTaskAssessmentRunResponseResponseTypeDef",
    {
        "ReplicationTaskAssessmentRun": "ReplicationTaskAssessmentRunTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartReplicationTaskMessageTypeDef = TypedDict(
    "_RequiredStartReplicationTaskMessageTypeDef",
    {
        "ReplicationTaskArn": str,
        "StartReplicationTaskType": StartReplicationTaskTypeValueType,
    },
)
_OptionalStartReplicationTaskMessageTypeDef = TypedDict(
    "_OptionalStartReplicationTaskMessageTypeDef",
    {
        "CdcStartTime": Union[datetime, str],
        "CdcStartPosition": str,
        "CdcStopPosition": str,
    },
    total=False,
)


class StartReplicationTaskMessageTypeDef(
    _RequiredStartReplicationTaskMessageTypeDef, _OptionalStartReplicationTaskMessageTypeDef
):
    pass


StartReplicationTaskResponseResponseTypeDef = TypedDict(
    "StartReplicationTaskResponseResponseTypeDef",
    {
        "ReplicationTask": "ReplicationTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopReplicationTaskMessageTypeDef = TypedDict(
    "StopReplicationTaskMessageTypeDef",
    {
        "ReplicationTaskArn": str,
    },
)

StopReplicationTaskResponseResponseTypeDef = TypedDict(
    "StopReplicationTaskResponseResponseTypeDef",
    {
        "ReplicationTask": "ReplicationTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubnetTypeDef = TypedDict(
    "SubnetTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": "AvailabilityZoneTypeDef",
        "SubnetStatus": str,
    },
    total=False,
)

SupportedEndpointTypeTypeDef = TypedDict(
    "SupportedEndpointTypeTypeDef",
    {
        "EngineName": str,
        "SupportsCDC": bool,
        "EndpointType": ReplicationEndpointTypeValueType,
        "ReplicationInstanceEngineMinimumVersion": str,
        "EngineDisplayName": str,
    },
    total=False,
)

SybaseSettingsTypeDef = TypedDict(
    "SybaseSettingsTypeDef",
    {
        "DatabaseName": str,
        "Password": str,
        "Port": int,
        "ServerName": str,
        "Username": str,
        "SecretsManagerAccessRoleArn": str,
        "SecretsManagerSecretId": str,
    },
    total=False,
)

TableStatisticsTypeDef = TypedDict(
    "TableStatisticsTypeDef",
    {
        "SchemaName": str,
        "TableName": str,
        "Inserts": int,
        "Deletes": int,
        "Updates": int,
        "Ddls": int,
        "FullLoadRows": int,
        "FullLoadCondtnlChkFailedRows": int,
        "FullLoadErrorRows": int,
        "FullLoadStartTime": datetime,
        "FullLoadEndTime": datetime,
        "FullLoadReloaded": bool,
        "LastUpdateTime": datetime,
        "TableState": str,
        "ValidationPendingRecords": int,
        "ValidationFailedRecords": int,
        "ValidationSuspendedRecords": int,
        "ValidationState": str,
        "ValidationStateDetails": str,
    },
    total=False,
)

TableToReloadTypeDef = TypedDict(
    "TableToReloadTypeDef",
    {
        "SchemaName": str,
        "TableName": str,
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

TestConnectionMessageTypeDef = TypedDict(
    "TestConnectionMessageTypeDef",
    {
        "ReplicationInstanceArn": str,
        "EndpointArn": str,
    },
)

TestConnectionResponseResponseTypeDef = TypedDict(
    "TestConnectionResponseResponseTypeDef",
    {
        "Connection": "ConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcSecurityGroupMembershipTypeDef = TypedDict(
    "VpcSecurityGroupMembershipTypeDef",
    {
        "VpcSecurityGroupId": str,
        "Status": str,
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
