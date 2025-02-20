# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMoveInherited(models.Model):
    _inherit = 'account.move'

    @api.model
    def create(self, vals):
        move = super(AccountMoveInherited, self).create(vals)
        if move.move_type == 'out_invoice':
            self._modify_journal_entry(move)

        return move
    
    def _modify_journal_entry(self, move):
        # debit_value = 100000.0
        # credit_value = 100000.0
        # account_debit = self.env['account.account'].search([('code', '=', '91100010')], limit=1)
        # account_credit = self.env['account.account'].search([('code', '=', '11110001')], limit=1)

        # if account_debit and account_credit:
        #     vals_debit = {
        #         'account_id': account_debit.id,
        #         'debit': debit_value,
        #         'credit': 0.0,
        #         'display_type': 'tax',
        #     }
        #     vals_credit = {
        #         'account_id': account_credit.id,
        #         'debit': 0.0,
        #         'credit': credit_value,
        #         'display_type': 'tax',
        #     }
        #     move.write({
        #         'line_ids': [(0, 0, vals_debit), (0, 0, vals_credit)]
        #     })

        # Persentase yang akan digunakan untuk menghitung debit dan kredit
        percentage = 0.05  # 5%

        # Memeriksa apakah move adalah sebuah invoice
        if move.move_type in ('out_invoice', 'out_refund', 'in_invoice', 'in_refund'):  # Sesuaikan dengan tipe invoice yang sesuai
            # Mengakses invoice lines
            invoice_lines = move.invoice_line_ids

            # Menghitung total harga dari semua produk di invoice
            total_price = sum(line.price_unit * line.quantity for line in invoice_lines)

            # Menghitung nilai debit dan kredit berdasarkan persentase dari total harga
            debit_value = total_price * percentage
            credit_value = total_price * percentage

            # Mencari account debit dan credit berdasarkan kode account
            account_debit = self.env['account.account'].search([('code', '=', '91100010')], limit=1)
            account_credit = self.env['account.account'].search([('code', '=', '11110001')], limit=1)

            if account_debit and account_credit:
                vals_debit = {
                    'account_id': account_debit.id,
                    'debit': debit_value,
                    'credit': 0.0,
                    'display_type': 'tax',
                }
                vals_credit = {
                    'account_id': account_credit.id,
                    'debit': 0.0,
                    'credit': credit_value,
                    'display_type': 'tax',
                }
                move.write({
                    'line_ids': [(0, 0, vals_debit), (0, 0, vals_credit)]
                })