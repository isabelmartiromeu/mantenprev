# -*- coding: utf-8 -*-

from odoo import models, fields, api


class responsable(models.Model):
     _name = 'mantenprev.responsable'
     _description = 'mantenprev.responsable'

     code = fields.Char(size = 6, required = True, string = "Código")
     name = fields.Char(required = True, string = "Nombre")
     movil = fields.Char(required = True, string = "Móvil")
     email = fields.Char(required = True, string = "E-mail")



     _sql_constraints = [
          ('code_uniq_responsable', 'unique(code)', 'El código debe ser único'),
          ('name_uniq_responsable', 'unique(name)', 'El nombre debe ser único'),
     ]

