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

S_ADDRESS_CREATE = {
  "street": {"type": "string", "required": True, "empty": False},
  "street2": {"type": "string"},
  "zip_code": {"type": "string", "required": True, "empty": False},
  "city": {"type": "string", "required": True, "empty": False},
  "country": {"type": "string", "required": True, "empty": False},
  "state": {"type": "string","required": True, "empty": False},
}

S_SUBSCRIPTION_REQUEST_CREATE_SC_FIELDS = {
  "iban": {"type": "string", "required": True},
  "vat": {"type": "string", "required": True},
  "address": {"type": "dict", "schema": S_ADDRESS_CREATE},
  "birthdate": {
    "type": "string",
    "regex": "\\d{4}-[01]\\d-[0-3]\\d"
  },
  "gender": {"type": "string"},
  "phone": {"type": "string"},
  "mobile": {"type": "string"},
  "firstname": {"type": "string"},
  "lastname": {"type": "string"},
  "is_company": {"type": "boolean"},
  "company_name": {"type": "string"},
  "company_email": {"type": "string"},
  "must_register_in_cs": {"type": "boolean"},
  "image_dni": {"type": "string"},
  "image_driving_license": {"type": "string"},
  "driving_license_expiration_date": {
    "type": "string",
    "regex": "\\d{4}-[01]\\d-[0-3]\\d"
  },
  "external_obj_id": {"type": "integer"},
  "representative_vat": {"type": "string"}
}
