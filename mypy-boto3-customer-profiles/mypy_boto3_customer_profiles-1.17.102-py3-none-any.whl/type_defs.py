"""
Type annotations for customer-profiles service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/type_defs.html)

Usage::

    ```python
    from mypy_boto3_customer_profiles.type_defs import AddProfileKeyRequestTypeDef

    data: AddProfileKeyRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

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
    "AddProfileKeyRequestTypeDef",
    "AddProfileKeyResponseResponseTypeDef",
    "AddressTypeDef",
    "ConnectorOperatorTypeDef",
    "CreateDomainRequestTypeDef",
    "CreateDomainResponseResponseTypeDef",
    "CreateProfileRequestTypeDef",
    "CreateProfileResponseResponseTypeDef",
    "DeleteDomainRequestTypeDef",
    "DeleteDomainResponseResponseTypeDef",
    "DeleteIntegrationRequestTypeDef",
    "DeleteIntegrationResponseResponseTypeDef",
    "DeleteProfileKeyRequestTypeDef",
    "DeleteProfileKeyResponseResponseTypeDef",
    "DeleteProfileObjectRequestTypeDef",
    "DeleteProfileObjectResponseResponseTypeDef",
    "DeleteProfileObjectTypeRequestTypeDef",
    "DeleteProfileObjectTypeResponseResponseTypeDef",
    "DeleteProfileRequestTypeDef",
    "DeleteProfileResponseResponseTypeDef",
    "DomainStatsTypeDef",
    "FieldSourceProfileIdsTypeDef",
    "FlowDefinitionTypeDef",
    "GetDomainRequestTypeDef",
    "GetDomainResponseResponseTypeDef",
    "GetIntegrationRequestTypeDef",
    "GetIntegrationResponseResponseTypeDef",
    "GetMatchesRequestTypeDef",
    "GetMatchesResponseResponseTypeDef",
    "GetProfileObjectTypeRequestTypeDef",
    "GetProfileObjectTypeResponseResponseTypeDef",
    "GetProfileObjectTypeTemplateRequestTypeDef",
    "GetProfileObjectTypeTemplateResponseResponseTypeDef",
    "IncrementalPullConfigTypeDef",
    "ListAccountIntegrationsRequestTypeDef",
    "ListAccountIntegrationsResponseResponseTypeDef",
    "ListDomainItemTypeDef",
    "ListDomainsRequestTypeDef",
    "ListDomainsResponseResponseTypeDef",
    "ListIntegrationItemTypeDef",
    "ListIntegrationsRequestTypeDef",
    "ListIntegrationsResponseResponseTypeDef",
    "ListProfileObjectTypeItemTypeDef",
    "ListProfileObjectTypeTemplateItemTypeDef",
    "ListProfileObjectTypeTemplatesRequestTypeDef",
    "ListProfileObjectTypeTemplatesResponseResponseTypeDef",
    "ListProfileObjectTypesRequestTypeDef",
    "ListProfileObjectTypesResponseResponseTypeDef",
    "ListProfileObjectsItemTypeDef",
    "ListProfileObjectsRequestTypeDef",
    "ListProfileObjectsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "MarketoSourcePropertiesTypeDef",
    "MatchItemTypeDef",
    "MatchingRequestTypeDef",
    "MatchingResponseTypeDef",
    "MergeProfilesRequestTypeDef",
    "MergeProfilesResponseResponseTypeDef",
    "ObjectTypeFieldTypeDef",
    "ObjectTypeKeyTypeDef",
    "ProfileTypeDef",
    "PutIntegrationRequestTypeDef",
    "PutIntegrationResponseResponseTypeDef",
    "PutProfileObjectRequestTypeDef",
    "PutProfileObjectResponseResponseTypeDef",
    "PutProfileObjectTypeRequestTypeDef",
    "PutProfileObjectTypeResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "S3SourcePropertiesTypeDef",
    "SalesforceSourcePropertiesTypeDef",
    "ScheduledTriggerPropertiesTypeDef",
    "SearchProfilesRequestTypeDef",
    "SearchProfilesResponseResponseTypeDef",
    "ServiceNowSourcePropertiesTypeDef",
    "SourceConnectorPropertiesTypeDef",
    "SourceFlowConfigTypeDef",
    "TagResourceRequestTypeDef",
    "TaskTypeDef",
    "TriggerConfigTypeDef",
    "TriggerPropertiesTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAddressTypeDef",
    "UpdateDomainRequestTypeDef",
    "UpdateDomainResponseResponseTypeDef",
    "UpdateProfileRequestTypeDef",
    "UpdateProfileResponseResponseTypeDef",
    "ZendeskSourcePropertiesTypeDef",
)

AddProfileKeyRequestTypeDef = TypedDict(
    "AddProfileKeyRequestTypeDef",
    {
        "ProfileId": str,
        "KeyName": str,
        "Values": List[str],
        "DomainName": str,
    },
)

AddProfileKeyResponseResponseTypeDef = TypedDict(
    "AddProfileKeyResponseResponseTypeDef",
    {
        "KeyName": str,
        "Values": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredCreateDomainRequestTypeDef = TypedDict(
    "_RequiredCreateDomainRequestTypeDef",
    {
        "DomainName": str,
        "DefaultExpirationDays": int,
    },
)
_OptionalCreateDomainRequestTypeDef = TypedDict(
    "_OptionalCreateDomainRequestTypeDef",
    {
        "DefaultEncryptionKey": str,
        "DeadLetterQueueUrl": str,
        "Matching": "MatchingRequestTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateDomainRequestTypeDef(
    _RequiredCreateDomainRequestTypeDef, _OptionalCreateDomainRequestTypeDef
):
    pass


CreateDomainResponseResponseTypeDef = TypedDict(
    "CreateDomainResponseResponseTypeDef",
    {
        "DomainName": str,
        "DefaultExpirationDays": int,
        "DefaultEncryptionKey": str,
        "DeadLetterQueueUrl": str,
        "Matching": "MatchingResponseTypeDef",
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProfileRequestTypeDef = TypedDict(
    "_RequiredCreateProfileRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalCreateProfileRequestTypeDef = TypedDict(
    "_OptionalCreateProfileRequestTypeDef",
    {
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


class CreateProfileRequestTypeDef(
    _RequiredCreateProfileRequestTypeDef, _OptionalCreateProfileRequestTypeDef
):
    pass


CreateProfileResponseResponseTypeDef = TypedDict(
    "CreateProfileResponseResponseTypeDef",
    {
        "ProfileId": str,
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
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteIntegrationRequestTypeDef = TypedDict(
    "DeleteIntegrationRequestTypeDef",
    {
        "DomainName": str,
        "Uri": str,
    },
)

DeleteIntegrationResponseResponseTypeDef = TypedDict(
    "DeleteIntegrationResponseResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProfileKeyRequestTypeDef = TypedDict(
    "DeleteProfileKeyRequestTypeDef",
    {
        "ProfileId": str,
        "KeyName": str,
        "Values": List[str],
        "DomainName": str,
    },
)

DeleteProfileKeyResponseResponseTypeDef = TypedDict(
    "DeleteProfileKeyResponseResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProfileObjectRequestTypeDef = TypedDict(
    "DeleteProfileObjectRequestTypeDef",
    {
        "ProfileId": str,
        "ProfileObjectUniqueKey": str,
        "ObjectTypeName": str,
        "DomainName": str,
    },
)

DeleteProfileObjectResponseResponseTypeDef = TypedDict(
    "DeleteProfileObjectResponseResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProfileObjectTypeRequestTypeDef = TypedDict(
    "DeleteProfileObjectTypeRequestTypeDef",
    {
        "DomainName": str,
        "ObjectTypeName": str,
    },
)

DeleteProfileObjectTypeResponseResponseTypeDef = TypedDict(
    "DeleteProfileObjectTypeResponseResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProfileRequestTypeDef = TypedDict(
    "DeleteProfileRequestTypeDef",
    {
        "ProfileId": str,
        "DomainName": str,
    },
)

DeleteProfileResponseResponseTypeDef = TypedDict(
    "DeleteProfileResponseResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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


GetDomainRequestTypeDef = TypedDict(
    "GetDomainRequestTypeDef",
    {
        "DomainName": str,
    },
)

GetDomainResponseResponseTypeDef = TypedDict(
    "GetDomainResponseResponseTypeDef",
    {
        "DomainName": str,
        "DefaultExpirationDays": int,
        "DefaultEncryptionKey": str,
        "DeadLetterQueueUrl": str,
        "Stats": "DomainStatsTypeDef",
        "Matching": "MatchingResponseTypeDef",
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIntegrationRequestTypeDef = TypedDict(
    "GetIntegrationRequestTypeDef",
    {
        "DomainName": str,
        "Uri": str,
    },
)

GetIntegrationResponseResponseTypeDef = TypedDict(
    "GetIntegrationResponseResponseTypeDef",
    {
        "DomainName": str,
        "Uri": str,
        "ObjectTypeName": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMatchesRequestTypeDef = TypedDict(
    "_RequiredGetMatchesRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalGetMatchesRequestTypeDef = TypedDict(
    "_OptionalGetMatchesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class GetMatchesRequestTypeDef(
    _RequiredGetMatchesRequestTypeDef, _OptionalGetMatchesRequestTypeDef
):
    pass


GetMatchesResponseResponseTypeDef = TypedDict(
    "GetMatchesResponseResponseTypeDef",
    {
        "NextToken": str,
        "MatchGenerationDate": datetime,
        "PotentialMatches": int,
        "Matches": List["MatchItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProfileObjectTypeRequestTypeDef = TypedDict(
    "GetProfileObjectTypeRequestTypeDef",
    {
        "DomainName": str,
        "ObjectTypeName": str,
    },
)

GetProfileObjectTypeResponseResponseTypeDef = TypedDict(
    "GetProfileObjectTypeResponseResponseTypeDef",
    {
        "ObjectTypeName": str,
        "Description": str,
        "TemplateId": str,
        "ExpirationDays": int,
        "EncryptionKey": str,
        "AllowProfileCreation": bool,
        "Fields": Dict[str, "ObjectTypeFieldTypeDef"],
        "Keys": Dict[str, List["ObjectTypeKeyTypeDef"]],
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProfileObjectTypeTemplateRequestTypeDef = TypedDict(
    "GetProfileObjectTypeTemplateRequestTypeDef",
    {
        "TemplateId": str,
    },
)

GetProfileObjectTypeTemplateResponseResponseTypeDef = TypedDict(
    "GetProfileObjectTypeTemplateResponseResponseTypeDef",
    {
        "TemplateId": str,
        "SourceName": str,
        "SourceObject": str,
        "AllowProfileCreation": bool,
        "Fields": Dict[str, "ObjectTypeFieldTypeDef"],
        "Keys": Dict[str, List["ObjectTypeKeyTypeDef"]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IncrementalPullConfigTypeDef = TypedDict(
    "IncrementalPullConfigTypeDef",
    {
        "DatetimeTypeFieldName": str,
    },
    total=False,
)

_RequiredListAccountIntegrationsRequestTypeDef = TypedDict(
    "_RequiredListAccountIntegrationsRequestTypeDef",
    {
        "Uri": str,
    },
)
_OptionalListAccountIntegrationsRequestTypeDef = TypedDict(
    "_OptionalListAccountIntegrationsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListAccountIntegrationsRequestTypeDef(
    _RequiredListAccountIntegrationsRequestTypeDef, _OptionalListAccountIntegrationsRequestTypeDef
):
    pass


ListAccountIntegrationsResponseResponseTypeDef = TypedDict(
    "ListAccountIntegrationsResponseResponseTypeDef",
    {
        "Items": List["ListIntegrationItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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


ListDomainsRequestTypeDef = TypedDict(
    "ListDomainsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDomainsResponseResponseTypeDef = TypedDict(
    "ListDomainsResponseResponseTypeDef",
    {
        "Items": List["ListDomainItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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


_RequiredListIntegrationsRequestTypeDef = TypedDict(
    "_RequiredListIntegrationsRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalListIntegrationsRequestTypeDef = TypedDict(
    "_OptionalListIntegrationsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListIntegrationsRequestTypeDef(
    _RequiredListIntegrationsRequestTypeDef, _OptionalListIntegrationsRequestTypeDef
):
    pass


ListIntegrationsResponseResponseTypeDef = TypedDict(
    "ListIntegrationsResponseResponseTypeDef",
    {
        "Items": List["ListIntegrationItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

ListProfileObjectTypeTemplatesRequestTypeDef = TypedDict(
    "ListProfileObjectTypeTemplatesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListProfileObjectTypeTemplatesResponseResponseTypeDef = TypedDict(
    "ListProfileObjectTypeTemplatesResponseResponseTypeDef",
    {
        "Items": List["ListProfileObjectTypeTemplateItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProfileObjectTypesRequestTypeDef = TypedDict(
    "_RequiredListProfileObjectTypesRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalListProfileObjectTypesRequestTypeDef = TypedDict(
    "_OptionalListProfileObjectTypesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListProfileObjectTypesRequestTypeDef(
    _RequiredListProfileObjectTypesRequestTypeDef, _OptionalListProfileObjectTypesRequestTypeDef
):
    pass


ListProfileObjectTypesResponseResponseTypeDef = TypedDict(
    "ListProfileObjectTypesResponseResponseTypeDef",
    {
        "Items": List["ListProfileObjectTypeItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredListProfileObjectsRequestTypeDef = TypedDict(
    "_RequiredListProfileObjectsRequestTypeDef",
    {
        "DomainName": str,
        "ObjectTypeName": str,
        "ProfileId": str,
    },
)
_OptionalListProfileObjectsRequestTypeDef = TypedDict(
    "_OptionalListProfileObjectsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListProfileObjectsRequestTypeDef(
    _RequiredListProfileObjectsRequestTypeDef, _OptionalListProfileObjectsRequestTypeDef
):
    pass


ListProfileObjectsResponseResponseTypeDef = TypedDict(
    "ListProfileObjectsResponseResponseTypeDef",
    {
        "Items": List["ListProfileObjectsItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredMergeProfilesRequestTypeDef = TypedDict(
    "_RequiredMergeProfilesRequestTypeDef",
    {
        "DomainName": str,
        "MainProfileId": str,
        "ProfileIdsToBeMerged": List[str],
    },
)
_OptionalMergeProfilesRequestTypeDef = TypedDict(
    "_OptionalMergeProfilesRequestTypeDef",
    {
        "FieldSourceProfileIds": "FieldSourceProfileIdsTypeDef",
    },
    total=False,
)


class MergeProfilesRequestTypeDef(
    _RequiredMergeProfilesRequestTypeDef, _OptionalMergeProfilesRequestTypeDef
):
    pass


MergeProfilesResponseResponseTypeDef = TypedDict(
    "MergeProfilesResponseResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredPutIntegrationRequestTypeDef = TypedDict(
    "_RequiredPutIntegrationRequestTypeDef",
    {
        "DomainName": str,
        "ObjectTypeName": str,
    },
)
_OptionalPutIntegrationRequestTypeDef = TypedDict(
    "_OptionalPutIntegrationRequestTypeDef",
    {
        "Uri": str,
        "Tags": Dict[str, str],
        "FlowDefinition": "FlowDefinitionTypeDef",
    },
    total=False,
)


class PutIntegrationRequestTypeDef(
    _RequiredPutIntegrationRequestTypeDef, _OptionalPutIntegrationRequestTypeDef
):
    pass


PutIntegrationResponseResponseTypeDef = TypedDict(
    "PutIntegrationResponseResponseTypeDef",
    {
        "DomainName": str,
        "Uri": str,
        "ObjectTypeName": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutProfileObjectRequestTypeDef = TypedDict(
    "PutProfileObjectRequestTypeDef",
    {
        "ObjectTypeName": str,
        "Object": str,
        "DomainName": str,
    },
)

PutProfileObjectResponseResponseTypeDef = TypedDict(
    "PutProfileObjectResponseResponseTypeDef",
    {
        "ProfileObjectUniqueKey": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutProfileObjectTypeRequestTypeDef = TypedDict(
    "_RequiredPutProfileObjectTypeRequestTypeDef",
    {
        "DomainName": str,
        "ObjectTypeName": str,
        "Description": str,
    },
)
_OptionalPutProfileObjectTypeRequestTypeDef = TypedDict(
    "_OptionalPutProfileObjectTypeRequestTypeDef",
    {
        "TemplateId": str,
        "ExpirationDays": int,
        "EncryptionKey": str,
        "AllowProfileCreation": bool,
        "Fields": Dict[str, "ObjectTypeFieldTypeDef"],
        "Keys": Dict[str, List["ObjectTypeKeyTypeDef"]],
        "Tags": Dict[str, str],
    },
    total=False,
)


class PutProfileObjectTypeRequestTypeDef(
    _RequiredPutProfileObjectTypeRequestTypeDef, _OptionalPutProfileObjectTypeRequestTypeDef
):
    pass


PutProfileObjectTypeResponseResponseTypeDef = TypedDict(
    "PutProfileObjectTypeResponseResponseTypeDef",
    {
        "ObjectTypeName": str,
        "Description": str,
        "TemplateId": str,
        "ExpirationDays": int,
        "EncryptionKey": str,
        "AllowProfileCreation": bool,
        "Fields": Dict[str, "ObjectTypeFieldTypeDef"],
        "Keys": Dict[str, List["ObjectTypeKeyTypeDef"]],
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
        "ScheduleStartTime": Union[datetime, str],
        "ScheduleEndTime": Union[datetime, str],
        "Timezone": str,
        "ScheduleOffset": int,
        "FirstExecutionFrom": Union[datetime, str],
    },
    total=False,
)


class ScheduledTriggerPropertiesTypeDef(
    _RequiredScheduledTriggerPropertiesTypeDef, _OptionalScheduledTriggerPropertiesTypeDef
):
    pass


_RequiredSearchProfilesRequestTypeDef = TypedDict(
    "_RequiredSearchProfilesRequestTypeDef",
    {
        "DomainName": str,
        "KeyName": str,
        "Values": List[str],
    },
)
_OptionalSearchProfilesRequestTypeDef = TypedDict(
    "_OptionalSearchProfilesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class SearchProfilesRequestTypeDef(
    _RequiredSearchProfilesRequestTypeDef, _OptionalSearchProfilesRequestTypeDef
):
    pass


SearchProfilesResponseResponseTypeDef = TypedDict(
    "SearchProfilesResponseResponseTypeDef",
    {
        "Items": List["ProfileTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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


TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

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

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
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

_RequiredUpdateDomainRequestTypeDef = TypedDict(
    "_RequiredUpdateDomainRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalUpdateDomainRequestTypeDef = TypedDict(
    "_OptionalUpdateDomainRequestTypeDef",
    {
        "DefaultExpirationDays": int,
        "DefaultEncryptionKey": str,
        "DeadLetterQueueUrl": str,
        "Matching": "MatchingRequestTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)


class UpdateDomainRequestTypeDef(
    _RequiredUpdateDomainRequestTypeDef, _OptionalUpdateDomainRequestTypeDef
):
    pass


UpdateDomainResponseResponseTypeDef = TypedDict(
    "UpdateDomainResponseResponseTypeDef",
    {
        "DomainName": str,
        "DefaultExpirationDays": int,
        "DefaultEncryptionKey": str,
        "DeadLetterQueueUrl": str,
        "Matching": "MatchingResponseTypeDef",
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateProfileRequestTypeDef = TypedDict(
    "_RequiredUpdateProfileRequestTypeDef",
    {
        "DomainName": str,
        "ProfileId": str,
    },
)
_OptionalUpdateProfileRequestTypeDef = TypedDict(
    "_OptionalUpdateProfileRequestTypeDef",
    {
        "AdditionalInformation": str,
        "AccountNumber": str,
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
        "Address": "UpdateAddressTypeDef",
        "ShippingAddress": "UpdateAddressTypeDef",
        "MailingAddress": "UpdateAddressTypeDef",
        "BillingAddress": "UpdateAddressTypeDef",
        "Attributes": Dict[str, str],
    },
    total=False,
)


class UpdateProfileRequestTypeDef(
    _RequiredUpdateProfileRequestTypeDef, _OptionalUpdateProfileRequestTypeDef
):
    pass


UpdateProfileResponseResponseTypeDef = TypedDict(
    "UpdateProfileResponseResponseTypeDef",
    {
        "ProfileId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ZendeskSourcePropertiesTypeDef = TypedDict(
    "ZendeskSourcePropertiesTypeDef",
    {
        "Object": str,
    },
)
