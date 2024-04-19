# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cliente(models.Model):
     _name = 'mantenprev.cliente'
     _description = 'mantenprev.cliente'

     code = fields.Char(size = 6, required = True, string = "Código")
     name = fields.Char(required = True, string = "Nombre")
     CIF_cli = fields.Char(size = 9, required = True, string = "CIF")
     IBAN_cli = fields.Char(size = 24, required = True, string = "IBAN")
     
     # Un cliente tiene muchas revisiones revisiones [N] : [1] cliente
     revisiones_id = fields.One2many('mantenprev.revisiones','cliente_id', string = "Revisiones")

     # Un cliente tiene muchos emplazamientos emplazamiento [N] : [1] cliente
     emplazamientos_id = fields.One2many('mantenprev.emplazamiento','cliente_id', string = "Emplazamientos")


     _sql_constraints = [
          ('code_uniq_cliente', 'unique(code)', 'El código debe ser único'),
          ('name_uniq_cliente', 'unique(name)', 'El nombre debe ser único'),
          ('CIF_cli_uniq_cliente', 'unique(CIF_cli)', 'El CIF debe ser único'),
          ('IBAN_cli_uniq_cliente', 'unique(IBAN_cli)', 'El IBAN debe ser único'),
     ]

