# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime, date
import base64
import logging
	

class informe(models.Model):
     _name = 'mantenprev.informe'
     _description = 'mantenprev.informe'
     #_inherit = 'mantenprev.informe'

     #code = fields.Char(size = 6, required = True, string = "Código")
     name = fields.Char(required = True, string = "Descripción")
     result = fields.Selection([('positivo', 'Positivo'), ('negativo', 'Negativo'), ('pendiente', 'Pendiente')], required = True, default = 'positivo', string = 'Resultado')

     observ = fields.Text(required = True, string = "Observaciones")
     solic_correc = fields.Selection([('no', 'No'), ('si', 'Sí')], required = True, default = 'false', string = 'Solicita correción')

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

     def imprimir_informe(self):
	     return self.env.ref('mantenprev.informe_pdf_report').report_action(self)

