# -*- coding: utf-8 -*-
# from odoo import http


# class VitInheritJurnal(http.Controller):
#     @http.route('/vit_inherit_jurnal/vit_inherit_jurnal', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_inherit_jurnal/vit_inherit_jurnal/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_inherit_jurnal.listing', {
#             'root': '/vit_inherit_jurnal/vit_inherit_jurnal',
#             'objects': http.request.env['vit_inherit_jurnal.vit_inherit_jurnal'].search([]),
#         })

#     @http.route('/vit_inherit_jurnal/vit_inherit_jurnal/objects/<model("vit_inherit_jurnal.vit_inherit_jurnal"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_inherit_jurnal.object', {
#             'object': obj
#         })
