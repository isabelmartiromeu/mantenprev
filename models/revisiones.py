# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta
from odoo.exceptions import ValidationError, UserError
from odoo.addons.base.models.ir_mail_server import MailDeliveryException

class revisiones(models.Model):
     _name = 'mantenprev.revisiones'
     _description = 'mantenprev.revisiones'

     code = fields.Char(size = 6, required = True, string = "Código")

     ciudad = fields.Char(required = True, string = "Ciudad")

     fecha_revision = fields.Date(required = True, string = "Fecha revision")
     estado = fields.Selection([('A', 'Activa'), ('P', 'Problemas de pago'), ('R', 'Realizada')], required = True, default = 'false', string = "Estado")


     # Un cliente tiene muchas revisiones revisiones [N] : [1] cliente

     cliente_id = fields.Many2one('mantenprev.cliente')
     name = fields.Char(required = True, related = 'cliente_id.name', string = "Cliente")


     # Un emplazamiento tiene muchas revisiones revisiones [N] : [1] emplazamiento
     # Pero además el emplazamiento pertenece a un cliente concreto.
     emplazamiento_id = fields.Many2one('mantenprev.emplazamiento')

     # Muestra el nombre del responsable de la empresa del cliente 
     responsable_id = fields.Char(string = "Responsable empresa",readonly=True)
     responsable_email = fields.Char(string = "Email responsable")

     _sql_constraints = [
         ('code_uniq_revisiones', 'unique(code)', 'El código debe ser único'),
     ]

     # El siguiente campo no puede ser de solo lectura, ya que si no el cron no puede
     # modificar su valor
     pendiente_notificar = fields.Boolean(string="Pendiente de notificar", default=False)

     # Definimos un campo calculado para controlar si la fecha de revisión esta dentro de la semana siguiente.
     dentro_de_una_semana = fields.Boolean(compute='_compute_dentro_de_una_semana', string="Dentro de una semana", store=True)



     @api.depends('fecha_revision')
     def _compute_dentro_de_una_semana(self):
        today = fields.Date.today()
        for record in self:
            if record.fecha_revision:
                fecha_revision = fields.Date.from_string(record.fecha_revision)
                una_semana_despues = today + timedelta(days=7)
                record.dentro_de_una_semana = today <= fecha_revision <= una_semana_despues
                # Si la revisión es dentro de una semana, quedará pendiente de notificar. 
                # Se avisará todos los días de la última semana a través del cron.
                if record.dentro_de_una_semana:
                    record.pendiente_notificar = True
                else:
                    record.pendiente_notificar = False
            else:
                record.dentro_de_una_semana = False



    # Cuando se elige un cliente, solamente se mostrarán los emplazamientos
    # pertenecientes a ese cliente en concreto.
    
     @api.onchange('cliente_id')
     def _onchange_cliente_id(self):
        if self.cliente_id:
            emplazamientos = self.env['mantenprev.emplazamiento'].search([('cliente_id', '=', self.cliente_id.id)])
            return {'domain': {'emplazamiento_id': [('id', 'in', emplazamientos.ids)]}}
        else:
            return {'domain': {'emplazamiento_id': []}}
        
     def realizar_avisos_revisiones(self):
     # Este método envía un email al responsable avisando de que las próximas revisiones
        peticiones = self.env['mantenprev.orden_facturacion'].search([('pendiente_notificar', '=', True)])
        for peticion in peticiones:
            email_to = peticion.email_responsable
            # Se avisa si la revisión es dentro de una semana.
            if peticion.dentro_de_una_semana: 
                if email_to:
                    # Construye el cuerpo del correo electrónico dependiendo del estado en el que se encuentra
                    body_html = f'Se va a realizar una revisión de mantenimiento el próximo día {peticion.fecha_revision}.'
                    body_html += f'\nEn el emplazamiento: {peticion.emplazamiento_id}'
                    if peticion.estado == 'Problemas de pago':
                        body_html += f'\nEl estado del emplazamiento se encuentra con: {peticion.estado}, por favor póngase en contacto con nosotros'
                    try:
                        mail = self.env['mail.mail'].create({
                            'email_from': 'isamarrom@alu.edu.gva.es',
                            'email_to': email_to,
                            'subject': 'Aviso próxima revisión',
                            'body_html': body_html
                        })
                        mail.send()
                    except MailDeliveryException as e:
                        raise UserError("Error al enviar el correo electrónico: %s" % str(e))
                    except Exception as e:
                        raise UserError("Se produjo un error inesperado al enviar el correo electrónico: %s" % str(e))

            # Actualizar el campo pendiente_notificar a False
            peticion.write({'pendiente_notificar': False})

