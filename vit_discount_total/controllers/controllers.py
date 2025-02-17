# -*- coding: utf-8 -*-
# from odoo import http


# class VitDiscountTotal(http.Controller):
#     @http.route('/vit_discount_total/vit_discount_total', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_discount_total/vit_discount_total/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_discount_total.listing', {
#             'root': '/vit_discount_total/vit_discount_total',
#             'objects': http.request.env['vit_discount_total.vit_discount_total'].search([]),
#         })

#     @http.route('/vit_discount_total/vit_discount_total/objects/<model("vit_discount_total.vit_discount_total"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_discount_total.object', {
#             'object': obj
#         })
