"""
sev3rance template settings
"""


def severance_settings(request):
    return_value = dict()

    # AA logo
    return_value["SEVERANCE_TEMPLATE_AA_LOGO"] = "/static/icons/allianceauth.png"

    # entity ID
    return_value["SEVERANCE_TEMPLATE_ENTITY_ID"] = 982284363

    # entity type
    return_value["SEVERANCE_TEMPLATE_ENTITY_TYPE"] = "alliance"

    # entity name
    return_value["SEVERANCE_TEMPLATE_ENTITY_NAME"] = "Sev3rance"

    return return_value
