from checkov.cloudformation.checks.resource.base_resource_value_check import BaseResourceValueCheck
from checkov.common.models.enums import CheckCategories
from checkov.common.models.consts import ANY_VALUE


class APIGatewayV2AccessLogging(BaseResourceValueCheck):
    def __init__(self):
        name = "Ensure API Gateway V2 has Access Logging enabled"
        id = "CKV_AWS_95"
        supported_resources = ['AWS::ApiGatewayV2::Stage']
        categories = [CheckCategories.LOGGING]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def get_inspected_key(self):
        return 'Properties/AccessLogSettings/DestinationArn'

    def get_expected_value(self):
        return ANY_VALUE


check = APIGatewayV2AccessLogging()
