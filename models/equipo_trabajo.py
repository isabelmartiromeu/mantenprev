# -*- coding: utf-8 -*-

from odoo import models, fields, api


class equipo_trabajo(models.Model):
     _name = 'mantenprev.equipo_trabajo'
     _description = 'mantenprev.equipo_trabajo'

     code = fields.Char(size = 6, required = True, string = "Código")
     name = fields.Char(required = True, string = "Nombre")
     ciudad = fields.Char(required = True, string = "Ciudad")

     especialidad = fields.Char(required = True, string = "Especialidad")
     email_responsable = fields.Char(required = True, string = "Email responsable")

     # Un mantenimiento concreto es realizado por un equipo de trabajo
     # pero un equipo de trabajo realiza muchos trabajos de mantenimiento
     # manteniento [n] : equipo_trabajo [1]
     mantenimiento_id = fields.One2many('mantenprev.mantenimiento','equipo_trabajo_id')   



     _sql_constraints = [
          ('code_uniq_equipo_trabajo', 'unique(code)', 'El código debe ser único'),
     ]