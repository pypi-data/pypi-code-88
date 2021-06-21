# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools.translate import _


class smp_car_config(models.Model):
  _inherit = 'smp.sm_car_config'
  _name = 'smp.sm_car_config'

  cs_carconfig_ids = fields.One2many(comodel_name='sm_carsharing_structure.cs_carconfig',
    inverse_name='db_carconfig_id', string='CS Carconfigs')