"""
Type annotations for personalize-runtime service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize_runtime/type_defs.html)

Usage::

    ```python
    from mypy_boto3_personalize_runtime.type_defs import GetPersonalizedRankingRequestTypeDef

    data: GetPersonalizedRankingRequestTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "GetPersonalizedRankingRequestTypeDef",
    "GetPersonalizedRankingResponseResponseTypeDef",
    "GetRecommendationsRequestTypeDef",
    "GetRecommendationsResponseResponseTypeDef",
    "PredictedItemTypeDef",
    "ResponseMetadataTypeDef",
)

_RequiredGetPersonalizedRankingRequestTypeDef = TypedDict(
    "_RequiredGetPersonalizedRankingRequestTypeDef",
    {
        "campaignArn": str,
        "inputList": List[str],
        "userId": str,
    },
)
_OptionalGetPersonalizedRankingRequestTypeDef = TypedDict(
    "_OptionalGetPersonalizedRankingRequestTypeDef",
    {
        "context": Dict[str, str],
        "filterArn": str,
        "filterValues": Dict[str, str],
    },
    total=False,
)


class GetPersonalizedRankingRequestTypeDef(
    _RequiredGetPersonalizedRankingRequestTypeDef, _OptionalGetPersonalizedRankingRequestTypeDef
):
    pass


GetPersonalizedRankingResponseResponseTypeDef = TypedDict(
    "GetPersonalizedRankingResponseResponseTypeDef",
    {
        "personalizedRanking": List["PredictedItemTypeDef"],
        "recommendationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRecommendationsRequestTypeDef = TypedDict(
    "_RequiredGetRecommendationsRequestTypeDef",
    {
        "campaignArn": str,
    },
)
_OptionalGetRecommendationsRequestTypeDef = TypedDict(
    "_OptionalGetRecommendationsRequestTypeDef",
    {
        "itemId": str,
        "userId": str,
        "numResults": int,
        "context": Dict[str, str],
        "filterArn": str,
        "filterValues": Dict[str, str],
    },
    total=False,
)


class GetRecommendationsRequestTypeDef(
    _RequiredGetRecommendationsRequestTypeDef, _OptionalGetRecommendationsRequestTypeDef
):
    pass


GetRecommendationsResponseResponseTypeDef = TypedDict(
    "GetRecommendationsResponseResponseTypeDef",
    {
        "itemList": List["PredictedItemTypeDef"],
        "recommendationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PredictedItemTypeDef = TypedDict(
    "PredictedItemTypeDef",
    {
        "itemId": str,
        "score": float,
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
