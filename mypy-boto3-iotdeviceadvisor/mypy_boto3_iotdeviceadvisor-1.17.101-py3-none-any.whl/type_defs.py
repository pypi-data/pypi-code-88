"""
Type annotations for iotdeviceadvisor service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iotdeviceadvisor.type_defs import CreateSuiteDefinitionResponseTypeDef

    data: CreateSuiteDefinitionResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from .literals import StatusType, SuiteRunStatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateSuiteDefinitionResponseTypeDef",
    "DeviceUnderTestTypeDef",
    "GetSuiteDefinitionResponseTypeDef",
    "GetSuiteRunReportResponseTypeDef",
    "GetSuiteRunResponseTypeDef",
    "GroupResultTypeDef",
    "ListSuiteDefinitionsResponseTypeDef",
    "ListSuiteRunsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartSuiteRunResponseTypeDef",
    "SuiteDefinitionConfigurationTypeDef",
    "SuiteDefinitionInformationTypeDef",
    "SuiteRunConfigurationTypeDef",
    "SuiteRunInformationTypeDef",
    "TestCaseRunTypeDef",
    "TestResultTypeDef",
    "UpdateSuiteDefinitionResponseTypeDef",
)

CreateSuiteDefinitionResponseTypeDef = TypedDict(
    "CreateSuiteDefinitionResponseTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteDefinitionArn": str,
        "suiteDefinitionName": str,
        "createdAt": datetime,
    },
    total=False,
)

DeviceUnderTestTypeDef = TypedDict(
    "DeviceUnderTestTypeDef",
    {
        "thingArn": str,
        "certificateArn": str,
    },
    total=False,
)

GetSuiteDefinitionResponseTypeDef = TypedDict(
    "GetSuiteDefinitionResponseTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteDefinitionArn": str,
        "suiteDefinitionVersion": str,
        "latestVersion": str,
        "suiteDefinitionConfiguration": "SuiteDefinitionConfigurationTypeDef",
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

GetSuiteRunReportResponseTypeDef = TypedDict(
    "GetSuiteRunReportResponseTypeDef",
    {
        "qualificationReportDownloadUrl": str,
    },
    total=False,
)

GetSuiteRunResponseTypeDef = TypedDict(
    "GetSuiteRunResponseTypeDef",
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
    },
    total=False,
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

ListSuiteDefinitionsResponseTypeDef = TypedDict(
    "ListSuiteDefinitionsResponseTypeDef",
    {
        "suiteDefinitionInformationList": List["SuiteDefinitionInformationTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListSuiteRunsResponseTypeDef = TypedDict(
    "ListSuiteRunsResponseTypeDef",
    {
        "suiteRunsList": List["SuiteRunInformationTypeDef"],
        "nextToken": str,
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

StartSuiteRunResponseTypeDef = TypedDict(
    "StartSuiteRunResponseTypeDef",
    {
        "suiteRunId": str,
        "suiteRunArn": str,
        "createdAt": datetime,
    },
    total=False,
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

UpdateSuiteDefinitionResponseTypeDef = TypedDict(
    "UpdateSuiteDefinitionResponseTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteDefinitionArn": str,
        "suiteDefinitionName": str,
        "suiteDefinitionVersion": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
    },
    total=False,
)
