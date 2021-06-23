# from nubium_schemas.campaign_response import Canon
#
#
# def test_data_models_can_generate_default_dictionaries():
#     expected = {
#         "campaign_response": {
#             "email_address": "",
#             "ext_tactic_id": "",
#             "int_tactic_id": "",
#             "offer_consumption_timestamp": "",
#             "offer_id": "",
#         },
#         "raw_formdata": {},
#         "tracking_ids": {
#             "eloqua_contacts_inquiries_id": "",
#             "sfdc_contact_id": "",
#             "sfdc_ext_tactic_contact_id": "",
#             "sfdc_ext_tactic_lead_id": "",
#             "sfdc_int_tactic_contact_id": "",
#             "sfdc_int_tactic_lead_id": "",
#             "sfdc_lead_id": "",
#             "sfdc_offer_contact_id": "",
#             "sfdc_offer_lead_id": "",
#         },
#     }
#     assert Canon().asdict() == expected
#
#
# def test_data_models_can_generate_avro_schema_in_python_dict_form():
#     expected = {
#         "name": "Canon",
#         "type": "record",
#         "fields": [
#             {
#                 "name": "campaign_response",
#                 "type": {
#                     "name": "CampaignResponse",
#                     "type": "record",
#                     "fields": [
#                         {
#                             "name": "email_address",
#                             "type": "string",
#                             "default": ""
#                         },
#                         {
#                             "name": "ext_tactic_id",
#                             "type": "string",
#                             "default": ""
#                         },
#                         {
#                             "name": "int_tactic_id",
#                             "type": "string",
#                             "default": ""
#                         },
#                         {
#                             "name": "offer_id",
#                             "type": "string",
#                             "default": ""
#                         },
#                         {
#                             "name": "offer_consumption_timestamp",
#                             "type": "string",
#                             "default": ""
#                         }
#                     ]
#                 }
#             },
#             {
#                 "name": "tracking_ids",
#                 "type": {
#                     "name": "TrackingIds",
#                     "type": "record",
#                     "fields": [
#                         {
#                             "name": "eloqua_contacts_inquiries_id",
#                             "type": "string",
#                             "default": ""
#                         },
#                         {
#                             "name": "sfdc_contact_id",
#                             "type": "string",
#                             "default": ""
#                         },
#                         {
#                             "name": "sfdc_lead_id",
#                             "type": "string",
#                             "default": ""
#                         },
#                         {
#                             "name": "sfdc_ext_tactic_lead_id",
#                             "type": "string",
#                             "default": ""
#                         },
#                         {
#                             "name": "sfdc_int_tactic_lead_id",
#                             "type": "string",
#                             "default": ""
#                         },
#                         {
#                             "name": "sfdc_offer_lead_id",
#                             "type": "string",
#                             "default": ""
#                         },
#                         {
#                             "name": "sfdc_ext_tactic_contact_id",
#                             "type": "string",
#                             "default": ""
#                         },
#                         {
#                             "name": "sfdc_int_tactic_contact_id",
#                             "type": "string",
#                             "default": ""
#                         },
#                         {
#                             "name": "sfdc_offer_contact_id",
#                             "type": "string",
#                             "default": ""
#                         }
#                     ]
#                 }
#             },
#             {
#                 "name": "raw_formdata",
#                 "type": {
#                     "type": "map",
#                     "values": "string"
#                 },
#                 "default": "{}"
#             }
#         ]
#     }
#
#     assert Canon.avro_schema_to_python() == expected
