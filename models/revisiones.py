# -*- coding: utf-8 -*-

from odoo import models, fields, api


class revisiones(models.Model):
     _name = 'mantenprev.revisiones'
     _description = 'mantenprev.revisiones'

     code = fields.Char(size = 6, required = True, string = "Código")

     # Un cliente tiene muchas revisiones revisiones [N] : [1] cliente

     cliente_id = fields.Many2one('mantenprev.cliente')
     name = fields.Char(required = True, related = 'cliente_id.name', string = "Cliente")


     # Un emplazamiento tiene muchas revisiones revisiones [N] : [1] emplazamiento
     # Pero además el emplazamiento pertenece a un cliente concreto.


     emplazamiento_id = fields.Many2one('mantenprev.emplazamiento')
     emplazamiento = fields.Char(required = True, related = 'emplazamiento_id.name', string = "Emplazamiento")


     

     #nombre_emplazamiento = fields.Char(required = True, string = "Emplazamiento")
     ciudad = fields.Char(required = True, string = "Ciudad")
     #fecha_revision = fields.Char(required = True, string = "Fecha revision")
     fecha_revision = fields.Date(required = True, string = "Fecha revision")
     estado = fields.Selection([('A', 'Activa'), ('P', 'Problemas de pago'), ('R', 'Realizada')], required = True, default = 'false', string = "Estado")

     _sql_constraints = [
          ('code_uniq_revisiones', 'unique(code)', 'El código debe ser único'),
     ]

