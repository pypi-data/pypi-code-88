# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.tools.translate import _

class smp_carsharing_tariff_reward(models.Model):
  _name = 'smp.sm_carsharing_tariff'
  _inherit = 'smp.sm_carsharing_tariff'
  related_reward_id = fields.Many2one('sm_rewards.sm_reward',string=_("Related reward"))
