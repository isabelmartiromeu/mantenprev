# -*- coding: utf-8 -*-

from odoo import models, fields, api


class emplazamiento(models.Model):
     _name = 'mantenprev.emplazamiento'
     _description = 'mantenprev.emplazamiento'

     code = fields.Char(size = 6, required = True, string = "Código")
     name = fields.Char(required = True, string = "Nombre")
     ciudad = fields.Char(required = True, string = "Ciudad")
     localizacion = fields.Char(required = True, string = "Localización")

     # Un cliente tiene muchos emplazamientos emplazamiento [N] : [1] cliente

     cliente_id = fields.Many2one('mantenprev.cliente')
     cliente = fields.Char(required = True, related = 'cliente_id.name', string = "Cliente")

     # Un emplazamiento tiene muchas revisiones revisiones [N] : [1] emplazamiento
     revisiones_id = fields.One2many('mantenprev.revisiones','emplazamiento_id', string = "Revisiones")
     
     _sql_constraints = [
          ('code_uniq_emplazamiento', 'unique(code)', 'El código debe ser único'),
          ('name_uniq_emplazamiento', 'unique(name)', 'El nombre debe ser único'),
     ]

