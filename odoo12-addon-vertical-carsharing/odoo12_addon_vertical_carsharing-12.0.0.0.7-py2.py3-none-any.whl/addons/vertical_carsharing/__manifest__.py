# -*- coding: utf-8 -*-
{
  'name': "vertical_carsharing",

  'summary': """
    Modules to masnage your carsharing enerprise using TMF reservation app""",

  'author': "Som Mobilitat",
  'website': "https://www.sommobilitat.coop",

  # Categories can be used to filter modules in modules listing
  # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
  # for the full list
  'category': 'vertical-carsharing',
  'version': '12.0.0.0.7',

  # any module necessary for this one to work correctly
  'depends': [
    'base_vat',
    'base',
  ],

  # always loaded
  'data': [
    # 'security/ir.model.access.csv',
    # 'email_tmpl/notification_email.xml',
    'views/views.xml',
    'views/views_members.xml',
  ],
  # only loaded in demonstration mode
  'demo': [
    # 'demo/demo.xml',
  ],
}
