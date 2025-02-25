# -*- coding: utf-8 -*-
# from odoo import http


# class VitPoState(http.Controller):
#     @http.route('/vit_po_state/vit_po_state', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_po_state/vit_po_state/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_po_state.listing', {
#             'root': '/vit_po_state/vit_po_state',
#             'objects': http.request.env['vit_po_state.vit_po_state'].search([]),
#         })

#     @http.route('/vit_po_state/vit_po_state/objects/<model("vit_po_state.vit_po_state"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_po_state.object', {
#             'object': obj
#         })
