# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.tools.translate import _

class carsharing_registration_request_reward(models.Model):
  _name = 'sm_partago_user.carsharing_registration_request'
  _inherit = 'sm_partago_user.carsharing_registration_request'
  related_reward_id = fields.Many2one('sm_rewards.sm_reward',string=_("Related reward"))
