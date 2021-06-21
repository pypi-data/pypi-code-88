"""
Type annotations for customer-profiles service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/type_defs.html)

Usage::

    ```python
    from mypy_boto3_customer_profiles.type_defs import AddProfileKeyResponseTypeDef

    data: AddProfileKeyResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from .literals import (
    DataPullModeType,
    FieldContentTypeType,
    GenderType,
    MarketoConnectorOperatorType,
    OperatorPropertiesKeysType,
    PartyTypeType,
    S3ConnectorOperatorType,
    SalesforceConnectorOperatorType,
    ServiceNowConnectorOperatorType,
    SourceConnectorTypeType,
    StandardIdentifierType,
    TaskTypeType,
    TriggerTypeType,
    ZendeskConnectorOperatorType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddProfileKeyResponseTypeDef",
    "AddressTypeDef",
    "ConnectorOperatorTypeDef",
    "CreateDomainResponseTypeDef",
    "CreateProfileResponseTypeDef",
    "DeleteDomainResponseTypeDef",
    "DeleteIntegrationResponseTypeDef",
    "DeleteProfileKeyResponseTypeDef",
    "DeleteProfileObjectResponseTypeDef",
    "DeleteProfileObjectTypeResponseTypeDef",
    "DeleteProfileResponseTypeDef",
    "DomainStatsTypeDef",
    "FieldSourceProfileIdsTypeDef",
    "FlowDefinitionTypeDef",
    "GetDomainResponseTypeDef",
    "GetIntegrationResponseTypeDef",
    "GetMatchesResponseTypeDef",
    "GetProfileObjectTypeResponseTypeDef",
    "GetProfileObjectTypeTemplateResponseTypeDef",
    "IncrementalPullConfigTypeDef",
    "ListAccountIntegrationsResponseTypeDef",
    "ListDomainItemTypeDef",
    "ListDomainsResponseTypeDef",
    "ListIntegrationItemTypeDef",
    "ListIntegrationsResponseTypeDef",
    "ListProfileObjectTypeItemTypeDef",
    "ListProfileObjectTypeTemplateItemTypeDef",
    "ListProfileObjectTypeTemplatesResponseTypeDef",
    "ListProfileObjectTypesResponseTypeDef",
    "ListProfileObjectsItemTypeDef",
    "ListProfileObjectsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MarketoSourcePropertiesTypeDef",
    "MatchItemTypeDef",
    "MatchingRequestTypeDef",
    "MatchingResponseTypeDef",
    "MergeProfilesResponseTypeDef",
    "ObjectTypeFieldTypeDef",
    "ObjectTypeKeyTypeDef",
    "ProfileTypeDef",
    "PutIntegrationResponseTypeDef",
    "PutProfileObjectResponseTypeDef",
    "PutProfileObjectTypeResponseTypeDef",
    "S3SourcePropertiesTypeDef",
    "SalesforceSourcePropertiesTypeDef",
    "ScheduledTriggerPropertiesTypeDef",
    "SearchProfilesResponseTypeDef",
    "ServiceNowSourcePropertiesTypeDef",
    "SourceConnectorPropertiesTypeDef",
    "SourceFlowConfigTypeDef",
    "TaskTypeDef",
    "TriggerConfigTypeDef",
    "TriggerPropertiesTypeDef",
    "UpdateAddressTypeDef",
    "UpdateDomainResponseTypeDef",
    "UpdateProfileResponseTypeDef",
    "ZendeskSourcePropertiesTypeDef",
)

AddProfileKeyResponseTypeDef = TypedDict(
    "AddProfileKeyResponseTypeDef",
    {
        "KeyName": str,
        "Values": List[str],
    },
    total=False,
)

AddressTypeDef = TypedDict(
    "AddressTypeDef",
    {
        "Address1": str,
        "Address2": str,
        "Address3": str,
        "Address4": str,
        "City": str,
        "County": str,
        "State": str,
        "Province": str,
        "Country": str,
        "PostalCode": str,
    },
    total=False,
)

ConnectorOperatorTypeDef = TypedDict(
    "ConnectorOperatorTypeDef",
    {
        "Marketo": MarketoConnectorOperatorType,
        "S3": S3ConnectorOperatorType,
        "Salesforce": SalesforceConnectorOperatorType,
        "ServiceNow": ServiceNowConnectorOperatorType,
        "Zendesk": ZendeskConnectorOperatorType,
    },
    total=False,
)

_RequiredCreateDomainResponseTypeDef = TypedDict(
    "_RequiredCreateDomainResponseTypeDef",
    {
        "DomainName": str,
        "DefaultExpirationDays": int,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
)
_OptionalCreateDomainResponseTypeDef = TypedDict(
    "_OptionalCreateDomainResponseTypeDef",
    {
        "DefaultEncryptionKey": str,
        "DeadLetterQueueUrl": str,
        "Matching": "MatchingResponseTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateDomainResponseTypeDef(
    _RequiredCreateDomainResponseTypeDef, _OptionalCreateDomainResponseTypeDef
):
    pass


CreateProfileResponseTypeDef = TypedDict(
    "CreateProfileResponseTypeDef",
    {
        "ProfileId": str,
    },
)

DeleteDomainResponseTypeDef = TypedDict(
    "DeleteDomainResponseTypeDef",
    {
        "Message": str,
    },
)

DeleteIntegrationResponseTypeDef = TypedDict(
    "DeleteIntegrationResponseTypeDef",
    {
        "Message": str,
    },
)

DeleteProfileKeyResponseTypeDef = TypedDict(
    "DeleteProfileKeyResponseTypeDef",
    {
        "Message": str,
    },
    total=False,
)

DeleteProfileObjectResponseTypeDef = TypedDict(
    "DeleteProfileObjectResponseTypeDef",
    {
        "Message": str,
    },
    total=False,
)

DeleteProfileObjectTypeResponseTypeDef = TypedDict(
    "DeleteProfileObjectTypeResponseTypeDef",
    {
        "Message": str,
    },
)

DeleteProfileResponseTypeDef = TypedDict(
    "DeleteProfileResponseTypeDef",
    {
        "Message": str,
    },
    total=False,
)

DomainStatsTypeDef = TypedDict(
    "DomainStatsTypeDef",
    {
        "ProfileCount": int,
        "MeteringProfileCount": int,
        "ObjectCount": int,
        "TotalSize": int,
    },
    total=False,
)

FieldSourceProfileIdsTypeDef = TypedDict(
    "FieldSourceProfileIdsTypeDef",
    {
        "AccountNumber": str,
        "AdditionalInformation": str,
        "PartyType": str,
        "BusinessName": str,
        "FirstName": str,
        "MiddleName": str,
        "LastName": str,
        "BirthDate": str,
        "Gender": str,
        "PhoneNumber": str,
        "MobilePhoneNumber": str,
        "HomePhoneNumber": str,
        "BusinessPhoneNumber": str,
        "EmailAddress": str,
        "PersonalEmailAddress": str,
        "BusinessEmailAddress": str,
        "Address": str,
        "ShippingAddress": str,
        "MailingAddress": str,
        "BillingAddress": str,
        "Attributes": Dict[str, str],
    },
    total=False,
)

_RequiredFlowDefinitionTypeDef = TypedDict(
    "_RequiredFlowDefinitionTypeDef",
    {
        "FlowName": str,
        "KmsArn": str,
        "SourceFlowConfig": "SourceFlowConfigTypeDef",
        "Tasks": List["TaskTypeDef"],
        "TriggerConfig": "TriggerConfigTypeDef",
    },
)
_OptionalFlowDefinitionTypeDef = TypedDict(
    "_OptionalFlowDefinitionTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class FlowDefinitionTypeDef(_RequiredFlowDefinitionTypeDef, _OptionalFlowDefinitionTypeDef):
    pass


_RequiredGetDomainResponseTypeDef = TypedDict(
    "_RequiredGetDomainResponseTypeDef",
    {
        "DomainName": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
)
_OptionalGetDomainResponseTypeDef = TypedDict(
    "_OptionalGetDomainResponseTypeDef",
    {
        "DefaultExpirationDays": int,
        "DefaultEncryptionKey": str,
        "DeadLetterQueueUrl": str,
        "Stats": "DomainStatsTypeDef",
        "Matching": "MatchingResponseTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)


class GetDomainResponseTypeDef(
    _RequiredGetDomainResponseTypeDef, _OptionalGetDomainResponseTypeDef
):
    pass


_RequiredGetIntegrationResponseTypeDef = TypedDict(
    "_RequiredGetIntegrationResponseTypeDef",
    {
        "DomainName": str,
        "Uri": str,
        "ObjectTypeName": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
)
_OptionalGetIntegrationResponseTypeDef = TypedDict(
    "_OptionalGetIntegrationResponseTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)


class GetIntegrationResponseTypeDef(
    _RequiredGetIntegrationResponseTypeDef, _OptionalGetIntegrationResponseTypeDef
):
    pass


GetMatchesResponseTypeDef = TypedDict(
    "GetMatchesResponseTypeDef",
    {
        "NextToken": str,
        "MatchGenerationDate": datetime,
        "PotentialMatches": int,
        "Matches": List["MatchItemTypeDef"],
    },
    total=False,
)

_RequiredGetProfileObjectTypeResponseTypeDef = TypedDict(
    "_RequiredGetProfileObjectTypeResponseTypeDef",
    {
        "ObjectTypeName": str,
        "Description": str,
    },
)
_OptionalGetProfileObjectTypeResponseTypeDef = TypedDict(
    "_OptionalGetProfileObjectTypeResponseTypeDef",
    {
        "TemplateId": str,
        "ExpirationDays": int,
        "EncryptionKey": str,
        "AllowProfileCreation": bool,
        "Fields": Dict[str, "ObjectTypeFieldTypeDef"],
        "Keys": Dict[str, List["ObjectTypeKeyTypeDef"]],
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
    },
    total=False,
)


class GetProfileObjectTypeResponseTypeDef(
    _RequiredGetProfileObjectTypeResponseTypeDef, _OptionalGetProfileObjectTypeResponseTypeDef
):
    pass


GetProfileObjectTypeTemplateResponseTypeDef = TypedDict(
    "GetProfileObjectTypeTemplateResponseTypeDef",
    {
        "TemplateId": str,
        "SourceName": str,
        "SourceObject": str,
        "AllowProfileCreation": bool,
        "Fields": Dict[str, "ObjectTypeFieldTypeDef"],
        "Keys": Dict[str, List["ObjectTypeKeyTypeDef"]],
    },
    total=False,
)

IncrementalPullConfigTypeDef = TypedDict(
    "IncrementalPullConfigTypeDef",
    {
        "DatetimeTypeFieldName": str,
    },
    total=False,
)

ListAccountIntegrationsResponseTypeDef = TypedDict(
    "ListAccountIntegrationsResponseTypeDef",
    {
        "Items": List["ListIntegrationItemTypeDef"],
        "NextToken": str,
    },
    total=False,
)

_RequiredListDomainItemTypeDef = TypedDict(
    "_RequiredListDomainItemTypeDef",
    {
        "DomainName": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
)
_OptionalListDomainItemTypeDef = TypedDict(
    "_OptionalListDomainItemTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)


class ListDomainItemTypeDef(_RequiredListDomainItemTypeDef, _OptionalListDomainItemTypeDef):
    pass


ListDomainsResponseTypeDef = TypedDict(
    "ListDomainsResponseTypeDef",
    {
        "Items": List["ListDomainItemTypeDef"],
        "NextToken": str,
    },
    total=False,
)

_RequiredListIntegrationItemTypeDef = TypedDict(
    "_RequiredListIntegrationItemTypeDef",
    {
        "DomainName": str,
        "Uri": str,
        "ObjectTypeName": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
)
_OptionalListIntegrationItemTypeDef = TypedDict(
    "_OptionalListIntegrationItemTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)


class ListIntegrationItemTypeDef(
    _RequiredListIntegrationItemTypeDef, _OptionalListIntegrationItemTypeDef
):
    pass


ListIntegrationsResponseTypeDef = TypedDict(
    "ListIntegrationsResponseTypeDef",
    {
        "Items": List["ListIntegrationItemTypeDef"],
        "NextToken": str,
    },
    total=False,
)

_RequiredListProfileObjectTypeItemTypeDef = TypedDict(
    "_RequiredListProfileObjectTypeItemTypeDef",
    {
        "ObjectTypeName": str,
        "Description": str,
    },
)
_OptionalListProfileObjectTypeItemTypeDef = TypedDict(
    "_OptionalListProfileObjectTypeItemTypeDef",
    {
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ListProfileObjectTypeItemTypeDef(
    _RequiredListProfileObjectTypeItemTypeDef, _OptionalListProfileObjectTypeItemTypeDef
):
    pass


ListProfileObjectTypeTemplateItemTypeDef = TypedDict(
    "ListProfileObjectTypeTemplateItemTypeDef",
    {
        "TemplateId": str,
        "SourceName": str,
        "SourceObject": str,
    },
    total=False,
)

ListProfileObjectTypeTemplatesResponseTypeDef = TypedDict(
    "ListProfileObjectTypeTemplatesResponseTypeDef",
    {
        "Items": List["ListProfileObjectTypeTemplateItemTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListProfileObjectTypesResponseTypeDef = TypedDict(
    "ListProfileObjectTypesResponseTypeDef",
    {
        "Items": List["ListProfileObjectTypeItemTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListProfileObjectsItemTypeDef = TypedDict(
    "ListProfileObjectsItemTypeDef",
    {
        "ObjectTypeName": str,
        "ProfileObjectUniqueKey": str,
        "Object": str,
    },
    total=False,
)

ListProfileObjectsResponseTypeDef = TypedDict(
    "ListProfileObjectsResponseTypeDef",
    {
        "Items": List["ListProfileObjectsItemTypeDef"],
        "NextToken": str,
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

MarketoSourcePropertiesTypeDef = TypedDict(
    "MarketoSourcePropertiesTypeDef",
    {
        "Object": str,
    },
)

MatchItemTypeDef = TypedDict(
    "MatchItemTypeDef",
    {
        "MatchId": str,
        "ProfileIds": List[str],
    },
    total=False,
)

MatchingRequestTypeDef = TypedDict(
    "MatchingRequestTypeDef",
    {
        "Enabled": bool,
    },
)

MatchingResponseTypeDef = TypedDict(
    "MatchingResponseTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

MergeProfilesResponseTypeDef = TypedDict(
    "MergeProfilesResponseTypeDef",
    {
        "Message": str,
    },
    total=False,
)

ObjectTypeFieldTypeDef = TypedDict(
    "ObjectTypeFieldTypeDef",
    {
        "Source": str,
        "Target": str,
        "ContentType": FieldContentTypeType,
    },
    total=False,
)

ObjectTypeKeyTypeDef = TypedDict(
    "ObjectTypeKeyTypeDef",
    {
        "StandardIdentifiers": List[StandardIdentifierType],
        "FieldNames": List[str],
    },
    total=False,
)

ProfileTypeDef = TypedDict(
    "ProfileTypeDef",
    {
        "ProfileId": str,
        "AccountNumber": str,
        "AdditionalInformation": str,
        "PartyType": PartyTypeType,
        "BusinessName": str,
        "FirstName": str,
        "MiddleName": str,
        "LastName": str,
        "BirthDate": str,
        "Gender": GenderType,
        "PhoneNumber": str,
        "MobilePhoneNumber": str,
        "HomePhoneNumber": str,
        "BusinessPhoneNumber": str,
        "EmailAddress": str,
        "PersonalEmailAddress": str,
        "BusinessEmailAddress": str,
        "Address": "AddressTypeDef",
        "ShippingAddress": "AddressTypeDef",
        "MailingAddress": "AddressTypeDef",
        "BillingAddress": "AddressTypeDef",
        "Attributes": Dict[str, str],
    },
    total=False,
)

_RequiredPutIntegrationResponseTypeDef = TypedDict(
    "_RequiredPutIntegrationResponseTypeDef",
    {
        "DomainName": str,
        "Uri": str,
        "ObjectTypeName": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
)
_OptionalPutIntegrationResponseTypeDef = TypedDict(
    "_OptionalPutIntegrationResponseTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)


class PutIntegrationResponseTypeDef(
    _RequiredPutIntegrationResponseTypeDef, _OptionalPutIntegrationResponseTypeDef
):
    pass


PutProfileObjectResponseTypeDef = TypedDict(
    "PutProfileObjectResponseTypeDef",
    {
        "ProfileObjectUniqueKey": str,
    },
    total=False,
)

_RequiredPutProfileObjectTypeResponseTypeDef = TypedDict(
    "_RequiredPutProfileObjectTypeResponseTypeDef",
    {
        "ObjectTypeName": str,
        "Description": str,
    },
)
_OptionalPutProfileObjectTypeResponseTypeDef = TypedDict(
    "_OptionalPutProfileObjectTypeResponseTypeDef",
    {
        "TemplateId": str,
        "ExpirationDays": int,
        "EncryptionKey": str,
        "AllowProfileCreation": bool,
        "Fields": Dict[str, "ObjectTypeFieldTypeDef"],
        "Keys": Dict[str, List["ObjectTypeKeyTypeDef"]],
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
    },
    total=False,
)


class PutProfileObjectTypeResponseTypeDef(
    _RequiredPutProfileObjectTypeResponseTypeDef, _OptionalPutProfileObjectTypeResponseTypeDef
):
    pass


_RequiredS3SourcePropertiesTypeDef = TypedDict(
    "_RequiredS3SourcePropertiesTypeDef",
    {
        "BucketName": str,
    },
)
_OptionalS3SourcePropertiesTypeDef = TypedDict(
    "_OptionalS3SourcePropertiesTypeDef",
    {
        "BucketPrefix": str,
    },
    total=False,
)


class S3SourcePropertiesTypeDef(
    _RequiredS3SourcePropertiesTypeDef, _OptionalS3SourcePropertiesTypeDef
):
    pass


_RequiredSalesforceSourcePropertiesTypeDef = TypedDict(
    "_RequiredSalesforceSourcePropertiesTypeDef",
    {
        "Object": str,
    },
)
_OptionalSalesforceSourcePropertiesTypeDef = TypedDict(
    "_OptionalSalesforceSourcePropertiesTypeDef",
    {
        "EnableDynamicFieldUpdate": bool,
        "IncludeDeletedRecords": bool,
    },
    total=False,
)


class SalesforceSourcePropertiesTypeDef(
    _RequiredSalesforceSourcePropertiesTypeDef, _OptionalSalesforceSourcePropertiesTypeDef
):
    pass


_RequiredScheduledTriggerPropertiesTypeDef = TypedDict(
    "_RequiredScheduledTriggerPropertiesTypeDef",
    {
        "ScheduleExpression": str,
    },
)
_OptionalScheduledTriggerPropertiesTypeDef = TypedDict(
    "_OptionalScheduledTriggerPropertiesTypeDef",
    {
        "DataPullMode": DataPullModeType,
        "ScheduleStartTime": datetime,
        "ScheduleEndTime": datetime,
        "Timezone": str,
        "ScheduleOffset": int,
        "FirstExecutionFrom": datetime,
    },
    total=False,
)


class ScheduledTriggerPropertiesTypeDef(
    _RequiredScheduledTriggerPropertiesTypeDef, _OptionalScheduledTriggerPropertiesTypeDef
):
    pass


SearchProfilesResponseTypeDef = TypedDict(
    "SearchProfilesResponseTypeDef",
    {
        "Items": List["ProfileTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ServiceNowSourcePropertiesTypeDef = TypedDict(
    "ServiceNowSourcePropertiesTypeDef",
    {
        "Object": str,
    },
)

SourceConnectorPropertiesTypeDef = TypedDict(
    "SourceConnectorPropertiesTypeDef",
    {
        "Marketo": "MarketoSourcePropertiesTypeDef",
        "S3": "S3SourcePropertiesTypeDef",
        "Salesforce": "SalesforceSourcePropertiesTypeDef",
        "ServiceNow": "ServiceNowSourcePropertiesTypeDef",
        "Zendesk": "ZendeskSourcePropertiesTypeDef",
    },
    total=False,
)

_RequiredSourceFlowConfigTypeDef = TypedDict(
    "_RequiredSourceFlowConfigTypeDef",
    {
        "ConnectorType": SourceConnectorTypeType,
        "SourceConnectorProperties": "SourceConnectorPropertiesTypeDef",
    },
)
_OptionalSourceFlowConfigTypeDef = TypedDict(
    "_OptionalSourceFlowConfigTypeDef",
    {
        "ConnectorProfileName": str,
        "IncrementalPullConfig": "IncrementalPullConfigTypeDef",
    },
    total=False,
)


class SourceFlowConfigTypeDef(_RequiredSourceFlowConfigTypeDef, _OptionalSourceFlowConfigTypeDef):
    pass


_RequiredTaskTypeDef = TypedDict(
    "_RequiredTaskTypeDef",
    {
        "SourceFields": List[str],
        "TaskType": TaskTypeType,
    },
)
_OptionalTaskTypeDef = TypedDict(
    "_OptionalTaskTypeDef",
    {
        "ConnectorOperator": "ConnectorOperatorTypeDef",
        "DestinationField": str,
        "TaskProperties": Dict[OperatorPropertiesKeysType, str],
    },
    total=False,
)


class TaskTypeDef(_RequiredTaskTypeDef, _OptionalTaskTypeDef):
    pass


_RequiredTriggerConfigTypeDef = TypedDict(
    "_RequiredTriggerConfigTypeDef",
    {
        "TriggerType": TriggerTypeType,
    },
)
_OptionalTriggerConfigTypeDef = TypedDict(
    "_OptionalTriggerConfigTypeDef",
    {
        "TriggerProperties": "TriggerPropertiesTypeDef",
    },
    total=False,
)


class TriggerConfigTypeDef(_RequiredTriggerConfigTypeDef, _OptionalTriggerConfigTypeDef):
    pass


TriggerPropertiesTypeDef = TypedDict(
    "TriggerPropertiesTypeDef",
    {
        "Scheduled": "ScheduledTriggerPropertiesTypeDef",
    },
    total=False,
)

UpdateAddressTypeDef = TypedDict(
    "UpdateAddressTypeDef",
    {
        "Address1": str,
        "Address2": str,
        "Address3": str,
        "Address4": str,
        "City": str,
        "County": str,
        "State": str,
        "Province": str,
        "Country": str,
        "PostalCode": str,
    },
    total=False,
)

_RequiredUpdateDomainResponseTypeDef = TypedDict(
    "_RequiredUpdateDomainResponseTypeDef",
    {
        "DomainName": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
)
_OptionalUpdateDomainResponseTypeDef = TypedDict(
    "_OptionalUpdateDomainResponseTypeDef",
    {
        "DefaultExpirationDays": int,
        "DefaultEncryptionKey": str,
        "DeadLetterQueueUrl": str,
        "Matching": "MatchingResponseTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)


class UpdateDomainResponseTypeDef(
    _RequiredUpdateDomainResponseTypeDef, _OptionalUpdateDomainResponseTypeDef
):
    pass


UpdateProfileResponseTypeDef = TypedDict(
    "UpdateProfileResponseTypeDef",
    {
        "ProfileId": str,
    },
)

ZendeskSourcePropertiesTypeDef = TypedDict(
    "ZendeskSourcePropertiesTypeDef",
    {
        "Object": str,
    },
)
