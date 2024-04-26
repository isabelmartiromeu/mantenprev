# -*- coding: utf-8 -*-

from odoo import models, fields, api


class informe(models.Model):
     _name = 'mantenprev.informe'
     _description = 'mantenprev.informe'

     code = fields.Char(size = 6, required = True, string = "Código")
     result = fields.Selection([('posit', 'Positivo'), ('negat', 'Negativo'), ('pend', 'Pendiente')], required = True, default = 'true', string = 'Resultado')

     observ = fields.Text(required = True, string = "Observaciones")
     solic_correc = fields.Selection([('false', 'No'), ('true', 'Sí')], required = True, default = 'false', string = 'Solicita correción')

     # Un mantenimiento concreto tiene un informe asociado
     # un informe en concreto solo es de un mantenimiento concreto
     # mantenimiento [1] : informe [1]
     #--------------------------------------------------------------
     # Parte de mantenimiento [n] : informe [1]
     mantenimiento_id = fields.One2many('mantenprev.mantenimiento','informe_id')   
     
     # Parte de mantenimiento [1] : informe [n]
     mi_mantenimiento_id = fields.Many2one('mantenprev.mantenimiento')
     mi_mantenimiento_name = fields.Char(related = 'mi_mantenimiento_id.code')

     _sql_constraints = [
          ('code_uniq_informe', 'unique(code)', 'El código debe ser único'),
     ]

