# -*- coding: utf-8 -*-
# from odoo import http


# class TestPartnerInvoice(http.Controller):
#     @http.route('/test_partner_invoice/test_partner_invoice', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_partner_invoice/test_partner_invoice/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_partner_invoice.listing', {
#             'root': '/test_partner_invoice/test_partner_invoice',
#             'objects': http.request.env['test_partner_invoice.test_partner_invoice'].search([]),
#         })

#     @http.route('/test_partner_invoice/test_partner_invoice/objects/<model("test_partner_invoice.test_partner_invoice"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_partner_invoice.object', {
#             'object': obj
#         })
