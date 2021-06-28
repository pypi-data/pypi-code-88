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
    "CreateBrokerRequestTypeDef",
    "CreateBrokerResponseResponseTypeDef",
    "CreateConfigurationRequestTypeDef",
    "CreateConfigurationResponseResponseTypeDef",
    "CreateTagsRequestTypeDef",
    "CreateUserRequestTypeDef",
    "DeleteBrokerRequestTypeDef",
    "DeleteBrokerResponseResponseTypeDef",
    "DeleteTagsRequestTypeDef",
    "DeleteUserRequestTypeDef",
    "DescribeBrokerEngineTypesRequestTypeDef",
    "DescribeBrokerEngineTypesResponseResponseTypeDef",
    "DescribeBrokerInstanceOptionsRequestTypeDef",
    "DescribeBrokerInstanceOptionsResponseResponseTypeDef",
    "DescribeBrokerRequestTypeDef",
    "DescribeBrokerResponseResponseTypeDef",
    "DescribeConfigurationRequestTypeDef",
    "DescribeConfigurationResponseResponseTypeDef",
    "DescribeConfigurationRevisionRequestTypeDef",
    "DescribeConfigurationRevisionResponseResponseTypeDef",
    "DescribeUserRequestTypeDef",
    "DescribeUserResponseResponseTypeDef",
    "EncryptionOptionsTypeDef",
    "EngineVersionTypeDef",
    "LdapServerMetadataInputTypeDef",
    "LdapServerMetadataOutputTypeDef",
    "ListBrokersRequestTypeDef",
    "ListBrokersResponseResponseTypeDef",
    "ListConfigurationRevisionsRequestTypeDef",
    "ListConfigurationRevisionsResponseResponseTypeDef",
    "ListConfigurationsRequestTypeDef",
    "ListConfigurationsResponseResponseTypeDef",
    "ListTagsRequestTypeDef",
    "ListTagsResponseResponseTypeDef",
    "ListUsersRequestTypeDef",
    "ListUsersResponseResponseTypeDef",
    "LogsSummaryTypeDef",
    "LogsTypeDef",
    "PaginatorConfigTypeDef",
    "PendingLogsTypeDef",
    "RebootBrokerRequestTypeDef",
    "ResponseMetadataTypeDef",
    "SanitizationWarningTypeDef",
    "UpdateBrokerRequestTypeDef",
    "UpdateBrokerResponseResponseTypeDef",
    "UpdateConfigurationRequestTypeDef",
    "UpdateConfigurationResponseResponseTypeDef",
    "UpdateUserRequestTypeDef",
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

CreateBrokerRequestTypeDef = TypedDict(
    "CreateBrokerRequestTypeDef",
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

CreateBrokerResponseResponseTypeDef = TypedDict(
    "CreateBrokerResponseResponseTypeDef",
    {
        "BrokerArn": str,
        "BrokerId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateConfigurationRequestTypeDef = TypedDict(
    "CreateConfigurationRequestTypeDef",
    {
        "AuthenticationStrategy": AuthenticationStrategyType,
        "EngineType": EngineTypeType,
        "EngineVersion": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

CreateConfigurationResponseResponseTypeDef = TypedDict(
    "CreateConfigurationResponseResponseTypeDef",
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

_RequiredCreateTagsRequestTypeDef = TypedDict(
    "_RequiredCreateTagsRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalCreateTagsRequestTypeDef = TypedDict(
    "_OptionalCreateTagsRequestTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateTagsRequestTypeDef(
    _RequiredCreateTagsRequestTypeDef, _OptionalCreateTagsRequestTypeDef
):
    pass


_RequiredCreateUserRequestTypeDef = TypedDict(
    "_RequiredCreateUserRequestTypeDef",
    {
        "BrokerId": str,
        "Username": str,
    },
)
_OptionalCreateUserRequestTypeDef = TypedDict(
    "_OptionalCreateUserRequestTypeDef",
    {
        "ConsoleAccess": bool,
        "Groups": List[str],
        "Password": str,
    },
    total=False,
)


class CreateUserRequestTypeDef(
    _RequiredCreateUserRequestTypeDef, _OptionalCreateUserRequestTypeDef
):
    pass


DeleteBrokerRequestTypeDef = TypedDict(
    "DeleteBrokerRequestTypeDef",
    {
        "BrokerId": str,
    },
)

DeleteBrokerResponseResponseTypeDef = TypedDict(
    "DeleteBrokerResponseResponseTypeDef",
    {
        "BrokerId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTagsRequestTypeDef = TypedDict(
    "DeleteTagsRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

DeleteUserRequestTypeDef = TypedDict(
    "DeleteUserRequestTypeDef",
    {
        "BrokerId": str,
        "Username": str,
    },
)

DescribeBrokerEngineTypesRequestTypeDef = TypedDict(
    "DescribeBrokerEngineTypesRequestTypeDef",
    {
        "EngineType": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeBrokerEngineTypesResponseResponseTypeDef = TypedDict(
    "DescribeBrokerEngineTypesResponseResponseTypeDef",
    {
        "BrokerEngineTypes": List["BrokerEngineTypeTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBrokerInstanceOptionsRequestTypeDef = TypedDict(
    "DescribeBrokerInstanceOptionsRequestTypeDef",
    {
        "EngineType": str,
        "HostInstanceType": str,
        "MaxResults": int,
        "NextToken": str,
        "StorageType": str,
    },
    total=False,
)

DescribeBrokerInstanceOptionsResponseResponseTypeDef = TypedDict(
    "DescribeBrokerInstanceOptionsResponseResponseTypeDef",
    {
        "BrokerInstanceOptions": List["BrokerInstanceOptionTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBrokerRequestTypeDef = TypedDict(
    "DescribeBrokerRequestTypeDef",
    {
        "BrokerId": str,
    },
)

DescribeBrokerResponseResponseTypeDef = TypedDict(
    "DescribeBrokerResponseResponseTypeDef",
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

DescribeConfigurationRequestTypeDef = TypedDict(
    "DescribeConfigurationRequestTypeDef",
    {
        "ConfigurationId": str,
    },
)

DescribeConfigurationResponseResponseTypeDef = TypedDict(
    "DescribeConfigurationResponseResponseTypeDef",
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

DescribeConfigurationRevisionRequestTypeDef = TypedDict(
    "DescribeConfigurationRevisionRequestTypeDef",
    {
        "ConfigurationId": str,
        "ConfigurationRevision": str,
    },
)

DescribeConfigurationRevisionResponseResponseTypeDef = TypedDict(
    "DescribeConfigurationRevisionResponseResponseTypeDef",
    {
        "ConfigurationId": str,
        "Created": datetime,
        "Data": str,
        "Description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserRequestTypeDef = TypedDict(
    "DescribeUserRequestTypeDef",
    {
        "BrokerId": str,
        "Username": str,
    },
)

DescribeUserResponseResponseTypeDef = TypedDict(
    "DescribeUserResponseResponseTypeDef",
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

ListBrokersRequestTypeDef = TypedDict(
    "ListBrokersRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListBrokersResponseResponseTypeDef = TypedDict(
    "ListBrokersResponseResponseTypeDef",
    {
        "BrokerSummaries": List["BrokerSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListConfigurationRevisionsRequestTypeDef = TypedDict(
    "_RequiredListConfigurationRevisionsRequestTypeDef",
    {
        "ConfigurationId": str,
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
        "ConfigurationId": str,
        "MaxResults": int,
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
        "MaxResults": int,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsRequestTypeDef = TypedDict(
    "ListTagsRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsResponseResponseTypeDef = TypedDict(
    "ListTagsResponseResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUsersRequestTypeDef = TypedDict(
    "_RequiredListUsersRequestTypeDef",
    {
        "BrokerId": str,
    },
)
_OptionalListUsersRequestTypeDef = TypedDict(
    "_OptionalListUsersRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListUsersRequestTypeDef(_RequiredListUsersRequestTypeDef, _OptionalListUsersRequestTypeDef):
    pass


ListUsersResponseResponseTypeDef = TypedDict(
    "ListUsersResponseResponseTypeDef",
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

RebootBrokerRequestTypeDef = TypedDict(
    "RebootBrokerRequestTypeDef",
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

_RequiredUpdateBrokerRequestTypeDef = TypedDict(
    "_RequiredUpdateBrokerRequestTypeDef",
    {
        "BrokerId": str,
    },
)
_OptionalUpdateBrokerRequestTypeDef = TypedDict(
    "_OptionalUpdateBrokerRequestTypeDef",
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


class UpdateBrokerRequestTypeDef(
    _RequiredUpdateBrokerRequestTypeDef, _OptionalUpdateBrokerRequestTypeDef
):
    pass


UpdateBrokerResponseResponseTypeDef = TypedDict(
    "UpdateBrokerResponseResponseTypeDef",
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

_RequiredUpdateConfigurationRequestTypeDef = TypedDict(
    "_RequiredUpdateConfigurationRequestTypeDef",
    {
        "ConfigurationId": str,
    },
)
_OptionalUpdateConfigurationRequestTypeDef = TypedDict(
    "_OptionalUpdateConfigurationRequestTypeDef",
    {
        "Data": str,
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
        "Created": datetime,
        "Id": str,
        "LatestRevision": "ConfigurationRevisionTypeDef",
        "Name": str,
        "Warnings": List["SanitizationWarningTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateUserRequestTypeDef = TypedDict(
    "_RequiredUpdateUserRequestTypeDef",
    {
        "BrokerId": str,
        "Username": str,
    },
)
_OptionalUpdateUserRequestTypeDef = TypedDict(
    "_OptionalUpdateUserRequestTypeDef",
    {
        "ConsoleAccess": bool,
        "Groups": List[str],
        "Password": str,
    },
    total=False,
)


class UpdateUserRequestTypeDef(
    _RequiredUpdateUserRequestTypeDef, _OptionalUpdateUserRequestTypeDef
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
