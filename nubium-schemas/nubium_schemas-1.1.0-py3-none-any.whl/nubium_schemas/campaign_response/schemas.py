import dataclasses
import typing

from dataclasses_avroschema import AvroModel

from .schema_components import campaign_response, tracking_ids, salesforce_campaign_member


@dataclasses.dataclass
class CampaignResponse(AvroModel):
    email_address: str = ""
    ext_tactic_id: str = ""
    int_tactic_id: str = ""
    offer_id: str = ""
    offer_consumption_timestamp: str = ""
    class Meta:
        schema_doc = False


@dataclasses.dataclass
class TrackingIds(AvroModel):
    eloqua_contacts_inquiries_id: str = ""
    sfdc_contact_id: str = ""
    sfdc_lead_id: str = ""
    sfdc_ext_tactic_lead_id: str = ""
    sfdc_int_tactic_lead_id: str = ""
    sfdc_offer_lead_id: str = ""
    sfdc_ext_tactic_contact_id: str = ""
    sfdc_int_tactic_contact_id: str = ""
    sfdc_offer_contact_id: str = ""
    class Meta:
        schema_doc = False


@dataclasses.dataclass
class Canon(AvroModel):
    campaign_response: CampaignResponse = dataclasses.field(default_factory=CampaignResponse)
    tracking_ids: TrackingIds = dataclasses.field(default_factory=TrackingIds)
    raw_formdata: typing.Dict[str, str] = dataclasses.field(default_factory=dict)
    class Meta:
        schema_doc = False


# canon = Canon.avro_schema_to_python()
canon = {
    "name": "Canon",
    "type": "record",
    "fields": [
        {"name": "campaign_response", "type": campaign_response},
        {"name": "tracking_ids", "type": tracking_ids},
        {"name": "raw_formdata", "type": {"type": "map", "values": "string"}, "default": "{}"}
     ]
}

campaign_members_create = {
    "name": "CampaignMembersCreate",
    "type": "record",
    "fields": [
        {"name": "campaign_members_to_create", "type": {"type": "array", "items": salesforce_campaign_member}},
        {"name": "campaign_response", "type": campaign_response},
        {"name": "tracking_ids", "type": tracking_ids}
    ]
}

campaign_members_update = {
    "name": "CampaignMembersUpdate",
    "type": "record",
    "fields": [
        {"name": "campaign_members_to_update", "type": {"type": "array", "items": salesforce_campaign_member}}
    ]
}
