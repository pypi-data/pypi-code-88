"""
Type annotations for iotwireless service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_iotwireless import IoTWirelessClient

    client: IoTWirelessClient = boto3.client("iotwireless")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from .literals import (
    ExpressionTypeType,
    LogLevelType,
    WirelessDeviceIdTypeType,
    WirelessDeviceTypeType,
    WirelessGatewayIdTypeType,
    WirelessGatewayServiceTypeType,
)
from .type_defs import (
    AssociateAwsAccountWithPartnerAccountResponseTypeDef,
    AssociateWirelessGatewayWithCertificateResponseTypeDef,
    CreateDestinationResponseTypeDef,
    CreateDeviceProfileResponseTypeDef,
    CreateServiceProfileResponseTypeDef,
    CreateWirelessDeviceResponseTypeDef,
    CreateWirelessGatewayResponseTypeDef,
    CreateWirelessGatewayTaskDefinitionResponseTypeDef,
    CreateWirelessGatewayTaskResponseTypeDef,
    GetDestinationResponseTypeDef,
    GetDeviceProfileResponseTypeDef,
    GetLogLevelsByResourceTypesResponseTypeDef,
    GetPartnerAccountResponseTypeDef,
    GetResourceLogLevelResponseTypeDef,
    GetServiceEndpointResponseTypeDef,
    GetServiceProfileResponseTypeDef,
    GetWirelessDeviceResponseTypeDef,
    GetWirelessDeviceStatisticsResponseTypeDef,
    GetWirelessGatewayCertificateResponseTypeDef,
    GetWirelessGatewayFirmwareInformationResponseTypeDef,
    GetWirelessGatewayResponseTypeDef,
    GetWirelessGatewayStatisticsResponseTypeDef,
    GetWirelessGatewayTaskDefinitionResponseTypeDef,
    GetWirelessGatewayTaskResponseTypeDef,
    ListDestinationsResponseTypeDef,
    ListDeviceProfilesResponseTypeDef,
    ListPartnerAccountsResponseTypeDef,
    ListServiceProfilesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWirelessDevicesResponseTypeDef,
    ListWirelessGatewaysResponseTypeDef,
    ListWirelessGatewayTaskDefinitionsResponseTypeDef,
    LoRaWANDeviceProfileTypeDef,
    LoRaWANDeviceTypeDef,
    LoRaWANGatewayTypeDef,
    LoRaWANServiceProfileTypeDef,
    LoRaWANUpdateDeviceTypeDef,
    SendDataToWirelessDeviceResponseTypeDef,
    SidewalkAccountInfoTypeDef,
    SidewalkUpdateAccountTypeDef,
    TagTypeDef,
    TestWirelessDeviceResponseTypeDef,
    UpdateWirelessGatewayTaskCreateTypeDef,
    WirelessDeviceLogOptionTypeDef,
    WirelessGatewayLogOptionTypeDef,
    WirelessMetadataTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("IoTWirelessClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class IoTWirelessClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_aws_account_with_partner_account(
        self,
        *,
        Sidewalk: "SidewalkAccountInfoTypeDef",
        ClientRequestToken: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> AssociateAwsAccountWithPartnerAccountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.associate_aws_account_with_partner_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#associate_aws_account_with_partner_account)
        """

    def associate_wireless_device_with_thing(self, *, Id: str, ThingArn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.associate_wireless_device_with_thing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#associate_wireless_device_with_thing)
        """

    def associate_wireless_gateway_with_certificate(
        self, *, Id: str, IotCertificateId: str
    ) -> AssociateWirelessGatewayWithCertificateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.associate_wireless_gateway_with_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#associate_wireless_gateway_with_certificate)
        """

    def associate_wireless_gateway_with_thing(self, *, Id: str, ThingArn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.associate_wireless_gateway_with_thing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#associate_wireless_gateway_with_thing)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#can_paginate)
        """

    def create_destination(
        self,
        *,
        Name: str,
        ExpressionType: ExpressionTypeType,
        Expression: str,
        RoleArn: str,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
        ClientRequestToken: str = None
    ) -> CreateDestinationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.create_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#create_destination)
        """

    def create_device_profile(
        self,
        *,
        Name: str = None,
        LoRaWAN: "LoRaWANDeviceProfileTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        ClientRequestToken: str = None
    ) -> CreateDeviceProfileResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.create_device_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#create_device_profile)
        """

    def create_service_profile(
        self,
        *,
        Name: str = None,
        LoRaWAN: LoRaWANServiceProfileTypeDef = None,
        Tags: List["TagTypeDef"] = None,
        ClientRequestToken: str = None
    ) -> CreateServiceProfileResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.create_service_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#create_service_profile)
        """

    def create_wireless_device(
        self,
        *,
        Type: WirelessDeviceTypeType,
        DestinationName: str,
        Name: str = None,
        Description: str = None,
        ClientRequestToken: str = None,
        LoRaWAN: "LoRaWANDeviceTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateWirelessDeviceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.create_wireless_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#create_wireless_device)
        """

    def create_wireless_gateway(
        self,
        *,
        LoRaWAN: "LoRaWANGatewayTypeDef",
        Name: str = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
        ClientRequestToken: str = None
    ) -> CreateWirelessGatewayResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.create_wireless_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#create_wireless_gateway)
        """

    def create_wireless_gateway_task(
        self, *, Id: str, WirelessGatewayTaskDefinitionId: str
    ) -> CreateWirelessGatewayTaskResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.create_wireless_gateway_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#create_wireless_gateway_task)
        """

    def create_wireless_gateway_task_definition(
        self,
        *,
        AutoCreateTasks: bool,
        Name: str = None,
        Update: "UpdateWirelessGatewayTaskCreateTypeDef" = None,
        ClientRequestToken: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateWirelessGatewayTaskDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.create_wireless_gateway_task_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#create_wireless_gateway_task_definition)
        """

    def delete_destination(self, *, Name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.delete_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#delete_destination)
        """

    def delete_device_profile(self, *, Id: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.delete_device_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#delete_device_profile)
        """

    def delete_service_profile(self, *, Id: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.delete_service_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#delete_service_profile)
        """

    def delete_wireless_device(self, *, Id: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.delete_wireless_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#delete_wireless_device)
        """

    def delete_wireless_gateway(self, *, Id: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.delete_wireless_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#delete_wireless_gateway)
        """

    def delete_wireless_gateway_task(self, *, Id: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.delete_wireless_gateway_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#delete_wireless_gateway_task)
        """

    def delete_wireless_gateway_task_definition(self, *, Id: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.delete_wireless_gateway_task_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#delete_wireless_gateway_task_definition)
        """

    def disassociate_aws_account_from_partner_account(
        self, *, PartnerAccountId: str, PartnerType: Literal["Sidewalk"]
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.disassociate_aws_account_from_partner_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#disassociate_aws_account_from_partner_account)
        """

    def disassociate_wireless_device_from_thing(self, *, Id: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.disassociate_wireless_device_from_thing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#disassociate_wireless_device_from_thing)
        """

    def disassociate_wireless_gateway_from_certificate(self, *, Id: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.disassociate_wireless_gateway_from_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#disassociate_wireless_gateway_from_certificate)
        """

    def disassociate_wireless_gateway_from_thing(self, *, Id: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.disassociate_wireless_gateway_from_thing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#disassociate_wireless_gateway_from_thing)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#generate_presigned_url)
        """

    def get_destination(self, *, Name: str) -> GetDestinationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.get_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_destination)
        """

    def get_device_profile(self, *, Id: str) -> GetDeviceProfileResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.get_device_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_device_profile)
        """

    def get_log_levels_by_resource_types(self) -> GetLogLevelsByResourceTypesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.get_log_levels_by_resource_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_log_levels_by_resource_types)
        """

    def get_partner_account(
        self, *, PartnerAccountId: str, PartnerType: Literal["Sidewalk"]
    ) -> GetPartnerAccountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.get_partner_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_partner_account)
        """

    def get_resource_log_level(
        self, *, ResourceIdentifier: str, ResourceType: str
    ) -> GetResourceLogLevelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.get_resource_log_level)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_resource_log_level)
        """

    def get_service_endpoint(
        self, *, ServiceType: WirelessGatewayServiceTypeType = None
    ) -> GetServiceEndpointResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.get_service_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_service_endpoint)
        """

    def get_service_profile(self, *, Id: str) -> GetServiceProfileResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.get_service_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_service_profile)
        """

    def get_wireless_device(
        self, *, Identifier: str, IdentifierType: WirelessDeviceIdTypeType
    ) -> GetWirelessDeviceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.get_wireless_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_wireless_device)
        """

    def get_wireless_device_statistics(
        self, *, WirelessDeviceId: str
    ) -> GetWirelessDeviceStatisticsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.get_wireless_device_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_wireless_device_statistics)
        """

    def get_wireless_gateway(
        self, *, Identifier: str, IdentifierType: WirelessGatewayIdTypeType
    ) -> GetWirelessGatewayResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.get_wireless_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_wireless_gateway)
        """

    def get_wireless_gateway_certificate(
        self, *, Id: str
    ) -> GetWirelessGatewayCertificateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.get_wireless_gateway_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_wireless_gateway_certificate)
        """

    def get_wireless_gateway_firmware_information(
        self, *, Id: str
    ) -> GetWirelessGatewayFirmwareInformationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.get_wireless_gateway_firmware_information)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_wireless_gateway_firmware_information)
        """

    def get_wireless_gateway_statistics(
        self, *, WirelessGatewayId: str
    ) -> GetWirelessGatewayStatisticsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.get_wireless_gateway_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_wireless_gateway_statistics)
        """

    def get_wireless_gateway_task(self, *, Id: str) -> GetWirelessGatewayTaskResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.get_wireless_gateway_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_wireless_gateway_task)
        """

    def get_wireless_gateway_task_definition(
        self, *, Id: str
    ) -> GetWirelessGatewayTaskDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.get_wireless_gateway_task_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#get_wireless_gateway_task_definition)
        """

    def list_destinations(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListDestinationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.list_destinations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#list_destinations)
        """

    def list_device_profiles(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListDeviceProfilesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.list_device_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#list_device_profiles)
        """

    def list_partner_accounts(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListPartnerAccountsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.list_partner_accounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#list_partner_accounts)
        """

    def list_service_profiles(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListServiceProfilesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.list_service_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#list_service_profiles)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#list_tags_for_resource)
        """

    def list_wireless_devices(
        self,
        *,
        MaxResults: int = None,
        NextToken: str = None,
        DestinationName: str = None,
        DeviceProfileId: str = None,
        ServiceProfileId: str = None,
        WirelessDeviceType: WirelessDeviceTypeType = None
    ) -> ListWirelessDevicesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.list_wireless_devices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#list_wireless_devices)
        """

    def list_wireless_gateway_task_definitions(
        self,
        *,
        MaxResults: int = None,
        NextToken: str = None,
        TaskDefinitionType: Literal["UPDATE"] = None
    ) -> ListWirelessGatewayTaskDefinitionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.list_wireless_gateway_task_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#list_wireless_gateway_task_definitions)
        """

    def list_wireless_gateways(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListWirelessGatewaysResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.list_wireless_gateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#list_wireless_gateways)
        """

    def put_resource_log_level(
        self, *, ResourceIdentifier: str, ResourceType: str, LogLevel: LogLevelType
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.put_resource_log_level)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#put_resource_log_level)
        """

    def reset_all_resource_log_levels(self) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.reset_all_resource_log_levels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#reset_all_resource_log_levels)
        """

    def reset_resource_log_level(
        self, *, ResourceIdentifier: str, ResourceType: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.reset_resource_log_level)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#reset_resource_log_level)
        """

    def send_data_to_wireless_device(
        self,
        *,
        Id: str,
        TransmitMode: int,
        PayloadData: str,
        WirelessMetadata: WirelessMetadataTypeDef = None
    ) -> SendDataToWirelessDeviceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.send_data_to_wireless_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#send_data_to_wireless_device)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#tag_resource)
        """

    def test_wireless_device(self, *, Id: str) -> TestWirelessDeviceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.test_wireless_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#test_wireless_device)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#untag_resource)
        """

    def update_destination(
        self,
        *,
        Name: str,
        ExpressionType: ExpressionTypeType = None,
        Expression: str = None,
        Description: str = None,
        RoleArn: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.update_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#update_destination)
        """

    def update_log_levels_by_resource_types(
        self,
        *,
        DefaultLogLevel: LogLevelType = None,
        WirelessDeviceLogOptions: List["WirelessDeviceLogOptionTypeDef"] = None,
        WirelessGatewayLogOptions: List["WirelessGatewayLogOptionTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.update_log_levels_by_resource_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#update_log_levels_by_resource_types)
        """

    def update_partner_account(
        self,
        *,
        Sidewalk: SidewalkUpdateAccountTypeDef,
        PartnerAccountId: str,
        PartnerType: Literal["Sidewalk"]
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.update_partner_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#update_partner_account)
        """

    def update_wireless_device(
        self,
        *,
        Id: str,
        DestinationName: str = None,
        Name: str = None,
        Description: str = None,
        LoRaWAN: LoRaWANUpdateDeviceTypeDef = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.update_wireless_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#update_wireless_device)
        """

    def update_wireless_gateway(
        self,
        *,
        Id: str,
        Name: str = None,
        Description: str = None,
        JoinEuiFilters: List[List[str]] = None,
        NetIdFilters: List[str] = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotwireless.html#IoTWireless.Client.update_wireless_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/client.html#update_wireless_gateway)
        """
