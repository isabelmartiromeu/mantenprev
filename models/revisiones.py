# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.addons.base.models.ir_mail_server import MailDeliveryException

class revisiones(models.Model):
     _name = 'mantenprev.revisiones'
     _description = 'mantenprev.revisiones'

     code = fields.Char(size = 6, required = True, string = "Código")

     #nombre_emplazamiento = fields.Char(required = True, string = "Emplazamiento")
     ciudad = fields.Char(required = True, string = "Ciudad")
     #fecha_revision = fields.Char(required = True, string = "Fecha revision")
     fecha_revision = fields.Date(required = True, string = "Fecha revision")
     estado = fields.Selection([('A', 'Activa'), ('P', 'Problemas de pago'), ('R', 'Realizada')], required = True, default = 'false', string = "Estado")


     # Un cliente tiene muchas revisiones revisiones [N] : [1] cliente

     cliente_id = fields.Many2one('mantenprev.cliente')
     name = fields.Char(required = True, related = 'cliente_id.name', string = "Cliente")


     # Un emplazamiento tiene muchas revisiones revisiones [N] : [1] emplazamiento
     # Pero además el emplazamiento pertenece a un cliente concreto.


     emplazamiento_id = fields.Many2one('mantenprev.emplazamiento')
     #emplazamiento = fields.Char(required = True, related = 'emplazamiento_id.name', string = "Emplazamiento")


    # Muestra el nombre del responsable de la empresa del cliente 
     responsable_id = fields.Char(string = "Responsable empresa",readonly=True)
     responsable_email = fields.Char(string = "Email responsable",readonly=True)

     _sql_constraints = [
         ('code_uniq_revisiones', 'unique(code)', 'El código debe ser único'),
     ]

    # Cuando se elige un cliente, solamente se mostrarán los emplazamientos
    # pertenecientes a ese cliente en concreto.
    
     @api.onchange('cliente_id')
     def _onchange_cliente_id(self):
        if self.cliente_id:
            emplazamientos = self.env['mantenprev.emplazamiento'].search([('cliente_id', '=', self.cliente_id.id)])
            return {'domain': {'emplazamiento_id': [('id', 'in', emplazamientos.ids)]}}
        else:
            return {'domain': {'emplazamiento_id': []}}
        
    # Cuando se elige un emplazmiento, se mostrará el responsable de la empresa del cliente

     @api.onchange('emplazamiento_id')
     def _onchange_emplazamiento_id(self):
        if self.emplazamiento_id:
            responsable_emplazamiento = self.emplazamiento_id.responsable_id
            print("Entra en @api.onchange('emplazamiento_id')")
            if responsable_emplazamiento:
                self.responsable_id = responsable_emplazamiento.name
                self.responsable_email = responsable_emplazamiento.email
            else:
                self.responsable_id = False
                self.responsable_email = False



     @api.model
     def create(self, values):
     # Se ejecutará cuando se cree un nuevo registro en el modelo
        # Llama a la creación de registro del modelo base
        new_record = super(revisiones, self).create(values)

        # Obtén el valor del campo responsable_email
        responsable_email = new_record.responsable_email
        f_revision = new_record.fecha_revision

        # Construye el cuerpo del correo electrónico
        body_html = 'Se va a realizar una revisión de mantenimiento el próximo día {f_revision}.'
        if new_record.estado == 'Problemas de pago':
            body_html += f'\nEl estado del emplazamiento se encuentra con: {new_record.estado}, por favor póngase en contacto con nosotros'

        # Envía el correo electrónico
        if responsable_email:
            try:
                self.env['mail.mail'].create({
                    'subject': f'Próxima revisión en {new_record.emplazamiento.id}',
                    'body_html': body_html,
                    'email_to': responsable_email,
                }).send()
            except MailDeliveryException as e:
                raise ValidationError(f"No se pudo enviar el correo electrónico {responsable_email}: {e}")

        return new_record

     def write(self, values):
     # Se ejecutará cuando se actualice un registro del modelo
        # Llama a la escritura del registro 
        result = super(revisiones, self).write(values)

        # Obtén el valor del campo responsable_email
        responsable_email = self.responsable_email
        f_revision = self.fecha_revision

        print("Entra en el método de modificación")

        # Construye el cuerpo del correo electrónico
        body_html = 'Se va a realizar una revisión de mantenimiento el próximo día {f_revision}.'
        if 'estado' in values and values['estado'] == 'Problemas de pago':
            body_html += f'\nEl estado del emplazamiento se encuentra con: {self.estado}, por favor póngase en contacto con nosotros'

        # Envía el correo electrónico
        if responsable_email:
            try:
                self.env['mail.mail'].create({
                    'subject': f'Próxima revisión en {self.emplazamiento.id}',
                    'body_html': body_html,
                    'email_to': responsable_email,
                }).send()
            except MailDeliveryException as e:
                raise ValidationError(f"No se pudo enviar el correo electrónico a {responsable_email}: {e}")

        return result
