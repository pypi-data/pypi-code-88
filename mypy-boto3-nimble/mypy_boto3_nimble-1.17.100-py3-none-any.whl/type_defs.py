"""
Type annotations for nimble service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/type_defs.html)

Usage::

    ```python
    from mypy_boto3_nimble.type_defs import AcceptEulasResponseTypeDef

    data: AcceptEulasResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

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
    "AcceptEulasResponseTypeDef",
    "ActiveDirectoryComputerAttributeTypeDef",
    "ActiveDirectoryConfigurationTypeDef",
    "ComputeFarmConfigurationTypeDef",
    "CreateLaunchProfileResponseTypeDef",
    "CreateStreamingImageResponseTypeDef",
    "CreateStreamingSessionResponseTypeDef",
    "CreateStreamingSessionStreamResponseTypeDef",
    "CreateStudioComponentResponseTypeDef",
    "CreateStudioResponseTypeDef",
    "DeleteLaunchProfileResponseTypeDef",
    "DeleteStreamingImageResponseTypeDef",
    "DeleteStreamingSessionResponseTypeDef",
    "DeleteStudioComponentResponseTypeDef",
    "DeleteStudioResponseTypeDef",
    "EulaAcceptanceTypeDef",
    "EulaTypeDef",
    "GetEulaResponseTypeDef",
    "GetLaunchProfileDetailsResponseTypeDef",
    "GetLaunchProfileInitializationResponseTypeDef",
    "GetLaunchProfileMemberResponseTypeDef",
    "GetLaunchProfileResponseTypeDef",
    "GetStreamingImageResponseTypeDef",
    "GetStreamingSessionResponseTypeDef",
    "GetStreamingSessionStreamResponseTypeDef",
    "GetStudioComponentResponseTypeDef",
    "GetStudioMemberResponseTypeDef",
    "GetStudioResponseTypeDef",
    "LaunchProfileInitializationActiveDirectoryTypeDef",
    "LaunchProfileInitializationScriptTypeDef",
    "LaunchProfileInitializationTypeDef",
    "LaunchProfileMembershipTypeDef",
    "LaunchProfileTypeDef",
    "LicenseServiceConfigurationTypeDef",
    "ListEulaAcceptancesResponseTypeDef",
    "ListEulasResponseTypeDef",
    "ListLaunchProfileMembersResponseTypeDef",
    "ListLaunchProfilesResponseTypeDef",
    "ListStreamingImagesResponseTypeDef",
    "ListStreamingSessionsResponseTypeDef",
    "ListStudioComponentsResponseTypeDef",
    "ListStudioMembersResponseTypeDef",
    "ListStudiosResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NewLaunchProfileMemberTypeDef",
    "NewStudioMemberTypeDef",
    "PaginatorConfigTypeDef",
    "ScriptParameterKeyValueTypeDef",
    "SharedFileSystemConfigurationTypeDef",
    "StartStudioSSOConfigurationRepairResponseTypeDef",
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
    "UpdateLaunchProfileMemberResponseTypeDef",
    "UpdateLaunchProfileResponseTypeDef",
    "UpdateStreamingImageResponseTypeDef",
    "UpdateStudioComponentResponseTypeDef",
    "UpdateStudioResponseTypeDef",
)

AcceptEulasResponseTypeDef = TypedDict(
    "AcceptEulasResponseTypeDef",
    {
        "eulaAcceptances": List["EulaAcceptanceTypeDef"],
    },
    total=False,
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

CreateLaunchProfileResponseTypeDef = TypedDict(
    "CreateLaunchProfileResponseTypeDef",
    {
        "launchProfile": "LaunchProfileTypeDef",
    },
    total=False,
)

CreateStreamingImageResponseTypeDef = TypedDict(
    "CreateStreamingImageResponseTypeDef",
    {
        "streamingImage": "StreamingImageTypeDef",
    },
    total=False,
)

CreateStreamingSessionResponseTypeDef = TypedDict(
    "CreateStreamingSessionResponseTypeDef",
    {
        "session": "StreamingSessionTypeDef",
    },
    total=False,
)

CreateStreamingSessionStreamResponseTypeDef = TypedDict(
    "CreateStreamingSessionStreamResponseTypeDef",
    {
        "stream": "StreamingSessionStreamTypeDef",
    },
    total=False,
)

CreateStudioComponentResponseTypeDef = TypedDict(
    "CreateStudioComponentResponseTypeDef",
    {
        "studioComponent": "StudioComponentTypeDef",
    },
    total=False,
)

CreateStudioResponseTypeDef = TypedDict(
    "CreateStudioResponseTypeDef",
    {
        "studio": "StudioTypeDef",
    },
    total=False,
)

DeleteLaunchProfileResponseTypeDef = TypedDict(
    "DeleteLaunchProfileResponseTypeDef",
    {
        "launchProfile": "LaunchProfileTypeDef",
    },
    total=False,
)

DeleteStreamingImageResponseTypeDef = TypedDict(
    "DeleteStreamingImageResponseTypeDef",
    {
        "streamingImage": "StreamingImageTypeDef",
    },
    total=False,
)

DeleteStreamingSessionResponseTypeDef = TypedDict(
    "DeleteStreamingSessionResponseTypeDef",
    {
        "session": "StreamingSessionTypeDef",
    },
    total=False,
)

DeleteStudioComponentResponseTypeDef = TypedDict(
    "DeleteStudioComponentResponseTypeDef",
    {
        "studioComponent": "StudioComponentTypeDef",
    },
    total=False,
)

DeleteStudioResponseTypeDef = TypedDict(
    "DeleteStudioResponseTypeDef",
    {
        "studio": "StudioTypeDef",
    },
    total=False,
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

GetEulaResponseTypeDef = TypedDict(
    "GetEulaResponseTypeDef",
    {
        "eula": "EulaTypeDef",
    },
    total=False,
)

GetLaunchProfileDetailsResponseTypeDef = TypedDict(
    "GetLaunchProfileDetailsResponseTypeDef",
    {
        "launchProfile": "LaunchProfileTypeDef",
        "streamingImages": List["StreamingImageTypeDef"],
        "studioComponentSummaries": List["StudioComponentSummaryTypeDef"],
    },
    total=False,
)

GetLaunchProfileInitializationResponseTypeDef = TypedDict(
    "GetLaunchProfileInitializationResponseTypeDef",
    {
        "launchProfileInitialization": "LaunchProfileInitializationTypeDef",
    },
    total=False,
)

GetLaunchProfileMemberResponseTypeDef = TypedDict(
    "GetLaunchProfileMemberResponseTypeDef",
    {
        "member": "LaunchProfileMembershipTypeDef",
    },
    total=False,
)

GetLaunchProfileResponseTypeDef = TypedDict(
    "GetLaunchProfileResponseTypeDef",
    {
        "launchProfile": "LaunchProfileTypeDef",
    },
    total=False,
)

GetStreamingImageResponseTypeDef = TypedDict(
    "GetStreamingImageResponseTypeDef",
    {
        "streamingImage": "StreamingImageTypeDef",
    },
    total=False,
)

GetStreamingSessionResponseTypeDef = TypedDict(
    "GetStreamingSessionResponseTypeDef",
    {
        "session": "StreamingSessionTypeDef",
    },
    total=False,
)

GetStreamingSessionStreamResponseTypeDef = TypedDict(
    "GetStreamingSessionStreamResponseTypeDef",
    {
        "stream": "StreamingSessionStreamTypeDef",
    },
    total=False,
)

GetStudioComponentResponseTypeDef = TypedDict(
    "GetStudioComponentResponseTypeDef",
    {
        "studioComponent": "StudioComponentTypeDef",
    },
    total=False,
)

GetStudioMemberResponseTypeDef = TypedDict(
    "GetStudioMemberResponseTypeDef",
    {
        "member": "StudioMembershipTypeDef",
    },
    total=False,
)

GetStudioResponseTypeDef = TypedDict(
    "GetStudioResponseTypeDef",
    {
        "studio": "StudioTypeDef",
    },
    total=False,
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

ListEulaAcceptancesResponseTypeDef = TypedDict(
    "ListEulaAcceptancesResponseTypeDef",
    {
        "eulaAcceptances": List["EulaAcceptanceTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListEulasResponseTypeDef = TypedDict(
    "ListEulasResponseTypeDef",
    {
        "eulas": List["EulaTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListLaunchProfileMembersResponseTypeDef = TypedDict(
    "ListLaunchProfileMembersResponseTypeDef",
    {
        "members": List["LaunchProfileMembershipTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListLaunchProfilesResponseTypeDef = TypedDict(
    "ListLaunchProfilesResponseTypeDef",
    {
        "launchProfiles": List["LaunchProfileTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListStreamingImagesResponseTypeDef = TypedDict(
    "ListStreamingImagesResponseTypeDef",
    {
        "nextToken": str,
        "streamingImages": List["StreamingImageTypeDef"],
    },
    total=False,
)

ListStreamingSessionsResponseTypeDef = TypedDict(
    "ListStreamingSessionsResponseTypeDef",
    {
        "nextToken": str,
        "sessions": List["StreamingSessionTypeDef"],
    },
    total=False,
)

ListStudioComponentsResponseTypeDef = TypedDict(
    "ListStudioComponentsResponseTypeDef",
    {
        "nextToken": str,
        "studioComponents": List["StudioComponentTypeDef"],
    },
    total=False,
)

ListStudioMembersResponseTypeDef = TypedDict(
    "ListStudioMembersResponseTypeDef",
    {
        "members": List["StudioMembershipTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListStudiosResponseTypeDef = TypedDict(
    "ListStudiosResponseTypeDef",
    {
        "nextToken": str,
        "studios": List["StudioTypeDef"],
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
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

StartStudioSSOConfigurationRepairResponseTypeDef = TypedDict(
    "StartStudioSSOConfigurationRepairResponseTypeDef",
    {
        "studio": "StudioTypeDef",
    },
    total=False,
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

UpdateLaunchProfileMemberResponseTypeDef = TypedDict(
    "UpdateLaunchProfileMemberResponseTypeDef",
    {
        "member": "LaunchProfileMembershipTypeDef",
    },
    total=False,
)

UpdateLaunchProfileResponseTypeDef = TypedDict(
    "UpdateLaunchProfileResponseTypeDef",
    {
        "launchProfile": "LaunchProfileTypeDef",
    },
    total=False,
)

UpdateStreamingImageResponseTypeDef = TypedDict(
    "UpdateStreamingImageResponseTypeDef",
    {
        "streamingImage": "StreamingImageTypeDef",
    },
    total=False,
)

UpdateStudioComponentResponseTypeDef = TypedDict(
    "UpdateStudioComponentResponseTypeDef",
    {
        "studioComponent": "StudioComponentTypeDef",
    },
    total=False,
)

UpdateStudioResponseTypeDef = TypedDict(
    "UpdateStudioResponseTypeDef",
    {
        "studio": "StudioTypeDef",
    },
    total=False,
)
