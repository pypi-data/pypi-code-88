# -*- coding: utf-8 -*-
{
  'name': "sm_carsharing_structure",

  'summary': """
    This module will organice everything that needs to be done in a car and a parking as projects. Also to define account structure for cs service""",

  'author': "Som Mobilitat",
  'website': "https://www.sommobilitat.coop",

  # Categories can be used to filter modules in modules listing
  # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
  # for the full list
  'category': 'carsharing',
  'version': '12.0.0.0.5',

  # any module necessary for this one to work correctly
  'depends': ['base','vertical_carsharing','project','project_category','fleet','sm_partago_db', 'helpdesk_mgmt'],

  # always loaded
  'data': [
    'security/ir.model.access.csv',
    'views/views.xml',
    'views/views_cs_car.xml',
    'views/views_cs_car_service.xml',
    'views/views_cs_carconfig.xml',
    'views/views_db_car_config.xml',
    'views/views_cs_production_unit.xml',
    'views/views_cs_community.xml',
    'views/views_cs_task.xml',
    'views/views_cs_task_wizard.xml',
    'views/views_cs_task_search.xml',
    'views/views_cs_helpdesk_ticket.xml',
    'views/views_cs_task_search.xml',
    'views/views_db_car.xml',
    'views/views_cs_helpdesk_ticket_wizard.xml'
  ],
  # only loaded in demonstration mode
  'demo': [
    #'demo/demo.xml',
  ],
}
