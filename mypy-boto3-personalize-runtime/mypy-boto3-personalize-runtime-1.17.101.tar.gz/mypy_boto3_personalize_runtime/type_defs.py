"""
Type annotations for personalize-runtime service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize_runtime/type_defs.html)

Usage::

    ```python
    from mypy_boto3_personalize_runtime.type_defs import GetPersonalizedRankingResponseTypeDef

    data: GetPersonalizedRankingResponseTypeDef = {...}
    ```
"""
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "GetPersonalizedRankingResponseTypeDef",
    "GetRecommendationsResponseTypeDef",
    "PredictedItemTypeDef",
)

GetPersonalizedRankingResponseTypeDef = TypedDict(
    "GetPersonalizedRankingResponseTypeDef",
    {
        "personalizedRanking": List["PredictedItemTypeDef"],
        "recommendationId": str,
    },
    total=False,
)

GetRecommendationsResponseTypeDef = TypedDict(
    "GetRecommendationsResponseTypeDef",
    {
        "itemList": List["PredictedItemTypeDef"],
        "recommendationId": str,
    },
    total=False,
)

PredictedItemTypeDef = TypedDict(
    "PredictedItemTypeDef",
    {
        "itemId": str,
        "score": float,
    },
    total=False,
)
