# -*- coding: utf-8 -*-

from odoo import models, fields, api


class oca(models.Model):
     _name = 'mantenprev.oca'
     _description = 'mantenprev.oca'

     code = fields.Char(size = 6, required = True, string = "Código")
     name = fields.Char(required = True, string = "Nombre")

     # Una empresa de OCA tiene muchos certificados OCA  [1] : certificado [n]
     certificado_id = fields.One2many('mantenprev.certificado','oca_id')


     # Un  mantenimiento concreto es certificado por una empresa OCA,
     # pero una empresa OCA certifica muchos mantenimientos
     # mantenimiento [n] : oca [1]
     mantenimiento_id = fields.One2many('mantenprev.mantenimiento','oca_id')    

     _sql_constraints = [
          ('code_uniq_oca', 'unique(code)', 'El código debe ser único'),
          ('name_uniq_oca', 'unique(name)', 'El nombre debe ser único'),
     ]

