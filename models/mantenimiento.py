# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.addons.base.models.ir_mail_server import MailDeliveryException


class mantenimiento(models.Model):
     _name = 'mantenprev.mantenimiento'
     _description = 'mantenprev.mantenimiento'

     code = fields.Char(size = 6, required = True, string = "Código")
     name = fields.Char(required = True, string = "Descripción")

     # Un mantenimiento concreto es realizado por un equipo de trabajo
     # pero un equipo de trabajo realiza muchos trabajos de mantenimiento
     # manteniento [n] : equipo_trabajo [1]
     equipo_trabajo_id = fields.Many2one('mantenprev.equipo_trabajo', string = "Id equipo")
     #equipo_trabajo_code = fields.Char(related = 'equipo_trabajo_id.code')

     # Un  mantenimiento concreto es certificado por una empresa OCA,
     # pero una empresa OCA certifica muchos mantenimientos
     # mantenimiento [n] : oca [1]
     oca_id = fields.Many2one('mantenprev.oca')
     #oca_name = fields.Char(related = 'oca_id.name')

     # Un mantenimiento concreto tiene un informe asociado
     # un informe en concreto solo es de un mantenimiento concreto
     # mantenimiento [1] : informe [1]
     #--------------------------------------------------------------
     # Parte de mantenimiento [n] : informe [1]
     informe_id = fields.Many2one('mantenprev.informe')
     #informe_name = fields.Char(related = 'informe_id.code')
     
     # Parte de mantenimiento [1] : informe [n]
     su_informe_id = fields.One2many('mantenprev.informe','mi_mantenimiento_id', string = "Informes")   

     # Un mantenimiento concreto es de un emplazamiento
     # pero un emplazamiento puede tener muchos mantenimientos
     # mantenimiento [n] : emplazamiento [1]
     emplazamiento_id = fields.Many2one('mantenprev.emplazamiento')
     #emplazamiento = fields.Char(required = True, related = 'emplazamiento_id.name', string = "Emplazamiento")

     # Un mantenimiento concreto produce una orden de facturación
     # una orden de facturación concreta es producida por un mantenimiento concreto
     # Se comunicará al departamento de facturación.
     # mantenimiento [1] : orden_facturacion [1]
     #--------------------------------------------------------------
     # Parte de mantenimiento [n] : orden_facturacion  [1]
     orden_facturacion_id = fields.Many2one('mantenprev.orden_facturacion')
     # Parte de mantenimiento [1] : orden_facturacion [n]
     orden_facturacion_name = fields.One2many('mantenprev.orden_facturacion','su_orden_facturacion_id', string = "Orden de facturación")   
     
     # Parte de mantenimiento [1] : informe [n]
     su_informe_id = fields.One2many('mantenprev.informe','mi_mantenimiento_id', string = "Informes")   
     _sql_constraints = [
          ('code_uniq_mantenimiento', 'unique(code)', 'El código debe ser único'),
     ]

