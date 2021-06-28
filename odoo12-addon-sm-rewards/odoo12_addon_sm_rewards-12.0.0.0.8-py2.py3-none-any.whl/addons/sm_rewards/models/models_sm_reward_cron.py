from odoo import models, api

class sm_cron(models.Model):
  _name = 'sm_rewards.reward_cron'

  @api.model
  def complete_rewards(self):
    rewards = self.env['sm_rewards.sm_reward'].search([
      ('final_state', '=', 'not_completed'),
      ('reward_type', '=', 'promocode'),
      ('cron_executed', '=', False)
    ])
    if rewards.exists():
      for reward in rewards:
        reward.write({'cron_executed':True})
        reward.process_reward_from_cron()
