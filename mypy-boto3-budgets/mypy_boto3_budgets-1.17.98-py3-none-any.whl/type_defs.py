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
from typing import Dict, List

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
    "CreateBudgetActionResponseTypeDef",
    "DefinitionTypeDef",
    "DeleteBudgetActionResponseTypeDef",
    "DescribeBudgetActionHistoriesResponseTypeDef",
    "DescribeBudgetActionResponseTypeDef",
    "DescribeBudgetActionsForAccountResponseTypeDef",
    "DescribeBudgetActionsForBudgetResponseTypeDef",
    "DescribeBudgetPerformanceHistoryResponseTypeDef",
    "DescribeBudgetResponseTypeDef",
    "DescribeBudgetsResponseTypeDef",
    "DescribeNotificationsForBudgetResponseTypeDef",
    "DescribeSubscribersForNotificationResponseTypeDef",
    "ExecuteBudgetActionResponseTypeDef",
    "IamActionDefinitionTypeDef",
    "NotificationTypeDef",
    "NotificationWithSubscribersTypeDef",
    "PaginatorConfigTypeDef",
    "ScpActionDefinitionTypeDef",
    "SpendTypeDef",
    "SsmActionDefinitionTypeDef",
    "SubscriberTypeDef",
    "TimePeriodTypeDef",
    "UpdateBudgetActionResponseTypeDef",
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
        "LastUpdatedTime": datetime,
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

CreateBudgetActionResponseTypeDef = TypedDict(
    "CreateBudgetActionResponseTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
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

DeleteBudgetActionResponseTypeDef = TypedDict(
    "DeleteBudgetActionResponseTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Action": "ActionTypeDef",
    },
)

_RequiredDescribeBudgetActionHistoriesResponseTypeDef = TypedDict(
    "_RequiredDescribeBudgetActionHistoriesResponseTypeDef",
    {
        "ActionHistories": List["ActionHistoryTypeDef"],
    },
)
_OptionalDescribeBudgetActionHistoriesResponseTypeDef = TypedDict(
    "_OptionalDescribeBudgetActionHistoriesResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class DescribeBudgetActionHistoriesResponseTypeDef(
    _RequiredDescribeBudgetActionHistoriesResponseTypeDef,
    _OptionalDescribeBudgetActionHistoriesResponseTypeDef,
):
    pass


DescribeBudgetActionResponseTypeDef = TypedDict(
    "DescribeBudgetActionResponseTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Action": "ActionTypeDef",
    },
)

_RequiredDescribeBudgetActionsForAccountResponseTypeDef = TypedDict(
    "_RequiredDescribeBudgetActionsForAccountResponseTypeDef",
    {
        "Actions": List["ActionTypeDef"],
    },
)
_OptionalDescribeBudgetActionsForAccountResponseTypeDef = TypedDict(
    "_OptionalDescribeBudgetActionsForAccountResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class DescribeBudgetActionsForAccountResponseTypeDef(
    _RequiredDescribeBudgetActionsForAccountResponseTypeDef,
    _OptionalDescribeBudgetActionsForAccountResponseTypeDef,
):
    pass


_RequiredDescribeBudgetActionsForBudgetResponseTypeDef = TypedDict(
    "_RequiredDescribeBudgetActionsForBudgetResponseTypeDef",
    {
        "Actions": List["ActionTypeDef"],
    },
)
_OptionalDescribeBudgetActionsForBudgetResponseTypeDef = TypedDict(
    "_OptionalDescribeBudgetActionsForBudgetResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class DescribeBudgetActionsForBudgetResponseTypeDef(
    _RequiredDescribeBudgetActionsForBudgetResponseTypeDef,
    _OptionalDescribeBudgetActionsForBudgetResponseTypeDef,
):
    pass


DescribeBudgetPerformanceHistoryResponseTypeDef = TypedDict(
    "DescribeBudgetPerformanceHistoryResponseTypeDef",
    {
        "BudgetPerformanceHistory": "BudgetPerformanceHistoryTypeDef",
        "NextToken": str,
    },
    total=False,
)

DescribeBudgetResponseTypeDef = TypedDict(
    "DescribeBudgetResponseTypeDef",
    {
        "Budget": "BudgetTypeDef",
    },
    total=False,
)

DescribeBudgetsResponseTypeDef = TypedDict(
    "DescribeBudgetsResponseTypeDef",
    {
        "Budgets": List["BudgetTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeNotificationsForBudgetResponseTypeDef = TypedDict(
    "DescribeNotificationsForBudgetResponseTypeDef",
    {
        "Notifications": List["NotificationTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeSubscribersForNotificationResponseTypeDef = TypedDict(
    "DescribeSubscribersForNotificationResponseTypeDef",
    {
        "Subscribers": List["SubscriberTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ExecuteBudgetActionResponseTypeDef = TypedDict(
    "ExecuteBudgetActionResponseTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
        "ExecutionType": ExecutionTypeType,
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
        "Start": datetime,
        "End": datetime,
    },
    total=False,
)

UpdateBudgetActionResponseTypeDef = TypedDict(
    "UpdateBudgetActionResponseTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "OldAction": "ActionTypeDef",
        "NewAction": "ActionTypeDef",
    },
)
