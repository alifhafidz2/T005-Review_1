# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import base64
import xlwt
from io import BytesIO

class test_partner_card(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    def print_customer_card(self):
        return self.env.ref('test_partner_card.action_report_customer_card').report_action(self)
    
    def export_partner_to_excel(self):
        workbook    = xlwt.Workbook()
        worksheet   = workbook.add_sheet('Partners')

        worksheet.write(0, 0, 'Name')
        worksheet.write(0, 1, self.name or '')

        worksheet.write(0, 3, 'Email')
        worksheet.write(0, 4, self.email or '')

        worksheet.write(1, 0, 'Phone')
        worksheet.write(1, 1, self.phone or '')

        # Data Contacts
        row = 5

        worksheet.write(row, 0, 'Contacts')
        row += 1
        worksheet.write(row, 0, 'Name')
        worksheet.write(row, 1, 'Email')
        worksheet.write(row, 2, 'Phone')
        row += 1
        for contact in self.child_ids:
            worksheet.write(row, 0, contact.name or '')
            worksheet.write(row, 1, contact.email or '')
            worksheet.write(row, 2, contact.phone or '')
            row += 1

        # Data Bank Account
        row += 1
        worksheet.write(row, 0, 'Bank Account')
        row += 1
        worksheet.write(row, 0, 'Name')
        worksheet.write(row, 1, 'Number')
        worksheet.write(row, 2, 'Holder')
        row += 1
        for account in self.bank_account_ids:
            worksheet.write(row, 0, account.bank_id.name or '')
            worksheet.write(row, 1, account.acc_number or '')
            worksheet.write(row, 2, account.partner_id.name or '')
            row += 1

        buffer = BytesIO()
        workbook.save(buffer)

        file_data = base64.b64encode(buffer.getvalue())

        attachment = {
            'name': 'partner_card.xls',
            'datas': file_data,
            'res_model': 'res.partner',
            'res_id': self.id,
            'type': 'binary',
        }
        attachment_id = self.env['ir.attachment'].create(attachment)

        return {
            'type': 'ir.actions.act_url',
            'url': '/web/content/%d?download=true' % attachment_id.id,
            'target': 'self',
        }