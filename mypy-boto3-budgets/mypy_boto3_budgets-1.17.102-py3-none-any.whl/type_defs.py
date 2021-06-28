"""
Type annotations for budgets service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/type_defs.html)

Usage::

    ```python
    from mypy_boto3_budgets.type_defs import ActionHistoryDetailsTypeDef

    data: ActionHistoryDetailsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ActionStatusType,
    ActionSubTypeType,
    ActionTypeType,
    ApprovalModelType,
    BudgetTypeType,
    ComparisonOperatorType,
    EventTypeType,
    ExecutionTypeType,
    NotificationStateType,
    NotificationTypeType,
    SubscriptionTypeType,
    ThresholdTypeType,
    TimeUnitType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActionHistoryDetailsTypeDef",
    "ActionHistoryTypeDef",
    "ActionThresholdTypeDef",
    "ActionTypeDef",
    "BudgetPerformanceHistoryTypeDef",
    "BudgetTypeDef",
    "BudgetedAndActualAmountsTypeDef",
    "CalculatedSpendTypeDef",
    "CostTypesTypeDef",
    "CreateBudgetActionRequestTypeDef",
    "CreateBudgetActionResponseResponseTypeDef",
    "CreateBudgetRequestTypeDef",
    "CreateNotificationRequestTypeDef",
    "CreateSubscriberRequestTypeDef",
    "DefinitionTypeDef",
    "DeleteBudgetActionRequestTypeDef",
    "DeleteBudgetActionResponseResponseTypeDef",
    "DeleteBudgetRequestTypeDef",
    "DeleteNotificationRequestTypeDef",
    "DeleteSubscriberRequestTypeDef",
    "DescribeBudgetActionHistoriesRequestTypeDef",
    "DescribeBudgetActionHistoriesResponseResponseTypeDef",
    "DescribeBudgetActionRequestTypeDef",
    "DescribeBudgetActionResponseResponseTypeDef",
    "DescribeBudgetActionsForAccountRequestTypeDef",
    "DescribeBudgetActionsForAccountResponseResponseTypeDef",
    "DescribeBudgetActionsForBudgetRequestTypeDef",
    "DescribeBudgetActionsForBudgetResponseResponseTypeDef",
    "DescribeBudgetPerformanceHistoryRequestTypeDef",
    "DescribeBudgetPerformanceHistoryResponseResponseTypeDef",
    "DescribeBudgetRequestTypeDef",
    "DescribeBudgetResponseResponseTypeDef",
    "DescribeBudgetsRequestTypeDef",
    "DescribeBudgetsResponseResponseTypeDef",
    "DescribeNotificationsForBudgetRequestTypeDef",
    "DescribeNotificationsForBudgetResponseResponseTypeDef",
    "DescribeSubscribersForNotificationRequestTypeDef",
    "DescribeSubscribersForNotificationResponseResponseTypeDef",
    "ExecuteBudgetActionRequestTypeDef",
    "ExecuteBudgetActionResponseResponseTypeDef",
    "IamActionDefinitionTypeDef",
    "NotificationTypeDef",
    "NotificationWithSubscribersTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "ScpActionDefinitionTypeDef",
    "SpendTypeDef",
    "SsmActionDefinitionTypeDef",
    "SubscriberTypeDef",
    "TimePeriodTypeDef",
    "UpdateBudgetActionRequestTypeDef",
    "UpdateBudgetActionResponseResponseTypeDef",
    "UpdateBudgetRequestTypeDef",
    "UpdateNotificationRequestTypeDef",
    "UpdateSubscriberRequestTypeDef",
)

ActionHistoryDetailsTypeDef = TypedDict(
    "ActionHistoryDetailsTypeDef",
    {
        "Message": str,
        "Action": "ActionTypeDef",
    },
)

ActionHistoryTypeDef = TypedDict(
    "ActionHistoryTypeDef",
    {
        "Timestamp": datetime,
        "Status": ActionStatusType,
        "EventType": EventTypeType,
        "ActionHistoryDetails": "ActionHistoryDetailsTypeDef",
    },
)

ActionThresholdTypeDef = TypedDict(
    "ActionThresholdTypeDef",
    {
        "ActionThresholdValue": float,
        "ActionThresholdType": ThresholdTypeType,
    },
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "ActionId": str,
        "BudgetName": str,
        "NotificationType": NotificationTypeType,
        "ActionType": ActionTypeType,
        "ActionThreshold": "ActionThresholdTypeDef",
        "Definition": "DefinitionTypeDef",
        "ExecutionRoleArn": str,
        "ApprovalModel": ApprovalModelType,
        "Status": ActionStatusType,
        "Subscribers": List["SubscriberTypeDef"],
    },
)

BudgetPerformanceHistoryTypeDef = TypedDict(
    "BudgetPerformanceHistoryTypeDef",
    {
        "BudgetName": str,
        "BudgetType": BudgetTypeType,
        "CostFilters": Dict[str, List[str]],
        "CostTypes": "CostTypesTypeDef",
        "TimeUnit": TimeUnitType,
        "BudgetedAndActualAmountsList": List["BudgetedAndActualAmountsTypeDef"],
    },
    total=False,
)

_RequiredBudgetTypeDef = TypedDict(
    "_RequiredBudgetTypeDef",
    {
        "BudgetName": str,
        "TimeUnit": TimeUnitType,
        "BudgetType": BudgetTypeType,
    },
)
_OptionalBudgetTypeDef = TypedDict(
    "_OptionalBudgetTypeDef",
    {
        "BudgetLimit": "SpendTypeDef",
        "PlannedBudgetLimits": Dict[str, "SpendTypeDef"],
        "CostFilters": Dict[str, List[str]],
        "CostTypes": "CostTypesTypeDef",
        "TimePeriod": "TimePeriodTypeDef",
        "CalculatedSpend": "CalculatedSpendTypeDef",
        "LastUpdatedTime": Union[datetime, str],
    },
    total=False,
)


class BudgetTypeDef(_RequiredBudgetTypeDef, _OptionalBudgetTypeDef):
    pass


BudgetedAndActualAmountsTypeDef = TypedDict(
    "BudgetedAndActualAmountsTypeDef",
    {
        "BudgetedAmount": "SpendTypeDef",
        "ActualAmount": "SpendTypeDef",
        "TimePeriod": "TimePeriodTypeDef",
    },
    total=False,
)

_RequiredCalculatedSpendTypeDef = TypedDict(
    "_RequiredCalculatedSpendTypeDef",
    {
        "ActualSpend": "SpendTypeDef",
    },
)
_OptionalCalculatedSpendTypeDef = TypedDict(
    "_OptionalCalculatedSpendTypeDef",
    {
        "ForecastedSpend": "SpendTypeDef",
    },
    total=False,
)


class CalculatedSpendTypeDef(_RequiredCalculatedSpendTypeDef, _OptionalCalculatedSpendTypeDef):
    pass


CostTypesTypeDef = TypedDict(
    "CostTypesTypeDef",
    {
        "IncludeTax": bool,
        "IncludeSubscription": bool,
        "UseBlended": bool,
        "IncludeRefund": bool,
        "IncludeCredit": bool,
        "IncludeUpfront": bool,
        "IncludeRecurring": bool,
        "IncludeOtherSubscription": bool,
        "IncludeSupport": bool,
        "IncludeDiscount": bool,
        "UseAmortized": bool,
    },
    total=False,
)

CreateBudgetActionRequestTypeDef = TypedDict(
    "CreateBudgetActionRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "NotificationType": NotificationTypeType,
        "ActionType": ActionTypeType,
        "ActionThreshold": "ActionThresholdTypeDef",
        "Definition": "DefinitionTypeDef",
        "ExecutionRoleArn": str,
        "ApprovalModel": ApprovalModelType,
        "Subscribers": List["SubscriberTypeDef"],
    },
)

CreateBudgetActionResponseResponseTypeDef = TypedDict(
    "CreateBudgetActionResponseResponseTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBudgetRequestTypeDef = TypedDict(
    "_RequiredCreateBudgetRequestTypeDef",
    {
        "AccountId": str,
        "Budget": "BudgetTypeDef",
    },
)
_OptionalCreateBudgetRequestTypeDef = TypedDict(
    "_OptionalCreateBudgetRequestTypeDef",
    {
        "NotificationsWithSubscribers": List["NotificationWithSubscribersTypeDef"],
    },
    total=False,
)


class CreateBudgetRequestTypeDef(
    _RequiredCreateBudgetRequestTypeDef, _OptionalCreateBudgetRequestTypeDef
):
    pass


CreateNotificationRequestTypeDef = TypedDict(
    "CreateNotificationRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Notification": "NotificationTypeDef",
        "Subscribers": List["SubscriberTypeDef"],
    },
)

CreateSubscriberRequestTypeDef = TypedDict(
    "CreateSubscriberRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Notification": "NotificationTypeDef",
        "Subscriber": "SubscriberTypeDef",
    },
)

DefinitionTypeDef = TypedDict(
    "DefinitionTypeDef",
    {
        "IamActionDefinition": "IamActionDefinitionTypeDef",
        "ScpActionDefinition": "ScpActionDefinitionTypeDef",
        "SsmActionDefinition": "SsmActionDefinitionTypeDef",
    },
    total=False,
)

DeleteBudgetActionRequestTypeDef = TypedDict(
    "DeleteBudgetActionRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
    },
)

DeleteBudgetActionResponseResponseTypeDef = TypedDict(
    "DeleteBudgetActionResponseResponseTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Action": "ActionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBudgetRequestTypeDef = TypedDict(
    "DeleteBudgetRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
    },
)

DeleteNotificationRequestTypeDef = TypedDict(
    "DeleteNotificationRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Notification": "NotificationTypeDef",
    },
)

DeleteSubscriberRequestTypeDef = TypedDict(
    "DeleteSubscriberRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Notification": "NotificationTypeDef",
        "Subscriber": "SubscriberTypeDef",
    },
)

_RequiredDescribeBudgetActionHistoriesRequestTypeDef = TypedDict(
    "_RequiredDescribeBudgetActionHistoriesRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
    },
)
_OptionalDescribeBudgetActionHistoriesRequestTypeDef = TypedDict(
    "_OptionalDescribeBudgetActionHistoriesRequestTypeDef",
    {
        "TimePeriod": "TimePeriodTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeBudgetActionHistoriesRequestTypeDef(
    _RequiredDescribeBudgetActionHistoriesRequestTypeDef,
    _OptionalDescribeBudgetActionHistoriesRequestTypeDef,
):
    pass


DescribeBudgetActionHistoriesResponseResponseTypeDef = TypedDict(
    "DescribeBudgetActionHistoriesResponseResponseTypeDef",
    {
        "ActionHistories": List["ActionHistoryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBudgetActionRequestTypeDef = TypedDict(
    "DescribeBudgetActionRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
    },
)

DescribeBudgetActionResponseResponseTypeDef = TypedDict(
    "DescribeBudgetActionResponseResponseTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Action": "ActionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeBudgetActionsForAccountRequestTypeDef = TypedDict(
    "_RequiredDescribeBudgetActionsForAccountRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalDescribeBudgetActionsForAccountRequestTypeDef = TypedDict(
    "_OptionalDescribeBudgetActionsForAccountRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeBudgetActionsForAccountRequestTypeDef(
    _RequiredDescribeBudgetActionsForAccountRequestTypeDef,
    _OptionalDescribeBudgetActionsForAccountRequestTypeDef,
):
    pass


DescribeBudgetActionsForAccountResponseResponseTypeDef = TypedDict(
    "DescribeBudgetActionsForAccountResponseResponseTypeDef",
    {
        "Actions": List["ActionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeBudgetActionsForBudgetRequestTypeDef = TypedDict(
    "_RequiredDescribeBudgetActionsForBudgetRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
    },
)
_OptionalDescribeBudgetActionsForBudgetRequestTypeDef = TypedDict(
    "_OptionalDescribeBudgetActionsForBudgetRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeBudgetActionsForBudgetRequestTypeDef(
    _RequiredDescribeBudgetActionsForBudgetRequestTypeDef,
    _OptionalDescribeBudgetActionsForBudgetRequestTypeDef,
):
    pass


DescribeBudgetActionsForBudgetResponseResponseTypeDef = TypedDict(
    "DescribeBudgetActionsForBudgetResponseResponseTypeDef",
    {
        "Actions": List["ActionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeBudgetPerformanceHistoryRequestTypeDef = TypedDict(
    "_RequiredDescribeBudgetPerformanceHistoryRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
    },
)
_OptionalDescribeBudgetPerformanceHistoryRequestTypeDef = TypedDict(
    "_OptionalDescribeBudgetPerformanceHistoryRequestTypeDef",
    {
        "TimePeriod": "TimePeriodTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeBudgetPerformanceHistoryRequestTypeDef(
    _RequiredDescribeBudgetPerformanceHistoryRequestTypeDef,
    _OptionalDescribeBudgetPerformanceHistoryRequestTypeDef,
):
    pass


DescribeBudgetPerformanceHistoryResponseResponseTypeDef = TypedDict(
    "DescribeBudgetPerformanceHistoryResponseResponseTypeDef",
    {
        "BudgetPerformanceHistory": "BudgetPerformanceHistoryTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBudgetRequestTypeDef = TypedDict(
    "DescribeBudgetRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
    },
)

DescribeBudgetResponseResponseTypeDef = TypedDict(
    "DescribeBudgetResponseResponseTypeDef",
    {
        "Budget": "BudgetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeBudgetsRequestTypeDef = TypedDict(
    "_RequiredDescribeBudgetsRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalDescribeBudgetsRequestTypeDef = TypedDict(
    "_OptionalDescribeBudgetsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeBudgetsRequestTypeDef(
    _RequiredDescribeBudgetsRequestTypeDef, _OptionalDescribeBudgetsRequestTypeDef
):
    pass


DescribeBudgetsResponseResponseTypeDef = TypedDict(
    "DescribeBudgetsResponseResponseTypeDef",
    {
        "Budgets": List["BudgetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeNotificationsForBudgetRequestTypeDef = TypedDict(
    "_RequiredDescribeNotificationsForBudgetRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
    },
)
_OptionalDescribeNotificationsForBudgetRequestTypeDef = TypedDict(
    "_OptionalDescribeNotificationsForBudgetRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeNotificationsForBudgetRequestTypeDef(
    _RequiredDescribeNotificationsForBudgetRequestTypeDef,
    _OptionalDescribeNotificationsForBudgetRequestTypeDef,
):
    pass


DescribeNotificationsForBudgetResponseResponseTypeDef = TypedDict(
    "DescribeNotificationsForBudgetResponseResponseTypeDef",
    {
        "Notifications": List["NotificationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeSubscribersForNotificationRequestTypeDef = TypedDict(
    "_RequiredDescribeSubscribersForNotificationRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Notification": "NotificationTypeDef",
    },
)
_OptionalDescribeSubscribersForNotificationRequestTypeDef = TypedDict(
    "_OptionalDescribeSubscribersForNotificationRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeSubscribersForNotificationRequestTypeDef(
    _RequiredDescribeSubscribersForNotificationRequestTypeDef,
    _OptionalDescribeSubscribersForNotificationRequestTypeDef,
):
    pass


DescribeSubscribersForNotificationResponseResponseTypeDef = TypedDict(
    "DescribeSubscribersForNotificationResponseResponseTypeDef",
    {
        "Subscribers": List["SubscriberTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExecuteBudgetActionRequestTypeDef = TypedDict(
    "ExecuteBudgetActionRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
        "ExecutionType": ExecutionTypeType,
    },
)

ExecuteBudgetActionResponseResponseTypeDef = TypedDict(
    "ExecuteBudgetActionResponseResponseTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
        "ExecutionType": ExecutionTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredIamActionDefinitionTypeDef = TypedDict(
    "_RequiredIamActionDefinitionTypeDef",
    {
        "PolicyArn": str,
    },
)
_OptionalIamActionDefinitionTypeDef = TypedDict(
    "_OptionalIamActionDefinitionTypeDef",
    {
        "Roles": List[str],
        "Groups": List[str],
        "Users": List[str],
    },
    total=False,
)


class IamActionDefinitionTypeDef(
    _RequiredIamActionDefinitionTypeDef, _OptionalIamActionDefinitionTypeDef
):
    pass


_RequiredNotificationTypeDef = TypedDict(
    "_RequiredNotificationTypeDef",
    {
        "NotificationType": NotificationTypeType,
        "ComparisonOperator": ComparisonOperatorType,
        "Threshold": float,
    },
)
_OptionalNotificationTypeDef = TypedDict(
    "_OptionalNotificationTypeDef",
    {
        "ThresholdType": ThresholdTypeType,
        "NotificationState": NotificationStateType,
    },
    total=False,
)


class NotificationTypeDef(_RequiredNotificationTypeDef, _OptionalNotificationTypeDef):
    pass


NotificationWithSubscribersTypeDef = TypedDict(
    "NotificationWithSubscribersTypeDef",
    {
        "Notification": "NotificationTypeDef",
        "Subscribers": List["SubscriberTypeDef"],
    },
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

ScpActionDefinitionTypeDef = TypedDict(
    "ScpActionDefinitionTypeDef",
    {
        "PolicyId": str,
        "TargetIds": List[str],
    },
)

SpendTypeDef = TypedDict(
    "SpendTypeDef",
    {
        "Amount": str,
        "Unit": str,
    },
)

SsmActionDefinitionTypeDef = TypedDict(
    "SsmActionDefinitionTypeDef",
    {
        "ActionSubType": ActionSubTypeType,
        "Region": str,
        "InstanceIds": List[str],
    },
)

SubscriberTypeDef = TypedDict(
    "SubscriberTypeDef",
    {
        "SubscriptionType": SubscriptionTypeType,
        "Address": str,
    },
)

TimePeriodTypeDef = TypedDict(
    "TimePeriodTypeDef",
    {
        "Start": Union[datetime, str],
        "End": Union[datetime, str],
    },
    total=False,
)

_RequiredUpdateBudgetActionRequestTypeDef = TypedDict(
    "_RequiredUpdateBudgetActionRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
    },
)
_OptionalUpdateBudgetActionRequestTypeDef = TypedDict(
    "_OptionalUpdateBudgetActionRequestTypeDef",
    {
        "NotificationType": NotificationTypeType,
        "ActionThreshold": "ActionThresholdTypeDef",
        "Definition": "DefinitionTypeDef",
        "ExecutionRoleArn": str,
        "ApprovalModel": ApprovalModelType,
        "Subscribers": List["SubscriberTypeDef"],
    },
    total=False,
)


class UpdateBudgetActionRequestTypeDef(
    _RequiredUpdateBudgetActionRequestTypeDef, _OptionalUpdateBudgetActionRequestTypeDef
):
    pass


UpdateBudgetActionResponseResponseTypeDef = TypedDict(
    "UpdateBudgetActionResponseResponseTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "OldAction": "ActionTypeDef",
        "NewAction": "ActionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBudgetRequestTypeDef = TypedDict(
    "UpdateBudgetRequestTypeDef",
    {
        "AccountId": str,
        "NewBudget": "BudgetTypeDef",
    },
)

UpdateNotificationRequestTypeDef = TypedDict(
    "UpdateNotificationRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "OldNotification": "NotificationTypeDef",
        "NewNotification": "NotificationTypeDef",
    },
)

UpdateSubscriberRequestTypeDef = TypedDict(
    "UpdateSubscriberRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Notification": "NotificationTypeDef",
        "OldSubscriber": "SubscriberTypeDef",
        "NewSubscriber": "SubscriberTypeDef",
    },
)
