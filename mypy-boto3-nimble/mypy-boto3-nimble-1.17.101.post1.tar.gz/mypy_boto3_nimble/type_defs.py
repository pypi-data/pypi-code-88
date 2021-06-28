"""
Type annotations for nimble service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/type_defs.html)

Usage::

    ```python
    from mypy_boto3_nimble.type_defs import AcceptEulasRequestTypeDef

    data: AcceptEulasRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    LaunchProfilePlatformType,
    LaunchProfileStateType,
    LaunchProfileStatusCodeType,
    StreamingClipboardModeType,
    StreamingImageStateType,
    StreamingImageStatusCodeType,
    StreamingInstanceTypeType,
    StreamingSessionStateType,
    StreamingSessionStatusCodeType,
    StreamingSessionStreamStateType,
    StreamingSessionStreamStatusCodeType,
    StudioComponentInitializationScriptRunContextType,
    StudioComponentStateType,
    StudioComponentStatusCodeType,
    StudioComponentSubtypeType,
    StudioComponentTypeType,
    StudioEncryptionConfigurationKeyTypeType,
    StudioStateType,
    StudioStatusCodeType,
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
    "AcceptEulasRequestTypeDef",
    "AcceptEulasResponseResponseTypeDef",
    "ActiveDirectoryComputerAttributeTypeDef",
    "ActiveDirectoryConfigurationTypeDef",
    "ComputeFarmConfigurationTypeDef",
    "CreateLaunchProfileRequestTypeDef",
    "CreateLaunchProfileResponseResponseTypeDef",
    "CreateStreamingImageRequestTypeDef",
    "CreateStreamingImageResponseResponseTypeDef",
    "CreateStreamingSessionRequestTypeDef",
    "CreateStreamingSessionResponseResponseTypeDef",
    "CreateStreamingSessionStreamRequestTypeDef",
    "CreateStreamingSessionStreamResponseResponseTypeDef",
    "CreateStudioComponentRequestTypeDef",
    "CreateStudioComponentResponseResponseTypeDef",
    "CreateStudioRequestTypeDef",
    "CreateStudioResponseResponseTypeDef",
    "DeleteLaunchProfileMemberRequestTypeDef",
    "DeleteLaunchProfileRequestTypeDef",
    "DeleteLaunchProfileResponseResponseTypeDef",
    "DeleteStreamingImageRequestTypeDef",
    "DeleteStreamingImageResponseResponseTypeDef",
    "DeleteStreamingSessionRequestTypeDef",
    "DeleteStreamingSessionResponseResponseTypeDef",
    "DeleteStudioComponentRequestTypeDef",
    "DeleteStudioComponentResponseResponseTypeDef",
    "DeleteStudioMemberRequestTypeDef",
    "DeleteStudioRequestTypeDef",
    "DeleteStudioResponseResponseTypeDef",
    "EulaAcceptanceTypeDef",
    "EulaTypeDef",
    "GetEulaRequestTypeDef",
    "GetEulaResponseResponseTypeDef",
    "GetLaunchProfileDetailsRequestTypeDef",
    "GetLaunchProfileDetailsResponseResponseTypeDef",
    "GetLaunchProfileInitializationRequestTypeDef",
    "GetLaunchProfileInitializationResponseResponseTypeDef",
    "GetLaunchProfileMemberRequestTypeDef",
    "GetLaunchProfileMemberResponseResponseTypeDef",
    "GetLaunchProfileRequestTypeDef",
    "GetLaunchProfileResponseResponseTypeDef",
    "GetStreamingImageRequestTypeDef",
    "GetStreamingImageResponseResponseTypeDef",
    "GetStreamingSessionRequestTypeDef",
    "GetStreamingSessionResponseResponseTypeDef",
    "GetStreamingSessionStreamRequestTypeDef",
    "GetStreamingSessionStreamResponseResponseTypeDef",
    "GetStudioComponentRequestTypeDef",
    "GetStudioComponentResponseResponseTypeDef",
    "GetStudioMemberRequestTypeDef",
    "GetStudioMemberResponseResponseTypeDef",
    "GetStudioRequestTypeDef",
    "GetStudioResponseResponseTypeDef",
    "LaunchProfileInitializationActiveDirectoryTypeDef",
    "LaunchProfileInitializationScriptTypeDef",
    "LaunchProfileInitializationTypeDef",
    "LaunchProfileMembershipTypeDef",
    "LaunchProfileTypeDef",
    "LicenseServiceConfigurationTypeDef",
    "ListEulaAcceptancesRequestTypeDef",
    "ListEulaAcceptancesResponseResponseTypeDef",
    "ListEulasRequestTypeDef",
    "ListEulasResponseResponseTypeDef",
    "ListLaunchProfileMembersRequestTypeDef",
    "ListLaunchProfileMembersResponseResponseTypeDef",
    "ListLaunchProfilesRequestTypeDef",
    "ListLaunchProfilesResponseResponseTypeDef",
    "ListStreamingImagesRequestTypeDef",
    "ListStreamingImagesResponseResponseTypeDef",
    "ListStreamingSessionsRequestTypeDef",
    "ListStreamingSessionsResponseResponseTypeDef",
    "ListStudioComponentsRequestTypeDef",
    "ListStudioComponentsResponseResponseTypeDef",
    "ListStudioMembersRequestTypeDef",
    "ListStudioMembersResponseResponseTypeDef",
    "ListStudiosRequestTypeDef",
    "ListStudiosResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "NewLaunchProfileMemberTypeDef",
    "NewStudioMemberTypeDef",
    "PaginatorConfigTypeDef",
    "PutLaunchProfileMembersRequestTypeDef",
    "PutStudioMembersRequestTypeDef",
    "ResponseMetadataTypeDef",
    "ScriptParameterKeyValueTypeDef",
    "SharedFileSystemConfigurationTypeDef",
    "StartStudioSSOConfigurationRepairRequestTypeDef",
    "StartStudioSSOConfigurationRepairResponseResponseTypeDef",
    "StreamConfigurationCreateTypeDef",
    "StreamConfigurationTypeDef",
    "StreamingImageEncryptionConfigurationTypeDef",
    "StreamingImageTypeDef",
    "StreamingSessionStreamTypeDef",
    "StreamingSessionTypeDef",
    "StudioComponentConfigurationTypeDef",
    "StudioComponentInitializationScriptTypeDef",
    "StudioComponentSummaryTypeDef",
    "StudioComponentTypeDef",
    "StudioEncryptionConfigurationTypeDef",
    "StudioMembershipTypeDef",
    "StudioTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateLaunchProfileMemberRequestTypeDef",
    "UpdateLaunchProfileMemberResponseResponseTypeDef",
    "UpdateLaunchProfileRequestTypeDef",
    "UpdateLaunchProfileResponseResponseTypeDef",
    "UpdateStreamingImageRequestTypeDef",
    "UpdateStreamingImageResponseResponseTypeDef",
    "UpdateStudioComponentRequestTypeDef",
    "UpdateStudioComponentResponseResponseTypeDef",
    "UpdateStudioRequestTypeDef",
    "UpdateStudioResponseResponseTypeDef",
)

_RequiredAcceptEulasRequestTypeDef = TypedDict(
    "_RequiredAcceptEulasRequestTypeDef",
    {
        "studioId": str,
    },
)
_OptionalAcceptEulasRequestTypeDef = TypedDict(
    "_OptionalAcceptEulasRequestTypeDef",
    {
        "clientToken": str,
        "eulaIds": List[str],
    },
    total=False,
)


class AcceptEulasRequestTypeDef(
    _RequiredAcceptEulasRequestTypeDef, _OptionalAcceptEulasRequestTypeDef
):
    pass


AcceptEulasResponseResponseTypeDef = TypedDict(
    "AcceptEulasResponseResponseTypeDef",
    {
        "eulaAcceptances": List["EulaAcceptanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ActiveDirectoryComputerAttributeTypeDef = TypedDict(
    "ActiveDirectoryComputerAttributeTypeDef",
    {
        "name": str,
        "value": str,
    },
    total=False,
)

ActiveDirectoryConfigurationTypeDef = TypedDict(
    "ActiveDirectoryConfigurationTypeDef",
    {
        "computerAttributes": List["ActiveDirectoryComputerAttributeTypeDef"],
        "directoryId": str,
        "organizationalUnitDistinguishedName": str,
    },
    total=False,
)

ComputeFarmConfigurationTypeDef = TypedDict(
    "ComputeFarmConfigurationTypeDef",
    {
        "activeDirectoryUser": str,
        "endpoint": str,
    },
    total=False,
)

_RequiredCreateLaunchProfileRequestTypeDef = TypedDict(
    "_RequiredCreateLaunchProfileRequestTypeDef",
    {
        "ec2SubnetIds": List[str],
        "launchProfileProtocolVersions": List[str],
        "name": str,
        "streamConfiguration": "StreamConfigurationCreateTypeDef",
        "studioComponentIds": List[str],
        "studioId": str,
    },
)
_OptionalCreateLaunchProfileRequestTypeDef = TypedDict(
    "_OptionalCreateLaunchProfileRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateLaunchProfileRequestTypeDef(
    _RequiredCreateLaunchProfileRequestTypeDef, _OptionalCreateLaunchProfileRequestTypeDef
):
    pass


CreateLaunchProfileResponseResponseTypeDef = TypedDict(
    "CreateLaunchProfileResponseResponseTypeDef",
    {
        "launchProfile": "LaunchProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStreamingImageRequestTypeDef = TypedDict(
    "_RequiredCreateStreamingImageRequestTypeDef",
    {
        "ec2ImageId": str,
        "name": str,
        "studioId": str,
    },
)
_OptionalCreateStreamingImageRequestTypeDef = TypedDict(
    "_OptionalCreateStreamingImageRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateStreamingImageRequestTypeDef(
    _RequiredCreateStreamingImageRequestTypeDef, _OptionalCreateStreamingImageRequestTypeDef
):
    pass


CreateStreamingImageResponseResponseTypeDef = TypedDict(
    "CreateStreamingImageResponseResponseTypeDef",
    {
        "streamingImage": "StreamingImageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStreamingSessionRequestTypeDef = TypedDict(
    "_RequiredCreateStreamingSessionRequestTypeDef",
    {
        "studioId": str,
    },
)
_OptionalCreateStreamingSessionRequestTypeDef = TypedDict(
    "_OptionalCreateStreamingSessionRequestTypeDef",
    {
        "clientToken": str,
        "ec2InstanceType": StreamingInstanceTypeType,
        "launchProfileId": str,
        "streamingImageId": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateStreamingSessionRequestTypeDef(
    _RequiredCreateStreamingSessionRequestTypeDef, _OptionalCreateStreamingSessionRequestTypeDef
):
    pass


CreateStreamingSessionResponseResponseTypeDef = TypedDict(
    "CreateStreamingSessionResponseResponseTypeDef",
    {
        "session": "StreamingSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStreamingSessionStreamRequestTypeDef = TypedDict(
    "_RequiredCreateStreamingSessionStreamRequestTypeDef",
    {
        "sessionId": str,
        "studioId": str,
    },
)
_OptionalCreateStreamingSessionStreamRequestTypeDef = TypedDict(
    "_OptionalCreateStreamingSessionStreamRequestTypeDef",
    {
        "clientToken": str,
        "expirationInSeconds": int,
    },
    total=False,
)


class CreateStreamingSessionStreamRequestTypeDef(
    _RequiredCreateStreamingSessionStreamRequestTypeDef,
    _OptionalCreateStreamingSessionStreamRequestTypeDef,
):
    pass


CreateStreamingSessionStreamResponseResponseTypeDef = TypedDict(
    "CreateStreamingSessionStreamResponseResponseTypeDef",
    {
        "stream": "StreamingSessionStreamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStudioComponentRequestTypeDef = TypedDict(
    "_RequiredCreateStudioComponentRequestTypeDef",
    {
        "name": str,
        "studioId": str,
        "type": StudioComponentTypeType,
    },
)
_OptionalCreateStudioComponentRequestTypeDef = TypedDict(
    "_OptionalCreateStudioComponentRequestTypeDef",
    {
        "clientToken": str,
        "configuration": "StudioComponentConfigurationTypeDef",
        "description": str,
        "ec2SecurityGroupIds": List[str],
        "initializationScripts": List["StudioComponentInitializationScriptTypeDef"],
        "scriptParameters": List["ScriptParameterKeyValueTypeDef"],
        "subtype": StudioComponentSubtypeType,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateStudioComponentRequestTypeDef(
    _RequiredCreateStudioComponentRequestTypeDef, _OptionalCreateStudioComponentRequestTypeDef
):
    pass


CreateStudioComponentResponseResponseTypeDef = TypedDict(
    "CreateStudioComponentResponseResponseTypeDef",
    {
        "studioComponent": "StudioComponentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStudioRequestTypeDef = TypedDict(
    "_RequiredCreateStudioRequestTypeDef",
    {
        "adminRoleArn": str,
        "displayName": str,
        "studioName": str,
        "userRoleArn": str,
    },
)
_OptionalCreateStudioRequestTypeDef = TypedDict(
    "_OptionalCreateStudioRequestTypeDef",
    {
        "clientToken": str,
        "studioEncryptionConfiguration": "StudioEncryptionConfigurationTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateStudioRequestTypeDef(
    _RequiredCreateStudioRequestTypeDef, _OptionalCreateStudioRequestTypeDef
):
    pass


CreateStudioResponseResponseTypeDef = TypedDict(
    "CreateStudioResponseResponseTypeDef",
    {
        "studio": "StudioTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteLaunchProfileMemberRequestTypeDef = TypedDict(
    "_RequiredDeleteLaunchProfileMemberRequestTypeDef",
    {
        "launchProfileId": str,
        "principalId": str,
        "studioId": str,
    },
)
_OptionalDeleteLaunchProfileMemberRequestTypeDef = TypedDict(
    "_OptionalDeleteLaunchProfileMemberRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class DeleteLaunchProfileMemberRequestTypeDef(
    _RequiredDeleteLaunchProfileMemberRequestTypeDef,
    _OptionalDeleteLaunchProfileMemberRequestTypeDef,
):
    pass


_RequiredDeleteLaunchProfileRequestTypeDef = TypedDict(
    "_RequiredDeleteLaunchProfileRequestTypeDef",
    {
        "launchProfileId": str,
        "studioId": str,
    },
)
_OptionalDeleteLaunchProfileRequestTypeDef = TypedDict(
    "_OptionalDeleteLaunchProfileRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class DeleteLaunchProfileRequestTypeDef(
    _RequiredDeleteLaunchProfileRequestTypeDef, _OptionalDeleteLaunchProfileRequestTypeDef
):
    pass


DeleteLaunchProfileResponseResponseTypeDef = TypedDict(
    "DeleteLaunchProfileResponseResponseTypeDef",
    {
        "launchProfile": "LaunchProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteStreamingImageRequestTypeDef = TypedDict(
    "_RequiredDeleteStreamingImageRequestTypeDef",
    {
        "streamingImageId": str,
        "studioId": str,
    },
)
_OptionalDeleteStreamingImageRequestTypeDef = TypedDict(
    "_OptionalDeleteStreamingImageRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class DeleteStreamingImageRequestTypeDef(
    _RequiredDeleteStreamingImageRequestTypeDef, _OptionalDeleteStreamingImageRequestTypeDef
):
    pass


DeleteStreamingImageResponseResponseTypeDef = TypedDict(
    "DeleteStreamingImageResponseResponseTypeDef",
    {
        "streamingImage": "StreamingImageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteStreamingSessionRequestTypeDef = TypedDict(
    "_RequiredDeleteStreamingSessionRequestTypeDef",
    {
        "sessionId": str,
        "studioId": str,
    },
)
_OptionalDeleteStreamingSessionRequestTypeDef = TypedDict(
    "_OptionalDeleteStreamingSessionRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class DeleteStreamingSessionRequestTypeDef(
    _RequiredDeleteStreamingSessionRequestTypeDef, _OptionalDeleteStreamingSessionRequestTypeDef
):
    pass


DeleteStreamingSessionResponseResponseTypeDef = TypedDict(
    "DeleteStreamingSessionResponseResponseTypeDef",
    {
        "session": "StreamingSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteStudioComponentRequestTypeDef = TypedDict(
    "_RequiredDeleteStudioComponentRequestTypeDef",
    {
        "studioComponentId": str,
        "studioId": str,
    },
)
_OptionalDeleteStudioComponentRequestTypeDef = TypedDict(
    "_OptionalDeleteStudioComponentRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class DeleteStudioComponentRequestTypeDef(
    _RequiredDeleteStudioComponentRequestTypeDef, _OptionalDeleteStudioComponentRequestTypeDef
):
    pass


DeleteStudioComponentResponseResponseTypeDef = TypedDict(
    "DeleteStudioComponentResponseResponseTypeDef",
    {
        "studioComponent": "StudioComponentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteStudioMemberRequestTypeDef = TypedDict(
    "_RequiredDeleteStudioMemberRequestTypeDef",
    {
        "principalId": str,
        "studioId": str,
    },
)
_OptionalDeleteStudioMemberRequestTypeDef = TypedDict(
    "_OptionalDeleteStudioMemberRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class DeleteStudioMemberRequestTypeDef(
    _RequiredDeleteStudioMemberRequestTypeDef, _OptionalDeleteStudioMemberRequestTypeDef
):
    pass


_RequiredDeleteStudioRequestTypeDef = TypedDict(
    "_RequiredDeleteStudioRequestTypeDef",
    {
        "studioId": str,
    },
)
_OptionalDeleteStudioRequestTypeDef = TypedDict(
    "_OptionalDeleteStudioRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class DeleteStudioRequestTypeDef(
    _RequiredDeleteStudioRequestTypeDef, _OptionalDeleteStudioRequestTypeDef
):
    pass


DeleteStudioResponseResponseTypeDef = TypedDict(
    "DeleteStudioResponseResponseTypeDef",
    {
        "studio": "StudioTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EulaAcceptanceTypeDef = TypedDict(
    "EulaAcceptanceTypeDef",
    {
        "acceptedAt": datetime,
        "acceptedBy": str,
        "accepteeId": str,
        "eulaAcceptanceId": str,
        "eulaId": str,
    },
    total=False,
)

EulaTypeDef = TypedDict(
    "EulaTypeDef",
    {
        "content": str,
        "createdAt": datetime,
        "eulaId": str,
        "name": str,
        "updatedAt": datetime,
    },
    total=False,
)

GetEulaRequestTypeDef = TypedDict(
    "GetEulaRequestTypeDef",
    {
        "eulaId": str,
    },
)

GetEulaResponseResponseTypeDef = TypedDict(
    "GetEulaResponseResponseTypeDef",
    {
        "eula": "EulaTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLaunchProfileDetailsRequestTypeDef = TypedDict(
    "GetLaunchProfileDetailsRequestTypeDef",
    {
        "launchProfileId": str,
        "studioId": str,
    },
)

GetLaunchProfileDetailsResponseResponseTypeDef = TypedDict(
    "GetLaunchProfileDetailsResponseResponseTypeDef",
    {
        "launchProfile": "LaunchProfileTypeDef",
        "streamingImages": List["StreamingImageTypeDef"],
        "studioComponentSummaries": List["StudioComponentSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLaunchProfileInitializationRequestTypeDef = TypedDict(
    "GetLaunchProfileInitializationRequestTypeDef",
    {
        "launchProfileId": str,
        "launchProfileProtocolVersions": List[str],
        "launchPurpose": str,
        "platform": str,
        "studioId": str,
    },
)

GetLaunchProfileInitializationResponseResponseTypeDef = TypedDict(
    "GetLaunchProfileInitializationResponseResponseTypeDef",
    {
        "launchProfileInitialization": "LaunchProfileInitializationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLaunchProfileMemberRequestTypeDef = TypedDict(
    "GetLaunchProfileMemberRequestTypeDef",
    {
        "launchProfileId": str,
        "principalId": str,
        "studioId": str,
    },
)

GetLaunchProfileMemberResponseResponseTypeDef = TypedDict(
    "GetLaunchProfileMemberResponseResponseTypeDef",
    {
        "member": "LaunchProfileMembershipTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLaunchProfileRequestTypeDef = TypedDict(
    "GetLaunchProfileRequestTypeDef",
    {
        "launchProfileId": str,
        "studioId": str,
    },
)

GetLaunchProfileResponseResponseTypeDef = TypedDict(
    "GetLaunchProfileResponseResponseTypeDef",
    {
        "launchProfile": "LaunchProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStreamingImageRequestTypeDef = TypedDict(
    "GetStreamingImageRequestTypeDef",
    {
        "streamingImageId": str,
        "studioId": str,
    },
)

GetStreamingImageResponseResponseTypeDef = TypedDict(
    "GetStreamingImageResponseResponseTypeDef",
    {
        "streamingImage": "StreamingImageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStreamingSessionRequestTypeDef = TypedDict(
    "GetStreamingSessionRequestTypeDef",
    {
        "sessionId": str,
        "studioId": str,
    },
)

GetStreamingSessionResponseResponseTypeDef = TypedDict(
    "GetStreamingSessionResponseResponseTypeDef",
    {
        "session": "StreamingSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStreamingSessionStreamRequestTypeDef = TypedDict(
    "GetStreamingSessionStreamRequestTypeDef",
    {
        "sessionId": str,
        "streamId": str,
        "studioId": str,
    },
)

GetStreamingSessionStreamResponseResponseTypeDef = TypedDict(
    "GetStreamingSessionStreamResponseResponseTypeDef",
    {
        "stream": "StreamingSessionStreamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStudioComponentRequestTypeDef = TypedDict(
    "GetStudioComponentRequestTypeDef",
    {
        "studioComponentId": str,
        "studioId": str,
    },
)

GetStudioComponentResponseResponseTypeDef = TypedDict(
    "GetStudioComponentResponseResponseTypeDef",
    {
        "studioComponent": "StudioComponentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStudioMemberRequestTypeDef = TypedDict(
    "GetStudioMemberRequestTypeDef",
    {
        "principalId": str,
        "studioId": str,
    },
)

GetStudioMemberResponseResponseTypeDef = TypedDict(
    "GetStudioMemberResponseResponseTypeDef",
    {
        "member": "StudioMembershipTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStudioRequestTypeDef = TypedDict(
    "GetStudioRequestTypeDef",
    {
        "studioId": str,
    },
)

GetStudioResponseResponseTypeDef = TypedDict(
    "GetStudioResponseResponseTypeDef",
    {
        "studio": "StudioTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LaunchProfileInitializationActiveDirectoryTypeDef = TypedDict(
    "LaunchProfileInitializationActiveDirectoryTypeDef",
    {
        "computerAttributes": List["ActiveDirectoryComputerAttributeTypeDef"],
        "directoryId": str,
        "directoryName": str,
        "dnsIpAddresses": List[str],
        "organizationalUnitDistinguishedName": str,
        "studioComponentId": str,
        "studioComponentName": str,
    },
    total=False,
)

LaunchProfileInitializationScriptTypeDef = TypedDict(
    "LaunchProfileInitializationScriptTypeDef",
    {
        "script": str,
        "studioComponentId": str,
        "studioComponentName": str,
    },
    total=False,
)

LaunchProfileInitializationTypeDef = TypedDict(
    "LaunchProfileInitializationTypeDef",
    {
        "activeDirectory": "LaunchProfileInitializationActiveDirectoryTypeDef",
        "ec2SecurityGroupIds": List[str],
        "launchProfileId": str,
        "launchProfileProtocolVersion": str,
        "launchPurpose": str,
        "name": str,
        "platform": LaunchProfilePlatformType,
        "systemInitializationScripts": List["LaunchProfileInitializationScriptTypeDef"],
        "userInitializationScripts": List["LaunchProfileInitializationScriptTypeDef"],
    },
    total=False,
)

LaunchProfileMembershipTypeDef = TypedDict(
    "LaunchProfileMembershipTypeDef",
    {
        "identityStoreId": str,
        "persona": Literal["USER"],
        "principalId": str,
    },
    total=False,
)

LaunchProfileTypeDef = TypedDict(
    "LaunchProfileTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "ec2SubnetIds": List[str],
        "launchProfileId": str,
        "launchProfileProtocolVersions": List[str],
        "name": str,
        "state": LaunchProfileStateType,
        "statusCode": LaunchProfileStatusCodeType,
        "statusMessage": str,
        "streamConfiguration": "StreamConfigurationTypeDef",
        "studioComponentIds": List[str],
        "tags": Dict[str, str],
        "updatedAt": datetime,
        "updatedBy": str,
    },
    total=False,
)

LicenseServiceConfigurationTypeDef = TypedDict(
    "LicenseServiceConfigurationTypeDef",
    {
        "endpoint": str,
    },
    total=False,
)

_RequiredListEulaAcceptancesRequestTypeDef = TypedDict(
    "_RequiredListEulaAcceptancesRequestTypeDef",
    {
        "studioId": str,
    },
)
_OptionalListEulaAcceptancesRequestTypeDef = TypedDict(
    "_OptionalListEulaAcceptancesRequestTypeDef",
    {
        "eulaIds": List[str],
        "nextToken": str,
    },
    total=False,
)


class ListEulaAcceptancesRequestTypeDef(
    _RequiredListEulaAcceptancesRequestTypeDef, _OptionalListEulaAcceptancesRequestTypeDef
):
    pass


ListEulaAcceptancesResponseResponseTypeDef = TypedDict(
    "ListEulaAcceptancesResponseResponseTypeDef",
    {
        "eulaAcceptances": List["EulaAcceptanceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEulasRequestTypeDef = TypedDict(
    "ListEulasRequestTypeDef",
    {
        "eulaIds": List[str],
        "nextToken": str,
    },
    total=False,
)

ListEulasResponseResponseTypeDef = TypedDict(
    "ListEulasResponseResponseTypeDef",
    {
        "eulas": List["EulaTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLaunchProfileMembersRequestTypeDef = TypedDict(
    "_RequiredListLaunchProfileMembersRequestTypeDef",
    {
        "launchProfileId": str,
        "studioId": str,
    },
)
_OptionalListLaunchProfileMembersRequestTypeDef = TypedDict(
    "_OptionalListLaunchProfileMembersRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListLaunchProfileMembersRequestTypeDef(
    _RequiredListLaunchProfileMembersRequestTypeDef, _OptionalListLaunchProfileMembersRequestTypeDef
):
    pass


ListLaunchProfileMembersResponseResponseTypeDef = TypedDict(
    "ListLaunchProfileMembersResponseResponseTypeDef",
    {
        "members": List["LaunchProfileMembershipTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLaunchProfilesRequestTypeDef = TypedDict(
    "_RequiredListLaunchProfilesRequestTypeDef",
    {
        "studioId": str,
    },
)
_OptionalListLaunchProfilesRequestTypeDef = TypedDict(
    "_OptionalListLaunchProfilesRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "principalId": str,
        "states": List[str],
    },
    total=False,
)


class ListLaunchProfilesRequestTypeDef(
    _RequiredListLaunchProfilesRequestTypeDef, _OptionalListLaunchProfilesRequestTypeDef
):
    pass


ListLaunchProfilesResponseResponseTypeDef = TypedDict(
    "ListLaunchProfilesResponseResponseTypeDef",
    {
        "launchProfiles": List["LaunchProfileTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStreamingImagesRequestTypeDef = TypedDict(
    "_RequiredListStreamingImagesRequestTypeDef",
    {
        "studioId": str,
    },
)
_OptionalListStreamingImagesRequestTypeDef = TypedDict(
    "_OptionalListStreamingImagesRequestTypeDef",
    {
        "nextToken": str,
        "owner": str,
    },
    total=False,
)


class ListStreamingImagesRequestTypeDef(
    _RequiredListStreamingImagesRequestTypeDef, _OptionalListStreamingImagesRequestTypeDef
):
    pass


ListStreamingImagesResponseResponseTypeDef = TypedDict(
    "ListStreamingImagesResponseResponseTypeDef",
    {
        "nextToken": str,
        "streamingImages": List["StreamingImageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStreamingSessionsRequestTypeDef = TypedDict(
    "_RequiredListStreamingSessionsRequestTypeDef",
    {
        "studioId": str,
    },
)
_OptionalListStreamingSessionsRequestTypeDef = TypedDict(
    "_OptionalListStreamingSessionsRequestTypeDef",
    {
        "createdBy": str,
        "nextToken": str,
        "sessionIds": str,
    },
    total=False,
)


class ListStreamingSessionsRequestTypeDef(
    _RequiredListStreamingSessionsRequestTypeDef, _OptionalListStreamingSessionsRequestTypeDef
):
    pass


ListStreamingSessionsResponseResponseTypeDef = TypedDict(
    "ListStreamingSessionsResponseResponseTypeDef",
    {
        "nextToken": str,
        "sessions": List["StreamingSessionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStudioComponentsRequestTypeDef = TypedDict(
    "_RequiredListStudioComponentsRequestTypeDef",
    {
        "studioId": str,
    },
)
_OptionalListStudioComponentsRequestTypeDef = TypedDict(
    "_OptionalListStudioComponentsRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "states": List[str],
        "types": List[str],
    },
    total=False,
)


class ListStudioComponentsRequestTypeDef(
    _RequiredListStudioComponentsRequestTypeDef, _OptionalListStudioComponentsRequestTypeDef
):
    pass


ListStudioComponentsResponseResponseTypeDef = TypedDict(
    "ListStudioComponentsResponseResponseTypeDef",
    {
        "nextToken": str,
        "studioComponents": List["StudioComponentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStudioMembersRequestTypeDef = TypedDict(
    "_RequiredListStudioMembersRequestTypeDef",
    {
        "studioId": str,
    },
)
_OptionalListStudioMembersRequestTypeDef = TypedDict(
    "_OptionalListStudioMembersRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListStudioMembersRequestTypeDef(
    _RequiredListStudioMembersRequestTypeDef, _OptionalListStudioMembersRequestTypeDef
):
    pass


ListStudioMembersResponseResponseTypeDef = TypedDict(
    "ListStudioMembersResponseResponseTypeDef",
    {
        "members": List["StudioMembershipTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStudiosRequestTypeDef = TypedDict(
    "ListStudiosRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

ListStudiosResponseResponseTypeDef = TypedDict(
    "ListStudiosResponseResponseTypeDef",
    {
        "nextToken": str,
        "studios": List["StudioTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NewLaunchProfileMemberTypeDef = TypedDict(
    "NewLaunchProfileMemberTypeDef",
    {
        "persona": Literal["USER"],
        "principalId": str,
    },
)

NewStudioMemberTypeDef = TypedDict(
    "NewStudioMemberTypeDef",
    {
        "persona": Literal["ADMINISTRATOR"],
        "principalId": str,
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

_RequiredPutLaunchProfileMembersRequestTypeDef = TypedDict(
    "_RequiredPutLaunchProfileMembersRequestTypeDef",
    {
        "identityStoreId": str,
        "launchProfileId": str,
        "members": List["NewLaunchProfileMemberTypeDef"],
        "studioId": str,
    },
)
_OptionalPutLaunchProfileMembersRequestTypeDef = TypedDict(
    "_OptionalPutLaunchProfileMembersRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class PutLaunchProfileMembersRequestTypeDef(
    _RequiredPutLaunchProfileMembersRequestTypeDef, _OptionalPutLaunchProfileMembersRequestTypeDef
):
    pass


_RequiredPutStudioMembersRequestTypeDef = TypedDict(
    "_RequiredPutStudioMembersRequestTypeDef",
    {
        "identityStoreId": str,
        "members": List["NewStudioMemberTypeDef"],
        "studioId": str,
    },
)
_OptionalPutStudioMembersRequestTypeDef = TypedDict(
    "_OptionalPutStudioMembersRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class PutStudioMembersRequestTypeDef(
    _RequiredPutStudioMembersRequestTypeDef, _OptionalPutStudioMembersRequestTypeDef
):
    pass


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

ScriptParameterKeyValueTypeDef = TypedDict(
    "ScriptParameterKeyValueTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

SharedFileSystemConfigurationTypeDef = TypedDict(
    "SharedFileSystemConfigurationTypeDef",
    {
        "endpoint": str,
        "fileSystemId": str,
        "linuxMountPoint": str,
        "shareName": str,
        "windowsMountDrive": str,
    },
    total=False,
)

_RequiredStartStudioSSOConfigurationRepairRequestTypeDef = TypedDict(
    "_RequiredStartStudioSSOConfigurationRepairRequestTypeDef",
    {
        "studioId": str,
    },
)
_OptionalStartStudioSSOConfigurationRepairRequestTypeDef = TypedDict(
    "_OptionalStartStudioSSOConfigurationRepairRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class StartStudioSSOConfigurationRepairRequestTypeDef(
    _RequiredStartStudioSSOConfigurationRepairRequestTypeDef,
    _OptionalStartStudioSSOConfigurationRepairRequestTypeDef,
):
    pass


StartStudioSSOConfigurationRepairResponseResponseTypeDef = TypedDict(
    "StartStudioSSOConfigurationRepairResponseResponseTypeDef",
    {
        "studio": "StudioTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStreamConfigurationCreateTypeDef = TypedDict(
    "_RequiredStreamConfigurationCreateTypeDef",
    {
        "clipboardMode": StreamingClipboardModeType,
        "ec2InstanceTypes": List[StreamingInstanceTypeType],
        "streamingImageIds": List[str],
    },
)
_OptionalStreamConfigurationCreateTypeDef = TypedDict(
    "_OptionalStreamConfigurationCreateTypeDef",
    {
        "maxSessionLengthInMinutes": int,
    },
    total=False,
)


class StreamConfigurationCreateTypeDef(
    _RequiredStreamConfigurationCreateTypeDef, _OptionalStreamConfigurationCreateTypeDef
):
    pass


StreamConfigurationTypeDef = TypedDict(
    "StreamConfigurationTypeDef",
    {
        "clipboardMode": StreamingClipboardModeType,
        "ec2InstanceTypes": List[StreamingInstanceTypeType],
        "maxSessionLengthInMinutes": int,
        "streamingImageIds": List[str],
    },
    total=False,
)

_RequiredStreamingImageEncryptionConfigurationTypeDef = TypedDict(
    "_RequiredStreamingImageEncryptionConfigurationTypeDef",
    {
        "keyType": Literal["CUSTOMER_MANAGED_KEY"],
    },
)
_OptionalStreamingImageEncryptionConfigurationTypeDef = TypedDict(
    "_OptionalStreamingImageEncryptionConfigurationTypeDef",
    {
        "keyArn": str,
    },
    total=False,
)


class StreamingImageEncryptionConfigurationTypeDef(
    _RequiredStreamingImageEncryptionConfigurationTypeDef,
    _OptionalStreamingImageEncryptionConfigurationTypeDef,
):
    pass


StreamingImageTypeDef = TypedDict(
    "StreamingImageTypeDef",
    {
        "arn": str,
        "description": str,
        "ec2ImageId": str,
        "encryptionConfiguration": "StreamingImageEncryptionConfigurationTypeDef",
        "eulaIds": List[str],
        "name": str,
        "owner": str,
        "platform": str,
        "state": StreamingImageStateType,
        "statusCode": StreamingImageStatusCodeType,
        "statusMessage": str,
        "streamingImageId": str,
        "tags": Dict[str, str],
    },
    total=False,
)

StreamingSessionStreamTypeDef = TypedDict(
    "StreamingSessionStreamTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "expiresAt": datetime,
        "state": StreamingSessionStreamStateType,
        "statusCode": StreamingSessionStreamStatusCodeType,
        "streamId": str,
        "url": str,
    },
    total=False,
)

StreamingSessionTypeDef = TypedDict(
    "StreamingSessionTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "createdBy": str,
        "ec2InstanceType": str,
        "launchProfileId": str,
        "sessionId": str,
        "state": StreamingSessionStateType,
        "statusCode": StreamingSessionStatusCodeType,
        "statusMessage": str,
        "streamingImageId": str,
        "tags": Dict[str, str],
        "terminateAt": datetime,
        "updatedAt": datetime,
        "updatedBy": str,
    },
    total=False,
)

StudioComponentConfigurationTypeDef = TypedDict(
    "StudioComponentConfigurationTypeDef",
    {
        "activeDirectoryConfiguration": "ActiveDirectoryConfigurationTypeDef",
        "computeFarmConfiguration": "ComputeFarmConfigurationTypeDef",
        "licenseServiceConfiguration": "LicenseServiceConfigurationTypeDef",
        "sharedFileSystemConfiguration": "SharedFileSystemConfigurationTypeDef",
    },
    total=False,
)

StudioComponentInitializationScriptTypeDef = TypedDict(
    "StudioComponentInitializationScriptTypeDef",
    {
        "launchProfileProtocolVersion": str,
        "platform": LaunchProfilePlatformType,
        "runContext": StudioComponentInitializationScriptRunContextType,
        "script": str,
    },
    total=False,
)

StudioComponentSummaryTypeDef = TypedDict(
    "StudioComponentSummaryTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "name": str,
        "studioComponentId": str,
        "subtype": StudioComponentSubtypeType,
        "type": StudioComponentTypeType,
        "updatedAt": datetime,
        "updatedBy": str,
    },
    total=False,
)

StudioComponentTypeDef = TypedDict(
    "StudioComponentTypeDef",
    {
        "arn": str,
        "configuration": "StudioComponentConfigurationTypeDef",
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "ec2SecurityGroupIds": List[str],
        "initializationScripts": List["StudioComponentInitializationScriptTypeDef"],
        "name": str,
        "scriptParameters": List["ScriptParameterKeyValueTypeDef"],
        "state": StudioComponentStateType,
        "statusCode": StudioComponentStatusCodeType,
        "statusMessage": str,
        "studioComponentId": str,
        "subtype": StudioComponentSubtypeType,
        "tags": Dict[str, str],
        "type": StudioComponentTypeType,
        "updatedAt": datetime,
        "updatedBy": str,
    },
    total=False,
)

_RequiredStudioEncryptionConfigurationTypeDef = TypedDict(
    "_RequiredStudioEncryptionConfigurationTypeDef",
    {
        "keyType": StudioEncryptionConfigurationKeyTypeType,
    },
)
_OptionalStudioEncryptionConfigurationTypeDef = TypedDict(
    "_OptionalStudioEncryptionConfigurationTypeDef",
    {
        "keyArn": str,
    },
    total=False,
)


class StudioEncryptionConfigurationTypeDef(
    _RequiredStudioEncryptionConfigurationTypeDef, _OptionalStudioEncryptionConfigurationTypeDef
):
    pass


StudioMembershipTypeDef = TypedDict(
    "StudioMembershipTypeDef",
    {
        "identityStoreId": str,
        "persona": Literal["ADMINISTRATOR"],
        "principalId": str,
    },
    total=False,
)

StudioTypeDef = TypedDict(
    "StudioTypeDef",
    {
        "adminRoleArn": str,
        "arn": str,
        "createdAt": datetime,
        "displayName": str,
        "homeRegion": str,
        "ssoClientId": str,
        "state": StudioStateType,
        "statusCode": StudioStatusCodeType,
        "statusMessage": str,
        "studioEncryptionConfiguration": "StudioEncryptionConfigurationTypeDef",
        "studioId": str,
        "studioName": str,
        "studioUrl": str,
        "tags": Dict[str, str],
        "updatedAt": datetime,
        "userRoleArn": str,
    },
    total=False,
)

_RequiredTagResourceRequestTypeDef = TypedDict(
    "_RequiredTagResourceRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalTagResourceRequestTypeDef = TypedDict(
    "_OptionalTagResourceRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)


class TagResourceRequestTypeDef(
    _RequiredTagResourceRequestTypeDef, _OptionalTagResourceRequestTypeDef
):
    pass


UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateLaunchProfileMemberRequestTypeDef = TypedDict(
    "_RequiredUpdateLaunchProfileMemberRequestTypeDef",
    {
        "launchProfileId": str,
        "persona": Literal["USER"],
        "principalId": str,
        "studioId": str,
    },
)
_OptionalUpdateLaunchProfileMemberRequestTypeDef = TypedDict(
    "_OptionalUpdateLaunchProfileMemberRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class UpdateLaunchProfileMemberRequestTypeDef(
    _RequiredUpdateLaunchProfileMemberRequestTypeDef,
    _OptionalUpdateLaunchProfileMemberRequestTypeDef,
):
    pass


UpdateLaunchProfileMemberResponseResponseTypeDef = TypedDict(
    "UpdateLaunchProfileMemberResponseResponseTypeDef",
    {
        "member": "LaunchProfileMembershipTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateLaunchProfileRequestTypeDef = TypedDict(
    "_RequiredUpdateLaunchProfileRequestTypeDef",
    {
        "launchProfileId": str,
        "studioId": str,
    },
)
_OptionalUpdateLaunchProfileRequestTypeDef = TypedDict(
    "_OptionalUpdateLaunchProfileRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "launchProfileProtocolVersions": List[str],
        "name": str,
        "streamConfiguration": "StreamConfigurationCreateTypeDef",
        "studioComponentIds": List[str],
    },
    total=False,
)


class UpdateLaunchProfileRequestTypeDef(
    _RequiredUpdateLaunchProfileRequestTypeDef, _OptionalUpdateLaunchProfileRequestTypeDef
):
    pass


UpdateLaunchProfileResponseResponseTypeDef = TypedDict(
    "UpdateLaunchProfileResponseResponseTypeDef",
    {
        "launchProfile": "LaunchProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateStreamingImageRequestTypeDef = TypedDict(
    "_RequiredUpdateStreamingImageRequestTypeDef",
    {
        "streamingImageId": str,
        "studioId": str,
    },
)
_OptionalUpdateStreamingImageRequestTypeDef = TypedDict(
    "_OptionalUpdateStreamingImageRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "name": str,
    },
    total=False,
)


class UpdateStreamingImageRequestTypeDef(
    _RequiredUpdateStreamingImageRequestTypeDef, _OptionalUpdateStreamingImageRequestTypeDef
):
    pass


UpdateStreamingImageResponseResponseTypeDef = TypedDict(
    "UpdateStreamingImageResponseResponseTypeDef",
    {
        "streamingImage": "StreamingImageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateStudioComponentRequestTypeDef = TypedDict(
    "_RequiredUpdateStudioComponentRequestTypeDef",
    {
        "studioComponentId": str,
        "studioId": str,
    },
)
_OptionalUpdateStudioComponentRequestTypeDef = TypedDict(
    "_OptionalUpdateStudioComponentRequestTypeDef",
    {
        "clientToken": str,
        "configuration": "StudioComponentConfigurationTypeDef",
        "description": str,
        "ec2SecurityGroupIds": List[str],
        "initializationScripts": List["StudioComponentInitializationScriptTypeDef"],
        "name": str,
        "scriptParameters": List["ScriptParameterKeyValueTypeDef"],
        "subtype": StudioComponentSubtypeType,
        "type": StudioComponentTypeType,
    },
    total=False,
)


class UpdateStudioComponentRequestTypeDef(
    _RequiredUpdateStudioComponentRequestTypeDef, _OptionalUpdateStudioComponentRequestTypeDef
):
    pass


UpdateStudioComponentResponseResponseTypeDef = TypedDict(
    "UpdateStudioComponentResponseResponseTypeDef",
    {
        "studioComponent": "StudioComponentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateStudioRequestTypeDef = TypedDict(
    "_RequiredUpdateStudioRequestTypeDef",
    {
        "studioId": str,
    },
)
_OptionalUpdateStudioRequestTypeDef = TypedDict(
    "_OptionalUpdateStudioRequestTypeDef",
    {
        "adminRoleArn": str,
        "clientToken": str,
        "displayName": str,
        "userRoleArn": str,
    },
    total=False,
)


class UpdateStudioRequestTypeDef(
    _RequiredUpdateStudioRequestTypeDef, _OptionalUpdateStudioRequestTypeDef
):
    pass


UpdateStudioResponseResponseTypeDef = TypedDict(
    "UpdateStudioResponseResponseTypeDef",
    {
        "studio": "StudioTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
