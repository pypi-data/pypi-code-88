"""
Type annotations for iotwireless service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iotwireless.type_defs import AbpV1_0_xTypeDef

    data: AbpV1_0_xTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import (
    BatteryLevelType,
    ConnectionStatusType,
    DeviceStateType,
    EventType,
    ExpressionTypeType,
    LogLevelType,
    MessageTypeType,
    SigningAlgType,
    WirelessDeviceEventType,
    WirelessDeviceIdTypeType,
    WirelessDeviceTypeType,
    WirelessGatewayEventType,
    WirelessGatewayIdTypeType,
    WirelessGatewayServiceTypeType,
    WirelessGatewayTaskStatusType,
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
    "AbpV1_0_xTypeDef",
    "AbpV1_1TypeDef",
    "AssociateAwsAccountWithPartnerAccountRequestTypeDef",
    "AssociateAwsAccountWithPartnerAccountResponseResponseTypeDef",
    "AssociateWirelessDeviceWithThingRequestTypeDef",
    "AssociateWirelessGatewayWithCertificateRequestTypeDef",
    "AssociateWirelessGatewayWithCertificateResponseResponseTypeDef",
    "AssociateWirelessGatewayWithThingRequestTypeDef",
    "CertificateListTypeDef",
    "CreateDestinationRequestTypeDef",
    "CreateDestinationResponseResponseTypeDef",
    "CreateDeviceProfileRequestTypeDef",
    "CreateDeviceProfileResponseResponseTypeDef",
    "CreateServiceProfileRequestTypeDef",
    "CreateServiceProfileResponseResponseTypeDef",
    "CreateWirelessDeviceRequestTypeDef",
    "CreateWirelessDeviceResponseResponseTypeDef",
    "CreateWirelessGatewayRequestTypeDef",
    "CreateWirelessGatewayResponseResponseTypeDef",
    "CreateWirelessGatewayTaskDefinitionRequestTypeDef",
    "CreateWirelessGatewayTaskDefinitionResponseResponseTypeDef",
    "CreateWirelessGatewayTaskRequestTypeDef",
    "CreateWirelessGatewayTaskResponseResponseTypeDef",
    "DeleteDestinationRequestTypeDef",
    "DeleteDeviceProfileRequestTypeDef",
    "DeleteServiceProfileRequestTypeDef",
    "DeleteWirelessDeviceRequestTypeDef",
    "DeleteWirelessGatewayRequestTypeDef",
    "DeleteWirelessGatewayTaskDefinitionRequestTypeDef",
    "DeleteWirelessGatewayTaskRequestTypeDef",
    "DestinationsTypeDef",
    "DeviceProfileTypeDef",
    "DisassociateAwsAccountFromPartnerAccountRequestTypeDef",
    "DisassociateWirelessDeviceFromThingRequestTypeDef",
    "DisassociateWirelessGatewayFromCertificateRequestTypeDef",
    "DisassociateWirelessGatewayFromThingRequestTypeDef",
    "GetDestinationRequestTypeDef",
    "GetDestinationResponseResponseTypeDef",
    "GetDeviceProfileRequestTypeDef",
    "GetDeviceProfileResponseResponseTypeDef",
    "GetLogLevelsByResourceTypesResponseResponseTypeDef",
    "GetPartnerAccountRequestTypeDef",
    "GetPartnerAccountResponseResponseTypeDef",
    "GetResourceLogLevelRequestTypeDef",
    "GetResourceLogLevelResponseResponseTypeDef",
    "GetServiceEndpointRequestTypeDef",
    "GetServiceEndpointResponseResponseTypeDef",
    "GetServiceProfileRequestTypeDef",
    "GetServiceProfileResponseResponseTypeDef",
    "GetWirelessDeviceRequestTypeDef",
    "GetWirelessDeviceResponseResponseTypeDef",
    "GetWirelessDeviceStatisticsRequestTypeDef",
    "GetWirelessDeviceStatisticsResponseResponseTypeDef",
    "GetWirelessGatewayCertificateRequestTypeDef",
    "GetWirelessGatewayCertificateResponseResponseTypeDef",
    "GetWirelessGatewayFirmwareInformationRequestTypeDef",
    "GetWirelessGatewayFirmwareInformationResponseResponseTypeDef",
    "GetWirelessGatewayRequestTypeDef",
    "GetWirelessGatewayResponseResponseTypeDef",
    "GetWirelessGatewayStatisticsRequestTypeDef",
    "GetWirelessGatewayStatisticsResponseResponseTypeDef",
    "GetWirelessGatewayTaskDefinitionRequestTypeDef",
    "GetWirelessGatewayTaskDefinitionResponseResponseTypeDef",
    "GetWirelessGatewayTaskRequestTypeDef",
    "GetWirelessGatewayTaskResponseResponseTypeDef",
    "ListDestinationsRequestTypeDef",
    "ListDestinationsResponseResponseTypeDef",
    "ListDeviceProfilesRequestTypeDef",
    "ListDeviceProfilesResponseResponseTypeDef",
    "ListPartnerAccountsRequestTypeDef",
    "ListPartnerAccountsResponseResponseTypeDef",
    "ListServiceProfilesRequestTypeDef",
    "ListServiceProfilesResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ListWirelessDevicesRequestTypeDef",
    "ListWirelessDevicesResponseResponseTypeDef",
    "ListWirelessGatewayTaskDefinitionsRequestTypeDef",
    "ListWirelessGatewayTaskDefinitionsResponseResponseTypeDef",
    "ListWirelessGatewaysRequestTypeDef",
    "ListWirelessGatewaysResponseResponseTypeDef",
    "LoRaWANDeviceMetadataTypeDef",
    "LoRaWANDeviceProfileTypeDef",
    "LoRaWANDeviceTypeDef",
    "LoRaWANGatewayCurrentVersionTypeDef",
    "LoRaWANGatewayMetadataTypeDef",
    "LoRaWANGatewayTypeDef",
    "LoRaWANGatewayVersionTypeDef",
    "LoRaWANGetServiceProfileInfoTypeDef",
    "LoRaWANListDeviceTypeDef",
    "LoRaWANSendDataToDeviceTypeDef",
    "LoRaWANServiceProfileTypeDef",
    "LoRaWANUpdateDeviceTypeDef",
    "LoRaWANUpdateGatewayTaskCreateTypeDef",
    "LoRaWANUpdateGatewayTaskEntryTypeDef",
    "OtaaV1_0_xTypeDef",
    "OtaaV1_1TypeDef",
    "PutResourceLogLevelRequestTypeDef",
    "ResetResourceLogLevelRequestTypeDef",
    "ResponseMetadataTypeDef",
    "SendDataToWirelessDeviceRequestTypeDef",
    "SendDataToWirelessDeviceResponseResponseTypeDef",
    "ServiceProfileTypeDef",
    "SessionKeysAbpV1_0_xTypeDef",
    "SessionKeysAbpV1_1TypeDef",
    "SidewalkAccountInfoTypeDef",
    "SidewalkAccountInfoWithFingerprintTypeDef",
    "SidewalkDeviceMetadataTypeDef",
    "SidewalkDeviceTypeDef",
    "SidewalkListDeviceTypeDef",
    "SidewalkSendDataToDeviceTypeDef",
    "SidewalkUpdateAccountTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TestWirelessDeviceRequestTypeDef",
    "TestWirelessDeviceResponseResponseTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateDestinationRequestTypeDef",
    "UpdateLogLevelsByResourceTypesRequestTypeDef",
    "UpdatePartnerAccountRequestTypeDef",
    "UpdateWirelessDeviceRequestTypeDef",
    "UpdateWirelessGatewayRequestTypeDef",
    "UpdateWirelessGatewayTaskCreateTypeDef",
    "UpdateWirelessGatewayTaskEntryTypeDef",
    "WirelessDeviceEventLogOptionTypeDef",
    "WirelessDeviceLogOptionTypeDef",
    "WirelessDeviceStatisticsTypeDef",
    "WirelessGatewayEventLogOptionTypeDef",
    "WirelessGatewayLogOptionTypeDef",
    "WirelessGatewayStatisticsTypeDef",
    "WirelessMetadataTypeDef",
)

AbpV1_0_xTypeDef = TypedDict(
    "AbpV1_0_xTypeDef",
    {
        "DevAddr": str,
        "SessionKeys": "SessionKeysAbpV1_0_xTypeDef",
    },
    total=False,
)

AbpV1_1TypeDef = TypedDict(
    "AbpV1_1TypeDef",
    {
        "DevAddr": str,
        "SessionKeys": "SessionKeysAbpV1_1TypeDef",
    },
    total=False,
)

_RequiredAssociateAwsAccountWithPartnerAccountRequestTypeDef = TypedDict(
    "_RequiredAssociateAwsAccountWithPartnerAccountRequestTypeDef",
    {
        "Sidewalk": "SidewalkAccountInfoTypeDef",
    },
)
_OptionalAssociateAwsAccountWithPartnerAccountRequestTypeDef = TypedDict(
    "_OptionalAssociateAwsAccountWithPartnerAccountRequestTypeDef",
    {
        "ClientRequestToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class AssociateAwsAccountWithPartnerAccountRequestTypeDef(
    _RequiredAssociateAwsAccountWithPartnerAccountRequestTypeDef,
    _OptionalAssociateAwsAccountWithPartnerAccountRequestTypeDef,
):
    pass


AssociateAwsAccountWithPartnerAccountResponseResponseTypeDef = TypedDict(
    "AssociateAwsAccountWithPartnerAccountResponseResponseTypeDef",
    {
        "Sidewalk": "SidewalkAccountInfoTypeDef",
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateWirelessDeviceWithThingRequestTypeDef = TypedDict(
    "AssociateWirelessDeviceWithThingRequestTypeDef",
    {
        "Id": str,
        "ThingArn": str,
    },
)

AssociateWirelessGatewayWithCertificateRequestTypeDef = TypedDict(
    "AssociateWirelessGatewayWithCertificateRequestTypeDef",
    {
        "Id": str,
        "IotCertificateId": str,
    },
)

AssociateWirelessGatewayWithCertificateResponseResponseTypeDef = TypedDict(
    "AssociateWirelessGatewayWithCertificateResponseResponseTypeDef",
    {
        "IotCertificateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateWirelessGatewayWithThingRequestTypeDef = TypedDict(
    "AssociateWirelessGatewayWithThingRequestTypeDef",
    {
        "Id": str,
        "ThingArn": str,
    },
)

CertificateListTypeDef = TypedDict(
    "CertificateListTypeDef",
    {
        "SigningAlg": SigningAlgType,
        "Value": str,
    },
)

_RequiredCreateDestinationRequestTypeDef = TypedDict(
    "_RequiredCreateDestinationRequestTypeDef",
    {
        "Name": str,
        "ExpressionType": ExpressionTypeType,
        "Expression": str,
        "RoleArn": str,
    },
)
_OptionalCreateDestinationRequestTypeDef = TypedDict(
    "_OptionalCreateDestinationRequestTypeDef",
    {
        "Description": str,
        "Tags": List["TagTypeDef"],
        "ClientRequestToken": str,
    },
    total=False,
)


class CreateDestinationRequestTypeDef(
    _RequiredCreateDestinationRequestTypeDef, _OptionalCreateDestinationRequestTypeDef
):
    pass


CreateDestinationResponseResponseTypeDef = TypedDict(
    "CreateDestinationResponseResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDeviceProfileRequestTypeDef = TypedDict(
    "CreateDeviceProfileRequestTypeDef",
    {
        "Name": str,
        "LoRaWAN": "LoRaWANDeviceProfileTypeDef",
        "Tags": List["TagTypeDef"],
        "ClientRequestToken": str,
    },
    total=False,
)

CreateDeviceProfileResponseResponseTypeDef = TypedDict(
    "CreateDeviceProfileResponseResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateServiceProfileRequestTypeDef = TypedDict(
    "CreateServiceProfileRequestTypeDef",
    {
        "Name": str,
        "LoRaWAN": "LoRaWANServiceProfileTypeDef",
        "Tags": List["TagTypeDef"],
        "ClientRequestToken": str,
    },
    total=False,
)

CreateServiceProfileResponseResponseTypeDef = TypedDict(
    "CreateServiceProfileResponseResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWirelessDeviceRequestTypeDef = TypedDict(
    "_RequiredCreateWirelessDeviceRequestTypeDef",
    {
        "Type": WirelessDeviceTypeType,
        "DestinationName": str,
    },
)
_OptionalCreateWirelessDeviceRequestTypeDef = TypedDict(
    "_OptionalCreateWirelessDeviceRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "ClientRequestToken": str,
        "LoRaWAN": "LoRaWANDeviceTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateWirelessDeviceRequestTypeDef(
    _RequiredCreateWirelessDeviceRequestTypeDef, _OptionalCreateWirelessDeviceRequestTypeDef
):
    pass


CreateWirelessDeviceResponseResponseTypeDef = TypedDict(
    "CreateWirelessDeviceResponseResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWirelessGatewayRequestTypeDef = TypedDict(
    "_RequiredCreateWirelessGatewayRequestTypeDef",
    {
        "LoRaWAN": "LoRaWANGatewayTypeDef",
    },
)
_OptionalCreateWirelessGatewayRequestTypeDef = TypedDict(
    "_OptionalCreateWirelessGatewayRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
        "ClientRequestToken": str,
    },
    total=False,
)


class CreateWirelessGatewayRequestTypeDef(
    _RequiredCreateWirelessGatewayRequestTypeDef, _OptionalCreateWirelessGatewayRequestTypeDef
):
    pass


CreateWirelessGatewayResponseResponseTypeDef = TypedDict(
    "CreateWirelessGatewayResponseResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWirelessGatewayTaskDefinitionRequestTypeDef = TypedDict(
    "_RequiredCreateWirelessGatewayTaskDefinitionRequestTypeDef",
    {
        "AutoCreateTasks": bool,
    },
)
_OptionalCreateWirelessGatewayTaskDefinitionRequestTypeDef = TypedDict(
    "_OptionalCreateWirelessGatewayTaskDefinitionRequestTypeDef",
    {
        "Name": str,
        "Update": "UpdateWirelessGatewayTaskCreateTypeDef",
        "ClientRequestToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateWirelessGatewayTaskDefinitionRequestTypeDef(
    _RequiredCreateWirelessGatewayTaskDefinitionRequestTypeDef,
    _OptionalCreateWirelessGatewayTaskDefinitionRequestTypeDef,
):
    pass


CreateWirelessGatewayTaskDefinitionResponseResponseTypeDef = TypedDict(
    "CreateWirelessGatewayTaskDefinitionResponseResponseTypeDef",
    {
        "Id": str,
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWirelessGatewayTaskRequestTypeDef = TypedDict(
    "CreateWirelessGatewayTaskRequestTypeDef",
    {
        "Id": str,
        "WirelessGatewayTaskDefinitionId": str,
    },
)

CreateWirelessGatewayTaskResponseResponseTypeDef = TypedDict(
    "CreateWirelessGatewayTaskResponseResponseTypeDef",
    {
        "WirelessGatewayTaskDefinitionId": str,
        "Status": WirelessGatewayTaskStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDestinationRequestTypeDef = TypedDict(
    "DeleteDestinationRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteDeviceProfileRequestTypeDef = TypedDict(
    "DeleteDeviceProfileRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteServiceProfileRequestTypeDef = TypedDict(
    "DeleteServiceProfileRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteWirelessDeviceRequestTypeDef = TypedDict(
    "DeleteWirelessDeviceRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteWirelessGatewayRequestTypeDef = TypedDict(
    "DeleteWirelessGatewayRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteWirelessGatewayTaskDefinitionRequestTypeDef = TypedDict(
    "DeleteWirelessGatewayTaskDefinitionRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteWirelessGatewayTaskRequestTypeDef = TypedDict(
    "DeleteWirelessGatewayTaskRequestTypeDef",
    {
        "Id": str,
    },
)

DestinationsTypeDef = TypedDict(
    "DestinationsTypeDef",
    {
        "Arn": str,
        "Name": str,
        "ExpressionType": ExpressionTypeType,
        "Expression": str,
        "Description": str,
        "RoleArn": str,
    },
    total=False,
)

DeviceProfileTypeDef = TypedDict(
    "DeviceProfileTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Id": str,
    },
    total=False,
)

DisassociateAwsAccountFromPartnerAccountRequestTypeDef = TypedDict(
    "DisassociateAwsAccountFromPartnerAccountRequestTypeDef",
    {
        "PartnerAccountId": str,
        "PartnerType": Literal["Sidewalk"],
    },
)

DisassociateWirelessDeviceFromThingRequestTypeDef = TypedDict(
    "DisassociateWirelessDeviceFromThingRequestTypeDef",
    {
        "Id": str,
    },
)

DisassociateWirelessGatewayFromCertificateRequestTypeDef = TypedDict(
    "DisassociateWirelessGatewayFromCertificateRequestTypeDef",
    {
        "Id": str,
    },
)

DisassociateWirelessGatewayFromThingRequestTypeDef = TypedDict(
    "DisassociateWirelessGatewayFromThingRequestTypeDef",
    {
        "Id": str,
    },
)

GetDestinationRequestTypeDef = TypedDict(
    "GetDestinationRequestTypeDef",
    {
        "Name": str,
    },
)

GetDestinationResponseResponseTypeDef = TypedDict(
    "GetDestinationResponseResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Expression": str,
        "ExpressionType": ExpressionTypeType,
        "Description": str,
        "RoleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeviceProfileRequestTypeDef = TypedDict(
    "GetDeviceProfileRequestTypeDef",
    {
        "Id": str,
    },
)

GetDeviceProfileResponseResponseTypeDef = TypedDict(
    "GetDeviceProfileResponseResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Id": str,
        "LoRaWAN": "LoRaWANDeviceProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLogLevelsByResourceTypesResponseResponseTypeDef = TypedDict(
    "GetLogLevelsByResourceTypesResponseResponseTypeDef",
    {
        "DefaultLogLevel": LogLevelType,
        "WirelessGatewayLogOptions": List["WirelessGatewayLogOptionTypeDef"],
        "WirelessDeviceLogOptions": List["WirelessDeviceLogOptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPartnerAccountRequestTypeDef = TypedDict(
    "GetPartnerAccountRequestTypeDef",
    {
        "PartnerAccountId": str,
        "PartnerType": Literal["Sidewalk"],
    },
)

GetPartnerAccountResponseResponseTypeDef = TypedDict(
    "GetPartnerAccountResponseResponseTypeDef",
    {
        "Sidewalk": "SidewalkAccountInfoWithFingerprintTypeDef",
        "AccountLinked": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourceLogLevelRequestTypeDef = TypedDict(
    "GetResourceLogLevelRequestTypeDef",
    {
        "ResourceIdentifier": str,
        "ResourceType": str,
    },
)

GetResourceLogLevelResponseResponseTypeDef = TypedDict(
    "GetResourceLogLevelResponseResponseTypeDef",
    {
        "LogLevel": LogLevelType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceEndpointRequestTypeDef = TypedDict(
    "GetServiceEndpointRequestTypeDef",
    {
        "ServiceType": WirelessGatewayServiceTypeType,
    },
    total=False,
)

GetServiceEndpointResponseResponseTypeDef = TypedDict(
    "GetServiceEndpointResponseResponseTypeDef",
    {
        "ServiceType": WirelessGatewayServiceTypeType,
        "ServiceEndpoint": str,
        "ServerTrust": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceProfileRequestTypeDef = TypedDict(
    "GetServiceProfileRequestTypeDef",
    {
        "Id": str,
    },
)

GetServiceProfileResponseResponseTypeDef = TypedDict(
    "GetServiceProfileResponseResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Id": str,
        "LoRaWAN": "LoRaWANGetServiceProfileInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWirelessDeviceRequestTypeDef = TypedDict(
    "GetWirelessDeviceRequestTypeDef",
    {
        "Identifier": str,
        "IdentifierType": WirelessDeviceIdTypeType,
    },
)

GetWirelessDeviceResponseResponseTypeDef = TypedDict(
    "GetWirelessDeviceResponseResponseTypeDef",
    {
        "Type": WirelessDeviceTypeType,
        "Name": str,
        "Description": str,
        "DestinationName": str,
        "Id": str,
        "Arn": str,
        "ThingName": str,
        "ThingArn": str,
        "LoRaWAN": "LoRaWANDeviceTypeDef",
        "Sidewalk": "SidewalkDeviceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWirelessDeviceStatisticsRequestTypeDef = TypedDict(
    "GetWirelessDeviceStatisticsRequestTypeDef",
    {
        "WirelessDeviceId": str,
    },
)

GetWirelessDeviceStatisticsResponseResponseTypeDef = TypedDict(
    "GetWirelessDeviceStatisticsResponseResponseTypeDef",
    {
        "WirelessDeviceId": str,
        "LastUplinkReceivedAt": str,
        "LoRaWAN": "LoRaWANDeviceMetadataTypeDef",
        "Sidewalk": "SidewalkDeviceMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWirelessGatewayCertificateRequestTypeDef = TypedDict(
    "GetWirelessGatewayCertificateRequestTypeDef",
    {
        "Id": str,
    },
)

GetWirelessGatewayCertificateResponseResponseTypeDef = TypedDict(
    "GetWirelessGatewayCertificateResponseResponseTypeDef",
    {
        "IotCertificateId": str,
        "LoRaWANNetworkServerCertificateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWirelessGatewayFirmwareInformationRequestTypeDef = TypedDict(
    "GetWirelessGatewayFirmwareInformationRequestTypeDef",
    {
        "Id": str,
    },
)

GetWirelessGatewayFirmwareInformationResponseResponseTypeDef = TypedDict(
    "GetWirelessGatewayFirmwareInformationResponseResponseTypeDef",
    {
        "LoRaWAN": "LoRaWANGatewayCurrentVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWirelessGatewayRequestTypeDef = TypedDict(
    "GetWirelessGatewayRequestTypeDef",
    {
        "Identifier": str,
        "IdentifierType": WirelessGatewayIdTypeType,
    },
)

GetWirelessGatewayResponseResponseTypeDef = TypedDict(
    "GetWirelessGatewayResponseResponseTypeDef",
    {
        "Name": str,
        "Id": str,
        "Description": str,
        "LoRaWAN": "LoRaWANGatewayTypeDef",
        "Arn": str,
        "ThingName": str,
        "ThingArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWirelessGatewayStatisticsRequestTypeDef = TypedDict(
    "GetWirelessGatewayStatisticsRequestTypeDef",
    {
        "WirelessGatewayId": str,
    },
)

GetWirelessGatewayStatisticsResponseResponseTypeDef = TypedDict(
    "GetWirelessGatewayStatisticsResponseResponseTypeDef",
    {
        "WirelessGatewayId": str,
        "LastUplinkReceivedAt": str,
        "ConnectionStatus": ConnectionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWirelessGatewayTaskDefinitionRequestTypeDef = TypedDict(
    "GetWirelessGatewayTaskDefinitionRequestTypeDef",
    {
        "Id": str,
    },
)

GetWirelessGatewayTaskDefinitionResponseResponseTypeDef = TypedDict(
    "GetWirelessGatewayTaskDefinitionResponseResponseTypeDef",
    {
        "AutoCreateTasks": bool,
        "Name": str,
        "Update": "UpdateWirelessGatewayTaskCreateTypeDef",
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWirelessGatewayTaskRequestTypeDef = TypedDict(
    "GetWirelessGatewayTaskRequestTypeDef",
    {
        "Id": str,
    },
)

GetWirelessGatewayTaskResponseResponseTypeDef = TypedDict(
    "GetWirelessGatewayTaskResponseResponseTypeDef",
    {
        "WirelessGatewayId": str,
        "WirelessGatewayTaskDefinitionId": str,
        "LastUplinkReceivedAt": str,
        "TaskCreatedAt": str,
        "Status": WirelessGatewayTaskStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDestinationsRequestTypeDef = TypedDict(
    "ListDestinationsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListDestinationsResponseResponseTypeDef = TypedDict(
    "ListDestinationsResponseResponseTypeDef",
    {
        "NextToken": str,
        "DestinationList": List["DestinationsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeviceProfilesRequestTypeDef = TypedDict(
    "ListDeviceProfilesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDeviceProfilesResponseResponseTypeDef = TypedDict(
    "ListDeviceProfilesResponseResponseTypeDef",
    {
        "NextToken": str,
        "DeviceProfileList": List["DeviceProfileTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPartnerAccountsRequestTypeDef = TypedDict(
    "ListPartnerAccountsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListPartnerAccountsResponseResponseTypeDef = TypedDict(
    "ListPartnerAccountsResponseResponseTypeDef",
    {
        "NextToken": str,
        "Sidewalk": List["SidewalkAccountInfoWithFingerprintTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServiceProfilesRequestTypeDef = TypedDict(
    "ListServiceProfilesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListServiceProfilesResponseResponseTypeDef = TypedDict(
    "ListServiceProfilesResponseResponseTypeDef",
    {
        "NextToken": str,
        "ServiceProfileList": List["ServiceProfileTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWirelessDevicesRequestTypeDef = TypedDict(
    "ListWirelessDevicesRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "DestinationName": str,
        "DeviceProfileId": str,
        "ServiceProfileId": str,
        "WirelessDeviceType": WirelessDeviceTypeType,
    },
    total=False,
)

ListWirelessDevicesResponseResponseTypeDef = TypedDict(
    "ListWirelessDevicesResponseResponseTypeDef",
    {
        "NextToken": str,
        "WirelessDeviceList": List["WirelessDeviceStatisticsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWirelessGatewayTaskDefinitionsRequestTypeDef = TypedDict(
    "ListWirelessGatewayTaskDefinitionsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "TaskDefinitionType": Literal["UPDATE"],
    },
    total=False,
)

ListWirelessGatewayTaskDefinitionsResponseResponseTypeDef = TypedDict(
    "ListWirelessGatewayTaskDefinitionsResponseResponseTypeDef",
    {
        "NextToken": str,
        "TaskDefinitions": List["UpdateWirelessGatewayTaskEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWirelessGatewaysRequestTypeDef = TypedDict(
    "ListWirelessGatewaysRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListWirelessGatewaysResponseResponseTypeDef = TypedDict(
    "ListWirelessGatewaysResponseResponseTypeDef",
    {
        "NextToken": str,
        "WirelessGatewayList": List["WirelessGatewayStatisticsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoRaWANDeviceMetadataTypeDef = TypedDict(
    "LoRaWANDeviceMetadataTypeDef",
    {
        "DevEui": str,
        "FPort": int,
        "DataRate": int,
        "Frequency": int,
        "Timestamp": str,
        "Gateways": List["LoRaWANGatewayMetadataTypeDef"],
    },
    total=False,
)

LoRaWANDeviceProfileTypeDef = TypedDict(
    "LoRaWANDeviceProfileTypeDef",
    {
        "SupportsClassB": bool,
        "ClassBTimeout": int,
        "PingSlotPeriod": int,
        "PingSlotDr": int,
        "PingSlotFreq": int,
        "SupportsClassC": bool,
        "ClassCTimeout": int,
        "MacVersion": str,
        "RegParamsRevision": str,
        "RxDelay1": int,
        "RxDrOffset1": int,
        "RxDataRate2": int,
        "RxFreq2": int,
        "FactoryPresetFreqsList": List[int],
        "MaxEirp": int,
        "MaxDutyCycle": int,
        "RfRegion": str,
        "SupportsJoin": bool,
        "Supports32BitFCnt": bool,
    },
    total=False,
)

LoRaWANDeviceTypeDef = TypedDict(
    "LoRaWANDeviceTypeDef",
    {
        "DevEui": str,
        "DeviceProfileId": str,
        "ServiceProfileId": str,
        "OtaaV1_1": "OtaaV1_1TypeDef",
        "OtaaV1_0_x": "OtaaV1_0_xTypeDef",
        "AbpV1_1": "AbpV1_1TypeDef",
        "AbpV1_0_x": "AbpV1_0_xTypeDef",
    },
    total=False,
)

LoRaWANGatewayCurrentVersionTypeDef = TypedDict(
    "LoRaWANGatewayCurrentVersionTypeDef",
    {
        "CurrentVersion": "LoRaWANGatewayVersionTypeDef",
    },
    total=False,
)

LoRaWANGatewayMetadataTypeDef = TypedDict(
    "LoRaWANGatewayMetadataTypeDef",
    {
        "GatewayEui": str,
        "Snr": float,
        "Rssi": float,
    },
    total=False,
)

LoRaWANGatewayTypeDef = TypedDict(
    "LoRaWANGatewayTypeDef",
    {
        "GatewayEui": str,
        "RfRegion": str,
        "JoinEuiFilters": List[List[str]],
        "NetIdFilters": List[str],
        "SubBands": List[int],
    },
    total=False,
)

LoRaWANGatewayVersionTypeDef = TypedDict(
    "LoRaWANGatewayVersionTypeDef",
    {
        "PackageVersion": str,
        "Model": str,
        "Station": str,
    },
    total=False,
)

LoRaWANGetServiceProfileInfoTypeDef = TypedDict(
    "LoRaWANGetServiceProfileInfoTypeDef",
    {
        "UlRate": int,
        "UlBucketSize": int,
        "UlRatePolicy": str,
        "DlRate": int,
        "DlBucketSize": int,
        "DlRatePolicy": str,
        "AddGwMetadata": bool,
        "DevStatusReqFreq": int,
        "ReportDevStatusBattery": bool,
        "ReportDevStatusMargin": bool,
        "DrMin": int,
        "DrMax": int,
        "ChannelMask": str,
        "PrAllowed": bool,
        "HrAllowed": bool,
        "RaAllowed": bool,
        "NwkGeoLoc": bool,
        "TargetPer": int,
        "MinGwDiversity": int,
    },
    total=False,
)

LoRaWANListDeviceTypeDef = TypedDict(
    "LoRaWANListDeviceTypeDef",
    {
        "DevEui": str,
    },
    total=False,
)

LoRaWANSendDataToDeviceTypeDef = TypedDict(
    "LoRaWANSendDataToDeviceTypeDef",
    {
        "FPort": int,
    },
    total=False,
)

LoRaWANServiceProfileTypeDef = TypedDict(
    "LoRaWANServiceProfileTypeDef",
    {
        "AddGwMetadata": bool,
    },
    total=False,
)

LoRaWANUpdateDeviceTypeDef = TypedDict(
    "LoRaWANUpdateDeviceTypeDef",
    {
        "DeviceProfileId": str,
        "ServiceProfileId": str,
    },
    total=False,
)

LoRaWANUpdateGatewayTaskCreateTypeDef = TypedDict(
    "LoRaWANUpdateGatewayTaskCreateTypeDef",
    {
        "UpdateSignature": str,
        "SigKeyCrc": int,
        "CurrentVersion": "LoRaWANGatewayVersionTypeDef",
        "UpdateVersion": "LoRaWANGatewayVersionTypeDef",
    },
    total=False,
)

LoRaWANUpdateGatewayTaskEntryTypeDef = TypedDict(
    "LoRaWANUpdateGatewayTaskEntryTypeDef",
    {
        "CurrentVersion": "LoRaWANGatewayVersionTypeDef",
        "UpdateVersion": "LoRaWANGatewayVersionTypeDef",
    },
    total=False,
)

OtaaV1_0_xTypeDef = TypedDict(
    "OtaaV1_0_xTypeDef",
    {
        "AppKey": str,
        "AppEui": str,
    },
    total=False,
)

OtaaV1_1TypeDef = TypedDict(
    "OtaaV1_1TypeDef",
    {
        "AppKey": str,
        "NwkKey": str,
        "JoinEui": str,
    },
    total=False,
)

PutResourceLogLevelRequestTypeDef = TypedDict(
    "PutResourceLogLevelRequestTypeDef",
    {
        "ResourceIdentifier": str,
        "ResourceType": str,
        "LogLevel": LogLevelType,
    },
)

ResetResourceLogLevelRequestTypeDef = TypedDict(
    "ResetResourceLogLevelRequestTypeDef",
    {
        "ResourceIdentifier": str,
        "ResourceType": str,
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

_RequiredSendDataToWirelessDeviceRequestTypeDef = TypedDict(
    "_RequiredSendDataToWirelessDeviceRequestTypeDef",
    {
        "Id": str,
        "TransmitMode": int,
        "PayloadData": str,
    },
)
_OptionalSendDataToWirelessDeviceRequestTypeDef = TypedDict(
    "_OptionalSendDataToWirelessDeviceRequestTypeDef",
    {
        "WirelessMetadata": "WirelessMetadataTypeDef",
    },
    total=False,
)


class SendDataToWirelessDeviceRequestTypeDef(
    _RequiredSendDataToWirelessDeviceRequestTypeDef, _OptionalSendDataToWirelessDeviceRequestTypeDef
):
    pass


SendDataToWirelessDeviceResponseResponseTypeDef = TypedDict(
    "SendDataToWirelessDeviceResponseResponseTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServiceProfileTypeDef = TypedDict(
    "ServiceProfileTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Id": str,
    },
    total=False,
)

SessionKeysAbpV1_0_xTypeDef = TypedDict(
    "SessionKeysAbpV1_0_xTypeDef",
    {
        "NwkSKey": str,
        "AppSKey": str,
    },
    total=False,
)

SessionKeysAbpV1_1TypeDef = TypedDict(
    "SessionKeysAbpV1_1TypeDef",
    {
        "FNwkSIntKey": str,
        "SNwkSIntKey": str,
        "NwkSEncKey": str,
        "AppSKey": str,
    },
    total=False,
)

SidewalkAccountInfoTypeDef = TypedDict(
    "SidewalkAccountInfoTypeDef",
    {
        "AmazonId": str,
        "AppServerPrivateKey": str,
    },
    total=False,
)

SidewalkAccountInfoWithFingerprintTypeDef = TypedDict(
    "SidewalkAccountInfoWithFingerprintTypeDef",
    {
        "AmazonId": str,
        "Fingerprint": str,
        "Arn": str,
    },
    total=False,
)

SidewalkDeviceMetadataTypeDef = TypedDict(
    "SidewalkDeviceMetadataTypeDef",
    {
        "Rssi": int,
        "BatteryLevel": BatteryLevelType,
        "Event": EventType,
        "DeviceState": DeviceStateType,
    },
    total=False,
)

SidewalkDeviceTypeDef = TypedDict(
    "SidewalkDeviceTypeDef",
    {
        "SidewalkId": str,
        "SidewalkManufacturingSn": str,
        "DeviceCertificates": List["CertificateListTypeDef"],
    },
    total=False,
)

SidewalkListDeviceTypeDef = TypedDict(
    "SidewalkListDeviceTypeDef",
    {
        "AmazonId": str,
        "SidewalkId": str,
        "SidewalkManufacturingSn": str,
        "DeviceCertificates": List["CertificateListTypeDef"],
    },
    total=False,
)

SidewalkSendDataToDeviceTypeDef = TypedDict(
    "SidewalkSendDataToDeviceTypeDef",
    {
        "Seq": int,
        "MessageType": MessageTypeType,
    },
    total=False,
)

SidewalkUpdateAccountTypeDef = TypedDict(
    "SidewalkUpdateAccountTypeDef",
    {
        "AppServerPrivateKey": str,
    },
    total=False,
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TestWirelessDeviceRequestTypeDef = TypedDict(
    "TestWirelessDeviceRequestTypeDef",
    {
        "Id": str,
    },
)

TestWirelessDeviceResponseResponseTypeDef = TypedDict(
    "TestWirelessDeviceResponseResponseTypeDef",
    {
        "Result": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateDestinationRequestTypeDef = TypedDict(
    "_RequiredUpdateDestinationRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateDestinationRequestTypeDef = TypedDict(
    "_OptionalUpdateDestinationRequestTypeDef",
    {
        "ExpressionType": ExpressionTypeType,
        "Expression": str,
        "Description": str,
        "RoleArn": str,
    },
    total=False,
)


class UpdateDestinationRequestTypeDef(
    _RequiredUpdateDestinationRequestTypeDef, _OptionalUpdateDestinationRequestTypeDef
):
    pass


UpdateLogLevelsByResourceTypesRequestTypeDef = TypedDict(
    "UpdateLogLevelsByResourceTypesRequestTypeDef",
    {
        "DefaultLogLevel": LogLevelType,
        "WirelessDeviceLogOptions": List["WirelessDeviceLogOptionTypeDef"],
        "WirelessGatewayLogOptions": List["WirelessGatewayLogOptionTypeDef"],
    },
    total=False,
)

UpdatePartnerAccountRequestTypeDef = TypedDict(
    "UpdatePartnerAccountRequestTypeDef",
    {
        "Sidewalk": "SidewalkUpdateAccountTypeDef",
        "PartnerAccountId": str,
        "PartnerType": Literal["Sidewalk"],
    },
)

_RequiredUpdateWirelessDeviceRequestTypeDef = TypedDict(
    "_RequiredUpdateWirelessDeviceRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalUpdateWirelessDeviceRequestTypeDef = TypedDict(
    "_OptionalUpdateWirelessDeviceRequestTypeDef",
    {
        "DestinationName": str,
        "Name": str,
        "Description": str,
        "LoRaWAN": "LoRaWANUpdateDeviceTypeDef",
    },
    total=False,
)


class UpdateWirelessDeviceRequestTypeDef(
    _RequiredUpdateWirelessDeviceRequestTypeDef, _OptionalUpdateWirelessDeviceRequestTypeDef
):
    pass


_RequiredUpdateWirelessGatewayRequestTypeDef = TypedDict(
    "_RequiredUpdateWirelessGatewayRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalUpdateWirelessGatewayRequestTypeDef = TypedDict(
    "_OptionalUpdateWirelessGatewayRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "JoinEuiFilters": List[List[str]],
        "NetIdFilters": List[str],
    },
    total=False,
)


class UpdateWirelessGatewayRequestTypeDef(
    _RequiredUpdateWirelessGatewayRequestTypeDef, _OptionalUpdateWirelessGatewayRequestTypeDef
):
    pass


UpdateWirelessGatewayTaskCreateTypeDef = TypedDict(
    "UpdateWirelessGatewayTaskCreateTypeDef",
    {
        "UpdateDataSource": str,
        "UpdateDataRole": str,
        "LoRaWAN": "LoRaWANUpdateGatewayTaskCreateTypeDef",
    },
    total=False,
)

UpdateWirelessGatewayTaskEntryTypeDef = TypedDict(
    "UpdateWirelessGatewayTaskEntryTypeDef",
    {
        "Id": str,
        "LoRaWAN": "LoRaWANUpdateGatewayTaskEntryTypeDef",
        "Arn": str,
    },
    total=False,
)

WirelessDeviceEventLogOptionTypeDef = TypedDict(
    "WirelessDeviceEventLogOptionTypeDef",
    {
        "Event": WirelessDeviceEventType,
        "LogLevel": LogLevelType,
    },
)

_RequiredWirelessDeviceLogOptionTypeDef = TypedDict(
    "_RequiredWirelessDeviceLogOptionTypeDef",
    {
        "Type": WirelessDeviceTypeType,
        "LogLevel": LogLevelType,
    },
)
_OptionalWirelessDeviceLogOptionTypeDef = TypedDict(
    "_OptionalWirelessDeviceLogOptionTypeDef",
    {
        "Events": List["WirelessDeviceEventLogOptionTypeDef"],
    },
    total=False,
)


class WirelessDeviceLogOptionTypeDef(
    _RequiredWirelessDeviceLogOptionTypeDef, _OptionalWirelessDeviceLogOptionTypeDef
):
    pass


WirelessDeviceStatisticsTypeDef = TypedDict(
    "WirelessDeviceStatisticsTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Type": WirelessDeviceTypeType,
        "Name": str,
        "DestinationName": str,
        "LastUplinkReceivedAt": str,
        "LoRaWAN": "LoRaWANListDeviceTypeDef",
        "Sidewalk": "SidewalkListDeviceTypeDef",
    },
    total=False,
)

WirelessGatewayEventLogOptionTypeDef = TypedDict(
    "WirelessGatewayEventLogOptionTypeDef",
    {
        "Event": WirelessGatewayEventType,
        "LogLevel": LogLevelType,
    },
)

_RequiredWirelessGatewayLogOptionTypeDef = TypedDict(
    "_RequiredWirelessGatewayLogOptionTypeDef",
    {
        "Type": Literal["LoRaWAN"],
        "LogLevel": LogLevelType,
    },
)
_OptionalWirelessGatewayLogOptionTypeDef = TypedDict(
    "_OptionalWirelessGatewayLogOptionTypeDef",
    {
        "Events": List["WirelessGatewayEventLogOptionTypeDef"],
    },
    total=False,
)


class WirelessGatewayLogOptionTypeDef(
    _RequiredWirelessGatewayLogOptionTypeDef, _OptionalWirelessGatewayLogOptionTypeDef
):
    pass


WirelessGatewayStatisticsTypeDef = TypedDict(
    "WirelessGatewayStatisticsTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "LoRaWAN": "LoRaWANGatewayTypeDef",
        "LastUplinkReceivedAt": str,
    },
    total=False,
)

WirelessMetadataTypeDef = TypedDict(
    "WirelessMetadataTypeDef",
    {
        "LoRaWAN": "LoRaWANSendDataToDeviceTypeDef",
        "Sidewalk": "SidewalkSendDataToDeviceTypeDef",
    },
    total=False,
)
