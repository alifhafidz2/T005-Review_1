# -*- coding: utf-8 -*-

from odoo import models, fields, api


class invoice(models.Model):
    _name = 'account.move'
    _inherit = 'account.move'

    discount_total = fields.Monetary(string='Discount Total', compute='total_discount')

    @api.depends('invoice_line_ids.quantity', 'invoice_line_ids.price_unit', 'invoice_line_ids.discount')
    def total_discount(self):
        for invoice in self:
            final_discount_amount = 0
            for line in invoice.invoice_line_ids:
                total_price = line.quantity * line.price_unit
                discount_amount = total_price - line.price_subtotal
                final_discount_amount = final_discount_amount + discount_amount
            invoice.discount_total = final_discount_amount

