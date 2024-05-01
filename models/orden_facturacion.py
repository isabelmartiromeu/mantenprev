from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError
from odoo.addons.base.models.ir_mail_server import MailDeliveryException

class OrdenFacturacion(models.Model):
    _name = 'mantenprev.orden_facturacion'
    _description = 'mantenprev.orden_facturacion'

    code = fields.Char(size=6, required=True, string="Código")
    name = fields.Char(required=True, string="Número de referencia")
    num_horas = fields.Char(size=6, required=True, string="Horas a facturar")
    email_aviso = fields.Char(required=True, string="Email aviso")

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

    def imprimir_informe(self):
        return self.env.ref('mantenprev.orden_facturacion_pdf_report').report_action(self)

    @api.model
    def create(self, vals):
        record = super(OrdenFacturacion, self).create(vals)
        if record.email_aviso:
            try:
                mail = self.env['mail.mail'].create({
                    'email_from': 'isamarrom@alu.edu.gva.es',
                    'email_to': record.email_aviso,
                    'subject': 'Nuevo registro de orden de facturación',
                    'body_html': '<p>Se ha creado una nueva orden de facturación con el número de referencia: %s</p>' % record.name,
                })
                mail.send()
            except MailDeliveryException as e:
                raise UserError("Error al enviar el correo electrónico: %s" % str(e))
            except Exception as e:
                raise UserError("Se produjo un error inesperado al enviar el correo electrónico: %s" % str(e))
        return record

    def write(self, vals):
        res = super(OrdenFacturacion, self).write(vals)
        for record in self:
            if record.email_aviso:
                try:
                    mail = self.env['mail.mail'].create({
                        'email_from': 'isamarrom@alu.edu.gva.es',
                        'email_to': record.email_aviso,
                        'subject': 'Actualización de orden de facturación',
                        'body_html': '<p>La orden de facturación con el número de referencia %s, ha sido actualizada.</p>' % record.name,
                    })
                    mail.send()
                except MailDeliveryException as e:
                    raise UserError("Error al enviar el correo electrónico: %s" % str(e))
                except Exception as e:
                    raise UserError("Se produjo un error inesperado al enviar el correo electrónico: %s" % str(e))
        return res
