def boolean_validator(field, value, error):
  if value and value not in ["true", "false"]:
    error(field, "Must be a boolean value: true or false")

def date_validator(field, value, error):
  try:
    Date.from_string(value)
  except ValueError:
    return error(
        field, _("{} does not match format '%Y-%m-%d'".format(value))
    )

### CS REGISTRATION REQUEST SCHEMAS ###
S_CS_REGISTRATION_REQUEST_GET = {"_id": {"type": "integer"}}

S_CS_REGISTRATION_REQUEST_RETURN_GET = {
  "id": {"type": "integer", "required": True},
  "force_registration": {"type": "boolean"},
  "group_index": {"type": "string"},
  "ba_behaviour": {"type": "string"},
  "ba_credits": {"type": "float"},
  "related_subscription_id": {"type": "integer"},
  "related_member_id": {"type": "integer"},
  "related_cs_update_data_id": {"type": "integer"},
  "completed": {"type": "boolean"},
  "completed_date": {"type": "string"},
  "completed_behaviour": {"type": "string"}
}

S_CS_REGISTRATION_REQUEST_CREATE = {
  "force_registration": {"type": "boolean", "required": True},
  "group_index": {"type": "string", "required": True},
  "ba_behaviour": {"type": "string", "required": True},
  "ba_credits": {"type": "float", "required": True},
  "related_subscription_id": {"type": "integer"},
  "related_member_id": {"type": "integer"},
}

S_CS_REGISTRATION_REQUEST_UPDATE = {
  "force_registration": {"type": "boolean"},
  "group_index": {"type": "string"},
  "ba_behaviour": {"type": "string"},
  "ba_credits": {"type": "float"},
  "related_subscription_id": {"type": "integer"},
  "related_member_id": {"type": "integer"},
}

S_CS_REGISTRATION_REQUEST_VALIDATE = {"_id": {"type": "integer"}}

### CS UPDATE DATA SCHEMAS ###

S_CS_UPDATE_DATA_GET = {"_id": {"type": "integer"}}

S_CS_UPDATE_DATA_RETURN_GET = {
  "id": {"type": "integer", "required": True},
  "form_id": {"type": "string", "required": True},
  "cs_update_type": {"type": "string"},
  "cs_update_dni": {"type": "string"},
  "cs_update_name": {"type": "string"},
  "cs_update_first_surname": {"type": "string"},
  "cs_update_second_surname": {"type": "string"},
  "cs_update_cif": {"type": "string"},
  "cs_update_dni_image": {"type": "string"},
  "cs_update_image_driving_license": {"type": "string"},
  "cs_update_email": {"type": "string"},
  "cs_update_mobile": {"type": "string"},
  "cs_update_birthday": {"type": "string"},
  "cs_update_driving_license_expiration_date": {"type": "string"},
  "cs_update_group": {"type": "string"},
  "cs_update_group_secondary": {"type": "string"},
  "cs_update_comments": {"type": "string"},
  "final_state": {"type": "string"}
}

S_CS_UPDATE_DATA_CREATE = {
  "form_id": {"type": "string", "required": True},
  "cs_update_type": {"type": "string", "required": True},
  "cs_update_dni": {"type": "string", "required": True},
  "cs_update_name": {"type": "string"},
  "cs_update_first_surname": {"type": "string"},
  "cs_update_second_surname": {"type": "string"},
  "cs_update_cif": {"type": "string"},
  "cs_update_dni_image": {"type": "string", "required": True},
  "cs_update_image_driving_license": {"type": "string", "required": True},
  "cs_update_email": {"type": "string", "required": True},
  "cs_update_mobile": {"type": "string", "required": True},
  "cs_update_birthday": {
    "type": "string",
    "required": True,
    "regex": "\\d{4}-[01]\\d-[0-3]\\d"
  },
  "cs_update_driving_license_expiration_date": {
    "type": "string",
    "required": True,
    "regex": "\\d{4}-[01]\\d-[0-3]\\d"
    },
  "cs_update_group": {"type": "string"},
  "cs_update_group_secondary": {"type": "string"},
  "cs_update_comments": {"type": "string"}
}

S_CS_UPDATE_DATA_UPDATE = {
  "form_id": {"type": "string"},
  "cs_update_type": {"type": "string"},
  "cs_update_dni": {"type": "string"},
  "cs_update_name": {"type": "string"},
  "cs_update_first_surname": {"type": "string"},
  "cs_update_second_surname": {"type": "string"},
  "cs_update_cif": {"type": "string"},
  "cs_update_dni_image": {"type": "string"},
  "cs_update_image_driving_license": {"type": "string"},
  "cs_update_email": {"type": "string"},
  "cs_update_mobile": {"type": "string"},
  "cs_update_birthday": {
    "type": "string",
    "regex": "\\d{4}-[01]\\d-[0-3]\\d"
  },
  "cs_update_driving_license_expiration_date": {
    "type": "string",
    "regex": "\\d{4}-[01]\\d-[0-3]\\d"
  },
  "cs_update_group": {"type": "string"},
  "cs_update_group_secondary": {"type": "string"},
  "cs_update_comments": {"type": "string"}
}

S_CS_UPDATE_DATA_VALIDATE = {"_id": {"type": "integer"}}