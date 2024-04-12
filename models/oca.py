# -*- coding: utf-8 -*-

from odoo import models, fields, api


class oca(models.Model):
     _name = 'mantenprev.oca'
     _description = 'mantenprev.oca'

     code = fields.Char(size = 6, required = True, string = "Código")
     name = fields.Char(required = True, string = "Nombre")



     _sql_constraints = [
          ('code_uniq_oca', 'unique(code)', 'El código debe ser único'),
          ('name_uniq_oca', 'unique(name)', 'El nombre debe ser único'),
     ]

