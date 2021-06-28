"""
Type annotations for cloudsearchdomain service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloudsearchdomain.type_defs import BucketInfoTypeDef

    data: BucketInfoTypeDef = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import ContentTypeType, QueryParserType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BucketInfoTypeDef",
    "BucketTypeDef",
    "DocumentServiceWarningTypeDef",
    "FieldStatsTypeDef",
    "HitTypeDef",
    "HitsTypeDef",
    "ResponseMetadataTypeDef",
    "SearchRequestTypeDef",
    "SearchResponseResponseTypeDef",
    "SearchStatusTypeDef",
    "SuggestModelTypeDef",
    "SuggestRequestTypeDef",
    "SuggestResponseResponseTypeDef",
    "SuggestStatusTypeDef",
    "SuggestionMatchTypeDef",
    "UploadDocumentsRequestTypeDef",
    "UploadDocumentsResponseResponseTypeDef",
)

BucketInfoTypeDef = TypedDict(
    "BucketInfoTypeDef",
    {
        "buckets": List["BucketTypeDef"],
    },
    total=False,
)

BucketTypeDef = TypedDict(
    "BucketTypeDef",
    {
        "value": str,
        "count": int,
    },
    total=False,
)

DocumentServiceWarningTypeDef = TypedDict(
    "DocumentServiceWarningTypeDef",
    {
        "message": str,
    },
    total=False,
)

FieldStatsTypeDef = TypedDict(
    "FieldStatsTypeDef",
    {
        "min": str,
        "max": str,
        "count": int,
        "missing": int,
        "sum": float,
        "sumOfSquares": float,
        "mean": str,
        "stddev": float,
    },
    total=False,
)

HitTypeDef = TypedDict(
    "HitTypeDef",
    {
        "id": str,
        "fields": Dict[str, List[str]],
        "exprs": Dict[str, str],
        "highlights": Dict[str, str],
    },
    total=False,
)

HitsTypeDef = TypedDict(
    "HitsTypeDef",
    {
        "found": int,
        "start": int,
        "cursor": str,
        "hit": List["HitTypeDef"],
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

_RequiredSearchRequestTypeDef = TypedDict(
    "_RequiredSearchRequestTypeDef",
    {
        "query": str,
    },
)
_OptionalSearchRequestTypeDef = TypedDict(
    "_OptionalSearchRequestTypeDef",
    {
        "cursor": str,
        "expr": str,
        "facet": str,
        "filterQuery": str,
        "highlight": str,
        "partial": bool,
        "queryOptions": str,
        "queryParser": QueryParserType,
        "returnFields": str,
        "size": int,
        "sort": str,
        "start": int,
        "stats": str,
    },
    total=False,
)


class SearchRequestTypeDef(_RequiredSearchRequestTypeDef, _OptionalSearchRequestTypeDef):
    pass


SearchResponseResponseTypeDef = TypedDict(
    "SearchResponseResponseTypeDef",
    {
        "status": "SearchStatusTypeDef",
        "hits": "HitsTypeDef",
        "facets": Dict[str, "BucketInfoTypeDef"],
        "stats": Dict[str, "FieldStatsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchStatusTypeDef = TypedDict(
    "SearchStatusTypeDef",
    {
        "timems": int,
        "rid": str,
    },
    total=False,
)

SuggestModelTypeDef = TypedDict(
    "SuggestModelTypeDef",
    {
        "query": str,
        "found": int,
        "suggestions": List["SuggestionMatchTypeDef"],
    },
    total=False,
)

_RequiredSuggestRequestTypeDef = TypedDict(
    "_RequiredSuggestRequestTypeDef",
    {
        "query": str,
        "suggester": str,
    },
)
_OptionalSuggestRequestTypeDef = TypedDict(
    "_OptionalSuggestRequestTypeDef",
    {
        "size": int,
    },
    total=False,
)


class SuggestRequestTypeDef(_RequiredSuggestRequestTypeDef, _OptionalSuggestRequestTypeDef):
    pass


SuggestResponseResponseTypeDef = TypedDict(
    "SuggestResponseResponseTypeDef",
    {
        "status": "SuggestStatusTypeDef",
        "suggest": "SuggestModelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SuggestStatusTypeDef = TypedDict(
    "SuggestStatusTypeDef",
    {
        "timems": int,
        "rid": str,
    },
    total=False,
)

SuggestionMatchTypeDef = TypedDict(
    "SuggestionMatchTypeDef",
    {
        "suggestion": str,
        "score": int,
        "id": str,
    },
    total=False,
)

UploadDocumentsRequestTypeDef = TypedDict(
    "UploadDocumentsRequestTypeDef",
    {
        "documents": Union[bytes, IO[bytes], StreamingBody],
        "contentType": ContentTypeType,
    },
)

UploadDocumentsResponseResponseTypeDef = TypedDict(
    "UploadDocumentsResponseResponseTypeDef",
    {
        "status": str,
        "adds": int,
        "deletes": int,
        "warnings": List["DocumentServiceWarningTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
