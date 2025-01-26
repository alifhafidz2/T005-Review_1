# -*- coding: utf-8 -*-
# from odoo import http


# class TestKota(http.Controller):
#     @http.route('/test_kota/test_kota', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_kota/test_kota/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_kota.listing', {
#             'root': '/test_kota/test_kota',
#             'objects': http.request.env['test_kota.test_kota'].search([]),
#         })

#     @http.route('/test_kota/test_kota/objects/<model("test_kota.test_kota"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_kota.object', {
#             'object': obj
#         })
