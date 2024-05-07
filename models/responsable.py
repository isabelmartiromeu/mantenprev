# -*- coding: utf-8 -*-

from odoo import models, fields, api


class responsable(models.Model):
     _name = 'mantenprev.responsable'
     _description = 'mantenprev.responsable'

     #code = fields.Char(size = 6, required = True, string = "Código")
     name = fields.Char(required = True, string = "Nombre")
     movil = fields.Char(required = True, string = "Móvil")
     email = fields.Char(required = True, string = "E-mail")

     # Un cliente tiene muchos responsables, que pertenecen a un solo cliente
     # responsalbe [N] : [1] cliente
     cliente_id = fields.Many2one('mantenprev.cliente')
     cliente_name = fields.Char(required = True, related = 'cliente_id.name', string = "Cliente")

     # Un emplezamiento tiene un responsable del cliente, pero un responsable
     # puede llevar varios emplazamientos.
     # responsable [1] : emplazamiento [n]

     emplazamiento_id = fields.One2many('mantenprev.emplazamiento','responsable_id', string = "Emplazamientos")

     _sql_constraints = [
          #('code_uniq_responsable', 'unique(code)', 'El código debe ser único'),
          ('name_uniq_responsable', 'unique(name)', 'El nombre debe ser único'),
     ]

