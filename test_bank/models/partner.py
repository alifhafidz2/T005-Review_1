# -*- coding: utf-8 -*-

from odoo import models, fields, api


class partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    bank_account_ids = fields.One2many(comodel_name='res.partner.bank', inverse_name='partner_id', string='Bank Accounts')