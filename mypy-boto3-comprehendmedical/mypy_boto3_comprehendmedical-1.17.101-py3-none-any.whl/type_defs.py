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
from typing import List

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
    "DescribeEntitiesDetectionV2JobResponseTypeDef",
    "DescribeICD10CMInferenceJobResponseTypeDef",
    "DescribePHIDetectionJobResponseTypeDef",
    "DescribeRxNormInferenceJobResponseTypeDef",
    "DetectEntitiesResponseTypeDef",
    "DetectEntitiesV2ResponseTypeDef",
    "DetectPHIResponseTypeDef",
    "EntityTypeDef",
    "ICD10CMAttributeTypeDef",
    "ICD10CMConceptTypeDef",
    "ICD10CMEntityTypeDef",
    "ICD10CMTraitTypeDef",
    "InferICD10CMResponseTypeDef",
    "InferRxNormResponseTypeDef",
    "InputDataConfigTypeDef",
    "ListEntitiesDetectionV2JobsResponseTypeDef",
    "ListICD10CMInferenceJobsResponseTypeDef",
    "ListPHIDetectionJobsResponseTypeDef",
    "ListRxNormInferenceJobsResponseTypeDef",
    "OutputDataConfigTypeDef",
    "RxNormAttributeTypeDef",
    "RxNormConceptTypeDef",
    "RxNormEntityTypeDef",
    "RxNormTraitTypeDef",
    "StartEntitiesDetectionV2JobResponseTypeDef",
    "StartICD10CMInferenceJobResponseTypeDef",
    "StartPHIDetectionJobResponseTypeDef",
    "StartRxNormInferenceJobResponseTypeDef",
    "StopEntitiesDetectionV2JobResponseTypeDef",
    "StopICD10CMInferenceJobResponseTypeDef",
    "StopPHIDetectionJobResponseTypeDef",
    "StopRxNormInferenceJobResponseTypeDef",
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
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
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

DescribeEntitiesDetectionV2JobResponseTypeDef = TypedDict(
    "DescribeEntitiesDetectionV2JobResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobProperties": "ComprehendMedicalAsyncJobPropertiesTypeDef",
    },
    total=False,
)

DescribeICD10CMInferenceJobResponseTypeDef = TypedDict(
    "DescribeICD10CMInferenceJobResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobProperties": "ComprehendMedicalAsyncJobPropertiesTypeDef",
    },
    total=False,
)

DescribePHIDetectionJobResponseTypeDef = TypedDict(
    "DescribePHIDetectionJobResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobProperties": "ComprehendMedicalAsyncJobPropertiesTypeDef",
    },
    total=False,
)

DescribeRxNormInferenceJobResponseTypeDef = TypedDict(
    "DescribeRxNormInferenceJobResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobProperties": "ComprehendMedicalAsyncJobPropertiesTypeDef",
    },
    total=False,
)

_RequiredDetectEntitiesResponseTypeDef = TypedDict(
    "_RequiredDetectEntitiesResponseTypeDef",
    {
        "Entities": List["EntityTypeDef"],
        "ModelVersion": str,
    },
)
_OptionalDetectEntitiesResponseTypeDef = TypedDict(
    "_OptionalDetectEntitiesResponseTypeDef",
    {
        "UnmappedAttributes": List["UnmappedAttributeTypeDef"],
        "PaginationToken": str,
    },
    total=False,
)


class DetectEntitiesResponseTypeDef(
    _RequiredDetectEntitiesResponseTypeDef, _OptionalDetectEntitiesResponseTypeDef
):
    pass


_RequiredDetectEntitiesV2ResponseTypeDef = TypedDict(
    "_RequiredDetectEntitiesV2ResponseTypeDef",
    {
        "Entities": List["EntityTypeDef"],
        "ModelVersion": str,
    },
)
_OptionalDetectEntitiesV2ResponseTypeDef = TypedDict(
    "_OptionalDetectEntitiesV2ResponseTypeDef",
    {
        "UnmappedAttributes": List["UnmappedAttributeTypeDef"],
        "PaginationToken": str,
    },
    total=False,
)


class DetectEntitiesV2ResponseTypeDef(
    _RequiredDetectEntitiesV2ResponseTypeDef, _OptionalDetectEntitiesV2ResponseTypeDef
):
    pass


_RequiredDetectPHIResponseTypeDef = TypedDict(
    "_RequiredDetectPHIResponseTypeDef",
    {
        "Entities": List["EntityTypeDef"],
        "ModelVersion": str,
    },
)
_OptionalDetectPHIResponseTypeDef = TypedDict(
    "_OptionalDetectPHIResponseTypeDef",
    {
        "PaginationToken": str,
    },
    total=False,
)


class DetectPHIResponseTypeDef(
    _RequiredDetectPHIResponseTypeDef, _OptionalDetectPHIResponseTypeDef
):
    pass


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

_RequiredInferICD10CMResponseTypeDef = TypedDict(
    "_RequiredInferICD10CMResponseTypeDef",
    {
        "Entities": List["ICD10CMEntityTypeDef"],
    },
)
_OptionalInferICD10CMResponseTypeDef = TypedDict(
    "_OptionalInferICD10CMResponseTypeDef",
    {
        "PaginationToken": str,
        "ModelVersion": str,
    },
    total=False,
)


class InferICD10CMResponseTypeDef(
    _RequiredInferICD10CMResponseTypeDef, _OptionalInferICD10CMResponseTypeDef
):
    pass


_RequiredInferRxNormResponseTypeDef = TypedDict(
    "_RequiredInferRxNormResponseTypeDef",
    {
        "Entities": List["RxNormEntityTypeDef"],
    },
)
_OptionalInferRxNormResponseTypeDef = TypedDict(
    "_OptionalInferRxNormResponseTypeDef",
    {
        "PaginationToken": str,
        "ModelVersion": str,
    },
    total=False,
)


class InferRxNormResponseTypeDef(
    _RequiredInferRxNormResponseTypeDef, _OptionalInferRxNormResponseTypeDef
):
    pass


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


ListEntitiesDetectionV2JobsResponseTypeDef = TypedDict(
    "ListEntitiesDetectionV2JobsResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobPropertiesList": List[
            "ComprehendMedicalAsyncJobPropertiesTypeDef"
        ],
        "NextToken": str,
    },
    total=False,
)

ListICD10CMInferenceJobsResponseTypeDef = TypedDict(
    "ListICD10CMInferenceJobsResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobPropertiesList": List[
            "ComprehendMedicalAsyncJobPropertiesTypeDef"
        ],
        "NextToken": str,
    },
    total=False,
)

ListPHIDetectionJobsResponseTypeDef = TypedDict(
    "ListPHIDetectionJobsResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobPropertiesList": List[
            "ComprehendMedicalAsyncJobPropertiesTypeDef"
        ],
        "NextToken": str,
    },
    total=False,
)

ListRxNormInferenceJobsResponseTypeDef = TypedDict(
    "ListRxNormInferenceJobsResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobPropertiesList": List[
            "ComprehendMedicalAsyncJobPropertiesTypeDef"
        ],
        "NextToken": str,
    },
    total=False,
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

StartEntitiesDetectionV2JobResponseTypeDef = TypedDict(
    "StartEntitiesDetectionV2JobResponseTypeDef",
    {
        "JobId": str,
    },
    total=False,
)

StartICD10CMInferenceJobResponseTypeDef = TypedDict(
    "StartICD10CMInferenceJobResponseTypeDef",
    {
        "JobId": str,
    },
    total=False,
)

StartPHIDetectionJobResponseTypeDef = TypedDict(
    "StartPHIDetectionJobResponseTypeDef",
    {
        "JobId": str,
    },
    total=False,
)

StartRxNormInferenceJobResponseTypeDef = TypedDict(
    "StartRxNormInferenceJobResponseTypeDef",
    {
        "JobId": str,
    },
    total=False,
)

StopEntitiesDetectionV2JobResponseTypeDef = TypedDict(
    "StopEntitiesDetectionV2JobResponseTypeDef",
    {
        "JobId": str,
    },
    total=False,
)

StopICD10CMInferenceJobResponseTypeDef = TypedDict(
    "StopICD10CMInferenceJobResponseTypeDef",
    {
        "JobId": str,
    },
    total=False,
)

StopPHIDetectionJobResponseTypeDef = TypedDict(
    "StopPHIDetectionJobResponseTypeDef",
    {
        "JobId": str,
    },
    total=False,
)

StopRxNormInferenceJobResponseTypeDef = TypedDict(
    "StopRxNormInferenceJobResponseTypeDef",
    {
        "JobId": str,
    },
    total=False,
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
