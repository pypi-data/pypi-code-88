"""
Type annotations for health service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_health/type_defs.html)

Usage::

    ```python
    from mypy_boto3_health.type_defs import AffectedEntityTypeDef

    data: AffectedEntityTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    entityStatusCodeType,
    eventScopeCodeType,
    eventStatusCodeType,
    eventTypeCategoryType,
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
    "AffectedEntityTypeDef",
    "DateTimeRangeTypeDef",
    "DescribeAffectedAccountsForOrganizationRequestTypeDef",
    "DescribeAffectedAccountsForOrganizationResponseResponseTypeDef",
    "DescribeAffectedEntitiesForOrganizationRequestTypeDef",
    "DescribeAffectedEntitiesForOrganizationResponseResponseTypeDef",
    "DescribeAffectedEntitiesRequestTypeDef",
    "DescribeAffectedEntitiesResponseResponseTypeDef",
    "DescribeEntityAggregatesRequestTypeDef",
    "DescribeEntityAggregatesResponseResponseTypeDef",
    "DescribeEventAggregatesRequestTypeDef",
    "DescribeEventAggregatesResponseResponseTypeDef",
    "DescribeEventDetailsForOrganizationRequestTypeDef",
    "DescribeEventDetailsForOrganizationResponseResponseTypeDef",
    "DescribeEventDetailsRequestTypeDef",
    "DescribeEventDetailsResponseResponseTypeDef",
    "DescribeEventTypesRequestTypeDef",
    "DescribeEventTypesResponseResponseTypeDef",
    "DescribeEventsForOrganizationRequestTypeDef",
    "DescribeEventsForOrganizationResponseResponseTypeDef",
    "DescribeEventsRequestTypeDef",
    "DescribeEventsResponseResponseTypeDef",
    "DescribeHealthServiceStatusForOrganizationResponseResponseTypeDef",
    "EntityAggregateTypeDef",
    "EntityFilterTypeDef",
    "EventAccountFilterTypeDef",
    "EventAggregateTypeDef",
    "EventDescriptionTypeDef",
    "EventDetailsErrorItemTypeDef",
    "EventDetailsTypeDef",
    "EventFilterTypeDef",
    "EventTypeDef",
    "EventTypeFilterTypeDef",
    "EventTypeTypeDef",
    "OrganizationAffectedEntitiesErrorItemTypeDef",
    "OrganizationEventDetailsErrorItemTypeDef",
    "OrganizationEventDetailsTypeDef",
    "OrganizationEventFilterTypeDef",
    "OrganizationEventTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
)

AffectedEntityTypeDef = TypedDict(
    "AffectedEntityTypeDef",
    {
        "entityArn": str,
        "eventArn": str,
        "entityValue": str,
        "entityUrl": str,
        "awsAccountId": str,
        "lastUpdatedTime": datetime,
        "statusCode": entityStatusCodeType,
        "tags": Dict[str, str],
    },
    total=False,
)

DateTimeRangeTypeDef = TypedDict(
    "DateTimeRangeTypeDef",
    {
        "from": Union[datetime, str],
        "to": Union[datetime, str],
    },
    total=False,
)

_RequiredDescribeAffectedAccountsForOrganizationRequestTypeDef = TypedDict(
    "_RequiredDescribeAffectedAccountsForOrganizationRequestTypeDef",
    {
        "eventArn": str,
    },
)
_OptionalDescribeAffectedAccountsForOrganizationRequestTypeDef = TypedDict(
    "_OptionalDescribeAffectedAccountsForOrganizationRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class DescribeAffectedAccountsForOrganizationRequestTypeDef(
    _RequiredDescribeAffectedAccountsForOrganizationRequestTypeDef,
    _OptionalDescribeAffectedAccountsForOrganizationRequestTypeDef,
):
    pass


DescribeAffectedAccountsForOrganizationResponseResponseTypeDef = TypedDict(
    "DescribeAffectedAccountsForOrganizationResponseResponseTypeDef",
    {
        "affectedAccounts": List[str],
        "eventScopeCode": eventScopeCodeType,
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeAffectedEntitiesForOrganizationRequestTypeDef = TypedDict(
    "_RequiredDescribeAffectedEntitiesForOrganizationRequestTypeDef",
    {
        "organizationEntityFilters": List["EventAccountFilterTypeDef"],
    },
)
_OptionalDescribeAffectedEntitiesForOrganizationRequestTypeDef = TypedDict(
    "_OptionalDescribeAffectedEntitiesForOrganizationRequestTypeDef",
    {
        "locale": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class DescribeAffectedEntitiesForOrganizationRequestTypeDef(
    _RequiredDescribeAffectedEntitiesForOrganizationRequestTypeDef,
    _OptionalDescribeAffectedEntitiesForOrganizationRequestTypeDef,
):
    pass


DescribeAffectedEntitiesForOrganizationResponseResponseTypeDef = TypedDict(
    "DescribeAffectedEntitiesForOrganizationResponseResponseTypeDef",
    {
        "entities": List["AffectedEntityTypeDef"],
        "failedSet": List["OrganizationAffectedEntitiesErrorItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeAffectedEntitiesRequestTypeDef = TypedDict(
    "_RequiredDescribeAffectedEntitiesRequestTypeDef",
    {
        "filter": "EntityFilterTypeDef",
    },
)
_OptionalDescribeAffectedEntitiesRequestTypeDef = TypedDict(
    "_OptionalDescribeAffectedEntitiesRequestTypeDef",
    {
        "locale": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class DescribeAffectedEntitiesRequestTypeDef(
    _RequiredDescribeAffectedEntitiesRequestTypeDef, _OptionalDescribeAffectedEntitiesRequestTypeDef
):
    pass


DescribeAffectedEntitiesResponseResponseTypeDef = TypedDict(
    "DescribeAffectedEntitiesResponseResponseTypeDef",
    {
        "entities": List["AffectedEntityTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEntityAggregatesRequestTypeDef = TypedDict(
    "DescribeEntityAggregatesRequestTypeDef",
    {
        "eventArns": List[str],
    },
    total=False,
)

DescribeEntityAggregatesResponseResponseTypeDef = TypedDict(
    "DescribeEntityAggregatesResponseResponseTypeDef",
    {
        "entityAggregates": List["EntityAggregateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeEventAggregatesRequestTypeDef = TypedDict(
    "_RequiredDescribeEventAggregatesRequestTypeDef",
    {
        "aggregateField": Literal["eventTypeCategory"],
    },
)
_OptionalDescribeEventAggregatesRequestTypeDef = TypedDict(
    "_OptionalDescribeEventAggregatesRequestTypeDef",
    {
        "filter": "EventFilterTypeDef",
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class DescribeEventAggregatesRequestTypeDef(
    _RequiredDescribeEventAggregatesRequestTypeDef, _OptionalDescribeEventAggregatesRequestTypeDef
):
    pass


DescribeEventAggregatesResponseResponseTypeDef = TypedDict(
    "DescribeEventAggregatesResponseResponseTypeDef",
    {
        "eventAggregates": List["EventAggregateTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeEventDetailsForOrganizationRequestTypeDef = TypedDict(
    "_RequiredDescribeEventDetailsForOrganizationRequestTypeDef",
    {
        "organizationEventDetailFilters": List["EventAccountFilterTypeDef"],
    },
)
_OptionalDescribeEventDetailsForOrganizationRequestTypeDef = TypedDict(
    "_OptionalDescribeEventDetailsForOrganizationRequestTypeDef",
    {
        "locale": str,
    },
    total=False,
)


class DescribeEventDetailsForOrganizationRequestTypeDef(
    _RequiredDescribeEventDetailsForOrganizationRequestTypeDef,
    _OptionalDescribeEventDetailsForOrganizationRequestTypeDef,
):
    pass


DescribeEventDetailsForOrganizationResponseResponseTypeDef = TypedDict(
    "DescribeEventDetailsForOrganizationResponseResponseTypeDef",
    {
        "successfulSet": List["OrganizationEventDetailsTypeDef"],
        "failedSet": List["OrganizationEventDetailsErrorItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeEventDetailsRequestTypeDef = TypedDict(
    "_RequiredDescribeEventDetailsRequestTypeDef",
    {
        "eventArns": List[str],
    },
)
_OptionalDescribeEventDetailsRequestTypeDef = TypedDict(
    "_OptionalDescribeEventDetailsRequestTypeDef",
    {
        "locale": str,
    },
    total=False,
)


class DescribeEventDetailsRequestTypeDef(
    _RequiredDescribeEventDetailsRequestTypeDef, _OptionalDescribeEventDetailsRequestTypeDef
):
    pass


DescribeEventDetailsResponseResponseTypeDef = TypedDict(
    "DescribeEventDetailsResponseResponseTypeDef",
    {
        "successfulSet": List["EventDetailsTypeDef"],
        "failedSet": List["EventDetailsErrorItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventTypesRequestTypeDef = TypedDict(
    "DescribeEventTypesRequestTypeDef",
    {
        "filter": "EventTypeFilterTypeDef",
        "locale": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

DescribeEventTypesResponseResponseTypeDef = TypedDict(
    "DescribeEventTypesResponseResponseTypeDef",
    {
        "eventTypes": List["EventTypeTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventsForOrganizationRequestTypeDef = TypedDict(
    "DescribeEventsForOrganizationRequestTypeDef",
    {
        "filter": "OrganizationEventFilterTypeDef",
        "nextToken": str,
        "maxResults": int,
        "locale": str,
    },
    total=False,
)

DescribeEventsForOrganizationResponseResponseTypeDef = TypedDict(
    "DescribeEventsForOrganizationResponseResponseTypeDef",
    {
        "events": List["OrganizationEventTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventsRequestTypeDef = TypedDict(
    "DescribeEventsRequestTypeDef",
    {
        "filter": "EventFilterTypeDef",
        "nextToken": str,
        "maxResults": int,
        "locale": str,
    },
    total=False,
)

DescribeEventsResponseResponseTypeDef = TypedDict(
    "DescribeEventsResponseResponseTypeDef",
    {
        "events": List["EventTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHealthServiceStatusForOrganizationResponseResponseTypeDef = TypedDict(
    "DescribeHealthServiceStatusForOrganizationResponseResponseTypeDef",
    {
        "healthServiceAccessStatusForOrganization": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EntityAggregateTypeDef = TypedDict(
    "EntityAggregateTypeDef",
    {
        "eventArn": str,
        "count": int,
    },
    total=False,
)

_RequiredEntityFilterTypeDef = TypedDict(
    "_RequiredEntityFilterTypeDef",
    {
        "eventArns": List[str],
    },
)
_OptionalEntityFilterTypeDef = TypedDict(
    "_OptionalEntityFilterTypeDef",
    {
        "entityArns": List[str],
        "entityValues": List[str],
        "lastUpdatedTimes": List["DateTimeRangeTypeDef"],
        "tags": List[Dict[str, str]],
        "statusCodes": List[entityStatusCodeType],
    },
    total=False,
)


class EntityFilterTypeDef(_RequiredEntityFilterTypeDef, _OptionalEntityFilterTypeDef):
    pass


_RequiredEventAccountFilterTypeDef = TypedDict(
    "_RequiredEventAccountFilterTypeDef",
    {
        "eventArn": str,
    },
)
_OptionalEventAccountFilterTypeDef = TypedDict(
    "_OptionalEventAccountFilterTypeDef",
    {
        "awsAccountId": str,
    },
    total=False,
)


class EventAccountFilterTypeDef(
    _RequiredEventAccountFilterTypeDef, _OptionalEventAccountFilterTypeDef
):
    pass


EventAggregateTypeDef = TypedDict(
    "EventAggregateTypeDef",
    {
        "aggregateValue": str,
        "count": int,
    },
    total=False,
)

EventDescriptionTypeDef = TypedDict(
    "EventDescriptionTypeDef",
    {
        "latestDescription": str,
    },
    total=False,
)

EventDetailsErrorItemTypeDef = TypedDict(
    "EventDetailsErrorItemTypeDef",
    {
        "eventArn": str,
        "errorName": str,
        "errorMessage": str,
    },
    total=False,
)

EventDetailsTypeDef = TypedDict(
    "EventDetailsTypeDef",
    {
        "event": "EventTypeDef",
        "eventDescription": "EventDescriptionTypeDef",
        "eventMetadata": Dict[str, str],
    },
    total=False,
)

EventFilterTypeDef = TypedDict(
    "EventFilterTypeDef",
    {
        "eventArns": List[str],
        "eventTypeCodes": List[str],
        "services": List[str],
        "regions": List[str],
        "availabilityZones": List[str],
        "startTimes": List["DateTimeRangeTypeDef"],
        "endTimes": List["DateTimeRangeTypeDef"],
        "lastUpdatedTimes": List["DateTimeRangeTypeDef"],
        "entityArns": List[str],
        "entityValues": List[str],
        "eventTypeCategories": List[eventTypeCategoryType],
        "tags": List[Dict[str, str]],
        "eventStatusCodes": List[eventStatusCodeType],
    },
    total=False,
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "arn": str,
        "service": str,
        "eventTypeCode": str,
        "eventTypeCategory": eventTypeCategoryType,
        "region": str,
        "availabilityZone": str,
        "startTime": datetime,
        "endTime": datetime,
        "lastUpdatedTime": datetime,
        "statusCode": eventStatusCodeType,
        "eventScopeCode": eventScopeCodeType,
    },
    total=False,
)

EventTypeFilterTypeDef = TypedDict(
    "EventTypeFilterTypeDef",
    {
        "eventTypeCodes": List[str],
        "services": List[str],
        "eventTypeCategories": List[eventTypeCategoryType],
    },
    total=False,
)

EventTypeTypeDef = TypedDict(
    "EventTypeTypeDef",
    {
        "service": str,
        "code": str,
        "category": eventTypeCategoryType,
    },
    total=False,
)

OrganizationAffectedEntitiesErrorItemTypeDef = TypedDict(
    "OrganizationAffectedEntitiesErrorItemTypeDef",
    {
        "awsAccountId": str,
        "eventArn": str,
        "errorName": str,
        "errorMessage": str,
    },
    total=False,
)

OrganizationEventDetailsErrorItemTypeDef = TypedDict(
    "OrganizationEventDetailsErrorItemTypeDef",
    {
        "awsAccountId": str,
        "eventArn": str,
        "errorName": str,
        "errorMessage": str,
    },
    total=False,
)

OrganizationEventDetailsTypeDef = TypedDict(
    "OrganizationEventDetailsTypeDef",
    {
        "awsAccountId": str,
        "event": "EventTypeDef",
        "eventDescription": "EventDescriptionTypeDef",
        "eventMetadata": Dict[str, str],
    },
    total=False,
)

OrganizationEventFilterTypeDef = TypedDict(
    "OrganizationEventFilterTypeDef",
    {
        "eventTypeCodes": List[str],
        "awsAccountIds": List[str],
        "services": List[str],
        "regions": List[str],
        "startTime": "DateTimeRangeTypeDef",
        "endTime": "DateTimeRangeTypeDef",
        "lastUpdatedTime": "DateTimeRangeTypeDef",
        "entityArns": List[str],
        "entityValues": List[str],
        "eventTypeCategories": List[eventTypeCategoryType],
        "eventStatusCodes": List[eventStatusCodeType],
    },
    total=False,
)

OrganizationEventTypeDef = TypedDict(
    "OrganizationEventTypeDef",
    {
        "arn": str,
        "service": str,
        "eventTypeCode": str,
        "eventTypeCategory": eventTypeCategoryType,
        "eventScopeCode": eventScopeCodeType,
        "region": str,
        "startTime": datetime,
        "endTime": datetime,
        "lastUpdatedTime": datetime,
        "statusCode": eventStatusCodeType,
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
