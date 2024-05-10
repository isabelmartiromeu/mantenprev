from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError
from odoo.addons.base.models.ir_mail_server import MailDeliveryException

class OrdenFacturacion(models.Model):
    _name = 'mantenprev.orden_facturacion'
    _description = 'mantenprev.orden_facturacion'


    name = fields.Char(required=True, string="Número de referencia")
    num_horas = fields.Char(size=6, required=True, string="Horas a facturar")
    email_aviso = fields.Char(required=True, string="Email aviso")

     # Un mantenimiento concreto tiene una orden de facturacion asociada
     # una orden de facturación en concreto solo es de un mantenimiento concreto
     # mantenimiento [1] : orden_facturacion [1]
     #--------------------------------------------------------------
     # Parte de mantenimiento [n] : orden_facturacion [1]
    # mantenimiento_id = fields.One2many('mantenprev.mantenimiento','informe_id', readonly=True)   
     
     # Parte de mantenimiento [1] : orden_facturacion [n]
    su_mantenimiento_id= fields.Many2one('mantenprev.mantenimiento')
    orden_facturacion_name = fields.Char(related = 'su_mantenimiento_id.code')

    # El siguiente campo no puede ser de solo lectura, ya que si no el cron no puede
    # modificar su valor
    pendiente_notificar = fields.Boolean(string="Pendiente de notificar", default=True)

    _sql_constraints = [

        ('name_uniq_orden_facturacion', 'unique(name)', 'El número de referencia debe ser único'),
    ]

    def imprimir_informe(self):
        return self.env.ref('mantenprev.orden_facturacion_pdf_report').report_action(self)

    def realizar_avisos_orden_facturacion(self):
    # Este método envía un email al responsable avisando de que el mantenimiento se ha dado por 
    # finalizado y se puede pasar a realizar una orde de facturación
        peticiones = self.env['mantenprev.orden_facturacion'].search([('pendiente_notificar', '=', True)])
        for peticion in peticiones:
            email_to = peticion.email_responsable
            num_refencia = peticion.name
            if email_to:
                try:
                    mail = self.env['mail.mail'].create({
                        'email_from': 'isamarrom@alu.edu.gva.es',
                        'email_to': email_to,
                        'subject': 'Creación registro de orden de facturación',
                        'body_html': '<p>Mantenimiento finalizado. Se ha creado o modificado una orden de facturación con el número de referencia: %s</p>' % num_refencia
                    })
                    mail.send()
                except MailDeliveryException as e:
                    raise UserError("Error al enviar el correo electrónico: %s" % str(e))
                except Exception as e:
                    raise UserError("Se produjo un error inesperado al enviar el correo electrónico: %s" % str(e))

            # Actualizar el campo pendiente_notificar a False
            peticion.write({'pendiente_notificar': False})