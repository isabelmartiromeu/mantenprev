# -*- coding: utf-8 -*-

from odoo import models, fields, api


class mantenimiento(models.Model):
     _name = 'mantenprev.mantenimiento'
     _description = 'mantenprev.mantenimiento'

     code = fields.Char(size = 6, required = True, string = "Código")

     # Un mantenimiento concreto es realizado por un equipo de trabajo
     # pero un equipo de trabajo realiza muchos trabajos de mantenimiento
     # manteniento [n] : equipo_trabajo [1]
     equipo_trabajo_id = fields.Many2one('mantenprev.equipo_trabajo')
     equipo_trabajo_code_equipo = fields.Char(related = 'equipo_trabajo_id.code')

     # Un  mantenimiento concreto es certificado por una empresa OCA,
     # pero una empresa OCA certifica muchos mantenimientos
     # mantenimiento [n] : oca [1]
     oca_id = fields.Many2one('mantenprev.oca')
     oca_name = fields.Char(related = 'oca_id.name')

     # Un mantenimiento concreto tiene un informe asociado
     # un informe en concreto solo es de un mantenimiento concreto
     # mantenimiento [1] : informe [1]
     #--------------------------------------------------------------
     # Parte de mantenimiento [n] : informe [1]
     informe_id = fields.Many2one('mantenprev.informe')
     informe_name = fields.Char(related = 'informe_id.code')
     
     # Parte de mantenimiento [1] : informe [n]
     mi_informe_id = fields.One2many('mantenprev.informe','mi_mantenimiento_id')   
     # Un mantenimiento concreto produce una orden de facturación
     # una orden de facturación concreta es producida por un mantenimiento concreto
     # Esto es una comunicación con el departamento de facturación, no una vista.

     _sql_constraints = [
          ('code_uniq_mantenimiento', 'unique(code)', 'El código debe ser único'),
     ]

