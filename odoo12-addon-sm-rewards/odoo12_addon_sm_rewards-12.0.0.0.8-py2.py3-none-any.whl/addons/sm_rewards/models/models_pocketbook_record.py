# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.tools.translate import _

class pocketbook_record_reward(models.Model):
  _name = 'pocketbook.pocketbook_record'
  _inherit = 'pocketbook.pocketbook_record'
  related_reward_id = fields.Many2one('sm_rewards.sm_reward',string=_("Related reward"))
