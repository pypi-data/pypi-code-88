"""
Type annotations for devicefarm service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/type_defs.html)

Usage::

    ```python
    from mypy_boto3_devicefarm.type_defs import AccountSettingsTypeDef

    data: AccountSettingsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ArtifactCategoryType,
    ArtifactTypeType,
    BillingMethodType,
    DeviceAttributeType,
    DeviceAvailabilityType,
    DeviceFilterAttributeType,
    DeviceFormFactorType,
    DevicePlatformType,
    DevicePoolTypeType,
    ExecutionResultCodeType,
    ExecutionResultType,
    ExecutionStatusType,
    InstanceStatusType,
    InteractionModeType,
    NetworkProfileTypeType,
    OfferingTransactionTypeType,
    RuleOperatorType,
    SampleTypeType,
    TestGridSessionArtifactCategoryType,
    TestGridSessionArtifactTypeType,
    TestGridSessionStatusType,
    TestTypeType,
    UploadCategoryType,
    UploadStatusType,
    UploadTypeType,
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
    "AccountSettingsTypeDef",
    "ArtifactTypeDef",
    "CPUTypeDef",
    "CountersTypeDef",
    "CreateDevicePoolRequestTypeDef",
    "CreateDevicePoolResultResponseTypeDef",
    "CreateInstanceProfileRequestTypeDef",
    "CreateInstanceProfileResultResponseTypeDef",
    "CreateNetworkProfileRequestTypeDef",
    "CreateNetworkProfileResultResponseTypeDef",
    "CreateProjectRequestTypeDef",
    "CreateProjectResultResponseTypeDef",
    "CreateRemoteAccessSessionConfigurationTypeDef",
    "CreateRemoteAccessSessionRequestTypeDef",
    "CreateRemoteAccessSessionResultResponseTypeDef",
    "CreateTestGridProjectRequestTypeDef",
    "CreateTestGridProjectResultResponseTypeDef",
    "CreateTestGridUrlRequestTypeDef",
    "CreateTestGridUrlResultResponseTypeDef",
    "CreateUploadRequestTypeDef",
    "CreateUploadResultResponseTypeDef",
    "CreateVPCEConfigurationRequestTypeDef",
    "CreateVPCEConfigurationResultResponseTypeDef",
    "CustomerArtifactPathsTypeDef",
    "DeleteDevicePoolRequestTypeDef",
    "DeleteInstanceProfileRequestTypeDef",
    "DeleteNetworkProfileRequestTypeDef",
    "DeleteProjectRequestTypeDef",
    "DeleteRemoteAccessSessionRequestTypeDef",
    "DeleteRunRequestTypeDef",
    "DeleteTestGridProjectRequestTypeDef",
    "DeleteUploadRequestTypeDef",
    "DeleteVPCEConfigurationRequestTypeDef",
    "DeviceFilterTypeDef",
    "DeviceInstanceTypeDef",
    "DeviceMinutesTypeDef",
    "DevicePoolCompatibilityResultTypeDef",
    "DevicePoolTypeDef",
    "DeviceSelectionConfigurationTypeDef",
    "DeviceSelectionResultTypeDef",
    "DeviceTypeDef",
    "ExecutionConfigurationTypeDef",
    "GetAccountSettingsResultResponseTypeDef",
    "GetDeviceInstanceRequestTypeDef",
    "GetDeviceInstanceResultResponseTypeDef",
    "GetDevicePoolCompatibilityRequestTypeDef",
    "GetDevicePoolCompatibilityResultResponseTypeDef",
    "GetDevicePoolRequestTypeDef",
    "GetDevicePoolResultResponseTypeDef",
    "GetDeviceRequestTypeDef",
    "GetDeviceResultResponseTypeDef",
    "GetInstanceProfileRequestTypeDef",
    "GetInstanceProfileResultResponseTypeDef",
    "GetJobRequestTypeDef",
    "GetJobResultResponseTypeDef",
    "GetNetworkProfileRequestTypeDef",
    "GetNetworkProfileResultResponseTypeDef",
    "GetOfferingStatusRequestTypeDef",
    "GetOfferingStatusResultResponseTypeDef",
    "GetProjectRequestTypeDef",
    "GetProjectResultResponseTypeDef",
    "GetRemoteAccessSessionRequestTypeDef",
    "GetRemoteAccessSessionResultResponseTypeDef",
    "GetRunRequestTypeDef",
    "GetRunResultResponseTypeDef",
    "GetSuiteRequestTypeDef",
    "GetSuiteResultResponseTypeDef",
    "GetTestGridProjectRequestTypeDef",
    "GetTestGridProjectResultResponseTypeDef",
    "GetTestGridSessionRequestTypeDef",
    "GetTestGridSessionResultResponseTypeDef",
    "GetTestRequestTypeDef",
    "GetTestResultResponseTypeDef",
    "GetUploadRequestTypeDef",
    "GetUploadResultResponseTypeDef",
    "GetVPCEConfigurationRequestTypeDef",
    "GetVPCEConfigurationResultResponseTypeDef",
    "IncompatibilityMessageTypeDef",
    "InstallToRemoteAccessSessionRequestTypeDef",
    "InstallToRemoteAccessSessionResultResponseTypeDef",
    "InstanceProfileTypeDef",
    "JobTypeDef",
    "ListArtifactsRequestTypeDef",
    "ListArtifactsResultResponseTypeDef",
    "ListDeviceInstancesRequestTypeDef",
    "ListDeviceInstancesResultResponseTypeDef",
    "ListDevicePoolsRequestTypeDef",
    "ListDevicePoolsResultResponseTypeDef",
    "ListDevicesRequestTypeDef",
    "ListDevicesResultResponseTypeDef",
    "ListInstanceProfilesRequestTypeDef",
    "ListInstanceProfilesResultResponseTypeDef",
    "ListJobsRequestTypeDef",
    "ListJobsResultResponseTypeDef",
    "ListNetworkProfilesRequestTypeDef",
    "ListNetworkProfilesResultResponseTypeDef",
    "ListOfferingPromotionsRequestTypeDef",
    "ListOfferingPromotionsResultResponseTypeDef",
    "ListOfferingTransactionsRequestTypeDef",
    "ListOfferingTransactionsResultResponseTypeDef",
    "ListOfferingsRequestTypeDef",
    "ListOfferingsResultResponseTypeDef",
    "ListProjectsRequestTypeDef",
    "ListProjectsResultResponseTypeDef",
    "ListRemoteAccessSessionsRequestTypeDef",
    "ListRemoteAccessSessionsResultResponseTypeDef",
    "ListRunsRequestTypeDef",
    "ListRunsResultResponseTypeDef",
    "ListSamplesRequestTypeDef",
    "ListSamplesResultResponseTypeDef",
    "ListSuitesRequestTypeDef",
    "ListSuitesResultResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ListTestGridProjectsRequestTypeDef",
    "ListTestGridProjectsResultResponseTypeDef",
    "ListTestGridSessionActionsRequestTypeDef",
    "ListTestGridSessionActionsResultResponseTypeDef",
    "ListTestGridSessionArtifactsRequestTypeDef",
    "ListTestGridSessionArtifactsResultResponseTypeDef",
    "ListTestGridSessionsRequestTypeDef",
    "ListTestGridSessionsResultResponseTypeDef",
    "ListTestsRequestTypeDef",
    "ListTestsResultResponseTypeDef",
    "ListUniqueProblemsRequestTypeDef",
    "ListUniqueProblemsResultResponseTypeDef",
    "ListUploadsRequestTypeDef",
    "ListUploadsResultResponseTypeDef",
    "ListVPCEConfigurationsRequestTypeDef",
    "ListVPCEConfigurationsResultResponseTypeDef",
    "LocationTypeDef",
    "MonetaryAmountTypeDef",
    "NetworkProfileTypeDef",
    "OfferingPromotionTypeDef",
    "OfferingStatusTypeDef",
    "OfferingTransactionTypeDef",
    "OfferingTypeDef",
    "PaginatorConfigTypeDef",
    "ProblemDetailTypeDef",
    "ProblemTypeDef",
    "ProjectTypeDef",
    "PurchaseOfferingRequestTypeDef",
    "PurchaseOfferingResultResponseTypeDef",
    "RadiosTypeDef",
    "RecurringChargeTypeDef",
    "RemoteAccessSessionTypeDef",
    "RenewOfferingRequestTypeDef",
    "RenewOfferingResultResponseTypeDef",
    "ResolutionTypeDef",
    "ResponseMetadataTypeDef",
    "RuleTypeDef",
    "RunTypeDef",
    "SampleTypeDef",
    "ScheduleRunConfigurationTypeDef",
    "ScheduleRunRequestTypeDef",
    "ScheduleRunResultResponseTypeDef",
    "ScheduleRunTestTypeDef",
    "StopJobRequestTypeDef",
    "StopJobResultResponseTypeDef",
    "StopRemoteAccessSessionRequestTypeDef",
    "StopRemoteAccessSessionResultResponseTypeDef",
    "StopRunRequestTypeDef",
    "StopRunResultResponseTypeDef",
    "SuiteTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TestGridProjectTypeDef",
    "TestGridSessionActionTypeDef",
    "TestGridSessionArtifactTypeDef",
    "TestGridSessionTypeDef",
    "TestGridVpcConfigTypeDef",
    "TestTypeDef",
    "TrialMinutesTypeDef",
    "UniqueProblemTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateDeviceInstanceRequestTypeDef",
    "UpdateDeviceInstanceResultResponseTypeDef",
    "UpdateDevicePoolRequestTypeDef",
    "UpdateDevicePoolResultResponseTypeDef",
    "UpdateInstanceProfileRequestTypeDef",
    "UpdateInstanceProfileResultResponseTypeDef",
    "UpdateNetworkProfileRequestTypeDef",
    "UpdateNetworkProfileResultResponseTypeDef",
    "UpdateProjectRequestTypeDef",
    "UpdateProjectResultResponseTypeDef",
    "UpdateTestGridProjectRequestTypeDef",
    "UpdateTestGridProjectResultResponseTypeDef",
    "UpdateUploadRequestTypeDef",
    "UpdateUploadResultResponseTypeDef",
    "UpdateVPCEConfigurationRequestTypeDef",
    "UpdateVPCEConfigurationResultResponseTypeDef",
    "UploadTypeDef",
    "VPCEConfigurationTypeDef",
)

AccountSettingsTypeDef = TypedDict(
    "AccountSettingsTypeDef",
    {
        "awsAccountNumber": str,
        "unmeteredDevices": Dict[DevicePlatformType, int],
        "unmeteredRemoteAccessDevices": Dict[DevicePlatformType, int],
        "maxJobTimeoutMinutes": int,
        "trialMinutes": "TrialMinutesTypeDef",
        "maxSlots": Dict[str, int],
        "defaultJobTimeoutMinutes": int,
        "skipAppResign": bool,
    },
    total=False,
)

ArtifactTypeDef = TypedDict(
    "ArtifactTypeDef",
    {
        "arn": str,
        "name": str,
        "type": ArtifactTypeType,
        "extension": str,
        "url": str,
    },
    total=False,
)

CPUTypeDef = TypedDict(
    "CPUTypeDef",
    {
        "frequency": str,
        "architecture": str,
        "clock": float,
    },
    total=False,
)

CountersTypeDef = TypedDict(
    "CountersTypeDef",
    {
        "total": int,
        "passed": int,
        "failed": int,
        "warned": int,
        "errored": int,
        "stopped": int,
        "skipped": int,
    },
    total=False,
)

_RequiredCreateDevicePoolRequestTypeDef = TypedDict(
    "_RequiredCreateDevicePoolRequestTypeDef",
    {
        "projectArn": str,
        "name": str,
        "rules": List["RuleTypeDef"],
    },
)
_OptionalCreateDevicePoolRequestTypeDef = TypedDict(
    "_OptionalCreateDevicePoolRequestTypeDef",
    {
        "description": str,
        "maxDevices": int,
    },
    total=False,
)


class CreateDevicePoolRequestTypeDef(
    _RequiredCreateDevicePoolRequestTypeDef, _OptionalCreateDevicePoolRequestTypeDef
):
    pass


CreateDevicePoolResultResponseTypeDef = TypedDict(
    "CreateDevicePoolResultResponseTypeDef",
    {
        "devicePool": "DevicePoolTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateInstanceProfileRequestTypeDef = TypedDict(
    "_RequiredCreateInstanceProfileRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateInstanceProfileRequestTypeDef = TypedDict(
    "_OptionalCreateInstanceProfileRequestTypeDef",
    {
        "description": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
    },
    total=False,
)


class CreateInstanceProfileRequestTypeDef(
    _RequiredCreateInstanceProfileRequestTypeDef, _OptionalCreateInstanceProfileRequestTypeDef
):
    pass


CreateInstanceProfileResultResponseTypeDef = TypedDict(
    "CreateInstanceProfileResultResponseTypeDef",
    {
        "instanceProfile": "InstanceProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateNetworkProfileRequestTypeDef = TypedDict(
    "_RequiredCreateNetworkProfileRequestTypeDef",
    {
        "projectArn": str,
        "name": str,
    },
)
_OptionalCreateNetworkProfileRequestTypeDef = TypedDict(
    "_OptionalCreateNetworkProfileRequestTypeDef",
    {
        "description": str,
        "type": NetworkProfileTypeType,
        "uplinkBandwidthBits": int,
        "downlinkBandwidthBits": int,
        "uplinkDelayMs": int,
        "downlinkDelayMs": int,
        "uplinkJitterMs": int,
        "downlinkJitterMs": int,
        "uplinkLossPercent": int,
        "downlinkLossPercent": int,
    },
    total=False,
)


class CreateNetworkProfileRequestTypeDef(
    _RequiredCreateNetworkProfileRequestTypeDef, _OptionalCreateNetworkProfileRequestTypeDef
):
    pass


CreateNetworkProfileResultResponseTypeDef = TypedDict(
    "CreateNetworkProfileResultResponseTypeDef",
    {
        "networkProfile": "NetworkProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProjectRequestTypeDef = TypedDict(
    "_RequiredCreateProjectRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateProjectRequestTypeDef = TypedDict(
    "_OptionalCreateProjectRequestTypeDef",
    {
        "defaultJobTimeoutMinutes": int,
    },
    total=False,
)


class CreateProjectRequestTypeDef(
    _RequiredCreateProjectRequestTypeDef, _OptionalCreateProjectRequestTypeDef
):
    pass


CreateProjectResultResponseTypeDef = TypedDict(
    "CreateProjectResultResponseTypeDef",
    {
        "project": "ProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRemoteAccessSessionConfigurationTypeDef = TypedDict(
    "CreateRemoteAccessSessionConfigurationTypeDef",
    {
        "billingMethod": BillingMethodType,
        "vpceConfigurationArns": List[str],
    },
    total=False,
)

_RequiredCreateRemoteAccessSessionRequestTypeDef = TypedDict(
    "_RequiredCreateRemoteAccessSessionRequestTypeDef",
    {
        "projectArn": str,
        "deviceArn": str,
    },
)
_OptionalCreateRemoteAccessSessionRequestTypeDef = TypedDict(
    "_OptionalCreateRemoteAccessSessionRequestTypeDef",
    {
        "instanceArn": str,
        "sshPublicKey": str,
        "remoteDebugEnabled": bool,
        "remoteRecordEnabled": bool,
        "remoteRecordAppArn": str,
        "name": str,
        "clientId": str,
        "configuration": "CreateRemoteAccessSessionConfigurationTypeDef",
        "interactionMode": InteractionModeType,
        "skipAppResign": bool,
    },
    total=False,
)


class CreateRemoteAccessSessionRequestTypeDef(
    _RequiredCreateRemoteAccessSessionRequestTypeDef,
    _OptionalCreateRemoteAccessSessionRequestTypeDef,
):
    pass


CreateRemoteAccessSessionResultResponseTypeDef = TypedDict(
    "CreateRemoteAccessSessionResultResponseTypeDef",
    {
        "remoteAccessSession": "RemoteAccessSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTestGridProjectRequestTypeDef = TypedDict(
    "_RequiredCreateTestGridProjectRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateTestGridProjectRequestTypeDef = TypedDict(
    "_OptionalCreateTestGridProjectRequestTypeDef",
    {
        "description": str,
        "vpcConfig": "TestGridVpcConfigTypeDef",
    },
    total=False,
)


class CreateTestGridProjectRequestTypeDef(
    _RequiredCreateTestGridProjectRequestTypeDef, _OptionalCreateTestGridProjectRequestTypeDef
):
    pass


CreateTestGridProjectResultResponseTypeDef = TypedDict(
    "CreateTestGridProjectResultResponseTypeDef",
    {
        "testGridProject": "TestGridProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTestGridUrlRequestTypeDef = TypedDict(
    "CreateTestGridUrlRequestTypeDef",
    {
        "projectArn": str,
        "expiresInSeconds": int,
    },
)

CreateTestGridUrlResultResponseTypeDef = TypedDict(
    "CreateTestGridUrlResultResponseTypeDef",
    {
        "url": str,
        "expires": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUploadRequestTypeDef = TypedDict(
    "_RequiredCreateUploadRequestTypeDef",
    {
        "projectArn": str,
        "name": str,
        "type": UploadTypeType,
    },
)
_OptionalCreateUploadRequestTypeDef = TypedDict(
    "_OptionalCreateUploadRequestTypeDef",
    {
        "contentType": str,
    },
    total=False,
)


class CreateUploadRequestTypeDef(
    _RequiredCreateUploadRequestTypeDef, _OptionalCreateUploadRequestTypeDef
):
    pass


CreateUploadResultResponseTypeDef = TypedDict(
    "CreateUploadResultResponseTypeDef",
    {
        "upload": "UploadTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVPCEConfigurationRequestTypeDef = TypedDict(
    "_RequiredCreateVPCEConfigurationRequestTypeDef",
    {
        "vpceConfigurationName": str,
        "vpceServiceName": str,
        "serviceDnsName": str,
    },
)
_OptionalCreateVPCEConfigurationRequestTypeDef = TypedDict(
    "_OptionalCreateVPCEConfigurationRequestTypeDef",
    {
        "vpceConfigurationDescription": str,
    },
    total=False,
)


class CreateVPCEConfigurationRequestTypeDef(
    _RequiredCreateVPCEConfigurationRequestTypeDef, _OptionalCreateVPCEConfigurationRequestTypeDef
):
    pass


CreateVPCEConfigurationResultResponseTypeDef = TypedDict(
    "CreateVPCEConfigurationResultResponseTypeDef",
    {
        "vpceConfiguration": "VPCEConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomerArtifactPathsTypeDef = TypedDict(
    "CustomerArtifactPathsTypeDef",
    {
        "iosPaths": List[str],
        "androidPaths": List[str],
        "deviceHostPaths": List[str],
    },
    total=False,
)

DeleteDevicePoolRequestTypeDef = TypedDict(
    "DeleteDevicePoolRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteInstanceProfileRequestTypeDef = TypedDict(
    "DeleteInstanceProfileRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteNetworkProfileRequestTypeDef = TypedDict(
    "DeleteNetworkProfileRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteProjectRequestTypeDef = TypedDict(
    "DeleteProjectRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteRemoteAccessSessionRequestTypeDef = TypedDict(
    "DeleteRemoteAccessSessionRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteRunRequestTypeDef = TypedDict(
    "DeleteRunRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteTestGridProjectRequestTypeDef = TypedDict(
    "DeleteTestGridProjectRequestTypeDef",
    {
        "projectArn": str,
    },
)

DeleteUploadRequestTypeDef = TypedDict(
    "DeleteUploadRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteVPCEConfigurationRequestTypeDef = TypedDict(
    "DeleteVPCEConfigurationRequestTypeDef",
    {
        "arn": str,
    },
)

DeviceFilterTypeDef = TypedDict(
    "DeviceFilterTypeDef",
    {
        "attribute": DeviceFilterAttributeType,
        "operator": RuleOperatorType,
        "values": List[str],
    },
)

DeviceInstanceTypeDef = TypedDict(
    "DeviceInstanceTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": InstanceStatusType,
        "udid": str,
        "instanceProfile": "InstanceProfileTypeDef",
    },
    total=False,
)

DeviceMinutesTypeDef = TypedDict(
    "DeviceMinutesTypeDef",
    {
        "total": float,
        "metered": float,
        "unmetered": float,
    },
    total=False,
)

DevicePoolCompatibilityResultTypeDef = TypedDict(
    "DevicePoolCompatibilityResultTypeDef",
    {
        "device": "DeviceTypeDef",
        "compatible": bool,
        "incompatibilityMessages": List["IncompatibilityMessageTypeDef"],
    },
    total=False,
)

DevicePoolTypeDef = TypedDict(
    "DevicePoolTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": DevicePoolTypeType,
        "rules": List["RuleTypeDef"],
        "maxDevices": int,
    },
    total=False,
)

DeviceSelectionConfigurationTypeDef = TypedDict(
    "DeviceSelectionConfigurationTypeDef",
    {
        "filters": List["DeviceFilterTypeDef"],
        "maxDevices": int,
    },
)

DeviceSelectionResultTypeDef = TypedDict(
    "DeviceSelectionResultTypeDef",
    {
        "filters": List["DeviceFilterTypeDef"],
        "matchedDevicesCount": int,
        "maxDevices": int,
    },
    total=False,
)

DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "arn": str,
        "name": str,
        "manufacturer": str,
        "model": str,
        "modelId": str,
        "formFactor": DeviceFormFactorType,
        "platform": DevicePlatformType,
        "os": str,
        "cpu": "CPUTypeDef",
        "resolution": "ResolutionTypeDef",
        "heapSize": int,
        "memory": int,
        "image": str,
        "carrier": str,
        "radio": str,
        "remoteAccessEnabled": bool,
        "remoteDebugEnabled": bool,
        "fleetType": str,
        "fleetName": str,
        "instances": List["DeviceInstanceTypeDef"],
        "availability": DeviceAvailabilityType,
    },
    total=False,
)

ExecutionConfigurationTypeDef = TypedDict(
    "ExecutionConfigurationTypeDef",
    {
        "jobTimeoutMinutes": int,
        "accountsCleanup": bool,
        "appPackagesCleanup": bool,
        "videoCapture": bool,
        "skipAppResign": bool,
    },
    total=False,
)

GetAccountSettingsResultResponseTypeDef = TypedDict(
    "GetAccountSettingsResultResponseTypeDef",
    {
        "accountSettings": "AccountSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeviceInstanceRequestTypeDef = TypedDict(
    "GetDeviceInstanceRequestTypeDef",
    {
        "arn": str,
    },
)

GetDeviceInstanceResultResponseTypeDef = TypedDict(
    "GetDeviceInstanceResultResponseTypeDef",
    {
        "deviceInstance": "DeviceInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDevicePoolCompatibilityRequestTypeDef = TypedDict(
    "_RequiredGetDevicePoolCompatibilityRequestTypeDef",
    {
        "devicePoolArn": str,
    },
)
_OptionalGetDevicePoolCompatibilityRequestTypeDef = TypedDict(
    "_OptionalGetDevicePoolCompatibilityRequestTypeDef",
    {
        "appArn": str,
        "testType": TestTypeType,
        "test": "ScheduleRunTestTypeDef",
        "configuration": "ScheduleRunConfigurationTypeDef",
    },
    total=False,
)


class GetDevicePoolCompatibilityRequestTypeDef(
    _RequiredGetDevicePoolCompatibilityRequestTypeDef,
    _OptionalGetDevicePoolCompatibilityRequestTypeDef,
):
    pass


GetDevicePoolCompatibilityResultResponseTypeDef = TypedDict(
    "GetDevicePoolCompatibilityResultResponseTypeDef",
    {
        "compatibleDevices": List["DevicePoolCompatibilityResultTypeDef"],
        "incompatibleDevices": List["DevicePoolCompatibilityResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDevicePoolRequestTypeDef = TypedDict(
    "GetDevicePoolRequestTypeDef",
    {
        "arn": str,
    },
)

GetDevicePoolResultResponseTypeDef = TypedDict(
    "GetDevicePoolResultResponseTypeDef",
    {
        "devicePool": "DevicePoolTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeviceRequestTypeDef = TypedDict(
    "GetDeviceRequestTypeDef",
    {
        "arn": str,
    },
)

GetDeviceResultResponseTypeDef = TypedDict(
    "GetDeviceResultResponseTypeDef",
    {
        "device": "DeviceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstanceProfileRequestTypeDef = TypedDict(
    "GetInstanceProfileRequestTypeDef",
    {
        "arn": str,
    },
)

GetInstanceProfileResultResponseTypeDef = TypedDict(
    "GetInstanceProfileResultResponseTypeDef",
    {
        "instanceProfile": "InstanceProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobRequestTypeDef = TypedDict(
    "GetJobRequestTypeDef",
    {
        "arn": str,
    },
)

GetJobResultResponseTypeDef = TypedDict(
    "GetJobResultResponseTypeDef",
    {
        "job": "JobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNetworkProfileRequestTypeDef = TypedDict(
    "GetNetworkProfileRequestTypeDef",
    {
        "arn": str,
    },
)

GetNetworkProfileResultResponseTypeDef = TypedDict(
    "GetNetworkProfileResultResponseTypeDef",
    {
        "networkProfile": "NetworkProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOfferingStatusRequestTypeDef = TypedDict(
    "GetOfferingStatusRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

GetOfferingStatusResultResponseTypeDef = TypedDict(
    "GetOfferingStatusResultResponseTypeDef",
    {
        "current": Dict[str, "OfferingStatusTypeDef"],
        "nextPeriod": Dict[str, "OfferingStatusTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProjectRequestTypeDef = TypedDict(
    "GetProjectRequestTypeDef",
    {
        "arn": str,
    },
)

GetProjectResultResponseTypeDef = TypedDict(
    "GetProjectResultResponseTypeDef",
    {
        "project": "ProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRemoteAccessSessionRequestTypeDef = TypedDict(
    "GetRemoteAccessSessionRequestTypeDef",
    {
        "arn": str,
    },
)

GetRemoteAccessSessionResultResponseTypeDef = TypedDict(
    "GetRemoteAccessSessionResultResponseTypeDef",
    {
        "remoteAccessSession": "RemoteAccessSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRunRequestTypeDef = TypedDict(
    "GetRunRequestTypeDef",
    {
        "arn": str,
    },
)

GetRunResultResponseTypeDef = TypedDict(
    "GetRunResultResponseTypeDef",
    {
        "run": "RunTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSuiteRequestTypeDef = TypedDict(
    "GetSuiteRequestTypeDef",
    {
        "arn": str,
    },
)

GetSuiteResultResponseTypeDef = TypedDict(
    "GetSuiteResultResponseTypeDef",
    {
        "suite": "SuiteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTestGridProjectRequestTypeDef = TypedDict(
    "GetTestGridProjectRequestTypeDef",
    {
        "projectArn": str,
    },
)

GetTestGridProjectResultResponseTypeDef = TypedDict(
    "GetTestGridProjectResultResponseTypeDef",
    {
        "testGridProject": "TestGridProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTestGridSessionRequestTypeDef = TypedDict(
    "GetTestGridSessionRequestTypeDef",
    {
        "projectArn": str,
        "sessionId": str,
        "sessionArn": str,
    },
    total=False,
)

GetTestGridSessionResultResponseTypeDef = TypedDict(
    "GetTestGridSessionResultResponseTypeDef",
    {
        "testGridSession": "TestGridSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTestRequestTypeDef = TypedDict(
    "GetTestRequestTypeDef",
    {
        "arn": str,
    },
)

GetTestResultResponseTypeDef = TypedDict(
    "GetTestResultResponseTypeDef",
    {
        "test": "TestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUploadRequestTypeDef = TypedDict(
    "GetUploadRequestTypeDef",
    {
        "arn": str,
    },
)

GetUploadResultResponseTypeDef = TypedDict(
    "GetUploadResultResponseTypeDef",
    {
        "upload": "UploadTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVPCEConfigurationRequestTypeDef = TypedDict(
    "GetVPCEConfigurationRequestTypeDef",
    {
        "arn": str,
    },
)

GetVPCEConfigurationResultResponseTypeDef = TypedDict(
    "GetVPCEConfigurationResultResponseTypeDef",
    {
        "vpceConfiguration": "VPCEConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IncompatibilityMessageTypeDef = TypedDict(
    "IncompatibilityMessageTypeDef",
    {
        "message": str,
        "type": DeviceAttributeType,
    },
    total=False,
)

InstallToRemoteAccessSessionRequestTypeDef = TypedDict(
    "InstallToRemoteAccessSessionRequestTypeDef",
    {
        "remoteAccessSessionArn": str,
        "appArn": str,
    },
)

InstallToRemoteAccessSessionResultResponseTypeDef = TypedDict(
    "InstallToRemoteAccessSessionResultResponseTypeDef",
    {
        "appUpload": "UploadTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceProfileTypeDef = TypedDict(
    "InstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)

JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "arn": str,
        "name": str,
        "type": TestTypeType,
        "created": datetime,
        "status": ExecutionStatusType,
        "result": ExecutionResultType,
        "started": datetime,
        "stopped": datetime,
        "counters": "CountersTypeDef",
        "message": str,
        "device": "DeviceTypeDef",
        "instanceArn": str,
        "deviceMinutes": "DeviceMinutesTypeDef",
        "videoEndpoint": str,
        "videoCapture": bool,
    },
    total=False,
)

_RequiredListArtifactsRequestTypeDef = TypedDict(
    "_RequiredListArtifactsRequestTypeDef",
    {
        "arn": str,
        "type": ArtifactCategoryType,
    },
)
_OptionalListArtifactsRequestTypeDef = TypedDict(
    "_OptionalListArtifactsRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)


class ListArtifactsRequestTypeDef(
    _RequiredListArtifactsRequestTypeDef, _OptionalListArtifactsRequestTypeDef
):
    pass


ListArtifactsResultResponseTypeDef = TypedDict(
    "ListArtifactsResultResponseTypeDef",
    {
        "artifacts": List["ArtifactTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeviceInstancesRequestTypeDef = TypedDict(
    "ListDeviceInstancesRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListDeviceInstancesResultResponseTypeDef = TypedDict(
    "ListDeviceInstancesResultResponseTypeDef",
    {
        "deviceInstances": List["DeviceInstanceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDevicePoolsRequestTypeDef = TypedDict(
    "_RequiredListDevicePoolsRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalListDevicePoolsRequestTypeDef = TypedDict(
    "_OptionalListDevicePoolsRequestTypeDef",
    {
        "type": DevicePoolTypeType,
        "nextToken": str,
    },
    total=False,
)


class ListDevicePoolsRequestTypeDef(
    _RequiredListDevicePoolsRequestTypeDef, _OptionalListDevicePoolsRequestTypeDef
):
    pass


ListDevicePoolsResultResponseTypeDef = TypedDict(
    "ListDevicePoolsResultResponseTypeDef",
    {
        "devicePools": List["DevicePoolTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDevicesRequestTypeDef = TypedDict(
    "ListDevicesRequestTypeDef",
    {
        "arn": str,
        "nextToken": str,
        "filters": List["DeviceFilterTypeDef"],
    },
    total=False,
)

ListDevicesResultResponseTypeDef = TypedDict(
    "ListDevicesResultResponseTypeDef",
    {
        "devices": List["DeviceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInstanceProfilesRequestTypeDef = TypedDict(
    "ListInstanceProfilesRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListInstanceProfilesResultResponseTypeDef = TypedDict(
    "ListInstanceProfilesResultResponseTypeDef",
    {
        "instanceProfiles": List["InstanceProfileTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListJobsRequestTypeDef = TypedDict(
    "_RequiredListJobsRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalListJobsRequestTypeDef = TypedDict(
    "_OptionalListJobsRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)


class ListJobsRequestTypeDef(_RequiredListJobsRequestTypeDef, _OptionalListJobsRequestTypeDef):
    pass


ListJobsResultResponseTypeDef = TypedDict(
    "ListJobsResultResponseTypeDef",
    {
        "jobs": List["JobTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListNetworkProfilesRequestTypeDef = TypedDict(
    "_RequiredListNetworkProfilesRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalListNetworkProfilesRequestTypeDef = TypedDict(
    "_OptionalListNetworkProfilesRequestTypeDef",
    {
        "type": NetworkProfileTypeType,
        "nextToken": str,
    },
    total=False,
)


class ListNetworkProfilesRequestTypeDef(
    _RequiredListNetworkProfilesRequestTypeDef, _OptionalListNetworkProfilesRequestTypeDef
):
    pass


ListNetworkProfilesResultResponseTypeDef = TypedDict(
    "ListNetworkProfilesResultResponseTypeDef",
    {
        "networkProfiles": List["NetworkProfileTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOfferingPromotionsRequestTypeDef = TypedDict(
    "ListOfferingPromotionsRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

ListOfferingPromotionsResultResponseTypeDef = TypedDict(
    "ListOfferingPromotionsResultResponseTypeDef",
    {
        "offeringPromotions": List["OfferingPromotionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOfferingTransactionsRequestTypeDef = TypedDict(
    "ListOfferingTransactionsRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

ListOfferingTransactionsResultResponseTypeDef = TypedDict(
    "ListOfferingTransactionsResultResponseTypeDef",
    {
        "offeringTransactions": List["OfferingTransactionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOfferingsRequestTypeDef = TypedDict(
    "ListOfferingsRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

ListOfferingsResultResponseTypeDef = TypedDict(
    "ListOfferingsResultResponseTypeDef",
    {
        "offerings": List["OfferingTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProjectsRequestTypeDef = TypedDict(
    "ListProjectsRequestTypeDef",
    {
        "arn": str,
        "nextToken": str,
    },
    total=False,
)

ListProjectsResultResponseTypeDef = TypedDict(
    "ListProjectsResultResponseTypeDef",
    {
        "projects": List["ProjectTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRemoteAccessSessionsRequestTypeDef = TypedDict(
    "_RequiredListRemoteAccessSessionsRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalListRemoteAccessSessionsRequestTypeDef = TypedDict(
    "_OptionalListRemoteAccessSessionsRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)


class ListRemoteAccessSessionsRequestTypeDef(
    _RequiredListRemoteAccessSessionsRequestTypeDef, _OptionalListRemoteAccessSessionsRequestTypeDef
):
    pass


ListRemoteAccessSessionsResultResponseTypeDef = TypedDict(
    "ListRemoteAccessSessionsResultResponseTypeDef",
    {
        "remoteAccessSessions": List["RemoteAccessSessionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRunsRequestTypeDef = TypedDict(
    "_RequiredListRunsRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalListRunsRequestTypeDef = TypedDict(
    "_OptionalListRunsRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)


class ListRunsRequestTypeDef(_RequiredListRunsRequestTypeDef, _OptionalListRunsRequestTypeDef):
    pass


ListRunsResultResponseTypeDef = TypedDict(
    "ListRunsResultResponseTypeDef",
    {
        "runs": List["RunTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSamplesRequestTypeDef = TypedDict(
    "_RequiredListSamplesRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalListSamplesRequestTypeDef = TypedDict(
    "_OptionalListSamplesRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)


class ListSamplesRequestTypeDef(
    _RequiredListSamplesRequestTypeDef, _OptionalListSamplesRequestTypeDef
):
    pass


ListSamplesResultResponseTypeDef = TypedDict(
    "ListSamplesResultResponseTypeDef",
    {
        "samples": List["SampleTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSuitesRequestTypeDef = TypedDict(
    "_RequiredListSuitesRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalListSuitesRequestTypeDef = TypedDict(
    "_OptionalListSuitesRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)


class ListSuitesRequestTypeDef(
    _RequiredListSuitesRequestTypeDef, _OptionalListSuitesRequestTypeDef
):
    pass


ListSuitesResultResponseTypeDef = TypedDict(
    "ListSuitesResultResponseTypeDef",
    {
        "suites": List["SuiteTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTestGridProjectsRequestTypeDef = TypedDict(
    "ListTestGridProjectsRequestTypeDef",
    {
        "maxResult": int,
        "nextToken": str,
    },
    total=False,
)

ListTestGridProjectsResultResponseTypeDef = TypedDict(
    "ListTestGridProjectsResultResponseTypeDef",
    {
        "testGridProjects": List["TestGridProjectTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTestGridSessionActionsRequestTypeDef = TypedDict(
    "_RequiredListTestGridSessionActionsRequestTypeDef",
    {
        "sessionArn": str,
    },
)
_OptionalListTestGridSessionActionsRequestTypeDef = TypedDict(
    "_OptionalListTestGridSessionActionsRequestTypeDef",
    {
        "maxResult": int,
        "nextToken": str,
    },
    total=False,
)


class ListTestGridSessionActionsRequestTypeDef(
    _RequiredListTestGridSessionActionsRequestTypeDef,
    _OptionalListTestGridSessionActionsRequestTypeDef,
):
    pass


ListTestGridSessionActionsResultResponseTypeDef = TypedDict(
    "ListTestGridSessionActionsResultResponseTypeDef",
    {
        "actions": List["TestGridSessionActionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTestGridSessionArtifactsRequestTypeDef = TypedDict(
    "_RequiredListTestGridSessionArtifactsRequestTypeDef",
    {
        "sessionArn": str,
    },
)
_OptionalListTestGridSessionArtifactsRequestTypeDef = TypedDict(
    "_OptionalListTestGridSessionArtifactsRequestTypeDef",
    {
        "type": TestGridSessionArtifactCategoryType,
        "maxResult": int,
        "nextToken": str,
    },
    total=False,
)


class ListTestGridSessionArtifactsRequestTypeDef(
    _RequiredListTestGridSessionArtifactsRequestTypeDef,
    _OptionalListTestGridSessionArtifactsRequestTypeDef,
):
    pass


ListTestGridSessionArtifactsResultResponseTypeDef = TypedDict(
    "ListTestGridSessionArtifactsResultResponseTypeDef",
    {
        "artifacts": List["TestGridSessionArtifactTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTestGridSessionsRequestTypeDef = TypedDict(
    "_RequiredListTestGridSessionsRequestTypeDef",
    {
        "projectArn": str,
    },
)
_OptionalListTestGridSessionsRequestTypeDef = TypedDict(
    "_OptionalListTestGridSessionsRequestTypeDef",
    {
        "status": TestGridSessionStatusType,
        "creationTimeAfter": Union[datetime, str],
        "creationTimeBefore": Union[datetime, str],
        "endTimeAfter": Union[datetime, str],
        "endTimeBefore": Union[datetime, str],
        "maxResult": int,
        "nextToken": str,
    },
    total=False,
)


class ListTestGridSessionsRequestTypeDef(
    _RequiredListTestGridSessionsRequestTypeDef, _OptionalListTestGridSessionsRequestTypeDef
):
    pass


ListTestGridSessionsResultResponseTypeDef = TypedDict(
    "ListTestGridSessionsResultResponseTypeDef",
    {
        "testGridSessions": List["TestGridSessionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTestsRequestTypeDef = TypedDict(
    "_RequiredListTestsRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalListTestsRequestTypeDef = TypedDict(
    "_OptionalListTestsRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)


class ListTestsRequestTypeDef(_RequiredListTestsRequestTypeDef, _OptionalListTestsRequestTypeDef):
    pass


ListTestsResultResponseTypeDef = TypedDict(
    "ListTestsResultResponseTypeDef",
    {
        "tests": List["TestTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUniqueProblemsRequestTypeDef = TypedDict(
    "_RequiredListUniqueProblemsRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalListUniqueProblemsRequestTypeDef = TypedDict(
    "_OptionalListUniqueProblemsRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)


class ListUniqueProblemsRequestTypeDef(
    _RequiredListUniqueProblemsRequestTypeDef, _OptionalListUniqueProblemsRequestTypeDef
):
    pass


ListUniqueProblemsResultResponseTypeDef = TypedDict(
    "ListUniqueProblemsResultResponseTypeDef",
    {
        "uniqueProblems": Dict[ExecutionResultType, List["UniqueProblemTypeDef"]],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUploadsRequestTypeDef = TypedDict(
    "_RequiredListUploadsRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalListUploadsRequestTypeDef = TypedDict(
    "_OptionalListUploadsRequestTypeDef",
    {
        "type": UploadTypeType,
        "nextToken": str,
    },
    total=False,
)


class ListUploadsRequestTypeDef(
    _RequiredListUploadsRequestTypeDef, _OptionalListUploadsRequestTypeDef
):
    pass


ListUploadsResultResponseTypeDef = TypedDict(
    "ListUploadsResultResponseTypeDef",
    {
        "uploads": List["UploadTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVPCEConfigurationsRequestTypeDef = TypedDict(
    "ListVPCEConfigurationsRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListVPCEConfigurationsResultResponseTypeDef = TypedDict(
    "ListVPCEConfigurationsResultResponseTypeDef",
    {
        "vpceConfigurations": List["VPCEConfigurationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LocationTypeDef = TypedDict(
    "LocationTypeDef",
    {
        "latitude": float,
        "longitude": float,
    },
)

MonetaryAmountTypeDef = TypedDict(
    "MonetaryAmountTypeDef",
    {
        "amount": float,
        "currencyCode": Literal["USD"],
    },
    total=False,
)

NetworkProfileTypeDef = TypedDict(
    "NetworkProfileTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": NetworkProfileTypeType,
        "uplinkBandwidthBits": int,
        "downlinkBandwidthBits": int,
        "uplinkDelayMs": int,
        "downlinkDelayMs": int,
        "uplinkJitterMs": int,
        "downlinkJitterMs": int,
        "uplinkLossPercent": int,
        "downlinkLossPercent": int,
    },
    total=False,
)

OfferingPromotionTypeDef = TypedDict(
    "OfferingPromotionTypeDef",
    {
        "id": str,
        "description": str,
    },
    total=False,
)

OfferingStatusTypeDef = TypedDict(
    "OfferingStatusTypeDef",
    {
        "type": OfferingTransactionTypeType,
        "offering": "OfferingTypeDef",
        "quantity": int,
        "effectiveOn": datetime,
    },
    total=False,
)

OfferingTransactionTypeDef = TypedDict(
    "OfferingTransactionTypeDef",
    {
        "offeringStatus": "OfferingStatusTypeDef",
        "transactionId": str,
        "offeringPromotionId": str,
        "createdOn": datetime,
        "cost": "MonetaryAmountTypeDef",
    },
    total=False,
)

OfferingTypeDef = TypedDict(
    "OfferingTypeDef",
    {
        "id": str,
        "description": str,
        "type": Literal["RECURRING"],
        "platform": DevicePlatformType,
        "recurringCharges": List["RecurringChargeTypeDef"],
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

ProblemDetailTypeDef = TypedDict(
    "ProblemDetailTypeDef",
    {
        "arn": str,
        "name": str,
    },
    total=False,
)

ProblemTypeDef = TypedDict(
    "ProblemTypeDef",
    {
        "run": "ProblemDetailTypeDef",
        "job": "ProblemDetailTypeDef",
        "suite": "ProblemDetailTypeDef",
        "test": "ProblemDetailTypeDef",
        "device": "DeviceTypeDef",
        "result": ExecutionResultType,
        "message": str,
    },
    total=False,
)

ProjectTypeDef = TypedDict(
    "ProjectTypeDef",
    {
        "arn": str,
        "name": str,
        "defaultJobTimeoutMinutes": int,
        "created": datetime,
    },
    total=False,
)

_RequiredPurchaseOfferingRequestTypeDef = TypedDict(
    "_RequiredPurchaseOfferingRequestTypeDef",
    {
        "offeringId": str,
        "quantity": int,
    },
)
_OptionalPurchaseOfferingRequestTypeDef = TypedDict(
    "_OptionalPurchaseOfferingRequestTypeDef",
    {
        "offeringPromotionId": str,
    },
    total=False,
)


class PurchaseOfferingRequestTypeDef(
    _RequiredPurchaseOfferingRequestTypeDef, _OptionalPurchaseOfferingRequestTypeDef
):
    pass


PurchaseOfferingResultResponseTypeDef = TypedDict(
    "PurchaseOfferingResultResponseTypeDef",
    {
        "offeringTransaction": "OfferingTransactionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RadiosTypeDef = TypedDict(
    "RadiosTypeDef",
    {
        "wifi": bool,
        "bluetooth": bool,
        "nfc": bool,
        "gps": bool,
    },
    total=False,
)

RecurringChargeTypeDef = TypedDict(
    "RecurringChargeTypeDef",
    {
        "cost": "MonetaryAmountTypeDef",
        "frequency": Literal["MONTHLY"],
    },
    total=False,
)

RemoteAccessSessionTypeDef = TypedDict(
    "RemoteAccessSessionTypeDef",
    {
        "arn": str,
        "name": str,
        "created": datetime,
        "status": ExecutionStatusType,
        "result": ExecutionResultType,
        "message": str,
        "started": datetime,
        "stopped": datetime,
        "device": "DeviceTypeDef",
        "instanceArn": str,
        "remoteDebugEnabled": bool,
        "remoteRecordEnabled": bool,
        "remoteRecordAppArn": str,
        "hostAddress": str,
        "clientId": str,
        "billingMethod": BillingMethodType,
        "deviceMinutes": "DeviceMinutesTypeDef",
        "endpoint": str,
        "deviceUdid": str,
        "interactionMode": InteractionModeType,
        "skipAppResign": bool,
    },
    total=False,
)

RenewOfferingRequestTypeDef = TypedDict(
    "RenewOfferingRequestTypeDef",
    {
        "offeringId": str,
        "quantity": int,
    },
)

RenewOfferingResultResponseTypeDef = TypedDict(
    "RenewOfferingResultResponseTypeDef",
    {
        "offeringTransaction": "OfferingTransactionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResolutionTypeDef = TypedDict(
    "ResolutionTypeDef",
    {
        "width": int,
        "height": int,
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

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "attribute": DeviceAttributeType,
        "operator": RuleOperatorType,
        "value": str,
    },
    total=False,
)

RunTypeDef = TypedDict(
    "RunTypeDef",
    {
        "arn": str,
        "name": str,
        "type": TestTypeType,
        "platform": DevicePlatformType,
        "created": datetime,
        "status": ExecutionStatusType,
        "result": ExecutionResultType,
        "started": datetime,
        "stopped": datetime,
        "counters": "CountersTypeDef",
        "message": str,
        "totalJobs": int,
        "completedJobs": int,
        "billingMethod": BillingMethodType,
        "deviceMinutes": "DeviceMinutesTypeDef",
        "networkProfile": "NetworkProfileTypeDef",
        "parsingResultUrl": str,
        "resultCode": ExecutionResultCodeType,
        "seed": int,
        "appUpload": str,
        "eventCount": int,
        "jobTimeoutMinutes": int,
        "devicePoolArn": str,
        "locale": str,
        "radios": "RadiosTypeDef",
        "location": "LocationTypeDef",
        "customerArtifactPaths": "CustomerArtifactPathsTypeDef",
        "webUrl": str,
        "skipAppResign": bool,
        "testSpecArn": str,
        "deviceSelectionResult": "DeviceSelectionResultTypeDef",
    },
    total=False,
)

SampleTypeDef = TypedDict(
    "SampleTypeDef",
    {
        "arn": str,
        "type": SampleTypeType,
        "url": str,
    },
    total=False,
)

ScheduleRunConfigurationTypeDef = TypedDict(
    "ScheduleRunConfigurationTypeDef",
    {
        "extraDataPackageArn": str,
        "networkProfileArn": str,
        "locale": str,
        "location": "LocationTypeDef",
        "vpceConfigurationArns": List[str],
        "customerArtifactPaths": "CustomerArtifactPathsTypeDef",
        "radios": "RadiosTypeDef",
        "auxiliaryApps": List[str],
        "billingMethod": BillingMethodType,
    },
    total=False,
)

_RequiredScheduleRunRequestTypeDef = TypedDict(
    "_RequiredScheduleRunRequestTypeDef",
    {
        "projectArn": str,
        "test": "ScheduleRunTestTypeDef",
    },
)
_OptionalScheduleRunRequestTypeDef = TypedDict(
    "_OptionalScheduleRunRequestTypeDef",
    {
        "appArn": str,
        "devicePoolArn": str,
        "deviceSelectionConfiguration": "DeviceSelectionConfigurationTypeDef",
        "name": str,
        "configuration": "ScheduleRunConfigurationTypeDef",
        "executionConfiguration": "ExecutionConfigurationTypeDef",
    },
    total=False,
)


class ScheduleRunRequestTypeDef(
    _RequiredScheduleRunRequestTypeDef, _OptionalScheduleRunRequestTypeDef
):
    pass


ScheduleRunResultResponseTypeDef = TypedDict(
    "ScheduleRunResultResponseTypeDef",
    {
        "run": "RunTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredScheduleRunTestTypeDef = TypedDict(
    "_RequiredScheduleRunTestTypeDef",
    {
        "type": TestTypeType,
    },
)
_OptionalScheduleRunTestTypeDef = TypedDict(
    "_OptionalScheduleRunTestTypeDef",
    {
        "testPackageArn": str,
        "testSpecArn": str,
        "filter": str,
        "parameters": Dict[str, str],
    },
    total=False,
)


class ScheduleRunTestTypeDef(_RequiredScheduleRunTestTypeDef, _OptionalScheduleRunTestTypeDef):
    pass


StopJobRequestTypeDef = TypedDict(
    "StopJobRequestTypeDef",
    {
        "arn": str,
    },
)

StopJobResultResponseTypeDef = TypedDict(
    "StopJobResultResponseTypeDef",
    {
        "job": "JobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopRemoteAccessSessionRequestTypeDef = TypedDict(
    "StopRemoteAccessSessionRequestTypeDef",
    {
        "arn": str,
    },
)

StopRemoteAccessSessionResultResponseTypeDef = TypedDict(
    "StopRemoteAccessSessionResultResponseTypeDef",
    {
        "remoteAccessSession": "RemoteAccessSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopRunRequestTypeDef = TypedDict(
    "StopRunRequestTypeDef",
    {
        "arn": str,
    },
)

StopRunResultResponseTypeDef = TypedDict(
    "StopRunResultResponseTypeDef",
    {
        "run": "RunTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SuiteTypeDef = TypedDict(
    "SuiteTypeDef",
    {
        "arn": str,
        "name": str,
        "type": TestTypeType,
        "created": datetime,
        "status": ExecutionStatusType,
        "result": ExecutionResultType,
        "started": datetime,
        "stopped": datetime,
        "counters": "CountersTypeDef",
        "message": str,
        "deviceMinutes": "DeviceMinutesTypeDef",
    },
    total=False,
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TestGridProjectTypeDef = TypedDict(
    "TestGridProjectTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "vpcConfig": "TestGridVpcConfigTypeDef",
        "created": datetime,
    },
    total=False,
)

TestGridSessionActionTypeDef = TypedDict(
    "TestGridSessionActionTypeDef",
    {
        "action": str,
        "started": datetime,
        "duration": int,
        "statusCode": str,
        "requestMethod": str,
    },
    total=False,
)

TestGridSessionArtifactTypeDef = TypedDict(
    "TestGridSessionArtifactTypeDef",
    {
        "filename": str,
        "type": TestGridSessionArtifactTypeType,
        "url": str,
    },
    total=False,
)

TestGridSessionTypeDef = TypedDict(
    "TestGridSessionTypeDef",
    {
        "arn": str,
        "status": TestGridSessionStatusType,
        "created": datetime,
        "ended": datetime,
        "billingMinutes": float,
        "seleniumProperties": str,
    },
    total=False,
)

TestGridVpcConfigTypeDef = TypedDict(
    "TestGridVpcConfigTypeDef",
    {
        "securityGroupIds": List[str],
        "subnetIds": List[str],
        "vpcId": str,
    },
)

TestTypeDef = TypedDict(
    "TestTypeDef",
    {
        "arn": str,
        "name": str,
        "type": TestTypeType,
        "created": datetime,
        "status": ExecutionStatusType,
        "result": ExecutionResultType,
        "started": datetime,
        "stopped": datetime,
        "counters": "CountersTypeDef",
        "message": str,
        "deviceMinutes": "DeviceMinutesTypeDef",
    },
    total=False,
)

TrialMinutesTypeDef = TypedDict(
    "TrialMinutesTypeDef",
    {
        "total": float,
        "remaining": float,
    },
    total=False,
)

UniqueProblemTypeDef = TypedDict(
    "UniqueProblemTypeDef",
    {
        "message": str,
        "problems": List["ProblemTypeDef"],
    },
    total=False,
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateDeviceInstanceRequestTypeDef = TypedDict(
    "_RequiredUpdateDeviceInstanceRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalUpdateDeviceInstanceRequestTypeDef = TypedDict(
    "_OptionalUpdateDeviceInstanceRequestTypeDef",
    {
        "profileArn": str,
        "labels": List[str],
    },
    total=False,
)


class UpdateDeviceInstanceRequestTypeDef(
    _RequiredUpdateDeviceInstanceRequestTypeDef, _OptionalUpdateDeviceInstanceRequestTypeDef
):
    pass


UpdateDeviceInstanceResultResponseTypeDef = TypedDict(
    "UpdateDeviceInstanceResultResponseTypeDef",
    {
        "deviceInstance": "DeviceInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDevicePoolRequestTypeDef = TypedDict(
    "_RequiredUpdateDevicePoolRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalUpdateDevicePoolRequestTypeDef = TypedDict(
    "_OptionalUpdateDevicePoolRequestTypeDef",
    {
        "name": str,
        "description": str,
        "rules": List["RuleTypeDef"],
        "maxDevices": int,
        "clearMaxDevices": bool,
    },
    total=False,
)


class UpdateDevicePoolRequestTypeDef(
    _RequiredUpdateDevicePoolRequestTypeDef, _OptionalUpdateDevicePoolRequestTypeDef
):
    pass


UpdateDevicePoolResultResponseTypeDef = TypedDict(
    "UpdateDevicePoolResultResponseTypeDef",
    {
        "devicePool": "DevicePoolTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateInstanceProfileRequestTypeDef = TypedDict(
    "_RequiredUpdateInstanceProfileRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalUpdateInstanceProfileRequestTypeDef = TypedDict(
    "_OptionalUpdateInstanceProfileRequestTypeDef",
    {
        "name": str,
        "description": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
    },
    total=False,
)


class UpdateInstanceProfileRequestTypeDef(
    _RequiredUpdateInstanceProfileRequestTypeDef, _OptionalUpdateInstanceProfileRequestTypeDef
):
    pass


UpdateInstanceProfileResultResponseTypeDef = TypedDict(
    "UpdateInstanceProfileResultResponseTypeDef",
    {
        "instanceProfile": "InstanceProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateNetworkProfileRequestTypeDef = TypedDict(
    "_RequiredUpdateNetworkProfileRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalUpdateNetworkProfileRequestTypeDef = TypedDict(
    "_OptionalUpdateNetworkProfileRequestTypeDef",
    {
        "name": str,
        "description": str,
        "type": NetworkProfileTypeType,
        "uplinkBandwidthBits": int,
        "downlinkBandwidthBits": int,
        "uplinkDelayMs": int,
        "downlinkDelayMs": int,
        "uplinkJitterMs": int,
        "downlinkJitterMs": int,
        "uplinkLossPercent": int,
        "downlinkLossPercent": int,
    },
    total=False,
)


class UpdateNetworkProfileRequestTypeDef(
    _RequiredUpdateNetworkProfileRequestTypeDef, _OptionalUpdateNetworkProfileRequestTypeDef
):
    pass


UpdateNetworkProfileResultResponseTypeDef = TypedDict(
    "UpdateNetworkProfileResultResponseTypeDef",
    {
        "networkProfile": "NetworkProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateProjectRequestTypeDef = TypedDict(
    "_RequiredUpdateProjectRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalUpdateProjectRequestTypeDef = TypedDict(
    "_OptionalUpdateProjectRequestTypeDef",
    {
        "name": str,
        "defaultJobTimeoutMinutes": int,
    },
    total=False,
)


class UpdateProjectRequestTypeDef(
    _RequiredUpdateProjectRequestTypeDef, _OptionalUpdateProjectRequestTypeDef
):
    pass


UpdateProjectResultResponseTypeDef = TypedDict(
    "UpdateProjectResultResponseTypeDef",
    {
        "project": "ProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTestGridProjectRequestTypeDef = TypedDict(
    "_RequiredUpdateTestGridProjectRequestTypeDef",
    {
        "projectArn": str,
    },
)
_OptionalUpdateTestGridProjectRequestTypeDef = TypedDict(
    "_OptionalUpdateTestGridProjectRequestTypeDef",
    {
        "name": str,
        "description": str,
        "vpcConfig": "TestGridVpcConfigTypeDef",
    },
    total=False,
)


class UpdateTestGridProjectRequestTypeDef(
    _RequiredUpdateTestGridProjectRequestTypeDef, _OptionalUpdateTestGridProjectRequestTypeDef
):
    pass


UpdateTestGridProjectResultResponseTypeDef = TypedDict(
    "UpdateTestGridProjectResultResponseTypeDef",
    {
        "testGridProject": "TestGridProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateUploadRequestTypeDef = TypedDict(
    "_RequiredUpdateUploadRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalUpdateUploadRequestTypeDef = TypedDict(
    "_OptionalUpdateUploadRequestTypeDef",
    {
        "name": str,
        "contentType": str,
        "editContent": bool,
    },
    total=False,
)


class UpdateUploadRequestTypeDef(
    _RequiredUpdateUploadRequestTypeDef, _OptionalUpdateUploadRequestTypeDef
):
    pass


UpdateUploadResultResponseTypeDef = TypedDict(
    "UpdateUploadResultResponseTypeDef",
    {
        "upload": "UploadTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateVPCEConfigurationRequestTypeDef = TypedDict(
    "_RequiredUpdateVPCEConfigurationRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalUpdateVPCEConfigurationRequestTypeDef = TypedDict(
    "_OptionalUpdateVPCEConfigurationRequestTypeDef",
    {
        "vpceConfigurationName": str,
        "vpceServiceName": str,
        "serviceDnsName": str,
        "vpceConfigurationDescription": str,
    },
    total=False,
)


class UpdateVPCEConfigurationRequestTypeDef(
    _RequiredUpdateVPCEConfigurationRequestTypeDef, _OptionalUpdateVPCEConfigurationRequestTypeDef
):
    pass


UpdateVPCEConfigurationResultResponseTypeDef = TypedDict(
    "UpdateVPCEConfigurationResultResponseTypeDef",
    {
        "vpceConfiguration": "VPCEConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UploadTypeDef = TypedDict(
    "UploadTypeDef",
    {
        "arn": str,
        "name": str,
        "created": datetime,
        "type": UploadTypeType,
        "status": UploadStatusType,
        "url": str,
        "metadata": str,
        "contentType": str,
        "message": str,
        "category": UploadCategoryType,
    },
    total=False,
)

VPCEConfigurationTypeDef = TypedDict(
    "VPCEConfigurationTypeDef",
    {
        "arn": str,
        "vpceConfigurationName": str,
        "vpceServiceName": str,
        "serviceDnsName": str,
        "vpceConfigurationDescription": str,
    },
    total=False,
)
