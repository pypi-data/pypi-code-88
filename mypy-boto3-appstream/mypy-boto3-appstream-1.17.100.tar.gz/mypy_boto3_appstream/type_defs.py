"""
Type annotations for appstream service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/type_defs.html)

Usage::

    ```python
    from mypy_boto3_appstream.type_defs import AccessEndpointTypeDef

    data: AccessEndpointTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from .literals import (
    ActionType,
    AuthenticationTypeType,
    FleetErrorCodeType,
    FleetStateType,
    FleetTypeType,
    ImageBuilderStateChangeReasonCodeType,
    ImageBuilderStateType,
    ImageStateChangeReasonCodeType,
    ImageStateType,
    PermissionType,
    PlatformTypeType,
    SessionConnectionStateType,
    SessionStateType,
    StackErrorCodeType,
    StorageConnectorTypeType,
    StreamViewType,
    UsageReportExecutionErrorCodeType,
    UserStackAssociationErrorCodeType,
    VisibilityTypeType,
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
    "AccessEndpointTypeDef",
    "ApplicationSettingsResponseTypeDef",
    "ApplicationSettingsTypeDef",
    "ApplicationTypeDef",
    "BatchAssociateUserStackResultTypeDef",
    "BatchDisassociateUserStackResultTypeDef",
    "ComputeCapacityStatusTypeDef",
    "ComputeCapacityTypeDef",
    "CopyImageResponseTypeDef",
    "CreateDirectoryConfigResultTypeDef",
    "CreateFleetResultTypeDef",
    "CreateImageBuilderResultTypeDef",
    "CreateImageBuilderStreamingURLResultTypeDef",
    "CreateStackResultTypeDef",
    "CreateStreamingURLResultTypeDef",
    "CreateUpdatedImageResultTypeDef",
    "CreateUsageReportSubscriptionResultTypeDef",
    "DeleteImageBuilderResultTypeDef",
    "DeleteImageResultTypeDef",
    "DescribeDirectoryConfigsResultTypeDef",
    "DescribeFleetsResultTypeDef",
    "DescribeImageBuildersResultTypeDef",
    "DescribeImagePermissionsResultTypeDef",
    "DescribeImagesResultTypeDef",
    "DescribeSessionsResultTypeDef",
    "DescribeStacksResultTypeDef",
    "DescribeUsageReportSubscriptionsResultTypeDef",
    "DescribeUserStackAssociationsResultTypeDef",
    "DescribeUsersResultTypeDef",
    "DirectoryConfigTypeDef",
    "DomainJoinInfoTypeDef",
    "FleetErrorTypeDef",
    "FleetTypeDef",
    "ImageBuilderStateChangeReasonTypeDef",
    "ImageBuilderTypeDef",
    "ImagePermissionsTypeDef",
    "ImageStateChangeReasonTypeDef",
    "ImageTypeDef",
    "LastReportGenerationExecutionErrorTypeDef",
    "ListAssociatedFleetsResultTypeDef",
    "ListAssociatedStacksResultTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NetworkAccessConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ResourceErrorTypeDef",
    "ServiceAccountCredentialsTypeDef",
    "SessionTypeDef",
    "SharedImagePermissionsTypeDef",
    "StackErrorTypeDef",
    "StackTypeDef",
    "StartImageBuilderResultTypeDef",
    "StopImageBuilderResultTypeDef",
    "StorageConnectorTypeDef",
    "UpdateDirectoryConfigResultTypeDef",
    "UpdateFleetResultTypeDef",
    "UpdateStackResultTypeDef",
    "UsageReportSubscriptionTypeDef",
    "UserSettingTypeDef",
    "UserStackAssociationErrorTypeDef",
    "UserStackAssociationTypeDef",
    "UserTypeDef",
    "VpcConfigTypeDef",
    "WaiterConfigTypeDef",
)

_RequiredAccessEndpointTypeDef = TypedDict(
    "_RequiredAccessEndpointTypeDef",
    {
        "EndpointType": Literal["STREAMING"],
    },
)
_OptionalAccessEndpointTypeDef = TypedDict(
    "_OptionalAccessEndpointTypeDef",
    {
        "VpceId": str,
    },
    total=False,
)


class AccessEndpointTypeDef(_RequiredAccessEndpointTypeDef, _OptionalAccessEndpointTypeDef):
    pass


ApplicationSettingsResponseTypeDef = TypedDict(
    "ApplicationSettingsResponseTypeDef",
    {
        "Enabled": bool,
        "SettingsGroup": str,
        "S3BucketName": str,
    },
    total=False,
)

_RequiredApplicationSettingsTypeDef = TypedDict(
    "_RequiredApplicationSettingsTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalApplicationSettingsTypeDef = TypedDict(
    "_OptionalApplicationSettingsTypeDef",
    {
        "SettingsGroup": str,
    },
    total=False,
)


class ApplicationSettingsTypeDef(
    _RequiredApplicationSettingsTypeDef, _OptionalApplicationSettingsTypeDef
):
    pass


ApplicationTypeDef = TypedDict(
    "ApplicationTypeDef",
    {
        "Name": str,
        "DisplayName": str,
        "IconURL": str,
        "LaunchPath": str,
        "LaunchParameters": str,
        "Enabled": bool,
        "Metadata": Dict[str, str],
    },
    total=False,
)

BatchAssociateUserStackResultTypeDef = TypedDict(
    "BatchAssociateUserStackResultTypeDef",
    {
        "errors": List["UserStackAssociationErrorTypeDef"],
    },
    total=False,
)

BatchDisassociateUserStackResultTypeDef = TypedDict(
    "BatchDisassociateUserStackResultTypeDef",
    {
        "errors": List["UserStackAssociationErrorTypeDef"],
    },
    total=False,
)

_RequiredComputeCapacityStatusTypeDef = TypedDict(
    "_RequiredComputeCapacityStatusTypeDef",
    {
        "Desired": int,
    },
)
_OptionalComputeCapacityStatusTypeDef = TypedDict(
    "_OptionalComputeCapacityStatusTypeDef",
    {
        "Running": int,
        "InUse": int,
        "Available": int,
    },
    total=False,
)


class ComputeCapacityStatusTypeDef(
    _RequiredComputeCapacityStatusTypeDef, _OptionalComputeCapacityStatusTypeDef
):
    pass


ComputeCapacityTypeDef = TypedDict(
    "ComputeCapacityTypeDef",
    {
        "DesiredInstances": int,
    },
)

CopyImageResponseTypeDef = TypedDict(
    "CopyImageResponseTypeDef",
    {
        "DestinationImageName": str,
    },
    total=False,
)

CreateDirectoryConfigResultTypeDef = TypedDict(
    "CreateDirectoryConfigResultTypeDef",
    {
        "DirectoryConfig": "DirectoryConfigTypeDef",
    },
    total=False,
)

CreateFleetResultTypeDef = TypedDict(
    "CreateFleetResultTypeDef",
    {
        "Fleet": "FleetTypeDef",
    },
    total=False,
)

CreateImageBuilderResultTypeDef = TypedDict(
    "CreateImageBuilderResultTypeDef",
    {
        "ImageBuilder": "ImageBuilderTypeDef",
    },
    total=False,
)

CreateImageBuilderStreamingURLResultTypeDef = TypedDict(
    "CreateImageBuilderStreamingURLResultTypeDef",
    {
        "StreamingURL": str,
        "Expires": datetime,
    },
    total=False,
)

CreateStackResultTypeDef = TypedDict(
    "CreateStackResultTypeDef",
    {
        "Stack": "StackTypeDef",
    },
    total=False,
)

CreateStreamingURLResultTypeDef = TypedDict(
    "CreateStreamingURLResultTypeDef",
    {
        "StreamingURL": str,
        "Expires": datetime,
    },
    total=False,
)

CreateUpdatedImageResultTypeDef = TypedDict(
    "CreateUpdatedImageResultTypeDef",
    {
        "image": "ImageTypeDef",
        "canUpdateImage": bool,
    },
    total=False,
)

CreateUsageReportSubscriptionResultTypeDef = TypedDict(
    "CreateUsageReportSubscriptionResultTypeDef",
    {
        "S3BucketName": str,
        "Schedule": Literal["DAILY"],
    },
    total=False,
)

DeleteImageBuilderResultTypeDef = TypedDict(
    "DeleteImageBuilderResultTypeDef",
    {
        "ImageBuilder": "ImageBuilderTypeDef",
    },
    total=False,
)

DeleteImageResultTypeDef = TypedDict(
    "DeleteImageResultTypeDef",
    {
        "Image": "ImageTypeDef",
    },
    total=False,
)

DescribeDirectoryConfigsResultTypeDef = TypedDict(
    "DescribeDirectoryConfigsResultTypeDef",
    {
        "DirectoryConfigs": List["DirectoryConfigTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeFleetsResultTypeDef = TypedDict(
    "DescribeFleetsResultTypeDef",
    {
        "Fleets": List["FleetTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeImageBuildersResultTypeDef = TypedDict(
    "DescribeImageBuildersResultTypeDef",
    {
        "ImageBuilders": List["ImageBuilderTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeImagePermissionsResultTypeDef = TypedDict(
    "DescribeImagePermissionsResultTypeDef",
    {
        "Name": str,
        "SharedImagePermissionsList": List["SharedImagePermissionsTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeImagesResultTypeDef = TypedDict(
    "DescribeImagesResultTypeDef",
    {
        "Images": List["ImageTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeSessionsResultTypeDef = TypedDict(
    "DescribeSessionsResultTypeDef",
    {
        "Sessions": List["SessionTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeStacksResultTypeDef = TypedDict(
    "DescribeStacksResultTypeDef",
    {
        "Stacks": List["StackTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeUsageReportSubscriptionsResultTypeDef = TypedDict(
    "DescribeUsageReportSubscriptionsResultTypeDef",
    {
        "UsageReportSubscriptions": List["UsageReportSubscriptionTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeUserStackAssociationsResultTypeDef = TypedDict(
    "DescribeUserStackAssociationsResultTypeDef",
    {
        "UserStackAssociations": List["UserStackAssociationTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeUsersResultTypeDef = TypedDict(
    "DescribeUsersResultTypeDef",
    {
        "Users": List["UserTypeDef"],
        "NextToken": str,
    },
    total=False,
)

_RequiredDirectoryConfigTypeDef = TypedDict(
    "_RequiredDirectoryConfigTypeDef",
    {
        "DirectoryName": str,
    },
)
_OptionalDirectoryConfigTypeDef = TypedDict(
    "_OptionalDirectoryConfigTypeDef",
    {
        "OrganizationalUnitDistinguishedNames": List[str],
        "ServiceAccountCredentials": "ServiceAccountCredentialsTypeDef",
        "CreatedTime": datetime,
    },
    total=False,
)


class DirectoryConfigTypeDef(_RequiredDirectoryConfigTypeDef, _OptionalDirectoryConfigTypeDef):
    pass


DomainJoinInfoTypeDef = TypedDict(
    "DomainJoinInfoTypeDef",
    {
        "DirectoryName": str,
        "OrganizationalUnitDistinguishedName": str,
    },
    total=False,
)

FleetErrorTypeDef = TypedDict(
    "FleetErrorTypeDef",
    {
        "ErrorCode": FleetErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

_RequiredFleetTypeDef = TypedDict(
    "_RequiredFleetTypeDef",
    {
        "Arn": str,
        "Name": str,
        "InstanceType": str,
        "ComputeCapacityStatus": "ComputeCapacityStatusTypeDef",
        "State": FleetStateType,
    },
)
_OptionalFleetTypeDef = TypedDict(
    "_OptionalFleetTypeDef",
    {
        "DisplayName": str,
        "Description": str,
        "ImageName": str,
        "ImageArn": str,
        "FleetType": FleetTypeType,
        "MaxUserDurationInSeconds": int,
        "DisconnectTimeoutInSeconds": int,
        "VpcConfig": "VpcConfigTypeDef",
        "CreatedTime": datetime,
        "FleetErrors": List["FleetErrorTypeDef"],
        "EnableDefaultInternetAccess": bool,
        "DomainJoinInfo": "DomainJoinInfoTypeDef",
        "IdleDisconnectTimeoutInSeconds": int,
        "IamRoleArn": str,
        "StreamView": StreamViewType,
    },
    total=False,
)


class FleetTypeDef(_RequiredFleetTypeDef, _OptionalFleetTypeDef):
    pass


ImageBuilderStateChangeReasonTypeDef = TypedDict(
    "ImageBuilderStateChangeReasonTypeDef",
    {
        "Code": ImageBuilderStateChangeReasonCodeType,
        "Message": str,
    },
    total=False,
)

_RequiredImageBuilderTypeDef = TypedDict(
    "_RequiredImageBuilderTypeDef",
    {
        "Name": str,
    },
)
_OptionalImageBuilderTypeDef = TypedDict(
    "_OptionalImageBuilderTypeDef",
    {
        "Arn": str,
        "ImageArn": str,
        "Description": str,
        "DisplayName": str,
        "VpcConfig": "VpcConfigTypeDef",
        "InstanceType": str,
        "Platform": PlatformTypeType,
        "IamRoleArn": str,
        "State": ImageBuilderStateType,
        "StateChangeReason": "ImageBuilderStateChangeReasonTypeDef",
        "CreatedTime": datetime,
        "EnableDefaultInternetAccess": bool,
        "DomainJoinInfo": "DomainJoinInfoTypeDef",
        "NetworkAccessConfiguration": "NetworkAccessConfigurationTypeDef",
        "ImageBuilderErrors": List["ResourceErrorTypeDef"],
        "AppstreamAgentVersion": str,
        "AccessEndpoints": List["AccessEndpointTypeDef"],
    },
    total=False,
)


class ImageBuilderTypeDef(_RequiredImageBuilderTypeDef, _OptionalImageBuilderTypeDef):
    pass


ImagePermissionsTypeDef = TypedDict(
    "ImagePermissionsTypeDef",
    {
        "allowFleet": bool,
        "allowImageBuilder": bool,
    },
    total=False,
)

ImageStateChangeReasonTypeDef = TypedDict(
    "ImageStateChangeReasonTypeDef",
    {
        "Code": ImageStateChangeReasonCodeType,
        "Message": str,
    },
    total=False,
)

_RequiredImageTypeDef = TypedDict(
    "_RequiredImageTypeDef",
    {
        "Name": str,
    },
)
_OptionalImageTypeDef = TypedDict(
    "_OptionalImageTypeDef",
    {
        "Arn": str,
        "BaseImageArn": str,
        "DisplayName": str,
        "State": ImageStateType,
        "Visibility": VisibilityTypeType,
        "ImageBuilderSupported": bool,
        "ImageBuilderName": str,
        "Platform": PlatformTypeType,
        "Description": str,
        "StateChangeReason": "ImageStateChangeReasonTypeDef",
        "Applications": List["ApplicationTypeDef"],
        "CreatedTime": datetime,
        "PublicBaseImageReleasedDate": datetime,
        "AppstreamAgentVersion": str,
        "ImagePermissions": "ImagePermissionsTypeDef",
        "ImageErrors": List["ResourceErrorTypeDef"],
    },
    total=False,
)


class ImageTypeDef(_RequiredImageTypeDef, _OptionalImageTypeDef):
    pass


LastReportGenerationExecutionErrorTypeDef = TypedDict(
    "LastReportGenerationExecutionErrorTypeDef",
    {
        "ErrorCode": UsageReportExecutionErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

ListAssociatedFleetsResultTypeDef = TypedDict(
    "ListAssociatedFleetsResultTypeDef",
    {
        "Names": List[str],
        "NextToken": str,
    },
    total=False,
)

ListAssociatedStacksResultTypeDef = TypedDict(
    "ListAssociatedStacksResultTypeDef",
    {
        "Names": List[str],
        "NextToken": str,
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)

NetworkAccessConfigurationTypeDef = TypedDict(
    "NetworkAccessConfigurationTypeDef",
    {
        "EniPrivateIpAddress": str,
        "EniId": str,
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

ResourceErrorTypeDef = TypedDict(
    "ResourceErrorTypeDef",
    {
        "ErrorCode": FleetErrorCodeType,
        "ErrorMessage": str,
        "ErrorTimestamp": datetime,
    },
    total=False,
)

ServiceAccountCredentialsTypeDef = TypedDict(
    "ServiceAccountCredentialsTypeDef",
    {
        "AccountName": str,
        "AccountPassword": str,
    },
)

_RequiredSessionTypeDef = TypedDict(
    "_RequiredSessionTypeDef",
    {
        "Id": str,
        "UserId": str,
        "StackName": str,
        "FleetName": str,
        "State": SessionStateType,
    },
)
_OptionalSessionTypeDef = TypedDict(
    "_OptionalSessionTypeDef",
    {
        "ConnectionState": SessionConnectionStateType,
        "StartTime": datetime,
        "MaxExpirationTime": datetime,
        "AuthenticationType": AuthenticationTypeType,
        "NetworkAccessConfiguration": "NetworkAccessConfigurationTypeDef",
    },
    total=False,
)


class SessionTypeDef(_RequiredSessionTypeDef, _OptionalSessionTypeDef):
    pass


SharedImagePermissionsTypeDef = TypedDict(
    "SharedImagePermissionsTypeDef",
    {
        "sharedAccountId": str,
        "imagePermissions": "ImagePermissionsTypeDef",
    },
)

StackErrorTypeDef = TypedDict(
    "StackErrorTypeDef",
    {
        "ErrorCode": StackErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

_RequiredStackTypeDef = TypedDict(
    "_RequiredStackTypeDef",
    {
        "Name": str,
    },
)
_OptionalStackTypeDef = TypedDict(
    "_OptionalStackTypeDef",
    {
        "Arn": str,
        "Description": str,
        "DisplayName": str,
        "CreatedTime": datetime,
        "StorageConnectors": List["StorageConnectorTypeDef"],
        "RedirectURL": str,
        "FeedbackURL": str,
        "StackErrors": List["StackErrorTypeDef"],
        "UserSettings": List["UserSettingTypeDef"],
        "ApplicationSettings": "ApplicationSettingsResponseTypeDef",
        "AccessEndpoints": List["AccessEndpointTypeDef"],
        "EmbedHostDomains": List[str],
    },
    total=False,
)


class StackTypeDef(_RequiredStackTypeDef, _OptionalStackTypeDef):
    pass


StartImageBuilderResultTypeDef = TypedDict(
    "StartImageBuilderResultTypeDef",
    {
        "ImageBuilder": "ImageBuilderTypeDef",
    },
    total=False,
)

StopImageBuilderResultTypeDef = TypedDict(
    "StopImageBuilderResultTypeDef",
    {
        "ImageBuilder": "ImageBuilderTypeDef",
    },
    total=False,
)

_RequiredStorageConnectorTypeDef = TypedDict(
    "_RequiredStorageConnectorTypeDef",
    {
        "ConnectorType": StorageConnectorTypeType,
    },
)
_OptionalStorageConnectorTypeDef = TypedDict(
    "_OptionalStorageConnectorTypeDef",
    {
        "ResourceIdentifier": str,
        "Domains": List[str],
    },
    total=False,
)


class StorageConnectorTypeDef(_RequiredStorageConnectorTypeDef, _OptionalStorageConnectorTypeDef):
    pass


UpdateDirectoryConfigResultTypeDef = TypedDict(
    "UpdateDirectoryConfigResultTypeDef",
    {
        "DirectoryConfig": "DirectoryConfigTypeDef",
    },
    total=False,
)

UpdateFleetResultTypeDef = TypedDict(
    "UpdateFleetResultTypeDef",
    {
        "Fleet": "FleetTypeDef",
    },
    total=False,
)

UpdateStackResultTypeDef = TypedDict(
    "UpdateStackResultTypeDef",
    {
        "Stack": "StackTypeDef",
    },
    total=False,
)

UsageReportSubscriptionTypeDef = TypedDict(
    "UsageReportSubscriptionTypeDef",
    {
        "S3BucketName": str,
        "Schedule": Literal["DAILY"],
        "LastGeneratedReportDate": datetime,
        "SubscriptionErrors": List["LastReportGenerationExecutionErrorTypeDef"],
    },
    total=False,
)

UserSettingTypeDef = TypedDict(
    "UserSettingTypeDef",
    {
        "Action": ActionType,
        "Permission": PermissionType,
    },
)

UserStackAssociationErrorTypeDef = TypedDict(
    "UserStackAssociationErrorTypeDef",
    {
        "UserStackAssociation": "UserStackAssociationTypeDef",
        "ErrorCode": UserStackAssociationErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

_RequiredUserStackAssociationTypeDef = TypedDict(
    "_RequiredUserStackAssociationTypeDef",
    {
        "StackName": str,
        "UserName": str,
        "AuthenticationType": AuthenticationTypeType,
    },
)
_OptionalUserStackAssociationTypeDef = TypedDict(
    "_OptionalUserStackAssociationTypeDef",
    {
        "SendEmailNotification": bool,
    },
    total=False,
)


class UserStackAssociationTypeDef(
    _RequiredUserStackAssociationTypeDef, _OptionalUserStackAssociationTypeDef
):
    pass


_RequiredUserTypeDef = TypedDict(
    "_RequiredUserTypeDef",
    {
        "AuthenticationType": AuthenticationTypeType,
    },
)
_OptionalUserTypeDef = TypedDict(
    "_OptionalUserTypeDef",
    {
        "Arn": str,
        "UserName": str,
        "Enabled": bool,
        "Status": str,
        "FirstName": str,
        "LastName": str,
        "CreatedTime": datetime,
    },
    total=False,
)


class UserTypeDef(_RequiredUserTypeDef, _OptionalUserTypeDef):
    pass


VpcConfigTypeDef = TypedDict(
    "VpcConfigTypeDef",
    {
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
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
