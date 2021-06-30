from enum import Enum


class CloudProviderDTO(str, Enum):
    AMAZON_WEB_SERVICES = 'amazon_web_services'
    AZURE = 'azure'
