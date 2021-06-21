# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.tools.translate import _

class cs_community(models.Model):
  _name = 'sm_carsharing_structure.cs_community'

  name = fields.Char(string=_("Name"))
  analytic_account_id = fields.Many2one('account.analytic.account',
    string=_("Related analytic account"))
  cs_production_unit_ids = fields.One2many(
    comodel_name ='sm_carsharing_structure.cs_production_unit',
    inverse_name='community_id',
    string=_("CS production units"))
  cs_task_ids = fields.One2many('project.task', 'cs_task_community_id', string=_("Related Tasks"))





