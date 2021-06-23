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
from typing import Dict, List

from .literals import (
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
    "CreateDevicePoolResultTypeDef",
    "CreateInstanceProfileResultTypeDef",
    "CreateNetworkProfileResultTypeDef",
    "CreateProjectResultTypeDef",
    "CreateRemoteAccessSessionConfigurationTypeDef",
    "CreateRemoteAccessSessionResultTypeDef",
    "CreateTestGridProjectResultTypeDef",
    "CreateTestGridUrlResultTypeDef",
    "CreateUploadResultTypeDef",
    "CreateVPCEConfigurationResultTypeDef",
    "CustomerArtifactPathsTypeDef",
    "DeviceFilterTypeDef",
    "DeviceInstanceTypeDef",
    "DeviceMinutesTypeDef",
    "DevicePoolCompatibilityResultTypeDef",
    "DevicePoolTypeDef",
    "DeviceSelectionConfigurationTypeDef",
    "DeviceSelectionResultTypeDef",
    "DeviceTypeDef",
    "ExecutionConfigurationTypeDef",
    "GetAccountSettingsResultTypeDef",
    "GetDeviceInstanceResultTypeDef",
    "GetDevicePoolCompatibilityResultTypeDef",
    "GetDevicePoolResultTypeDef",
    "GetDeviceResultTypeDef",
    "GetInstanceProfileResultTypeDef",
    "GetJobResultTypeDef",
    "GetNetworkProfileResultTypeDef",
    "GetOfferingStatusResultTypeDef",
    "GetProjectResultTypeDef",
    "GetRemoteAccessSessionResultTypeDef",
    "GetRunResultTypeDef",
    "GetSuiteResultTypeDef",
    "GetTestGridProjectResultTypeDef",
    "GetTestGridSessionResultTypeDef",
    "GetTestResultTypeDef",
    "GetUploadResultTypeDef",
    "GetVPCEConfigurationResultTypeDef",
    "IncompatibilityMessageTypeDef",
    "InstallToRemoteAccessSessionResultTypeDef",
    "InstanceProfileTypeDef",
    "JobTypeDef",
    "ListArtifactsResultTypeDef",
    "ListDeviceInstancesResultTypeDef",
    "ListDevicePoolsResultTypeDef",
    "ListDevicesResultTypeDef",
    "ListInstanceProfilesResultTypeDef",
    "ListJobsResultTypeDef",
    "ListNetworkProfilesResultTypeDef",
    "ListOfferingPromotionsResultTypeDef",
    "ListOfferingTransactionsResultTypeDef",
    "ListOfferingsResultTypeDef",
    "ListProjectsResultTypeDef",
    "ListRemoteAccessSessionsResultTypeDef",
    "ListRunsResultTypeDef",
    "ListSamplesResultTypeDef",
    "ListSuitesResultTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTestGridProjectsResultTypeDef",
    "ListTestGridSessionActionsResultTypeDef",
    "ListTestGridSessionArtifactsResultTypeDef",
    "ListTestGridSessionsResultTypeDef",
    "ListTestsResultTypeDef",
    "ListUniqueProblemsResultTypeDef",
    "ListUploadsResultTypeDef",
    "ListVPCEConfigurationsResultTypeDef",
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
    "PurchaseOfferingResultTypeDef",
    "RadiosTypeDef",
    "RecurringChargeTypeDef",
    "RemoteAccessSessionTypeDef",
    "RenewOfferingResultTypeDef",
    "ResolutionTypeDef",
    "RuleTypeDef",
    "RunTypeDef",
    "SampleTypeDef",
    "ScheduleRunConfigurationTypeDef",
    "ScheduleRunResultTypeDef",
    "ScheduleRunTestTypeDef",
    "StopJobResultTypeDef",
    "StopRemoteAccessSessionResultTypeDef",
    "StopRunResultTypeDef",
    "SuiteTypeDef",
    "TagTypeDef",
    "TestGridProjectTypeDef",
    "TestGridSessionActionTypeDef",
    "TestGridSessionArtifactTypeDef",
    "TestGridSessionTypeDef",
    "TestGridVpcConfigTypeDef",
    "TestTypeDef",
    "TrialMinutesTypeDef",
    "UniqueProblemTypeDef",
    "UpdateDeviceInstanceResultTypeDef",
    "UpdateDevicePoolResultTypeDef",
    "UpdateInstanceProfileResultTypeDef",
    "UpdateNetworkProfileResultTypeDef",
    "UpdateProjectResultTypeDef",
    "UpdateTestGridProjectResultTypeDef",
    "UpdateUploadResultTypeDef",
    "UpdateVPCEConfigurationResultTypeDef",
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

CreateDevicePoolResultTypeDef = TypedDict(
    "CreateDevicePoolResultTypeDef",
    {
        "devicePool": "DevicePoolTypeDef",
    },
    total=False,
)

CreateInstanceProfileResultTypeDef = TypedDict(
    "CreateInstanceProfileResultTypeDef",
    {
        "instanceProfile": "InstanceProfileTypeDef",
    },
    total=False,
)

CreateNetworkProfileResultTypeDef = TypedDict(
    "CreateNetworkProfileResultTypeDef",
    {
        "networkProfile": "NetworkProfileTypeDef",
    },
    total=False,
)

CreateProjectResultTypeDef = TypedDict(
    "CreateProjectResultTypeDef",
    {
        "project": "ProjectTypeDef",
    },
    total=False,
)

CreateRemoteAccessSessionConfigurationTypeDef = TypedDict(
    "CreateRemoteAccessSessionConfigurationTypeDef",
    {
        "billingMethod": BillingMethodType,
        "vpceConfigurationArns": List[str],
    },
    total=False,
)

CreateRemoteAccessSessionResultTypeDef = TypedDict(
    "CreateRemoteAccessSessionResultTypeDef",
    {
        "remoteAccessSession": "RemoteAccessSessionTypeDef",
    },
    total=False,
)

CreateTestGridProjectResultTypeDef = TypedDict(
    "CreateTestGridProjectResultTypeDef",
    {
        "testGridProject": "TestGridProjectTypeDef",
    },
    total=False,
)

CreateTestGridUrlResultTypeDef = TypedDict(
    "CreateTestGridUrlResultTypeDef",
    {
        "url": str,
        "expires": datetime,
    },
    total=False,
)

CreateUploadResultTypeDef = TypedDict(
    "CreateUploadResultTypeDef",
    {
        "upload": "UploadTypeDef",
    },
    total=False,
)

CreateVPCEConfigurationResultTypeDef = TypedDict(
    "CreateVPCEConfigurationResultTypeDef",
    {
        "vpceConfiguration": "VPCEConfigurationTypeDef",
    },
    total=False,
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

GetAccountSettingsResultTypeDef = TypedDict(
    "GetAccountSettingsResultTypeDef",
    {
        "accountSettings": "AccountSettingsTypeDef",
    },
    total=False,
)

GetDeviceInstanceResultTypeDef = TypedDict(
    "GetDeviceInstanceResultTypeDef",
    {
        "deviceInstance": "DeviceInstanceTypeDef",
    },
    total=False,
)

GetDevicePoolCompatibilityResultTypeDef = TypedDict(
    "GetDevicePoolCompatibilityResultTypeDef",
    {
        "compatibleDevices": List["DevicePoolCompatibilityResultTypeDef"],
        "incompatibleDevices": List["DevicePoolCompatibilityResultTypeDef"],
    },
    total=False,
)

GetDevicePoolResultTypeDef = TypedDict(
    "GetDevicePoolResultTypeDef",
    {
        "devicePool": "DevicePoolTypeDef",
    },
    total=False,
)

GetDeviceResultTypeDef = TypedDict(
    "GetDeviceResultTypeDef",
    {
        "device": "DeviceTypeDef",
    },
    total=False,
)

GetInstanceProfileResultTypeDef = TypedDict(
    "GetInstanceProfileResultTypeDef",
    {
        "instanceProfile": "InstanceProfileTypeDef",
    },
    total=False,
)

GetJobResultTypeDef = TypedDict(
    "GetJobResultTypeDef",
    {
        "job": "JobTypeDef",
    },
    total=False,
)

GetNetworkProfileResultTypeDef = TypedDict(
    "GetNetworkProfileResultTypeDef",
    {
        "networkProfile": "NetworkProfileTypeDef",
    },
    total=False,
)

GetOfferingStatusResultTypeDef = TypedDict(
    "GetOfferingStatusResultTypeDef",
    {
        "current": Dict[str, "OfferingStatusTypeDef"],
        "nextPeriod": Dict[str, "OfferingStatusTypeDef"],
        "nextToken": str,
    },
    total=False,
)

GetProjectResultTypeDef = TypedDict(
    "GetProjectResultTypeDef",
    {
        "project": "ProjectTypeDef",
    },
    total=False,
)

GetRemoteAccessSessionResultTypeDef = TypedDict(
    "GetRemoteAccessSessionResultTypeDef",
    {
        "remoteAccessSession": "RemoteAccessSessionTypeDef",
    },
    total=False,
)

GetRunResultTypeDef = TypedDict(
    "GetRunResultTypeDef",
    {
        "run": "RunTypeDef",
    },
    total=False,
)

GetSuiteResultTypeDef = TypedDict(
    "GetSuiteResultTypeDef",
    {
        "suite": "SuiteTypeDef",
    },
    total=False,
)

GetTestGridProjectResultTypeDef = TypedDict(
    "GetTestGridProjectResultTypeDef",
    {
        "testGridProject": "TestGridProjectTypeDef",
    },
    total=False,
)

GetTestGridSessionResultTypeDef = TypedDict(
    "GetTestGridSessionResultTypeDef",
    {
        "testGridSession": "TestGridSessionTypeDef",
    },
    total=False,
)

GetTestResultTypeDef = TypedDict(
    "GetTestResultTypeDef",
    {
        "test": "TestTypeDef",
    },
    total=False,
)

GetUploadResultTypeDef = TypedDict(
    "GetUploadResultTypeDef",
    {
        "upload": "UploadTypeDef",
    },
    total=False,
)

GetVPCEConfigurationResultTypeDef = TypedDict(
    "GetVPCEConfigurationResultTypeDef",
    {
        "vpceConfiguration": "VPCEConfigurationTypeDef",
    },
    total=False,
)

IncompatibilityMessageTypeDef = TypedDict(
    "IncompatibilityMessageTypeDef",
    {
        "message": str,
        "type": DeviceAttributeType,
    },
    total=False,
)

InstallToRemoteAccessSessionResultTypeDef = TypedDict(
    "InstallToRemoteAccessSessionResultTypeDef",
    {
        "appUpload": "UploadTypeDef",
    },
    total=False,
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

ListArtifactsResultTypeDef = TypedDict(
    "ListArtifactsResultTypeDef",
    {
        "artifacts": List["ArtifactTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListDeviceInstancesResultTypeDef = TypedDict(
    "ListDeviceInstancesResultTypeDef",
    {
        "deviceInstances": List["DeviceInstanceTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListDevicePoolsResultTypeDef = TypedDict(
    "ListDevicePoolsResultTypeDef",
    {
        "devicePools": List["DevicePoolTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListDevicesResultTypeDef = TypedDict(
    "ListDevicesResultTypeDef",
    {
        "devices": List["DeviceTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListInstanceProfilesResultTypeDef = TypedDict(
    "ListInstanceProfilesResultTypeDef",
    {
        "instanceProfiles": List["InstanceProfileTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListJobsResultTypeDef = TypedDict(
    "ListJobsResultTypeDef",
    {
        "jobs": List["JobTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListNetworkProfilesResultTypeDef = TypedDict(
    "ListNetworkProfilesResultTypeDef",
    {
        "networkProfiles": List["NetworkProfileTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListOfferingPromotionsResultTypeDef = TypedDict(
    "ListOfferingPromotionsResultTypeDef",
    {
        "offeringPromotions": List["OfferingPromotionTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListOfferingTransactionsResultTypeDef = TypedDict(
    "ListOfferingTransactionsResultTypeDef",
    {
        "offeringTransactions": List["OfferingTransactionTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListOfferingsResultTypeDef = TypedDict(
    "ListOfferingsResultTypeDef",
    {
        "offerings": List["OfferingTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListProjectsResultTypeDef = TypedDict(
    "ListProjectsResultTypeDef",
    {
        "projects": List["ProjectTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListRemoteAccessSessionsResultTypeDef = TypedDict(
    "ListRemoteAccessSessionsResultTypeDef",
    {
        "remoteAccessSessions": List["RemoteAccessSessionTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListRunsResultTypeDef = TypedDict(
    "ListRunsResultTypeDef",
    {
        "runs": List["RunTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListSamplesResultTypeDef = TypedDict(
    "ListSamplesResultTypeDef",
    {
        "samples": List["SampleTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListSuitesResultTypeDef = TypedDict(
    "ListSuitesResultTypeDef",
    {
        "suites": List["SuiteTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ListTestGridProjectsResultTypeDef = TypedDict(
    "ListTestGridProjectsResultTypeDef",
    {
        "testGridProjects": List["TestGridProjectTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListTestGridSessionActionsResultTypeDef = TypedDict(
    "ListTestGridSessionActionsResultTypeDef",
    {
        "actions": List["TestGridSessionActionTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListTestGridSessionArtifactsResultTypeDef = TypedDict(
    "ListTestGridSessionArtifactsResultTypeDef",
    {
        "artifacts": List["TestGridSessionArtifactTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListTestGridSessionsResultTypeDef = TypedDict(
    "ListTestGridSessionsResultTypeDef",
    {
        "testGridSessions": List["TestGridSessionTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListTestsResultTypeDef = TypedDict(
    "ListTestsResultTypeDef",
    {
        "tests": List["TestTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListUniqueProblemsResultTypeDef = TypedDict(
    "ListUniqueProblemsResultTypeDef",
    {
        "uniqueProblems": Dict[ExecutionResultType, List["UniqueProblemTypeDef"]],
        "nextToken": str,
    },
    total=False,
)

ListUploadsResultTypeDef = TypedDict(
    "ListUploadsResultTypeDef",
    {
        "uploads": List["UploadTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListVPCEConfigurationsResultTypeDef = TypedDict(
    "ListVPCEConfigurationsResultTypeDef",
    {
        "vpceConfigurations": List["VPCEConfigurationTypeDef"],
        "nextToken": str,
    },
    total=False,
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

PurchaseOfferingResultTypeDef = TypedDict(
    "PurchaseOfferingResultTypeDef",
    {
        "offeringTransaction": "OfferingTransactionTypeDef",
    },
    total=False,
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

RenewOfferingResultTypeDef = TypedDict(
    "RenewOfferingResultTypeDef",
    {
        "offeringTransaction": "OfferingTransactionTypeDef",
    },
    total=False,
)

ResolutionTypeDef = TypedDict(
    "ResolutionTypeDef",
    {
        "width": int,
        "height": int,
    },
    total=False,
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

ScheduleRunResultTypeDef = TypedDict(
    "ScheduleRunResultTypeDef",
    {
        "run": "RunTypeDef",
    },
    total=False,
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


StopJobResultTypeDef = TypedDict(
    "StopJobResultTypeDef",
    {
        "job": "JobTypeDef",
    },
    total=False,
)

StopRemoteAccessSessionResultTypeDef = TypedDict(
    "StopRemoteAccessSessionResultTypeDef",
    {
        "remoteAccessSession": "RemoteAccessSessionTypeDef",
    },
    total=False,
)

StopRunResultTypeDef = TypedDict(
    "StopRunResultTypeDef",
    {
        "run": "RunTypeDef",
    },
    total=False,
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

UpdateDeviceInstanceResultTypeDef = TypedDict(
    "UpdateDeviceInstanceResultTypeDef",
    {
        "deviceInstance": "DeviceInstanceTypeDef",
    },
    total=False,
)

UpdateDevicePoolResultTypeDef = TypedDict(
    "UpdateDevicePoolResultTypeDef",
    {
        "devicePool": "DevicePoolTypeDef",
    },
    total=False,
)

UpdateInstanceProfileResultTypeDef = TypedDict(
    "UpdateInstanceProfileResultTypeDef",
    {
        "instanceProfile": "InstanceProfileTypeDef",
    },
    total=False,
)

UpdateNetworkProfileResultTypeDef = TypedDict(
    "UpdateNetworkProfileResultTypeDef",
    {
        "networkProfile": "NetworkProfileTypeDef",
    },
    total=False,
)

UpdateProjectResultTypeDef = TypedDict(
    "UpdateProjectResultTypeDef",
    {
        "project": "ProjectTypeDef",
    },
    total=False,
)

UpdateTestGridProjectResultTypeDef = TypedDict(
    "UpdateTestGridProjectResultTypeDef",
    {
        "testGridProject": "TestGridProjectTypeDef",
    },
    total=False,
)

UpdateUploadResultTypeDef = TypedDict(
    "UpdateUploadResultTypeDef",
    {
        "upload": "UploadTypeDef",
    },
    total=False,
)

UpdateVPCEConfigurationResultTypeDef = TypedDict(
    "UpdateVPCEConfigurationResultTypeDef",
    {
        "vpceConfiguration": "VPCEConfigurationTypeDef",
    },
    total=False,
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
