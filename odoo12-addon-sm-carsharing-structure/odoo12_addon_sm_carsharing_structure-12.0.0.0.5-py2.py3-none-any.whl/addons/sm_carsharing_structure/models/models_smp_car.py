# -*- coding: utf-8 -*-

from odoo import api, models, fields
from odoo.tools.translate import _


class smp_car(models.Model):
  _inherit = 'smp.sm_car'

  cs_car_ids = fields.One2many('fleet.vehicle', 'db_car_id', string=_('CS Cars'))