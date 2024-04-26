# -*- coding: utf-8 -*-

from odoo import models, fields, api

class certificado(models.Model):
     _name = 'mantenprev.certificado'
     _description = 'mantenprev.certificado'

     code = fields.Char(size = 6, required = True, string = "Código")
     name = fields.Char(required = True, string = "Número de referencia")

     #El titular es un cliente. 
     # Un cliente tiene muchos certificados. cliente [1] : certificados [n]
     cliente_id = fields.Many2one('mantenprev.cliente')
     titular = fields.Char(required = True, related = 'cliente_id.name', string = "Titular")
     
     #titular = fields.Char(required = True, string = "Titular")
     resultado = fields.Selection([('true', 'Positivo'), ('false', 'Negativo')], required = True, default = 'true', string = 'Resultado')
     anyo = fields.Integer(required = True, string = "Año reglamento")

     tipo = fields.Selection([('prev', 'Preventiva'), ('correc', 'Correctiva')], required = True, default = 'prev', string = 'Tipo de inspección')

     # Una empresa de OCA tiene muchos certificados OCA  [1] : certificado [n]
     oca_id = fields.Many2one('mantenprev.oca')
     oca_name = fields.Char(related = 'oca_id.name')



     _sql_constraints = [
          ('code_uniq_certificado', 'unique(code)', 'El código debe ser único'),
          ('name_uniq_certificado', 'unique(name)', 'El nombre debe ser único'),
     ]

