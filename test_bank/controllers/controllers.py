# -*- coding: utf-8 -*-
# from odoo import http


# class TestBank(http.Controller):
#     @http.route('/test_bank/test_bank', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_bank/test_bank/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_bank.listing', {
#             'root': '/test_bank/test_bank',
#             'objects': http.request.env['test_bank.test_bank'].search([]),
#         })

#     @http.route('/test_bank/test_bank/objects/<model("test_bank.test_bank"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_bank.object', {
#             'object': obj
#         })
