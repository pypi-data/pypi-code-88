# -*- coding: utf-8 -*-
{
  'name': "sm_partago_user",

  'summary': """
    Handles all carsharing user related data and actions
  """,

  'description': """
    Handles all carsharing user related data and actions
  """,

  'author': "Som Mobilitat",
  'website': "http://www.sommobilitat.coop",
  'category': 'vertical-carsharing',
  'version': '12.0.0.0.7',

  # any module necessary for this one to work correctly
  'depends': ['base', 'vertical_carsharing', 'sm_partago_db'],

  # always loaded
  'data': [
    'email_tmpl/cs_access_requested.xml',
    'email_tmpl/cs_company_access_requested.xml',
    'email_tmpl/cs_complete_data_soci_not_found_email.xml',
    'email_tmpl/cs_complete_data_successful_email.xml',
    'email_tmpl/cs_email_already_active.xml',
    'email_tmpl/cs_missing_data_email.xml',
    'security/ir.model.access.csv',
    'views/views.xml',
    'views/views_res_config_settings.xml',
    'views/views_members.xml',
    'views/views_carsharing_update_data.xml',
    'views/views_member_cs_groups.xml',
    'views/views_cs_registration_request.xml',
    'views/views_cs_registration_wizard.xml',
    'views/views_cron.xml',
    'views/views_db.xml',
  ],
  # only loaded in demonstration mode
  'demo': [],
}
