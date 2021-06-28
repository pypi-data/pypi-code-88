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
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

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
    "CreateCachePolicyRequestTypeDef",
    "CreateCachePolicyResultResponseTypeDef",
    "CreateCloudFrontOriginAccessIdentityRequestTypeDef",
    "CreateCloudFrontOriginAccessIdentityResultResponseTypeDef",
    "CreateDistributionRequestTypeDef",
    "CreateDistributionResultResponseTypeDef",
    "CreateDistributionWithTagsRequestTypeDef",
    "CreateDistributionWithTagsResultResponseTypeDef",
    "CreateFieldLevelEncryptionConfigRequestTypeDef",
    "CreateFieldLevelEncryptionConfigResultResponseTypeDef",
    "CreateFieldLevelEncryptionProfileRequestTypeDef",
    "CreateFieldLevelEncryptionProfileResultResponseTypeDef",
    "CreateFunctionRequestTypeDef",
    "CreateFunctionResultResponseTypeDef",
    "CreateInvalidationRequestTypeDef",
    "CreateInvalidationResultResponseTypeDef",
    "CreateKeyGroupRequestTypeDef",
    "CreateKeyGroupResultResponseTypeDef",
    "CreateMonitoringSubscriptionRequestTypeDef",
    "CreateMonitoringSubscriptionResultResponseTypeDef",
    "CreateOriginRequestPolicyRequestTypeDef",
    "CreateOriginRequestPolicyResultResponseTypeDef",
    "CreatePublicKeyRequestTypeDef",
    "CreatePublicKeyResultResponseTypeDef",
    "CreateRealtimeLogConfigRequestTypeDef",
    "CreateRealtimeLogConfigResultResponseTypeDef",
    "CreateStreamingDistributionRequestTypeDef",
    "CreateStreamingDistributionResultResponseTypeDef",
    "CreateStreamingDistributionWithTagsRequestTypeDef",
    "CreateStreamingDistributionWithTagsResultResponseTypeDef",
    "CustomErrorResponseTypeDef",
    "CustomErrorResponsesTypeDef",
    "CustomHeadersTypeDef",
    "CustomOriginConfigTypeDef",
    "DefaultCacheBehaviorTypeDef",
    "DeleteCachePolicyRequestTypeDef",
    "DeleteCloudFrontOriginAccessIdentityRequestTypeDef",
    "DeleteDistributionRequestTypeDef",
    "DeleteFieldLevelEncryptionConfigRequestTypeDef",
    "DeleteFieldLevelEncryptionProfileRequestTypeDef",
    "DeleteFunctionRequestTypeDef",
    "DeleteKeyGroupRequestTypeDef",
    "DeleteMonitoringSubscriptionRequestTypeDef",
    "DeleteOriginRequestPolicyRequestTypeDef",
    "DeletePublicKeyRequestTypeDef",
    "DeleteRealtimeLogConfigRequestTypeDef",
    "DeleteStreamingDistributionRequestTypeDef",
    "DescribeFunctionRequestTypeDef",
    "DescribeFunctionResultResponseTypeDef",
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
    "GetCachePolicyConfigRequestTypeDef",
    "GetCachePolicyConfigResultResponseTypeDef",
    "GetCachePolicyRequestTypeDef",
    "GetCachePolicyResultResponseTypeDef",
    "GetCloudFrontOriginAccessIdentityConfigRequestTypeDef",
    "GetCloudFrontOriginAccessIdentityConfigResultResponseTypeDef",
    "GetCloudFrontOriginAccessIdentityRequestTypeDef",
    "GetCloudFrontOriginAccessIdentityResultResponseTypeDef",
    "GetDistributionConfigRequestTypeDef",
    "GetDistributionConfigResultResponseTypeDef",
    "GetDistributionRequestTypeDef",
    "GetDistributionResultResponseTypeDef",
    "GetFieldLevelEncryptionConfigRequestTypeDef",
    "GetFieldLevelEncryptionConfigResultResponseTypeDef",
    "GetFieldLevelEncryptionProfileConfigRequestTypeDef",
    "GetFieldLevelEncryptionProfileConfigResultResponseTypeDef",
    "GetFieldLevelEncryptionProfileRequestTypeDef",
    "GetFieldLevelEncryptionProfileResultResponseTypeDef",
    "GetFieldLevelEncryptionRequestTypeDef",
    "GetFieldLevelEncryptionResultResponseTypeDef",
    "GetFunctionRequestTypeDef",
    "GetFunctionResultResponseTypeDef",
    "GetInvalidationRequestTypeDef",
    "GetInvalidationResultResponseTypeDef",
    "GetKeyGroupConfigRequestTypeDef",
    "GetKeyGroupConfigResultResponseTypeDef",
    "GetKeyGroupRequestTypeDef",
    "GetKeyGroupResultResponseTypeDef",
    "GetMonitoringSubscriptionRequestTypeDef",
    "GetMonitoringSubscriptionResultResponseTypeDef",
    "GetOriginRequestPolicyConfigRequestTypeDef",
    "GetOriginRequestPolicyConfigResultResponseTypeDef",
    "GetOriginRequestPolicyRequestTypeDef",
    "GetOriginRequestPolicyResultResponseTypeDef",
    "GetPublicKeyConfigRequestTypeDef",
    "GetPublicKeyConfigResultResponseTypeDef",
    "GetPublicKeyRequestTypeDef",
    "GetPublicKeyResultResponseTypeDef",
    "GetRealtimeLogConfigRequestTypeDef",
    "GetRealtimeLogConfigResultResponseTypeDef",
    "GetStreamingDistributionConfigRequestTypeDef",
    "GetStreamingDistributionConfigResultResponseTypeDef",
    "GetStreamingDistributionRequestTypeDef",
    "GetStreamingDistributionResultResponseTypeDef",
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
    "ListCachePoliciesRequestTypeDef",
    "ListCachePoliciesResultResponseTypeDef",
    "ListCloudFrontOriginAccessIdentitiesRequestTypeDef",
    "ListCloudFrontOriginAccessIdentitiesResultResponseTypeDef",
    "ListDistributionsByCachePolicyIdRequestTypeDef",
    "ListDistributionsByCachePolicyIdResultResponseTypeDef",
    "ListDistributionsByKeyGroupRequestTypeDef",
    "ListDistributionsByKeyGroupResultResponseTypeDef",
    "ListDistributionsByOriginRequestPolicyIdRequestTypeDef",
    "ListDistributionsByOriginRequestPolicyIdResultResponseTypeDef",
    "ListDistributionsByRealtimeLogConfigRequestTypeDef",
    "ListDistributionsByRealtimeLogConfigResultResponseTypeDef",
    "ListDistributionsByWebACLIdRequestTypeDef",
    "ListDistributionsByWebACLIdResultResponseTypeDef",
    "ListDistributionsRequestTypeDef",
    "ListDistributionsResultResponseTypeDef",
    "ListFieldLevelEncryptionConfigsRequestTypeDef",
    "ListFieldLevelEncryptionConfigsResultResponseTypeDef",
    "ListFieldLevelEncryptionProfilesRequestTypeDef",
    "ListFieldLevelEncryptionProfilesResultResponseTypeDef",
    "ListFunctionsRequestTypeDef",
    "ListFunctionsResultResponseTypeDef",
    "ListInvalidationsRequestTypeDef",
    "ListInvalidationsResultResponseTypeDef",
    "ListKeyGroupsRequestTypeDef",
    "ListKeyGroupsResultResponseTypeDef",
    "ListOriginRequestPoliciesRequestTypeDef",
    "ListOriginRequestPoliciesResultResponseTypeDef",
    "ListPublicKeysRequestTypeDef",
    "ListPublicKeysResultResponseTypeDef",
    "ListRealtimeLogConfigsRequestTypeDef",
    "ListRealtimeLogConfigsResultResponseTypeDef",
    "ListStreamingDistributionsRequestTypeDef",
    "ListStreamingDistributionsResultResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResultResponseTypeDef",
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
    "PublishFunctionRequestTypeDef",
    "PublishFunctionResultResponseTypeDef",
    "QueryArgProfileConfigTypeDef",
    "QueryArgProfileTypeDef",
    "QueryArgProfilesTypeDef",
    "QueryStringCacheKeysTypeDef",
    "QueryStringNamesTypeDef",
    "RealtimeLogConfigTypeDef",
    "RealtimeLogConfigsTypeDef",
    "RealtimeMetricsSubscriptionConfigTypeDef",
    "ResponseMetadataTypeDef",
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
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TagsTypeDef",
    "TestFunctionRequestTypeDef",
    "TestFunctionResultResponseTypeDef",
    "TestResultTypeDef",
    "TrustedKeyGroupsTypeDef",
    "TrustedSignersTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateCachePolicyRequestTypeDef",
    "UpdateCachePolicyResultResponseTypeDef",
    "UpdateCloudFrontOriginAccessIdentityRequestTypeDef",
    "UpdateCloudFrontOriginAccessIdentityResultResponseTypeDef",
    "UpdateDistributionRequestTypeDef",
    "UpdateDistributionResultResponseTypeDef",
    "UpdateFieldLevelEncryptionConfigRequestTypeDef",
    "UpdateFieldLevelEncryptionConfigResultResponseTypeDef",
    "UpdateFieldLevelEncryptionProfileRequestTypeDef",
    "UpdateFieldLevelEncryptionProfileResultResponseTypeDef",
    "UpdateFunctionRequestTypeDef",
    "UpdateFunctionResultResponseTypeDef",
    "UpdateKeyGroupRequestTypeDef",
    "UpdateKeyGroupResultResponseTypeDef",
    "UpdateOriginRequestPolicyRequestTypeDef",
    "UpdateOriginRequestPolicyResultResponseTypeDef",
    "UpdatePublicKeyRequestTypeDef",
    "UpdatePublicKeyResultResponseTypeDef",
    "UpdateRealtimeLogConfigRequestTypeDef",
    "UpdateRealtimeLogConfigResultResponseTypeDef",
    "UpdateStreamingDistributionRequestTypeDef",
    "UpdateStreamingDistributionResultResponseTypeDef",
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


CreateCachePolicyRequestTypeDef = TypedDict(
    "CreateCachePolicyRequestTypeDef",
    {
        "CachePolicyConfig": "CachePolicyConfigTypeDef",
    },
)

CreateCachePolicyResultResponseTypeDef = TypedDict(
    "CreateCachePolicyResultResponseTypeDef",
    {
        "CachePolicy": "CachePolicyTypeDef",
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCloudFrontOriginAccessIdentityRequestTypeDef = TypedDict(
    "CreateCloudFrontOriginAccessIdentityRequestTypeDef",
    {
        "CloudFrontOriginAccessIdentityConfig": "CloudFrontOriginAccessIdentityConfigTypeDef",
    },
)

CreateCloudFrontOriginAccessIdentityResultResponseTypeDef = TypedDict(
    "CreateCloudFrontOriginAccessIdentityResultResponseTypeDef",
    {
        "CloudFrontOriginAccessIdentity": "CloudFrontOriginAccessIdentityTypeDef",
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDistributionRequestTypeDef = TypedDict(
    "CreateDistributionRequestTypeDef",
    {
        "DistributionConfig": "DistributionConfigTypeDef",
    },
)

CreateDistributionResultResponseTypeDef = TypedDict(
    "CreateDistributionResultResponseTypeDef",
    {
        "Distribution": "DistributionTypeDef",
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDistributionWithTagsRequestTypeDef = TypedDict(
    "CreateDistributionWithTagsRequestTypeDef",
    {
        "DistributionConfigWithTags": "DistributionConfigWithTagsTypeDef",
    },
)

CreateDistributionWithTagsResultResponseTypeDef = TypedDict(
    "CreateDistributionWithTagsResultResponseTypeDef",
    {
        "Distribution": "DistributionTypeDef",
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFieldLevelEncryptionConfigRequestTypeDef = TypedDict(
    "CreateFieldLevelEncryptionConfigRequestTypeDef",
    {
        "FieldLevelEncryptionConfig": "FieldLevelEncryptionConfigTypeDef",
    },
)

CreateFieldLevelEncryptionConfigResultResponseTypeDef = TypedDict(
    "CreateFieldLevelEncryptionConfigResultResponseTypeDef",
    {
        "FieldLevelEncryption": "FieldLevelEncryptionTypeDef",
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFieldLevelEncryptionProfileRequestTypeDef = TypedDict(
    "CreateFieldLevelEncryptionProfileRequestTypeDef",
    {
        "FieldLevelEncryptionProfileConfig": "FieldLevelEncryptionProfileConfigTypeDef",
    },
)

CreateFieldLevelEncryptionProfileResultResponseTypeDef = TypedDict(
    "CreateFieldLevelEncryptionProfileResultResponseTypeDef",
    {
        "FieldLevelEncryptionProfile": "FieldLevelEncryptionProfileTypeDef",
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFunctionRequestTypeDef = TypedDict(
    "CreateFunctionRequestTypeDef",
    {
        "Name": str,
        "FunctionConfig": "FunctionConfigTypeDef",
        "FunctionCode": Union[bytes, IO[bytes], StreamingBody],
    },
)

CreateFunctionResultResponseTypeDef = TypedDict(
    "CreateFunctionResultResponseTypeDef",
    {
        "FunctionSummary": "FunctionSummaryTypeDef",
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInvalidationRequestTypeDef = TypedDict(
    "CreateInvalidationRequestTypeDef",
    {
        "DistributionId": str,
        "InvalidationBatch": "InvalidationBatchTypeDef",
    },
)

CreateInvalidationResultResponseTypeDef = TypedDict(
    "CreateInvalidationResultResponseTypeDef",
    {
        "Location": str,
        "Invalidation": "InvalidationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateKeyGroupRequestTypeDef = TypedDict(
    "CreateKeyGroupRequestTypeDef",
    {
        "KeyGroupConfig": "KeyGroupConfigTypeDef",
    },
)

CreateKeyGroupResultResponseTypeDef = TypedDict(
    "CreateKeyGroupResultResponseTypeDef",
    {
        "KeyGroup": "KeyGroupTypeDef",
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMonitoringSubscriptionRequestTypeDef = TypedDict(
    "CreateMonitoringSubscriptionRequestTypeDef",
    {
        "DistributionId": str,
        "MonitoringSubscription": "MonitoringSubscriptionTypeDef",
    },
)

CreateMonitoringSubscriptionResultResponseTypeDef = TypedDict(
    "CreateMonitoringSubscriptionResultResponseTypeDef",
    {
        "MonitoringSubscription": "MonitoringSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateOriginRequestPolicyRequestTypeDef = TypedDict(
    "CreateOriginRequestPolicyRequestTypeDef",
    {
        "OriginRequestPolicyConfig": "OriginRequestPolicyConfigTypeDef",
    },
)

CreateOriginRequestPolicyResultResponseTypeDef = TypedDict(
    "CreateOriginRequestPolicyResultResponseTypeDef",
    {
        "OriginRequestPolicy": "OriginRequestPolicyTypeDef",
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePublicKeyRequestTypeDef = TypedDict(
    "CreatePublicKeyRequestTypeDef",
    {
        "PublicKeyConfig": "PublicKeyConfigTypeDef",
    },
)

CreatePublicKeyResultResponseTypeDef = TypedDict(
    "CreatePublicKeyResultResponseTypeDef",
    {
        "PublicKey": "PublicKeyTypeDef",
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRealtimeLogConfigRequestTypeDef = TypedDict(
    "CreateRealtimeLogConfigRequestTypeDef",
    {
        "EndPoints": List["EndPointTypeDef"],
        "Fields": List[str],
        "Name": str,
        "SamplingRate": int,
    },
)

CreateRealtimeLogConfigResultResponseTypeDef = TypedDict(
    "CreateRealtimeLogConfigResultResponseTypeDef",
    {
        "RealtimeLogConfig": "RealtimeLogConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStreamingDistributionRequestTypeDef = TypedDict(
    "CreateStreamingDistributionRequestTypeDef",
    {
        "StreamingDistributionConfig": "StreamingDistributionConfigTypeDef",
    },
)

CreateStreamingDistributionResultResponseTypeDef = TypedDict(
    "CreateStreamingDistributionResultResponseTypeDef",
    {
        "StreamingDistribution": "StreamingDistributionTypeDef",
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStreamingDistributionWithTagsRequestTypeDef = TypedDict(
    "CreateStreamingDistributionWithTagsRequestTypeDef",
    {
        "StreamingDistributionConfigWithTags": "StreamingDistributionConfigWithTagsTypeDef",
    },
)

CreateStreamingDistributionWithTagsResultResponseTypeDef = TypedDict(
    "CreateStreamingDistributionWithTagsResultResponseTypeDef",
    {
        "StreamingDistribution": "StreamingDistributionTypeDef",
        "Location": str,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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


_RequiredDeleteCachePolicyRequestTypeDef = TypedDict(
    "_RequiredDeleteCachePolicyRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalDeleteCachePolicyRequestTypeDef = TypedDict(
    "_OptionalDeleteCachePolicyRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)


class DeleteCachePolicyRequestTypeDef(
    _RequiredDeleteCachePolicyRequestTypeDef, _OptionalDeleteCachePolicyRequestTypeDef
):
    pass


_RequiredDeleteCloudFrontOriginAccessIdentityRequestTypeDef = TypedDict(
    "_RequiredDeleteCloudFrontOriginAccessIdentityRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalDeleteCloudFrontOriginAccessIdentityRequestTypeDef = TypedDict(
    "_OptionalDeleteCloudFrontOriginAccessIdentityRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)


class DeleteCloudFrontOriginAccessIdentityRequestTypeDef(
    _RequiredDeleteCloudFrontOriginAccessIdentityRequestTypeDef,
    _OptionalDeleteCloudFrontOriginAccessIdentityRequestTypeDef,
):
    pass


_RequiredDeleteDistributionRequestTypeDef = TypedDict(
    "_RequiredDeleteDistributionRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalDeleteDistributionRequestTypeDef = TypedDict(
    "_OptionalDeleteDistributionRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)


class DeleteDistributionRequestTypeDef(
    _RequiredDeleteDistributionRequestTypeDef, _OptionalDeleteDistributionRequestTypeDef
):
    pass


_RequiredDeleteFieldLevelEncryptionConfigRequestTypeDef = TypedDict(
    "_RequiredDeleteFieldLevelEncryptionConfigRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalDeleteFieldLevelEncryptionConfigRequestTypeDef = TypedDict(
    "_OptionalDeleteFieldLevelEncryptionConfigRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)


class DeleteFieldLevelEncryptionConfigRequestTypeDef(
    _RequiredDeleteFieldLevelEncryptionConfigRequestTypeDef,
    _OptionalDeleteFieldLevelEncryptionConfigRequestTypeDef,
):
    pass


_RequiredDeleteFieldLevelEncryptionProfileRequestTypeDef = TypedDict(
    "_RequiredDeleteFieldLevelEncryptionProfileRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalDeleteFieldLevelEncryptionProfileRequestTypeDef = TypedDict(
    "_OptionalDeleteFieldLevelEncryptionProfileRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)


class DeleteFieldLevelEncryptionProfileRequestTypeDef(
    _RequiredDeleteFieldLevelEncryptionProfileRequestTypeDef,
    _OptionalDeleteFieldLevelEncryptionProfileRequestTypeDef,
):
    pass


DeleteFunctionRequestTypeDef = TypedDict(
    "DeleteFunctionRequestTypeDef",
    {
        "Name": str,
        "IfMatch": str,
    },
)

_RequiredDeleteKeyGroupRequestTypeDef = TypedDict(
    "_RequiredDeleteKeyGroupRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalDeleteKeyGroupRequestTypeDef = TypedDict(
    "_OptionalDeleteKeyGroupRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)


class DeleteKeyGroupRequestTypeDef(
    _RequiredDeleteKeyGroupRequestTypeDef, _OptionalDeleteKeyGroupRequestTypeDef
):
    pass


DeleteMonitoringSubscriptionRequestTypeDef = TypedDict(
    "DeleteMonitoringSubscriptionRequestTypeDef",
    {
        "DistributionId": str,
    },
)

_RequiredDeleteOriginRequestPolicyRequestTypeDef = TypedDict(
    "_RequiredDeleteOriginRequestPolicyRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalDeleteOriginRequestPolicyRequestTypeDef = TypedDict(
    "_OptionalDeleteOriginRequestPolicyRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)


class DeleteOriginRequestPolicyRequestTypeDef(
    _RequiredDeleteOriginRequestPolicyRequestTypeDef,
    _OptionalDeleteOriginRequestPolicyRequestTypeDef,
):
    pass


_RequiredDeletePublicKeyRequestTypeDef = TypedDict(
    "_RequiredDeletePublicKeyRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalDeletePublicKeyRequestTypeDef = TypedDict(
    "_OptionalDeletePublicKeyRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)


class DeletePublicKeyRequestTypeDef(
    _RequiredDeletePublicKeyRequestTypeDef, _OptionalDeletePublicKeyRequestTypeDef
):
    pass


DeleteRealtimeLogConfigRequestTypeDef = TypedDict(
    "DeleteRealtimeLogConfigRequestTypeDef",
    {
        "Name": str,
        "ARN": str,
    },
    total=False,
)

_RequiredDeleteStreamingDistributionRequestTypeDef = TypedDict(
    "_RequiredDeleteStreamingDistributionRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalDeleteStreamingDistributionRequestTypeDef = TypedDict(
    "_OptionalDeleteStreamingDistributionRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)


class DeleteStreamingDistributionRequestTypeDef(
    _RequiredDeleteStreamingDistributionRequestTypeDef,
    _OptionalDeleteStreamingDistributionRequestTypeDef,
):
    pass


_RequiredDescribeFunctionRequestTypeDef = TypedDict(
    "_RequiredDescribeFunctionRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalDescribeFunctionRequestTypeDef = TypedDict(
    "_OptionalDescribeFunctionRequestTypeDef",
    {
        "Stage": FunctionStageType,
    },
    total=False,
)


class DescribeFunctionRequestTypeDef(
    _RequiredDescribeFunctionRequestTypeDef, _OptionalDescribeFunctionRequestTypeDef
):
    pass


DescribeFunctionResultResponseTypeDef = TypedDict(
    "DescribeFunctionResultResponseTypeDef",
    {
        "FunctionSummary": "FunctionSummaryTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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


GetCachePolicyConfigRequestTypeDef = TypedDict(
    "GetCachePolicyConfigRequestTypeDef",
    {
        "Id": str,
    },
)

GetCachePolicyConfigResultResponseTypeDef = TypedDict(
    "GetCachePolicyConfigResultResponseTypeDef",
    {
        "CachePolicyConfig": "CachePolicyConfigTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCachePolicyRequestTypeDef = TypedDict(
    "GetCachePolicyRequestTypeDef",
    {
        "Id": str,
    },
)

GetCachePolicyResultResponseTypeDef = TypedDict(
    "GetCachePolicyResultResponseTypeDef",
    {
        "CachePolicy": "CachePolicyTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCloudFrontOriginAccessIdentityConfigRequestTypeDef = TypedDict(
    "GetCloudFrontOriginAccessIdentityConfigRequestTypeDef",
    {
        "Id": str,
    },
)

GetCloudFrontOriginAccessIdentityConfigResultResponseTypeDef = TypedDict(
    "GetCloudFrontOriginAccessIdentityConfigResultResponseTypeDef",
    {
        "CloudFrontOriginAccessIdentityConfig": "CloudFrontOriginAccessIdentityConfigTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCloudFrontOriginAccessIdentityRequestTypeDef = TypedDict(
    "GetCloudFrontOriginAccessIdentityRequestTypeDef",
    {
        "Id": str,
    },
)

GetCloudFrontOriginAccessIdentityResultResponseTypeDef = TypedDict(
    "GetCloudFrontOriginAccessIdentityResultResponseTypeDef",
    {
        "CloudFrontOriginAccessIdentity": "CloudFrontOriginAccessIdentityTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDistributionConfigRequestTypeDef = TypedDict(
    "GetDistributionConfigRequestTypeDef",
    {
        "Id": str,
    },
)

GetDistributionConfigResultResponseTypeDef = TypedDict(
    "GetDistributionConfigResultResponseTypeDef",
    {
        "DistributionConfig": "DistributionConfigTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDistributionRequestTypeDef = TypedDict(
    "GetDistributionRequestTypeDef",
    {
        "Id": str,
    },
)

GetDistributionResultResponseTypeDef = TypedDict(
    "GetDistributionResultResponseTypeDef",
    {
        "Distribution": "DistributionTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFieldLevelEncryptionConfigRequestTypeDef = TypedDict(
    "GetFieldLevelEncryptionConfigRequestTypeDef",
    {
        "Id": str,
    },
)

GetFieldLevelEncryptionConfigResultResponseTypeDef = TypedDict(
    "GetFieldLevelEncryptionConfigResultResponseTypeDef",
    {
        "FieldLevelEncryptionConfig": "FieldLevelEncryptionConfigTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFieldLevelEncryptionProfileConfigRequestTypeDef = TypedDict(
    "GetFieldLevelEncryptionProfileConfigRequestTypeDef",
    {
        "Id": str,
    },
)

GetFieldLevelEncryptionProfileConfigResultResponseTypeDef = TypedDict(
    "GetFieldLevelEncryptionProfileConfigResultResponseTypeDef",
    {
        "FieldLevelEncryptionProfileConfig": "FieldLevelEncryptionProfileConfigTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFieldLevelEncryptionProfileRequestTypeDef = TypedDict(
    "GetFieldLevelEncryptionProfileRequestTypeDef",
    {
        "Id": str,
    },
)

GetFieldLevelEncryptionProfileResultResponseTypeDef = TypedDict(
    "GetFieldLevelEncryptionProfileResultResponseTypeDef",
    {
        "FieldLevelEncryptionProfile": "FieldLevelEncryptionProfileTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFieldLevelEncryptionRequestTypeDef = TypedDict(
    "GetFieldLevelEncryptionRequestTypeDef",
    {
        "Id": str,
    },
)

GetFieldLevelEncryptionResultResponseTypeDef = TypedDict(
    "GetFieldLevelEncryptionResultResponseTypeDef",
    {
        "FieldLevelEncryption": "FieldLevelEncryptionTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFunctionRequestTypeDef = TypedDict(
    "_RequiredGetFunctionRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalGetFunctionRequestTypeDef = TypedDict(
    "_OptionalGetFunctionRequestTypeDef",
    {
        "Stage": FunctionStageType,
    },
    total=False,
)


class GetFunctionRequestTypeDef(
    _RequiredGetFunctionRequestTypeDef, _OptionalGetFunctionRequestTypeDef
):
    pass


GetFunctionResultResponseTypeDef = TypedDict(
    "GetFunctionResultResponseTypeDef",
    {
        "FunctionCode": bytes,
        "ETag": str,
        "ContentType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInvalidationRequestTypeDef = TypedDict(
    "GetInvalidationRequestTypeDef",
    {
        "DistributionId": str,
        "Id": str,
    },
)

GetInvalidationResultResponseTypeDef = TypedDict(
    "GetInvalidationResultResponseTypeDef",
    {
        "Invalidation": "InvalidationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetKeyGroupConfigRequestTypeDef = TypedDict(
    "GetKeyGroupConfigRequestTypeDef",
    {
        "Id": str,
    },
)

GetKeyGroupConfigResultResponseTypeDef = TypedDict(
    "GetKeyGroupConfigResultResponseTypeDef",
    {
        "KeyGroupConfig": "KeyGroupConfigTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetKeyGroupRequestTypeDef = TypedDict(
    "GetKeyGroupRequestTypeDef",
    {
        "Id": str,
    },
)

GetKeyGroupResultResponseTypeDef = TypedDict(
    "GetKeyGroupResultResponseTypeDef",
    {
        "KeyGroup": "KeyGroupTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMonitoringSubscriptionRequestTypeDef = TypedDict(
    "GetMonitoringSubscriptionRequestTypeDef",
    {
        "DistributionId": str,
    },
)

GetMonitoringSubscriptionResultResponseTypeDef = TypedDict(
    "GetMonitoringSubscriptionResultResponseTypeDef",
    {
        "MonitoringSubscription": "MonitoringSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOriginRequestPolicyConfigRequestTypeDef = TypedDict(
    "GetOriginRequestPolicyConfigRequestTypeDef",
    {
        "Id": str,
    },
)

GetOriginRequestPolicyConfigResultResponseTypeDef = TypedDict(
    "GetOriginRequestPolicyConfigResultResponseTypeDef",
    {
        "OriginRequestPolicyConfig": "OriginRequestPolicyConfigTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOriginRequestPolicyRequestTypeDef = TypedDict(
    "GetOriginRequestPolicyRequestTypeDef",
    {
        "Id": str,
    },
)

GetOriginRequestPolicyResultResponseTypeDef = TypedDict(
    "GetOriginRequestPolicyResultResponseTypeDef",
    {
        "OriginRequestPolicy": "OriginRequestPolicyTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPublicKeyConfigRequestTypeDef = TypedDict(
    "GetPublicKeyConfigRequestTypeDef",
    {
        "Id": str,
    },
)

GetPublicKeyConfigResultResponseTypeDef = TypedDict(
    "GetPublicKeyConfigResultResponseTypeDef",
    {
        "PublicKeyConfig": "PublicKeyConfigTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPublicKeyRequestTypeDef = TypedDict(
    "GetPublicKeyRequestTypeDef",
    {
        "Id": str,
    },
)

GetPublicKeyResultResponseTypeDef = TypedDict(
    "GetPublicKeyResultResponseTypeDef",
    {
        "PublicKey": "PublicKeyTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRealtimeLogConfigRequestTypeDef = TypedDict(
    "GetRealtimeLogConfigRequestTypeDef",
    {
        "Name": str,
        "ARN": str,
    },
    total=False,
)

GetRealtimeLogConfigResultResponseTypeDef = TypedDict(
    "GetRealtimeLogConfigResultResponseTypeDef",
    {
        "RealtimeLogConfig": "RealtimeLogConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStreamingDistributionConfigRequestTypeDef = TypedDict(
    "GetStreamingDistributionConfigRequestTypeDef",
    {
        "Id": str,
    },
)

GetStreamingDistributionConfigResultResponseTypeDef = TypedDict(
    "GetStreamingDistributionConfigResultResponseTypeDef",
    {
        "StreamingDistributionConfig": "StreamingDistributionConfigTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStreamingDistributionRequestTypeDef = TypedDict(
    "GetStreamingDistributionRequestTypeDef",
    {
        "Id": str,
    },
)

GetStreamingDistributionResultResponseTypeDef = TypedDict(
    "GetStreamingDistributionResultResponseTypeDef",
    {
        "StreamingDistribution": "StreamingDistributionTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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


ListCachePoliciesRequestTypeDef = TypedDict(
    "ListCachePoliciesRequestTypeDef",
    {
        "Type": CachePolicyTypeType,
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)

ListCachePoliciesResultResponseTypeDef = TypedDict(
    "ListCachePoliciesResultResponseTypeDef",
    {
        "CachePolicyList": "CachePolicyListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCloudFrontOriginAccessIdentitiesRequestTypeDef = TypedDict(
    "ListCloudFrontOriginAccessIdentitiesRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)

ListCloudFrontOriginAccessIdentitiesResultResponseTypeDef = TypedDict(
    "ListCloudFrontOriginAccessIdentitiesResultResponseTypeDef",
    {
        "CloudFrontOriginAccessIdentityList": "CloudFrontOriginAccessIdentityListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDistributionsByCachePolicyIdRequestTypeDef = TypedDict(
    "_RequiredListDistributionsByCachePolicyIdRequestTypeDef",
    {
        "CachePolicyId": str,
    },
)
_OptionalListDistributionsByCachePolicyIdRequestTypeDef = TypedDict(
    "_OptionalListDistributionsByCachePolicyIdRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)


class ListDistributionsByCachePolicyIdRequestTypeDef(
    _RequiredListDistributionsByCachePolicyIdRequestTypeDef,
    _OptionalListDistributionsByCachePolicyIdRequestTypeDef,
):
    pass


ListDistributionsByCachePolicyIdResultResponseTypeDef = TypedDict(
    "ListDistributionsByCachePolicyIdResultResponseTypeDef",
    {
        "DistributionIdList": "DistributionIdListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDistributionsByKeyGroupRequestTypeDef = TypedDict(
    "_RequiredListDistributionsByKeyGroupRequestTypeDef",
    {
        "KeyGroupId": str,
    },
)
_OptionalListDistributionsByKeyGroupRequestTypeDef = TypedDict(
    "_OptionalListDistributionsByKeyGroupRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)


class ListDistributionsByKeyGroupRequestTypeDef(
    _RequiredListDistributionsByKeyGroupRequestTypeDef,
    _OptionalListDistributionsByKeyGroupRequestTypeDef,
):
    pass


ListDistributionsByKeyGroupResultResponseTypeDef = TypedDict(
    "ListDistributionsByKeyGroupResultResponseTypeDef",
    {
        "DistributionIdList": "DistributionIdListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDistributionsByOriginRequestPolicyIdRequestTypeDef = TypedDict(
    "_RequiredListDistributionsByOriginRequestPolicyIdRequestTypeDef",
    {
        "OriginRequestPolicyId": str,
    },
)
_OptionalListDistributionsByOriginRequestPolicyIdRequestTypeDef = TypedDict(
    "_OptionalListDistributionsByOriginRequestPolicyIdRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)


class ListDistributionsByOriginRequestPolicyIdRequestTypeDef(
    _RequiredListDistributionsByOriginRequestPolicyIdRequestTypeDef,
    _OptionalListDistributionsByOriginRequestPolicyIdRequestTypeDef,
):
    pass


ListDistributionsByOriginRequestPolicyIdResultResponseTypeDef = TypedDict(
    "ListDistributionsByOriginRequestPolicyIdResultResponseTypeDef",
    {
        "DistributionIdList": "DistributionIdListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDistributionsByRealtimeLogConfigRequestTypeDef = TypedDict(
    "ListDistributionsByRealtimeLogConfigRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
        "RealtimeLogConfigName": str,
        "RealtimeLogConfigArn": str,
    },
    total=False,
)

ListDistributionsByRealtimeLogConfigResultResponseTypeDef = TypedDict(
    "ListDistributionsByRealtimeLogConfigResultResponseTypeDef",
    {
        "DistributionList": "DistributionListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDistributionsByWebACLIdRequestTypeDef = TypedDict(
    "_RequiredListDistributionsByWebACLIdRequestTypeDef",
    {
        "WebACLId": str,
    },
)
_OptionalListDistributionsByWebACLIdRequestTypeDef = TypedDict(
    "_OptionalListDistributionsByWebACLIdRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)


class ListDistributionsByWebACLIdRequestTypeDef(
    _RequiredListDistributionsByWebACLIdRequestTypeDef,
    _OptionalListDistributionsByWebACLIdRequestTypeDef,
):
    pass


ListDistributionsByWebACLIdResultResponseTypeDef = TypedDict(
    "ListDistributionsByWebACLIdResultResponseTypeDef",
    {
        "DistributionList": "DistributionListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDistributionsRequestTypeDef = TypedDict(
    "ListDistributionsRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)

ListDistributionsResultResponseTypeDef = TypedDict(
    "ListDistributionsResultResponseTypeDef",
    {
        "DistributionList": "DistributionListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFieldLevelEncryptionConfigsRequestTypeDef = TypedDict(
    "ListFieldLevelEncryptionConfigsRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)

ListFieldLevelEncryptionConfigsResultResponseTypeDef = TypedDict(
    "ListFieldLevelEncryptionConfigsResultResponseTypeDef",
    {
        "FieldLevelEncryptionList": "FieldLevelEncryptionListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFieldLevelEncryptionProfilesRequestTypeDef = TypedDict(
    "ListFieldLevelEncryptionProfilesRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)

ListFieldLevelEncryptionProfilesResultResponseTypeDef = TypedDict(
    "ListFieldLevelEncryptionProfilesResultResponseTypeDef",
    {
        "FieldLevelEncryptionProfileList": "FieldLevelEncryptionProfileListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFunctionsRequestTypeDef = TypedDict(
    "ListFunctionsRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
        "Stage": FunctionStageType,
    },
    total=False,
)

ListFunctionsResultResponseTypeDef = TypedDict(
    "ListFunctionsResultResponseTypeDef",
    {
        "FunctionList": "FunctionListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListInvalidationsRequestTypeDef = TypedDict(
    "_RequiredListInvalidationsRequestTypeDef",
    {
        "DistributionId": str,
    },
)
_OptionalListInvalidationsRequestTypeDef = TypedDict(
    "_OptionalListInvalidationsRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)


class ListInvalidationsRequestTypeDef(
    _RequiredListInvalidationsRequestTypeDef, _OptionalListInvalidationsRequestTypeDef
):
    pass


ListInvalidationsResultResponseTypeDef = TypedDict(
    "ListInvalidationsResultResponseTypeDef",
    {
        "InvalidationList": "InvalidationListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListKeyGroupsRequestTypeDef = TypedDict(
    "ListKeyGroupsRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)

ListKeyGroupsResultResponseTypeDef = TypedDict(
    "ListKeyGroupsResultResponseTypeDef",
    {
        "KeyGroupList": "KeyGroupListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOriginRequestPoliciesRequestTypeDef = TypedDict(
    "ListOriginRequestPoliciesRequestTypeDef",
    {
        "Type": OriginRequestPolicyTypeType,
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)

ListOriginRequestPoliciesResultResponseTypeDef = TypedDict(
    "ListOriginRequestPoliciesResultResponseTypeDef",
    {
        "OriginRequestPolicyList": "OriginRequestPolicyListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPublicKeysRequestTypeDef = TypedDict(
    "ListPublicKeysRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)

ListPublicKeysResultResponseTypeDef = TypedDict(
    "ListPublicKeysResultResponseTypeDef",
    {
        "PublicKeyList": "PublicKeyListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRealtimeLogConfigsRequestTypeDef = TypedDict(
    "ListRealtimeLogConfigsRequestTypeDef",
    {
        "MaxItems": str,
        "Marker": str,
    },
    total=False,
)

ListRealtimeLogConfigsResultResponseTypeDef = TypedDict(
    "ListRealtimeLogConfigsResultResponseTypeDef",
    {
        "RealtimeLogConfigs": "RealtimeLogConfigsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStreamingDistributionsRequestTypeDef = TypedDict(
    "ListStreamingDistributionsRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)

ListStreamingDistributionsResultResponseTypeDef = TypedDict(
    "ListStreamingDistributionsResultResponseTypeDef",
    {
        "StreamingDistributionList": "StreamingDistributionListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "Resource": str,
    },
)

ListTagsForResourceResultResponseTypeDef = TypedDict(
    "ListTagsForResourceResultResponseTypeDef",
    {
        "Tags": "TagsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

PublishFunctionRequestTypeDef = TypedDict(
    "PublishFunctionRequestTypeDef",
    {
        "Name": str,
        "IfMatch": str,
    },
)

PublishFunctionResultResponseTypeDef = TypedDict(
    "PublishFunctionResultResponseTypeDef",
    {
        "FunctionSummary": "FunctionSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "Resource": str,
        "Tags": "TagsTypeDef",
    },
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

_RequiredTestFunctionRequestTypeDef = TypedDict(
    "_RequiredTestFunctionRequestTypeDef",
    {
        "Name": str,
        "IfMatch": str,
        "EventObject": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalTestFunctionRequestTypeDef = TypedDict(
    "_OptionalTestFunctionRequestTypeDef",
    {
        "Stage": FunctionStageType,
    },
    total=False,
)


class TestFunctionRequestTypeDef(
    _RequiredTestFunctionRequestTypeDef, _OptionalTestFunctionRequestTypeDef
):
    pass


TestFunctionResultResponseTypeDef = TypedDict(
    "TestFunctionResultResponseTypeDef",
    {
        "TestResult": "TestResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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


UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "Resource": str,
        "TagKeys": "TagKeysTypeDef",
    },
)

_RequiredUpdateCachePolicyRequestTypeDef = TypedDict(
    "_RequiredUpdateCachePolicyRequestTypeDef",
    {
        "CachePolicyConfig": "CachePolicyConfigTypeDef",
        "Id": str,
    },
)
_OptionalUpdateCachePolicyRequestTypeDef = TypedDict(
    "_OptionalUpdateCachePolicyRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)


class UpdateCachePolicyRequestTypeDef(
    _RequiredUpdateCachePolicyRequestTypeDef, _OptionalUpdateCachePolicyRequestTypeDef
):
    pass


UpdateCachePolicyResultResponseTypeDef = TypedDict(
    "UpdateCachePolicyResultResponseTypeDef",
    {
        "CachePolicy": "CachePolicyTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateCloudFrontOriginAccessIdentityRequestTypeDef = TypedDict(
    "_RequiredUpdateCloudFrontOriginAccessIdentityRequestTypeDef",
    {
        "CloudFrontOriginAccessIdentityConfig": "CloudFrontOriginAccessIdentityConfigTypeDef",
        "Id": str,
    },
)
_OptionalUpdateCloudFrontOriginAccessIdentityRequestTypeDef = TypedDict(
    "_OptionalUpdateCloudFrontOriginAccessIdentityRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)


class UpdateCloudFrontOriginAccessIdentityRequestTypeDef(
    _RequiredUpdateCloudFrontOriginAccessIdentityRequestTypeDef,
    _OptionalUpdateCloudFrontOriginAccessIdentityRequestTypeDef,
):
    pass


UpdateCloudFrontOriginAccessIdentityResultResponseTypeDef = TypedDict(
    "UpdateCloudFrontOriginAccessIdentityResultResponseTypeDef",
    {
        "CloudFrontOriginAccessIdentity": "CloudFrontOriginAccessIdentityTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDistributionRequestTypeDef = TypedDict(
    "_RequiredUpdateDistributionRequestTypeDef",
    {
        "DistributionConfig": "DistributionConfigTypeDef",
        "Id": str,
    },
)
_OptionalUpdateDistributionRequestTypeDef = TypedDict(
    "_OptionalUpdateDistributionRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)


class UpdateDistributionRequestTypeDef(
    _RequiredUpdateDistributionRequestTypeDef, _OptionalUpdateDistributionRequestTypeDef
):
    pass


UpdateDistributionResultResponseTypeDef = TypedDict(
    "UpdateDistributionResultResponseTypeDef",
    {
        "Distribution": "DistributionTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFieldLevelEncryptionConfigRequestTypeDef = TypedDict(
    "_RequiredUpdateFieldLevelEncryptionConfigRequestTypeDef",
    {
        "FieldLevelEncryptionConfig": "FieldLevelEncryptionConfigTypeDef",
        "Id": str,
    },
)
_OptionalUpdateFieldLevelEncryptionConfigRequestTypeDef = TypedDict(
    "_OptionalUpdateFieldLevelEncryptionConfigRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)


class UpdateFieldLevelEncryptionConfigRequestTypeDef(
    _RequiredUpdateFieldLevelEncryptionConfigRequestTypeDef,
    _OptionalUpdateFieldLevelEncryptionConfigRequestTypeDef,
):
    pass


UpdateFieldLevelEncryptionConfigResultResponseTypeDef = TypedDict(
    "UpdateFieldLevelEncryptionConfigResultResponseTypeDef",
    {
        "FieldLevelEncryption": "FieldLevelEncryptionTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFieldLevelEncryptionProfileRequestTypeDef = TypedDict(
    "_RequiredUpdateFieldLevelEncryptionProfileRequestTypeDef",
    {
        "FieldLevelEncryptionProfileConfig": "FieldLevelEncryptionProfileConfigTypeDef",
        "Id": str,
    },
)
_OptionalUpdateFieldLevelEncryptionProfileRequestTypeDef = TypedDict(
    "_OptionalUpdateFieldLevelEncryptionProfileRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)


class UpdateFieldLevelEncryptionProfileRequestTypeDef(
    _RequiredUpdateFieldLevelEncryptionProfileRequestTypeDef,
    _OptionalUpdateFieldLevelEncryptionProfileRequestTypeDef,
):
    pass


UpdateFieldLevelEncryptionProfileResultResponseTypeDef = TypedDict(
    "UpdateFieldLevelEncryptionProfileResultResponseTypeDef",
    {
        "FieldLevelEncryptionProfile": "FieldLevelEncryptionProfileTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFunctionRequestTypeDef = TypedDict(
    "UpdateFunctionRequestTypeDef",
    {
        "Name": str,
        "IfMatch": str,
        "FunctionConfig": "FunctionConfigTypeDef",
        "FunctionCode": Union[bytes, IO[bytes], StreamingBody],
    },
)

UpdateFunctionResultResponseTypeDef = TypedDict(
    "UpdateFunctionResultResponseTypeDef",
    {
        "FunctionSummary": "FunctionSummaryTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateKeyGroupRequestTypeDef = TypedDict(
    "_RequiredUpdateKeyGroupRequestTypeDef",
    {
        "KeyGroupConfig": "KeyGroupConfigTypeDef",
        "Id": str,
    },
)
_OptionalUpdateKeyGroupRequestTypeDef = TypedDict(
    "_OptionalUpdateKeyGroupRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)


class UpdateKeyGroupRequestTypeDef(
    _RequiredUpdateKeyGroupRequestTypeDef, _OptionalUpdateKeyGroupRequestTypeDef
):
    pass


UpdateKeyGroupResultResponseTypeDef = TypedDict(
    "UpdateKeyGroupResultResponseTypeDef",
    {
        "KeyGroup": "KeyGroupTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateOriginRequestPolicyRequestTypeDef = TypedDict(
    "_RequiredUpdateOriginRequestPolicyRequestTypeDef",
    {
        "OriginRequestPolicyConfig": "OriginRequestPolicyConfigTypeDef",
        "Id": str,
    },
)
_OptionalUpdateOriginRequestPolicyRequestTypeDef = TypedDict(
    "_OptionalUpdateOriginRequestPolicyRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)


class UpdateOriginRequestPolicyRequestTypeDef(
    _RequiredUpdateOriginRequestPolicyRequestTypeDef,
    _OptionalUpdateOriginRequestPolicyRequestTypeDef,
):
    pass


UpdateOriginRequestPolicyResultResponseTypeDef = TypedDict(
    "UpdateOriginRequestPolicyResultResponseTypeDef",
    {
        "OriginRequestPolicy": "OriginRequestPolicyTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePublicKeyRequestTypeDef = TypedDict(
    "_RequiredUpdatePublicKeyRequestTypeDef",
    {
        "PublicKeyConfig": "PublicKeyConfigTypeDef",
        "Id": str,
    },
)
_OptionalUpdatePublicKeyRequestTypeDef = TypedDict(
    "_OptionalUpdatePublicKeyRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)


class UpdatePublicKeyRequestTypeDef(
    _RequiredUpdatePublicKeyRequestTypeDef, _OptionalUpdatePublicKeyRequestTypeDef
):
    pass


UpdatePublicKeyResultResponseTypeDef = TypedDict(
    "UpdatePublicKeyResultResponseTypeDef",
    {
        "PublicKey": "PublicKeyTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRealtimeLogConfigRequestTypeDef = TypedDict(
    "UpdateRealtimeLogConfigRequestTypeDef",
    {
        "EndPoints": List["EndPointTypeDef"],
        "Fields": List[str],
        "Name": str,
        "ARN": str,
        "SamplingRate": int,
    },
    total=False,
)

UpdateRealtimeLogConfigResultResponseTypeDef = TypedDict(
    "UpdateRealtimeLogConfigResultResponseTypeDef",
    {
        "RealtimeLogConfig": "RealtimeLogConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateStreamingDistributionRequestTypeDef = TypedDict(
    "_RequiredUpdateStreamingDistributionRequestTypeDef",
    {
        "StreamingDistributionConfig": "StreamingDistributionConfigTypeDef",
        "Id": str,
    },
)
_OptionalUpdateStreamingDistributionRequestTypeDef = TypedDict(
    "_OptionalUpdateStreamingDistributionRequestTypeDef",
    {
        "IfMatch": str,
    },
    total=False,
)


class UpdateStreamingDistributionRequestTypeDef(
    _RequiredUpdateStreamingDistributionRequestTypeDef,
    _OptionalUpdateStreamingDistributionRequestTypeDef,
):
    pass


UpdateStreamingDistributionResultResponseTypeDef = TypedDict(
    "UpdateStreamingDistributionResultResponseTypeDef",
    {
        "StreamingDistribution": "StreamingDistributionTypeDef",
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
