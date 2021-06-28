# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.tools.translate import _

class reward_user(models.Model):
  _inherit = 'res.partner'
  _name = 'res.partner'

  creation_coupon = fields.Char(string=_("Creation coupon"))
  cs_rewards_id = fields.One2many(comodel_name='sm_rewards.sm_reward',
    inverse_name='related_member_id', string='Related Rewards')

reward_user()
