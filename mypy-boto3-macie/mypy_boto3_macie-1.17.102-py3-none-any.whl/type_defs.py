"""
Type annotations for macie service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie/type_defs.html)

Usage::

    ```python
    from mypy_boto3_macie.type_defs import AssociateMemberAccountRequestTypeDef

    data: AssociateMemberAccountRequestTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import S3OneTimeClassificationTypeType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssociateMemberAccountRequestTypeDef",
    "AssociateS3ResourcesRequestTypeDef",
    "AssociateS3ResourcesResultResponseTypeDef",
    "ClassificationTypeTypeDef",
    "ClassificationTypeUpdateTypeDef",
    "DisassociateMemberAccountRequestTypeDef",
    "DisassociateS3ResourcesRequestTypeDef",
    "DisassociateS3ResourcesResultResponseTypeDef",
    "FailedS3ResourceTypeDef",
    "ListMemberAccountsRequestTypeDef",
    "ListMemberAccountsResultResponseTypeDef",
    "ListS3ResourcesRequestTypeDef",
    "ListS3ResourcesResultResponseTypeDef",
    "MemberAccountTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "S3ResourceClassificationTypeDef",
    "S3ResourceClassificationUpdateTypeDef",
    "S3ResourceTypeDef",
    "UpdateS3ResourcesRequestTypeDef",
    "UpdateS3ResourcesResultResponseTypeDef",
)

AssociateMemberAccountRequestTypeDef = TypedDict(
    "AssociateMemberAccountRequestTypeDef",
    {
        "memberAccountId": str,
    },
)

_RequiredAssociateS3ResourcesRequestTypeDef = TypedDict(
    "_RequiredAssociateS3ResourcesRequestTypeDef",
    {
        "s3Resources": List["S3ResourceClassificationTypeDef"],
    },
)
_OptionalAssociateS3ResourcesRequestTypeDef = TypedDict(
    "_OptionalAssociateS3ResourcesRequestTypeDef",
    {
        "memberAccountId": str,
    },
    total=False,
)


class AssociateS3ResourcesRequestTypeDef(
    _RequiredAssociateS3ResourcesRequestTypeDef, _OptionalAssociateS3ResourcesRequestTypeDef
):
    pass


AssociateS3ResourcesResultResponseTypeDef = TypedDict(
    "AssociateS3ResourcesResultResponseTypeDef",
    {
        "failedS3Resources": List["FailedS3ResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ClassificationTypeTypeDef = TypedDict(
    "ClassificationTypeTypeDef",
    {
        "oneTime": S3OneTimeClassificationTypeType,
        "continuous": Literal["FULL"],
    },
)

ClassificationTypeUpdateTypeDef = TypedDict(
    "ClassificationTypeUpdateTypeDef",
    {
        "oneTime": S3OneTimeClassificationTypeType,
        "continuous": Literal["FULL"],
    },
    total=False,
)

DisassociateMemberAccountRequestTypeDef = TypedDict(
    "DisassociateMemberAccountRequestTypeDef",
    {
        "memberAccountId": str,
    },
)

_RequiredDisassociateS3ResourcesRequestTypeDef = TypedDict(
    "_RequiredDisassociateS3ResourcesRequestTypeDef",
    {
        "associatedS3Resources": List["S3ResourceTypeDef"],
    },
)
_OptionalDisassociateS3ResourcesRequestTypeDef = TypedDict(
    "_OptionalDisassociateS3ResourcesRequestTypeDef",
    {
        "memberAccountId": str,
    },
    total=False,
)


class DisassociateS3ResourcesRequestTypeDef(
    _RequiredDisassociateS3ResourcesRequestTypeDef, _OptionalDisassociateS3ResourcesRequestTypeDef
):
    pass


DisassociateS3ResourcesResultResponseTypeDef = TypedDict(
    "DisassociateS3ResourcesResultResponseTypeDef",
    {
        "failedS3Resources": List["FailedS3ResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FailedS3ResourceTypeDef = TypedDict(
    "FailedS3ResourceTypeDef",
    {
        "failedItem": "S3ResourceTypeDef",
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)

ListMemberAccountsRequestTypeDef = TypedDict(
    "ListMemberAccountsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListMemberAccountsResultResponseTypeDef = TypedDict(
    "ListMemberAccountsResultResponseTypeDef",
    {
        "memberAccounts": List["MemberAccountTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListS3ResourcesRequestTypeDef = TypedDict(
    "ListS3ResourcesRequestTypeDef",
    {
        "memberAccountId": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListS3ResourcesResultResponseTypeDef = TypedDict(
    "ListS3ResourcesResultResponseTypeDef",
    {
        "s3Resources": List["S3ResourceClassificationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MemberAccountTypeDef = TypedDict(
    "MemberAccountTypeDef",
    {
        "accountId": str,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
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

_RequiredS3ResourceClassificationTypeDef = TypedDict(
    "_RequiredS3ResourceClassificationTypeDef",
    {
        "bucketName": str,
        "classificationType": "ClassificationTypeTypeDef",
    },
)
_OptionalS3ResourceClassificationTypeDef = TypedDict(
    "_OptionalS3ResourceClassificationTypeDef",
    {
        "prefix": str,
    },
    total=False,
)


class S3ResourceClassificationTypeDef(
    _RequiredS3ResourceClassificationTypeDef, _OptionalS3ResourceClassificationTypeDef
):
    pass


_RequiredS3ResourceClassificationUpdateTypeDef = TypedDict(
    "_RequiredS3ResourceClassificationUpdateTypeDef",
    {
        "bucketName": str,
        "classificationTypeUpdate": "ClassificationTypeUpdateTypeDef",
    },
)
_OptionalS3ResourceClassificationUpdateTypeDef = TypedDict(
    "_OptionalS3ResourceClassificationUpdateTypeDef",
    {
        "prefix": str,
    },
    total=False,
)


class S3ResourceClassificationUpdateTypeDef(
    _RequiredS3ResourceClassificationUpdateTypeDef, _OptionalS3ResourceClassificationUpdateTypeDef
):
    pass


_RequiredS3ResourceTypeDef = TypedDict(
    "_RequiredS3ResourceTypeDef",
    {
        "bucketName": str,
    },
)
_OptionalS3ResourceTypeDef = TypedDict(
    "_OptionalS3ResourceTypeDef",
    {
        "prefix": str,
    },
    total=False,
)


class S3ResourceTypeDef(_RequiredS3ResourceTypeDef, _OptionalS3ResourceTypeDef):
    pass


_RequiredUpdateS3ResourcesRequestTypeDef = TypedDict(
    "_RequiredUpdateS3ResourcesRequestTypeDef",
    {
        "s3ResourcesUpdate": List["S3ResourceClassificationUpdateTypeDef"],
    },
)
_OptionalUpdateS3ResourcesRequestTypeDef = TypedDict(
    "_OptionalUpdateS3ResourcesRequestTypeDef",
    {
        "memberAccountId": str,
    },
    total=False,
)


class UpdateS3ResourcesRequestTypeDef(
    _RequiredUpdateS3ResourcesRequestTypeDef, _OptionalUpdateS3ResourcesRequestTypeDef
):
    pass


UpdateS3ResourcesResultResponseTypeDef = TypedDict(
    "UpdateS3ResourcesResultResponseTypeDef",
    {
        "failedS3Resources": List["FailedS3ResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
