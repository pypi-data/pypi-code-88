"""
Type annotations for appmesh service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/type_defs.html)

Usage::

    ```python
    from mypy_boto3_appmesh.type_defs import AccessLogTypeDef

    data: AccessLogTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    DefaultGatewayRouteRewriteType,
    DnsResponseTypeType,
    DurationUnitType,
    EgressFilterTypeType,
    GatewayRouteStatusCodeType,
    GrpcRetryPolicyEventType,
    HttpMethodType,
    HttpSchemeType,
    ListenerTlsModeType,
    MeshStatusCodeType,
    PortProtocolType,
    RouteStatusCodeType,
    VirtualGatewayListenerTlsModeType,
    VirtualGatewayPortProtocolType,
    VirtualGatewayStatusCodeType,
    VirtualNodeStatusCodeType,
    VirtualRouterStatusCodeType,
    VirtualServiceStatusCodeType,
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
    "AccessLogTypeDef",
    "AwsCloudMapInstanceAttributeTypeDef",
    "AwsCloudMapServiceDiscoveryTypeDef",
    "BackendDefaultsTypeDef",
    "BackendTypeDef",
    "ClientPolicyTlsTypeDef",
    "ClientPolicyTypeDef",
    "ClientTlsCertificateTypeDef",
    "CreateGatewayRouteInputTypeDef",
    "CreateGatewayRouteOutputResponseTypeDef",
    "CreateMeshInputTypeDef",
    "CreateMeshOutputResponseTypeDef",
    "CreateRouteInputTypeDef",
    "CreateRouteOutputResponseTypeDef",
    "CreateVirtualGatewayInputTypeDef",
    "CreateVirtualGatewayOutputResponseTypeDef",
    "CreateVirtualNodeInputTypeDef",
    "CreateVirtualNodeOutputResponseTypeDef",
    "CreateVirtualRouterInputTypeDef",
    "CreateVirtualRouterOutputResponseTypeDef",
    "CreateVirtualServiceInputTypeDef",
    "CreateVirtualServiceOutputResponseTypeDef",
    "DeleteGatewayRouteInputTypeDef",
    "DeleteGatewayRouteOutputResponseTypeDef",
    "DeleteMeshInputTypeDef",
    "DeleteMeshOutputResponseTypeDef",
    "DeleteRouteInputTypeDef",
    "DeleteRouteOutputResponseTypeDef",
    "DeleteVirtualGatewayInputTypeDef",
    "DeleteVirtualGatewayOutputResponseTypeDef",
    "DeleteVirtualNodeInputTypeDef",
    "DeleteVirtualNodeOutputResponseTypeDef",
    "DeleteVirtualRouterInputTypeDef",
    "DeleteVirtualRouterOutputResponseTypeDef",
    "DeleteVirtualServiceInputTypeDef",
    "DeleteVirtualServiceOutputResponseTypeDef",
    "DescribeGatewayRouteInputTypeDef",
    "DescribeGatewayRouteOutputResponseTypeDef",
    "DescribeMeshInputTypeDef",
    "DescribeMeshOutputResponseTypeDef",
    "DescribeRouteInputTypeDef",
    "DescribeRouteOutputResponseTypeDef",
    "DescribeVirtualGatewayInputTypeDef",
    "DescribeVirtualGatewayOutputResponseTypeDef",
    "DescribeVirtualNodeInputTypeDef",
    "DescribeVirtualNodeOutputResponseTypeDef",
    "DescribeVirtualRouterInputTypeDef",
    "DescribeVirtualRouterOutputResponseTypeDef",
    "DescribeVirtualServiceInputTypeDef",
    "DescribeVirtualServiceOutputResponseTypeDef",
    "DnsServiceDiscoveryTypeDef",
    "DurationTypeDef",
    "EgressFilterTypeDef",
    "FileAccessLogTypeDef",
    "GatewayRouteDataTypeDef",
    "GatewayRouteHostnameMatchTypeDef",
    "GatewayRouteHostnameRewriteTypeDef",
    "GatewayRouteRefTypeDef",
    "GatewayRouteSpecTypeDef",
    "GatewayRouteStatusTypeDef",
    "GatewayRouteTargetTypeDef",
    "GatewayRouteVirtualServiceTypeDef",
    "GrpcGatewayRouteActionTypeDef",
    "GrpcGatewayRouteMatchTypeDef",
    "GrpcGatewayRouteMetadataTypeDef",
    "GrpcGatewayRouteRewriteTypeDef",
    "GrpcGatewayRouteTypeDef",
    "GrpcMetadataMatchMethodTypeDef",
    "GrpcRetryPolicyTypeDef",
    "GrpcRouteActionTypeDef",
    "GrpcRouteMatchTypeDef",
    "GrpcRouteMetadataMatchMethodTypeDef",
    "GrpcRouteMetadataTypeDef",
    "GrpcRouteTypeDef",
    "GrpcTimeoutTypeDef",
    "HeaderMatchMethodTypeDef",
    "HealthCheckPolicyTypeDef",
    "HttpGatewayRouteActionTypeDef",
    "HttpGatewayRouteHeaderTypeDef",
    "HttpGatewayRouteMatchTypeDef",
    "HttpGatewayRoutePathRewriteTypeDef",
    "HttpGatewayRoutePrefixRewriteTypeDef",
    "HttpGatewayRouteRewriteTypeDef",
    "HttpGatewayRouteTypeDef",
    "HttpPathMatchTypeDef",
    "HttpQueryParameterTypeDef",
    "HttpRetryPolicyTypeDef",
    "HttpRouteActionTypeDef",
    "HttpRouteHeaderTypeDef",
    "HttpRouteMatchTypeDef",
    "HttpRouteTypeDef",
    "HttpTimeoutTypeDef",
    "ListGatewayRoutesInputTypeDef",
    "ListGatewayRoutesOutputResponseTypeDef",
    "ListMeshesInputTypeDef",
    "ListMeshesOutputResponseTypeDef",
    "ListRoutesInputTypeDef",
    "ListRoutesOutputResponseTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputResponseTypeDef",
    "ListVirtualGatewaysInputTypeDef",
    "ListVirtualGatewaysOutputResponseTypeDef",
    "ListVirtualNodesInputTypeDef",
    "ListVirtualNodesOutputResponseTypeDef",
    "ListVirtualRoutersInputTypeDef",
    "ListVirtualRoutersOutputResponseTypeDef",
    "ListVirtualServicesInputTypeDef",
    "ListVirtualServicesOutputResponseTypeDef",
    "ListenerTimeoutTypeDef",
    "ListenerTlsAcmCertificateTypeDef",
    "ListenerTlsCertificateTypeDef",
    "ListenerTlsFileCertificateTypeDef",
    "ListenerTlsSdsCertificateTypeDef",
    "ListenerTlsTypeDef",
    "ListenerTlsValidationContextTrustTypeDef",
    "ListenerTlsValidationContextTypeDef",
    "ListenerTypeDef",
    "LoggingTypeDef",
    "MatchRangeTypeDef",
    "MeshDataTypeDef",
    "MeshRefTypeDef",
    "MeshSpecTypeDef",
    "MeshStatusTypeDef",
    "OutlierDetectionTypeDef",
    "PaginatorConfigTypeDef",
    "PortMappingTypeDef",
    "QueryParameterMatchTypeDef",
    "ResourceMetadataTypeDef",
    "ResponseMetadataTypeDef",
    "RouteDataTypeDef",
    "RouteRefTypeDef",
    "RouteSpecTypeDef",
    "RouteStatusTypeDef",
    "ServiceDiscoveryTypeDef",
    "SubjectAlternativeNameMatchersTypeDef",
    "SubjectAlternativeNamesTypeDef",
    "TagRefTypeDef",
    "TagResourceInputTypeDef",
    "TcpRouteActionTypeDef",
    "TcpRouteTypeDef",
    "TcpTimeoutTypeDef",
    "TlsValidationContextAcmTrustTypeDef",
    "TlsValidationContextFileTrustTypeDef",
    "TlsValidationContextSdsTrustTypeDef",
    "TlsValidationContextTrustTypeDef",
    "TlsValidationContextTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateGatewayRouteInputTypeDef",
    "UpdateGatewayRouteOutputResponseTypeDef",
    "UpdateMeshInputTypeDef",
    "UpdateMeshOutputResponseTypeDef",
    "UpdateRouteInputTypeDef",
    "UpdateRouteOutputResponseTypeDef",
    "UpdateVirtualGatewayInputTypeDef",
    "UpdateVirtualGatewayOutputResponseTypeDef",
    "UpdateVirtualNodeInputTypeDef",
    "UpdateVirtualNodeOutputResponseTypeDef",
    "UpdateVirtualRouterInputTypeDef",
    "UpdateVirtualRouterOutputResponseTypeDef",
    "UpdateVirtualServiceInputTypeDef",
    "UpdateVirtualServiceOutputResponseTypeDef",
    "VirtualGatewayAccessLogTypeDef",
    "VirtualGatewayBackendDefaultsTypeDef",
    "VirtualGatewayClientPolicyTlsTypeDef",
    "VirtualGatewayClientPolicyTypeDef",
    "VirtualGatewayClientTlsCertificateTypeDef",
    "VirtualGatewayConnectionPoolTypeDef",
    "VirtualGatewayDataTypeDef",
    "VirtualGatewayFileAccessLogTypeDef",
    "VirtualGatewayGrpcConnectionPoolTypeDef",
    "VirtualGatewayHealthCheckPolicyTypeDef",
    "VirtualGatewayHttp2ConnectionPoolTypeDef",
    "VirtualGatewayHttpConnectionPoolTypeDef",
    "VirtualGatewayListenerTlsAcmCertificateTypeDef",
    "VirtualGatewayListenerTlsCertificateTypeDef",
    "VirtualGatewayListenerTlsFileCertificateTypeDef",
    "VirtualGatewayListenerTlsSdsCertificateTypeDef",
    "VirtualGatewayListenerTlsTypeDef",
    "VirtualGatewayListenerTlsValidationContextTrustTypeDef",
    "VirtualGatewayListenerTlsValidationContextTypeDef",
    "VirtualGatewayListenerTypeDef",
    "VirtualGatewayLoggingTypeDef",
    "VirtualGatewayPortMappingTypeDef",
    "VirtualGatewayRefTypeDef",
    "VirtualGatewaySpecTypeDef",
    "VirtualGatewayStatusTypeDef",
    "VirtualGatewayTlsValidationContextAcmTrustTypeDef",
    "VirtualGatewayTlsValidationContextFileTrustTypeDef",
    "VirtualGatewayTlsValidationContextSdsTrustTypeDef",
    "VirtualGatewayTlsValidationContextTrustTypeDef",
    "VirtualGatewayTlsValidationContextTypeDef",
    "VirtualNodeConnectionPoolTypeDef",
    "VirtualNodeDataTypeDef",
    "VirtualNodeGrpcConnectionPoolTypeDef",
    "VirtualNodeHttp2ConnectionPoolTypeDef",
    "VirtualNodeHttpConnectionPoolTypeDef",
    "VirtualNodeRefTypeDef",
    "VirtualNodeServiceProviderTypeDef",
    "VirtualNodeSpecTypeDef",
    "VirtualNodeStatusTypeDef",
    "VirtualNodeTcpConnectionPoolTypeDef",
    "VirtualRouterDataTypeDef",
    "VirtualRouterListenerTypeDef",
    "VirtualRouterRefTypeDef",
    "VirtualRouterServiceProviderTypeDef",
    "VirtualRouterSpecTypeDef",
    "VirtualRouterStatusTypeDef",
    "VirtualServiceBackendTypeDef",
    "VirtualServiceDataTypeDef",
    "VirtualServiceProviderTypeDef",
    "VirtualServiceRefTypeDef",
    "VirtualServiceSpecTypeDef",
    "VirtualServiceStatusTypeDef",
    "WeightedTargetTypeDef",
)

AccessLogTypeDef = TypedDict(
    "AccessLogTypeDef",
    {
        "file": "FileAccessLogTypeDef",
    },
    total=False,
)

AwsCloudMapInstanceAttributeTypeDef = TypedDict(
    "AwsCloudMapInstanceAttributeTypeDef",
    {
        "key": str,
        "value": str,
    },
)

_RequiredAwsCloudMapServiceDiscoveryTypeDef = TypedDict(
    "_RequiredAwsCloudMapServiceDiscoveryTypeDef",
    {
        "namespaceName": str,
        "serviceName": str,
    },
)
_OptionalAwsCloudMapServiceDiscoveryTypeDef = TypedDict(
    "_OptionalAwsCloudMapServiceDiscoveryTypeDef",
    {
        "attributes": List["AwsCloudMapInstanceAttributeTypeDef"],
    },
    total=False,
)


class AwsCloudMapServiceDiscoveryTypeDef(
    _RequiredAwsCloudMapServiceDiscoveryTypeDef, _OptionalAwsCloudMapServiceDiscoveryTypeDef
):
    pass


BackendDefaultsTypeDef = TypedDict(
    "BackendDefaultsTypeDef",
    {
        "clientPolicy": "ClientPolicyTypeDef",
    },
    total=False,
)

BackendTypeDef = TypedDict(
    "BackendTypeDef",
    {
        "virtualService": "VirtualServiceBackendTypeDef",
    },
    total=False,
)

_RequiredClientPolicyTlsTypeDef = TypedDict(
    "_RequiredClientPolicyTlsTypeDef",
    {
        "validation": "TlsValidationContextTypeDef",
    },
)
_OptionalClientPolicyTlsTypeDef = TypedDict(
    "_OptionalClientPolicyTlsTypeDef",
    {
        "certificate": "ClientTlsCertificateTypeDef",
        "enforce": bool,
        "ports": List[int],
    },
    total=False,
)


class ClientPolicyTlsTypeDef(_RequiredClientPolicyTlsTypeDef, _OptionalClientPolicyTlsTypeDef):
    pass


ClientPolicyTypeDef = TypedDict(
    "ClientPolicyTypeDef",
    {
        "tls": "ClientPolicyTlsTypeDef",
    },
    total=False,
)

ClientTlsCertificateTypeDef = TypedDict(
    "ClientTlsCertificateTypeDef",
    {
        "file": "ListenerTlsFileCertificateTypeDef",
        "sds": "ListenerTlsSdsCertificateTypeDef",
    },
    total=False,
)

_RequiredCreateGatewayRouteInputTypeDef = TypedDict(
    "_RequiredCreateGatewayRouteInputTypeDef",
    {
        "gatewayRouteName": str,
        "meshName": str,
        "spec": "GatewayRouteSpecTypeDef",
        "virtualGatewayName": str,
    },
)
_OptionalCreateGatewayRouteInputTypeDef = TypedDict(
    "_OptionalCreateGatewayRouteInputTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
        "tags": List["TagRefTypeDef"],
    },
    total=False,
)


class CreateGatewayRouteInputTypeDef(
    _RequiredCreateGatewayRouteInputTypeDef, _OptionalCreateGatewayRouteInputTypeDef
):
    pass


CreateGatewayRouteOutputResponseTypeDef = TypedDict(
    "CreateGatewayRouteOutputResponseTypeDef",
    {
        "gatewayRoute": "GatewayRouteDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMeshInputTypeDef = TypedDict(
    "_RequiredCreateMeshInputTypeDef",
    {
        "meshName": str,
    },
)
_OptionalCreateMeshInputTypeDef = TypedDict(
    "_OptionalCreateMeshInputTypeDef",
    {
        "clientToken": str,
        "spec": "MeshSpecTypeDef",
        "tags": List["TagRefTypeDef"],
    },
    total=False,
)


class CreateMeshInputTypeDef(_RequiredCreateMeshInputTypeDef, _OptionalCreateMeshInputTypeDef):
    pass


CreateMeshOutputResponseTypeDef = TypedDict(
    "CreateMeshOutputResponseTypeDef",
    {
        "mesh": "MeshDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRouteInputTypeDef = TypedDict(
    "_RequiredCreateRouteInputTypeDef",
    {
        "meshName": str,
        "routeName": str,
        "spec": "RouteSpecTypeDef",
        "virtualRouterName": str,
    },
)
_OptionalCreateRouteInputTypeDef = TypedDict(
    "_OptionalCreateRouteInputTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
        "tags": List["TagRefTypeDef"],
    },
    total=False,
)


class CreateRouteInputTypeDef(_RequiredCreateRouteInputTypeDef, _OptionalCreateRouteInputTypeDef):
    pass


CreateRouteOutputResponseTypeDef = TypedDict(
    "CreateRouteOutputResponseTypeDef",
    {
        "route": "RouteDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVirtualGatewayInputTypeDef = TypedDict(
    "_RequiredCreateVirtualGatewayInputTypeDef",
    {
        "meshName": str,
        "spec": "VirtualGatewaySpecTypeDef",
        "virtualGatewayName": str,
    },
)
_OptionalCreateVirtualGatewayInputTypeDef = TypedDict(
    "_OptionalCreateVirtualGatewayInputTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
        "tags": List["TagRefTypeDef"],
    },
    total=False,
)


class CreateVirtualGatewayInputTypeDef(
    _RequiredCreateVirtualGatewayInputTypeDef, _OptionalCreateVirtualGatewayInputTypeDef
):
    pass


CreateVirtualGatewayOutputResponseTypeDef = TypedDict(
    "CreateVirtualGatewayOutputResponseTypeDef",
    {
        "virtualGateway": "VirtualGatewayDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVirtualNodeInputTypeDef = TypedDict(
    "_RequiredCreateVirtualNodeInputTypeDef",
    {
        "meshName": str,
        "spec": "VirtualNodeSpecTypeDef",
        "virtualNodeName": str,
    },
)
_OptionalCreateVirtualNodeInputTypeDef = TypedDict(
    "_OptionalCreateVirtualNodeInputTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
        "tags": List["TagRefTypeDef"],
    },
    total=False,
)


class CreateVirtualNodeInputTypeDef(
    _RequiredCreateVirtualNodeInputTypeDef, _OptionalCreateVirtualNodeInputTypeDef
):
    pass


CreateVirtualNodeOutputResponseTypeDef = TypedDict(
    "CreateVirtualNodeOutputResponseTypeDef",
    {
        "virtualNode": "VirtualNodeDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVirtualRouterInputTypeDef = TypedDict(
    "_RequiredCreateVirtualRouterInputTypeDef",
    {
        "meshName": str,
        "spec": "VirtualRouterSpecTypeDef",
        "virtualRouterName": str,
    },
)
_OptionalCreateVirtualRouterInputTypeDef = TypedDict(
    "_OptionalCreateVirtualRouterInputTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
        "tags": List["TagRefTypeDef"],
    },
    total=False,
)


class CreateVirtualRouterInputTypeDef(
    _RequiredCreateVirtualRouterInputTypeDef, _OptionalCreateVirtualRouterInputTypeDef
):
    pass


CreateVirtualRouterOutputResponseTypeDef = TypedDict(
    "CreateVirtualRouterOutputResponseTypeDef",
    {
        "virtualRouter": "VirtualRouterDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVirtualServiceInputTypeDef = TypedDict(
    "_RequiredCreateVirtualServiceInputTypeDef",
    {
        "meshName": str,
        "spec": "VirtualServiceSpecTypeDef",
        "virtualServiceName": str,
    },
)
_OptionalCreateVirtualServiceInputTypeDef = TypedDict(
    "_OptionalCreateVirtualServiceInputTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
        "tags": List["TagRefTypeDef"],
    },
    total=False,
)


class CreateVirtualServiceInputTypeDef(
    _RequiredCreateVirtualServiceInputTypeDef, _OptionalCreateVirtualServiceInputTypeDef
):
    pass


CreateVirtualServiceOutputResponseTypeDef = TypedDict(
    "CreateVirtualServiceOutputResponseTypeDef",
    {
        "virtualService": "VirtualServiceDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteGatewayRouteInputTypeDef = TypedDict(
    "_RequiredDeleteGatewayRouteInputTypeDef",
    {
        "gatewayRouteName": str,
        "meshName": str,
        "virtualGatewayName": str,
    },
)
_OptionalDeleteGatewayRouteInputTypeDef = TypedDict(
    "_OptionalDeleteGatewayRouteInputTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)


class DeleteGatewayRouteInputTypeDef(
    _RequiredDeleteGatewayRouteInputTypeDef, _OptionalDeleteGatewayRouteInputTypeDef
):
    pass


DeleteGatewayRouteOutputResponseTypeDef = TypedDict(
    "DeleteGatewayRouteOutputResponseTypeDef",
    {
        "gatewayRoute": "GatewayRouteDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMeshInputTypeDef = TypedDict(
    "DeleteMeshInputTypeDef",
    {
        "meshName": str,
    },
)

DeleteMeshOutputResponseTypeDef = TypedDict(
    "DeleteMeshOutputResponseTypeDef",
    {
        "mesh": "MeshDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteRouteInputTypeDef = TypedDict(
    "_RequiredDeleteRouteInputTypeDef",
    {
        "meshName": str,
        "routeName": str,
        "virtualRouterName": str,
    },
)
_OptionalDeleteRouteInputTypeDef = TypedDict(
    "_OptionalDeleteRouteInputTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)


class DeleteRouteInputTypeDef(_RequiredDeleteRouteInputTypeDef, _OptionalDeleteRouteInputTypeDef):
    pass


DeleteRouteOutputResponseTypeDef = TypedDict(
    "DeleteRouteOutputResponseTypeDef",
    {
        "route": "RouteDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteVirtualGatewayInputTypeDef = TypedDict(
    "_RequiredDeleteVirtualGatewayInputTypeDef",
    {
        "meshName": str,
        "virtualGatewayName": str,
    },
)
_OptionalDeleteVirtualGatewayInputTypeDef = TypedDict(
    "_OptionalDeleteVirtualGatewayInputTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)


class DeleteVirtualGatewayInputTypeDef(
    _RequiredDeleteVirtualGatewayInputTypeDef, _OptionalDeleteVirtualGatewayInputTypeDef
):
    pass


DeleteVirtualGatewayOutputResponseTypeDef = TypedDict(
    "DeleteVirtualGatewayOutputResponseTypeDef",
    {
        "virtualGateway": "VirtualGatewayDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteVirtualNodeInputTypeDef = TypedDict(
    "_RequiredDeleteVirtualNodeInputTypeDef",
    {
        "meshName": str,
        "virtualNodeName": str,
    },
)
_OptionalDeleteVirtualNodeInputTypeDef = TypedDict(
    "_OptionalDeleteVirtualNodeInputTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)


class DeleteVirtualNodeInputTypeDef(
    _RequiredDeleteVirtualNodeInputTypeDef, _OptionalDeleteVirtualNodeInputTypeDef
):
    pass


DeleteVirtualNodeOutputResponseTypeDef = TypedDict(
    "DeleteVirtualNodeOutputResponseTypeDef",
    {
        "virtualNode": "VirtualNodeDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteVirtualRouterInputTypeDef = TypedDict(
    "_RequiredDeleteVirtualRouterInputTypeDef",
    {
        "meshName": str,
        "virtualRouterName": str,
    },
)
_OptionalDeleteVirtualRouterInputTypeDef = TypedDict(
    "_OptionalDeleteVirtualRouterInputTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)


class DeleteVirtualRouterInputTypeDef(
    _RequiredDeleteVirtualRouterInputTypeDef, _OptionalDeleteVirtualRouterInputTypeDef
):
    pass


DeleteVirtualRouterOutputResponseTypeDef = TypedDict(
    "DeleteVirtualRouterOutputResponseTypeDef",
    {
        "virtualRouter": "VirtualRouterDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteVirtualServiceInputTypeDef = TypedDict(
    "_RequiredDeleteVirtualServiceInputTypeDef",
    {
        "meshName": str,
        "virtualServiceName": str,
    },
)
_OptionalDeleteVirtualServiceInputTypeDef = TypedDict(
    "_OptionalDeleteVirtualServiceInputTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)


class DeleteVirtualServiceInputTypeDef(
    _RequiredDeleteVirtualServiceInputTypeDef, _OptionalDeleteVirtualServiceInputTypeDef
):
    pass


DeleteVirtualServiceOutputResponseTypeDef = TypedDict(
    "DeleteVirtualServiceOutputResponseTypeDef",
    {
        "virtualService": "VirtualServiceDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeGatewayRouteInputTypeDef = TypedDict(
    "_RequiredDescribeGatewayRouteInputTypeDef",
    {
        "gatewayRouteName": str,
        "meshName": str,
        "virtualGatewayName": str,
    },
)
_OptionalDescribeGatewayRouteInputTypeDef = TypedDict(
    "_OptionalDescribeGatewayRouteInputTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)


class DescribeGatewayRouteInputTypeDef(
    _RequiredDescribeGatewayRouteInputTypeDef, _OptionalDescribeGatewayRouteInputTypeDef
):
    pass


DescribeGatewayRouteOutputResponseTypeDef = TypedDict(
    "DescribeGatewayRouteOutputResponseTypeDef",
    {
        "gatewayRoute": "GatewayRouteDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeMeshInputTypeDef = TypedDict(
    "_RequiredDescribeMeshInputTypeDef",
    {
        "meshName": str,
    },
)
_OptionalDescribeMeshInputTypeDef = TypedDict(
    "_OptionalDescribeMeshInputTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)


class DescribeMeshInputTypeDef(
    _RequiredDescribeMeshInputTypeDef, _OptionalDescribeMeshInputTypeDef
):
    pass


DescribeMeshOutputResponseTypeDef = TypedDict(
    "DescribeMeshOutputResponseTypeDef",
    {
        "mesh": "MeshDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeRouteInputTypeDef = TypedDict(
    "_RequiredDescribeRouteInputTypeDef",
    {
        "meshName": str,
        "routeName": str,
        "virtualRouterName": str,
    },
)
_OptionalDescribeRouteInputTypeDef = TypedDict(
    "_OptionalDescribeRouteInputTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)


class DescribeRouteInputTypeDef(
    _RequiredDescribeRouteInputTypeDef, _OptionalDescribeRouteInputTypeDef
):
    pass


DescribeRouteOutputResponseTypeDef = TypedDict(
    "DescribeRouteOutputResponseTypeDef",
    {
        "route": "RouteDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeVirtualGatewayInputTypeDef = TypedDict(
    "_RequiredDescribeVirtualGatewayInputTypeDef",
    {
        "meshName": str,
        "virtualGatewayName": str,
    },
)
_OptionalDescribeVirtualGatewayInputTypeDef = TypedDict(
    "_OptionalDescribeVirtualGatewayInputTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)


class DescribeVirtualGatewayInputTypeDef(
    _RequiredDescribeVirtualGatewayInputTypeDef, _OptionalDescribeVirtualGatewayInputTypeDef
):
    pass


DescribeVirtualGatewayOutputResponseTypeDef = TypedDict(
    "DescribeVirtualGatewayOutputResponseTypeDef",
    {
        "virtualGateway": "VirtualGatewayDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeVirtualNodeInputTypeDef = TypedDict(
    "_RequiredDescribeVirtualNodeInputTypeDef",
    {
        "meshName": str,
        "virtualNodeName": str,
    },
)
_OptionalDescribeVirtualNodeInputTypeDef = TypedDict(
    "_OptionalDescribeVirtualNodeInputTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)


class DescribeVirtualNodeInputTypeDef(
    _RequiredDescribeVirtualNodeInputTypeDef, _OptionalDescribeVirtualNodeInputTypeDef
):
    pass


DescribeVirtualNodeOutputResponseTypeDef = TypedDict(
    "DescribeVirtualNodeOutputResponseTypeDef",
    {
        "virtualNode": "VirtualNodeDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeVirtualRouterInputTypeDef = TypedDict(
    "_RequiredDescribeVirtualRouterInputTypeDef",
    {
        "meshName": str,
        "virtualRouterName": str,
    },
)
_OptionalDescribeVirtualRouterInputTypeDef = TypedDict(
    "_OptionalDescribeVirtualRouterInputTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)


class DescribeVirtualRouterInputTypeDef(
    _RequiredDescribeVirtualRouterInputTypeDef, _OptionalDescribeVirtualRouterInputTypeDef
):
    pass


DescribeVirtualRouterOutputResponseTypeDef = TypedDict(
    "DescribeVirtualRouterOutputResponseTypeDef",
    {
        "virtualRouter": "VirtualRouterDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeVirtualServiceInputTypeDef = TypedDict(
    "_RequiredDescribeVirtualServiceInputTypeDef",
    {
        "meshName": str,
        "virtualServiceName": str,
    },
)
_OptionalDescribeVirtualServiceInputTypeDef = TypedDict(
    "_OptionalDescribeVirtualServiceInputTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)


class DescribeVirtualServiceInputTypeDef(
    _RequiredDescribeVirtualServiceInputTypeDef, _OptionalDescribeVirtualServiceInputTypeDef
):
    pass


DescribeVirtualServiceOutputResponseTypeDef = TypedDict(
    "DescribeVirtualServiceOutputResponseTypeDef",
    {
        "virtualService": "VirtualServiceDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDnsServiceDiscoveryTypeDef = TypedDict(
    "_RequiredDnsServiceDiscoveryTypeDef",
    {
        "hostname": str,
    },
)
_OptionalDnsServiceDiscoveryTypeDef = TypedDict(
    "_OptionalDnsServiceDiscoveryTypeDef",
    {
        "responseType": DnsResponseTypeType,
    },
    total=False,
)


class DnsServiceDiscoveryTypeDef(
    _RequiredDnsServiceDiscoveryTypeDef, _OptionalDnsServiceDiscoveryTypeDef
):
    pass


DurationTypeDef = TypedDict(
    "DurationTypeDef",
    {
        "unit": DurationUnitType,
        "value": int,
    },
    total=False,
)

EgressFilterTypeDef = TypedDict(
    "EgressFilterTypeDef",
    {
        "type": EgressFilterTypeType,
    },
)

FileAccessLogTypeDef = TypedDict(
    "FileAccessLogTypeDef",
    {
        "path": str,
    },
)

GatewayRouteDataTypeDef = TypedDict(
    "GatewayRouteDataTypeDef",
    {
        "gatewayRouteName": str,
        "meshName": str,
        "metadata": "ResourceMetadataTypeDef",
        "spec": "GatewayRouteSpecTypeDef",
        "status": "GatewayRouteStatusTypeDef",
        "virtualGatewayName": str,
    },
)

GatewayRouteHostnameMatchTypeDef = TypedDict(
    "GatewayRouteHostnameMatchTypeDef",
    {
        "exact": str,
        "suffix": str,
    },
    total=False,
)

GatewayRouteHostnameRewriteTypeDef = TypedDict(
    "GatewayRouteHostnameRewriteTypeDef",
    {
        "defaultTargetHostname": DefaultGatewayRouteRewriteType,
    },
    total=False,
)

GatewayRouteRefTypeDef = TypedDict(
    "GatewayRouteRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "gatewayRouteName": str,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "version": int,
        "virtualGatewayName": str,
    },
)

GatewayRouteSpecTypeDef = TypedDict(
    "GatewayRouteSpecTypeDef",
    {
        "grpcRoute": "GrpcGatewayRouteTypeDef",
        "http2Route": "HttpGatewayRouteTypeDef",
        "httpRoute": "HttpGatewayRouteTypeDef",
        "priority": int,
    },
    total=False,
)

GatewayRouteStatusTypeDef = TypedDict(
    "GatewayRouteStatusTypeDef",
    {
        "status": GatewayRouteStatusCodeType,
    },
)

GatewayRouteTargetTypeDef = TypedDict(
    "GatewayRouteTargetTypeDef",
    {
        "virtualService": "GatewayRouteVirtualServiceTypeDef",
    },
)

GatewayRouteVirtualServiceTypeDef = TypedDict(
    "GatewayRouteVirtualServiceTypeDef",
    {
        "virtualServiceName": str,
    },
)

_RequiredGrpcGatewayRouteActionTypeDef = TypedDict(
    "_RequiredGrpcGatewayRouteActionTypeDef",
    {
        "target": "GatewayRouteTargetTypeDef",
    },
)
_OptionalGrpcGatewayRouteActionTypeDef = TypedDict(
    "_OptionalGrpcGatewayRouteActionTypeDef",
    {
        "rewrite": "GrpcGatewayRouteRewriteTypeDef",
    },
    total=False,
)


class GrpcGatewayRouteActionTypeDef(
    _RequiredGrpcGatewayRouteActionTypeDef, _OptionalGrpcGatewayRouteActionTypeDef
):
    pass


GrpcGatewayRouteMatchTypeDef = TypedDict(
    "GrpcGatewayRouteMatchTypeDef",
    {
        "hostname": "GatewayRouteHostnameMatchTypeDef",
        "metadata": List["GrpcGatewayRouteMetadataTypeDef"],
        "serviceName": str,
    },
    total=False,
)

_RequiredGrpcGatewayRouteMetadataTypeDef = TypedDict(
    "_RequiredGrpcGatewayRouteMetadataTypeDef",
    {
        "name": str,
    },
)
_OptionalGrpcGatewayRouteMetadataTypeDef = TypedDict(
    "_OptionalGrpcGatewayRouteMetadataTypeDef",
    {
        "invert": bool,
        "match": "GrpcMetadataMatchMethodTypeDef",
    },
    total=False,
)


class GrpcGatewayRouteMetadataTypeDef(
    _RequiredGrpcGatewayRouteMetadataTypeDef, _OptionalGrpcGatewayRouteMetadataTypeDef
):
    pass


GrpcGatewayRouteRewriteTypeDef = TypedDict(
    "GrpcGatewayRouteRewriteTypeDef",
    {
        "hostname": "GatewayRouteHostnameRewriteTypeDef",
    },
    total=False,
)

GrpcGatewayRouteTypeDef = TypedDict(
    "GrpcGatewayRouteTypeDef",
    {
        "action": "GrpcGatewayRouteActionTypeDef",
        "match": "GrpcGatewayRouteMatchTypeDef",
    },
)

GrpcMetadataMatchMethodTypeDef = TypedDict(
    "GrpcMetadataMatchMethodTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": "MatchRangeTypeDef",
        "regex": str,
        "suffix": str,
    },
    total=False,
)

_RequiredGrpcRetryPolicyTypeDef = TypedDict(
    "_RequiredGrpcRetryPolicyTypeDef",
    {
        "maxRetries": int,
        "perRetryTimeout": "DurationTypeDef",
    },
)
_OptionalGrpcRetryPolicyTypeDef = TypedDict(
    "_OptionalGrpcRetryPolicyTypeDef",
    {
        "grpcRetryEvents": List[GrpcRetryPolicyEventType],
        "httpRetryEvents": List[str],
        "tcpRetryEvents": List[Literal["connection-error"]],
    },
    total=False,
)


class GrpcRetryPolicyTypeDef(_RequiredGrpcRetryPolicyTypeDef, _OptionalGrpcRetryPolicyTypeDef):
    pass


GrpcRouteActionTypeDef = TypedDict(
    "GrpcRouteActionTypeDef",
    {
        "weightedTargets": List["WeightedTargetTypeDef"],
    },
)

GrpcRouteMatchTypeDef = TypedDict(
    "GrpcRouteMatchTypeDef",
    {
        "metadata": List["GrpcRouteMetadataTypeDef"],
        "methodName": str,
        "serviceName": str,
    },
    total=False,
)

GrpcRouteMetadataMatchMethodTypeDef = TypedDict(
    "GrpcRouteMetadataMatchMethodTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": "MatchRangeTypeDef",
        "regex": str,
        "suffix": str,
    },
    total=False,
)

_RequiredGrpcRouteMetadataTypeDef = TypedDict(
    "_RequiredGrpcRouteMetadataTypeDef",
    {
        "name": str,
    },
)
_OptionalGrpcRouteMetadataTypeDef = TypedDict(
    "_OptionalGrpcRouteMetadataTypeDef",
    {
        "invert": bool,
        "match": "GrpcRouteMetadataMatchMethodTypeDef",
    },
    total=False,
)


class GrpcRouteMetadataTypeDef(
    _RequiredGrpcRouteMetadataTypeDef, _OptionalGrpcRouteMetadataTypeDef
):
    pass


_RequiredGrpcRouteTypeDef = TypedDict(
    "_RequiredGrpcRouteTypeDef",
    {
        "action": "GrpcRouteActionTypeDef",
        "match": "GrpcRouteMatchTypeDef",
    },
)
_OptionalGrpcRouteTypeDef = TypedDict(
    "_OptionalGrpcRouteTypeDef",
    {
        "retryPolicy": "GrpcRetryPolicyTypeDef",
        "timeout": "GrpcTimeoutTypeDef",
    },
    total=False,
)


class GrpcRouteTypeDef(_RequiredGrpcRouteTypeDef, _OptionalGrpcRouteTypeDef):
    pass


GrpcTimeoutTypeDef = TypedDict(
    "GrpcTimeoutTypeDef",
    {
        "idle": "DurationTypeDef",
        "perRequest": "DurationTypeDef",
    },
    total=False,
)

HeaderMatchMethodTypeDef = TypedDict(
    "HeaderMatchMethodTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": "MatchRangeTypeDef",
        "regex": str,
        "suffix": str,
    },
    total=False,
)

_RequiredHealthCheckPolicyTypeDef = TypedDict(
    "_RequiredHealthCheckPolicyTypeDef",
    {
        "healthyThreshold": int,
        "intervalMillis": int,
        "protocol": PortProtocolType,
        "timeoutMillis": int,
        "unhealthyThreshold": int,
    },
)
_OptionalHealthCheckPolicyTypeDef = TypedDict(
    "_OptionalHealthCheckPolicyTypeDef",
    {
        "path": str,
        "port": int,
    },
    total=False,
)


class HealthCheckPolicyTypeDef(
    _RequiredHealthCheckPolicyTypeDef, _OptionalHealthCheckPolicyTypeDef
):
    pass


_RequiredHttpGatewayRouteActionTypeDef = TypedDict(
    "_RequiredHttpGatewayRouteActionTypeDef",
    {
        "target": "GatewayRouteTargetTypeDef",
    },
)
_OptionalHttpGatewayRouteActionTypeDef = TypedDict(
    "_OptionalHttpGatewayRouteActionTypeDef",
    {
        "rewrite": "HttpGatewayRouteRewriteTypeDef",
    },
    total=False,
)


class HttpGatewayRouteActionTypeDef(
    _RequiredHttpGatewayRouteActionTypeDef, _OptionalHttpGatewayRouteActionTypeDef
):
    pass


_RequiredHttpGatewayRouteHeaderTypeDef = TypedDict(
    "_RequiredHttpGatewayRouteHeaderTypeDef",
    {
        "name": str,
    },
)
_OptionalHttpGatewayRouteHeaderTypeDef = TypedDict(
    "_OptionalHttpGatewayRouteHeaderTypeDef",
    {
        "invert": bool,
        "match": "HeaderMatchMethodTypeDef",
    },
    total=False,
)


class HttpGatewayRouteHeaderTypeDef(
    _RequiredHttpGatewayRouteHeaderTypeDef, _OptionalHttpGatewayRouteHeaderTypeDef
):
    pass


HttpGatewayRouteMatchTypeDef = TypedDict(
    "HttpGatewayRouteMatchTypeDef",
    {
        "headers": List["HttpGatewayRouteHeaderTypeDef"],
        "hostname": "GatewayRouteHostnameMatchTypeDef",
        "method": HttpMethodType,
        "path": "HttpPathMatchTypeDef",
        "prefix": str,
        "queryParameters": List["HttpQueryParameterTypeDef"],
    },
    total=False,
)

HttpGatewayRoutePathRewriteTypeDef = TypedDict(
    "HttpGatewayRoutePathRewriteTypeDef",
    {
        "exact": str,
    },
    total=False,
)

HttpGatewayRoutePrefixRewriteTypeDef = TypedDict(
    "HttpGatewayRoutePrefixRewriteTypeDef",
    {
        "defaultPrefix": DefaultGatewayRouteRewriteType,
        "value": str,
    },
    total=False,
)

HttpGatewayRouteRewriteTypeDef = TypedDict(
    "HttpGatewayRouteRewriteTypeDef",
    {
        "hostname": "GatewayRouteHostnameRewriteTypeDef",
        "path": "HttpGatewayRoutePathRewriteTypeDef",
        "prefix": "HttpGatewayRoutePrefixRewriteTypeDef",
    },
    total=False,
)

HttpGatewayRouteTypeDef = TypedDict(
    "HttpGatewayRouteTypeDef",
    {
        "action": "HttpGatewayRouteActionTypeDef",
        "match": "HttpGatewayRouteMatchTypeDef",
    },
)

HttpPathMatchTypeDef = TypedDict(
    "HttpPathMatchTypeDef",
    {
        "exact": str,
        "regex": str,
    },
    total=False,
)

_RequiredHttpQueryParameterTypeDef = TypedDict(
    "_RequiredHttpQueryParameterTypeDef",
    {
        "name": str,
    },
)
_OptionalHttpQueryParameterTypeDef = TypedDict(
    "_OptionalHttpQueryParameterTypeDef",
    {
        "match": "QueryParameterMatchTypeDef",
    },
    total=False,
)


class HttpQueryParameterTypeDef(
    _RequiredHttpQueryParameterTypeDef, _OptionalHttpQueryParameterTypeDef
):
    pass


_RequiredHttpRetryPolicyTypeDef = TypedDict(
    "_RequiredHttpRetryPolicyTypeDef",
    {
        "maxRetries": int,
        "perRetryTimeout": "DurationTypeDef",
    },
)
_OptionalHttpRetryPolicyTypeDef = TypedDict(
    "_OptionalHttpRetryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "tcpRetryEvents": List[Literal["connection-error"]],
    },
    total=False,
)


class HttpRetryPolicyTypeDef(_RequiredHttpRetryPolicyTypeDef, _OptionalHttpRetryPolicyTypeDef):
    pass


HttpRouteActionTypeDef = TypedDict(
    "HttpRouteActionTypeDef",
    {
        "weightedTargets": List["WeightedTargetTypeDef"],
    },
)

_RequiredHttpRouteHeaderTypeDef = TypedDict(
    "_RequiredHttpRouteHeaderTypeDef",
    {
        "name": str,
    },
)
_OptionalHttpRouteHeaderTypeDef = TypedDict(
    "_OptionalHttpRouteHeaderTypeDef",
    {
        "invert": bool,
        "match": "HeaderMatchMethodTypeDef",
    },
    total=False,
)


class HttpRouteHeaderTypeDef(_RequiredHttpRouteHeaderTypeDef, _OptionalHttpRouteHeaderTypeDef):
    pass


HttpRouteMatchTypeDef = TypedDict(
    "HttpRouteMatchTypeDef",
    {
        "headers": List["HttpRouteHeaderTypeDef"],
        "method": HttpMethodType,
        "path": "HttpPathMatchTypeDef",
        "prefix": str,
        "queryParameters": List["HttpQueryParameterTypeDef"],
        "scheme": HttpSchemeType,
    },
    total=False,
)

_RequiredHttpRouteTypeDef = TypedDict(
    "_RequiredHttpRouteTypeDef",
    {
        "action": "HttpRouteActionTypeDef",
        "match": "HttpRouteMatchTypeDef",
    },
)
_OptionalHttpRouteTypeDef = TypedDict(
    "_OptionalHttpRouteTypeDef",
    {
        "retryPolicy": "HttpRetryPolicyTypeDef",
        "timeout": "HttpTimeoutTypeDef",
    },
    total=False,
)


class HttpRouteTypeDef(_RequiredHttpRouteTypeDef, _OptionalHttpRouteTypeDef):
    pass


HttpTimeoutTypeDef = TypedDict(
    "HttpTimeoutTypeDef",
    {
        "idle": "DurationTypeDef",
        "perRequest": "DurationTypeDef",
    },
    total=False,
)

_RequiredListGatewayRoutesInputTypeDef = TypedDict(
    "_RequiredListGatewayRoutesInputTypeDef",
    {
        "meshName": str,
        "virtualGatewayName": str,
    },
)
_OptionalListGatewayRoutesInputTypeDef = TypedDict(
    "_OptionalListGatewayRoutesInputTypeDef",
    {
        "limit": int,
        "meshOwner": str,
        "nextToken": str,
    },
    total=False,
)


class ListGatewayRoutesInputTypeDef(
    _RequiredListGatewayRoutesInputTypeDef, _OptionalListGatewayRoutesInputTypeDef
):
    pass


ListGatewayRoutesOutputResponseTypeDef = TypedDict(
    "ListGatewayRoutesOutputResponseTypeDef",
    {
        "gatewayRoutes": List["GatewayRouteRefTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMeshesInputTypeDef = TypedDict(
    "ListMeshesInputTypeDef",
    {
        "limit": int,
        "nextToken": str,
    },
    total=False,
)

ListMeshesOutputResponseTypeDef = TypedDict(
    "ListMeshesOutputResponseTypeDef",
    {
        "meshes": List["MeshRefTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRoutesInputTypeDef = TypedDict(
    "_RequiredListRoutesInputTypeDef",
    {
        "meshName": str,
        "virtualRouterName": str,
    },
)
_OptionalListRoutesInputTypeDef = TypedDict(
    "_OptionalListRoutesInputTypeDef",
    {
        "limit": int,
        "meshOwner": str,
        "nextToken": str,
    },
    total=False,
)


class ListRoutesInputTypeDef(_RequiredListRoutesInputTypeDef, _OptionalListRoutesInputTypeDef):
    pass


ListRoutesOutputResponseTypeDef = TypedDict(
    "ListRoutesOutputResponseTypeDef",
    {
        "nextToken": str,
        "routes": List["RouteRefTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceInputTypeDef = TypedDict(
    "_RequiredListTagsForResourceInputTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalListTagsForResourceInputTypeDef = TypedDict(
    "_OptionalListTagsForResourceInputTypeDef",
    {
        "limit": int,
        "nextToken": str,
    },
    total=False,
)


class ListTagsForResourceInputTypeDef(
    _RequiredListTagsForResourceInputTypeDef, _OptionalListTagsForResourceInputTypeDef
):
    pass


ListTagsForResourceOutputResponseTypeDef = TypedDict(
    "ListTagsForResourceOutputResponseTypeDef",
    {
        "nextToken": str,
        "tags": List["TagRefTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListVirtualGatewaysInputTypeDef = TypedDict(
    "_RequiredListVirtualGatewaysInputTypeDef",
    {
        "meshName": str,
    },
)
_OptionalListVirtualGatewaysInputTypeDef = TypedDict(
    "_OptionalListVirtualGatewaysInputTypeDef",
    {
        "limit": int,
        "meshOwner": str,
        "nextToken": str,
    },
    total=False,
)


class ListVirtualGatewaysInputTypeDef(
    _RequiredListVirtualGatewaysInputTypeDef, _OptionalListVirtualGatewaysInputTypeDef
):
    pass


ListVirtualGatewaysOutputResponseTypeDef = TypedDict(
    "ListVirtualGatewaysOutputResponseTypeDef",
    {
        "nextToken": str,
        "virtualGateways": List["VirtualGatewayRefTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListVirtualNodesInputTypeDef = TypedDict(
    "_RequiredListVirtualNodesInputTypeDef",
    {
        "meshName": str,
    },
)
_OptionalListVirtualNodesInputTypeDef = TypedDict(
    "_OptionalListVirtualNodesInputTypeDef",
    {
        "limit": int,
        "meshOwner": str,
        "nextToken": str,
    },
    total=False,
)


class ListVirtualNodesInputTypeDef(
    _RequiredListVirtualNodesInputTypeDef, _OptionalListVirtualNodesInputTypeDef
):
    pass


ListVirtualNodesOutputResponseTypeDef = TypedDict(
    "ListVirtualNodesOutputResponseTypeDef",
    {
        "nextToken": str,
        "virtualNodes": List["VirtualNodeRefTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListVirtualRoutersInputTypeDef = TypedDict(
    "_RequiredListVirtualRoutersInputTypeDef",
    {
        "meshName": str,
    },
)
_OptionalListVirtualRoutersInputTypeDef = TypedDict(
    "_OptionalListVirtualRoutersInputTypeDef",
    {
        "limit": int,
        "meshOwner": str,
        "nextToken": str,
    },
    total=False,
)


class ListVirtualRoutersInputTypeDef(
    _RequiredListVirtualRoutersInputTypeDef, _OptionalListVirtualRoutersInputTypeDef
):
    pass


ListVirtualRoutersOutputResponseTypeDef = TypedDict(
    "ListVirtualRoutersOutputResponseTypeDef",
    {
        "nextToken": str,
        "virtualRouters": List["VirtualRouterRefTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListVirtualServicesInputTypeDef = TypedDict(
    "_RequiredListVirtualServicesInputTypeDef",
    {
        "meshName": str,
    },
)
_OptionalListVirtualServicesInputTypeDef = TypedDict(
    "_OptionalListVirtualServicesInputTypeDef",
    {
        "limit": int,
        "meshOwner": str,
        "nextToken": str,
    },
    total=False,
)


class ListVirtualServicesInputTypeDef(
    _RequiredListVirtualServicesInputTypeDef, _OptionalListVirtualServicesInputTypeDef
):
    pass


ListVirtualServicesOutputResponseTypeDef = TypedDict(
    "ListVirtualServicesOutputResponseTypeDef",
    {
        "nextToken": str,
        "virtualServices": List["VirtualServiceRefTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListenerTimeoutTypeDef = TypedDict(
    "ListenerTimeoutTypeDef",
    {
        "grpc": "GrpcTimeoutTypeDef",
        "http": "HttpTimeoutTypeDef",
        "http2": "HttpTimeoutTypeDef",
        "tcp": "TcpTimeoutTypeDef",
    },
    total=False,
)

ListenerTlsAcmCertificateTypeDef = TypedDict(
    "ListenerTlsAcmCertificateTypeDef",
    {
        "certificateArn": str,
    },
)

ListenerTlsCertificateTypeDef = TypedDict(
    "ListenerTlsCertificateTypeDef",
    {
        "acm": "ListenerTlsAcmCertificateTypeDef",
        "file": "ListenerTlsFileCertificateTypeDef",
        "sds": "ListenerTlsSdsCertificateTypeDef",
    },
    total=False,
)

ListenerTlsFileCertificateTypeDef = TypedDict(
    "ListenerTlsFileCertificateTypeDef",
    {
        "certificateChain": str,
        "privateKey": str,
    },
)

ListenerTlsSdsCertificateTypeDef = TypedDict(
    "ListenerTlsSdsCertificateTypeDef",
    {
        "secretName": str,
    },
)

_RequiredListenerTlsTypeDef = TypedDict(
    "_RequiredListenerTlsTypeDef",
    {
        "certificate": "ListenerTlsCertificateTypeDef",
        "mode": ListenerTlsModeType,
    },
)
_OptionalListenerTlsTypeDef = TypedDict(
    "_OptionalListenerTlsTypeDef",
    {
        "validation": "ListenerTlsValidationContextTypeDef",
    },
    total=False,
)


class ListenerTlsTypeDef(_RequiredListenerTlsTypeDef, _OptionalListenerTlsTypeDef):
    pass


ListenerTlsValidationContextTrustTypeDef = TypedDict(
    "ListenerTlsValidationContextTrustTypeDef",
    {
        "file": "TlsValidationContextFileTrustTypeDef",
        "sds": "TlsValidationContextSdsTrustTypeDef",
    },
    total=False,
)

_RequiredListenerTlsValidationContextTypeDef = TypedDict(
    "_RequiredListenerTlsValidationContextTypeDef",
    {
        "trust": "ListenerTlsValidationContextTrustTypeDef",
    },
)
_OptionalListenerTlsValidationContextTypeDef = TypedDict(
    "_OptionalListenerTlsValidationContextTypeDef",
    {
        "subjectAlternativeNames": "SubjectAlternativeNamesTypeDef",
    },
    total=False,
)


class ListenerTlsValidationContextTypeDef(
    _RequiredListenerTlsValidationContextTypeDef, _OptionalListenerTlsValidationContextTypeDef
):
    pass


_RequiredListenerTypeDef = TypedDict(
    "_RequiredListenerTypeDef",
    {
        "portMapping": "PortMappingTypeDef",
    },
)
_OptionalListenerTypeDef = TypedDict(
    "_OptionalListenerTypeDef",
    {
        "connectionPool": "VirtualNodeConnectionPoolTypeDef",
        "healthCheck": "HealthCheckPolicyTypeDef",
        "outlierDetection": "OutlierDetectionTypeDef",
        "timeout": "ListenerTimeoutTypeDef",
        "tls": "ListenerTlsTypeDef",
    },
    total=False,
)


class ListenerTypeDef(_RequiredListenerTypeDef, _OptionalListenerTypeDef):
    pass


LoggingTypeDef = TypedDict(
    "LoggingTypeDef",
    {
        "accessLog": "AccessLogTypeDef",
    },
    total=False,
)

MatchRangeTypeDef = TypedDict(
    "MatchRangeTypeDef",
    {
        "end": int,
        "start": int,
    },
)

MeshDataTypeDef = TypedDict(
    "MeshDataTypeDef",
    {
        "meshName": str,
        "metadata": "ResourceMetadataTypeDef",
        "spec": "MeshSpecTypeDef",
        "status": "MeshStatusTypeDef",
    },
)

MeshRefTypeDef = TypedDict(
    "MeshRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "version": int,
    },
)

MeshSpecTypeDef = TypedDict(
    "MeshSpecTypeDef",
    {
        "egressFilter": "EgressFilterTypeDef",
    },
    total=False,
)

MeshStatusTypeDef = TypedDict(
    "MeshStatusTypeDef",
    {
        "status": MeshStatusCodeType,
    },
    total=False,
)

OutlierDetectionTypeDef = TypedDict(
    "OutlierDetectionTypeDef",
    {
        "baseEjectionDuration": "DurationTypeDef",
        "interval": "DurationTypeDef",
        "maxEjectionPercent": int,
        "maxServerErrors": int,
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

PortMappingTypeDef = TypedDict(
    "PortMappingTypeDef",
    {
        "port": int,
        "protocol": PortProtocolType,
    },
)

QueryParameterMatchTypeDef = TypedDict(
    "QueryParameterMatchTypeDef",
    {
        "exact": str,
    },
    total=False,
)

ResourceMetadataTypeDef = TypedDict(
    "ResourceMetadataTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshOwner": str,
        "resourceOwner": str,
        "uid": str,
        "version": int,
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

RouteDataTypeDef = TypedDict(
    "RouteDataTypeDef",
    {
        "meshName": str,
        "metadata": "ResourceMetadataTypeDef",
        "routeName": str,
        "spec": "RouteSpecTypeDef",
        "status": "RouteStatusTypeDef",
        "virtualRouterName": str,
    },
)

RouteRefTypeDef = TypedDict(
    "RouteRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "routeName": str,
        "version": int,
        "virtualRouterName": str,
    },
)

RouteSpecTypeDef = TypedDict(
    "RouteSpecTypeDef",
    {
        "grpcRoute": "GrpcRouteTypeDef",
        "http2Route": "HttpRouteTypeDef",
        "httpRoute": "HttpRouteTypeDef",
        "priority": int,
        "tcpRoute": "TcpRouteTypeDef",
    },
    total=False,
)

RouteStatusTypeDef = TypedDict(
    "RouteStatusTypeDef",
    {
        "status": RouteStatusCodeType,
    },
)

ServiceDiscoveryTypeDef = TypedDict(
    "ServiceDiscoveryTypeDef",
    {
        "awsCloudMap": "AwsCloudMapServiceDiscoveryTypeDef",
        "dns": "DnsServiceDiscoveryTypeDef",
    },
    total=False,
)

SubjectAlternativeNameMatchersTypeDef = TypedDict(
    "SubjectAlternativeNameMatchersTypeDef",
    {
        "exact": List[str],
    },
)

SubjectAlternativeNamesTypeDef = TypedDict(
    "SubjectAlternativeNamesTypeDef",
    {
        "match": "SubjectAlternativeNameMatchersTypeDef",
    },
)

TagRefTypeDef = TypedDict(
    "TagRefTypeDef",
    {
        "key": str,
        "value": str,
    },
)

TagResourceInputTypeDef = TypedDict(
    "TagResourceInputTypeDef",
    {
        "resourceArn": str,
        "tags": List["TagRefTypeDef"],
    },
)

TcpRouteActionTypeDef = TypedDict(
    "TcpRouteActionTypeDef",
    {
        "weightedTargets": List["WeightedTargetTypeDef"],
    },
)

_RequiredTcpRouteTypeDef = TypedDict(
    "_RequiredTcpRouteTypeDef",
    {
        "action": "TcpRouteActionTypeDef",
    },
)
_OptionalTcpRouteTypeDef = TypedDict(
    "_OptionalTcpRouteTypeDef",
    {
        "timeout": "TcpTimeoutTypeDef",
    },
    total=False,
)


class TcpRouteTypeDef(_RequiredTcpRouteTypeDef, _OptionalTcpRouteTypeDef):
    pass


TcpTimeoutTypeDef = TypedDict(
    "TcpTimeoutTypeDef",
    {
        "idle": "DurationTypeDef",
    },
    total=False,
)

TlsValidationContextAcmTrustTypeDef = TypedDict(
    "TlsValidationContextAcmTrustTypeDef",
    {
        "certificateAuthorityArns": List[str],
    },
)

TlsValidationContextFileTrustTypeDef = TypedDict(
    "TlsValidationContextFileTrustTypeDef",
    {
        "certificateChain": str,
    },
)

TlsValidationContextSdsTrustTypeDef = TypedDict(
    "TlsValidationContextSdsTrustTypeDef",
    {
        "secretName": str,
    },
)

TlsValidationContextTrustTypeDef = TypedDict(
    "TlsValidationContextTrustTypeDef",
    {
        "acm": "TlsValidationContextAcmTrustTypeDef",
        "file": "TlsValidationContextFileTrustTypeDef",
        "sds": "TlsValidationContextSdsTrustTypeDef",
    },
    total=False,
)

_RequiredTlsValidationContextTypeDef = TypedDict(
    "_RequiredTlsValidationContextTypeDef",
    {
        "trust": "TlsValidationContextTrustTypeDef",
    },
)
_OptionalTlsValidationContextTypeDef = TypedDict(
    "_OptionalTlsValidationContextTypeDef",
    {
        "subjectAlternativeNames": "SubjectAlternativeNamesTypeDef",
    },
    total=False,
)


class TlsValidationContextTypeDef(
    _RequiredTlsValidationContextTypeDef, _OptionalTlsValidationContextTypeDef
):
    pass


UntagResourceInputTypeDef = TypedDict(
    "UntagResourceInputTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateGatewayRouteInputTypeDef = TypedDict(
    "_RequiredUpdateGatewayRouteInputTypeDef",
    {
        "gatewayRouteName": str,
        "meshName": str,
        "spec": "GatewayRouteSpecTypeDef",
        "virtualGatewayName": str,
    },
)
_OptionalUpdateGatewayRouteInputTypeDef = TypedDict(
    "_OptionalUpdateGatewayRouteInputTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
    },
    total=False,
)


class UpdateGatewayRouteInputTypeDef(
    _RequiredUpdateGatewayRouteInputTypeDef, _OptionalUpdateGatewayRouteInputTypeDef
):
    pass


UpdateGatewayRouteOutputResponseTypeDef = TypedDict(
    "UpdateGatewayRouteOutputResponseTypeDef",
    {
        "gatewayRoute": "GatewayRouteDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateMeshInputTypeDef = TypedDict(
    "_RequiredUpdateMeshInputTypeDef",
    {
        "meshName": str,
    },
)
_OptionalUpdateMeshInputTypeDef = TypedDict(
    "_OptionalUpdateMeshInputTypeDef",
    {
        "clientToken": str,
        "spec": "MeshSpecTypeDef",
    },
    total=False,
)


class UpdateMeshInputTypeDef(_RequiredUpdateMeshInputTypeDef, _OptionalUpdateMeshInputTypeDef):
    pass


UpdateMeshOutputResponseTypeDef = TypedDict(
    "UpdateMeshOutputResponseTypeDef",
    {
        "mesh": "MeshDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateRouteInputTypeDef = TypedDict(
    "_RequiredUpdateRouteInputTypeDef",
    {
        "meshName": str,
        "routeName": str,
        "spec": "RouteSpecTypeDef",
        "virtualRouterName": str,
    },
)
_OptionalUpdateRouteInputTypeDef = TypedDict(
    "_OptionalUpdateRouteInputTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
    },
    total=False,
)


class UpdateRouteInputTypeDef(_RequiredUpdateRouteInputTypeDef, _OptionalUpdateRouteInputTypeDef):
    pass


UpdateRouteOutputResponseTypeDef = TypedDict(
    "UpdateRouteOutputResponseTypeDef",
    {
        "route": "RouteDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateVirtualGatewayInputTypeDef = TypedDict(
    "_RequiredUpdateVirtualGatewayInputTypeDef",
    {
        "meshName": str,
        "spec": "VirtualGatewaySpecTypeDef",
        "virtualGatewayName": str,
    },
)
_OptionalUpdateVirtualGatewayInputTypeDef = TypedDict(
    "_OptionalUpdateVirtualGatewayInputTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
    },
    total=False,
)


class UpdateVirtualGatewayInputTypeDef(
    _RequiredUpdateVirtualGatewayInputTypeDef, _OptionalUpdateVirtualGatewayInputTypeDef
):
    pass


UpdateVirtualGatewayOutputResponseTypeDef = TypedDict(
    "UpdateVirtualGatewayOutputResponseTypeDef",
    {
        "virtualGateway": "VirtualGatewayDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateVirtualNodeInputTypeDef = TypedDict(
    "_RequiredUpdateVirtualNodeInputTypeDef",
    {
        "meshName": str,
        "spec": "VirtualNodeSpecTypeDef",
        "virtualNodeName": str,
    },
)
_OptionalUpdateVirtualNodeInputTypeDef = TypedDict(
    "_OptionalUpdateVirtualNodeInputTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
    },
    total=False,
)


class UpdateVirtualNodeInputTypeDef(
    _RequiredUpdateVirtualNodeInputTypeDef, _OptionalUpdateVirtualNodeInputTypeDef
):
    pass


UpdateVirtualNodeOutputResponseTypeDef = TypedDict(
    "UpdateVirtualNodeOutputResponseTypeDef",
    {
        "virtualNode": "VirtualNodeDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateVirtualRouterInputTypeDef = TypedDict(
    "_RequiredUpdateVirtualRouterInputTypeDef",
    {
        "meshName": str,
        "spec": "VirtualRouterSpecTypeDef",
        "virtualRouterName": str,
    },
)
_OptionalUpdateVirtualRouterInputTypeDef = TypedDict(
    "_OptionalUpdateVirtualRouterInputTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
    },
    total=False,
)


class UpdateVirtualRouterInputTypeDef(
    _RequiredUpdateVirtualRouterInputTypeDef, _OptionalUpdateVirtualRouterInputTypeDef
):
    pass


UpdateVirtualRouterOutputResponseTypeDef = TypedDict(
    "UpdateVirtualRouterOutputResponseTypeDef",
    {
        "virtualRouter": "VirtualRouterDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateVirtualServiceInputTypeDef = TypedDict(
    "_RequiredUpdateVirtualServiceInputTypeDef",
    {
        "meshName": str,
        "spec": "VirtualServiceSpecTypeDef",
        "virtualServiceName": str,
    },
)
_OptionalUpdateVirtualServiceInputTypeDef = TypedDict(
    "_OptionalUpdateVirtualServiceInputTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
    },
    total=False,
)


class UpdateVirtualServiceInputTypeDef(
    _RequiredUpdateVirtualServiceInputTypeDef, _OptionalUpdateVirtualServiceInputTypeDef
):
    pass


UpdateVirtualServiceOutputResponseTypeDef = TypedDict(
    "UpdateVirtualServiceOutputResponseTypeDef",
    {
        "virtualService": "VirtualServiceDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VirtualGatewayAccessLogTypeDef = TypedDict(
    "VirtualGatewayAccessLogTypeDef",
    {
        "file": "VirtualGatewayFileAccessLogTypeDef",
    },
    total=False,
)

VirtualGatewayBackendDefaultsTypeDef = TypedDict(
    "VirtualGatewayBackendDefaultsTypeDef",
    {
        "clientPolicy": "VirtualGatewayClientPolicyTypeDef",
    },
    total=False,
)

_RequiredVirtualGatewayClientPolicyTlsTypeDef = TypedDict(
    "_RequiredVirtualGatewayClientPolicyTlsTypeDef",
    {
        "validation": "VirtualGatewayTlsValidationContextTypeDef",
    },
)
_OptionalVirtualGatewayClientPolicyTlsTypeDef = TypedDict(
    "_OptionalVirtualGatewayClientPolicyTlsTypeDef",
    {
        "certificate": "VirtualGatewayClientTlsCertificateTypeDef",
        "enforce": bool,
        "ports": List[int],
    },
    total=False,
)


class VirtualGatewayClientPolicyTlsTypeDef(
    _RequiredVirtualGatewayClientPolicyTlsTypeDef, _OptionalVirtualGatewayClientPolicyTlsTypeDef
):
    pass


VirtualGatewayClientPolicyTypeDef = TypedDict(
    "VirtualGatewayClientPolicyTypeDef",
    {
        "tls": "VirtualGatewayClientPolicyTlsTypeDef",
    },
    total=False,
)

VirtualGatewayClientTlsCertificateTypeDef = TypedDict(
    "VirtualGatewayClientTlsCertificateTypeDef",
    {
        "file": "VirtualGatewayListenerTlsFileCertificateTypeDef",
        "sds": "VirtualGatewayListenerTlsSdsCertificateTypeDef",
    },
    total=False,
)

VirtualGatewayConnectionPoolTypeDef = TypedDict(
    "VirtualGatewayConnectionPoolTypeDef",
    {
        "grpc": "VirtualGatewayGrpcConnectionPoolTypeDef",
        "http": "VirtualGatewayHttpConnectionPoolTypeDef",
        "http2": "VirtualGatewayHttp2ConnectionPoolTypeDef",
    },
    total=False,
)

VirtualGatewayDataTypeDef = TypedDict(
    "VirtualGatewayDataTypeDef",
    {
        "meshName": str,
        "metadata": "ResourceMetadataTypeDef",
        "spec": "VirtualGatewaySpecTypeDef",
        "status": "VirtualGatewayStatusTypeDef",
        "virtualGatewayName": str,
    },
)

VirtualGatewayFileAccessLogTypeDef = TypedDict(
    "VirtualGatewayFileAccessLogTypeDef",
    {
        "path": str,
    },
)

VirtualGatewayGrpcConnectionPoolTypeDef = TypedDict(
    "VirtualGatewayGrpcConnectionPoolTypeDef",
    {
        "maxRequests": int,
    },
)

_RequiredVirtualGatewayHealthCheckPolicyTypeDef = TypedDict(
    "_RequiredVirtualGatewayHealthCheckPolicyTypeDef",
    {
        "healthyThreshold": int,
        "intervalMillis": int,
        "protocol": VirtualGatewayPortProtocolType,
        "timeoutMillis": int,
        "unhealthyThreshold": int,
    },
)
_OptionalVirtualGatewayHealthCheckPolicyTypeDef = TypedDict(
    "_OptionalVirtualGatewayHealthCheckPolicyTypeDef",
    {
        "path": str,
        "port": int,
    },
    total=False,
)


class VirtualGatewayHealthCheckPolicyTypeDef(
    _RequiredVirtualGatewayHealthCheckPolicyTypeDef, _OptionalVirtualGatewayHealthCheckPolicyTypeDef
):
    pass


VirtualGatewayHttp2ConnectionPoolTypeDef = TypedDict(
    "VirtualGatewayHttp2ConnectionPoolTypeDef",
    {
        "maxRequests": int,
    },
)

_RequiredVirtualGatewayHttpConnectionPoolTypeDef = TypedDict(
    "_RequiredVirtualGatewayHttpConnectionPoolTypeDef",
    {
        "maxConnections": int,
    },
)
_OptionalVirtualGatewayHttpConnectionPoolTypeDef = TypedDict(
    "_OptionalVirtualGatewayHttpConnectionPoolTypeDef",
    {
        "maxPendingRequests": int,
    },
    total=False,
)


class VirtualGatewayHttpConnectionPoolTypeDef(
    _RequiredVirtualGatewayHttpConnectionPoolTypeDef,
    _OptionalVirtualGatewayHttpConnectionPoolTypeDef,
):
    pass


VirtualGatewayListenerTlsAcmCertificateTypeDef = TypedDict(
    "VirtualGatewayListenerTlsAcmCertificateTypeDef",
    {
        "certificateArn": str,
    },
)

VirtualGatewayListenerTlsCertificateTypeDef = TypedDict(
    "VirtualGatewayListenerTlsCertificateTypeDef",
    {
        "acm": "VirtualGatewayListenerTlsAcmCertificateTypeDef",
        "file": "VirtualGatewayListenerTlsFileCertificateTypeDef",
        "sds": "VirtualGatewayListenerTlsSdsCertificateTypeDef",
    },
    total=False,
)

VirtualGatewayListenerTlsFileCertificateTypeDef = TypedDict(
    "VirtualGatewayListenerTlsFileCertificateTypeDef",
    {
        "certificateChain": str,
        "privateKey": str,
    },
)

VirtualGatewayListenerTlsSdsCertificateTypeDef = TypedDict(
    "VirtualGatewayListenerTlsSdsCertificateTypeDef",
    {
        "secretName": str,
    },
)

_RequiredVirtualGatewayListenerTlsTypeDef = TypedDict(
    "_RequiredVirtualGatewayListenerTlsTypeDef",
    {
        "certificate": "VirtualGatewayListenerTlsCertificateTypeDef",
        "mode": VirtualGatewayListenerTlsModeType,
    },
)
_OptionalVirtualGatewayListenerTlsTypeDef = TypedDict(
    "_OptionalVirtualGatewayListenerTlsTypeDef",
    {
        "validation": "VirtualGatewayListenerTlsValidationContextTypeDef",
    },
    total=False,
)


class VirtualGatewayListenerTlsTypeDef(
    _RequiredVirtualGatewayListenerTlsTypeDef, _OptionalVirtualGatewayListenerTlsTypeDef
):
    pass


VirtualGatewayListenerTlsValidationContextTrustTypeDef = TypedDict(
    "VirtualGatewayListenerTlsValidationContextTrustTypeDef",
    {
        "file": "VirtualGatewayTlsValidationContextFileTrustTypeDef",
        "sds": "VirtualGatewayTlsValidationContextSdsTrustTypeDef",
    },
    total=False,
)

_RequiredVirtualGatewayListenerTlsValidationContextTypeDef = TypedDict(
    "_RequiredVirtualGatewayListenerTlsValidationContextTypeDef",
    {
        "trust": "VirtualGatewayListenerTlsValidationContextTrustTypeDef",
    },
)
_OptionalVirtualGatewayListenerTlsValidationContextTypeDef = TypedDict(
    "_OptionalVirtualGatewayListenerTlsValidationContextTypeDef",
    {
        "subjectAlternativeNames": "SubjectAlternativeNamesTypeDef",
    },
    total=False,
)


class VirtualGatewayListenerTlsValidationContextTypeDef(
    _RequiredVirtualGatewayListenerTlsValidationContextTypeDef,
    _OptionalVirtualGatewayListenerTlsValidationContextTypeDef,
):
    pass


_RequiredVirtualGatewayListenerTypeDef = TypedDict(
    "_RequiredVirtualGatewayListenerTypeDef",
    {
        "portMapping": "VirtualGatewayPortMappingTypeDef",
    },
)
_OptionalVirtualGatewayListenerTypeDef = TypedDict(
    "_OptionalVirtualGatewayListenerTypeDef",
    {
        "connectionPool": "VirtualGatewayConnectionPoolTypeDef",
        "healthCheck": "VirtualGatewayHealthCheckPolicyTypeDef",
        "tls": "VirtualGatewayListenerTlsTypeDef",
    },
    total=False,
)


class VirtualGatewayListenerTypeDef(
    _RequiredVirtualGatewayListenerTypeDef, _OptionalVirtualGatewayListenerTypeDef
):
    pass


VirtualGatewayLoggingTypeDef = TypedDict(
    "VirtualGatewayLoggingTypeDef",
    {
        "accessLog": "VirtualGatewayAccessLogTypeDef",
    },
    total=False,
)

VirtualGatewayPortMappingTypeDef = TypedDict(
    "VirtualGatewayPortMappingTypeDef",
    {
        "port": int,
        "protocol": VirtualGatewayPortProtocolType,
    },
)

VirtualGatewayRefTypeDef = TypedDict(
    "VirtualGatewayRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "version": int,
        "virtualGatewayName": str,
    },
)

_RequiredVirtualGatewaySpecTypeDef = TypedDict(
    "_RequiredVirtualGatewaySpecTypeDef",
    {
        "listeners": List["VirtualGatewayListenerTypeDef"],
    },
)
_OptionalVirtualGatewaySpecTypeDef = TypedDict(
    "_OptionalVirtualGatewaySpecTypeDef",
    {
        "backendDefaults": "VirtualGatewayBackendDefaultsTypeDef",
        "logging": "VirtualGatewayLoggingTypeDef",
    },
    total=False,
)


class VirtualGatewaySpecTypeDef(
    _RequiredVirtualGatewaySpecTypeDef, _OptionalVirtualGatewaySpecTypeDef
):
    pass


VirtualGatewayStatusTypeDef = TypedDict(
    "VirtualGatewayStatusTypeDef",
    {
        "status": VirtualGatewayStatusCodeType,
    },
)

VirtualGatewayTlsValidationContextAcmTrustTypeDef = TypedDict(
    "VirtualGatewayTlsValidationContextAcmTrustTypeDef",
    {
        "certificateAuthorityArns": List[str],
    },
)

VirtualGatewayTlsValidationContextFileTrustTypeDef = TypedDict(
    "VirtualGatewayTlsValidationContextFileTrustTypeDef",
    {
        "certificateChain": str,
    },
)

VirtualGatewayTlsValidationContextSdsTrustTypeDef = TypedDict(
    "VirtualGatewayTlsValidationContextSdsTrustTypeDef",
    {
        "secretName": str,
    },
)

VirtualGatewayTlsValidationContextTrustTypeDef = TypedDict(
    "VirtualGatewayTlsValidationContextTrustTypeDef",
    {
        "acm": "VirtualGatewayTlsValidationContextAcmTrustTypeDef",
        "file": "VirtualGatewayTlsValidationContextFileTrustTypeDef",
        "sds": "VirtualGatewayTlsValidationContextSdsTrustTypeDef",
    },
    total=False,
)

_RequiredVirtualGatewayTlsValidationContextTypeDef = TypedDict(
    "_RequiredVirtualGatewayTlsValidationContextTypeDef",
    {
        "trust": "VirtualGatewayTlsValidationContextTrustTypeDef",
    },
)
_OptionalVirtualGatewayTlsValidationContextTypeDef = TypedDict(
    "_OptionalVirtualGatewayTlsValidationContextTypeDef",
    {
        "subjectAlternativeNames": "SubjectAlternativeNamesTypeDef",
    },
    total=False,
)


class VirtualGatewayTlsValidationContextTypeDef(
    _RequiredVirtualGatewayTlsValidationContextTypeDef,
    _OptionalVirtualGatewayTlsValidationContextTypeDef,
):
    pass


VirtualNodeConnectionPoolTypeDef = TypedDict(
    "VirtualNodeConnectionPoolTypeDef",
    {
        "grpc": "VirtualNodeGrpcConnectionPoolTypeDef",
        "http": "VirtualNodeHttpConnectionPoolTypeDef",
        "http2": "VirtualNodeHttp2ConnectionPoolTypeDef",
        "tcp": "VirtualNodeTcpConnectionPoolTypeDef",
    },
    total=False,
)

VirtualNodeDataTypeDef = TypedDict(
    "VirtualNodeDataTypeDef",
    {
        "meshName": str,
        "metadata": "ResourceMetadataTypeDef",
        "spec": "VirtualNodeSpecTypeDef",
        "status": "VirtualNodeStatusTypeDef",
        "virtualNodeName": str,
    },
)

VirtualNodeGrpcConnectionPoolTypeDef = TypedDict(
    "VirtualNodeGrpcConnectionPoolTypeDef",
    {
        "maxRequests": int,
    },
)

VirtualNodeHttp2ConnectionPoolTypeDef = TypedDict(
    "VirtualNodeHttp2ConnectionPoolTypeDef",
    {
        "maxRequests": int,
    },
)

_RequiredVirtualNodeHttpConnectionPoolTypeDef = TypedDict(
    "_RequiredVirtualNodeHttpConnectionPoolTypeDef",
    {
        "maxConnections": int,
    },
)
_OptionalVirtualNodeHttpConnectionPoolTypeDef = TypedDict(
    "_OptionalVirtualNodeHttpConnectionPoolTypeDef",
    {
        "maxPendingRequests": int,
    },
    total=False,
)


class VirtualNodeHttpConnectionPoolTypeDef(
    _RequiredVirtualNodeHttpConnectionPoolTypeDef, _OptionalVirtualNodeHttpConnectionPoolTypeDef
):
    pass


VirtualNodeRefTypeDef = TypedDict(
    "VirtualNodeRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "version": int,
        "virtualNodeName": str,
    },
)

VirtualNodeServiceProviderTypeDef = TypedDict(
    "VirtualNodeServiceProviderTypeDef",
    {
        "virtualNodeName": str,
    },
)

VirtualNodeSpecTypeDef = TypedDict(
    "VirtualNodeSpecTypeDef",
    {
        "backendDefaults": "BackendDefaultsTypeDef",
        "backends": List["BackendTypeDef"],
        "listeners": List["ListenerTypeDef"],
        "logging": "LoggingTypeDef",
        "serviceDiscovery": "ServiceDiscoveryTypeDef",
    },
    total=False,
)

VirtualNodeStatusTypeDef = TypedDict(
    "VirtualNodeStatusTypeDef",
    {
        "status": VirtualNodeStatusCodeType,
    },
)

VirtualNodeTcpConnectionPoolTypeDef = TypedDict(
    "VirtualNodeTcpConnectionPoolTypeDef",
    {
        "maxConnections": int,
    },
)

VirtualRouterDataTypeDef = TypedDict(
    "VirtualRouterDataTypeDef",
    {
        "meshName": str,
        "metadata": "ResourceMetadataTypeDef",
        "spec": "VirtualRouterSpecTypeDef",
        "status": "VirtualRouterStatusTypeDef",
        "virtualRouterName": str,
    },
)

VirtualRouterListenerTypeDef = TypedDict(
    "VirtualRouterListenerTypeDef",
    {
        "portMapping": "PortMappingTypeDef",
    },
)

VirtualRouterRefTypeDef = TypedDict(
    "VirtualRouterRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "version": int,
        "virtualRouterName": str,
    },
)

VirtualRouterServiceProviderTypeDef = TypedDict(
    "VirtualRouterServiceProviderTypeDef",
    {
        "virtualRouterName": str,
    },
)

VirtualRouterSpecTypeDef = TypedDict(
    "VirtualRouterSpecTypeDef",
    {
        "listeners": List["VirtualRouterListenerTypeDef"],
    },
    total=False,
)

VirtualRouterStatusTypeDef = TypedDict(
    "VirtualRouterStatusTypeDef",
    {
        "status": VirtualRouterStatusCodeType,
    },
)

_RequiredVirtualServiceBackendTypeDef = TypedDict(
    "_RequiredVirtualServiceBackendTypeDef",
    {
        "virtualServiceName": str,
    },
)
_OptionalVirtualServiceBackendTypeDef = TypedDict(
    "_OptionalVirtualServiceBackendTypeDef",
    {
        "clientPolicy": "ClientPolicyTypeDef",
    },
    total=False,
)


class VirtualServiceBackendTypeDef(
    _RequiredVirtualServiceBackendTypeDef, _OptionalVirtualServiceBackendTypeDef
):
    pass


VirtualServiceDataTypeDef = TypedDict(
    "VirtualServiceDataTypeDef",
    {
        "meshName": str,
        "metadata": "ResourceMetadataTypeDef",
        "spec": "VirtualServiceSpecTypeDef",
        "status": "VirtualServiceStatusTypeDef",
        "virtualServiceName": str,
    },
)

VirtualServiceProviderTypeDef = TypedDict(
    "VirtualServiceProviderTypeDef",
    {
        "virtualNode": "VirtualNodeServiceProviderTypeDef",
        "virtualRouter": "VirtualRouterServiceProviderTypeDef",
    },
    total=False,
)

VirtualServiceRefTypeDef = TypedDict(
    "VirtualServiceRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "version": int,
        "virtualServiceName": str,
    },
)

VirtualServiceSpecTypeDef = TypedDict(
    "VirtualServiceSpecTypeDef",
    {
        "provider": "VirtualServiceProviderTypeDef",
    },
    total=False,
)

VirtualServiceStatusTypeDef = TypedDict(
    "VirtualServiceStatusTypeDef",
    {
        "status": VirtualServiceStatusCodeType,
    },
)

WeightedTargetTypeDef = TypedDict(
    "WeightedTargetTypeDef",
    {
        "virtualNode": str,
        "weight": int,
    },
)
