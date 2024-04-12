# -*- coding: utf-8 -*-

from odoo import models, fields, api


class informe(models.Model):
     _name = 'mantenprev.informe'
     _description = 'mantenprev.informe'

     code = fields.Char(size = 6, required = True, string = "Código")
     result = fields.Char(required = True, string = "Resultado")

     observ = fields.Char(required = True, string = "Observaciones")
     solic_correc = fields.Selection([('false', 'No'), ('true', 'Sí')], required = True, default = 'false', string = 'Solicita correción')


     _sql_constraints = [
          ('code_uniq_informe', 'unique(code)', 'El código debe ser único'),
     ]

