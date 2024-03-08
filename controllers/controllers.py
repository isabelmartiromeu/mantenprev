# -*- coding: utf-8 -*-
# from odoo import http


# class Mantenprev(http.Controller):
#     @http.route('/mantenprev/mantenprev/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mantenprev/mantenprev/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mantenprev.listing', {
#             'root': '/mantenprev/mantenprev',
#             'objects': http.request.env['mantenprev.mantenprev'].search([]),
#         })

#     @http.route('/mantenprev/mantenprev/objects/<model("mantenprev.mantenprev"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mantenprev.object', {
#             'object': obj
#         })
