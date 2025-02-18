# -*- coding: utf-8 -*-

from odoo import models, fields, api


class vit_send_invoice(models.Model):
    _name = 'account.move'
    _inherit = 'account.move'

    def action_post(self):
        super(vit_send_invoice, self).action_post()

        # Send email after invoice is posted
        self.action_send_email()

        return False
    
    def action_send_email(self):
        template = self.env.ref('vit_send_invoice.email_notif_post')
        template.send_mail(self.id, force_send=True)