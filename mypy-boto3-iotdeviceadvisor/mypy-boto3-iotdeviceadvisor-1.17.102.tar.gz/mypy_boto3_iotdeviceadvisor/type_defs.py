"""
Type annotations for iotdeviceadvisor service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iotdeviceadvisor.type_defs import CreateSuiteDefinitionRequestTypeDef

    data: CreateSuiteDefinitionRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import StatusType, SuiteRunStatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateSuiteDefinitionRequestTypeDef",
    "CreateSuiteDefinitionResponseResponseTypeDef",
    "DeleteSuiteDefinitionRequestTypeDef",
    "DeviceUnderTestTypeDef",
    "GetSuiteDefinitionRequestTypeDef",
    "GetSuiteDefinitionResponseResponseTypeDef",
    "GetSuiteRunReportRequestTypeDef",
    "GetSuiteRunReportResponseResponseTypeDef",
    "GetSuiteRunRequestTypeDef",
    "GetSuiteRunResponseResponseTypeDef",
    "GroupResultTypeDef",
    "ListSuiteDefinitionsRequestTypeDef",
    "ListSuiteDefinitionsResponseResponseTypeDef",
    "ListSuiteRunsRequestTypeDef",
    "ListSuiteRunsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "StartSuiteRunRequestTypeDef",
    "StartSuiteRunResponseResponseTypeDef",
    "StopSuiteRunRequestTypeDef",
    "SuiteDefinitionConfigurationTypeDef",
    "SuiteDefinitionInformationTypeDef",
    "SuiteRunConfigurationTypeDef",
    "SuiteRunInformationTypeDef",
    "TagResourceRequestTypeDef",
    "TestCaseRunTypeDef",
    "TestResultTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateSuiteDefinitionRequestTypeDef",
    "UpdateSuiteDefinitionResponseResponseTypeDef",
)

CreateSuiteDefinitionRequestTypeDef = TypedDict(
    "CreateSuiteDefinitionRequestTypeDef",
    {
        "suiteDefinitionConfiguration": "SuiteDefinitionConfigurationTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

CreateSuiteDefinitionResponseResponseTypeDef = TypedDict(
    "CreateSuiteDefinitionResponseResponseTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteDefinitionArn": str,
        "suiteDefinitionName": str,
        "createdAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSuiteDefinitionRequestTypeDef = TypedDict(
    "DeleteSuiteDefinitionRequestTypeDef",
    {
        "suiteDefinitionId": str,
    },
)

DeviceUnderTestTypeDef = TypedDict(
    "DeviceUnderTestTypeDef",
    {
        "thingArn": str,
        "certificateArn": str,
    },
    total=False,
)

_RequiredGetSuiteDefinitionRequestTypeDef = TypedDict(
    "_RequiredGetSuiteDefinitionRequestTypeDef",
    {
        "suiteDefinitionId": str,
    },
)
_OptionalGetSuiteDefinitionRequestTypeDef = TypedDict(
    "_OptionalGetSuiteDefinitionRequestTypeDef",
    {
        "suiteDefinitionVersion": str,
    },
    total=False,
)


class GetSuiteDefinitionRequestTypeDef(
    _RequiredGetSuiteDefinitionRequestTypeDef, _OptionalGetSuiteDefinitionRequestTypeDef
):
    pass


GetSuiteDefinitionResponseResponseTypeDef = TypedDict(
    "GetSuiteDefinitionResponseResponseTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteDefinitionArn": str,
        "suiteDefinitionVersion": str,
        "latestVersion": str,
        "suiteDefinitionConfiguration": "SuiteDefinitionConfigurationTypeDef",
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSuiteRunReportRequestTypeDef = TypedDict(
    "GetSuiteRunReportRequestTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteRunId": str,
    },
)

GetSuiteRunReportResponseResponseTypeDef = TypedDict(
    "GetSuiteRunReportResponseResponseTypeDef",
    {
        "qualificationReportDownloadUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSuiteRunRequestTypeDef = TypedDict(
    "GetSuiteRunRequestTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteRunId": str,
    },
)

GetSuiteRunResponseResponseTypeDef = TypedDict(
    "GetSuiteRunResponseResponseTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteDefinitionVersion": str,
        "suiteRunId": str,
        "suiteRunArn": str,
        "suiteRunConfiguration": "SuiteRunConfigurationTypeDef",
        "testResult": "TestResultTypeDef",
        "startTime": datetime,
        "endTime": datetime,
        "status": SuiteRunStatusType,
        "errorReason": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupResultTypeDef = TypedDict(
    "GroupResultTypeDef",
    {
        "groupId": str,
        "groupName": str,
        "tests": List["TestCaseRunTypeDef"],
    },
    total=False,
)

ListSuiteDefinitionsRequestTypeDef = TypedDict(
    "ListSuiteDefinitionsRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListSuiteDefinitionsResponseResponseTypeDef = TypedDict(
    "ListSuiteDefinitionsResponseResponseTypeDef",
    {
        "suiteDefinitionInformationList": List["SuiteDefinitionInformationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSuiteRunsRequestTypeDef = TypedDict(
    "ListSuiteRunsRequestTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteDefinitionVersion": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListSuiteRunsResponseResponseTypeDef = TypedDict(
    "ListSuiteRunsResponseResponseTypeDef",
    {
        "suiteRunsList": List["SuiteRunInformationTypeDef"],
        "nextToken": str,
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

_RequiredStartSuiteRunRequestTypeDef = TypedDict(
    "_RequiredStartSuiteRunRequestTypeDef",
    {
        "suiteDefinitionId": str,
    },
)
_OptionalStartSuiteRunRequestTypeDef = TypedDict(
    "_OptionalStartSuiteRunRequestTypeDef",
    {
        "suiteDefinitionVersion": str,
        "suiteRunConfiguration": "SuiteRunConfigurationTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)


class StartSuiteRunRequestTypeDef(
    _RequiredStartSuiteRunRequestTypeDef, _OptionalStartSuiteRunRequestTypeDef
):
    pass


StartSuiteRunResponseResponseTypeDef = TypedDict(
    "StartSuiteRunResponseResponseTypeDef",
    {
        "suiteRunId": str,
        "suiteRunArn": str,
        "createdAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopSuiteRunRequestTypeDef = TypedDict(
    "StopSuiteRunRequestTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteRunId": str,
    },
)

SuiteDefinitionConfigurationTypeDef = TypedDict(
    "SuiteDefinitionConfigurationTypeDef",
    {
        "suiteDefinitionName": str,
        "devices": List["DeviceUnderTestTypeDef"],
        "intendedForQualification": bool,
        "rootGroup": str,
        "devicePermissionRoleArn": str,
    },
    total=False,
)

SuiteDefinitionInformationTypeDef = TypedDict(
    "SuiteDefinitionInformationTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteDefinitionName": str,
        "defaultDevices": List["DeviceUnderTestTypeDef"],
        "intendedForQualification": bool,
        "createdAt": datetime,
    },
    total=False,
)

SuiteRunConfigurationTypeDef = TypedDict(
    "SuiteRunConfigurationTypeDef",
    {
        "primaryDevice": "DeviceUnderTestTypeDef",
        "selectedTestList": List[str],
    },
    total=False,
)

SuiteRunInformationTypeDef = TypedDict(
    "SuiteRunInformationTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteDefinitionVersion": str,
        "suiteDefinitionName": str,
        "suiteRunId": str,
        "createdAt": datetime,
        "startedAt": datetime,
        "endAt": datetime,
        "status": SuiteRunStatusType,
        "passed": int,
        "failed": int,
    },
    total=False,
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

TestCaseRunTypeDef = TypedDict(
    "TestCaseRunTypeDef",
    {
        "testCaseRunId": str,
        "testCaseDefinitionId": str,
        "testCaseDefinitionName": str,
        "status": StatusType,
        "startTime": datetime,
        "endTime": datetime,
        "logUrl": str,
        "warnings": str,
        "failure": str,
    },
    total=False,
)

TestResultTypeDef = TypedDict(
    "TestResultTypeDef",
    {
        "groups": List["GroupResultTypeDef"],
    },
    total=False,
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateSuiteDefinitionRequestTypeDef = TypedDict(
    "_RequiredUpdateSuiteDefinitionRequestTypeDef",
    {
        "suiteDefinitionId": str,
    },
)
_OptionalUpdateSuiteDefinitionRequestTypeDef = TypedDict(
    "_OptionalUpdateSuiteDefinitionRequestTypeDef",
    {
        "suiteDefinitionConfiguration": "SuiteDefinitionConfigurationTypeDef",
    },
    total=False,
)


class UpdateSuiteDefinitionRequestTypeDef(
    _RequiredUpdateSuiteDefinitionRequestTypeDef, _OptionalUpdateSuiteDefinitionRequestTypeDef
):
    pass


UpdateSuiteDefinitionResponseResponseTypeDef = TypedDict(
    "UpdateSuiteDefinitionResponseResponseTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteDefinitionArn": str,
        "suiteDefinitionName": str,
        "suiteDefinitionVersion": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
