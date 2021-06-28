"""
Type annotations for meteringmarketplace service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_meteringmarketplace/type_defs.html)

Usage::

    ```python
    from mypy_boto3_meteringmarketplace.type_defs import BatchMeterUsageRequestTypeDef

    data: BatchMeterUsageRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import UsageRecordResultStatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BatchMeterUsageRequestTypeDef",
    "BatchMeterUsageResultResponseTypeDef",
    "MeterUsageRequestTypeDef",
    "MeterUsageResultResponseTypeDef",
    "RegisterUsageRequestTypeDef",
    "RegisterUsageResultResponseTypeDef",
    "ResolveCustomerRequestTypeDef",
    "ResolveCustomerResultResponseTypeDef",
    "ResponseMetadataTypeDef",
    "TagTypeDef",
    "UsageAllocationTypeDef",
    "UsageRecordResultTypeDef",
    "UsageRecordTypeDef",
)

BatchMeterUsageRequestTypeDef = TypedDict(
    "BatchMeterUsageRequestTypeDef",
    {
        "UsageRecords": List["UsageRecordTypeDef"],
        "ProductCode": str,
    },
)

BatchMeterUsageResultResponseTypeDef = TypedDict(
    "BatchMeterUsageResultResponseTypeDef",
    {
        "Results": List["UsageRecordResultTypeDef"],
        "UnprocessedRecords": List["UsageRecordTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMeterUsageRequestTypeDef = TypedDict(
    "_RequiredMeterUsageRequestTypeDef",
    {
        "ProductCode": str,
        "Timestamp": Union[datetime, str],
        "UsageDimension": str,
    },
)
_OptionalMeterUsageRequestTypeDef = TypedDict(
    "_OptionalMeterUsageRequestTypeDef",
    {
        "UsageQuantity": int,
        "DryRun": bool,
        "UsageAllocations": List["UsageAllocationTypeDef"],
    },
    total=False,
)


class MeterUsageRequestTypeDef(
    _RequiredMeterUsageRequestTypeDef, _OptionalMeterUsageRequestTypeDef
):
    pass


MeterUsageResultResponseTypeDef = TypedDict(
    "MeterUsageResultResponseTypeDef",
    {
        "MeteringRecordId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegisterUsageRequestTypeDef = TypedDict(
    "_RequiredRegisterUsageRequestTypeDef",
    {
        "ProductCode": str,
        "PublicKeyVersion": int,
    },
)
_OptionalRegisterUsageRequestTypeDef = TypedDict(
    "_OptionalRegisterUsageRequestTypeDef",
    {
        "Nonce": str,
    },
    total=False,
)


class RegisterUsageRequestTypeDef(
    _RequiredRegisterUsageRequestTypeDef, _OptionalRegisterUsageRequestTypeDef
):
    pass


RegisterUsageResultResponseTypeDef = TypedDict(
    "RegisterUsageResultResponseTypeDef",
    {
        "PublicKeyRotationTimestamp": datetime,
        "Signature": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResolveCustomerRequestTypeDef = TypedDict(
    "ResolveCustomerRequestTypeDef",
    {
        "RegistrationToken": str,
    },
)

ResolveCustomerResultResponseTypeDef = TypedDict(
    "ResolveCustomerResultResponseTypeDef",
    {
        "CustomerIdentifier": str,
        "ProductCode": str,
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

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

_RequiredUsageAllocationTypeDef = TypedDict(
    "_RequiredUsageAllocationTypeDef",
    {
        "AllocatedUsageQuantity": int,
    },
)
_OptionalUsageAllocationTypeDef = TypedDict(
    "_OptionalUsageAllocationTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class UsageAllocationTypeDef(_RequiredUsageAllocationTypeDef, _OptionalUsageAllocationTypeDef):
    pass


UsageRecordResultTypeDef = TypedDict(
    "UsageRecordResultTypeDef",
    {
        "UsageRecord": "UsageRecordTypeDef",
        "MeteringRecordId": str,
        "Status": UsageRecordResultStatusType,
    },
    total=False,
)

_RequiredUsageRecordTypeDef = TypedDict(
    "_RequiredUsageRecordTypeDef",
    {
        "Timestamp": Union[datetime, str],
        "CustomerIdentifier": str,
        "Dimension": str,
    },
)
_OptionalUsageRecordTypeDef = TypedDict(
    "_OptionalUsageRecordTypeDef",
    {
        "Quantity": int,
        "UsageAllocations": List["UsageAllocationTypeDef"],
    },
    total=False,
)


class UsageRecordTypeDef(_RequiredUsageRecordTypeDef, _OptionalUsageRecordTypeDef):
    pass
