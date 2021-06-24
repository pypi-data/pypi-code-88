"""
Type annotations for savingsplans service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/type_defs.html)

Usage::

    ```python
    from mypy_boto3_savingsplans.type_defs import CreateSavingsPlanResponseTypeDef

    data: CreateSavingsPlanResponseTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

from .literals import (
    CurrencyCodeType,
    SavingsPlanOfferingFilterAttributeType,
    SavingsPlanOfferingPropertyKeyType,
    SavingsPlanPaymentOptionType,
    SavingsPlanProductTypeType,
    SavingsPlanRateFilterAttributeType,
    SavingsPlanRateFilterNameType,
    SavingsPlanRatePropertyKeyType,
    SavingsPlanRateServiceCodeType,
    SavingsPlanRateUnitType,
    SavingsPlansFilterNameType,
    SavingsPlanStateType,
    SavingsPlanTypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateSavingsPlanResponseTypeDef",
    "DescribeSavingsPlanRatesResponseTypeDef",
    "DescribeSavingsPlansOfferingRatesResponseTypeDef",
    "DescribeSavingsPlansOfferingsResponseTypeDef",
    "DescribeSavingsPlansResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ParentSavingsPlanOfferingTypeDef",
    "SavingsPlanFilterTypeDef",
    "SavingsPlanOfferingFilterElementTypeDef",
    "SavingsPlanOfferingPropertyTypeDef",
    "SavingsPlanOfferingRateFilterElementTypeDef",
    "SavingsPlanOfferingRatePropertyTypeDef",
    "SavingsPlanOfferingRateTypeDef",
    "SavingsPlanOfferingTypeDef",
    "SavingsPlanRateFilterTypeDef",
    "SavingsPlanRatePropertyTypeDef",
    "SavingsPlanRateTypeDef",
    "SavingsPlanTypeDef",
)

CreateSavingsPlanResponseTypeDef = TypedDict(
    "CreateSavingsPlanResponseTypeDef",
    {
        "savingsPlanId": str,
    },
    total=False,
)

DescribeSavingsPlanRatesResponseTypeDef = TypedDict(
    "DescribeSavingsPlanRatesResponseTypeDef",
    {
        "savingsPlanId": str,
        "searchResults": List["SavingsPlanRateTypeDef"],
        "nextToken": str,
    },
    total=False,
)

DescribeSavingsPlansOfferingRatesResponseTypeDef = TypedDict(
    "DescribeSavingsPlansOfferingRatesResponseTypeDef",
    {
        "searchResults": List["SavingsPlanOfferingRateTypeDef"],
        "nextToken": str,
    },
    total=False,
)

DescribeSavingsPlansOfferingsResponseTypeDef = TypedDict(
    "DescribeSavingsPlansOfferingsResponseTypeDef",
    {
        "searchResults": List["SavingsPlanOfferingTypeDef"],
        "nextToken": str,
    },
    total=False,
)

DescribeSavingsPlansResponseTypeDef = TypedDict(
    "DescribeSavingsPlansResponseTypeDef",
    {
        "savingsPlans": List["SavingsPlanTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

ParentSavingsPlanOfferingTypeDef = TypedDict(
    "ParentSavingsPlanOfferingTypeDef",
    {
        "offeringId": str,
        "paymentOption": SavingsPlanPaymentOptionType,
        "planType": SavingsPlanTypeType,
        "durationSeconds": int,
        "currency": CurrencyCodeType,
        "planDescription": str,
    },
    total=False,
)

SavingsPlanFilterTypeDef = TypedDict(
    "SavingsPlanFilterTypeDef",
    {
        "name": SavingsPlansFilterNameType,
        "values": List[str],
    },
    total=False,
)

SavingsPlanOfferingFilterElementTypeDef = TypedDict(
    "SavingsPlanOfferingFilterElementTypeDef",
    {
        "name": SavingsPlanOfferingFilterAttributeType,
        "values": List[str],
    },
    total=False,
)

SavingsPlanOfferingPropertyTypeDef = TypedDict(
    "SavingsPlanOfferingPropertyTypeDef",
    {
        "name": SavingsPlanOfferingPropertyKeyType,
        "value": str,
    },
    total=False,
)

SavingsPlanOfferingRateFilterElementTypeDef = TypedDict(
    "SavingsPlanOfferingRateFilterElementTypeDef",
    {
        "name": SavingsPlanRateFilterAttributeType,
        "values": List[str],
    },
    total=False,
)

SavingsPlanOfferingRatePropertyTypeDef = TypedDict(
    "SavingsPlanOfferingRatePropertyTypeDef",
    {
        "name": str,
        "value": str,
    },
    total=False,
)

SavingsPlanOfferingRateTypeDef = TypedDict(
    "SavingsPlanOfferingRateTypeDef",
    {
        "savingsPlanOffering": "ParentSavingsPlanOfferingTypeDef",
        "rate": str,
        "unit": SavingsPlanRateUnitType,
        "productType": SavingsPlanProductTypeType,
        "serviceCode": SavingsPlanRateServiceCodeType,
        "usageType": str,
        "operation": str,
        "properties": List["SavingsPlanOfferingRatePropertyTypeDef"],
    },
    total=False,
)

SavingsPlanOfferingTypeDef = TypedDict(
    "SavingsPlanOfferingTypeDef",
    {
        "offeringId": str,
        "productTypes": List[SavingsPlanProductTypeType],
        "planType": SavingsPlanTypeType,
        "description": str,
        "paymentOption": SavingsPlanPaymentOptionType,
        "durationSeconds": int,
        "currency": CurrencyCodeType,
        "serviceCode": str,
        "usageType": str,
        "operation": str,
        "properties": List["SavingsPlanOfferingPropertyTypeDef"],
    },
    total=False,
)

SavingsPlanRateFilterTypeDef = TypedDict(
    "SavingsPlanRateFilterTypeDef",
    {
        "name": SavingsPlanRateFilterNameType,
        "values": List[str],
    },
    total=False,
)

SavingsPlanRatePropertyTypeDef = TypedDict(
    "SavingsPlanRatePropertyTypeDef",
    {
        "name": SavingsPlanRatePropertyKeyType,
        "value": str,
    },
    total=False,
)

SavingsPlanRateTypeDef = TypedDict(
    "SavingsPlanRateTypeDef",
    {
        "rate": str,
        "currency": CurrencyCodeType,
        "unit": SavingsPlanRateUnitType,
        "productType": SavingsPlanProductTypeType,
        "serviceCode": SavingsPlanRateServiceCodeType,
        "usageType": str,
        "operation": str,
        "properties": List["SavingsPlanRatePropertyTypeDef"],
    },
    total=False,
)

SavingsPlanTypeDef = TypedDict(
    "SavingsPlanTypeDef",
    {
        "offeringId": str,
        "savingsPlanId": str,
        "savingsPlanArn": str,
        "description": str,
        "start": str,
        "end": str,
        "state": SavingsPlanStateType,
        "region": str,
        "ec2InstanceFamily": str,
        "savingsPlanType": SavingsPlanTypeType,
        "paymentOption": SavingsPlanPaymentOptionType,
        "productTypes": List[SavingsPlanProductTypeType],
        "currency": CurrencyCodeType,
        "commitment": str,
        "upfrontPaymentAmount": str,
        "recurringPaymentAmount": str,
        "termDurationInSeconds": int,
        "tags": Dict[str, str],
    },
    total=False,
)
