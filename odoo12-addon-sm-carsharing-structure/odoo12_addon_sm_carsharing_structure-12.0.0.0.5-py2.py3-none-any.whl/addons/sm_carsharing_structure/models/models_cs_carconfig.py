# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.tools.translate import _

class cs_carconfig(models.Model):
  _name = 'sm_carsharing_structure.cs_carconfig'

  name = fields.Char(string=_("Name"))

  db_carconfig_id = fields.Many2one('smp.sm_car_config',string=_("DB APP: Carconfig"))
  db_carconfig_name = fields.Char(string=_("Carconfig Name"),compute="_get_db_carconfig_name",store=True)
  analytic_account_id = fields.Many2one('account.analytic.account', string=_("Related analytic account"))
  teletac_analytic_account_id = fields.Many2one('account.analytic.account',string=_("Related teletac analytic account"))
  production_unit_id = fields.Many2one('sm_carsharing_structure.cs_production_unit',string=_("Related production unit"))
  community_id = fields.Many2one('sm_carsharing_structure.cs_community',string=_("Related community"),compute="_get_community_id")
  db_carconfig_group_index = fields.Char(string=_("DB APP: Group"),compute="_get_db_carconfig_group_index",store=True)
  db_carconfig_owner_group_index = fields.Char(string=_("DB APP: Owner Group"),compute="_get_db_carconfig_owner_group_index",store=True)

  @api.depends('db_carconfig_id')
  def _get_db_carconfig_name(self):
    for record in self:
      if record.db_carconfig_id:
        record.db_carconfig_name = record.db_carconfig_id.name

  @api.depends('production_unit_id')
  def _get_community_id(self):
    for record in self:
      if record.production_unit_id:
        record.community_id = record.production_unit_id.community_id

  @api.depends('db_carconfig_id')
  def _get_db_carconfig_owner_group_index(self):
    for record in self:
      if record.db_carconfig_id:
        record.db_carconfig_owner_group_index = record.db_carconfig_id.owner_group_index

  @api.depends('db_carconfig_id')
  def _get_db_carconfig_group_index(self):
    for record in self:
      if record.db_carconfig_id:
        record.db_carconfig_group_index = record.db_carconfig_id.group_index

  # TODO: Finishup this relation and historic!!!!
  # related_current_cs_car = fields.Many2one('sm_carsharing_structure.cs_car',compute="_get_related_current_cs_car",store=False)
  # @api.depends('db_carconfig_id')
  # def _get_related_current_cs_car(self):
  #     for record in self:
  #         if record.db_carconfig_id




