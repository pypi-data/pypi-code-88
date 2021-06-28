"""
Type annotations for qldb service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb/type_defs.html)

Usage::

    ```python
    from mypy_boto3_qldb.type_defs import CancelJournalKinesisStreamRequestTypeDef

    data: CancelJournalKinesisStreamRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

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
    "CancelJournalKinesisStreamRequestTypeDef",
    "CancelJournalKinesisStreamResponseResponseTypeDef",
    "CreateLedgerRequestTypeDef",
    "CreateLedgerResponseResponseTypeDef",
    "DeleteLedgerRequestTypeDef",
    "DescribeJournalKinesisStreamRequestTypeDef",
    "DescribeJournalKinesisStreamResponseResponseTypeDef",
    "DescribeJournalS3ExportRequestTypeDef",
    "DescribeJournalS3ExportResponseResponseTypeDef",
    "DescribeLedgerRequestTypeDef",
    "DescribeLedgerResponseResponseTypeDef",
    "ExportJournalToS3RequestTypeDef",
    "ExportJournalToS3ResponseResponseTypeDef",
    "GetBlockRequestTypeDef",
    "GetBlockResponseResponseTypeDef",
    "GetDigestRequestTypeDef",
    "GetDigestResponseResponseTypeDef",
    "GetRevisionRequestTypeDef",
    "GetRevisionResponseResponseTypeDef",
    "JournalKinesisStreamDescriptionTypeDef",
    "JournalS3ExportDescriptionTypeDef",
    "KinesisConfigurationTypeDef",
    "LedgerSummaryTypeDef",
    "ListJournalKinesisStreamsForLedgerRequestTypeDef",
    "ListJournalKinesisStreamsForLedgerResponseResponseTypeDef",
    "ListJournalS3ExportsForLedgerRequestTypeDef",
    "ListJournalS3ExportsForLedgerResponseResponseTypeDef",
    "ListJournalS3ExportsRequestTypeDef",
    "ListJournalS3ExportsResponseResponseTypeDef",
    "ListLedgersRequestTypeDef",
    "ListLedgersResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "S3EncryptionConfigurationTypeDef",
    "S3ExportConfigurationTypeDef",
    "StreamJournalToKinesisRequestTypeDef",
    "StreamJournalToKinesisResponseResponseTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateLedgerPermissionsModeRequestTypeDef",
    "UpdateLedgerPermissionsModeResponseResponseTypeDef",
    "UpdateLedgerRequestTypeDef",
    "UpdateLedgerResponseResponseTypeDef",
    "ValueHolderTypeDef",
)

CancelJournalKinesisStreamRequestTypeDef = TypedDict(
    "CancelJournalKinesisStreamRequestTypeDef",
    {
        "LedgerName": str,
        "StreamId": str,
    },
)

CancelJournalKinesisStreamResponseResponseTypeDef = TypedDict(
    "CancelJournalKinesisStreamResponseResponseTypeDef",
    {
        "StreamId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLedgerRequestTypeDef = TypedDict(
    "_RequiredCreateLedgerRequestTypeDef",
    {
        "Name": str,
        "PermissionsMode": PermissionsModeType,
    },
)
_OptionalCreateLedgerRequestTypeDef = TypedDict(
    "_OptionalCreateLedgerRequestTypeDef",
    {
        "Tags": Dict[str, str],
        "DeletionProtection": bool,
    },
    total=False,
)


class CreateLedgerRequestTypeDef(
    _RequiredCreateLedgerRequestTypeDef, _OptionalCreateLedgerRequestTypeDef
):
    pass


CreateLedgerResponseResponseTypeDef = TypedDict(
    "CreateLedgerResponseResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "State": LedgerStateType,
        "CreationDateTime": datetime,
        "PermissionsMode": PermissionsModeType,
        "DeletionProtection": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLedgerRequestTypeDef = TypedDict(
    "DeleteLedgerRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeJournalKinesisStreamRequestTypeDef = TypedDict(
    "DescribeJournalKinesisStreamRequestTypeDef",
    {
        "LedgerName": str,
        "StreamId": str,
    },
)

DescribeJournalKinesisStreamResponseResponseTypeDef = TypedDict(
    "DescribeJournalKinesisStreamResponseResponseTypeDef",
    {
        "Stream": "JournalKinesisStreamDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJournalS3ExportRequestTypeDef = TypedDict(
    "DescribeJournalS3ExportRequestTypeDef",
    {
        "Name": str,
        "ExportId": str,
    },
)

DescribeJournalS3ExportResponseResponseTypeDef = TypedDict(
    "DescribeJournalS3ExportResponseResponseTypeDef",
    {
        "ExportDescription": "JournalS3ExportDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLedgerRequestTypeDef = TypedDict(
    "DescribeLedgerRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeLedgerResponseResponseTypeDef = TypedDict(
    "DescribeLedgerResponseResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "State": LedgerStateType,
        "CreationDateTime": datetime,
        "PermissionsMode": PermissionsModeType,
        "DeletionProtection": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportJournalToS3RequestTypeDef = TypedDict(
    "ExportJournalToS3RequestTypeDef",
    {
        "Name": str,
        "InclusiveStartTime": Union[datetime, str],
        "ExclusiveEndTime": Union[datetime, str],
        "S3ExportConfiguration": "S3ExportConfigurationTypeDef",
        "RoleArn": str,
    },
)

ExportJournalToS3ResponseResponseTypeDef = TypedDict(
    "ExportJournalToS3ResponseResponseTypeDef",
    {
        "ExportId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBlockRequestTypeDef = TypedDict(
    "_RequiredGetBlockRequestTypeDef",
    {
        "Name": str,
        "BlockAddress": "ValueHolderTypeDef",
    },
)
_OptionalGetBlockRequestTypeDef = TypedDict(
    "_OptionalGetBlockRequestTypeDef",
    {
        "DigestTipAddress": "ValueHolderTypeDef",
    },
    total=False,
)


class GetBlockRequestTypeDef(_RequiredGetBlockRequestTypeDef, _OptionalGetBlockRequestTypeDef):
    pass


GetBlockResponseResponseTypeDef = TypedDict(
    "GetBlockResponseResponseTypeDef",
    {
        "Block": "ValueHolderTypeDef",
        "Proof": "ValueHolderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDigestRequestTypeDef = TypedDict(
    "GetDigestRequestTypeDef",
    {
        "Name": str,
    },
)

GetDigestResponseResponseTypeDef = TypedDict(
    "GetDigestResponseResponseTypeDef",
    {
        "Digest": bytes,
        "DigestTipAddress": "ValueHolderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRevisionRequestTypeDef = TypedDict(
    "_RequiredGetRevisionRequestTypeDef",
    {
        "Name": str,
        "BlockAddress": "ValueHolderTypeDef",
        "DocumentId": str,
    },
)
_OptionalGetRevisionRequestTypeDef = TypedDict(
    "_OptionalGetRevisionRequestTypeDef",
    {
        "DigestTipAddress": "ValueHolderTypeDef",
    },
    total=False,
)


class GetRevisionRequestTypeDef(
    _RequiredGetRevisionRequestTypeDef, _OptionalGetRevisionRequestTypeDef
):
    pass


GetRevisionResponseResponseTypeDef = TypedDict(
    "GetRevisionResponseResponseTypeDef",
    {
        "Proof": "ValueHolderTypeDef",
        "Revision": "ValueHolderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

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

_RequiredListJournalKinesisStreamsForLedgerRequestTypeDef = TypedDict(
    "_RequiredListJournalKinesisStreamsForLedgerRequestTypeDef",
    {
        "LedgerName": str,
    },
)
_OptionalListJournalKinesisStreamsForLedgerRequestTypeDef = TypedDict(
    "_OptionalListJournalKinesisStreamsForLedgerRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListJournalKinesisStreamsForLedgerRequestTypeDef(
    _RequiredListJournalKinesisStreamsForLedgerRequestTypeDef,
    _OptionalListJournalKinesisStreamsForLedgerRequestTypeDef,
):
    pass


ListJournalKinesisStreamsForLedgerResponseResponseTypeDef = TypedDict(
    "ListJournalKinesisStreamsForLedgerResponseResponseTypeDef",
    {
        "Streams": List["JournalKinesisStreamDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListJournalS3ExportsForLedgerRequestTypeDef = TypedDict(
    "_RequiredListJournalS3ExportsForLedgerRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalListJournalS3ExportsForLedgerRequestTypeDef = TypedDict(
    "_OptionalListJournalS3ExportsForLedgerRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListJournalS3ExportsForLedgerRequestTypeDef(
    _RequiredListJournalS3ExportsForLedgerRequestTypeDef,
    _OptionalListJournalS3ExportsForLedgerRequestTypeDef,
):
    pass


ListJournalS3ExportsForLedgerResponseResponseTypeDef = TypedDict(
    "ListJournalS3ExportsForLedgerResponseResponseTypeDef",
    {
        "JournalS3Exports": List["JournalS3ExportDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJournalS3ExportsRequestTypeDef = TypedDict(
    "ListJournalS3ExportsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListJournalS3ExportsResponseResponseTypeDef = TypedDict(
    "ListJournalS3ExportsResponseResponseTypeDef",
    {
        "JournalS3Exports": List["JournalS3ExportDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLedgersRequestTypeDef = TypedDict(
    "ListLedgersRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListLedgersResponseResponseTypeDef = TypedDict(
    "ListLedgersResponseResponseTypeDef",
    {
        "Ledgers": List["LedgerSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "Tags": Dict[str, str],
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

_RequiredStreamJournalToKinesisRequestTypeDef = TypedDict(
    "_RequiredStreamJournalToKinesisRequestTypeDef",
    {
        "LedgerName": str,
        "RoleArn": str,
        "InclusiveStartTime": Union[datetime, str],
        "KinesisConfiguration": "KinesisConfigurationTypeDef",
        "StreamName": str,
    },
)
_OptionalStreamJournalToKinesisRequestTypeDef = TypedDict(
    "_OptionalStreamJournalToKinesisRequestTypeDef",
    {
        "Tags": Dict[str, str],
        "ExclusiveEndTime": Union[datetime, str],
    },
    total=False,
)


class StreamJournalToKinesisRequestTypeDef(
    _RequiredStreamJournalToKinesisRequestTypeDef, _OptionalStreamJournalToKinesisRequestTypeDef
):
    pass


StreamJournalToKinesisResponseResponseTypeDef = TypedDict(
    "StreamJournalToKinesisResponseResponseTypeDef",
    {
        "StreamId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

UpdateLedgerPermissionsModeRequestTypeDef = TypedDict(
    "UpdateLedgerPermissionsModeRequestTypeDef",
    {
        "Name": str,
        "PermissionsMode": PermissionsModeType,
    },
)

UpdateLedgerPermissionsModeResponseResponseTypeDef = TypedDict(
    "UpdateLedgerPermissionsModeResponseResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "PermissionsMode": PermissionsModeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateLedgerRequestTypeDef = TypedDict(
    "_RequiredUpdateLedgerRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateLedgerRequestTypeDef = TypedDict(
    "_OptionalUpdateLedgerRequestTypeDef",
    {
        "DeletionProtection": bool,
    },
    total=False,
)


class UpdateLedgerRequestTypeDef(
    _RequiredUpdateLedgerRequestTypeDef, _OptionalUpdateLedgerRequestTypeDef
):
    pass


UpdateLedgerResponseResponseTypeDef = TypedDict(
    "UpdateLedgerResponseResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "State": LedgerStateType,
        "CreationDateTime": datetime,
        "DeletionProtection": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ValueHolderTypeDef = TypedDict(
    "ValueHolderTypeDef",
    {
        "IonText": str,
    },
    total=False,
)
