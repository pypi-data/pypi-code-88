"""
Type annotations for comprehendmedical service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehendmedical/type_defs.html)

Usage::

    ```python
    from mypy_boto3_comprehendmedical.type_defs import AttributeTypeDef

    data: AttributeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AttributeNameType,
    EntitySubTypeType,
    EntityTypeType,
    ICD10CMAttributeTypeType,
    ICD10CMEntityTypeType,
    ICD10CMRelationshipTypeType,
    ICD10CMTraitNameType,
    JobStatusType,
    RelationshipTypeType,
    RxNormAttributeTypeType,
    RxNormEntityTypeType,
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
    "AttributeTypeDef",
    "ComprehendMedicalAsyncJobFilterTypeDef",
    "ComprehendMedicalAsyncJobPropertiesTypeDef",
    "DescribeEntitiesDetectionV2JobRequestTypeDef",
    "DescribeEntitiesDetectionV2JobResponseResponseTypeDef",
    "DescribeICD10CMInferenceJobRequestTypeDef",
    "DescribeICD10CMInferenceJobResponseResponseTypeDef",
    "DescribePHIDetectionJobRequestTypeDef",
    "DescribePHIDetectionJobResponseResponseTypeDef",
    "DescribeRxNormInferenceJobRequestTypeDef",
    "DescribeRxNormInferenceJobResponseResponseTypeDef",
    "DetectEntitiesRequestTypeDef",
    "DetectEntitiesResponseResponseTypeDef",
    "DetectEntitiesV2RequestTypeDef",
    "DetectEntitiesV2ResponseResponseTypeDef",
    "DetectPHIRequestTypeDef",
    "DetectPHIResponseResponseTypeDef",
    "EntityTypeDef",
    "ICD10CMAttributeTypeDef",
    "ICD10CMConceptTypeDef",
    "ICD10CMEntityTypeDef",
    "ICD10CMTraitTypeDef",
    "InferICD10CMRequestTypeDef",
    "InferICD10CMResponseResponseTypeDef",
    "InferRxNormRequestTypeDef",
    "InferRxNormResponseResponseTypeDef",
    "InputDataConfigTypeDef",
    "ListEntitiesDetectionV2JobsRequestTypeDef",
    "ListEntitiesDetectionV2JobsResponseResponseTypeDef",
    "ListICD10CMInferenceJobsRequestTypeDef",
    "ListICD10CMInferenceJobsResponseResponseTypeDef",
    "ListPHIDetectionJobsRequestTypeDef",
    "ListPHIDetectionJobsResponseResponseTypeDef",
    "ListRxNormInferenceJobsRequestTypeDef",
    "ListRxNormInferenceJobsResponseResponseTypeDef",
    "OutputDataConfigTypeDef",
    "ResponseMetadataTypeDef",
    "RxNormAttributeTypeDef",
    "RxNormConceptTypeDef",
    "RxNormEntityTypeDef",
    "RxNormTraitTypeDef",
    "StartEntitiesDetectionV2JobRequestTypeDef",
    "StartEntitiesDetectionV2JobResponseResponseTypeDef",
    "StartICD10CMInferenceJobRequestTypeDef",
    "StartICD10CMInferenceJobResponseResponseTypeDef",
    "StartPHIDetectionJobRequestTypeDef",
    "StartPHIDetectionJobResponseResponseTypeDef",
    "StartRxNormInferenceJobRequestTypeDef",
    "StartRxNormInferenceJobResponseResponseTypeDef",
    "StopEntitiesDetectionV2JobRequestTypeDef",
    "StopEntitiesDetectionV2JobResponseResponseTypeDef",
    "StopICD10CMInferenceJobRequestTypeDef",
    "StopICD10CMInferenceJobResponseResponseTypeDef",
    "StopPHIDetectionJobRequestTypeDef",
    "StopPHIDetectionJobResponseResponseTypeDef",
    "StopRxNormInferenceJobRequestTypeDef",
    "StopRxNormInferenceJobResponseResponseTypeDef",
    "TraitTypeDef",
    "UnmappedAttributeTypeDef",
)

AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "Type": EntitySubTypeType,
        "Score": float,
        "RelationshipScore": float,
        "RelationshipType": RelationshipTypeType,
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Text": str,
        "Category": EntityTypeType,
        "Traits": List["TraitTypeDef"],
    },
    total=False,
)

ComprehendMedicalAsyncJobFilterTypeDef = TypedDict(
    "ComprehendMedicalAsyncJobFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": JobStatusType,
        "SubmitTimeBefore": Union[datetime, str],
        "SubmitTimeAfter": Union[datetime, str],
    },
    total=False,
)

ComprehendMedicalAsyncJobPropertiesTypeDef = TypedDict(
    "ComprehendMedicalAsyncJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": JobStatusType,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "ExpirationTime": datetime,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "LanguageCode": Literal["en"],
        "DataAccessRoleArn": str,
        "ManifestFilePath": str,
        "KMSKey": str,
        "ModelVersion": str,
    },
    total=False,
)

DescribeEntitiesDetectionV2JobRequestTypeDef = TypedDict(
    "DescribeEntitiesDetectionV2JobRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeEntitiesDetectionV2JobResponseResponseTypeDef = TypedDict(
    "DescribeEntitiesDetectionV2JobResponseResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobProperties": "ComprehendMedicalAsyncJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeICD10CMInferenceJobRequestTypeDef = TypedDict(
    "DescribeICD10CMInferenceJobRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeICD10CMInferenceJobResponseResponseTypeDef = TypedDict(
    "DescribeICD10CMInferenceJobResponseResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobProperties": "ComprehendMedicalAsyncJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePHIDetectionJobRequestTypeDef = TypedDict(
    "DescribePHIDetectionJobRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribePHIDetectionJobResponseResponseTypeDef = TypedDict(
    "DescribePHIDetectionJobResponseResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobProperties": "ComprehendMedicalAsyncJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRxNormInferenceJobRequestTypeDef = TypedDict(
    "DescribeRxNormInferenceJobRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeRxNormInferenceJobResponseResponseTypeDef = TypedDict(
    "DescribeRxNormInferenceJobResponseResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobProperties": "ComprehendMedicalAsyncJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectEntitiesRequestTypeDef = TypedDict(
    "DetectEntitiesRequestTypeDef",
    {
        "Text": str,
    },
)

DetectEntitiesResponseResponseTypeDef = TypedDict(
    "DetectEntitiesResponseResponseTypeDef",
    {
        "Entities": List["EntityTypeDef"],
        "UnmappedAttributes": List["UnmappedAttributeTypeDef"],
        "PaginationToken": str,
        "ModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectEntitiesV2RequestTypeDef = TypedDict(
    "DetectEntitiesV2RequestTypeDef",
    {
        "Text": str,
    },
)

DetectEntitiesV2ResponseResponseTypeDef = TypedDict(
    "DetectEntitiesV2ResponseResponseTypeDef",
    {
        "Entities": List["EntityTypeDef"],
        "UnmappedAttributes": List["UnmappedAttributeTypeDef"],
        "PaginationToken": str,
        "ModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectPHIRequestTypeDef = TypedDict(
    "DetectPHIRequestTypeDef",
    {
        "Text": str,
    },
)

DetectPHIResponseResponseTypeDef = TypedDict(
    "DetectPHIResponseResponseTypeDef",
    {
        "Entities": List["EntityTypeDef"],
        "PaginationToken": str,
        "ModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EntityTypeDef = TypedDict(
    "EntityTypeDef",
    {
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Score": float,
        "Text": str,
        "Category": EntityTypeType,
        "Type": EntitySubTypeType,
        "Traits": List["TraitTypeDef"],
        "Attributes": List["AttributeTypeDef"],
    },
    total=False,
)

ICD10CMAttributeTypeDef = TypedDict(
    "ICD10CMAttributeTypeDef",
    {
        "Type": ICD10CMAttributeTypeType,
        "Score": float,
        "RelationshipScore": float,
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Text": str,
        "Traits": List["ICD10CMTraitTypeDef"],
        "Category": ICD10CMEntityTypeType,
        "RelationshipType": ICD10CMRelationshipTypeType,
    },
    total=False,
)

ICD10CMConceptTypeDef = TypedDict(
    "ICD10CMConceptTypeDef",
    {
        "Description": str,
        "Code": str,
        "Score": float,
    },
    total=False,
)

ICD10CMEntityTypeDef = TypedDict(
    "ICD10CMEntityTypeDef",
    {
        "Id": int,
        "Text": str,
        "Category": Literal["MEDICAL_CONDITION"],
        "Type": ICD10CMEntityTypeType,
        "Score": float,
        "BeginOffset": int,
        "EndOffset": int,
        "Attributes": List["ICD10CMAttributeTypeDef"],
        "Traits": List["ICD10CMTraitTypeDef"],
        "ICD10CMConcepts": List["ICD10CMConceptTypeDef"],
    },
    total=False,
)

ICD10CMTraitTypeDef = TypedDict(
    "ICD10CMTraitTypeDef",
    {
        "Name": ICD10CMTraitNameType,
        "Score": float,
    },
    total=False,
)

InferICD10CMRequestTypeDef = TypedDict(
    "InferICD10CMRequestTypeDef",
    {
        "Text": str,
    },
)

InferICD10CMResponseResponseTypeDef = TypedDict(
    "InferICD10CMResponseResponseTypeDef",
    {
        "Entities": List["ICD10CMEntityTypeDef"],
        "PaginationToken": str,
        "ModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InferRxNormRequestTypeDef = TypedDict(
    "InferRxNormRequestTypeDef",
    {
        "Text": str,
    },
)

InferRxNormResponseResponseTypeDef = TypedDict(
    "InferRxNormResponseResponseTypeDef",
    {
        "Entities": List["RxNormEntityTypeDef"],
        "PaginationToken": str,
        "ModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredInputDataConfigTypeDef = TypedDict(
    "_RequiredInputDataConfigTypeDef",
    {
        "S3Bucket": str,
    },
)
_OptionalInputDataConfigTypeDef = TypedDict(
    "_OptionalInputDataConfigTypeDef",
    {
        "S3Key": str,
    },
    total=False,
)


class InputDataConfigTypeDef(_RequiredInputDataConfigTypeDef, _OptionalInputDataConfigTypeDef):
    pass


ListEntitiesDetectionV2JobsRequestTypeDef = TypedDict(
    "ListEntitiesDetectionV2JobsRequestTypeDef",
    {
        "Filter": "ComprehendMedicalAsyncJobFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListEntitiesDetectionV2JobsResponseResponseTypeDef = TypedDict(
    "ListEntitiesDetectionV2JobsResponseResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobPropertiesList": List[
            "ComprehendMedicalAsyncJobPropertiesTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListICD10CMInferenceJobsRequestTypeDef = TypedDict(
    "ListICD10CMInferenceJobsRequestTypeDef",
    {
        "Filter": "ComprehendMedicalAsyncJobFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListICD10CMInferenceJobsResponseResponseTypeDef = TypedDict(
    "ListICD10CMInferenceJobsResponseResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobPropertiesList": List[
            "ComprehendMedicalAsyncJobPropertiesTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPHIDetectionJobsRequestTypeDef = TypedDict(
    "ListPHIDetectionJobsRequestTypeDef",
    {
        "Filter": "ComprehendMedicalAsyncJobFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListPHIDetectionJobsResponseResponseTypeDef = TypedDict(
    "ListPHIDetectionJobsResponseResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobPropertiesList": List[
            "ComprehendMedicalAsyncJobPropertiesTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRxNormInferenceJobsRequestTypeDef = TypedDict(
    "ListRxNormInferenceJobsRequestTypeDef",
    {
        "Filter": "ComprehendMedicalAsyncJobFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListRxNormInferenceJobsResponseResponseTypeDef = TypedDict(
    "ListRxNormInferenceJobsResponseResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobPropertiesList": List[
            "ComprehendMedicalAsyncJobPropertiesTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredOutputDataConfigTypeDef = TypedDict(
    "_RequiredOutputDataConfigTypeDef",
    {
        "S3Bucket": str,
    },
)
_OptionalOutputDataConfigTypeDef = TypedDict(
    "_OptionalOutputDataConfigTypeDef",
    {
        "S3Key": str,
    },
    total=False,
)


class OutputDataConfigTypeDef(_RequiredOutputDataConfigTypeDef, _OptionalOutputDataConfigTypeDef):
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

RxNormAttributeTypeDef = TypedDict(
    "RxNormAttributeTypeDef",
    {
        "Type": RxNormAttributeTypeType,
        "Score": float,
        "RelationshipScore": float,
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Text": str,
        "Traits": List["RxNormTraitTypeDef"],
    },
    total=False,
)

RxNormConceptTypeDef = TypedDict(
    "RxNormConceptTypeDef",
    {
        "Description": str,
        "Code": str,
        "Score": float,
    },
    total=False,
)

RxNormEntityTypeDef = TypedDict(
    "RxNormEntityTypeDef",
    {
        "Id": int,
        "Text": str,
        "Category": Literal["MEDICATION"],
        "Type": RxNormEntityTypeType,
        "Score": float,
        "BeginOffset": int,
        "EndOffset": int,
        "Attributes": List["RxNormAttributeTypeDef"],
        "Traits": List["RxNormTraitTypeDef"],
        "RxNormConcepts": List["RxNormConceptTypeDef"],
    },
    total=False,
)

RxNormTraitTypeDef = TypedDict(
    "RxNormTraitTypeDef",
    {
        "Name": Literal["NEGATION"],
        "Score": float,
    },
    total=False,
)

_RequiredStartEntitiesDetectionV2JobRequestTypeDef = TypedDict(
    "_RequiredStartEntitiesDetectionV2JobRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "LanguageCode": Literal["en"],
    },
)
_OptionalStartEntitiesDetectionV2JobRequestTypeDef = TypedDict(
    "_OptionalStartEntitiesDetectionV2JobRequestTypeDef",
    {
        "JobName": str,
        "ClientRequestToken": str,
        "KMSKey": str,
    },
    total=False,
)


class StartEntitiesDetectionV2JobRequestTypeDef(
    _RequiredStartEntitiesDetectionV2JobRequestTypeDef,
    _OptionalStartEntitiesDetectionV2JobRequestTypeDef,
):
    pass


StartEntitiesDetectionV2JobResponseResponseTypeDef = TypedDict(
    "StartEntitiesDetectionV2JobResponseResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartICD10CMInferenceJobRequestTypeDef = TypedDict(
    "_RequiredStartICD10CMInferenceJobRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "LanguageCode": Literal["en"],
    },
)
_OptionalStartICD10CMInferenceJobRequestTypeDef = TypedDict(
    "_OptionalStartICD10CMInferenceJobRequestTypeDef",
    {
        "JobName": str,
        "ClientRequestToken": str,
        "KMSKey": str,
    },
    total=False,
)


class StartICD10CMInferenceJobRequestTypeDef(
    _RequiredStartICD10CMInferenceJobRequestTypeDef, _OptionalStartICD10CMInferenceJobRequestTypeDef
):
    pass


StartICD10CMInferenceJobResponseResponseTypeDef = TypedDict(
    "StartICD10CMInferenceJobResponseResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartPHIDetectionJobRequestTypeDef = TypedDict(
    "_RequiredStartPHIDetectionJobRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "LanguageCode": Literal["en"],
    },
)
_OptionalStartPHIDetectionJobRequestTypeDef = TypedDict(
    "_OptionalStartPHIDetectionJobRequestTypeDef",
    {
        "JobName": str,
        "ClientRequestToken": str,
        "KMSKey": str,
    },
    total=False,
)


class StartPHIDetectionJobRequestTypeDef(
    _RequiredStartPHIDetectionJobRequestTypeDef, _OptionalStartPHIDetectionJobRequestTypeDef
):
    pass


StartPHIDetectionJobResponseResponseTypeDef = TypedDict(
    "StartPHIDetectionJobResponseResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartRxNormInferenceJobRequestTypeDef = TypedDict(
    "_RequiredStartRxNormInferenceJobRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "LanguageCode": Literal["en"],
    },
)
_OptionalStartRxNormInferenceJobRequestTypeDef = TypedDict(
    "_OptionalStartRxNormInferenceJobRequestTypeDef",
    {
        "JobName": str,
        "ClientRequestToken": str,
        "KMSKey": str,
    },
    total=False,
)


class StartRxNormInferenceJobRequestTypeDef(
    _RequiredStartRxNormInferenceJobRequestTypeDef, _OptionalStartRxNormInferenceJobRequestTypeDef
):
    pass


StartRxNormInferenceJobResponseResponseTypeDef = TypedDict(
    "StartRxNormInferenceJobResponseResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopEntitiesDetectionV2JobRequestTypeDef = TypedDict(
    "StopEntitiesDetectionV2JobRequestTypeDef",
    {
        "JobId": str,
    },
)

StopEntitiesDetectionV2JobResponseResponseTypeDef = TypedDict(
    "StopEntitiesDetectionV2JobResponseResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopICD10CMInferenceJobRequestTypeDef = TypedDict(
    "StopICD10CMInferenceJobRequestTypeDef",
    {
        "JobId": str,
    },
)

StopICD10CMInferenceJobResponseResponseTypeDef = TypedDict(
    "StopICD10CMInferenceJobResponseResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopPHIDetectionJobRequestTypeDef = TypedDict(
    "StopPHIDetectionJobRequestTypeDef",
    {
        "JobId": str,
    },
)

StopPHIDetectionJobResponseResponseTypeDef = TypedDict(
    "StopPHIDetectionJobResponseResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopRxNormInferenceJobRequestTypeDef = TypedDict(
    "StopRxNormInferenceJobRequestTypeDef",
    {
        "JobId": str,
    },
)

StopRxNormInferenceJobResponseResponseTypeDef = TypedDict(
    "StopRxNormInferenceJobResponseResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TraitTypeDef = TypedDict(
    "TraitTypeDef",
    {
        "Name": AttributeNameType,
        "Score": float,
    },
    total=False,
)

UnmappedAttributeTypeDef = TypedDict(
    "UnmappedAttributeTypeDef",
    {
        "Type": EntityTypeType,
        "Attribute": "AttributeTypeDef",
    },
    total=False,
)
