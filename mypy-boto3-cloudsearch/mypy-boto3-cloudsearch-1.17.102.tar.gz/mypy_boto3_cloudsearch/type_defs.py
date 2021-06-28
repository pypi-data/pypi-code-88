"""
Type annotations for cloudsearch service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloudsearch.type_defs import AccessPoliciesStatusTypeDef

    data: AccessPoliciesStatusTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AlgorithmicStemmingType,
    AnalysisSchemeLanguageType,
    IndexFieldTypeType,
    OptionStateType,
    PartitionInstanceTypeType,
    SuggesterFuzzyMatchingType,
    TLSSecurityPolicyType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccessPoliciesStatusTypeDef",
    "AnalysisOptionsTypeDef",
    "AnalysisSchemeStatusTypeDef",
    "AnalysisSchemeTypeDef",
    "AvailabilityOptionsStatusTypeDef",
    "BuildSuggestersRequestTypeDef",
    "BuildSuggestersResponseResponseTypeDef",
    "CreateDomainRequestTypeDef",
    "CreateDomainResponseResponseTypeDef",
    "DateArrayOptionsTypeDef",
    "DateOptionsTypeDef",
    "DefineAnalysisSchemeRequestTypeDef",
    "DefineAnalysisSchemeResponseResponseTypeDef",
    "DefineExpressionRequestTypeDef",
    "DefineExpressionResponseResponseTypeDef",
    "DefineIndexFieldRequestTypeDef",
    "DefineIndexFieldResponseResponseTypeDef",
    "DefineSuggesterRequestTypeDef",
    "DefineSuggesterResponseResponseTypeDef",
    "DeleteAnalysisSchemeRequestTypeDef",
    "DeleteAnalysisSchemeResponseResponseTypeDef",
    "DeleteDomainRequestTypeDef",
    "DeleteDomainResponseResponseTypeDef",
    "DeleteExpressionRequestTypeDef",
    "DeleteExpressionResponseResponseTypeDef",
    "DeleteIndexFieldRequestTypeDef",
    "DeleteIndexFieldResponseResponseTypeDef",
    "DeleteSuggesterRequestTypeDef",
    "DeleteSuggesterResponseResponseTypeDef",
    "DescribeAnalysisSchemesRequestTypeDef",
    "DescribeAnalysisSchemesResponseResponseTypeDef",
    "DescribeAvailabilityOptionsRequestTypeDef",
    "DescribeAvailabilityOptionsResponseResponseTypeDef",
    "DescribeDomainEndpointOptionsRequestTypeDef",
    "DescribeDomainEndpointOptionsResponseResponseTypeDef",
    "DescribeDomainsRequestTypeDef",
    "DescribeDomainsResponseResponseTypeDef",
    "DescribeExpressionsRequestTypeDef",
    "DescribeExpressionsResponseResponseTypeDef",
    "DescribeIndexFieldsRequestTypeDef",
    "DescribeIndexFieldsResponseResponseTypeDef",
    "DescribeScalingParametersRequestTypeDef",
    "DescribeScalingParametersResponseResponseTypeDef",
    "DescribeServiceAccessPoliciesRequestTypeDef",
    "DescribeServiceAccessPoliciesResponseResponseTypeDef",
    "DescribeSuggestersRequestTypeDef",
    "DescribeSuggestersResponseResponseTypeDef",
    "DocumentSuggesterOptionsTypeDef",
    "DomainEndpointOptionsStatusTypeDef",
    "DomainEndpointOptionsTypeDef",
    "DomainStatusTypeDef",
    "DoubleArrayOptionsTypeDef",
    "DoubleOptionsTypeDef",
    "ExpressionStatusTypeDef",
    "ExpressionTypeDef",
    "IndexDocumentsRequestTypeDef",
    "IndexDocumentsResponseResponseTypeDef",
    "IndexFieldStatusTypeDef",
    "IndexFieldTypeDef",
    "IntArrayOptionsTypeDef",
    "IntOptionsTypeDef",
    "LatLonOptionsTypeDef",
    "LimitsTypeDef",
    "ListDomainNamesResponseResponseTypeDef",
    "LiteralArrayOptionsTypeDef",
    "LiteralOptionsTypeDef",
    "OptionStatusTypeDef",
    "ResponseMetadataTypeDef",
    "ScalingParametersStatusTypeDef",
    "ScalingParametersTypeDef",
    "ServiceEndpointTypeDef",
    "SuggesterStatusTypeDef",
    "SuggesterTypeDef",
    "TextArrayOptionsTypeDef",
    "TextOptionsTypeDef",
    "UpdateAvailabilityOptionsRequestTypeDef",
    "UpdateAvailabilityOptionsResponseResponseTypeDef",
    "UpdateDomainEndpointOptionsRequestTypeDef",
    "UpdateDomainEndpointOptionsResponseResponseTypeDef",
    "UpdateScalingParametersRequestTypeDef",
    "UpdateScalingParametersResponseResponseTypeDef",
    "UpdateServiceAccessPoliciesRequestTypeDef",
    "UpdateServiceAccessPoliciesResponseResponseTypeDef",
)

AccessPoliciesStatusTypeDef = TypedDict(
    "AccessPoliciesStatusTypeDef",
    {
        "Options": str,
        "Status": "OptionStatusTypeDef",
    },
)

AnalysisOptionsTypeDef = TypedDict(
    "AnalysisOptionsTypeDef",
    {
        "Synonyms": str,
        "Stopwords": str,
        "StemmingDictionary": str,
        "JapaneseTokenizationDictionary": str,
        "AlgorithmicStemming": AlgorithmicStemmingType,
    },
    total=False,
)

AnalysisSchemeStatusTypeDef = TypedDict(
    "AnalysisSchemeStatusTypeDef",
    {
        "Options": "AnalysisSchemeTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

_RequiredAnalysisSchemeTypeDef = TypedDict(
    "_RequiredAnalysisSchemeTypeDef",
    {
        "AnalysisSchemeName": str,
        "AnalysisSchemeLanguage": AnalysisSchemeLanguageType,
    },
)
_OptionalAnalysisSchemeTypeDef = TypedDict(
    "_OptionalAnalysisSchemeTypeDef",
    {
        "AnalysisOptions": "AnalysisOptionsTypeDef",
    },
    total=False,
)


class AnalysisSchemeTypeDef(_RequiredAnalysisSchemeTypeDef, _OptionalAnalysisSchemeTypeDef):
    pass


AvailabilityOptionsStatusTypeDef = TypedDict(
    "AvailabilityOptionsStatusTypeDef",
    {
        "Options": bool,
        "Status": "OptionStatusTypeDef",
    },
)

BuildSuggestersRequestTypeDef = TypedDict(
    "BuildSuggestersRequestTypeDef",
    {
        "DomainName": str,
    },
)

BuildSuggestersResponseResponseTypeDef = TypedDict(
    "BuildSuggestersResponseResponseTypeDef",
    {
        "FieldNames": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDomainRequestTypeDef = TypedDict(
    "CreateDomainRequestTypeDef",
    {
        "DomainName": str,
    },
)

CreateDomainResponseResponseTypeDef = TypedDict(
    "CreateDomainResponseResponseTypeDef",
    {
        "DomainStatus": "DomainStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DateArrayOptionsTypeDef = TypedDict(
    "DateArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

DateOptionsTypeDef = TypedDict(
    "DateOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

DefineAnalysisSchemeRequestTypeDef = TypedDict(
    "DefineAnalysisSchemeRequestTypeDef",
    {
        "DomainName": str,
        "AnalysisScheme": "AnalysisSchemeTypeDef",
    },
)

DefineAnalysisSchemeResponseResponseTypeDef = TypedDict(
    "DefineAnalysisSchemeResponseResponseTypeDef",
    {
        "AnalysisScheme": "AnalysisSchemeStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DefineExpressionRequestTypeDef = TypedDict(
    "DefineExpressionRequestTypeDef",
    {
        "DomainName": str,
        "Expression": "ExpressionTypeDef",
    },
)

DefineExpressionResponseResponseTypeDef = TypedDict(
    "DefineExpressionResponseResponseTypeDef",
    {
        "Expression": "ExpressionStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DefineIndexFieldRequestTypeDef = TypedDict(
    "DefineIndexFieldRequestTypeDef",
    {
        "DomainName": str,
        "IndexField": "IndexFieldTypeDef",
    },
)

DefineIndexFieldResponseResponseTypeDef = TypedDict(
    "DefineIndexFieldResponseResponseTypeDef",
    {
        "IndexField": "IndexFieldStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DefineSuggesterRequestTypeDef = TypedDict(
    "DefineSuggesterRequestTypeDef",
    {
        "DomainName": str,
        "Suggester": "SuggesterTypeDef",
    },
)

DefineSuggesterResponseResponseTypeDef = TypedDict(
    "DefineSuggesterResponseResponseTypeDef",
    {
        "Suggester": "SuggesterStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAnalysisSchemeRequestTypeDef = TypedDict(
    "DeleteAnalysisSchemeRequestTypeDef",
    {
        "DomainName": str,
        "AnalysisSchemeName": str,
    },
)

DeleteAnalysisSchemeResponseResponseTypeDef = TypedDict(
    "DeleteAnalysisSchemeResponseResponseTypeDef",
    {
        "AnalysisScheme": "AnalysisSchemeStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDomainRequestTypeDef = TypedDict(
    "DeleteDomainRequestTypeDef",
    {
        "DomainName": str,
    },
)

DeleteDomainResponseResponseTypeDef = TypedDict(
    "DeleteDomainResponseResponseTypeDef",
    {
        "DomainStatus": "DomainStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteExpressionRequestTypeDef = TypedDict(
    "DeleteExpressionRequestTypeDef",
    {
        "DomainName": str,
        "ExpressionName": str,
    },
)

DeleteExpressionResponseResponseTypeDef = TypedDict(
    "DeleteExpressionResponseResponseTypeDef",
    {
        "Expression": "ExpressionStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteIndexFieldRequestTypeDef = TypedDict(
    "DeleteIndexFieldRequestTypeDef",
    {
        "DomainName": str,
        "IndexFieldName": str,
    },
)

DeleteIndexFieldResponseResponseTypeDef = TypedDict(
    "DeleteIndexFieldResponseResponseTypeDef",
    {
        "IndexField": "IndexFieldStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSuggesterRequestTypeDef = TypedDict(
    "DeleteSuggesterRequestTypeDef",
    {
        "DomainName": str,
        "SuggesterName": str,
    },
)

DeleteSuggesterResponseResponseTypeDef = TypedDict(
    "DeleteSuggesterResponseResponseTypeDef",
    {
        "Suggester": "SuggesterStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeAnalysisSchemesRequestTypeDef = TypedDict(
    "_RequiredDescribeAnalysisSchemesRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalDescribeAnalysisSchemesRequestTypeDef = TypedDict(
    "_OptionalDescribeAnalysisSchemesRequestTypeDef",
    {
        "AnalysisSchemeNames": List[str],
        "Deployed": bool,
    },
    total=False,
)


class DescribeAnalysisSchemesRequestTypeDef(
    _RequiredDescribeAnalysisSchemesRequestTypeDef, _OptionalDescribeAnalysisSchemesRequestTypeDef
):
    pass


DescribeAnalysisSchemesResponseResponseTypeDef = TypedDict(
    "DescribeAnalysisSchemesResponseResponseTypeDef",
    {
        "AnalysisSchemes": List["AnalysisSchemeStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeAvailabilityOptionsRequestTypeDef = TypedDict(
    "_RequiredDescribeAvailabilityOptionsRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalDescribeAvailabilityOptionsRequestTypeDef = TypedDict(
    "_OptionalDescribeAvailabilityOptionsRequestTypeDef",
    {
        "Deployed": bool,
    },
    total=False,
)


class DescribeAvailabilityOptionsRequestTypeDef(
    _RequiredDescribeAvailabilityOptionsRequestTypeDef,
    _OptionalDescribeAvailabilityOptionsRequestTypeDef,
):
    pass


DescribeAvailabilityOptionsResponseResponseTypeDef = TypedDict(
    "DescribeAvailabilityOptionsResponseResponseTypeDef",
    {
        "AvailabilityOptions": "AvailabilityOptionsStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeDomainEndpointOptionsRequestTypeDef = TypedDict(
    "_RequiredDescribeDomainEndpointOptionsRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalDescribeDomainEndpointOptionsRequestTypeDef = TypedDict(
    "_OptionalDescribeDomainEndpointOptionsRequestTypeDef",
    {
        "Deployed": bool,
    },
    total=False,
)


class DescribeDomainEndpointOptionsRequestTypeDef(
    _RequiredDescribeDomainEndpointOptionsRequestTypeDef,
    _OptionalDescribeDomainEndpointOptionsRequestTypeDef,
):
    pass


DescribeDomainEndpointOptionsResponseResponseTypeDef = TypedDict(
    "DescribeDomainEndpointOptionsResponseResponseTypeDef",
    {
        "DomainEndpointOptions": "DomainEndpointOptionsStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDomainsRequestTypeDef = TypedDict(
    "DescribeDomainsRequestTypeDef",
    {
        "DomainNames": List[str],
    },
    total=False,
)

DescribeDomainsResponseResponseTypeDef = TypedDict(
    "DescribeDomainsResponseResponseTypeDef",
    {
        "DomainStatusList": List["DomainStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeExpressionsRequestTypeDef = TypedDict(
    "_RequiredDescribeExpressionsRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalDescribeExpressionsRequestTypeDef = TypedDict(
    "_OptionalDescribeExpressionsRequestTypeDef",
    {
        "ExpressionNames": List[str],
        "Deployed": bool,
    },
    total=False,
)


class DescribeExpressionsRequestTypeDef(
    _RequiredDescribeExpressionsRequestTypeDef, _OptionalDescribeExpressionsRequestTypeDef
):
    pass


DescribeExpressionsResponseResponseTypeDef = TypedDict(
    "DescribeExpressionsResponseResponseTypeDef",
    {
        "Expressions": List["ExpressionStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeIndexFieldsRequestTypeDef = TypedDict(
    "_RequiredDescribeIndexFieldsRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalDescribeIndexFieldsRequestTypeDef = TypedDict(
    "_OptionalDescribeIndexFieldsRequestTypeDef",
    {
        "FieldNames": List[str],
        "Deployed": bool,
    },
    total=False,
)


class DescribeIndexFieldsRequestTypeDef(
    _RequiredDescribeIndexFieldsRequestTypeDef, _OptionalDescribeIndexFieldsRequestTypeDef
):
    pass


DescribeIndexFieldsResponseResponseTypeDef = TypedDict(
    "DescribeIndexFieldsResponseResponseTypeDef",
    {
        "IndexFields": List["IndexFieldStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeScalingParametersRequestTypeDef = TypedDict(
    "DescribeScalingParametersRequestTypeDef",
    {
        "DomainName": str,
    },
)

DescribeScalingParametersResponseResponseTypeDef = TypedDict(
    "DescribeScalingParametersResponseResponseTypeDef",
    {
        "ScalingParameters": "ScalingParametersStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeServiceAccessPoliciesRequestTypeDef = TypedDict(
    "_RequiredDescribeServiceAccessPoliciesRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalDescribeServiceAccessPoliciesRequestTypeDef = TypedDict(
    "_OptionalDescribeServiceAccessPoliciesRequestTypeDef",
    {
        "Deployed": bool,
    },
    total=False,
)


class DescribeServiceAccessPoliciesRequestTypeDef(
    _RequiredDescribeServiceAccessPoliciesRequestTypeDef,
    _OptionalDescribeServiceAccessPoliciesRequestTypeDef,
):
    pass


DescribeServiceAccessPoliciesResponseResponseTypeDef = TypedDict(
    "DescribeServiceAccessPoliciesResponseResponseTypeDef",
    {
        "AccessPolicies": "AccessPoliciesStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeSuggestersRequestTypeDef = TypedDict(
    "_RequiredDescribeSuggestersRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalDescribeSuggestersRequestTypeDef = TypedDict(
    "_OptionalDescribeSuggestersRequestTypeDef",
    {
        "SuggesterNames": List[str],
        "Deployed": bool,
    },
    total=False,
)


class DescribeSuggestersRequestTypeDef(
    _RequiredDescribeSuggestersRequestTypeDef, _OptionalDescribeSuggestersRequestTypeDef
):
    pass


DescribeSuggestersResponseResponseTypeDef = TypedDict(
    "DescribeSuggestersResponseResponseTypeDef",
    {
        "Suggesters": List["SuggesterStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDocumentSuggesterOptionsTypeDef = TypedDict(
    "_RequiredDocumentSuggesterOptionsTypeDef",
    {
        "SourceField": str,
    },
)
_OptionalDocumentSuggesterOptionsTypeDef = TypedDict(
    "_OptionalDocumentSuggesterOptionsTypeDef",
    {
        "FuzzyMatching": SuggesterFuzzyMatchingType,
        "SortExpression": str,
    },
    total=False,
)


class DocumentSuggesterOptionsTypeDef(
    _RequiredDocumentSuggesterOptionsTypeDef, _OptionalDocumentSuggesterOptionsTypeDef
):
    pass


DomainEndpointOptionsStatusTypeDef = TypedDict(
    "DomainEndpointOptionsStatusTypeDef",
    {
        "Options": "DomainEndpointOptionsTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

DomainEndpointOptionsTypeDef = TypedDict(
    "DomainEndpointOptionsTypeDef",
    {
        "EnforceHTTPS": bool,
        "TLSSecurityPolicy": TLSSecurityPolicyType,
    },
    total=False,
)

_RequiredDomainStatusTypeDef = TypedDict(
    "_RequiredDomainStatusTypeDef",
    {
        "DomainId": str,
        "DomainName": str,
        "RequiresIndexDocuments": bool,
    },
)
_OptionalDomainStatusTypeDef = TypedDict(
    "_OptionalDomainStatusTypeDef",
    {
        "ARN": str,
        "Created": bool,
        "Deleted": bool,
        "DocService": "ServiceEndpointTypeDef",
        "SearchService": "ServiceEndpointTypeDef",
        "Processing": bool,
        "SearchInstanceType": str,
        "SearchPartitionCount": int,
        "SearchInstanceCount": int,
        "Limits": "LimitsTypeDef",
    },
    total=False,
)


class DomainStatusTypeDef(_RequiredDomainStatusTypeDef, _OptionalDomainStatusTypeDef):
    pass


DoubleArrayOptionsTypeDef = TypedDict(
    "DoubleArrayOptionsTypeDef",
    {
        "DefaultValue": float,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

DoubleOptionsTypeDef = TypedDict(
    "DoubleOptionsTypeDef",
    {
        "DefaultValue": float,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

ExpressionStatusTypeDef = TypedDict(
    "ExpressionStatusTypeDef",
    {
        "Options": "ExpressionTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

ExpressionTypeDef = TypedDict(
    "ExpressionTypeDef",
    {
        "ExpressionName": str,
        "ExpressionValue": str,
    },
)

IndexDocumentsRequestTypeDef = TypedDict(
    "IndexDocumentsRequestTypeDef",
    {
        "DomainName": str,
    },
)

IndexDocumentsResponseResponseTypeDef = TypedDict(
    "IndexDocumentsResponseResponseTypeDef",
    {
        "FieldNames": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IndexFieldStatusTypeDef = TypedDict(
    "IndexFieldStatusTypeDef",
    {
        "Options": "IndexFieldTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

_RequiredIndexFieldTypeDef = TypedDict(
    "_RequiredIndexFieldTypeDef",
    {
        "IndexFieldName": str,
        "IndexFieldType": IndexFieldTypeType,
    },
)
_OptionalIndexFieldTypeDef = TypedDict(
    "_OptionalIndexFieldTypeDef",
    {
        "IntOptions": "IntOptionsTypeDef",
        "DoubleOptions": "DoubleOptionsTypeDef",
        "LiteralOptions": "LiteralOptionsTypeDef",
        "TextOptions": "TextOptionsTypeDef",
        "DateOptions": "DateOptionsTypeDef",
        "LatLonOptions": "LatLonOptionsTypeDef",
        "IntArrayOptions": "IntArrayOptionsTypeDef",
        "DoubleArrayOptions": "DoubleArrayOptionsTypeDef",
        "LiteralArrayOptions": "LiteralArrayOptionsTypeDef",
        "TextArrayOptions": "TextArrayOptionsTypeDef",
        "DateArrayOptions": "DateArrayOptionsTypeDef",
    },
    total=False,
)


class IndexFieldTypeDef(_RequiredIndexFieldTypeDef, _OptionalIndexFieldTypeDef):
    pass


IntArrayOptionsTypeDef = TypedDict(
    "IntArrayOptionsTypeDef",
    {
        "DefaultValue": int,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

IntOptionsTypeDef = TypedDict(
    "IntOptionsTypeDef",
    {
        "DefaultValue": int,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

LatLonOptionsTypeDef = TypedDict(
    "LatLonOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

LimitsTypeDef = TypedDict(
    "LimitsTypeDef",
    {
        "MaximumReplicationCount": int,
        "MaximumPartitionCount": int,
    },
)

ListDomainNamesResponseResponseTypeDef = TypedDict(
    "ListDomainNamesResponseResponseTypeDef",
    {
        "DomainNames": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LiteralArrayOptionsTypeDef = TypedDict(
    "LiteralArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

LiteralOptionsTypeDef = TypedDict(
    "LiteralOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

_RequiredOptionStatusTypeDef = TypedDict(
    "_RequiredOptionStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "State": OptionStateType,
    },
)
_OptionalOptionStatusTypeDef = TypedDict(
    "_OptionalOptionStatusTypeDef",
    {
        "UpdateVersion": int,
        "PendingDeletion": bool,
    },
    total=False,
)


class OptionStatusTypeDef(_RequiredOptionStatusTypeDef, _OptionalOptionStatusTypeDef):
    pass


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

ScalingParametersStatusTypeDef = TypedDict(
    "ScalingParametersStatusTypeDef",
    {
        "Options": "ScalingParametersTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

ScalingParametersTypeDef = TypedDict(
    "ScalingParametersTypeDef",
    {
        "DesiredInstanceType": PartitionInstanceTypeType,
        "DesiredReplicationCount": int,
        "DesiredPartitionCount": int,
    },
    total=False,
)

ServiceEndpointTypeDef = TypedDict(
    "ServiceEndpointTypeDef",
    {
        "Endpoint": str,
    },
    total=False,
)

SuggesterStatusTypeDef = TypedDict(
    "SuggesterStatusTypeDef",
    {
        "Options": "SuggesterTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

SuggesterTypeDef = TypedDict(
    "SuggesterTypeDef",
    {
        "SuggesterName": str,
        "DocumentSuggesterOptions": "DocumentSuggesterOptionsTypeDef",
    },
)

TextArrayOptionsTypeDef = TypedDict(
    "TextArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "ReturnEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)

TextOptionsTypeDef = TypedDict(
    "TextOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)

UpdateAvailabilityOptionsRequestTypeDef = TypedDict(
    "UpdateAvailabilityOptionsRequestTypeDef",
    {
        "DomainName": str,
        "MultiAZ": bool,
    },
)

UpdateAvailabilityOptionsResponseResponseTypeDef = TypedDict(
    "UpdateAvailabilityOptionsResponseResponseTypeDef",
    {
        "AvailabilityOptions": "AvailabilityOptionsStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDomainEndpointOptionsRequestTypeDef = TypedDict(
    "UpdateDomainEndpointOptionsRequestTypeDef",
    {
        "DomainName": str,
        "DomainEndpointOptions": "DomainEndpointOptionsTypeDef",
    },
)

UpdateDomainEndpointOptionsResponseResponseTypeDef = TypedDict(
    "UpdateDomainEndpointOptionsResponseResponseTypeDef",
    {
        "DomainEndpointOptions": "DomainEndpointOptionsStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateScalingParametersRequestTypeDef = TypedDict(
    "UpdateScalingParametersRequestTypeDef",
    {
        "DomainName": str,
        "ScalingParameters": "ScalingParametersTypeDef",
    },
)

UpdateScalingParametersResponseResponseTypeDef = TypedDict(
    "UpdateScalingParametersResponseResponseTypeDef",
    {
        "ScalingParameters": "ScalingParametersStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateServiceAccessPoliciesRequestTypeDef = TypedDict(
    "UpdateServiceAccessPoliciesRequestTypeDef",
    {
        "DomainName": str,
        "AccessPolicies": str,
    },
)

UpdateServiceAccessPoliciesResponseResponseTypeDef = TypedDict(
    "UpdateServiceAccessPoliciesResponseResponseTypeDef",
    {
        "AccessPolicies": "AccessPoliciesStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
