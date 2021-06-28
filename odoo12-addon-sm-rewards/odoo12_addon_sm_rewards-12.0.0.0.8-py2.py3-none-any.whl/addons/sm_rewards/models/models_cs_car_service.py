# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.tools.translate import _

class cs_car_service(models.Model):
  _name = 'fleet.vehicle.log.services'
  _inherit = 'fleet.vehicle.log.services'
  related_reward_id = fields.Many2one('sm_rewards.sm_reward',string=_("Related reward"))
