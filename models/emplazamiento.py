# -*- coding: utf-8 -*-

from odoo import models, fields, api


class emplazamiento(models.Model):
     _name = 'mantenprev.emplazamiento'
     _description = 'mantenprev.emplazamiento'

     code = fields.Char(size = 6, required = True, string = "Código")
     name = fields.Char(required = True, string = "Nombre")
     ciudad = fields.Char(required = True, string = "Ciudad")
     localizacion = fields.Char(required = True, string = "Localización")



     _sql_constraints = [
          ('code_uniq_emplazamiento', 'unique(code)', 'El código debe ser único'),
          ('name_uniq_emplazamiento', 'unique(name)', 'El nombre debe ser único'),
     ]

