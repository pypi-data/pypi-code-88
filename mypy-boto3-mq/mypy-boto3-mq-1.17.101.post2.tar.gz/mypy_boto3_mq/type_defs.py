"""
Type annotations for mq service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mq.type_defs import AvailabilityZoneTypeDef

    data: AvailabilityZoneTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AuthenticationStrategyType,
    BrokerStateType,
    BrokerStorageTypeType,
    ChangeTypeType,
    DayOfWeekType,
    DeploymentModeType,
    EngineTypeType,
    SanitizationWarningReasonType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AvailabilityZoneTypeDef",
    "BrokerEngineTypeTypeDef",
    "BrokerInstanceOptionTypeDef",
    "BrokerInstanceTypeDef",
    "BrokerSummaryTypeDef",
    "ConfigurationIdTypeDef",
    "ConfigurationRevisionTypeDef",
    "ConfigurationTypeDef",
    "ConfigurationsTypeDef",
    "CreateBrokerRequestRequestTypeDef",
    "CreateBrokerResponseTypeDef",
    "CreateConfigurationRequestRequestTypeDef",
    "CreateConfigurationResponseTypeDef",
    "CreateTagsRequestRequestTypeDef",
    "CreateUserRequestRequestTypeDef",
    "DeleteBrokerRequestRequestTypeDef",
    "DeleteBrokerResponseTypeDef",
    "DeleteTagsRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DescribeBrokerEngineTypesRequestRequestTypeDef",
    "DescribeBrokerEngineTypesResponseTypeDef",
    "DescribeBrokerInstanceOptionsRequestRequestTypeDef",
    "DescribeBrokerInstanceOptionsResponseTypeDef",
    "DescribeBrokerRequestRequestTypeDef",
    "DescribeBrokerResponseTypeDef",
    "DescribeConfigurationRequestRequestTypeDef",
    "DescribeConfigurationResponseTypeDef",
    "DescribeConfigurationRevisionRequestRequestTypeDef",
    "DescribeConfigurationRevisionResponseTypeDef",
    "DescribeUserRequestRequestTypeDef",
    "DescribeUserResponseTypeDef",
    "EncryptionOptionsTypeDef",
    "EngineVersionTypeDef",
    "LdapServerMetadataInputTypeDef",
    "LdapServerMetadataOutputTypeDef",
    "ListBrokersRequestRequestTypeDef",
    "ListBrokersResponseTypeDef",
    "ListConfigurationRevisionsRequestRequestTypeDef",
    "ListConfigurationRevisionsResponseTypeDef",
    "ListConfigurationsRequestRequestTypeDef",
    "ListConfigurationsResponseTypeDef",
    "ListTagsRequestRequestTypeDef",
    "ListTagsResponseTypeDef",
    "ListUsersRequestRequestTypeDef",
    "ListUsersResponseTypeDef",
    "LogsSummaryTypeDef",
    "LogsTypeDef",
    "PaginatorConfigTypeDef",
    "PendingLogsTypeDef",
    "RebootBrokerRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "SanitizationWarningTypeDef",
    "UpdateBrokerRequestRequestTypeDef",
    "UpdateBrokerResponseTypeDef",
    "UpdateConfigurationRequestRequestTypeDef",
    "UpdateConfigurationResponseTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "UserPendingChangesTypeDef",
    "UserSummaryTypeDef",
    "UserTypeDef",
    "WeeklyStartTimeTypeDef",
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "Name": str,
    },
    total=False,
)

BrokerEngineTypeTypeDef = TypedDict(
    "BrokerEngineTypeTypeDef",
    {
        "EngineType": EngineTypeType,
        "EngineVersions": List["EngineVersionTypeDef"],
    },
    total=False,
)

BrokerInstanceOptionTypeDef = TypedDict(
    "BrokerInstanceOptionTypeDef",
    {
        "AvailabilityZones": List["AvailabilityZoneTypeDef"],
        "EngineType": EngineTypeType,
        "HostInstanceType": str,
        "StorageType": BrokerStorageTypeType,
        "SupportedDeploymentModes": List[DeploymentModeType],
        "SupportedEngineVersions": List[str],
    },
    total=False,
)

BrokerInstanceTypeDef = TypedDict(
    "BrokerInstanceTypeDef",
    {
        "ConsoleURL": str,
        "Endpoints": List[str],
        "IpAddress": str,
    },
    total=False,
)

BrokerSummaryTypeDef = TypedDict(
    "BrokerSummaryTypeDef",
    {
        "BrokerArn": str,
        "BrokerId": str,
        "BrokerName": str,
        "BrokerState": BrokerStateType,
        "Created": datetime,
        "DeploymentMode": DeploymentModeType,
        "EngineType": EngineTypeType,
        "HostInstanceType": str,
    },
    total=False,
)

ConfigurationIdTypeDef = TypedDict(
    "ConfigurationIdTypeDef",
    {
        "Id": str,
        "Revision": int,
    },
    total=False,
)

ConfigurationRevisionTypeDef = TypedDict(
    "ConfigurationRevisionTypeDef",
    {
        "Created": datetime,
        "Description": str,
        "Revision": int,
    },
    total=False,
)

ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "Arn": str,
        "AuthenticationStrategy": AuthenticationStrategyType,
        "Created": datetime,
        "Description": str,
        "EngineType": EngineTypeType,
        "EngineVersion": str,
        "Id": str,
        "LatestRevision": "ConfigurationRevisionTypeDef",
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ConfigurationsTypeDef = TypedDict(
    "ConfigurationsTypeDef",
    {
        "Current": "ConfigurationIdTypeDef",
        "History": List["ConfigurationIdTypeDef"],
        "Pending": "ConfigurationIdTypeDef",
    },
    total=False,
)

CreateBrokerRequestRequestTypeDef = TypedDict(
    "CreateBrokerRequestRequestTypeDef",
    {
        "AuthenticationStrategy": AuthenticationStrategyType,
        "AutoMinorVersionUpgrade": bool,
        "BrokerName": str,
        "Configuration": "ConfigurationIdTypeDef",
        "CreatorRequestId": str,
        "DeploymentMode": DeploymentModeType,
        "EncryptionOptions": "EncryptionOptionsTypeDef",
        "EngineType": EngineTypeType,
        "EngineVersion": str,
        "HostInstanceType": str,
        "LdapServerMetadata": "LdapServerMetadataInputTypeDef",
        "Logs": "LogsTypeDef",
        "MaintenanceWindowStartTime": "WeeklyStartTimeTypeDef",
        "PubliclyAccessible": bool,
        "SecurityGroups": List[str],
        "StorageType": BrokerStorageTypeType,
        "SubnetIds": List[str],
        "Tags": Dict[str, str],
        "Users": List["UserTypeDef"],
    },
    total=False,
)

CreateBrokerResponseTypeDef = TypedDict(
    "CreateBrokerResponseTypeDef",
    {
        "BrokerArn": str,
        "BrokerId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateConfigurationRequestRequestTypeDef = TypedDict(
    "CreateConfigurationRequestRequestTypeDef",
    {
        "AuthenticationStrategy": AuthenticationStrategyType,
        "EngineType": EngineTypeType,
        "EngineVersion": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

CreateConfigurationResponseTypeDef = TypedDict(
    "CreateConfigurationResponseTypeDef",
    {
        "Arn": str,
        "AuthenticationStrategy": AuthenticationStrategyType,
        "Created": datetime,
        "Id": str,
        "LatestRevision": "ConfigurationRevisionTypeDef",
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTagsRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTagsRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalCreateTagsRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTagsRequestRequestTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateTagsRequestRequestTypeDef(
    _RequiredCreateTagsRequestRequestTypeDef, _OptionalCreateTagsRequestRequestTypeDef
):
    pass


_RequiredCreateUserRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserRequestRequestTypeDef",
    {
        "BrokerId": str,
        "Username": str,
    },
)
_OptionalCreateUserRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserRequestRequestTypeDef",
    {
        "ConsoleAccess": bool,
        "Groups": List[str],
        "Password": str,
    },
    total=False,
)


class CreateUserRequestRequestTypeDef(
    _RequiredCreateUserRequestRequestTypeDef, _OptionalCreateUserRequestRequestTypeDef
):
    pass


DeleteBrokerRequestRequestTypeDef = TypedDict(
    "DeleteBrokerRequestRequestTypeDef",
    {
        "BrokerId": str,
    },
)

DeleteBrokerResponseTypeDef = TypedDict(
    "DeleteBrokerResponseTypeDef",
    {
        "BrokerId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTagsRequestRequestTypeDef = TypedDict(
    "DeleteTagsRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "BrokerId": str,
        "Username": str,
    },
)

DescribeBrokerEngineTypesRequestRequestTypeDef = TypedDict(
    "DescribeBrokerEngineTypesRequestRequestTypeDef",
    {
        "EngineType": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeBrokerEngineTypesResponseTypeDef = TypedDict(
    "DescribeBrokerEngineTypesResponseTypeDef",
    {
        "BrokerEngineTypes": List["BrokerEngineTypeTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBrokerInstanceOptionsRequestRequestTypeDef = TypedDict(
    "DescribeBrokerInstanceOptionsRequestRequestTypeDef",
    {
        "EngineType": str,
        "HostInstanceType": str,
        "MaxResults": int,
        "NextToken": str,
        "StorageType": str,
    },
    total=False,
)

DescribeBrokerInstanceOptionsResponseTypeDef = TypedDict(
    "DescribeBrokerInstanceOptionsResponseTypeDef",
    {
        "BrokerInstanceOptions": List["BrokerInstanceOptionTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBrokerRequestRequestTypeDef = TypedDict(
    "DescribeBrokerRequestRequestTypeDef",
    {
        "BrokerId": str,
    },
)

DescribeBrokerResponseTypeDef = TypedDict(
    "DescribeBrokerResponseTypeDef",
    {
        "AuthenticationStrategy": AuthenticationStrategyType,
        "AutoMinorVersionUpgrade": bool,
        "BrokerArn": str,
        "BrokerId": str,
        "BrokerInstances": List["BrokerInstanceTypeDef"],
        "BrokerName": str,
        "BrokerState": BrokerStateType,
        "Configurations": "ConfigurationsTypeDef",
        "Created": datetime,
        "DeploymentMode": DeploymentModeType,
        "EncryptionOptions": "EncryptionOptionsTypeDef",
        "EngineType": EngineTypeType,
        "EngineVersion": str,
        "HostInstanceType": str,
        "LdapServerMetadata": "LdapServerMetadataOutputTypeDef",
        "Logs": "LogsSummaryTypeDef",
        "MaintenanceWindowStartTime": "WeeklyStartTimeTypeDef",
        "PendingAuthenticationStrategy": AuthenticationStrategyType,
        "PendingEngineVersion": str,
        "PendingHostInstanceType": str,
        "PendingLdapServerMetadata": "LdapServerMetadataOutputTypeDef",
        "PendingSecurityGroups": List[str],
        "PubliclyAccessible": bool,
        "SecurityGroups": List[str],
        "StorageType": BrokerStorageTypeType,
        "SubnetIds": List[str],
        "Tags": Dict[str, str],
        "Users": List["UserSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationRequestRequestTypeDef",
    {
        "ConfigurationId": str,
    },
)

DescribeConfigurationResponseTypeDef = TypedDict(
    "DescribeConfigurationResponseTypeDef",
    {
        "Arn": str,
        "AuthenticationStrategy": AuthenticationStrategyType,
        "Created": datetime,
        "Description": str,
        "EngineType": EngineTypeType,
        "EngineVersion": str,
        "Id": str,
        "LatestRevision": "ConfigurationRevisionTypeDef",
        "Name": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigurationRevisionRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationRevisionRequestRequestTypeDef",
    {
        "ConfigurationId": str,
        "ConfigurationRevision": str,
    },
)

DescribeConfigurationRevisionResponseTypeDef = TypedDict(
    "DescribeConfigurationRevisionResponseTypeDef",
    {
        "ConfigurationId": str,
        "Created": datetime,
        "Data": str,
        "Description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserRequestRequestTypeDef = TypedDict(
    "DescribeUserRequestRequestTypeDef",
    {
        "BrokerId": str,
        "Username": str,
    },
)

DescribeUserResponseTypeDef = TypedDict(
    "DescribeUserResponseTypeDef",
    {
        "BrokerId": str,
        "ConsoleAccess": bool,
        "Groups": List[str],
        "Pending": "UserPendingChangesTypeDef",
        "Username": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEncryptionOptionsTypeDef = TypedDict(
    "_RequiredEncryptionOptionsTypeDef",
    {
        "UseAwsOwnedKey": bool,
    },
)
_OptionalEncryptionOptionsTypeDef = TypedDict(
    "_OptionalEncryptionOptionsTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)


class EncryptionOptionsTypeDef(
    _RequiredEncryptionOptionsTypeDef, _OptionalEncryptionOptionsTypeDef
):
    pass


EngineVersionTypeDef = TypedDict(
    "EngineVersionTypeDef",
    {
        "Name": str,
    },
    total=False,
)

LdapServerMetadataInputTypeDef = TypedDict(
    "LdapServerMetadataInputTypeDef",
    {
        "Hosts": List[str],
        "RoleBase": str,
        "RoleName": str,
        "RoleSearchMatching": str,
        "RoleSearchSubtree": bool,
        "ServiceAccountPassword": str,
        "ServiceAccountUsername": str,
        "UserBase": str,
        "UserRoleName": str,
        "UserSearchMatching": str,
        "UserSearchSubtree": bool,
    },
    total=False,
)

LdapServerMetadataOutputTypeDef = TypedDict(
    "LdapServerMetadataOutputTypeDef",
    {
        "Hosts": List[str],
        "RoleBase": str,
        "RoleName": str,
        "RoleSearchMatching": str,
        "RoleSearchSubtree": bool,
        "ServiceAccountUsername": str,
        "UserBase": str,
        "UserRoleName": str,
        "UserSearchMatching": str,
        "UserSearchSubtree": bool,
    },
    total=False,
)

ListBrokersRequestRequestTypeDef = TypedDict(
    "ListBrokersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListBrokersResponseTypeDef = TypedDict(
    "ListBrokersResponseTypeDef",
    {
        "BrokerSummaries": List["BrokerSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListConfigurationRevisionsRequestRequestTypeDef = TypedDict(
    "_RequiredListConfigurationRevisionsRequestRequestTypeDef",
    {
        "ConfigurationId": str,
    },
)
_OptionalListConfigurationRevisionsRequestRequestTypeDef = TypedDict(
    "_OptionalListConfigurationRevisionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListConfigurationRevisionsRequestRequestTypeDef(
    _RequiredListConfigurationRevisionsRequestRequestTypeDef,
    _OptionalListConfigurationRevisionsRequestRequestTypeDef,
):
    pass


ListConfigurationRevisionsResponseTypeDef = TypedDict(
    "ListConfigurationRevisionsResponseTypeDef",
    {
        "ConfigurationId": str,
        "MaxResults": int,
        "NextToken": str,
        "Revisions": List["ConfigurationRevisionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListConfigurationsRequestRequestTypeDef = TypedDict(
    "ListConfigurationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListConfigurationsResponseTypeDef = TypedDict(
    "ListConfigurationsResponseTypeDef",
    {
        "Configurations": List["ConfigurationTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsRequestRequestTypeDef = TypedDict(
    "ListTagsRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUsersRequestRequestTypeDef = TypedDict(
    "_RequiredListUsersRequestRequestTypeDef",
    {
        "BrokerId": str,
    },
)
_OptionalListUsersRequestRequestTypeDef = TypedDict(
    "_OptionalListUsersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListUsersRequestRequestTypeDef(
    _RequiredListUsersRequestRequestTypeDef, _OptionalListUsersRequestRequestTypeDef
):
    pass


ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "BrokerId": str,
        "MaxResults": int,
        "NextToken": str,
        "Users": List["UserSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogsSummaryTypeDef = TypedDict(
    "LogsSummaryTypeDef",
    {
        "Audit": bool,
        "AuditLogGroup": str,
        "General": bool,
        "GeneralLogGroup": str,
        "Pending": "PendingLogsTypeDef",
    },
    total=False,
)

LogsTypeDef = TypedDict(
    "LogsTypeDef",
    {
        "Audit": bool,
        "General": bool,
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

PendingLogsTypeDef = TypedDict(
    "PendingLogsTypeDef",
    {
        "Audit": bool,
        "General": bool,
    },
    total=False,
)

RebootBrokerRequestRequestTypeDef = TypedDict(
    "RebootBrokerRequestRequestTypeDef",
    {
        "BrokerId": str,
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

SanitizationWarningTypeDef = TypedDict(
    "SanitizationWarningTypeDef",
    {
        "AttributeName": str,
        "ElementName": str,
        "Reason": SanitizationWarningReasonType,
    },
    total=False,
)

_RequiredUpdateBrokerRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateBrokerRequestRequestTypeDef",
    {
        "BrokerId": str,
    },
)
_OptionalUpdateBrokerRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateBrokerRequestRequestTypeDef",
    {
        "AuthenticationStrategy": AuthenticationStrategyType,
        "AutoMinorVersionUpgrade": bool,
        "Configuration": "ConfigurationIdTypeDef",
        "EngineVersion": str,
        "HostInstanceType": str,
        "LdapServerMetadata": "LdapServerMetadataInputTypeDef",
        "Logs": "LogsTypeDef",
        "SecurityGroups": List[str],
    },
    total=False,
)


class UpdateBrokerRequestRequestTypeDef(
    _RequiredUpdateBrokerRequestRequestTypeDef, _OptionalUpdateBrokerRequestRequestTypeDef
):
    pass


UpdateBrokerResponseTypeDef = TypedDict(
    "UpdateBrokerResponseTypeDef",
    {
        "AuthenticationStrategy": AuthenticationStrategyType,
        "AutoMinorVersionUpgrade": bool,
        "BrokerId": str,
        "Configuration": "ConfigurationIdTypeDef",
        "EngineVersion": str,
        "HostInstanceType": str,
        "LdapServerMetadata": "LdapServerMetadataOutputTypeDef",
        "Logs": "LogsTypeDef",
        "SecurityGroups": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateConfigurationRequestRequestTypeDef",
    {
        "ConfigurationId": str,
    },
)
_OptionalUpdateConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateConfigurationRequestRequestTypeDef",
    {
        "Data": str,
        "Description": str,
    },
    total=False,
)


class UpdateConfigurationRequestRequestTypeDef(
    _RequiredUpdateConfigurationRequestRequestTypeDef,
    _OptionalUpdateConfigurationRequestRequestTypeDef,
):
    pass


UpdateConfigurationResponseTypeDef = TypedDict(
    "UpdateConfigurationResponseTypeDef",
    {
        "Arn": str,
        "Created": datetime,
        "Id": str,
        "LatestRevision": "ConfigurationRevisionTypeDef",
        "Name": str,
        "Warnings": List["SanitizationWarningTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateUserRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUserRequestRequestTypeDef",
    {
        "BrokerId": str,
        "Username": str,
    },
)
_OptionalUpdateUserRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUserRequestRequestTypeDef",
    {
        "ConsoleAccess": bool,
        "Groups": List[str],
        "Password": str,
    },
    total=False,
)


class UpdateUserRequestRequestTypeDef(
    _RequiredUpdateUserRequestRequestTypeDef, _OptionalUpdateUserRequestRequestTypeDef
):
    pass


UserPendingChangesTypeDef = TypedDict(
    "UserPendingChangesTypeDef",
    {
        "ConsoleAccess": bool,
        "Groups": List[str],
        "PendingChange": ChangeTypeType,
    },
    total=False,
)

UserSummaryTypeDef = TypedDict(
    "UserSummaryTypeDef",
    {
        "PendingChange": ChangeTypeType,
        "Username": str,
    },
    total=False,
)

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "ConsoleAccess": bool,
        "Groups": List[str],
        "Password": str,
        "Username": str,
    },
    total=False,
)

WeeklyStartTimeTypeDef = TypedDict(
    "WeeklyStartTimeTypeDef",
    {
        "DayOfWeek": DayOfWeekType,
        "TimeOfDay": str,
        "TimeZone": str,
    },
    total=False,
)
