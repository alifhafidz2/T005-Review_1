# -*- coding: utf-8 -*-
from odoo import models, fields, api

class kota(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    kota_id = fields.Many2one("vit.kota", string="Kota")
