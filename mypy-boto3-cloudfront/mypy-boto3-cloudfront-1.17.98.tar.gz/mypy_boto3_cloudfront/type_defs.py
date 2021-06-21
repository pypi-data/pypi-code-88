"""
Type annotations for cloudfront service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloudfront.type_defs import ActiveTrustedKeyGroupsTypeDef

    data: ActiveTrustedKeyGroupsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, List, Union

from .literals import (
    CachePolicyCookieBehaviorType,
    CachePolicyHeaderBehaviorType,
    CachePolicyQueryStringBehaviorType,
    CachePolicyTypeType,
    CertificateSourceType,
    EventTypeType,
    FunctionStageType,
    GeoRestrictionTypeType,
    HttpVersionType,
    ICPRecordalStatusType,
    ItemSelectionType,
    MethodType,
    MinimumProtocolVersionType,
    OriginProtocolPolicyType,
    OriginRequestPolicyCookieBehaviorType,
    OriginRequestPolicyHeaderBehaviorType,
    OriginRequestPolicyQueryStringBehaviorType,
    OriginRequestPolicyTypeType,
    PriceClassType,
    RealtimeMetricsSubscriptionStatusType,
    SslProtocolType,
    SSLSupportMethodType,
    ViewerProtocolPolicyType,
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
    "ActiveTrustedKeyGroupsTypeDef",
    "ActiveTrustedSignersTypeDef",
    "AliasICPRecordalTypeDef",
    "AliasesTypeDef",
    "AllowedMethodsTypeDef",
    "CacheBehaviorTypeDef",
    "CacheBehaviorsTypeDef",
    "CachePolicyConfigTypeDef",
    "CachePolicyCookiesConfigTypeDef",
    "CachePolicyHeadersConfigTypeDef",
    "CachePolicyListTypeDef",
    "CachePolicyQueryStringsConfigTypeDef",
    "CachePolicySummaryTypeDef",
    "CachePolicyTypeDef",
    "CachedMethodsTypeDef",
    "CloudFrontOriginAccessIdentityConfigTypeDef",
    "CloudFrontOriginAccessIdentityListTypeDef",
    "CloudFrontOriginAccessIdentitySummaryTypeDef",
    "CloudFrontOriginAccessIdentityTypeDef",
    "ContentTypeProfileConfigTypeDef",
    "ContentTypeProfileTypeDef",
    "ContentTypeProfilesTypeDef",
    "CookieNamesTypeDef",
    "CookiePreferenceTypeDef",
    "CreateCachePolicyResultTypeDef",
    "CreateCloudFrontOriginAccessIdentityResultTypeDef",
    "CreateDistributionResultTypeDef",
    "CreateDistributionWithTagsResultTypeDef",
    "CreateFieldLevelEncryptionConfigResultTypeDef",
    "CreateFieldLevelEncryptionProfileResultTypeDef",
    "CreateFunctionResultTypeDef",
    "CreateInvalidationResultTypeDef",
    "CreateKeyGroupResultTypeDef",
    "CreateMonitoringSubscriptionResultTypeDef",
    "CreateOriginRequestPolicyResultTypeDef",
    "CreatePublicKeyResultTypeDef",
    "CreateRealtimeLogConfigResultTypeDef",
    "CreateStreamingDistributionResultTypeDef",
    "CreateStreamingDistributionWithTagsResultTypeDef",
    "CustomErrorResponseTypeDef",
    "CustomErrorResponsesTypeDef",
    "CustomHeadersTypeDef",
    "CustomOriginConfigTypeDef",
    "DefaultCacheBehaviorTypeDef",
    "DescribeFunctionResultTypeDef",
    "DistributionConfigTypeDef",
    "DistributionConfigWithTagsTypeDef",
    "DistributionIdListTypeDef",
    "DistributionListTypeDef",
    "DistributionSummaryTypeDef",
    "DistributionTypeDef",
    "EncryptionEntitiesTypeDef",
    "EncryptionEntityTypeDef",
    "EndPointTypeDef",
    "FieldLevelEncryptionConfigTypeDef",
    "FieldLevelEncryptionListTypeDef",
    "FieldLevelEncryptionProfileConfigTypeDef",
    "FieldLevelEncryptionProfileListTypeDef",
    "FieldLevelEncryptionProfileSummaryTypeDef",
    "FieldLevelEncryptionProfileTypeDef",
    "FieldLevelEncryptionSummaryTypeDef",
    "FieldLevelEncryptionTypeDef",
    "FieldPatternsTypeDef",
    "ForwardedValuesTypeDef",
    "FunctionAssociationTypeDef",
    "FunctionAssociationsTypeDef",
    "FunctionConfigTypeDef",
    "FunctionListTypeDef",
    "FunctionMetadataTypeDef",
    "FunctionSummaryTypeDef",
    "GeoRestrictionTypeDef",
    "GetCachePolicyConfigResultTypeDef",
    "GetCachePolicyResultTypeDef",
    "GetCloudFrontOriginAccessIdentityConfigResultTypeDef",
    "GetCloudFrontOriginAccessIdentityResultTypeDef",
    "GetDistributionConfigResultTypeDef",
    "GetDistributionResultTypeDef",
    "GetFieldLevelEncryptionConfigResultTypeDef",
    "GetFieldLevelEncryptionProfileConfigResultTypeDef",
    "GetFieldLevelEncryptionProfileResultTypeDef",
    "GetFieldLevelEncryptionResultTypeDef",
    "GetFunctionResultTypeDef",
    "GetInvalidationResultTypeDef",
    "GetKeyGroupConfigResultTypeDef",
    "GetKeyGroupResultTypeDef",
    "GetMonitoringSubscriptionResultTypeDef",
    "GetOriginRequestPolicyConfigResultTypeDef",
    "GetOriginRequestPolicyResultTypeDef",
    "GetPublicKeyConfigResultTypeDef",
    "GetPublicKeyResultTypeDef",
    "GetRealtimeLogConfigResultTypeDef",
    "GetStreamingDistributionConfigResultTypeDef",
    "GetStreamingDistributionResultTypeDef",
    "HeadersTypeDef",
    "InvalidationBatchTypeDef",
    "InvalidationListTypeDef",
    "InvalidationSummaryTypeDef",
    "InvalidationTypeDef",
    "KGKeyPairIdsTypeDef",
    "KeyGroupConfigTypeDef",
    "KeyGroupListTypeDef",
    "KeyGroupSummaryTypeDef",
    "KeyGroupTypeDef",
    "KeyPairIdsTypeDef",
    "KinesisStreamConfigTypeDef",
    "LambdaFunctionAssociationTypeDef",
    "LambdaFunctionAssociationsTypeDef",
    "ListCachePoliciesResultTypeDef",
    "ListCloudFrontOriginAccessIdentitiesResultTypeDef",
    "ListDistributionsByCachePolicyIdResultTypeDef",
    "ListDistributionsByKeyGroupResultTypeDef",
    "ListDistributionsByOriginRequestPolicyIdResultTypeDef",
    "ListDistributionsByRealtimeLogConfigResultTypeDef",
    "ListDistributionsByWebACLIdResultTypeDef",
    "ListDistributionsResultTypeDef",
    "ListFieldLevelEncryptionConfigsResultTypeDef",
    "ListFieldLevelEncryptionProfilesResultTypeDef",
    "ListFunctionsResultTypeDef",
    "ListInvalidationsResultTypeDef",
    "ListKeyGroupsResultTypeDef",
    "ListOriginRequestPoliciesResultTypeDef",
    "ListPublicKeysResultTypeDef",
    "ListRealtimeLogConfigsResultTypeDef",
    "ListStreamingDistributionsResultTypeDef",
    "ListTagsForResourceResultTypeDef",
    "LoggingConfigTypeDef",
    "MonitoringSubscriptionTypeDef",
    "OriginCustomHeaderTypeDef",
    "OriginGroupFailoverCriteriaTypeDef",
    "OriginGroupMemberTypeDef",
    "OriginGroupMembersTypeDef",
    "OriginGroupTypeDef",
    "OriginGroupsTypeDef",
    "OriginRequestPolicyConfigTypeDef",
    "OriginRequestPolicyCookiesConfigTypeDef",
    "OriginRequestPolicyHeadersConfigTypeDef",
    "OriginRequestPolicyListTypeDef",
    "OriginRequestPolicyQueryStringsConfigTypeDef",
    "OriginRequestPolicySummaryTypeDef",
    "OriginRequestPolicyTypeDef",
    "OriginShieldTypeDef",
    "OriginSslProtocolsTypeDef",
    "OriginTypeDef",
    "OriginsTypeDef",
    "PaginatorConfigTypeDef",
    "ParametersInCacheKeyAndForwardedToOriginTypeDef",
    "PathsTypeDef",
    "PublicKeyConfigTypeDef",
    "PublicKeyListTypeDef",
    "PublicKeySummaryTypeDef",
    "PublicKeyTypeDef",
    "PublishFunctionResultTypeDef",
    "QueryArgProfileConfigTypeDef",
    "QueryArgProfileTypeDef",
    "QueryArgProfilesTypeDef",
    "QueryStringCacheKeysTypeDef",
    "QueryStringNamesTypeDef",
    "RealtimeLogConfigTypeDef",
    "RealtimeLogConfigsTypeDef",
    "RealtimeMetricsSubscriptionConfigTypeDef",
    "RestrictionsTypeDef",
    "S3OriginConfigTypeDef",
    "S3OriginTypeDef",
    "SignerTypeDef",
    "StatusCodesTypeDef",
    "StreamingDistributionConfigTypeDef",
    "StreamingDistributionConfigWithTagsTypeDef",
    "StreamingDistributionListTypeDef",
    "StreamingDistributionSummaryTypeDef",
    "StreamingDistributionTypeDef",
    "StreamingLoggingConfigTypeDef",
    "TagKeysTypeDef",
    "TagTypeDef",
    "TagsTypeDef",
    "TestFunctionResultTypeDef",
    "TestResultTypeDef",
    "TrustedKeyGroupsTypeDef",
    "TrustedSignersTypeDef",
    "UpdateCachePolicyResultTypeDef",
    "UpdateCloudFrontOriginAccessIdentityResultTypeDef",
    "UpdateDistributionResultTypeDef",
    "UpdateFieldLevelEncryptionConfigResultTypeDef",
    "UpdateFieldLevelEncryptionProfileResultTypeDef",
    "UpdateFunctionResultTypeDef",
    "UpdateKeyGroupResultTypeDef",
    "UpdateOriginRequestPolicyResultTypeDef",
    "UpdatePublicKeyResultTypeDef",
    "UpdateRealtimeLogConfigResultTypeDef",
    "UpdateStreamingDistributionResultTypeDef",
    "ViewerCertificateTypeDef",
    "WaiterConfigTypeDef",
)

_RequiredActiveTrustedKeyGroupsTypeDef = TypedDict(
    "_RequiredActiveTrustedKeyGroupsTypeDef",
    {
        "Enabled": bool,
        "Quantity": int,
    },
)
_OptionalActiveTrustedKeyGroupsTypeDef = TypedDict(
    "_OptionalActiveTrustedKeyGroupsTypeDef",
    {
        "Items": List["KGKeyPairIdsTypeDef"],
    },
    total=False,
)


class ActiveTrustedKeyGroupsTypeDef(
    _RequiredActiveTrustedKeyGroupsTypeDef, _OptionalActiveTrustedKeyGroupsTypeDef
):
    pass


_RequiredActiveTrustedSignersTypeDef = TypedDict(
    "_RequiredActiveTrustedSignersTypeDef",
    {
        "Enabled": bool,
        "Quantity": int,
    },
)
_OptionalActiveTrustedSignersTypeDef = TypedDict(
    "_OptionalActiveTrustedSignersTypeDef",
    {
        "Items": List["SignerTypeDef"],
    },
    total=False,
)


class ActiveTrustedSignersTypeDef(
    _RequiredActiveTrustedSignersTypeDef, _OptionalActiveTrustedSignersTypeDef
):
    pass


AliasICPRecordalTypeDef = TypedDict(
    "AliasICPRecordalTypeDef",
    {
        "CNAME": str,
        "ICPRecordalStatus": ICPRecordalStatusType,
    },
    total=False,
)

_RequiredAliasesTypeDef = TypedDict(
    "_RequiredAliasesTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalAliasesTypeDef = TypedDict(
    "_OptionalAliasesTypeDef",
    {
        "Items": List[str],
    },
    total=False,
)


class AliasesTypeDef(_RequiredAliasesTypeDef, _OptionalAliasesTypeDef):
    pass


_RequiredAllowedMethodsTypeDef = TypedDict(
    "_RequiredAllowedMethodsTypeDef",
    {
        "Quantity": int,
        "Items": List[MethodType],
    },
)
_OptionalAllowedMethodsTypeDef = TypedDict(
    "_OptionalAllowedMethodsTypeDef",
    {
        "CachedMethods": "CachedMethodsTypeDef",
    },
    total=False,
)


class AllowedMethodsTypeDef(_RequiredAllowedMethodsTypeDef, _OptionalAllowedMethodsTypeDef):
    pass


_RequiredCacheBehaviorTypeDef = TypedDict(
    "_RequiredCacheBehaviorTypeDef",
    {
        "PathPattern": str,
        "TargetOriginId": str,
        "ViewerProtocolPolicy": ViewerProtocolPolicyType,
    },
)
_OptionalCacheBehaviorTypeDef = TypedDict(
    "_OptionalCacheBehaviorTypeDef",
    {
        "TrustedSigners": "TrustedSignersTypeDef",
        "TrustedKeyGroups": "TrustedKeyGroupsTypeDef",
        "AllowedMethods": "AllowedMethodsTypeDef",
        "SmoothStreaming": bool,
        "Compress": bool,
        "LambdaFunctionAssociations": "LambdaFunctionAssociationsTypeDef",
        "FunctionAssociations": "FunctionAssociationsTypeDef",
        "FieldLevelEncryptionId": str,
        "RealtimeLogConfigArn": str,
        "CachePolicyId": str,
        "OriginRequestPolicyId": str,
        "ForwardedValues": "ForwardedValuesTypeDef",
        "MinTTL": int,
        "DefaultTTL": int,
        "MaxTTL": int,
    },
    total=False,
)


class CacheBehaviorTypeDef(_RequiredCacheBehaviorTypeDef, _OptionalCacheBehaviorTypeDef):
    pass


_RequiredCacheBehaviorsTypeDef = TypedDict(
    "_RequiredCacheBehaviorsTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalCacheBehaviorsTypeDef = TypedDict(
    "_OptionalCacheBehaviorsTypeDef",
    {
        "Items": List["CacheBehaviorTypeDef"],
    },
    total=False,
)


class CacheBehaviorsTypeDef(_RequiredCacheBehaviorsTypeDef, _OptionalCacheBehaviorsTypeDef):
    pass


_RequiredCachePolicyConfigTypeDef = TypedDict(
    "_RequiredCachePolicyConfigTypeDef",
    {
        "Name": str,
        "MinTTL": int,
    },
)
_OptionalCachePolicyConfigTypeDef = TypedDict(
    "_OptionalCachePolicyConfigTypeDef",
    {
        "Comment": str,
        "DefaultTTL": int,
        "MaxTTL": int,
        "ParametersInCacheKeyAndForwardedToOrigin": "ParametersInCacheKeyAndForwardedToOriginTypeDef",
    },
    total=False,
)


class CachePolicyConfigTypeDef(
    _RequiredCachePolicyConfigTypeDef, _OptionalCachePolicyConfigTypeDef
):
    pass


_RequiredCachePolicyCookiesConfigTypeDef = TypedDict(
    "_RequiredCachePolicyCookiesConfigTypeDef",
    {
        "CookieBehavior": CachePolicyCookieBehaviorType,
    },
)
_OptionalCachePolicyCookiesConfigTypeDef = TypedDict(
    "_OptionalCachePolicyCookiesConfigTypeDef",
    {
        "Cookies": "CookieNamesTypeDef",
    },
    total=False,
)


class CachePolicyCookiesConfigTypeDef(
    _RequiredCachePolicyCookiesConfigTypeDef, _OptionalCachePolicyCookiesConfigTypeDef
):
    pass


_RequiredCachePolicyHeadersConfigTypeDef = TypedDict(
    "_RequiredCachePolicyHeadersConfigTypeDef",
    {
        "HeaderBehavior": CachePolicyHeaderBehaviorType,
    },
)
_OptionalCachePolicyHeadersConfigTypeDef = TypedDict(
    "_OptionalCachePolicyHeadersConfigTypeDef",
    {
        "Headers": "HeadersTypeDef",
    },
    total=False,
)


class CachePolicyHeadersConfigTypeDef(
    _RequiredCachePolicyHeadersConfigTypeDef, _OptionalCachePolicyHeadersConfigTypeDef
):
    pass


_RequiredCachePolicyListTypeDef = TypedDict(
    "_RequiredCachePolicyListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
    },
)
_OptionalCachePolicyListTypeDef = TypedDict(
    "_OptionalCachePolicyListTypeDef",
    {
        "NextMarker": str,
        "Items": List["CachePolicySummaryTypeDef"],
    },
    total=False,
)


class CachePolicyListTypeDef(_RequiredCachePolicyListTypeDef, _OptionalCachePolicyListTypeDef):
    pass


_RequiredCachePolicyQueryStringsConfigTypeDef = TypedDict(
    "_RequiredCachePolicyQueryStringsConfigTypeDef",
    {
        "QueryStringBehavior": CachePolicyQueryStringBehaviorType,
    },
)
_OptionalCachePolicyQueryStringsConfigTypeDef = TypedDict(
    "_OptionalCachePolicyQueryStringsConfigTypeDef",
    {
        "QueryStrings": "QueryStringNamesTypeDef",
    },
    total=False,
)


class CachePolicyQueryStringsConfigTypeDef(
    _RequiredCachePolicyQueryStringsConfigTypeDef, _OptionalCachePolicyQueryStringsConfigTypeDef
):
    pass


CachePolicySummaryTypeDef = TypedDict(
    "CachePolicySummaryTypeDef",
    {
        "Type": CachePolicyTypeType,
        "CachePolicy": "CachePolicyTypeDef",
    },
)

CachePolicyTypeDef = TypedDict(
    "CachePolicyTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "CachePolicyConfig": "CachePolicyConfigTypeDef",
    },
)

CachedMethodsTypeDef = TypedDict(
    "CachedMethodsTypeDef",
    {
        "Quantity": int,
        "Items": List[MethodType],
    },
)

CloudFrontOriginAccessIdentityConfigTypeDef = TypedDict(
    "CloudFrontOriginAccessIdentityConfigTypeDef",
    {
        "CallerReference": str,
        "Comment": str,
    },
)

_RequiredCloudFrontOriginAccessIdentityListTypeDef = TypedDict(
    "_RequiredCloudFrontOriginAccessIdentityListTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
        "IsTruncated": bool,
        "Quantity": int,
    },
)
_OptionalCloudFrontOriginAccessIdentityListTypeDef = TypedDict(
    "_OptionalCloudFrontOriginAccessIdentityListTypeDef",
    {
        "NextMarker": str,
        "Items": List["CloudFrontOriginAccessIdentitySummaryTypeDef"],
    },
    total=False,
)


class CloudFrontOriginAccessIdentityListTypeDef(
    _RequiredCloudFrontOriginAccessIdentityListTypeDef,
    _OptionalCloudFrontOriginAccessIdentityListTypeDef,
):
    pass


CloudFrontOriginAccessIdentitySummaryTypeDef = TypedDict(
    "CloudFrontOriginAccessIdentitySummaryTypeDef",
    {
        "Id": str,
        "S3CanonicalUserId": str,
        "Comment": str,
    },
)

_RequiredCloudFrontOriginAccessIdentityTypeDef = TypedDict(
    "_RequiredCloudFrontOriginAccessIdentityTypeDef",
    {
        "Id": str,
        "S3CanonicalUserId": str,
    },
)
_OptionalCloudFrontOriginAccessIdentityTypeDef = TypedDict(
    "_OptionalCloudFrontOriginAccessIdentityTypeDef",
    {
        "CloudFrontOriginAccessIdentityConfig": "CloudFrontOriginAccessIdentityConfigTypeDef",
    },
    total=False,
)


class CloudFrontOriginAccessIdentityTypeDef(
    _RequiredCloudFrontOriginAccessIdentityTypeDef, _OptionalCloudFrontOriginAccessIdentityTypeDef
):
    pass


_RequiredContentTypeProfileConfigTypeDef = TypedDict(
    "_RequiredContentTypeProfileConfigTypeDef",
    {
        "ForwardWhenContentTypeIsUnknown": bool,
    },
)
_OptionalContentTypeProfileConfigTypeDef = TypedDict(
    "_OptionalContentTypeProfileConfigTypeDef",
    {
        "ContentTypeProfiles": "ContentTypeProfilesTypeDef",
    },
    total=False,
)


class ContentTypeProfileConfigTypeDef(
    _RequiredContentTypeProfileConfigTypeDef, _OptionalContentTypeProfileConfigTypeDef
):
    pass


_RequiredContentTypeProfileTypeDef = TypedDict(
    "_RequiredContentTypeProfileTypeDef",
    {
        "Format": Literal["URLEncoded"],
        "ContentType": str,
    },
)
_OptionalContentTypeProfileTypeDef = TypedDict(
    "_OptionalContentTypeProfileTypeDef",
    {
        "ProfileId": str,
    },
    total=False,
)


class ContentTypeProfileTypeDef(
    _RequiredContentTypeProfileTypeDef, _OptionalContentTypeProfileTypeDef
):
    pass


_RequiredContentTypeProfilesTypeDef = TypedDict(
    "_RequiredContentTypeProfilesTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalContentTypeProfilesTypeDef = TypedDict(
    "_OptionalContentTypeProfilesTypeDef",
    {
        "Items": List["ContentTypeProfileTypeDef"],
    },
    total=False,
)


class ContentTypeProfilesTypeDef(
    _RequiredContentTypeProfilesTypeDef, _OptionalContentTypeProfilesTypeDef
):
    pass


_RequiredCookieNamesTypeDef = TypedDict(
    "_RequiredCookieNamesTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalCookieNamesTypeDef = TypedDict(
    "_OptionalCookieNamesTypeDef",
    {
        "Items": List[str],
    },
    total=False,
)


class CookieNamesTypeDef(_RequiredCookieNamesTypeDef, _OptionalCookieNamesTypeDef):
    pass


_RequiredCookiePreferenceTypeDef = TypedDict(
    "_RequiredCookiePreferenceTypeDef",
    {
        "Forward": ItemSelectionType,
    },
)
_OptionalCookiePreferenceTypeDef = TypedDict(
    "_OptionalCookiePreferenceTypeDef",
    {
        "WhitelistedNames": "CookieNamesTypeDef",
    },
    total=False,
)


class CookiePreferenceTypeDef(_RequiredCookiePreferenceTypeDef, _OptionalCookiePreferenceTypeDef):
    pass


CreateCachePolicyResultTypeDef = TypedDict(
    "CreateCachePolicyResultTypeDef",
    {
        "CachePolicy": "CachePolicyTypeDef",
        "Location": str,
        "ETag": str,
    },
    total=False,
)

CreateCloudFrontOriginAccessIdentityResultTypeDef = TypedDict(
    "CreateCloudFrontOriginAccessIdentityResultTypeDef",
    {
        "CloudFrontOriginAccessIdentity": "CloudFrontOriginAccessIdentityTypeDef",
        "Location": str,
        "ETag": str,
    },
    total=False,
)

CreateDistributionResultTypeDef = TypedDict(
    "CreateDistributionResultTypeDef",
    {
        "Distribution": "DistributionTypeDef",
        "Location": str,
        "ETag": str,
    },
    total=False,
)

CreateDistributionWithTagsResultTypeDef = TypedDict(
    "CreateDistributionWithTagsResultTypeDef",
    {
        "Distribution": "DistributionTypeDef",
        "Location": str,
        "ETag": str,
    },
    total=False,
)

CreateFieldLevelEncryptionConfigResultTypeDef = TypedDict(
    "CreateFieldLevelEncryptionConfigResultTypeDef",
    {
        "FieldLevelEncryption": "FieldLevelEncryptionTypeDef",
        "Location": str,
        "ETag": str,
    },
    total=False,
)

CreateFieldLevelEncryptionProfileResultTypeDef = TypedDict(
    "CreateFieldLevelEncryptionProfileResultTypeDef",
    {
        "FieldLevelEncryptionProfile": "FieldLevelEncryptionProfileTypeDef",
        "Location": str,
        "ETag": str,
    },
    total=False,
)

CreateFunctionResultTypeDef = TypedDict(
    "CreateFunctionResultTypeDef",
    {
        "FunctionSummary": "FunctionSummaryTypeDef",
        "Location": str,
        "ETag": str,
    },
    total=False,
)

CreateInvalidationResultTypeDef = TypedDict(
    "CreateInvalidationResultTypeDef",
    {
        "Location": str,
        "Invalidation": "InvalidationTypeDef",
    },
    total=False,
)

CreateKeyGroupResultTypeDef = TypedDict(
    "CreateKeyGroupResultTypeDef",
    {
        "KeyGroup": "KeyGroupTypeDef",
        "Location": str,
        "ETag": str,
    },
    total=False,
)

CreateMonitoringSubscriptionResultTypeDef = TypedDict(
    "CreateMonitoringSubscriptionResultTypeDef",
    {
        "MonitoringSubscription": "MonitoringSubscriptionTypeDef",
    },
    total=False,
)

CreateOriginRequestPolicyResultTypeDef = TypedDict(
    "CreateOriginRequestPolicyResultTypeDef",
    {
        "OriginRequestPolicy": "OriginRequestPolicyTypeDef",
        "Location": str,
        "ETag": str,
    },
    total=False,
)

CreatePublicKeyResultTypeDef = TypedDict(
    "CreatePublicKeyResultTypeDef",
    {
        "PublicKey": "PublicKeyTypeDef",
        "Location": str,
        "ETag": str,
    },
    total=False,
)

CreateRealtimeLogConfigResultTypeDef = TypedDict(
    "CreateRealtimeLogConfigResultTypeDef",
    {
        "RealtimeLogConfig": "RealtimeLogConfigTypeDef",
    },
    total=False,
)

CreateStreamingDistributionResultTypeDef = TypedDict(
    "CreateStreamingDistributionResultTypeDef",
    {
        "StreamingDistribution": "StreamingDistributionTypeDef",
        "Location": str,
        "ETag": str,
    },
    total=False,
)

CreateStreamingDistributionWithTagsResultTypeDef = TypedDict(
    "CreateStreamingDistributionWithTagsResultTypeDef",
    {
        "StreamingDistribution": "StreamingDistributionTypeDef",
        "Location": str,
        "ETag": str,
    },
    total=False,
)

_RequiredCustomErrorResponseTypeDef = TypedDict(
    "_RequiredCustomErrorResponseTypeDef",
    {
        "ErrorCode": int,
    },
)
_OptionalCustomErrorResponseTypeDef = TypedDict(
    "_OptionalCustomErrorResponseTypeDef",
    {
        "ResponsePagePath": str,
        "ResponseCode": str,
        "ErrorCachingMinTTL": int,
    },
    total=False,
)


class CustomErrorResponseTypeDef(
    _RequiredCustomErrorResponseTypeDef, _OptionalCustomErrorResponseTypeDef
):
    pass


_RequiredCustomErrorResponsesTypeDef = TypedDict(
    "_RequiredCustomErrorResponsesTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalCustomErrorResponsesTypeDef = TypedDict(
    "_OptionalCustomErrorResponsesTypeDef",
    {
        "Items": List["CustomErrorResponseTypeDef"],
    },
    total=False,
)


class CustomErrorResponsesTypeDef(
    _RequiredCustomErrorResponsesTypeDef, _OptionalCustomErrorResponsesTypeDef
):
    pass


_RequiredCustomHeadersTypeDef = TypedDict(
    "_RequiredCustomHeadersTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalCustomHeadersTypeDef = TypedDict(
    "_OptionalCustomHeadersTypeDef",
    {
        "Items": List["OriginCustomHeaderTypeDef"],
    },
    total=False,
)


class CustomHeadersTypeDef(_RequiredCustomHeadersTypeDef, _OptionalCustomHeadersTypeDef):
    pass


_RequiredCustomOriginConfigTypeDef = TypedDict(
    "_RequiredCustomOriginConfigTypeDef",
    {
        "HTTPPort": int,
        "HTTPSPort": int,
        "OriginProtocolPolicy": OriginProtocolPolicyType,
    },
)
_OptionalCustomOriginConfigTypeDef = TypedDict(
    "_OptionalCustomOriginConfigTypeDef",
    {
        "OriginSslProtocols": "OriginSslProtocolsTypeDef",
        "OriginReadTimeout": int,
        "OriginKeepaliveTimeout": int,
    },
    total=False,
)


class CustomOriginConfigTypeDef(
    _RequiredCustomOriginConfigTypeDef, _OptionalCustomOriginConfigTypeDef
):
    pass


_RequiredDefaultCacheBehaviorTypeDef = TypedDict(
    "_RequiredDefaultCacheBehaviorTypeDef",
    {
        "TargetOriginId": str,
        "ViewerProtocolPolicy": ViewerProtocolPolicyType,
    },
)
_OptionalDefaultCacheBehaviorTypeDef = TypedDict(
    "_OptionalDefaultCacheBehaviorTypeDef",
    {
        "TrustedSigners": "TrustedSignersTypeDef",
        "TrustedKeyGroups": "TrustedKeyGroupsTypeDef",
        "AllowedMethods": "AllowedMethodsTypeDef",
        "SmoothStreaming": bool,
        "Compress": bool,
        "LambdaFunctionAssociations": "LambdaFunctionAssociationsTypeDef",
        "FunctionAssociations": "FunctionAssociationsTypeDef",
        "FieldLevelEncryptionId": str,
        "RealtimeLogConfigArn": str,
        "CachePolicyId": str,
        "OriginRequestPolicyId": str,
        "ForwardedValues": "ForwardedValuesTypeDef",
        "MinTTL": int,
        "DefaultTTL": int,
        "MaxTTL": int,
    },
    total=False,
)


class DefaultCacheBehaviorTypeDef(
    _RequiredDefaultCacheBehaviorTypeDef, _OptionalDefaultCacheBehaviorTypeDef
):
    pass


DescribeFunctionResultTypeDef = TypedDict(
    "DescribeFunctionResultTypeDef",
    {
        "FunctionSummary": "FunctionSummaryTypeDef",
        "ETag": str,
    },
    total=False,
)

_RequiredDistributionConfigTypeDef = TypedDict(
    "_RequiredDistributionConfigTypeDef",
    {
        "CallerReference": str,
        "Origins": "OriginsTypeDef",
        "DefaultCacheBehavior": "DefaultCacheBehaviorTypeDef",
        "Comment": str,
        "Enabled": bool,
    },
)
_OptionalDistributionConfigTypeDef = TypedDict(
    "_OptionalDistributionConfigTypeDef",
    {
        "Aliases": "AliasesTypeDef",
        "DefaultRootObject": str,
        "OriginGroups": "OriginGroupsTypeDef",
        "CacheBehaviors": "CacheBehaviorsTypeDef",
        "CustomErrorResponses": "CustomErrorResponsesTypeDef",
        "Logging": "LoggingConfigTypeDef",
        "PriceClass": PriceClassType,
        "ViewerCertificate": "ViewerCertificateTypeDef",
        "Restrictions": "RestrictionsTypeDef",
        "WebACLId": str,
        "HttpVersion": HttpVersionType,
        "IsIPV6Enabled": bool,
    },
    total=False,
)


class DistributionConfigTypeDef(
    _RequiredDistributionConfigTypeDef, _OptionalDistributionConfigTypeDef
):
    pass


DistributionConfigWithTagsTypeDef = TypedDict(
    "DistributionConfigWithTagsTypeDef",
    {
        "DistributionConfig": "DistributionConfigTypeDef",
        "Tags": "TagsTypeDef",
    },
)

_RequiredDistributionIdListTypeDef = TypedDict(
    "_RequiredDistributionIdListTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
        "IsTruncated": bool,
        "Quantity": int,
    },
)
_OptionalDistributionIdListTypeDef = TypedDict(
    "_OptionalDistributionIdListTypeDef",
    {
        "NextMarker": str,
        "Items": List[str],
    },
    total=False,
)


class DistributionIdListTypeDef(
    _RequiredDistributionIdListTypeDef, _OptionalDistributionIdListTypeDef
):
    pass


_RequiredDistributionListTypeDef = TypedDict(
    "_RequiredDistributionListTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
        "IsTruncated": bool,
        "Quantity": int,
    },
)
_OptionalDistributionListTypeDef = TypedDict(
    "_OptionalDistributionListTypeDef",
    {
        "NextMarker": str,
        "Items": List["DistributionSummaryTypeDef"],
    },
    total=False,
)


class DistributionListTypeDef(_RequiredDistributionListTypeDef, _OptionalDistributionListTypeDef):
    pass


_RequiredDistributionSummaryTypeDef = TypedDict(
    "_RequiredDistributionSummaryTypeDef",
    {
        "Id": str,
        "ARN": str,
        "Status": str,
        "LastModifiedTime": datetime,
        "DomainName": str,
        "Aliases": "AliasesTypeDef",
        "Origins": "OriginsTypeDef",
        "DefaultCacheBehavior": "DefaultCacheBehaviorTypeDef",
        "CacheBehaviors": "CacheBehaviorsTypeDef",
        "CustomErrorResponses": "CustomErrorResponsesTypeDef",
        "Comment": str,
        "PriceClass": PriceClassType,
        "Enabled": bool,
        "ViewerCertificate": "ViewerCertificateTypeDef",
        "Restrictions": "RestrictionsTypeDef",
        "WebACLId": str,
        "HttpVersion": HttpVersionType,
        "IsIPV6Enabled": bool,
    },
)
_OptionalDistributionSummaryTypeDef = TypedDict(
    "_OptionalDistributionSummaryTypeDef",
    {
        "OriginGroups": "OriginGroupsTypeDef",
        "AliasICPRecordals": List["AliasICPRecordalTypeDef"],
    },
    total=False,
)


class DistributionSummaryTypeDef(
    _RequiredDistributionSummaryTypeDef, _OptionalDistributionSummaryTypeDef
):
    pass


_RequiredDistributionTypeDef = TypedDict(
    "_RequiredDistributionTypeDef",
    {
        "Id": str,
        "ARN": str,
        "Status": str,
        "LastModifiedTime": datetime,
        "InProgressInvalidationBatches": int,
        "DomainName": str,
        "DistributionConfig": "DistributionConfigTypeDef",
    },
)
_OptionalDistributionTypeDef = TypedDict(
    "_OptionalDistributionTypeDef",
    {
        "ActiveTrustedSigners": "ActiveTrustedSignersTypeDef",
        "ActiveTrustedKeyGroups": "ActiveTrustedKeyGroupsTypeDef",
        "AliasICPRecordals": List["AliasICPRecordalTypeDef"],
    },
    total=False,
)


class DistributionTypeDef(_RequiredDistributionTypeDef, _OptionalDistributionTypeDef):
    pass


_RequiredEncryptionEntitiesTypeDef = TypedDict(
    "_RequiredEncryptionEntitiesTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalEncryptionEntitiesTypeDef = TypedDict(
    "_OptionalEncryptionEntitiesTypeDef",
    {
        "Items": List["EncryptionEntityTypeDef"],
    },
    total=False,
)


class EncryptionEntitiesTypeDef(
    _RequiredEncryptionEntitiesTypeDef, _OptionalEncryptionEntitiesTypeDef
):
    pass


EncryptionEntityTypeDef = TypedDict(
    "EncryptionEntityTypeDef",
    {
        "PublicKeyId": str,
        "ProviderId": str,
        "FieldPatterns": "FieldPatternsTypeDef",
    },
)

_RequiredEndPointTypeDef = TypedDict(
    "_RequiredEndPointTypeDef",
    {
        "StreamType": str,
    },
)
_OptionalEndPointTypeDef = TypedDict(
    "_OptionalEndPointTypeDef",
    {
        "KinesisStreamConfig": "KinesisStreamConfigTypeDef",
    },
    total=False,
)


class EndPointTypeDef(_RequiredEndPointTypeDef, _OptionalEndPointTypeDef):
    pass


_RequiredFieldLevelEncryptionConfigTypeDef = TypedDict(
    "_RequiredFieldLevelEncryptionConfigTypeDef",
    {
        "CallerReference": str,
    },
)
_OptionalFieldLevelEncryptionConfigTypeDef = TypedDict(
    "_OptionalFieldLevelEncryptionConfigTypeDef",
    {
        "Comment": str,
        "QueryArgProfileConfig": "QueryArgProfileConfigTypeDef",
        "ContentTypeProfileConfig": "ContentTypeProfileConfigTypeDef",
    },
    total=False,
)


class FieldLevelEncryptionConfigTypeDef(
    _RequiredFieldLevelEncryptionConfigTypeDef, _OptionalFieldLevelEncryptionConfigTypeDef
):
    pass


_RequiredFieldLevelEncryptionListTypeDef = TypedDict(
    "_RequiredFieldLevelEncryptionListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
    },
)
_OptionalFieldLevelEncryptionListTypeDef = TypedDict(
    "_OptionalFieldLevelEncryptionListTypeDef",
    {
        "NextMarker": str,
        "Items": List["FieldLevelEncryptionSummaryTypeDef"],
    },
    total=False,
)


class FieldLevelEncryptionListTypeDef(
    _RequiredFieldLevelEncryptionListTypeDef, _OptionalFieldLevelEncryptionListTypeDef
):
    pass


_RequiredFieldLevelEncryptionProfileConfigTypeDef = TypedDict(
    "_RequiredFieldLevelEncryptionProfileConfigTypeDef",
    {
        "Name": str,
        "CallerReference": str,
        "EncryptionEntities": "EncryptionEntitiesTypeDef",
    },
)
_OptionalFieldLevelEncryptionProfileConfigTypeDef = TypedDict(
    "_OptionalFieldLevelEncryptionProfileConfigTypeDef",
    {
        "Comment": str,
    },
    total=False,
)


class FieldLevelEncryptionProfileConfigTypeDef(
    _RequiredFieldLevelEncryptionProfileConfigTypeDef,
    _OptionalFieldLevelEncryptionProfileConfigTypeDef,
):
    pass


_RequiredFieldLevelEncryptionProfileListTypeDef = TypedDict(
    "_RequiredFieldLevelEncryptionProfileListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
    },
)
_OptionalFieldLevelEncryptionProfileListTypeDef = TypedDict(
    "_OptionalFieldLevelEncryptionProfileListTypeDef",
    {
        "NextMarker": str,
        "Items": List["FieldLevelEncryptionProfileSummaryTypeDef"],
    },
    total=False,
)


class FieldLevelEncryptionProfileListTypeDef(
    _RequiredFieldLevelEncryptionProfileListTypeDef, _OptionalFieldLevelEncryptionProfileListTypeDef
):
    pass


_RequiredFieldLevelEncryptionProfileSummaryTypeDef = TypedDict(
    "_RequiredFieldLevelEncryptionProfileSummaryTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "Name": str,
        "EncryptionEntities": "EncryptionEntitiesTypeDef",
    },
)
_OptionalFieldLevelEncryptionProfileSummaryTypeDef = TypedDict(
    "_OptionalFieldLevelEncryptionProfileSummaryTypeDef",
    {
        "Comment": str,
    },
    total=False,
)


class FieldLevelEncryptionProfileSummaryTypeDef(
    _RequiredFieldLevelEncryptionProfileSummaryTypeDef,
    _OptionalFieldLevelEncryptionProfileSummaryTypeDef,
):
    pass


FieldLevelEncryptionProfileTypeDef = TypedDict(
    "FieldLevelEncryptionProfileTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "FieldLevelEncryptionProfileConfig": "FieldLevelEncryptionProfileConfigTypeDef",
    },
)

_RequiredFieldLevelEncryptionSummaryTypeDef = TypedDict(
    "_RequiredFieldLevelEncryptionSummaryTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
    },
)
_OptionalFieldLevelEncryptionSummaryTypeDef = TypedDict(
    "_OptionalFieldLevelEncryptionSummaryTypeDef",
    {
        "Comment": str,
        "QueryArgProfileConfig": "QueryArgProfileConfigTypeDef",
        "ContentTypeProfileConfig": "ContentTypeProfileConfigTypeDef",
    },
    total=False,
)


class FieldLevelEncryptionSummaryTypeDef(
    _RequiredFieldLevelEncryptionSummaryTypeDef, _OptionalFieldLevelEncryptionSummaryTypeDef
):
    pass


FieldLevelEncryptionTypeDef = TypedDict(
    "FieldLevelEncryptionTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "FieldLevelEncryptionConfig": "FieldLevelEncryptionConfigTypeDef",
    },
)

_RequiredFieldPatternsTypeDef = TypedDict(
    "_RequiredFieldPatternsTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalFieldPatternsTypeDef = TypedDict(
    "_OptionalFieldPatternsTypeDef",
    {
        "Items": List[str],
    },
    total=False,
)


class FieldPatternsTypeDef(_RequiredFieldPatternsTypeDef, _OptionalFieldPatternsTypeDef):
    pass


_RequiredForwardedValuesTypeDef = TypedDict(
    "_RequiredForwardedValuesTypeDef",
    {
        "QueryString": bool,
        "Cookies": "CookiePreferenceTypeDef",
    },
)
_OptionalForwardedValuesTypeDef = TypedDict(
    "_OptionalForwardedValuesTypeDef",
    {
        "Headers": "HeadersTypeDef",
        "QueryStringCacheKeys": "QueryStringCacheKeysTypeDef",
    },
    total=False,
)


class ForwardedValuesTypeDef(_RequiredForwardedValuesTypeDef, _OptionalForwardedValuesTypeDef):
    pass


FunctionAssociationTypeDef = TypedDict(
    "FunctionAssociationTypeDef",
    {
        "FunctionARN": str,
        "EventType": EventTypeType,
    },
)

_RequiredFunctionAssociationsTypeDef = TypedDict(
    "_RequiredFunctionAssociationsTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalFunctionAssociationsTypeDef = TypedDict(
    "_OptionalFunctionAssociationsTypeDef",
    {
        "Items": List["FunctionAssociationTypeDef"],
    },
    total=False,
)


class FunctionAssociationsTypeDef(
    _RequiredFunctionAssociationsTypeDef, _OptionalFunctionAssociationsTypeDef
):
    pass


FunctionConfigTypeDef = TypedDict(
    "FunctionConfigTypeDef",
    {
        "Comment": str,
        "Runtime": Literal["cloudfront-js-1.0"],
    },
)

_RequiredFunctionListTypeDef = TypedDict(
    "_RequiredFunctionListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
    },
)
_OptionalFunctionListTypeDef = TypedDict(
    "_OptionalFunctionListTypeDef",
    {
        "NextMarker": str,
        "Items": List["FunctionSummaryTypeDef"],
    },
    total=False,
)


class FunctionListTypeDef(_RequiredFunctionListTypeDef, _OptionalFunctionListTypeDef):
    pass


_RequiredFunctionMetadataTypeDef = TypedDict(
    "_RequiredFunctionMetadataTypeDef",
    {
        "FunctionARN": str,
        "LastModifiedTime": datetime,
    },
)
_OptionalFunctionMetadataTypeDef = TypedDict(
    "_OptionalFunctionMetadataTypeDef",
    {
        "Stage": FunctionStageType,
        "CreatedTime": datetime,
    },
    total=False,
)


class FunctionMetadataTypeDef(_RequiredFunctionMetadataTypeDef, _OptionalFunctionMetadataTypeDef):
    pass


_RequiredFunctionSummaryTypeDef = TypedDict(
    "_RequiredFunctionSummaryTypeDef",
    {
        "Name": str,
        "FunctionConfig": "FunctionConfigTypeDef",
        "FunctionMetadata": "FunctionMetadataTypeDef",
    },
)
_OptionalFunctionSummaryTypeDef = TypedDict(
    "_OptionalFunctionSummaryTypeDef",
    {
        "Status": str,
    },
    total=False,
)


class FunctionSummaryTypeDef(_RequiredFunctionSummaryTypeDef, _OptionalFunctionSummaryTypeDef):
    pass


_RequiredGeoRestrictionTypeDef = TypedDict(
    "_RequiredGeoRestrictionTypeDef",
    {
        "RestrictionType": GeoRestrictionTypeType,
        "Quantity": int,
    },
)
_OptionalGeoRestrictionTypeDef = TypedDict(
    "_OptionalGeoRestrictionTypeDef",
    {
        "Items": List[str],
    },
    total=False,
)


class GeoRestrictionTypeDef(_RequiredGeoRestrictionTypeDef, _OptionalGeoRestrictionTypeDef):
    pass


GetCachePolicyConfigResultTypeDef = TypedDict(
    "GetCachePolicyConfigResultTypeDef",
    {
        "CachePolicyConfig": "CachePolicyConfigTypeDef",
        "ETag": str,
    },
    total=False,
)

GetCachePolicyResultTypeDef = TypedDict(
    "GetCachePolicyResultTypeDef",
    {
        "CachePolicy": "CachePolicyTypeDef",
        "ETag": str,
    },
    total=False,
)

GetCloudFrontOriginAccessIdentityConfigResultTypeDef = TypedDict(
    "GetCloudFrontOriginAccessIdentityConfigResultTypeDef",
    {
        "CloudFrontOriginAccessIdentityConfig": "CloudFrontOriginAccessIdentityConfigTypeDef",
        "ETag": str,
    },
    total=False,
)

GetCloudFrontOriginAccessIdentityResultTypeDef = TypedDict(
    "GetCloudFrontOriginAccessIdentityResultTypeDef",
    {
        "CloudFrontOriginAccessIdentity": "CloudFrontOriginAccessIdentityTypeDef",
        "ETag": str,
    },
    total=False,
)

GetDistributionConfigResultTypeDef = TypedDict(
    "GetDistributionConfigResultTypeDef",
    {
        "DistributionConfig": "DistributionConfigTypeDef",
        "ETag": str,
    },
    total=False,
)

GetDistributionResultTypeDef = TypedDict(
    "GetDistributionResultTypeDef",
    {
        "Distribution": "DistributionTypeDef",
        "ETag": str,
    },
    total=False,
)

GetFieldLevelEncryptionConfigResultTypeDef = TypedDict(
    "GetFieldLevelEncryptionConfigResultTypeDef",
    {
        "FieldLevelEncryptionConfig": "FieldLevelEncryptionConfigTypeDef",
        "ETag": str,
    },
    total=False,
)

GetFieldLevelEncryptionProfileConfigResultTypeDef = TypedDict(
    "GetFieldLevelEncryptionProfileConfigResultTypeDef",
    {
        "FieldLevelEncryptionProfileConfig": "FieldLevelEncryptionProfileConfigTypeDef",
        "ETag": str,
    },
    total=False,
)

GetFieldLevelEncryptionProfileResultTypeDef = TypedDict(
    "GetFieldLevelEncryptionProfileResultTypeDef",
    {
        "FieldLevelEncryptionProfile": "FieldLevelEncryptionProfileTypeDef",
        "ETag": str,
    },
    total=False,
)

GetFieldLevelEncryptionResultTypeDef = TypedDict(
    "GetFieldLevelEncryptionResultTypeDef",
    {
        "FieldLevelEncryption": "FieldLevelEncryptionTypeDef",
        "ETag": str,
    },
    total=False,
)

GetFunctionResultTypeDef = TypedDict(
    "GetFunctionResultTypeDef",
    {
        "FunctionCode": Union[bytes, IO[bytes]],
        "ETag": str,
        "ContentType": str,
    },
    total=False,
)

GetInvalidationResultTypeDef = TypedDict(
    "GetInvalidationResultTypeDef",
    {
        "Invalidation": "InvalidationTypeDef",
    },
    total=False,
)

GetKeyGroupConfigResultTypeDef = TypedDict(
    "GetKeyGroupConfigResultTypeDef",
    {
        "KeyGroupConfig": "KeyGroupConfigTypeDef",
        "ETag": str,
    },
    total=False,
)

GetKeyGroupResultTypeDef = TypedDict(
    "GetKeyGroupResultTypeDef",
    {
        "KeyGroup": "KeyGroupTypeDef",
        "ETag": str,
    },
    total=False,
)

GetMonitoringSubscriptionResultTypeDef = TypedDict(
    "GetMonitoringSubscriptionResultTypeDef",
    {
        "MonitoringSubscription": "MonitoringSubscriptionTypeDef",
    },
    total=False,
)

GetOriginRequestPolicyConfigResultTypeDef = TypedDict(
    "GetOriginRequestPolicyConfigResultTypeDef",
    {
        "OriginRequestPolicyConfig": "OriginRequestPolicyConfigTypeDef",
        "ETag": str,
    },
    total=False,
)

GetOriginRequestPolicyResultTypeDef = TypedDict(
    "GetOriginRequestPolicyResultTypeDef",
    {
        "OriginRequestPolicy": "OriginRequestPolicyTypeDef",
        "ETag": str,
    },
    total=False,
)

GetPublicKeyConfigResultTypeDef = TypedDict(
    "GetPublicKeyConfigResultTypeDef",
    {
        "PublicKeyConfig": "PublicKeyConfigTypeDef",
        "ETag": str,
    },
    total=False,
)

GetPublicKeyResultTypeDef = TypedDict(
    "GetPublicKeyResultTypeDef",
    {
        "PublicKey": "PublicKeyTypeDef",
        "ETag": str,
    },
    total=False,
)

GetRealtimeLogConfigResultTypeDef = TypedDict(
    "GetRealtimeLogConfigResultTypeDef",
    {
        "RealtimeLogConfig": "RealtimeLogConfigTypeDef",
    },
    total=False,
)

GetStreamingDistributionConfigResultTypeDef = TypedDict(
    "GetStreamingDistributionConfigResultTypeDef",
    {
        "StreamingDistributionConfig": "StreamingDistributionConfigTypeDef",
        "ETag": str,
    },
    total=False,
)

GetStreamingDistributionResultTypeDef = TypedDict(
    "GetStreamingDistributionResultTypeDef",
    {
        "StreamingDistribution": "StreamingDistributionTypeDef",
        "ETag": str,
    },
    total=False,
)

_RequiredHeadersTypeDef = TypedDict(
    "_RequiredHeadersTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalHeadersTypeDef = TypedDict(
    "_OptionalHeadersTypeDef",
    {
        "Items": List[str],
    },
    total=False,
)


class HeadersTypeDef(_RequiredHeadersTypeDef, _OptionalHeadersTypeDef):
    pass


InvalidationBatchTypeDef = TypedDict(
    "InvalidationBatchTypeDef",
    {
        "Paths": "PathsTypeDef",
        "CallerReference": str,
    },
)

_RequiredInvalidationListTypeDef = TypedDict(
    "_RequiredInvalidationListTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
        "IsTruncated": bool,
        "Quantity": int,
    },
)
_OptionalInvalidationListTypeDef = TypedDict(
    "_OptionalInvalidationListTypeDef",
    {
        "NextMarker": str,
        "Items": List["InvalidationSummaryTypeDef"],
    },
    total=False,
)


class InvalidationListTypeDef(_RequiredInvalidationListTypeDef, _OptionalInvalidationListTypeDef):
    pass


InvalidationSummaryTypeDef = TypedDict(
    "InvalidationSummaryTypeDef",
    {
        "Id": str,
        "CreateTime": datetime,
        "Status": str,
    },
)

InvalidationTypeDef = TypedDict(
    "InvalidationTypeDef",
    {
        "Id": str,
        "Status": str,
        "CreateTime": datetime,
        "InvalidationBatch": "InvalidationBatchTypeDef",
    },
)

KGKeyPairIdsTypeDef = TypedDict(
    "KGKeyPairIdsTypeDef",
    {
        "KeyGroupId": str,
        "KeyPairIds": "KeyPairIdsTypeDef",
    },
    total=False,
)

_RequiredKeyGroupConfigTypeDef = TypedDict(
    "_RequiredKeyGroupConfigTypeDef",
    {
        "Name": str,
        "Items": List[str],
    },
)
_OptionalKeyGroupConfigTypeDef = TypedDict(
    "_OptionalKeyGroupConfigTypeDef",
    {
        "Comment": str,
    },
    total=False,
)


class KeyGroupConfigTypeDef(_RequiredKeyGroupConfigTypeDef, _OptionalKeyGroupConfigTypeDef):
    pass


_RequiredKeyGroupListTypeDef = TypedDict(
    "_RequiredKeyGroupListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
    },
)
_OptionalKeyGroupListTypeDef = TypedDict(
    "_OptionalKeyGroupListTypeDef",
    {
        "NextMarker": str,
        "Items": List["KeyGroupSummaryTypeDef"],
    },
    total=False,
)


class KeyGroupListTypeDef(_RequiredKeyGroupListTypeDef, _OptionalKeyGroupListTypeDef):
    pass


KeyGroupSummaryTypeDef = TypedDict(
    "KeyGroupSummaryTypeDef",
    {
        "KeyGroup": "KeyGroupTypeDef",
    },
)

KeyGroupTypeDef = TypedDict(
    "KeyGroupTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "KeyGroupConfig": "KeyGroupConfigTypeDef",
    },
)

_RequiredKeyPairIdsTypeDef = TypedDict(
    "_RequiredKeyPairIdsTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalKeyPairIdsTypeDef = TypedDict(
    "_OptionalKeyPairIdsTypeDef",
    {
        "Items": List[str],
    },
    total=False,
)


class KeyPairIdsTypeDef(_RequiredKeyPairIdsTypeDef, _OptionalKeyPairIdsTypeDef):
    pass


KinesisStreamConfigTypeDef = TypedDict(
    "KinesisStreamConfigTypeDef",
    {
        "RoleARN": str,
        "StreamARN": str,
    },
)

_RequiredLambdaFunctionAssociationTypeDef = TypedDict(
    "_RequiredLambdaFunctionAssociationTypeDef",
    {
        "LambdaFunctionARN": str,
        "EventType": EventTypeType,
    },
)
_OptionalLambdaFunctionAssociationTypeDef = TypedDict(
    "_OptionalLambdaFunctionAssociationTypeDef",
    {
        "IncludeBody": bool,
    },
    total=False,
)


class LambdaFunctionAssociationTypeDef(
    _RequiredLambdaFunctionAssociationTypeDef, _OptionalLambdaFunctionAssociationTypeDef
):
    pass


_RequiredLambdaFunctionAssociationsTypeDef = TypedDict(
    "_RequiredLambdaFunctionAssociationsTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalLambdaFunctionAssociationsTypeDef = TypedDict(
    "_OptionalLambdaFunctionAssociationsTypeDef",
    {
        "Items": List["LambdaFunctionAssociationTypeDef"],
    },
    total=False,
)


class LambdaFunctionAssociationsTypeDef(
    _RequiredLambdaFunctionAssociationsTypeDef, _OptionalLambdaFunctionAssociationsTypeDef
):
    pass


ListCachePoliciesResultTypeDef = TypedDict(
    "ListCachePoliciesResultTypeDef",
    {
        "CachePolicyList": "CachePolicyListTypeDef",
    },
    total=False,
)

ListCloudFrontOriginAccessIdentitiesResultTypeDef = TypedDict(
    "ListCloudFrontOriginAccessIdentitiesResultTypeDef",
    {
        "CloudFrontOriginAccessIdentityList": "CloudFrontOriginAccessIdentityListTypeDef",
    },
    total=False,
)

ListDistributionsByCachePolicyIdResultTypeDef = TypedDict(
    "ListDistributionsByCachePolicyIdResultTypeDef",
    {
        "DistributionIdList": "DistributionIdListTypeDef",
    },
    total=False,
)

ListDistributionsByKeyGroupResultTypeDef = TypedDict(
    "ListDistributionsByKeyGroupResultTypeDef",
    {
        "DistributionIdList": "DistributionIdListTypeDef",
    },
    total=False,
)

ListDistributionsByOriginRequestPolicyIdResultTypeDef = TypedDict(
    "ListDistributionsByOriginRequestPolicyIdResultTypeDef",
    {
        "DistributionIdList": "DistributionIdListTypeDef",
    },
    total=False,
)

ListDistributionsByRealtimeLogConfigResultTypeDef = TypedDict(
    "ListDistributionsByRealtimeLogConfigResultTypeDef",
    {
        "DistributionList": "DistributionListTypeDef",
    },
    total=False,
)

ListDistributionsByWebACLIdResultTypeDef = TypedDict(
    "ListDistributionsByWebACLIdResultTypeDef",
    {
        "DistributionList": "DistributionListTypeDef",
    },
    total=False,
)

ListDistributionsResultTypeDef = TypedDict(
    "ListDistributionsResultTypeDef",
    {
        "DistributionList": "DistributionListTypeDef",
    },
    total=False,
)

ListFieldLevelEncryptionConfigsResultTypeDef = TypedDict(
    "ListFieldLevelEncryptionConfigsResultTypeDef",
    {
        "FieldLevelEncryptionList": "FieldLevelEncryptionListTypeDef",
    },
    total=False,
)

ListFieldLevelEncryptionProfilesResultTypeDef = TypedDict(
    "ListFieldLevelEncryptionProfilesResultTypeDef",
    {
        "FieldLevelEncryptionProfileList": "FieldLevelEncryptionProfileListTypeDef",
    },
    total=False,
)

ListFunctionsResultTypeDef = TypedDict(
    "ListFunctionsResultTypeDef",
    {
        "FunctionList": "FunctionListTypeDef",
    },
    total=False,
)

ListInvalidationsResultTypeDef = TypedDict(
    "ListInvalidationsResultTypeDef",
    {
        "InvalidationList": "InvalidationListTypeDef",
    },
    total=False,
)

ListKeyGroupsResultTypeDef = TypedDict(
    "ListKeyGroupsResultTypeDef",
    {
        "KeyGroupList": "KeyGroupListTypeDef",
    },
    total=False,
)

ListOriginRequestPoliciesResultTypeDef = TypedDict(
    "ListOriginRequestPoliciesResultTypeDef",
    {
        "OriginRequestPolicyList": "OriginRequestPolicyListTypeDef",
    },
    total=False,
)

ListPublicKeysResultTypeDef = TypedDict(
    "ListPublicKeysResultTypeDef",
    {
        "PublicKeyList": "PublicKeyListTypeDef",
    },
    total=False,
)

ListRealtimeLogConfigsResultTypeDef = TypedDict(
    "ListRealtimeLogConfigsResultTypeDef",
    {
        "RealtimeLogConfigs": "RealtimeLogConfigsTypeDef",
    },
    total=False,
)

ListStreamingDistributionsResultTypeDef = TypedDict(
    "ListStreamingDistributionsResultTypeDef",
    {
        "StreamingDistributionList": "StreamingDistributionListTypeDef",
    },
    total=False,
)

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "Tags": "TagsTypeDef",
    },
)

LoggingConfigTypeDef = TypedDict(
    "LoggingConfigTypeDef",
    {
        "Enabled": bool,
        "IncludeCookies": bool,
        "Bucket": str,
        "Prefix": str,
    },
)

MonitoringSubscriptionTypeDef = TypedDict(
    "MonitoringSubscriptionTypeDef",
    {
        "RealtimeMetricsSubscriptionConfig": "RealtimeMetricsSubscriptionConfigTypeDef",
    },
    total=False,
)

OriginCustomHeaderTypeDef = TypedDict(
    "OriginCustomHeaderTypeDef",
    {
        "HeaderName": str,
        "HeaderValue": str,
    },
)

OriginGroupFailoverCriteriaTypeDef = TypedDict(
    "OriginGroupFailoverCriteriaTypeDef",
    {
        "StatusCodes": "StatusCodesTypeDef",
    },
)

OriginGroupMemberTypeDef = TypedDict(
    "OriginGroupMemberTypeDef",
    {
        "OriginId": str,
    },
)

OriginGroupMembersTypeDef = TypedDict(
    "OriginGroupMembersTypeDef",
    {
        "Quantity": int,
        "Items": List["OriginGroupMemberTypeDef"],
    },
)

OriginGroupTypeDef = TypedDict(
    "OriginGroupTypeDef",
    {
        "Id": str,
        "FailoverCriteria": "OriginGroupFailoverCriteriaTypeDef",
        "Members": "OriginGroupMembersTypeDef",
    },
)

_RequiredOriginGroupsTypeDef = TypedDict(
    "_RequiredOriginGroupsTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalOriginGroupsTypeDef = TypedDict(
    "_OptionalOriginGroupsTypeDef",
    {
        "Items": List["OriginGroupTypeDef"],
    },
    total=False,
)


class OriginGroupsTypeDef(_RequiredOriginGroupsTypeDef, _OptionalOriginGroupsTypeDef):
    pass


_RequiredOriginRequestPolicyConfigTypeDef = TypedDict(
    "_RequiredOriginRequestPolicyConfigTypeDef",
    {
        "Name": str,
        "HeadersConfig": "OriginRequestPolicyHeadersConfigTypeDef",
        "CookiesConfig": "OriginRequestPolicyCookiesConfigTypeDef",
        "QueryStringsConfig": "OriginRequestPolicyQueryStringsConfigTypeDef",
    },
)
_OptionalOriginRequestPolicyConfigTypeDef = TypedDict(
    "_OptionalOriginRequestPolicyConfigTypeDef",
    {
        "Comment": str,
    },
    total=False,
)


class OriginRequestPolicyConfigTypeDef(
    _RequiredOriginRequestPolicyConfigTypeDef, _OptionalOriginRequestPolicyConfigTypeDef
):
    pass


_RequiredOriginRequestPolicyCookiesConfigTypeDef = TypedDict(
    "_RequiredOriginRequestPolicyCookiesConfigTypeDef",
    {
        "CookieBehavior": OriginRequestPolicyCookieBehaviorType,
    },
)
_OptionalOriginRequestPolicyCookiesConfigTypeDef = TypedDict(
    "_OptionalOriginRequestPolicyCookiesConfigTypeDef",
    {
        "Cookies": "CookieNamesTypeDef",
    },
    total=False,
)


class OriginRequestPolicyCookiesConfigTypeDef(
    _RequiredOriginRequestPolicyCookiesConfigTypeDef,
    _OptionalOriginRequestPolicyCookiesConfigTypeDef,
):
    pass


_RequiredOriginRequestPolicyHeadersConfigTypeDef = TypedDict(
    "_RequiredOriginRequestPolicyHeadersConfigTypeDef",
    {
        "HeaderBehavior": OriginRequestPolicyHeaderBehaviorType,
    },
)
_OptionalOriginRequestPolicyHeadersConfigTypeDef = TypedDict(
    "_OptionalOriginRequestPolicyHeadersConfigTypeDef",
    {
        "Headers": "HeadersTypeDef",
    },
    total=False,
)


class OriginRequestPolicyHeadersConfigTypeDef(
    _RequiredOriginRequestPolicyHeadersConfigTypeDef,
    _OptionalOriginRequestPolicyHeadersConfigTypeDef,
):
    pass


_RequiredOriginRequestPolicyListTypeDef = TypedDict(
    "_RequiredOriginRequestPolicyListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
    },
)
_OptionalOriginRequestPolicyListTypeDef = TypedDict(
    "_OptionalOriginRequestPolicyListTypeDef",
    {
        "NextMarker": str,
        "Items": List["OriginRequestPolicySummaryTypeDef"],
    },
    total=False,
)


class OriginRequestPolicyListTypeDef(
    _RequiredOriginRequestPolicyListTypeDef, _OptionalOriginRequestPolicyListTypeDef
):
    pass


_RequiredOriginRequestPolicyQueryStringsConfigTypeDef = TypedDict(
    "_RequiredOriginRequestPolicyQueryStringsConfigTypeDef",
    {
        "QueryStringBehavior": OriginRequestPolicyQueryStringBehaviorType,
    },
)
_OptionalOriginRequestPolicyQueryStringsConfigTypeDef = TypedDict(
    "_OptionalOriginRequestPolicyQueryStringsConfigTypeDef",
    {
        "QueryStrings": "QueryStringNamesTypeDef",
    },
    total=False,
)


class OriginRequestPolicyQueryStringsConfigTypeDef(
    _RequiredOriginRequestPolicyQueryStringsConfigTypeDef,
    _OptionalOriginRequestPolicyQueryStringsConfigTypeDef,
):
    pass


OriginRequestPolicySummaryTypeDef = TypedDict(
    "OriginRequestPolicySummaryTypeDef",
    {
        "Type": OriginRequestPolicyTypeType,
        "OriginRequestPolicy": "OriginRequestPolicyTypeDef",
    },
)

OriginRequestPolicyTypeDef = TypedDict(
    "OriginRequestPolicyTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "OriginRequestPolicyConfig": "OriginRequestPolicyConfigTypeDef",
    },
)

_RequiredOriginShieldTypeDef = TypedDict(
    "_RequiredOriginShieldTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalOriginShieldTypeDef = TypedDict(
    "_OptionalOriginShieldTypeDef",
    {
        "OriginShieldRegion": str,
    },
    total=False,
)


class OriginShieldTypeDef(_RequiredOriginShieldTypeDef, _OptionalOriginShieldTypeDef):
    pass


OriginSslProtocolsTypeDef = TypedDict(
    "OriginSslProtocolsTypeDef",
    {
        "Quantity": int,
        "Items": List[SslProtocolType],
    },
)

_RequiredOriginTypeDef = TypedDict(
    "_RequiredOriginTypeDef",
    {
        "Id": str,
        "DomainName": str,
    },
)
_OptionalOriginTypeDef = TypedDict(
    "_OptionalOriginTypeDef",
    {
        "OriginPath": str,
        "CustomHeaders": "CustomHeadersTypeDef",
        "S3OriginConfig": "S3OriginConfigTypeDef",
        "CustomOriginConfig": "CustomOriginConfigTypeDef",
        "ConnectionAttempts": int,
        "ConnectionTimeout": int,
        "OriginShield": "OriginShieldTypeDef",
    },
    total=False,
)


class OriginTypeDef(_RequiredOriginTypeDef, _OptionalOriginTypeDef):
    pass


OriginsTypeDef = TypedDict(
    "OriginsTypeDef",
    {
        "Quantity": int,
        "Items": List["OriginTypeDef"],
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

_RequiredParametersInCacheKeyAndForwardedToOriginTypeDef = TypedDict(
    "_RequiredParametersInCacheKeyAndForwardedToOriginTypeDef",
    {
        "EnableAcceptEncodingGzip": bool,
        "HeadersConfig": "CachePolicyHeadersConfigTypeDef",
        "CookiesConfig": "CachePolicyCookiesConfigTypeDef",
        "QueryStringsConfig": "CachePolicyQueryStringsConfigTypeDef",
    },
)
_OptionalParametersInCacheKeyAndForwardedToOriginTypeDef = TypedDict(
    "_OptionalParametersInCacheKeyAndForwardedToOriginTypeDef",
    {
        "EnableAcceptEncodingBrotli": bool,
    },
    total=False,
)


class ParametersInCacheKeyAndForwardedToOriginTypeDef(
    _RequiredParametersInCacheKeyAndForwardedToOriginTypeDef,
    _OptionalParametersInCacheKeyAndForwardedToOriginTypeDef,
):
    pass


_RequiredPathsTypeDef = TypedDict(
    "_RequiredPathsTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalPathsTypeDef = TypedDict(
    "_OptionalPathsTypeDef",
    {
        "Items": List[str],
    },
    total=False,
)


class PathsTypeDef(_RequiredPathsTypeDef, _OptionalPathsTypeDef):
    pass


_RequiredPublicKeyConfigTypeDef = TypedDict(
    "_RequiredPublicKeyConfigTypeDef",
    {
        "CallerReference": str,
        "Name": str,
        "EncodedKey": str,
    },
)
_OptionalPublicKeyConfigTypeDef = TypedDict(
    "_OptionalPublicKeyConfigTypeDef",
    {
        "Comment": str,
    },
    total=False,
)


class PublicKeyConfigTypeDef(_RequiredPublicKeyConfigTypeDef, _OptionalPublicKeyConfigTypeDef):
    pass


_RequiredPublicKeyListTypeDef = TypedDict(
    "_RequiredPublicKeyListTypeDef",
    {
        "MaxItems": int,
        "Quantity": int,
    },
)
_OptionalPublicKeyListTypeDef = TypedDict(
    "_OptionalPublicKeyListTypeDef",
    {
        "NextMarker": str,
        "Items": List["PublicKeySummaryTypeDef"],
    },
    total=False,
)


class PublicKeyListTypeDef(_RequiredPublicKeyListTypeDef, _OptionalPublicKeyListTypeDef):
    pass


_RequiredPublicKeySummaryTypeDef = TypedDict(
    "_RequiredPublicKeySummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "CreatedTime": datetime,
        "EncodedKey": str,
    },
)
_OptionalPublicKeySummaryTypeDef = TypedDict(
    "_OptionalPublicKeySummaryTypeDef",
    {
        "Comment": str,
    },
    total=False,
)


class PublicKeySummaryTypeDef(_RequiredPublicKeySummaryTypeDef, _OptionalPublicKeySummaryTypeDef):
    pass


PublicKeyTypeDef = TypedDict(
    "PublicKeyTypeDef",
    {
        "Id": str,
        "CreatedTime": datetime,
        "PublicKeyConfig": "PublicKeyConfigTypeDef",
    },
)

PublishFunctionResultTypeDef = TypedDict(
    "PublishFunctionResultTypeDef",
    {
        "FunctionSummary": "FunctionSummaryTypeDef",
    },
    total=False,
)

_RequiredQueryArgProfileConfigTypeDef = TypedDict(
    "_RequiredQueryArgProfileConfigTypeDef",
    {
        "ForwardWhenQueryArgProfileIsUnknown": bool,
    },
)
_OptionalQueryArgProfileConfigTypeDef = TypedDict(
    "_OptionalQueryArgProfileConfigTypeDef",
    {
        "QueryArgProfiles": "QueryArgProfilesTypeDef",
    },
    total=False,
)


class QueryArgProfileConfigTypeDef(
    _RequiredQueryArgProfileConfigTypeDef, _OptionalQueryArgProfileConfigTypeDef
):
    pass


QueryArgProfileTypeDef = TypedDict(
    "QueryArgProfileTypeDef",
    {
        "QueryArg": str,
        "ProfileId": str,
    },
)

_RequiredQueryArgProfilesTypeDef = TypedDict(
    "_RequiredQueryArgProfilesTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalQueryArgProfilesTypeDef = TypedDict(
    "_OptionalQueryArgProfilesTypeDef",
    {
        "Items": List["QueryArgProfileTypeDef"],
    },
    total=False,
)


class QueryArgProfilesTypeDef(_RequiredQueryArgProfilesTypeDef, _OptionalQueryArgProfilesTypeDef):
    pass


_RequiredQueryStringCacheKeysTypeDef = TypedDict(
    "_RequiredQueryStringCacheKeysTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalQueryStringCacheKeysTypeDef = TypedDict(
    "_OptionalQueryStringCacheKeysTypeDef",
    {
        "Items": List[str],
    },
    total=False,
)


class QueryStringCacheKeysTypeDef(
    _RequiredQueryStringCacheKeysTypeDef, _OptionalQueryStringCacheKeysTypeDef
):
    pass


_RequiredQueryStringNamesTypeDef = TypedDict(
    "_RequiredQueryStringNamesTypeDef",
    {
        "Quantity": int,
    },
)
_OptionalQueryStringNamesTypeDef = TypedDict(
    "_OptionalQueryStringNamesTypeDef",
    {
        "Items": List[str],
    },
    total=False,
)


class QueryStringNamesTypeDef(_RequiredQueryStringNamesTypeDef, _OptionalQueryStringNamesTypeDef):
    pass


RealtimeLogConfigTypeDef = TypedDict(
    "RealtimeLogConfigTypeDef",
    {
        "ARN": str,
        "Name": str,
        "SamplingRate": int,
        "EndPoints": List["EndPointTypeDef"],
        "Fields": List[str],
    },
)

_RequiredRealtimeLogConfigsTypeDef = TypedDict(
    "_RequiredRealtimeLogConfigsTypeDef",
    {
        "MaxItems": int,
        "IsTruncated": bool,
        "Marker": str,
    },
)
_OptionalRealtimeLogConfigsTypeDef = TypedDict(
    "_OptionalRealtimeLogConfigsTypeDef",
    {
        "Items": List["RealtimeLogConfigTypeDef"],
        "NextMarker": str,
    },
    total=False,
)


class RealtimeLogConfigsTypeDef(
    _RequiredRealtimeLogConfigsTypeDef, _OptionalRealtimeLogConfigsTypeDef
):
    pass


RealtimeMetricsSubscriptionConfigTypeDef = TypedDict(
    "RealtimeMetricsSubscriptionConfigTypeDef",
    {
        "RealtimeMetricsSubscriptionStatus": RealtimeMetricsSubscriptionStatusType,
    },
)

RestrictionsTypeDef = TypedDict(
    "RestrictionsTypeDef",
    {
        "GeoRestriction": "GeoRestrictionTypeDef",
    },
)

S3OriginConfigTypeDef = TypedDict(
    "S3OriginConfigTypeDef",
    {
        "OriginAccessIdentity": str,
    },
)

S3OriginTypeDef = TypedDict(
    "S3OriginTypeDef",
    {
        "DomainName": str,
        "OriginAccessIdentity": str,
    },
)

SignerTypeDef = TypedDict(
    "SignerTypeDef",
    {
        "AwsAccountNumber": str,
        "KeyPairIds": "KeyPairIdsTypeDef",
    },
    total=False,
)

StatusCodesTypeDef = TypedDict(
    "StatusCodesTypeDef",
    {
        "Quantity": int,
        "Items": List[int],
    },
)

_RequiredStreamingDistributionConfigTypeDef = TypedDict(
    "_RequiredStreamingDistributionConfigTypeDef",
    {
        "CallerReference": str,
        "S3Origin": "S3OriginTypeDef",
        "Comment": str,
        "TrustedSigners": "TrustedSignersTypeDef",
        "Enabled": bool,
    },
)
_OptionalStreamingDistributionConfigTypeDef = TypedDict(
    "_OptionalStreamingDistributionConfigTypeDef",
    {
        "Aliases": "AliasesTypeDef",
        "Logging": "StreamingLoggingConfigTypeDef",
        "PriceClass": PriceClassType,
    },
    total=False,
)


class StreamingDistributionConfigTypeDef(
    _RequiredStreamingDistributionConfigTypeDef, _OptionalStreamingDistributionConfigTypeDef
):
    pass


StreamingDistributionConfigWithTagsTypeDef = TypedDict(
    "StreamingDistributionConfigWithTagsTypeDef",
    {
        "StreamingDistributionConfig": "StreamingDistributionConfigTypeDef",
        "Tags": "TagsTypeDef",
    },
)

_RequiredStreamingDistributionListTypeDef = TypedDict(
    "_RequiredStreamingDistributionListTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
        "IsTruncated": bool,
        "Quantity": int,
    },
)
_OptionalStreamingDistributionListTypeDef = TypedDict(
    "_OptionalStreamingDistributionListTypeDef",
    {
        "NextMarker": str,
        "Items": List["StreamingDistributionSummaryTypeDef"],
    },
    total=False,
)


class StreamingDistributionListTypeDef(
    _RequiredStreamingDistributionListTypeDef, _OptionalStreamingDistributionListTypeDef
):
    pass


StreamingDistributionSummaryTypeDef = TypedDict(
    "StreamingDistributionSummaryTypeDef",
    {
        "Id": str,
        "ARN": str,
        "Status": str,
        "LastModifiedTime": datetime,
        "DomainName": str,
        "S3Origin": "S3OriginTypeDef",
        "Aliases": "AliasesTypeDef",
        "TrustedSigners": "TrustedSignersTypeDef",
        "Comment": str,
        "PriceClass": PriceClassType,
        "Enabled": bool,
    },
)

_RequiredStreamingDistributionTypeDef = TypedDict(
    "_RequiredStreamingDistributionTypeDef",
    {
        "Id": str,
        "ARN": str,
        "Status": str,
        "DomainName": str,
        "ActiveTrustedSigners": "ActiveTrustedSignersTypeDef",
        "StreamingDistributionConfig": "StreamingDistributionConfigTypeDef",
    },
)
_OptionalStreamingDistributionTypeDef = TypedDict(
    "_OptionalStreamingDistributionTypeDef",
    {
        "LastModifiedTime": datetime,
    },
    total=False,
)


class StreamingDistributionTypeDef(
    _RequiredStreamingDistributionTypeDef, _OptionalStreamingDistributionTypeDef
):
    pass


StreamingLoggingConfigTypeDef = TypedDict(
    "StreamingLoggingConfigTypeDef",
    {
        "Enabled": bool,
        "Bucket": str,
        "Prefix": str,
    },
)

TagKeysTypeDef = TypedDict(
    "TagKeysTypeDef",
    {
        "Items": List[str],
    },
    total=False,
)

_RequiredTagTypeDef = TypedDict(
    "_RequiredTagTypeDef",
    {
        "Key": str,
    },
)
_OptionalTagTypeDef = TypedDict(
    "_OptionalTagTypeDef",
    {
        "Value": str,
    },
    total=False,
)


class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass


TagsTypeDef = TypedDict(
    "TagsTypeDef",
    {
        "Items": List["TagTypeDef"],
    },
    total=False,
)

TestFunctionResultTypeDef = TypedDict(
    "TestFunctionResultTypeDef",
    {
        "TestResult": "TestResultTypeDef",
    },
    total=False,
)

TestResultTypeDef = TypedDict(
    "TestResultTypeDef",
    {
        "FunctionSummary": "FunctionSummaryTypeDef",
        "ComputeUtilization": str,
        "FunctionExecutionLogs": List[str],
        "FunctionErrorMessage": str,
        "FunctionOutput": str,
    },
    total=False,
)

_RequiredTrustedKeyGroupsTypeDef = TypedDict(
    "_RequiredTrustedKeyGroupsTypeDef",
    {
        "Enabled": bool,
        "Quantity": int,
    },
)
_OptionalTrustedKeyGroupsTypeDef = TypedDict(
    "_OptionalTrustedKeyGroupsTypeDef",
    {
        "Items": List[str],
    },
    total=False,
)


class TrustedKeyGroupsTypeDef(_RequiredTrustedKeyGroupsTypeDef, _OptionalTrustedKeyGroupsTypeDef):
    pass


_RequiredTrustedSignersTypeDef = TypedDict(
    "_RequiredTrustedSignersTypeDef",
    {
        "Enabled": bool,
        "Quantity": int,
    },
)
_OptionalTrustedSignersTypeDef = TypedDict(
    "_OptionalTrustedSignersTypeDef",
    {
        "Items": List[str],
    },
    total=False,
)


class TrustedSignersTypeDef(_RequiredTrustedSignersTypeDef, _OptionalTrustedSignersTypeDef):
    pass


UpdateCachePolicyResultTypeDef = TypedDict(
    "UpdateCachePolicyResultTypeDef",
    {
        "CachePolicy": "CachePolicyTypeDef",
        "ETag": str,
    },
    total=False,
)

UpdateCloudFrontOriginAccessIdentityResultTypeDef = TypedDict(
    "UpdateCloudFrontOriginAccessIdentityResultTypeDef",
    {
        "CloudFrontOriginAccessIdentity": "CloudFrontOriginAccessIdentityTypeDef",
        "ETag": str,
    },
    total=False,
)

UpdateDistributionResultTypeDef = TypedDict(
    "UpdateDistributionResultTypeDef",
    {
        "Distribution": "DistributionTypeDef",
        "ETag": str,
    },
    total=False,
)

UpdateFieldLevelEncryptionConfigResultTypeDef = TypedDict(
    "UpdateFieldLevelEncryptionConfigResultTypeDef",
    {
        "FieldLevelEncryption": "FieldLevelEncryptionTypeDef",
        "ETag": str,
    },
    total=False,
)

UpdateFieldLevelEncryptionProfileResultTypeDef = TypedDict(
    "UpdateFieldLevelEncryptionProfileResultTypeDef",
    {
        "FieldLevelEncryptionProfile": "FieldLevelEncryptionProfileTypeDef",
        "ETag": str,
    },
    total=False,
)

UpdateFunctionResultTypeDef = TypedDict(
    "UpdateFunctionResultTypeDef",
    {
        "FunctionSummary": "FunctionSummaryTypeDef",
        "ETag": str,
    },
    total=False,
)

UpdateKeyGroupResultTypeDef = TypedDict(
    "UpdateKeyGroupResultTypeDef",
    {
        "KeyGroup": "KeyGroupTypeDef",
        "ETag": str,
    },
    total=False,
)

UpdateOriginRequestPolicyResultTypeDef = TypedDict(
    "UpdateOriginRequestPolicyResultTypeDef",
    {
        "OriginRequestPolicy": "OriginRequestPolicyTypeDef",
        "ETag": str,
    },
    total=False,
)

UpdatePublicKeyResultTypeDef = TypedDict(
    "UpdatePublicKeyResultTypeDef",
    {
        "PublicKey": "PublicKeyTypeDef",
        "ETag": str,
    },
    total=False,
)

UpdateRealtimeLogConfigResultTypeDef = TypedDict(
    "UpdateRealtimeLogConfigResultTypeDef",
    {
        "RealtimeLogConfig": "RealtimeLogConfigTypeDef",
    },
    total=False,
)

UpdateStreamingDistributionResultTypeDef = TypedDict(
    "UpdateStreamingDistributionResultTypeDef",
    {
        "StreamingDistribution": "StreamingDistributionTypeDef",
        "ETag": str,
    },
    total=False,
)

ViewerCertificateTypeDef = TypedDict(
    "ViewerCertificateTypeDef",
    {
        "CloudFrontDefaultCertificate": bool,
        "IAMCertificateId": str,
        "ACMCertificateArn": str,
        "SSLSupportMethod": SSLSupportMethodType,
        "MinimumProtocolVersion": MinimumProtocolVersionType,
        "Certificate": str,
        "CertificateSource": CertificateSourceType,
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
