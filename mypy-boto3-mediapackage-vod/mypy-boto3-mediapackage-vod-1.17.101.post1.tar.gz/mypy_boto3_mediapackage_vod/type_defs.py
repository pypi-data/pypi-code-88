"""
Type annotations for mediapackage-vod service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mediapackage_vod.type_defs import AssetShallowTypeDef

    data: AssetShallowTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import (
    AdMarkersType,
    EncryptionMethodType,
    ManifestLayoutType,
    ProfileType,
    SegmentTemplateFormatType,
    StreamOrderType,
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
    "AssetShallowTypeDef",
    "AuthorizationTypeDef",
    "CmafEncryptionTypeDef",
    "CmafPackageTypeDef",
    "ConfigureLogsRequestTypeDef",
    "ConfigureLogsResponseResponseTypeDef",
    "CreateAssetRequestTypeDef",
    "CreateAssetResponseResponseTypeDef",
    "CreatePackagingConfigurationRequestTypeDef",
    "CreatePackagingConfigurationResponseResponseTypeDef",
    "CreatePackagingGroupRequestTypeDef",
    "CreatePackagingGroupResponseResponseTypeDef",
    "DashEncryptionTypeDef",
    "DashManifestTypeDef",
    "DashPackageTypeDef",
    "DeleteAssetRequestTypeDef",
    "DeletePackagingConfigurationRequestTypeDef",
    "DeletePackagingGroupRequestTypeDef",
    "DescribeAssetRequestTypeDef",
    "DescribeAssetResponseResponseTypeDef",
    "DescribePackagingConfigurationRequestTypeDef",
    "DescribePackagingConfigurationResponseResponseTypeDef",
    "DescribePackagingGroupRequestTypeDef",
    "DescribePackagingGroupResponseResponseTypeDef",
    "EgressAccessLogsTypeDef",
    "EgressEndpointTypeDef",
    "HlsEncryptionTypeDef",
    "HlsManifestTypeDef",
    "HlsPackageTypeDef",
    "ListAssetsRequestTypeDef",
    "ListAssetsResponseResponseTypeDef",
    "ListPackagingConfigurationsRequestTypeDef",
    "ListPackagingConfigurationsResponseResponseTypeDef",
    "ListPackagingGroupsRequestTypeDef",
    "ListPackagingGroupsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "MssEncryptionTypeDef",
    "MssManifestTypeDef",
    "MssPackageTypeDef",
    "PackagingConfigurationTypeDef",
    "PackagingGroupTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SpekeKeyProviderTypeDef",
    "StreamSelectionTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdatePackagingGroupRequestTypeDef",
    "UpdatePackagingGroupResponseResponseTypeDef",
)

AssetShallowTypeDef = TypedDict(
    "AssetShallowTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "Id": str,
        "PackagingGroupId": str,
        "ResourceId": str,
        "SourceArn": str,
        "SourceRoleArn": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

AuthorizationTypeDef = TypedDict(
    "AuthorizationTypeDef",
    {
        "CdnIdentifierSecret": str,
        "SecretsRoleArn": str,
    },
)

CmafEncryptionTypeDef = TypedDict(
    "CmafEncryptionTypeDef",
    {
        "SpekeKeyProvider": "SpekeKeyProviderTypeDef",
    },
)

_RequiredCmafPackageTypeDef = TypedDict(
    "_RequiredCmafPackageTypeDef",
    {
        "HlsManifests": List["HlsManifestTypeDef"],
    },
)
_OptionalCmafPackageTypeDef = TypedDict(
    "_OptionalCmafPackageTypeDef",
    {
        "Encryption": "CmafEncryptionTypeDef",
        "IncludeEncoderConfigurationInSegments": bool,
        "SegmentDurationSeconds": int,
    },
    total=False,
)


class CmafPackageTypeDef(_RequiredCmafPackageTypeDef, _OptionalCmafPackageTypeDef):
    pass


_RequiredConfigureLogsRequestTypeDef = TypedDict(
    "_RequiredConfigureLogsRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalConfigureLogsRequestTypeDef = TypedDict(
    "_OptionalConfigureLogsRequestTypeDef",
    {
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
    },
    total=False,
)


class ConfigureLogsRequestTypeDef(
    _RequiredConfigureLogsRequestTypeDef, _OptionalConfigureLogsRequestTypeDef
):
    pass


ConfigureLogsResponseResponseTypeDef = TypedDict(
    "ConfigureLogsResponseResponseTypeDef",
    {
        "Arn": str,
        "Authorization": "AuthorizationTypeDef",
        "DomainName": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "Id": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAssetRequestTypeDef = TypedDict(
    "_RequiredCreateAssetRequestTypeDef",
    {
        "Id": str,
        "PackagingGroupId": str,
        "SourceArn": str,
        "SourceRoleArn": str,
    },
)
_OptionalCreateAssetRequestTypeDef = TypedDict(
    "_OptionalCreateAssetRequestTypeDef",
    {
        "ResourceId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateAssetRequestTypeDef(
    _RequiredCreateAssetRequestTypeDef, _OptionalCreateAssetRequestTypeDef
):
    pass


CreateAssetResponseResponseTypeDef = TypedDict(
    "CreateAssetResponseResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "EgressEndpoints": List["EgressEndpointTypeDef"],
        "Id": str,
        "PackagingGroupId": str,
        "ResourceId": str,
        "SourceArn": str,
        "SourceRoleArn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePackagingConfigurationRequestTypeDef = TypedDict(
    "_RequiredCreatePackagingConfigurationRequestTypeDef",
    {
        "Id": str,
        "PackagingGroupId": str,
    },
)
_OptionalCreatePackagingConfigurationRequestTypeDef = TypedDict(
    "_OptionalCreatePackagingConfigurationRequestTypeDef",
    {
        "CmafPackage": "CmafPackageTypeDef",
        "DashPackage": "DashPackageTypeDef",
        "HlsPackage": "HlsPackageTypeDef",
        "MssPackage": "MssPackageTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreatePackagingConfigurationRequestTypeDef(
    _RequiredCreatePackagingConfigurationRequestTypeDef,
    _OptionalCreatePackagingConfigurationRequestTypeDef,
):
    pass


CreatePackagingConfigurationResponseResponseTypeDef = TypedDict(
    "CreatePackagingConfigurationResponseResponseTypeDef",
    {
        "Arn": str,
        "CmafPackage": "CmafPackageTypeDef",
        "DashPackage": "DashPackageTypeDef",
        "HlsPackage": "HlsPackageTypeDef",
        "Id": str,
        "MssPackage": "MssPackageTypeDef",
        "PackagingGroupId": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePackagingGroupRequestTypeDef = TypedDict(
    "_RequiredCreatePackagingGroupRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalCreatePackagingGroupRequestTypeDef = TypedDict(
    "_OptionalCreatePackagingGroupRequestTypeDef",
    {
        "Authorization": "AuthorizationTypeDef",
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreatePackagingGroupRequestTypeDef(
    _RequiredCreatePackagingGroupRequestTypeDef, _OptionalCreatePackagingGroupRequestTypeDef
):
    pass


CreatePackagingGroupResponseResponseTypeDef = TypedDict(
    "CreatePackagingGroupResponseResponseTypeDef",
    {
        "Arn": str,
        "Authorization": "AuthorizationTypeDef",
        "DomainName": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "Id": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DashEncryptionTypeDef = TypedDict(
    "DashEncryptionTypeDef",
    {
        "SpekeKeyProvider": "SpekeKeyProviderTypeDef",
    },
)

DashManifestTypeDef = TypedDict(
    "DashManifestTypeDef",
    {
        "ManifestLayout": ManifestLayoutType,
        "ManifestName": str,
        "MinBufferTimeSeconds": int,
        "Profile": ProfileType,
        "StreamSelection": "StreamSelectionTypeDef",
    },
    total=False,
)

_RequiredDashPackageTypeDef = TypedDict(
    "_RequiredDashPackageTypeDef",
    {
        "DashManifests": List["DashManifestTypeDef"],
    },
)
_OptionalDashPackageTypeDef = TypedDict(
    "_OptionalDashPackageTypeDef",
    {
        "Encryption": "DashEncryptionTypeDef",
        "IncludeEncoderConfigurationInSegments": bool,
        "PeriodTriggers": List[Literal["ADS"]],
        "SegmentDurationSeconds": int,
        "SegmentTemplateFormat": SegmentTemplateFormatType,
    },
    total=False,
)


class DashPackageTypeDef(_RequiredDashPackageTypeDef, _OptionalDashPackageTypeDef):
    pass


DeleteAssetRequestTypeDef = TypedDict(
    "DeleteAssetRequestTypeDef",
    {
        "Id": str,
    },
)

DeletePackagingConfigurationRequestTypeDef = TypedDict(
    "DeletePackagingConfigurationRequestTypeDef",
    {
        "Id": str,
    },
)

DeletePackagingGroupRequestTypeDef = TypedDict(
    "DeletePackagingGroupRequestTypeDef",
    {
        "Id": str,
    },
)

DescribeAssetRequestTypeDef = TypedDict(
    "DescribeAssetRequestTypeDef",
    {
        "Id": str,
    },
)

DescribeAssetResponseResponseTypeDef = TypedDict(
    "DescribeAssetResponseResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "EgressEndpoints": List["EgressEndpointTypeDef"],
        "Id": str,
        "PackagingGroupId": str,
        "ResourceId": str,
        "SourceArn": str,
        "SourceRoleArn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePackagingConfigurationRequestTypeDef = TypedDict(
    "DescribePackagingConfigurationRequestTypeDef",
    {
        "Id": str,
    },
)

DescribePackagingConfigurationResponseResponseTypeDef = TypedDict(
    "DescribePackagingConfigurationResponseResponseTypeDef",
    {
        "Arn": str,
        "CmafPackage": "CmafPackageTypeDef",
        "DashPackage": "DashPackageTypeDef",
        "HlsPackage": "HlsPackageTypeDef",
        "Id": str,
        "MssPackage": "MssPackageTypeDef",
        "PackagingGroupId": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePackagingGroupRequestTypeDef = TypedDict(
    "DescribePackagingGroupRequestTypeDef",
    {
        "Id": str,
    },
)

DescribePackagingGroupResponseResponseTypeDef = TypedDict(
    "DescribePackagingGroupResponseResponseTypeDef",
    {
        "Arn": str,
        "Authorization": "AuthorizationTypeDef",
        "DomainName": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "Id": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EgressAccessLogsTypeDef = TypedDict(
    "EgressAccessLogsTypeDef",
    {
        "LogGroupName": str,
    },
    total=False,
)

EgressEndpointTypeDef = TypedDict(
    "EgressEndpointTypeDef",
    {
        "PackagingConfigurationId": str,
        "Url": str,
    },
    total=False,
)

_RequiredHlsEncryptionTypeDef = TypedDict(
    "_RequiredHlsEncryptionTypeDef",
    {
        "SpekeKeyProvider": "SpekeKeyProviderTypeDef",
    },
)
_OptionalHlsEncryptionTypeDef = TypedDict(
    "_OptionalHlsEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": EncryptionMethodType,
    },
    total=False,
)


class HlsEncryptionTypeDef(_RequiredHlsEncryptionTypeDef, _OptionalHlsEncryptionTypeDef):
    pass


HlsManifestTypeDef = TypedDict(
    "HlsManifestTypeDef",
    {
        "AdMarkers": AdMarkersType,
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "ProgramDateTimeIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "StreamSelection": "StreamSelectionTypeDef",
    },
    total=False,
)

_RequiredHlsPackageTypeDef = TypedDict(
    "_RequiredHlsPackageTypeDef",
    {
        "HlsManifests": List["HlsManifestTypeDef"],
    },
)
_OptionalHlsPackageTypeDef = TypedDict(
    "_OptionalHlsPackageTypeDef",
    {
        "Encryption": "HlsEncryptionTypeDef",
        "SegmentDurationSeconds": int,
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)


class HlsPackageTypeDef(_RequiredHlsPackageTypeDef, _OptionalHlsPackageTypeDef):
    pass


ListAssetsRequestTypeDef = TypedDict(
    "ListAssetsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "PackagingGroupId": str,
    },
    total=False,
)

ListAssetsResponseResponseTypeDef = TypedDict(
    "ListAssetsResponseResponseTypeDef",
    {
        "Assets": List["AssetShallowTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPackagingConfigurationsRequestTypeDef = TypedDict(
    "ListPackagingConfigurationsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "PackagingGroupId": str,
    },
    total=False,
)

ListPackagingConfigurationsResponseResponseTypeDef = TypedDict(
    "ListPackagingConfigurationsResponseResponseTypeDef",
    {
        "NextToken": str,
        "PackagingConfigurations": List["PackagingConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPackagingGroupsRequestTypeDef = TypedDict(
    "ListPackagingGroupsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListPackagingGroupsResponseResponseTypeDef = TypedDict(
    "ListPackagingGroupsResponseResponseTypeDef",
    {
        "NextToken": str,
        "PackagingGroups": List["PackagingGroupTypeDef"],
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

MssEncryptionTypeDef = TypedDict(
    "MssEncryptionTypeDef",
    {
        "SpekeKeyProvider": "SpekeKeyProviderTypeDef",
    },
)

MssManifestTypeDef = TypedDict(
    "MssManifestTypeDef",
    {
        "ManifestName": str,
        "StreamSelection": "StreamSelectionTypeDef",
    },
    total=False,
)

_RequiredMssPackageTypeDef = TypedDict(
    "_RequiredMssPackageTypeDef",
    {
        "MssManifests": List["MssManifestTypeDef"],
    },
)
_OptionalMssPackageTypeDef = TypedDict(
    "_OptionalMssPackageTypeDef",
    {
        "Encryption": "MssEncryptionTypeDef",
        "SegmentDurationSeconds": int,
    },
    total=False,
)


class MssPackageTypeDef(_RequiredMssPackageTypeDef, _OptionalMssPackageTypeDef):
    pass


PackagingConfigurationTypeDef = TypedDict(
    "PackagingConfigurationTypeDef",
    {
        "Arn": str,
        "CmafPackage": "CmafPackageTypeDef",
        "DashPackage": "DashPackageTypeDef",
        "HlsPackage": "HlsPackageTypeDef",
        "Id": str,
        "MssPackage": "MssPackageTypeDef",
        "PackagingGroupId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

PackagingGroupTypeDef = TypedDict(
    "PackagingGroupTypeDef",
    {
        "Arn": str,
        "Authorization": "AuthorizationTypeDef",
        "DomainName": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "Id": str,
        "Tags": Dict[str, str],
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

SpekeKeyProviderTypeDef = TypedDict(
    "SpekeKeyProviderTypeDef",
    {
        "RoleArn": str,
        "SystemIds": List[str],
        "Url": str,
    },
)

StreamSelectionTypeDef = TypedDict(
    "StreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": StreamOrderType,
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

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdatePackagingGroupRequestTypeDef = TypedDict(
    "_RequiredUpdatePackagingGroupRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalUpdatePackagingGroupRequestTypeDef = TypedDict(
    "_OptionalUpdatePackagingGroupRequestTypeDef",
    {
        "Authorization": "AuthorizationTypeDef",
    },
    total=False,
)


class UpdatePackagingGroupRequestTypeDef(
    _RequiredUpdatePackagingGroupRequestTypeDef, _OptionalUpdatePackagingGroupRequestTypeDef
):
    pass


UpdatePackagingGroupResponseResponseTypeDef = TypedDict(
    "UpdatePackagingGroupResponseResponseTypeDef",
    {
        "Arn": str,
        "Authorization": "AuthorizationTypeDef",
        "DomainName": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "Id": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
