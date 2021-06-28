# -*- coding: utf-8 -*-
{
  'name': "sm_pocketbook",

  'summary': """
    This module is used to have full control over pocketbook actions into the sytem.
  """,

  'author': "Som Mobilitat",
  'website': "http://www.sommobilitat.coop",

  # Categories can be used to filter modules in modules listing
  # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
  # for the full list
  'category': 'vertical-carsharing',
  'version': '12.0.0.0.8',

  # any module necessary for this one to work correctly
  'depends': ['base', 'account','vertical_carsharing','sm_partago_tariffs'],
  # always loaded
  'data': [
    'security/ir.model.access.csv',
    'views/views_members.xml',
    'views/views_pocketbook_record.xml',
    'views/views_pocketbook_record_history.xml'
  ],
  # only loaded in demonstration mode
  # 'demo': [
  #     'demo/demo.xml',
  # ],
}
