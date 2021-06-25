"""
Type annotations for macie service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie/type_defs.html)

Usage::

    ```python
    from mypy_boto3_macie.type_defs import AssociateS3ResourcesResultTypeDef

    data: AssociateS3ResourcesResultTypeDef = {...}
    ```
"""
import sys
from typing import List

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
    "AssociateS3ResourcesResultTypeDef",
    "ClassificationTypeTypeDef",
    "ClassificationTypeUpdateTypeDef",
    "DisassociateS3ResourcesResultTypeDef",
    "FailedS3ResourceTypeDef",
    "ListMemberAccountsResultTypeDef",
    "ListS3ResourcesResultTypeDef",
    "MemberAccountTypeDef",
    "PaginatorConfigTypeDef",
    "S3ResourceClassificationTypeDef",
    "S3ResourceClassificationUpdateTypeDef",
    "S3ResourceTypeDef",
    "UpdateS3ResourcesResultTypeDef",
)

AssociateS3ResourcesResultTypeDef = TypedDict(
    "AssociateS3ResourcesResultTypeDef",
    {
        "failedS3Resources": List["FailedS3ResourceTypeDef"],
    },
    total=False,
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

DisassociateS3ResourcesResultTypeDef = TypedDict(
    "DisassociateS3ResourcesResultTypeDef",
    {
        "failedS3Resources": List["FailedS3ResourceTypeDef"],
    },
    total=False,
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

ListMemberAccountsResultTypeDef = TypedDict(
    "ListMemberAccountsResultTypeDef",
    {
        "memberAccounts": List["MemberAccountTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListS3ResourcesResultTypeDef = TypedDict(
    "ListS3ResourcesResultTypeDef",
    {
        "s3Resources": List["S3ResourceClassificationTypeDef"],
        "nextToken": str,
    },
    total=False,
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


UpdateS3ResourcesResultTypeDef = TypedDict(
    "UpdateS3ResourcesResultTypeDef",
    {
        "failedS3Resources": List["FailedS3ResourceTypeDef"],
    },
    total=False,
)
