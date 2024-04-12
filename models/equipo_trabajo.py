# -*- coding: utf-8 -*-

from odoo import models, fields, api


class equipo_trabajo(models.Model):
     _name = 'mantenprev.equipo_trabajo'
     _description = 'mantenprev.equipo_trabajo'

     code_equipo = fields.Char(size = 6, required = True, string = "Código")
     ciudad = fields.Char(required = True, string = "Ciudad")

     especialidad = fields.Char(required = True, string = "Especialidad")

     _sql_constraints = [
          ('code_uniq_equipo_trabajo', 'unique(code_equipo)', 'El código debe ser único'),
     ]