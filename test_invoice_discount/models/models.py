# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.tools.float_utils import float_is_zero

class invoice(models.Model):
    _inherit = 'account.move.line'

    discount_fixed = fields.Monetary(string='Discount Fixed', default=0.0, currency_field='currency_id', help='Apply a fixed discount on the invoice amount')

    @api.onchange('discount_fixed')
    def _onchange_discount_fixed(self):
        if self.env.context.get('ignore_discount_onchange'):
            return
        
        self.env.context = self.with_context(ignore_discount_onchange=True).env.context
        self.discount = self._get_discount_from_fixed_discount()

    def _get_discount_from_fixed_discount(self):
        self.ensure_one()
        currency = self.currency_id or self.company_id.currency_id
        if float_is_zero(self.discount_fixed, precision_rounding=currency.rounding):
            return 0.0
        return (
            (self.price_unit != 0)
            and ((self.discount_fixed) / self.price_unit) * 100 or 0.00
        )
    
    @api.onchange('discount')
    def _onchange_discount(self):
        if self.env.context.get('ignore_discount_onchange'):
            return
        self.env.context = self.with_context(ignore_discount_onchange=True).env.context
        self.discount_fixed = 0.0