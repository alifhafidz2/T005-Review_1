from odoo import models, fields, api, _
import time

class test_partner_invoice(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    def action_create_invoice(self):
        product = self.env['product.product'].search([('name', '=', 'Storage Box')])
        for partner in self:
            invoice = self.env['account.move'].create({
                'move_type': 'out_invoice',
                'partner_id': partner.id,
                'invoice_date': time.strftime('%Y-%m-01'),
                'invoice_line_ids': [(0,0,{
                    'name': 'Monthly Subscription',
                    'product_id': product.id,
                    'quantity'  : 1,
                    'price_unit': product.lst_price,
                    'account_id': product.categ_id.property_account_income_categ_id.id,
                })]
            })
            invoice.action_post()