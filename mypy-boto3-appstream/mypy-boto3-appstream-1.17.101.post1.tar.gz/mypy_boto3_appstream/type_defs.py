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
from typing import Any, Dict, List

from .literals import (
    ActionType,
    AuthenticationTypeType,
    FleetAttributeType,
    FleetErrorCodeType,
    FleetStateType,
    FleetTypeType,
    ImageBuilderStateChangeReasonCodeType,
    ImageBuilderStateType,
    ImageStateChangeReasonCodeType,
    ImageStateType,
    MessageActionType,
    PermissionType,
    PlatformTypeType,
    SessionConnectionStateType,
    SessionStateType,
    StackAttributeType,
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
    "AssociateFleetRequestTypeDef",
    "BatchAssociateUserStackRequestTypeDef",
    "BatchAssociateUserStackResultResponseTypeDef",
    "BatchDisassociateUserStackRequestTypeDef",
    "BatchDisassociateUserStackResultResponseTypeDef",
    "ComputeCapacityStatusTypeDef",
    "ComputeCapacityTypeDef",
    "CopyImageRequestTypeDef",
    "CopyImageResponseResponseTypeDef",
    "CreateDirectoryConfigRequestTypeDef",
    "CreateDirectoryConfigResultResponseTypeDef",
    "CreateFleetRequestTypeDef",
    "CreateFleetResultResponseTypeDef",
    "CreateImageBuilderRequestTypeDef",
    "CreateImageBuilderResultResponseTypeDef",
    "CreateImageBuilderStreamingURLRequestTypeDef",
    "CreateImageBuilderStreamingURLResultResponseTypeDef",
    "CreateStackRequestTypeDef",
    "CreateStackResultResponseTypeDef",
    "CreateStreamingURLRequestTypeDef",
    "CreateStreamingURLResultResponseTypeDef",
    "CreateUpdatedImageRequestTypeDef",
    "CreateUpdatedImageResultResponseTypeDef",
    "CreateUsageReportSubscriptionResultResponseTypeDef",
    "CreateUserRequestTypeDef",
    "DeleteDirectoryConfigRequestTypeDef",
    "DeleteFleetRequestTypeDef",
    "DeleteImageBuilderRequestTypeDef",
    "DeleteImageBuilderResultResponseTypeDef",
    "DeleteImagePermissionsRequestTypeDef",
    "DeleteImageRequestTypeDef",
    "DeleteImageResultResponseTypeDef",
    "DeleteStackRequestTypeDef",
    "DeleteUserRequestTypeDef",
    "DescribeDirectoryConfigsRequestTypeDef",
    "DescribeDirectoryConfigsResultResponseTypeDef",
    "DescribeFleetsRequestTypeDef",
    "DescribeFleetsResultResponseTypeDef",
    "DescribeImageBuildersRequestTypeDef",
    "DescribeImageBuildersResultResponseTypeDef",
    "DescribeImagePermissionsRequestTypeDef",
    "DescribeImagePermissionsResultResponseTypeDef",
    "DescribeImagesRequestTypeDef",
    "DescribeImagesResultResponseTypeDef",
    "DescribeSessionsRequestTypeDef",
    "DescribeSessionsResultResponseTypeDef",
    "DescribeStacksRequestTypeDef",
    "DescribeStacksResultResponseTypeDef",
    "DescribeUsageReportSubscriptionsRequestTypeDef",
    "DescribeUsageReportSubscriptionsResultResponseTypeDef",
    "DescribeUserStackAssociationsRequestTypeDef",
    "DescribeUserStackAssociationsResultResponseTypeDef",
    "DescribeUsersRequestTypeDef",
    "DescribeUsersResultResponseTypeDef",
    "DirectoryConfigTypeDef",
    "DisableUserRequestTypeDef",
    "DisassociateFleetRequestTypeDef",
    "DomainJoinInfoTypeDef",
    "EnableUserRequestTypeDef",
    "ExpireSessionRequestTypeDef",
    "FleetErrorTypeDef",
    "FleetTypeDef",
    "ImageBuilderStateChangeReasonTypeDef",
    "ImageBuilderTypeDef",
    "ImagePermissionsTypeDef",
    "ImageStateChangeReasonTypeDef",
    "ImageTypeDef",
    "LastReportGenerationExecutionErrorTypeDef",
    "ListAssociatedFleetsRequestTypeDef",
    "ListAssociatedFleetsResultResponseTypeDef",
    "ListAssociatedStacksRequestTypeDef",
    "ListAssociatedStacksResultResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "NetworkAccessConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ResourceErrorTypeDef",
    "ResponseMetadataTypeDef",
    "ServiceAccountCredentialsTypeDef",
    "SessionTypeDef",
    "SharedImagePermissionsTypeDef",
    "StackErrorTypeDef",
    "StackTypeDef",
    "StartFleetRequestTypeDef",
    "StartImageBuilderRequestTypeDef",
    "StartImageBuilderResultResponseTypeDef",
    "StopFleetRequestTypeDef",
    "StopImageBuilderRequestTypeDef",
    "StopImageBuilderResultResponseTypeDef",
    "StorageConnectorTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateDirectoryConfigRequestTypeDef",
    "UpdateDirectoryConfigResultResponseTypeDef",
    "UpdateFleetRequestTypeDef",
    "UpdateFleetResultResponseTypeDef",
    "UpdateImagePermissionsRequestTypeDef",
    "UpdateStackRequestTypeDef",
    "UpdateStackResultResponseTypeDef",
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

AssociateFleetRequestTypeDef = TypedDict(
    "AssociateFleetRequestTypeDef",
    {
        "FleetName": str,
        "StackName": str,
    },
)

BatchAssociateUserStackRequestTypeDef = TypedDict(
    "BatchAssociateUserStackRequestTypeDef",
    {
        "UserStackAssociations": List["UserStackAssociationTypeDef"],
    },
)

BatchAssociateUserStackResultResponseTypeDef = TypedDict(
    "BatchAssociateUserStackResultResponseTypeDef",
    {
        "errors": List["UserStackAssociationErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDisassociateUserStackRequestTypeDef = TypedDict(
    "BatchDisassociateUserStackRequestTypeDef",
    {
        "UserStackAssociations": List["UserStackAssociationTypeDef"],
    },
)

BatchDisassociateUserStackResultResponseTypeDef = TypedDict(
    "BatchDisassociateUserStackResultResponseTypeDef",
    {
        "errors": List["UserStackAssociationErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredCopyImageRequestTypeDef = TypedDict(
    "_RequiredCopyImageRequestTypeDef",
    {
        "SourceImageName": str,
        "DestinationImageName": str,
        "DestinationRegion": str,
    },
)
_OptionalCopyImageRequestTypeDef = TypedDict(
    "_OptionalCopyImageRequestTypeDef",
    {
        "DestinationImageDescription": str,
    },
    total=False,
)


class CopyImageRequestTypeDef(_RequiredCopyImageRequestTypeDef, _OptionalCopyImageRequestTypeDef):
    pass


CopyImageResponseResponseTypeDef = TypedDict(
    "CopyImageResponseResponseTypeDef",
    {
        "DestinationImageName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDirectoryConfigRequestTypeDef = TypedDict(
    "_RequiredCreateDirectoryConfigRequestTypeDef",
    {
        "DirectoryName": str,
        "OrganizationalUnitDistinguishedNames": List[str],
    },
)
_OptionalCreateDirectoryConfigRequestTypeDef = TypedDict(
    "_OptionalCreateDirectoryConfigRequestTypeDef",
    {
        "ServiceAccountCredentials": "ServiceAccountCredentialsTypeDef",
    },
    total=False,
)


class CreateDirectoryConfigRequestTypeDef(
    _RequiredCreateDirectoryConfigRequestTypeDef, _OptionalCreateDirectoryConfigRequestTypeDef
):
    pass


CreateDirectoryConfigResultResponseTypeDef = TypedDict(
    "CreateDirectoryConfigResultResponseTypeDef",
    {
        "DirectoryConfig": "DirectoryConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFleetRequestTypeDef = TypedDict(
    "_RequiredCreateFleetRequestTypeDef",
    {
        "Name": str,
        "InstanceType": str,
        "ComputeCapacity": "ComputeCapacityTypeDef",
    },
)
_OptionalCreateFleetRequestTypeDef = TypedDict(
    "_OptionalCreateFleetRequestTypeDef",
    {
        "ImageName": str,
        "ImageArn": str,
        "FleetType": FleetTypeType,
        "VpcConfig": "VpcConfigTypeDef",
        "MaxUserDurationInSeconds": int,
        "DisconnectTimeoutInSeconds": int,
        "Description": str,
        "DisplayName": str,
        "EnableDefaultInternetAccess": bool,
        "DomainJoinInfo": "DomainJoinInfoTypeDef",
        "Tags": Dict[str, str],
        "IdleDisconnectTimeoutInSeconds": int,
        "IamRoleArn": str,
        "StreamView": StreamViewType,
    },
    total=False,
)


class CreateFleetRequestTypeDef(
    _RequiredCreateFleetRequestTypeDef, _OptionalCreateFleetRequestTypeDef
):
    pass


CreateFleetResultResponseTypeDef = TypedDict(
    "CreateFleetResultResponseTypeDef",
    {
        "Fleet": "FleetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateImageBuilderRequestTypeDef = TypedDict(
    "_RequiredCreateImageBuilderRequestTypeDef",
    {
        "Name": str,
        "InstanceType": str,
    },
)
_OptionalCreateImageBuilderRequestTypeDef = TypedDict(
    "_OptionalCreateImageBuilderRequestTypeDef",
    {
        "ImageName": str,
        "ImageArn": str,
        "Description": str,
        "DisplayName": str,
        "VpcConfig": "VpcConfigTypeDef",
        "IamRoleArn": str,
        "EnableDefaultInternetAccess": bool,
        "DomainJoinInfo": "DomainJoinInfoTypeDef",
        "AppstreamAgentVersion": str,
        "Tags": Dict[str, str],
        "AccessEndpoints": List["AccessEndpointTypeDef"],
    },
    total=False,
)


class CreateImageBuilderRequestTypeDef(
    _RequiredCreateImageBuilderRequestTypeDef, _OptionalCreateImageBuilderRequestTypeDef
):
    pass


CreateImageBuilderResultResponseTypeDef = TypedDict(
    "CreateImageBuilderResultResponseTypeDef",
    {
        "ImageBuilder": "ImageBuilderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateImageBuilderStreamingURLRequestTypeDef = TypedDict(
    "_RequiredCreateImageBuilderStreamingURLRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateImageBuilderStreamingURLRequestTypeDef = TypedDict(
    "_OptionalCreateImageBuilderStreamingURLRequestTypeDef",
    {
        "Validity": int,
    },
    total=False,
)


class CreateImageBuilderStreamingURLRequestTypeDef(
    _RequiredCreateImageBuilderStreamingURLRequestTypeDef,
    _OptionalCreateImageBuilderStreamingURLRequestTypeDef,
):
    pass


CreateImageBuilderStreamingURLResultResponseTypeDef = TypedDict(
    "CreateImageBuilderStreamingURLResultResponseTypeDef",
    {
        "StreamingURL": str,
        "Expires": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStackRequestTypeDef = TypedDict(
    "_RequiredCreateStackRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateStackRequestTypeDef = TypedDict(
    "_OptionalCreateStackRequestTypeDef",
    {
        "Description": str,
        "DisplayName": str,
        "StorageConnectors": List["StorageConnectorTypeDef"],
        "RedirectURL": str,
        "FeedbackURL": str,
        "UserSettings": List["UserSettingTypeDef"],
        "ApplicationSettings": "ApplicationSettingsTypeDef",
        "Tags": Dict[str, str],
        "AccessEndpoints": List["AccessEndpointTypeDef"],
        "EmbedHostDomains": List[str],
    },
    total=False,
)


class CreateStackRequestTypeDef(
    _RequiredCreateStackRequestTypeDef, _OptionalCreateStackRequestTypeDef
):
    pass


CreateStackResultResponseTypeDef = TypedDict(
    "CreateStackResultResponseTypeDef",
    {
        "Stack": "StackTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStreamingURLRequestTypeDef = TypedDict(
    "_RequiredCreateStreamingURLRequestTypeDef",
    {
        "StackName": str,
        "FleetName": str,
        "UserId": str,
    },
)
_OptionalCreateStreamingURLRequestTypeDef = TypedDict(
    "_OptionalCreateStreamingURLRequestTypeDef",
    {
        "ApplicationId": str,
        "Validity": int,
        "SessionContext": str,
    },
    total=False,
)


class CreateStreamingURLRequestTypeDef(
    _RequiredCreateStreamingURLRequestTypeDef, _OptionalCreateStreamingURLRequestTypeDef
):
    pass


CreateStreamingURLResultResponseTypeDef = TypedDict(
    "CreateStreamingURLResultResponseTypeDef",
    {
        "StreamingURL": str,
        "Expires": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUpdatedImageRequestTypeDef = TypedDict(
    "_RequiredCreateUpdatedImageRequestTypeDef",
    {
        "existingImageName": str,
        "newImageName": str,
    },
)
_OptionalCreateUpdatedImageRequestTypeDef = TypedDict(
    "_OptionalCreateUpdatedImageRequestTypeDef",
    {
        "newImageDescription": str,
        "newImageDisplayName": str,
        "newImageTags": Dict[str, str],
        "dryRun": bool,
    },
    total=False,
)


class CreateUpdatedImageRequestTypeDef(
    _RequiredCreateUpdatedImageRequestTypeDef, _OptionalCreateUpdatedImageRequestTypeDef
):
    pass


CreateUpdatedImageResultResponseTypeDef = TypedDict(
    "CreateUpdatedImageResultResponseTypeDef",
    {
        "image": "ImageTypeDef",
        "canUpdateImage": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUsageReportSubscriptionResultResponseTypeDef = TypedDict(
    "CreateUsageReportSubscriptionResultResponseTypeDef",
    {
        "S3BucketName": str,
        "Schedule": Literal["DAILY"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserRequestTypeDef = TypedDict(
    "_RequiredCreateUserRequestTypeDef",
    {
        "UserName": str,
        "AuthenticationType": AuthenticationTypeType,
    },
)
_OptionalCreateUserRequestTypeDef = TypedDict(
    "_OptionalCreateUserRequestTypeDef",
    {
        "MessageAction": MessageActionType,
        "FirstName": str,
        "LastName": str,
    },
    total=False,
)


class CreateUserRequestTypeDef(
    _RequiredCreateUserRequestTypeDef, _OptionalCreateUserRequestTypeDef
):
    pass


DeleteDirectoryConfigRequestTypeDef = TypedDict(
    "DeleteDirectoryConfigRequestTypeDef",
    {
        "DirectoryName": str,
    },
)

DeleteFleetRequestTypeDef = TypedDict(
    "DeleteFleetRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteImageBuilderRequestTypeDef = TypedDict(
    "DeleteImageBuilderRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteImageBuilderResultResponseTypeDef = TypedDict(
    "DeleteImageBuilderResultResponseTypeDef",
    {
        "ImageBuilder": "ImageBuilderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteImagePermissionsRequestTypeDef = TypedDict(
    "DeleteImagePermissionsRequestTypeDef",
    {
        "Name": str,
        "SharedAccountId": str,
    },
)

DeleteImageRequestTypeDef = TypedDict(
    "DeleteImageRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteImageResultResponseTypeDef = TypedDict(
    "DeleteImageResultResponseTypeDef",
    {
        "Image": "ImageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteStackRequestTypeDef = TypedDict(
    "DeleteStackRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteUserRequestTypeDef = TypedDict(
    "DeleteUserRequestTypeDef",
    {
        "UserName": str,
        "AuthenticationType": AuthenticationTypeType,
    },
)

DescribeDirectoryConfigsRequestTypeDef = TypedDict(
    "DescribeDirectoryConfigsRequestTypeDef",
    {
        "DirectoryNames": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeDirectoryConfigsResultResponseTypeDef = TypedDict(
    "DescribeDirectoryConfigsResultResponseTypeDef",
    {
        "DirectoryConfigs": List["DirectoryConfigTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetsRequestTypeDef = TypedDict(
    "DescribeFleetsRequestTypeDef",
    {
        "Names": List[str],
        "NextToken": str,
    },
    total=False,
)

DescribeFleetsResultResponseTypeDef = TypedDict(
    "DescribeFleetsResultResponseTypeDef",
    {
        "Fleets": List["FleetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImageBuildersRequestTypeDef = TypedDict(
    "DescribeImageBuildersRequestTypeDef",
    {
        "Names": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeImageBuildersResultResponseTypeDef = TypedDict(
    "DescribeImageBuildersResultResponseTypeDef",
    {
        "ImageBuilders": List["ImageBuilderTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeImagePermissionsRequestTypeDef = TypedDict(
    "_RequiredDescribeImagePermissionsRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalDescribeImagePermissionsRequestTypeDef = TypedDict(
    "_OptionalDescribeImagePermissionsRequestTypeDef",
    {
        "MaxResults": int,
        "SharedAwsAccountIds": List[str],
        "NextToken": str,
    },
    total=False,
)


class DescribeImagePermissionsRequestTypeDef(
    _RequiredDescribeImagePermissionsRequestTypeDef, _OptionalDescribeImagePermissionsRequestTypeDef
):
    pass


DescribeImagePermissionsResultResponseTypeDef = TypedDict(
    "DescribeImagePermissionsResultResponseTypeDef",
    {
        "Name": str,
        "SharedImagePermissionsList": List["SharedImagePermissionsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImagesRequestTypeDef = TypedDict(
    "DescribeImagesRequestTypeDef",
    {
        "Names": List[str],
        "Arns": List[str],
        "Type": VisibilityTypeType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeImagesResultResponseTypeDef = TypedDict(
    "DescribeImagesResultResponseTypeDef",
    {
        "Images": List["ImageTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeSessionsRequestTypeDef = TypedDict(
    "_RequiredDescribeSessionsRequestTypeDef",
    {
        "StackName": str,
        "FleetName": str,
    },
)
_OptionalDescribeSessionsRequestTypeDef = TypedDict(
    "_OptionalDescribeSessionsRequestTypeDef",
    {
        "UserId": str,
        "NextToken": str,
        "Limit": int,
        "AuthenticationType": AuthenticationTypeType,
    },
    total=False,
)


class DescribeSessionsRequestTypeDef(
    _RequiredDescribeSessionsRequestTypeDef, _OptionalDescribeSessionsRequestTypeDef
):
    pass


DescribeSessionsResultResponseTypeDef = TypedDict(
    "DescribeSessionsResultResponseTypeDef",
    {
        "Sessions": List["SessionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStacksRequestTypeDef = TypedDict(
    "DescribeStacksRequestTypeDef",
    {
        "Names": List[str],
        "NextToken": str,
    },
    total=False,
)

DescribeStacksResultResponseTypeDef = TypedDict(
    "DescribeStacksResultResponseTypeDef",
    {
        "Stacks": List["StackTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUsageReportSubscriptionsRequestTypeDef = TypedDict(
    "DescribeUsageReportSubscriptionsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeUsageReportSubscriptionsResultResponseTypeDef = TypedDict(
    "DescribeUsageReportSubscriptionsResultResponseTypeDef",
    {
        "UsageReportSubscriptions": List["UsageReportSubscriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserStackAssociationsRequestTypeDef = TypedDict(
    "DescribeUserStackAssociationsRequestTypeDef",
    {
        "StackName": str,
        "UserName": str,
        "AuthenticationType": AuthenticationTypeType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeUserStackAssociationsResultResponseTypeDef = TypedDict(
    "DescribeUserStackAssociationsResultResponseTypeDef",
    {
        "UserStackAssociations": List["UserStackAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeUsersRequestTypeDef = TypedDict(
    "_RequiredDescribeUsersRequestTypeDef",
    {
        "AuthenticationType": AuthenticationTypeType,
    },
)
_OptionalDescribeUsersRequestTypeDef = TypedDict(
    "_OptionalDescribeUsersRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeUsersRequestTypeDef(
    _RequiredDescribeUsersRequestTypeDef, _OptionalDescribeUsersRequestTypeDef
):
    pass


DescribeUsersResultResponseTypeDef = TypedDict(
    "DescribeUsersResultResponseTypeDef",
    {
        "Users": List["UserTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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


DisableUserRequestTypeDef = TypedDict(
    "DisableUserRequestTypeDef",
    {
        "UserName": str,
        "AuthenticationType": AuthenticationTypeType,
    },
)

DisassociateFleetRequestTypeDef = TypedDict(
    "DisassociateFleetRequestTypeDef",
    {
        "FleetName": str,
        "StackName": str,
    },
)

DomainJoinInfoTypeDef = TypedDict(
    "DomainJoinInfoTypeDef",
    {
        "DirectoryName": str,
        "OrganizationalUnitDistinguishedName": str,
    },
    total=False,
)

EnableUserRequestTypeDef = TypedDict(
    "EnableUserRequestTypeDef",
    {
        "UserName": str,
        "AuthenticationType": AuthenticationTypeType,
    },
)

ExpireSessionRequestTypeDef = TypedDict(
    "ExpireSessionRequestTypeDef",
    {
        "SessionId": str,
    },
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

_RequiredListAssociatedFleetsRequestTypeDef = TypedDict(
    "_RequiredListAssociatedFleetsRequestTypeDef",
    {
        "StackName": str,
    },
)
_OptionalListAssociatedFleetsRequestTypeDef = TypedDict(
    "_OptionalListAssociatedFleetsRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListAssociatedFleetsRequestTypeDef(
    _RequiredListAssociatedFleetsRequestTypeDef, _OptionalListAssociatedFleetsRequestTypeDef
):
    pass


ListAssociatedFleetsResultResponseTypeDef = TypedDict(
    "ListAssociatedFleetsResultResponseTypeDef",
    {
        "Names": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAssociatedStacksRequestTypeDef = TypedDict(
    "_RequiredListAssociatedStacksRequestTypeDef",
    {
        "FleetName": str,
    },
)
_OptionalListAssociatedStacksRequestTypeDef = TypedDict(
    "_OptionalListAssociatedStacksRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListAssociatedStacksRequestTypeDef(
    _RequiredListAssociatedStacksRequestTypeDef, _OptionalListAssociatedStacksRequestTypeDef
):
    pass


ListAssociatedStacksResultResponseTypeDef = TypedDict(
    "ListAssociatedStacksResultResponseTypeDef",
    {
        "Names": List[str],
        "NextToken": str,
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


StartFleetRequestTypeDef = TypedDict(
    "StartFleetRequestTypeDef",
    {
        "Name": str,
    },
)

_RequiredStartImageBuilderRequestTypeDef = TypedDict(
    "_RequiredStartImageBuilderRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalStartImageBuilderRequestTypeDef = TypedDict(
    "_OptionalStartImageBuilderRequestTypeDef",
    {
        "AppstreamAgentVersion": str,
    },
    total=False,
)


class StartImageBuilderRequestTypeDef(
    _RequiredStartImageBuilderRequestTypeDef, _OptionalStartImageBuilderRequestTypeDef
):
    pass


StartImageBuilderResultResponseTypeDef = TypedDict(
    "StartImageBuilderResultResponseTypeDef",
    {
        "ImageBuilder": "ImageBuilderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopFleetRequestTypeDef = TypedDict(
    "StopFleetRequestTypeDef",
    {
        "Name": str,
    },
)

StopImageBuilderRequestTypeDef = TypedDict(
    "StopImageBuilderRequestTypeDef",
    {
        "Name": str,
    },
)

StopImageBuilderResultResponseTypeDef = TypedDict(
    "StopImageBuilderResultResponseTypeDef",
    {
        "ImageBuilder": "ImageBuilderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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


TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateDirectoryConfigRequestTypeDef = TypedDict(
    "_RequiredUpdateDirectoryConfigRequestTypeDef",
    {
        "DirectoryName": str,
    },
)
_OptionalUpdateDirectoryConfigRequestTypeDef = TypedDict(
    "_OptionalUpdateDirectoryConfigRequestTypeDef",
    {
        "OrganizationalUnitDistinguishedNames": List[str],
        "ServiceAccountCredentials": "ServiceAccountCredentialsTypeDef",
    },
    total=False,
)


class UpdateDirectoryConfigRequestTypeDef(
    _RequiredUpdateDirectoryConfigRequestTypeDef, _OptionalUpdateDirectoryConfigRequestTypeDef
):
    pass


UpdateDirectoryConfigResultResponseTypeDef = TypedDict(
    "UpdateDirectoryConfigResultResponseTypeDef",
    {
        "DirectoryConfig": "DirectoryConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFleetRequestTypeDef = TypedDict(
    "UpdateFleetRequestTypeDef",
    {
        "ImageName": str,
        "ImageArn": str,
        "Name": str,
        "InstanceType": str,
        "ComputeCapacity": "ComputeCapacityTypeDef",
        "VpcConfig": "VpcConfigTypeDef",
        "MaxUserDurationInSeconds": int,
        "DisconnectTimeoutInSeconds": int,
        "DeleteVpcConfig": bool,
        "Description": str,
        "DisplayName": str,
        "EnableDefaultInternetAccess": bool,
        "DomainJoinInfo": "DomainJoinInfoTypeDef",
        "IdleDisconnectTimeoutInSeconds": int,
        "AttributesToDelete": List[FleetAttributeType],
        "IamRoleArn": str,
        "StreamView": StreamViewType,
    },
    total=False,
)

UpdateFleetResultResponseTypeDef = TypedDict(
    "UpdateFleetResultResponseTypeDef",
    {
        "Fleet": "FleetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateImagePermissionsRequestTypeDef = TypedDict(
    "UpdateImagePermissionsRequestTypeDef",
    {
        "Name": str,
        "SharedAccountId": str,
        "ImagePermissions": "ImagePermissionsTypeDef",
    },
)

_RequiredUpdateStackRequestTypeDef = TypedDict(
    "_RequiredUpdateStackRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateStackRequestTypeDef = TypedDict(
    "_OptionalUpdateStackRequestTypeDef",
    {
        "DisplayName": str,
        "Description": str,
        "StorageConnectors": List["StorageConnectorTypeDef"],
        "DeleteStorageConnectors": bool,
        "RedirectURL": str,
        "FeedbackURL": str,
        "AttributesToDelete": List[StackAttributeType],
        "UserSettings": List["UserSettingTypeDef"],
        "ApplicationSettings": "ApplicationSettingsTypeDef",
        "AccessEndpoints": List["AccessEndpointTypeDef"],
        "EmbedHostDomains": List[str],
    },
    total=False,
)


class UpdateStackRequestTypeDef(
    _RequiredUpdateStackRequestTypeDef, _OptionalUpdateStackRequestTypeDef
):
    pass


UpdateStackResultResponseTypeDef = TypedDict(
    "UpdateStackResultResponseTypeDef",
    {
        "Stack": "StackTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
