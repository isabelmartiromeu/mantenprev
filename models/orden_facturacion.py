# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.addons.base.models.ir_mail_server import MailDeliveryException

class orden_facturacion(models.Model):
     _name = 'mantenprev.orden_facturacion'
     _description = 'mantenprev.orden_facturacion'

     code = fields.Char(size = 6, required = True, string = "Código")
     name = fields.Char(required = True, string = "Número de referencia")
     num_horas = fields.Char(size = 6, required = True, string = "Horas a facturar")
     email_aviso =  fields.Char(required = True, string = "Email aviso")

     # Un mantenimiento concreto tiene una orden de facturacion asociada
     # una orden de facturación en concreto solo es de un mantenimiento concreto
     # mantenimiento [1] : orden_facturacion [1]
     #--------------------------------------------------------------
     # Parte de mantenimiento [n] : orden_facturacion [1]
     mantenimiento_id = fields.One2many('mantenprev.mantenimiento','informe_id', readonly=True)   
     
     # Parte de mantenimiento [1] : orden_facturacion [n]
     su_orden_facturacion_id= fields.Many2one('mantenprev.mantenimiento')
     orden_facturacion_name = fields.Char(related = 'su_orden_facturacion_id.code')



     _sql_constraints = [
          ('code_uniq_orden_facturacion', 'unique(code)', 'El código debe ser único'),
          ('name_uniq_orden_facturacion', 'unique(name)', 'El número de referencia debe ser único'),
     ]

    
    #  @api.model
    #  def create(self, values):
    #     # Se ejecutará cuando se cree un nuevo registro en el modelo
    #     # Llama a la creación de registro del modelo base
    #     new_record = super(orden_facturacion, self).create(values)

    #     # Obtén el valor del email donde tenemos que mandar el aviso
    #     responsable_email = new_record.email_aviso 
    #     num_referencia = new_record.name

    #     # Construye el cuerpo del correo electrónico
    #     body_html = f'Se requiere una orden de facturación para el informe con el número de referencia: {num_referencia}.'

    #     # Envía el correo electrónico
    #     if responsable_email:
    #         try:
    #             self.env['mail.mail'].create({
    #                 'subject': f'Orden de facturación {num_referencia}',
    #                 'body_html': body_html,
    #                 'email_to': responsable_email,
    #             }).send()
    #         except MailDeliveryException as e:
    #             raise ValidationError(f"No se pudo enviar el correo electrónico {responsable_email}: {e}")

    #     return new_record

    #  def write(self, values):
    #     # Llama a la escritura del registro 
    #     result = super(orden_facturacion, self).write(values)

    #     # Obtén el valor del email donde tenemos que mandar el aviso
    #     responsable_email = self.email_aviso 
    #     num_referencia = self.name

    #     # Construye el cuerpo del correo electrónico
    #     body_html = f'Se requiere una orden de facturación para el informe modificado, con el número de referencia: {num_referencia}.'

    #     # Envía el correo electrónico
    #     if responsable_email:
    #         try:
    #             self.env['mail.mail'].create({
    #                 'subject': f'Orden de facturación {num_referencia}',
    #                 'body_html': body_html,
    #                 'email_to': responsable_email,
    #             }).send()
    #         except MailDeliveryException as e:
    #             raise ValidationError(f"No se pudo enviar el correo electrónico a {responsable_email}: {e}")

    #     return result


     def imprimir_informe(self):
        return self.env.ref('mantenprev.orden_facturacion_pdf_report').report_action(self)