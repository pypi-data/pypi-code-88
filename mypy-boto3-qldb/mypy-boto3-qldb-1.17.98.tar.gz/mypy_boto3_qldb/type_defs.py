"""
Type annotations for qldb service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb/type_defs.html)

Usage::

    ```python
    from mypy_boto3_qldb.type_defs import CancelJournalKinesisStreamResponseTypeDef

    data: CancelJournalKinesisStreamResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Union

from .literals import (
    ErrorCauseType,
    ExportStatusType,
    LedgerStateType,
    PermissionsModeType,
    S3ObjectEncryptionTypeType,
    StreamStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CancelJournalKinesisStreamResponseTypeDef",
    "CreateLedgerResponseTypeDef",
    "DescribeJournalKinesisStreamResponseTypeDef",
    "DescribeJournalS3ExportResponseTypeDef",
    "DescribeLedgerResponseTypeDef",
    "ExportJournalToS3ResponseTypeDef",
    "GetBlockResponseTypeDef",
    "GetDigestResponseTypeDef",
    "GetRevisionResponseTypeDef",
    "JournalKinesisStreamDescriptionTypeDef",
    "JournalS3ExportDescriptionTypeDef",
    "KinesisConfigurationTypeDef",
    "LedgerSummaryTypeDef",
    "ListJournalKinesisStreamsForLedgerResponseTypeDef",
    "ListJournalS3ExportsForLedgerResponseTypeDef",
    "ListJournalS3ExportsResponseTypeDef",
    "ListLedgersResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "S3EncryptionConfigurationTypeDef",
    "S3ExportConfigurationTypeDef",
    "StreamJournalToKinesisResponseTypeDef",
    "UpdateLedgerPermissionsModeResponseTypeDef",
    "UpdateLedgerResponseTypeDef",
    "ValueHolderTypeDef",
)

CancelJournalKinesisStreamResponseTypeDef = TypedDict(
    "CancelJournalKinesisStreamResponseTypeDef",
    {
        "StreamId": str,
    },
    total=False,
)

CreateLedgerResponseTypeDef = TypedDict(
    "CreateLedgerResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "State": LedgerStateType,
        "CreationDateTime": datetime,
        "PermissionsMode": PermissionsModeType,
        "DeletionProtection": bool,
    },
    total=False,
)

DescribeJournalKinesisStreamResponseTypeDef = TypedDict(
    "DescribeJournalKinesisStreamResponseTypeDef",
    {
        "Stream": "JournalKinesisStreamDescriptionTypeDef",
    },
    total=False,
)

DescribeJournalS3ExportResponseTypeDef = TypedDict(
    "DescribeJournalS3ExportResponseTypeDef",
    {
        "ExportDescription": "JournalS3ExportDescriptionTypeDef",
    },
)

DescribeLedgerResponseTypeDef = TypedDict(
    "DescribeLedgerResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "State": LedgerStateType,
        "CreationDateTime": datetime,
        "PermissionsMode": PermissionsModeType,
        "DeletionProtection": bool,
    },
    total=False,
)

ExportJournalToS3ResponseTypeDef = TypedDict(
    "ExportJournalToS3ResponseTypeDef",
    {
        "ExportId": str,
    },
)

_RequiredGetBlockResponseTypeDef = TypedDict(
    "_RequiredGetBlockResponseTypeDef",
    {
        "Block": "ValueHolderTypeDef",
    },
)
_OptionalGetBlockResponseTypeDef = TypedDict(
    "_OptionalGetBlockResponseTypeDef",
    {
        "Proof": "ValueHolderTypeDef",
    },
    total=False,
)


class GetBlockResponseTypeDef(_RequiredGetBlockResponseTypeDef, _OptionalGetBlockResponseTypeDef):
    pass


GetDigestResponseTypeDef = TypedDict(
    "GetDigestResponseTypeDef",
    {
        "Digest": Union[bytes, IO[bytes]],
        "DigestTipAddress": "ValueHolderTypeDef",
    },
)

_RequiredGetRevisionResponseTypeDef = TypedDict(
    "_RequiredGetRevisionResponseTypeDef",
    {
        "Revision": "ValueHolderTypeDef",
    },
)
_OptionalGetRevisionResponseTypeDef = TypedDict(
    "_OptionalGetRevisionResponseTypeDef",
    {
        "Proof": "ValueHolderTypeDef",
    },
    total=False,
)


class GetRevisionResponseTypeDef(
    _RequiredGetRevisionResponseTypeDef, _OptionalGetRevisionResponseTypeDef
):
    pass


_RequiredJournalKinesisStreamDescriptionTypeDef = TypedDict(
    "_RequiredJournalKinesisStreamDescriptionTypeDef",
    {
        "LedgerName": str,
        "RoleArn": str,
        "StreamId": str,
        "Status": StreamStatusType,
        "KinesisConfiguration": "KinesisConfigurationTypeDef",
        "StreamName": str,
    },
)
_OptionalJournalKinesisStreamDescriptionTypeDef = TypedDict(
    "_OptionalJournalKinesisStreamDescriptionTypeDef",
    {
        "CreationTime": datetime,
        "InclusiveStartTime": datetime,
        "ExclusiveEndTime": datetime,
        "Arn": str,
        "ErrorCause": ErrorCauseType,
    },
    total=False,
)


class JournalKinesisStreamDescriptionTypeDef(
    _RequiredJournalKinesisStreamDescriptionTypeDef, _OptionalJournalKinesisStreamDescriptionTypeDef
):
    pass


JournalS3ExportDescriptionTypeDef = TypedDict(
    "JournalS3ExportDescriptionTypeDef",
    {
        "LedgerName": str,
        "ExportId": str,
        "ExportCreationTime": datetime,
        "Status": ExportStatusType,
        "InclusiveStartTime": datetime,
        "ExclusiveEndTime": datetime,
        "S3ExportConfiguration": "S3ExportConfigurationTypeDef",
        "RoleArn": str,
    },
)

_RequiredKinesisConfigurationTypeDef = TypedDict(
    "_RequiredKinesisConfigurationTypeDef",
    {
        "StreamArn": str,
    },
)
_OptionalKinesisConfigurationTypeDef = TypedDict(
    "_OptionalKinesisConfigurationTypeDef",
    {
        "AggregationEnabled": bool,
    },
    total=False,
)


class KinesisConfigurationTypeDef(
    _RequiredKinesisConfigurationTypeDef, _OptionalKinesisConfigurationTypeDef
):
    pass


LedgerSummaryTypeDef = TypedDict(
    "LedgerSummaryTypeDef",
    {
        "Name": str,
        "State": LedgerStateType,
        "CreationDateTime": datetime,
    },
    total=False,
)

ListJournalKinesisStreamsForLedgerResponseTypeDef = TypedDict(
    "ListJournalKinesisStreamsForLedgerResponseTypeDef",
    {
        "Streams": List["JournalKinesisStreamDescriptionTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListJournalS3ExportsForLedgerResponseTypeDef = TypedDict(
    "ListJournalS3ExportsForLedgerResponseTypeDef",
    {
        "JournalS3Exports": List["JournalS3ExportDescriptionTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListJournalS3ExportsResponseTypeDef = TypedDict(
    "ListJournalS3ExportsResponseTypeDef",
    {
        "JournalS3Exports": List["JournalS3ExportDescriptionTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListLedgersResponseTypeDef = TypedDict(
    "ListLedgersResponseTypeDef",
    {
        "Ledgers": List["LedgerSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)

_RequiredS3EncryptionConfigurationTypeDef = TypedDict(
    "_RequiredS3EncryptionConfigurationTypeDef",
    {
        "ObjectEncryptionType": S3ObjectEncryptionTypeType,
    },
)
_OptionalS3EncryptionConfigurationTypeDef = TypedDict(
    "_OptionalS3EncryptionConfigurationTypeDef",
    {
        "KmsKeyArn": str,
    },
    total=False,
)


class S3EncryptionConfigurationTypeDef(
    _RequiredS3EncryptionConfigurationTypeDef, _OptionalS3EncryptionConfigurationTypeDef
):
    pass


S3ExportConfigurationTypeDef = TypedDict(
    "S3ExportConfigurationTypeDef",
    {
        "Bucket": str,
        "Prefix": str,
        "EncryptionConfiguration": "S3EncryptionConfigurationTypeDef",
    },
)

StreamJournalToKinesisResponseTypeDef = TypedDict(
    "StreamJournalToKinesisResponseTypeDef",
    {
        "StreamId": str,
    },
    total=False,
)

UpdateLedgerPermissionsModeResponseTypeDef = TypedDict(
    "UpdateLedgerPermissionsModeResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "PermissionsMode": PermissionsModeType,
    },
    total=False,
)

UpdateLedgerResponseTypeDef = TypedDict(
    "UpdateLedgerResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "State": LedgerStateType,
        "CreationDateTime": datetime,
        "DeletionProtection": bool,
    },
    total=False,
)

ValueHolderTypeDef = TypedDict(
    "ValueHolderTypeDef",
    {
        "IonText": str,
    },
    total=False,
)
