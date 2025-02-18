# -*- coding: utf-8 -*-
# from odoo import http


# class VitSendInvoice(http.Controller):
#     @http.route('/vit_send_invoice/vit_send_invoice', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_send_invoice/vit_send_invoice/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_send_invoice.listing', {
#             'root': '/vit_send_invoice/vit_send_invoice',
#             'objects': http.request.env['vit_send_invoice.vit_send_invoice'].search([]),
#         })

#     @http.route('/vit_send_invoice/vit_send_invoice/objects/<model("vit_send_invoice.vit_send_invoice"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_send_invoice.object', {
#             'object': obj
#         })
