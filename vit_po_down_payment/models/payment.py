from odoo import models, fields

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    purchase_id = fields.Many2one(
        comodel_name="purchase.order", 
        string="Purchase",
        readonly=True,
        states={"draft": [("readonly", False)]},
    )

