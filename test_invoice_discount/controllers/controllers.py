# -*- coding: utf-8 -*-
# from odoo import http


# class TestInvoiceDiscount(http.Controller):
#     @http.route('/test_invoice_discount/test_invoice_discount', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_invoice_discount/test_invoice_discount/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_invoice_discount.listing', {
#             'root': '/test_invoice_discount/test_invoice_discount',
#             'objects': http.request.env['test_invoice_discount.test_invoice_discount'].search([]),
#         })

#     @http.route('/test_invoice_discount/test_invoice_discount/objects/<model("test_invoice_discount.test_invoice_discount"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_invoice_discount.object', {
#             'object': obj
#         })
