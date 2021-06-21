from odoo import fields, models


class ContractTerminateUserReason(models.Model):

    _name = 'contract.terminate.user.reason'
    _description = 'Contract Termination User Reason'

    name = fields.Char(required=True)
