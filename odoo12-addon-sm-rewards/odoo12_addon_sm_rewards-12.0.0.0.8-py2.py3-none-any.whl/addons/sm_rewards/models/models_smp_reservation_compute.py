# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.tools.translate import _

class smp_reservation_compute(models.Model):
  _name = 'smp.sm_reservation_compute'
  _inherit = 'smp.sm_reservation_compute'

  related_reward_ids = fields.One2many(comodel_name='sm_rewards.sm_reward', inverse_name='maintenance_reservation_id', string=_("Related rewards"))
  related_reward_count = fields.Integer(compute='_compute_related_reward_count', type='integer', string="Related Rewards count")

  @api.multi
  def _compute_related_reward_count(self):
      for reservation in self:
        if reservation.related_reward_ids:
          reservation.related_reward_count = len(reservation.related_reward_ids)

  @api.multi
  def rewards_return_action_to_open(self, context):
    """ This opens the xml view specified in xml_id for the current vehicle """
    self.ensure_one()
    xml_id = "view_reward_window"
    if xml_id:
        res = self.env['ir.actions.act_window'].for_xml_id('sm_rewards', xml_id)
        res.update(
            context=dict(self.env.context, group_by=False),
            domain=[('maintenance_reservation_id', '=', self.id)]
        )
        return res
    return False