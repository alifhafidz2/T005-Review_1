# -*- coding: utf-8 -*-
# from odoo import http


# class TestPartnerCard(http.Controller):
#     @http.route('/test_partner_card/test_partner_card', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_partner_card/test_partner_card/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_partner_card.listing', {
#             'root': '/test_partner_card/test_partner_card',
#             'objects': http.request.env['test_partner_card.test_partner_card'].search([]),
#         })

#     @http.route('/test_partner_card/test_partner_card/objects/<model("test_partner_card.test_partner_card"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_partner_card.object', {
#             'object': obj
#         })
