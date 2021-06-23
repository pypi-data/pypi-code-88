from odoo import models, fields


class CrmLead(models.Model):
    _inherit = 'crm.lead'
    birth_date = fields.Char(string="Birth Date")
    dni = fields.Char(string="DNI")
    iban = fields.Char(string="IBAN")
    invoice_address = fields.Char(string="Invoice Address")
    language = fields.Selection(
        [('eu_ES', 'EU'), ('es', 'ES')],
        string="Language")
    policy_accepted = fields.Boolean(string="Policy accepted")
    portability_number = fields.Char(string="Portability Number")
